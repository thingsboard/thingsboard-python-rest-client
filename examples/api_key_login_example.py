#  Copyright 2025. ThingsBoard
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import logging
# Importing models and REST client class from Community Edition version
from tb_rest_client.rest_client_ce import *
from tb_rest_client.rest import ApiException

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# ThingsBoard REST API URL
url = "http://127.0.0.1:8080"

api_key = "YOUR_API_KEY_HERE"


def main():
    # Creating the REST client object with context manager
    with RestClientCE(base_url=url) as rest_client:
        try:
            # Auth with API Key
            rest_client.api_key_login(api_key)

            # Creating a Device
            # Also, you can use default Device Profile:
            # default_device_profile_id = rest_client.get_default_device_profile_info().id
            device_profile = DeviceProfile(name="Thermometer",
                                           type="DEFAULT",
                                           transport_type="DEFAULT",
                                           profile_data=DeviceProfileData(configuration={"type": "DEFAULT"},
                                                                          transport_configuration={"type": "DEFAULT"}))
            device_profile = rest_client.save_device_profile(device_profile)
            device = Device(name="Thermometer 1", label="Thermometer 1",
                            device_profile_id=device_profile.id)
            device = rest_client.save_device(device)

            logging.info(" Device was created:\n%r\n", device)
        except ApiException as e:
            logging.exception(e)


if __name__ == '__main__':
    main()
