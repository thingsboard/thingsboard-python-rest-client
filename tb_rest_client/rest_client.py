from time import time, sleep

from requests import post
from threading import Thread
from logging import getLogger

from tb_rest_client import *

logger = getLogger(__name__)


class RestClient(Thread):
    def __init__(self, base_url):
        super().__init__()
        if base_url.startswith("http"):
            self.__base_url = base_url
        else:
            self.__base_url = "http://" + base_url
        self.__token_info = {"token": "", "refreshToken": 0}
        self.api_client = None
        self.__username = None
        self.__password = None
        self.__stopped = True

    def run(self):
        self.__stopped = False
        while not self.__stopped:
            try:
                check_time = time()
                if check_time >= self.__token_info["refreshToken"]:
                    if self.__username and self.__password:
                        self.login(self.__username, self.__password)
                    else:
                        logger.error("No username or password provided!")
                sleep(1)
            except Exception as e:
                logger.exception(e)
                break
            except KeyboardInterrupt:
                break

    def stop(self):
        self.__stopped = True

    def login(self, username, password):
        """Authorization on the host and saving the toke information"""
        if self.__username is None and self.__password is None:
            self.__username = username
            self.__password = password

        token_json = post(self.__base_url + "/api/auth/login", json={"username": username, "password": password}).json()
        token = None
        if isinstance(token_json, dict) and token_json.get("token") is not None:
            token = token_json["token"]

        configuration = Configuration()
        configuration.host = self.__base_url
        configuration.api_key_prefix["X-Authorization"] = "Bearer"
        configuration.api_key["X-Authorization"] = token

        self.api_client = ApiClient(configuration)
        self.__load_controllers()

    """Admin controller endpoints"""

    def get_admin_settings(self, key):
        return self.admin_controller.get_admin_settings_using_get(key=key)

    def save_admin_settings(self, admin_settings):
        return self.admin_controller.save_admin_settings_using_post(admin_settings)

    def __load_controllers(self):
        self.auth_controller = AuthControllerApi(self.api_client)
        self.admin_controller = AdminControllerApi(self.api_client)
        self.alarm_controller = AlarmControllerApi(self.api_client)
        self.asset_controller = AssetControllerApi(self.api_client)
        self.audit_log_controller = AuditLogControllerApi(self.api_client)
        self.blob_entity_controller = BlobEntityControllerApi(self.api_client)
        self.component_descriptor_controller = ComponentDescriptorControllerApi(self.api_client)
        self.converter_controller = ConverterControllerApi(self.api_client)
        self.custom_menu_controller = CustomMenuControllerApi(self.api_client)
        self.custom_translation_controller = CustomTranslationControllerApi(self.api_client)
        self.customer_controller = CustomerControllerApi(self.api_client)
        self.dashboard_controller = DashboardControllerApi(self.api_client)
        self.device_controller = DeviceControllerApi(self.api_client)
        self.entity_group_controller = EntityGroupControllerApi(self.api_client)
        self.entity_relation_controller = EntityRelationControllerApi(self.api_client)
        self.entity_view_controller = EntityViewControllerApi(self.api_client)
        self.event_controller = EventControllerApi(self.api_client)
        self.group_permission_controller = GroupPermissionControllerApi(self.api_client)
        self.http_integration_controller = HttpIntegrationControllerApi(self.api_client)
        self.integration_controller = IntegrationControllerApi(self.api_client)
        self.ocean_connect_integration_controller = OceanConnectIntegrationControllerApi(self.api_client)
        self.owner_controller = OwnerControllerApi(self.api_client)
        self.queue_controller = QueueControllerApi(self.api_client)
        self.report_controller = ReportControllerApi(self.api_client)
        self.role_controller = RoleControllerApi(self.api_client)
        self.rpc_controller = RpcControllerApi(self.api_client)
        self.rule_chain_controller = RuleChainControllerApi(self.api_client)
        self.rule_engine_controller = RuleEngineControllerApi(self.api_client)
        self.scheduler_event_controller = SchedulerEventControllerApi(self.api_client)
        self.self_registration_controller = SelfRegistrationControllerApi(self.api_client)
        self.sigfox_integration_controller = SigFoxIntegrationControllerApi(self.api_client)
        self.sign_up_controller = SignUpControllerApi(self.api_client)
        self.tmobile_iot_cdp_integration_controller = TMobileIotCdpIntegrationControllerApi(self.api_client)
        self.telemetry_controller = TelemetryControllerApi(self.api_client)
        self.tenant_controller = TenantControllerApi(self.api_client)
        self.thingpark_integration_controller = ThingParkIntegrationControllerApi(self.api_client)
        self.trail_controller = TrailControllerApi(self.api_client)
        self.user_controller = UserControllerApi(self.api_client)
        self.user_permissions_controller = UserPermissionsControllerApi(self.api_client)
        self.white_labeling_controller = WhiteLabelingControllerApi(self.api_client)
        self.widget_type_controller = WidgetTypeControllerApi(self.api_client)
        self.widgets_bundle_controller = WidgetsBundleControllerApi(self.api_client)

if __name__ == '__main__':
    restClient = RestClient("127.0.0.1:8080")
    restClient.start()
    restClient.login("tenant@thingsboard.org", "tenant")
    admin_settings = restClient.get_admin_settings("name")
    restClient.stop()
    logger.error(admin_settings)

