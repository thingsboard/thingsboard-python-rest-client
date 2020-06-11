import logging
from tb_rest_client_pe import RestClient_CE
from tb_rest_client_pe.models import Asset, Device, EntityRelation
from tb_rest_client_pe.rest import ApiException


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

url = "http://localhost:8080"
username = "tenant@thingsboard.org"
password = "tenant"

rest_client = RestClient_CE(base_url=url)
rest_client.login(username=username, password=password)

try:
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
