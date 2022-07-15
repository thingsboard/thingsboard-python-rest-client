import logging
from random import choice
from string import hexdigits
from time import sleep
from typing import Optional

from tb_rest_client.models.models_pe import EntityVersion, EntityTypeVersionCreateConfig, Device, EntityId, \
    ComplexVersionCreateRequest, EntityTypeVersionLoadRequest, EntityTypeVersionLoadConfig
from tb_rest_client.rest import ApiException
from tb_rest_client import RestClientPE

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

try:
    from deepdiff import DeepDiff
    from pprint import pformat
except ImportError:
    logging.error("Please install DeepDiff package using the following command first: \n pip3 install deepdiff")

# ThingsBoard REST API URL
url = "http://localhost:8080"

# Default Tenant Administrator credentials
username = "tenant@thingsboard.org"
password = "tenant"

test_basic_device_name = "Test Device A1"

test_attribute_key = "test_attribute"

available_entity_types_for_save = ['CUSTOMER', 'ASSET', 'RULE_CHAIN', 'DASHBOARD', 'DEVICE_PROFILE', 'DEVICE',
                                   'ENTITY_VIEW', 'WIDGETS_BUNDLE', 'CONVERTER', 'INTEGRATION', 'ROLE', 'USER',
                                   'ENTITY_GROUP']


def check_versions_for_entity(entity_id: EntityId):
    return rest_client.list_entity_versions(entity_id.entity_type, entity_id.id, default_branch['name'], 10, 0)['data']


def get_new_device_name(current_device_name: str):
    if "Extra" in current_device_name:
        new_device_name = current_device_name[:-5]
    else:
        new_device_name = current_device_name + "Extra"
    return new_device_name


def get_latest_test_attribute_value(entity_id: EntityId) -> Optional[int]:
    attribute_keys = rest_client.get_attributes_by_scope(entity_id, "SERVER_SCOPE", test_attribute_key)
    if attribute_keys:
        latest_attribute = attribute_keys[0]["value"]
        logging.info("Latest value: %r", latest_attribute)
        return latest_attribute
    else:
        return None


def update_device(device: Device, rest_client: RestClientPE) -> tuple[Device, int]:
    new_device_name = get_new_device_name(device.name)
    device.name = new_device_name
    latest_test_attribute_value = get_latest_test_attribute_value(device.id)
    if latest_test_attribute_value is not None:
        new_attribute_value = latest_test_attribute_value + 1
        result = rest_client.save_device_attributes(device.id, "SERVER_SCOPE",
                                                    {test_attribute_key: new_attribute_value})
    else:
        new_attribute_value = 0
        result = rest_client.save_device_attributes(device.id, "SERVER_SCOPE", {test_attribute_key: 0})

    logging.info(result)
    logging.info("After save")
    get_latest_test_attribute_value(device.id)

    return rest_client.save_device(device), new_attribute_value


if __name__ == '__main__':
    with RestClientPE(base_url=url) as rest_client:
        try:
            # Auth with credentials
            rest_client.login(username=username, password=password)

            # Get device
            tenant_devices = rest_client.get_tenant_devices(10, 0)
            test_device = next((device for device in tenant_devices.data if
                                device.name in (test_basic_device_name, test_basic_device_name + "Extra")))

            logging.info("Test device name is: %r", test_device.name)

            # VCS functionality testing
            # Get branches
            branches = rest_client.list_branches()
            logging.info("Branches: %r", branches)

            # Get default branch
            default_branch = next((branch for branch in branches if branch["default"]))
            logging.info("Default branch is: %r", default_branch)

            # Get versions for first branch
            versions_page_data = rest_client.list_versions(default_branch["name"], 10, 0)
            versions = versions_page_data['data']
            logging.info("Found versions: %r", versions)

            if versions:
                create_new_versions_count = 2
            else:
                create_new_versions_count = 3

            # Create new versions for tests
            for _ in range(create_new_versions_count):
                updated_device, previous_version_test_attribute = update_device(test_device, rest_client)

                logging.info("Updated device name: %r", updated_device.name)

                # Create version create request for device
                entity_type_version_create_request_config = EntityTypeVersionCreateConfig(True, None, True, True, True,
                                                                                          True, True, "MERGE")
                configs_for_entity_types = {entity_type: entity_type_version_create_request_config for entity_type in
                                            available_entity_types_for_save}
                vcr = ComplexVersionCreateRequest(default_branch['name'], configs_for_entity_types, "MERGE", "COMPLEX",
                                                  "".join(choice(hexdigits) for _ in range(5)))

                version_request_id = rest_client.save_entities_version(vcr)
                logging.info("Version request id: %r", version_request_id)

                # Get the result for request_status
                request_status = rest_client.get_version_create_request_status(version_request_id)
                while not isinstance(request_status, EntityVersion) and not request_status.done:
                    request_status = rest_client.get_version_create_request_status(version_request_id)
                    sleep(1)

                logging.info("Version creation result: %r", request_status)

            list_versions = rest_client.list_versions(default_branch['name'], 10, 0)['data']
            latest_version = list_versions[0]
            previous_version = list_versions[1]
            entities_at_version = rest_client.list_all_entities_at_version(latest_version['id'])
            latest_version_entity_types = set(
                [entity_obj['externalId']['entityType'] for entity_obj in entities_at_version])
            # latest version information
            logging.info(f"Latest version information:\n\
                           Name: {latest_version['name']}\n\
                           Timestamp: {latest_version['timestamp']}\n\
                           Version id: {latest_version['id']}\n\
                           Author: {latest_version['author']}")
            logging.info("Latest version contains following entity types: %r", latest_version_entity_types)

            assert previous_version['name'] != latest_version['name']
            assert previous_version['timestamp'] != latest_version['timestamp']
            assert previous_version['id'] != latest_version['id']

            # Revert previous version

            logging.info("Restoring to version with name: %r", previous_version['name'])

            # Create load version request for previous version

            entities_at_previous_version = rest_client.list_all_entities_at_version(previous_version['id'])
            previous_version_entity_types = set(
                [entity_obj['externalId']['entityType'] for entity_obj in entities_at_previous_version])

            version_load_request_config = EntityTypeVersionLoadConfig(True, True, True, True, True, True, True)
            entity_type_version_load_request_config = {entity_type: version_load_request_config for entity_type in
                                                       previous_version_entity_types}
            previous_version_load_request = EntityTypeVersionLoadRequest(entity_type_version_load_request_config,
                                                                         "ENTITY_TYPE", previous_version['id'])

            load_request_id = rest_client.load_entities_version(previous_version_load_request)

            load_request_status = rest_client.get_version_load_request_status(load_request_id)
            # Wait for restoring and check status
            while not isinstance(load_request_status, EntityVersion) and not load_request_status.done:
                load_request_status = rest_client.get_version_load_request_status(load_request_id)
                sleep(1)

            logging.info("Version load result: %r", load_request_status)

            current_version = previous_version
            previous_version = latest_version

            current_version_test_device_attribute = get_latest_test_attribute_value(test_device.id)

            assert current_version['name'] != latest_version['name']
            assert current_version['timestamp'] != latest_version['timestamp']
            assert current_version['id'] != latest_version['id']
            assert previous_version_test_attribute != current_version_test_device_attribute

            # Such as we changed device to get some difference between versions we will compare current version of the device after reverting with the device version from the latest version:
            tenant_devices = rest_client.get_tenant_devices(10, 0)
            test_device = next((device for device in tenant_devices.data if
                                device.name in (test_basic_device_name, test_basic_device_name + "Extra")))

            logging.info("Device version with name %r was restored, current device name is: %r",
                         current_version['name'], test_device.name)
            logging.info(
                f"Current test attribute value is {current_version_test_device_attribute}, previous version attribute value was {previous_version_test_attribute}")

            # Compare current device version to the latest version

            device_versions_dict = rest_client.compare_entity_data_to_version(test_device.id, latest_version['id'])
            logging.info("Difference between device entities are: \n %s", pformat(
                DeepDiff(device_versions_dict['currentVersion'], device_versions_dict['otherVersion'])[
                    "values_changed"], indent=2))

        except ApiException as e:
            logging.exception(e)
