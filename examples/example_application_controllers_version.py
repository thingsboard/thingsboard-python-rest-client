from requests import post
import tb_rest_client
from tb_rest_client.rest import ApiException
import logging



logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

url = "http://localhost:8080"

username = "tenant@thingsboard.org"
password = "tenant"

token_json = post(url+"/api/auth/login", json={"username": username, "password": password}).json()
token = None
if isinstance(token_json, dict) and token_json.get("token") is not None:
    token = token_json["token"]

configuration = tb_rest_client.Configuration()
configuration.host = url
configuration.api_key_prefix["X-Authorization"] = "Bearer"
configuration.api_key["X-Authorization"] = token

api_client = tb_rest_client.ApiClient(configuration)


asset = None
device = None
relation = None

try:
    asset_controller = tb_rest_client.AssetControllerApi(api_client)
    new_asset = tb_rest_client.Asset(name="Building 1", type="building")
    asset = asset_controller.save_asset_using_post(asset=new_asset)

    logging.info("Asset was created:\n%r\n", asset)
except ApiException as e:
    logging.exception(e)

try:
    device_controller = tb_rest_client.DeviceControllerApi(api_client)
    new_device = tb_rest_client.Device(name="Thermometer 1", type="thermometer")
    device = device_controller.save_device_using_post(new_device)

    logging.info(" Device was created:\n%r\n", device)
except ApiException as e:
    logging.exception(e)

if asset is not None and device is not None:
    try:
        relation_controller = tb_rest_client.EntityRelationControllerApi(api_client)

        relation = tb_rest_client.EntityRelation(_from=asset.id, to=device.id, type="Contains")
        relation_controller.save_relation_using_post(relation)

        logging.info(" Relation was created:\n%r\n", relation)

    except ApiException as e:
        logging.exception(e)
else:
    logging.exception("Cannot create the relation, please check the output.")
