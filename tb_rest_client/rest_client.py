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

    def getToken(self):
        return self.__token_info["token"]

    """Admin controller endpoints"""

    def get_admin_settings(self, key, system_by_default=False):
        return self.admin_controller.get_admin_settings_using_get(key=key, system_by_default=system_by_default)

    def save_admin_settings(self, admin_settings):
        return self.admin_controller.save_admin_settings_using_post(admin_settings)

    def send_test_mail(self, admin_settings):
        return self.admin_controller.send_test_mail_using_post(admin_settings)

    def get_security_settings(self):
        return self.admin_controller.get_security_settings_using_get()

    def save_security_settings(self, security_settings):
        return self.admin_controller.save_security_settings_using_post(security_settings)

    def check_updates(self):
        return self.admin_controller.check_updates_using_get()

    """Alarm controller endpoints"""

    def get_alarm_by_id(self, alarm_id):
        return self.alarm_controller.get_alarm_by_id_using_get(alarm_id)

    def get_alarm_info_by_id(self, alarm_id):
        return self.alarm_controller.get_alarm_info_by_id_using_get(alarm_id)

    def save_alarm(self, alarm_id):
        return self.alarm_controller.save_alarm_using_post(alarm_id)

    def delete_alarm(self, alarm_id):
        return self.alarm_controller.delete_alarm_using_delete(alarm_id)

    def ack_alarm(self, alarm_id):
        return self.alarm_controller.ack_alarm_using_post(alarm_id)

    def clear_alarm(self, alarm_id):
        return self.alarm_controller.clear_alarm_using_post(alarm_id)

    def get_alarms(self, entity_id, page_size=10, page=0, search_status=None, status=None, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None, offset=None, fetch_originator=None):
        return self.alarm_controller.get_alarms_using_get(entity_type=entity_id.type,
                                                          entity_id=entity_id.id,
                                                          page_size=page_size,
                                                          page=page,
                                                          search_status=search_status,
                                                          status=status,
                                                          text_search=text_search,
                                                          sort_property=sort_property,
                                                          sort_order=sort_order,
                                                          start_time=start_time,
                                                          end_time=end_time,
                                                          offset=offset,
                                                          fetch_originator=fetch_originator)

    def get_highest_alarm_severity(self, entity_id, search_status, status):
        return self.alarm_controller.get_highest_alarm_severity_using_get(entity_type=entity_id.type,
                                                                          entity_id=entity_id.id,
                                                                          search_status=search_status,
                                                                          status=status)

    def save_alarm(self, alarm):
        return self.alarm_controller.save_alarm_using_post(alarm)

    """Asset controller endpoints"""
    def get_asset_by_id(self, asset_id):
        return self.asset_controller.get_asset_by_id_using_get(asset_id)

    def save_asset(self, asset):
        return self.asset_controller.save_asset_using_post(asset)

    def delete_asset(self, asset_id):
        return self.asset_controller.delete_asset_using_delete(asset_id)

    def get_tenant_assets(self, type=None, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        return self.asset_controller.get_tenant_assets_using_get(page_size=str(page_size),
                                                                 page=str(page),
                                                                 type=type,
                                                                 text_search=text_search,
                                                                 sort_property=sort_property,
                                                                 sort_order=sort_order)

    def get_tenant_asset(self, asset_name):
        return self.asset_controller.get_tenant_asset_using_get(asset_name)

    def get_customer_assets(self, customer_id, type, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        return self.asset_controller.get_customer_assets_using_get(customer_id=customer_id,
                                                                   page_size=str(page_size),
                                                                   page=str(page),
                                                                   type=type,
                                                                   text_search=text_search,
                                                                   sort_property=sort_property,
                                                                   sort_order=sort_order)

    def get_assets_by_ids(self, asset_ids):
        return self.asset_controller.get_assets_by_ids_using_get(asset_ids)

    def find_by_query(self, query):
        if isinstance(query, AssetSearchQuery):
            return self.asset_controller.find_by_query_using_post(query)
        elif isinstance(query, DeviceSearchQuery):
            return self.device_controller.find_by_query_using_post1(query)
        elif isinstance(query, EntityRelationsQuery):
            return self.entity_relation_controller.find_by_query_using_post2(query)
        elif isinstance(query, EntityViewSearchQuery):
            return self.entity_view_controller.find_by_query_using_post3(query)

    def get_asset_types(self):
        return self.asset_controller.get_asset_types_using_get()

    """Audit Log endpoints"""

    def get_audit_logs_by_customer_id(self, customer_id, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None, action_types=None):
        return self.audit_log_controller.get_audit_logs_by_customer_id_using_get(customer_id=customer_id,
                                                                                 page_size=str(page_size),
                                                                                 page=str(page),
                                                                                 text_search=text_search,
                                                                                 sort_property=sort_property,
                                                                                 sort_order=sort_order,
                                                                                 start_time=start_time,
                                                                                 end_time=end_time,
                                                                                 action_types=action_types)

    def get_audit_logs_by_user_id(self, user_id, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None, action_types=None):
        return self.audit_log_controller.get_audit_logs_by_user_id_using_get(user_id=user_id,
                                                                             page_size=str(page_size),
                                                                             page=str(page),
                                                                             text_search=text_search,
                                                                             sort_property=sort_property,
                                                                             sort_order=sort_order,
                                                                             start_time=start_time,
                                                                             end_time=end_time,
                                                                             action_types=action_types)

    def get_audit_logs_by_entity_id(self, entity_id, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None, action_types=None):
        return self.audit_log_controller.get_audit_logs_by_entity_id_using_get(entity_type=entity_id.type,
                                                                               entity_id=entity_id.id,
                                                                               page_size=str(page_size),
                                                                               page=str(page),
                                                                               text_search=text_search,
                                                                               sort_property=sort_property,
                                                                               sort_order=sort_order,
                                                                               start_time=start_time,
                                                                               end_time=end_time,
                                                                               action_types=action_types)

    def get_audit_logs(self, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None, action_types=None):
        return self.audit_log_controller.get_audit_logs_using_get(page_size=str(page_size),
                                                                  page=str(page),
                                                                  text_search=text_search,
                                                                  sort_property=sort_property,
                                                                  sort_order=sort_order,
                                                                  start_time=start_time,
                                                                  end_time=end_time,
                                                                  action_types=action_types)

    def get_activation_token(self, user_id):
        return self.user_controller.get_user_token_using_get(user_id)

    def get_user(self):
        return self.auth_controller.get_user_using_get()

    def logout(self):
        self.auth_controller.logout_using_post()

    def change_password(self, current_password, new_password):
        change_password_request = '{"currentPassword": "%s","newPassword": "%s"}' % (current_password, new_password)
        self.auth_controller.change_password_using_post(change_password_request)

    def get_user_password_policy(self):
        return self.auth_controller.get_user_password_policy_using_get()

    def check_activation_token(self, user_id):
        activation_token = self.get_activation_token(user_id)
        return self.auth_controller.check_activate_token_using_get(activation_token)

    def request_reset_password_by_email(self, email):
        self.auth_controller.request_reset_password_by_email_using_post('{"email":"%s"}' % email)

    def activate_user(self, user_id, password):
        activation_request = {"activateToken": self.get_activation_token(user_id), "password":password}
        return self.auth_controller.activate_user_using_post(activation_request)

    """Component descriptors endpoints"""

    def get_component(self, component_descriptor_class_name):
        return self.component_descriptor_controller.get_component_descriptor_by_clazz_using_get(component_descriptor_class_name)

    def get_component_descriptors_by_type(self, component_type):
        return self.component_descriptor_controller.get_component_descriptors_by_type_using_get(component_type)

    def get_component_descriptors_by_types(self, component_types):
        return self.component_descriptor_controller.get_component_descriptors_by_types_using_get(component_types)

    """Customers endpoints"""

    def get_customer_by_id(self, customer_id):
        return self.customer_controller.get_customer_by_id_using_get(customer_id)

    def get_short_customer_info_by_id(self, customer_id):
        return self.customer_controller.get_short_customer_info_by_id_using_get(customer_id)

    def get_customer_title_by_id(self, customer_id):
        return self.customer_controller.get_customer_title_by_id_using_get(customer_id)

    def save_customer(self, customer):
        return self.customer_controller.save_customer_using_post(customer)

    def delete_customer(self, customer):
        self.customer_controller.delete_customer_using_delete(customer)

    def get_customers(self, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        return self.customer_controller.get_customers_using_get(page_size=str(page_size),
                                                                page=str(page),
                                                                text_search=text_search,
                                                                sort_property=sort_property,
                                                                sort_order=sort_order)

    def get_tenant_customer(self, customer_title):
        return self.customer_controller.get_tenant_customer_using_get(customer_title)

    """Dashboards endpoints"""

    def get_server_time(self):
        return self.dashboard_controller.get_server_time_using_get()

    def get_max_datapoints_limit(self):
        return self.dashboard_controller.get_max_datapoints_limit_using_get()

    def get_dashboard_info_by_id(self, dashboard_id):
        return self.dashboard_controller.get_dashboard_info_by_id_using_get(dashboard_id)

    def get_dashboard_by_id(self, dashboard_id):
        return self.dashboard_controller.get_dashboard_by_id_using_get(dashboard_id)

    def save_dashboard(self, dashboard):
        return self.dashboard_controller.save_dashboard_using_post(dashboard)

    def delete_dashboard(self, dashboard_id):
        self.dashboard_controller.delete_dashboard_using_delete(dashboard_id)

    def get_tenant_dashboards(self, tenant_id=None, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        if tenant_id is not None:
            return self.dashboard_controller.get_tenant_dashboards_using_get1(tenant_id=tenant_id,
                                                                              page_size=str(page_size),
                                                                              page=str(page),
                                                                              text_search=text_search,
                                                                              sort_property=sort_property,
                                                                              sort_order=sort_order)
        else:
            return self.dashboard_controller.get_tenant_dashboards_using_get(page_size=str(page_size),
                                                                             page=str(page),
                                                                             text_search=text_search,
                                                                             sort_property=sort_property,
                                                                             sort_order=sort_order)

    """Device endpoints"""

    def get_device_by_id(self, deivce_id):
        return self.device_controller.get_device_by_id_using_get(deivce_id)

    def save_device(self, device):
        return self.device_controller.save_device_using_post(device)

    def delete_device(self, device_id):
        return self.device_controller.delete_device_using_delete(device_id)

    def get_device_credentials_by_device_id(self, device_id):
        return self.device_controller.get_device_credentials_by_device_id_using_get(device_id)

    def save_device_credentials(self, device_credentials):
        return self.device_controller.save_device_credentials_using_post(device_credentials)

    def get_tenant_devices(self, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        return self.device_controller.get_tenant_devices_using_get(page_size=str(page_size),
                                                                   page=str(page),
                                                                   text_search=text_search,
                                                                   sort_property=sort_property,
                                                                   sort_order=sort_order)
    def get_tenant_device(self, device_name):
        return self.device_controller.get_tenant_device_using_get(device_name)

    def get_customer_devices(self, customer_id, type=None, page_size=None, page=None, text_search=None, sort_property=None, sort_order=None):
        return self.device_controller.get_customer_devices_using_get(customer_id=customer_id,
                                                                     page_size=str(page_size),
                                                                     page=str(page),
                                                                     type=type,
                                                                     text_search=text_search,
                                                                     sort_property=sort_property,
                                                                     sort_order=sort_order)

    def get_devices_by_ids(self, device_ids):
        self.device_controller.get_devices_by_ids_using_get(device_ids)

    def get_device_types(self):
        return self.device_controller.get_device_types_using_get()

    def claim_device(self, device_name, secret_key, sub_customer_id):
        return self.device_controller.claim_device_using_post(device_name, claim_request='{"secret_key": "%s"}' % secret_key, sub_customer_id=None)

    def reclaim_device(self, device_name):
        self.device_controller.re_claim_device_using_delete(device_name)

    """Relation endpoints"""

    def save_relation(self, relation):
        return self.entity_relation_controller.save_relation_using_post(relation)

    def delete_relation(self, from_id, from_type, relation_type, to_id, to_type, relation_type_group):
        self.entity_relation_controller.delete_relation_using_delete(from_id=from_id,
                                                                     from_type=from_type,
                                                                     relation_type=relation_type,
                                                                     to_id=to_id,
                                                                     to_type=to_type,
                                                                     relation_type_group=relation_type_group)

    def delete_relations(self, entity_id):
        self.entity_relation_controller.delete_relations_using_delete(entity_id=entity_id.id,
                                                                      entity_type=entity_id.type)

    def get_relations(self, from_id, relation_type, to_id, relation_type_group):
        return self.entity_relation_controller.get_relation_using_get(from_id=from_id.id,
                                                                      from_type=from_id.type,
                                                                      relation_type=relation_type,
                                                                      to_id=to_id.id,
                                                                      to_type=to_id.type,
                                                                      relation_type_group=relation_type_group)

    def find_by_from(self, from_id, relation_type_group, relation_type=None):
        if relation_type is not None:
            return self.entity_relation_controller.find_by_from_using_get(from_id=from_id.id,
                                                                          from_type=from_id.type,
                                                                          relation_type=relation_type,
                                                                          relation_type_group=relation_type_group)
        else:
            return self.entity_relation_controller.find_by_from_using_get1(from_id=from_id.id,
                                                                           from_type=from_id.type,
                                                                           relation_type_group=relation_type_group)

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

