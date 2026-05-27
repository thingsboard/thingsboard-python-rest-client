#  Copyright 2026. ThingsBoard
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

import unittest

from tb_rest_client.api.api_ce.device_controller_api import DeviceControllerApi as CEDeviceControllerApi
from tb_rest_client.api.api_pe.device_controller_api import DeviceControllerApi
from tb_rest_client.api.api_pe.self_registration_controller_api import SelfRegistrationControllerApi
from tb_rest_client.rest_client_pe import RestClientPE


class RestClientPEApiKeyLoginTests(unittest.TestCase):

    def test_api_key_login_loads_pe_controllers(self):
        client = RestClientPE("http://localhost:8080")

        client.api_key_login("test-api-key")

        self.assertEqual("ApiKey", client.configuration.api_key_prefix["X-Authorization"])
        self.assertEqual("test-api-key", client.configuration.api_key["X-Authorization"])
        self.assertIsInstance(client.device_controller, DeviceControllerApi)
        self.assertNotIsInstance(client.device_controller, CEDeviceControllerApi)
        self.assertIsInstance(client.self_registration_controller, SelfRegistrationControllerApi)


if __name__ == '__main__':
    unittest.main()
