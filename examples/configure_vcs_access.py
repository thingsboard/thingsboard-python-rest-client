import logging
from argparse import ArgumentParser
from os.path import pathsep

from tb_rest_client.models.models_ce.repository_settings import RepositorySettings
from tb_rest_client.rest import ApiException
from tb_rest_client.rest_client_ce import RestClientCE

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def main(github_password, private_key, private_key_password, user: str, password: str, host: str = "localhost",
         port: int = 80, default_branch: str = "", repository_uri: str = "", github_username: str = ""):
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

            auth_method = "USERNAME_PASSWORD"
            private_key_file_name = None

            if private_key:
                auth_method = "PRIVATE_KEY"
                private_key_file_name = private_key.split(pathsep)[-1]
                with open(private_key, "r") as pkf:
                    private_key = pkf.read()

            repository_settings_config = {
                "auth_method": auth_method,
                "default_branch": default_branch,
                "password": github_password,
                "private_key": private_key,
                "private_key_file_name": private_key_file_name,
                "private_key_password": private_key_password,
                "repository_uri": repository_uri,
                "username": github_username
            }

            repository_settings = RepositorySettings(**repository_settings_config)

            saved_repository_settings = rest_client.save_repository_settings(repository_settings)

            logging.info(f"Saved repository settings: {saved_repository_settings}")

        except ApiException as e:
            logging.exception(e)


if __name__ == '__main__':
    parser = ArgumentParser(description="""
    Using this script you can configure version control system on ThingsBoard.""")
    parser.add_argument("-U", "--user", help="User email to login into ThingsBoard", required=True)
    parser.add_argument("-P", "--password", help="User password to login into ThingsBoard", required=True)

    parser.add_argument("-H", "--host", help="ThingsBoard host", default="localhost")
    parser.add_argument("-p", "--port", help="ThingsBoard port", type=int, default=80)

    parser.add_argument("-b", "--default_branch", help="Default branch on repository", type=str, default="main")
    parser.add_argument("-r", "--repository_uri", help="Repository url", type=str, default="", required=True)
    parser.add_argument("-gu", "--github_username", help="GitHub username", type=str, default="", required=True)
    parser.add_argument("-gp", "--github_password", help="Github password", type=str, default="")
    parser.add_argument("-pk", "--private_key", help="Path to private key", type=str, default="")
    parser.add_argument("-pkp", "--private_key_password", help="Private key password", type=str, default="")

    args = parser.parse_args()
    main(**args.__dict__)
