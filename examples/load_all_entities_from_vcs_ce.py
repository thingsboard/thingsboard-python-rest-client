import logging
from argparse import ArgumentParser
from random import choice
from string import hexdigits
from time import sleep

from tb_rest_client.models.models_ce import EntityVersion, EntityTypeVersionLoadConfig, EntityTypeVersionLoadRequest
from tb_rest_client.rest import ApiException
from tb_rest_client.rest_client_ce import RestClientCE

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def main(user: str, password: str, host: str = "localhost", port: int = 80, branch: str = "main",
         find_existing_entity_by_name: bool = True,
         load_attributes: bool = True, load_credentials: bool = True, load_relations: bool = True,
         remove_other_entities: bool = True,
         version_name=None):
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
                "find_existing_entity_by_name": find_existing_entity_by_name,
                "load_attributes": load_attributes,
                "load_credentials": load_credentials,
                "load_relations": load_relations,
                "remove_other_entities": remove_other_entities
            }

            if not [b for b in rest_client.list_branches() if branch in b['name']]:
                logging.error("Branch not found!")
                exit(1)

            versions = rest_client.list_versions(branch, 1000, 0)
            target_versions = [version for version in versions['data'] if version_name in version['name']]

            target_version = target_versions[0]
            if len(target_versions) > 1:
                logging.warning(f"\nFound more than one version:\n {target_versions}\n")
                target_version_index = -1
                while 0 < target_version_index < len(target_versions):
                    target_version_index = int(input(f"Please choose the version (1..{len(target_versions)})"))
                target_version = target_versions[target_version_index - 1]

            logging.info("Restoring version with name: %r", version_name)
            # Create load version request for previous version

            entities_at_previous_version = rest_client.list_all_entities_at_version(target_version['id'])
            previous_version_entity_types = set(
                [entity_obj['externalId']['entityType'] for entity_obj in entities_at_previous_version])

            version_load_request_config = EntityTypeVersionLoadConfig(**request_config_parameters)
            entity_type_version_load_request_config = {entity_type: version_load_request_config for entity_type in
                                                       previous_version_entity_types}
            previous_version_load_request = EntityTypeVersionLoadRequest(entity_type_version_load_request_config,
                                                                         "ENTITY_TYPE", target_version['id'])

            load_request_id = rest_client.load_entities_version(previous_version_load_request)

            load_request_status = rest_client.get_version_load_request_status(load_request_id)
            # Wait for restoring and check status
            while not isinstance(load_request_status, EntityVersion) and not load_request_status.done:
                load_request_status = rest_client.get_version_load_request_status(load_request_id)
                sleep(1)

            logging.info("Version load result: %r", load_request_status)
        except ApiException as e:
            logging.exception(e)


if __name__ == '__main__':
    parser = ArgumentParser(description="""
    This script creates new version of all available entities and loads it from version control system.""")
    parser.add_argument("-U", "--user", help="User email to login into ThingsBoard", required=True)
    parser.add_argument("-P", "--password", help="User password to login into ThingsBoard", required=True)

    parser.add_argument("-H", "--host", help="ThingsBoard host", default="localhost")
    parser.add_argument("-p", "--port", help="ThingsBoard port", type=int, default=80)

    parser.add_argument("-B", "--branch", help="Branch", default="main")
    parser.add_argument("-N", "--version_name",
                        help="Version name (Commit name), by default 5 symbols string will be generated.")

    parser.add_argument("--find_existing_entity_by_name", help="Find entities by name", type=bool, default=True)
    parser.add_argument("--load_attributes", help="Load attributes for entities", type=bool, default=True)
    parser.add_argument("--load_credentials", help="Load credentials for devices and users", type=bool, default=True)
    parser.add_argument("--load_relations", help="Load relations for entities", type=bool, default=True)
    parser.add_argument("--remove_other_entities", help="Remove existing entity", type=bool, default=False)

    args = parser.parse_args()
    main(**args.__dict__)
