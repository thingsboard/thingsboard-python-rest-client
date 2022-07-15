import logging
from argparse import ArgumentParser
from random import choice
from string import hexdigits
from time import sleep

from tb_rest_client.models.models_ce import EntityVersion, EntityTypeVersionCreateConfig, ComplexVersionCreateRequest
from tb_rest_client.rest import ApiException
from tb_rest_client.rest_client_ce import RestClientCE

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

available_entity_types_for_save = ['CUSTOMER', 'ASSET', 'RULE_CHAIN', 'DASHBOARD', 'DEVICE_PROFILE', 'DEVICE',
                                   'ENTITY_VIEW', 'WIDGETS_BUNDLE', 'USER']


def main(user: str, password: str, host: str = "localhost", port: int = 80, branch: str = "main",
         save_attributes: bool = True, save_credentials: bool = True, save_relations: bool = True,
         sync_strategy: str = "MERGE", version_name=None):

    url = host
    if "https://" not in host:
        if "http://" not in host:
            if port != 443:
                url = "http://" + host + ":" + str(port)
            else:
                url = "https://" + host + ":443"

    with RestClientCE(base_url=url) as rest_client:
        try:
            # Auth with credentials
            logging.info("Logging in...")
            rest_client.login(username=user, password=password)
            logging.info("Logged in.")

            if version_name is None:
                version_name = "".join(choice(hexdigits) for _ in range(5))

            request_config_parameters = {
                "all_entities": True,
                "entity_ids": None,
                "save_attributes": save_attributes,
                "save_credentials": save_credentials,
                "save_relations": save_relations,
                "sync_strategy": sync_strategy.upper()
            }

            # Create version create request for device

            entity_type_version_create_request_config = EntityTypeVersionCreateConfig(**request_config_parameters)
            configs_for_entity_types = {entity_type: entity_type_version_create_request_config for entity_type in
                                        available_entity_types_for_save}
            vcr = ComplexVersionCreateRequest(branch, configs_for_entity_types,
                                              request_config_parameters['sync_strategy'], "COMPLEX",
                                              version_name)

            version_request_id = rest_client.save_entities_version(vcr)
            logging.info("Version creation request id: %r", version_request_id)

            # Get the result for request_status

            request_status = rest_client.get_version_create_request_status(version_request_id)
            while not isinstance(request_status, EntityVersion) and not request_status.done:
                request_status = rest_client.get_version_create_request_status(version_request_id)
                sleep(1)

            logging.info("Version with name %s creation result: \n %r", version_name, request_status)

        except ApiException as e:
            logging.exception(e)


if __name__ == '__main__':
    parser = ArgumentParser(description="""
    This script creates new version of all available entities and saves it to version control system.""")
    parser.add_argument("-U", "--user", help="User email to login into ThingsBoard", required=True)
    parser.add_argument("-P", "--password", help="User password to login into ThingsBoard", required=True)

    parser.add_argument("-H", "--host", help="ThingsBoard host", default="localhost")
    parser.add_argument("-p", "--port", help="ThingsBoard port", type=int, default=80)

    parser.add_argument("-B", "--branch", help="Branch", default="main")
    parser.add_argument("-N", "--version_name",
                        help="Version name (Commit name), by default 5 symbols string will be generated.")

    parser.add_argument("--save_attributes", help="Save attributes for entities", type=bool, default=True)
    parser.add_argument("--save_credentials", help="Save credentials for devices and users", type=bool, default=True)
    parser.add_argument("--save_relations", help="Save relations for entities", type=bool, default=True)
    parser.add_argument("--sync_strategy", help="Sync strategy can be MERGE or OVERWRITE", default="MERGE")

    args = parser.parse_args()
    main(**args.__dict__)
