#      Copyright 2020. ThingsBoard
#  #
#      Licensed under the Apache License, Version 2.0 (the "License");
#      you may not use this file except in compliance with the License.
#      You may obtain a copy of the License at
#  #
#          http://www.apache.org/licenses/LICENSE-2.0
#  #
#      Unless required by applicable law or agreed to in writing, software
#      distributed under the License is distributed on an "AS IS" BASIS,
#      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#      See the License for the specific language governing permissions and
#      limitations under the License.
#

import logging
from tb_rest_client.rest_client_ce import *
from tb_rest_client.rest import ApiException


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

url = "http://localhost:8080"
username = "tenant@thingsboard.org"
password = "tenant"

with RestClientCE(base_url=url) as rest_client:
    try:
        rest_client.login(username=username, password=password)

        asset = Asset(name="Building 1", type="building")
        asset = rest_client.save_asset(asset)

        logging.info("Asset was created:\n%r\n", asset)

        device = Device(name="Thermometer 1", type="thermometer")
        device = rest_client.save_device(device)

        logging.info(" Device was created:\n%r\n", device)

        relation = EntityRelation(_from=asset.id, to=device.id, type="Contains")
        relation = rest_client.save_relation(relation)

        logging.info(" Relation was created:\n%r\n", relation)
    except ApiException as e:
        logging.exception(e)

