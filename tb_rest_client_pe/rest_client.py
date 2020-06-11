from json import dumps
from time import time, sleep

from requests import post
from threading import Thread
from logging import getLogger

from tb_rest_client_pe.api import *
from tb_rest_client_pe.models import *
from tb_rest_client_pe.configuration import Configuration
from tb_rest_client_pe.api_client import ApiClient

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
        self.__logged_in = False
        self.__stopped = True
        self.__configuration = Configuration()
        self.__configuration.host = self.__base_url

    def run(self):
        self.__stopped = False
        while not self.__stopped:
            try:
                check_time = time()
                if check_time >= self.__token_info["refreshToken"] and self.__logged_in:
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
            self.__logged_in = True

        token_json = post(self.__base_url + "/api/auth/login", json={"username": username, "password": password}).json()
        token = None
        if isinstance(token_json, dict) and token_json.get("token") is not None:
            token = token_json["token"]
        self.__configuration.api_key_prefix["X-Authorization"] = "Bearer"
        self.__configuration.api_key["X-Authorization"] = token

        self.api_client = ApiClient(self.__configuration)
        self.__load_controllers()

    def getToken(self):
        return self.__token_info["token"]

    """Admin controller endpoints"""

    def get_admin_settings(self, key, system_by_default=False):
        return self.admin_controller.get_admin_settings_using_get(key=key, system_by_default=system_by_default)

    def save_admin_settings(self, admin_settings: AdminSettings):
        return self.admin_controller.save_admin_settings_using_post(admin_settings)

    def send_test_mail(self, admin_settings: AdminSettings):
        return self.admin_controller.send_test_mail_using_post(admin_settings)

    def get_security_settings(self):
        return self.admin_controller.get_security_settings_using_get()

    def save_security_settings(self, security_settings: SecuritySettings):
        return self.admin_controller.save_security_settings_using_post(security_settings)

    def check_updates(self):
        return self.admin_controller.check_updates_using_get()

    """Alarm controller endpoints"""

    def get_alarm_by_id(self, alarm_id: AlarmId):
        alarm_id = self.get_id(alarm_id)
        return self.alarm_controller.get_alarm_by_id_using_get(alarm_id)

    def get_alarm_info_by_id(self, alarm_id: AlarmId):
        alarm_id = self.get_id(alarm_id)
        return self.alarm_controller.get_alarm_info_by_id_using_get(alarm_id)

    def delete_alarm(self, alarm_id: AlarmId):
        alarm_id = self.get_id(alarm_id)
        return self.alarm_controller.delete_alarm_using_delete(alarm_id)

    def ack_alarm(self, alarm_id: AlarmId):
        alarm_id = self.get_id(alarm_id)
        return self.alarm_controller.ack_alarm_using_post(alarm_id)

    def clear_alarm(self, alarm_id: AlarmId):
        alarm_id = self.get_id(alarm_id)
        return self.alarm_controller.clear_alarm_using_post(alarm_id)

    def get_alarms(self, entity_id: EntityId, page_size=10, page=0, search_status=None, status=None, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None, offset=None, fetch_originator=None):
        return self.alarm_controller.get_alarms_using_get(entity_type=entity_id.entity_type,
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

    def get_highest_alarm_severity(self, entity_id: EntityId, search_status, status):
        return self.alarm_controller.get_highest_alarm_severity_using_get(entity_type=entity_id.entity_type,
                                                                          entity_id=entity_id.id,
                                                                          search_status=search_status,
                                                                          status=status)

    def save_alarm(self, alarm: Alarm):
        return self.alarm_controller.save_alarm_using_post(alarm)

    """Asset controller endpoints"""
    def get_asset_by_id(self, asset_id: AssetId):
        asset_id = self.get_id(asset_id)
        return self.asset_controller.get_asset_by_id_using_get(asset_id)

    def save_asset(self, asset):
        return self.asset_controller.save_asset_using_post(asset)

    def delete_asset(self, asset_id: AssetId):
        asset_id = self.get_id(asset_id)
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

    def get_customer_assets(self, customer_id: CustomerId, type, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
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

    def get_audit_logs_by_customer_id(self, customer_id: CustomerId, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None, action_types=None):
        customer_id = self.get_id(customer_id)
        return self.audit_log_controller.get_audit_logs_by_customer_id_using_get(customer_id=customer_id,
                                                                                 page_size=str(page_size),
                                                                                 page=str(page),
                                                                                 text_search=text_search,
                                                                                 sort_property=sort_property,
                                                                                 sort_order=sort_order,
                                                                                 start_time=start_time,
                                                                                 end_time=end_time,
                                                                                 action_types=action_types)

    def get_audit_logs_by_user_id(self, user_id: UserId, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None, action_types=None):
        user_id = self.get_id(user_id)
        return self.audit_log_controller.get_audit_logs_by_user_id_using_get(user_id=user_id,
                                                                             page_size=str(page_size),
                                                                             page=str(page),
                                                                             text_search=text_search,
                                                                             sort_property=sort_property,
                                                                             sort_order=sort_order,
                                                                             start_time=start_time,
                                                                             end_time=end_time,
                                                                             action_types=action_types)

    def get_audit_logs_by_entity_id(self, entity_id: EntityId, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None, action_types=None):
        return self.audit_log_controller.get_audit_logs_by_entity_id_using_get(entity_type=entity_id.entity_type,
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

    def get_activation_token(self, user_id: UserId):
        user_id = self.get_id(user_id)
        return self.user_controller.get_activation_token_using_get(user_id)

    def get_user(self):
        return self.auth_controller.get_user_using_get()

    def logout(self):
        self.auth_controller.logout_using_post()

    def change_password(self, current_password, new_password):
        change_password_request = '{"currentPassword": "%s","newPassword": "%s"}' % (current_password, new_password)
        self.auth_controller.change_password_using_post(change_password_request)

    def get_user_password_policy(self):
        return self.auth_controller.get_user_password_policy_using_get()

    def check_activation_token(self, user_id: UserId):
        activation_token = self.get_activation_token(user_id)
        return self.auth_controller.check_activate_token_using_get(activation_token)

    def request_reset_password_by_email(self, email: str):
        self.auth_controller.request_reset_password_by_email_using_post('{"email":"%s"}' % email)

    def activate_user(self, user_id: UserId, password):
        user_id = self.get_id(user_id)
        activation_request = {"activateToken": self.get_activation_token(user_id).replace("'", '"'), "password":password}
        return self.auth_controller.activate_user_using_post(activation_request)

    """Component descriptors endpoints"""

    def get_component(self, component_descriptor_class_name):
        return self.component_descriptor_controller.get_component_descriptor_by_clazz_using_get(component_descriptor_class_name)

    def get_component_descriptors_by_type(self, component_type):
        return self.component_descriptor_controller.get_component_descriptors_by_type_using_get(component_type)

    def get_component_descriptors_by_types(self, component_types):
        return self.component_descriptor_controller.get_component_descriptors_by_types_using_get(component_types)

    """Customers endpoints"""

    def get_customer_by_id(self, customer_id: CustomerId):
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_customer_by_id_using_get(customer_id)

    def get_short_customer_info_by_id(self, customer_id: CustomerId):
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_short_customer_info_by_id_using_get(customer_id)

    def get_customer_title_by_id(self, customer_id: CustomerId):
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_customer_title_by_id_using_get(customer_id)

    def save_customer(self, customer: Customer):
        return self.customer_controller.save_customer_using_post(customer)

    def delete_customer(self, customer_id: CustomerId):
        customer_id = self.get_id(customer_id)
        self.customer_controller.delete_customer_using_delete(customer_id=customer_id)

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

    def get_dashboard_info_by_id(self, dashboard_id: DashboardId):
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.get_dashboard_info_by_id_using_get(dashboard_id)

    def get_dashboard_by_id(self, dashboard_id: DashboardId):
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.get_dashboard_by_id_using_get(dashboard_id)

    def save_dashboard(self, dashboard: Dashboard):
        return self.dashboard_controller.save_dashboard_using_post(dashboard)

    def delete_dashboard(self, dashboard_id: DashboardId):
        dashboard_id = self.get_id(dashboard_id)
        self.dashboard_controller.delete_dashboard_using_delete(dashboard_id)

    def get_tenant_dashboards(self, tenant_id=None, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        if tenant_id is not None:
            tenant_id = self.get_id(tenant_id)
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

    def get_user_dashboards(self, user_id: UserId, operation, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        user_id = self.get_id(user_id)
        return self.dashboard_controller.get_user_dashboards_using_get(page_size=str(page_size),
                                                                       page=str(page),
                                                                       text_search=text_search,
                                                                       sort_property=sort_property,
                                                                       sort_order=sort_order,
                                                                       operation=operation,
                                                                       user_id=user_id)

    def get_group_dashboards(self, entity_group_id: EntityGroupId, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        entity_group_id = self.get_id(entity_group_id)
        return self.dashboard_controller.get_group_dashboards_using_get(entity_group_id=entity_group_id,
                                                                        page_size=str(page_size),
                                                                        page=str(page),
                                                                        text_search=text_search,
                                                                        sort_property=sort_property,
                                                                        sort_order=sort_order)

    def get_dasboards_by_ids(self, dashboards_ids):
        if isinstance(dashboards_ids, list):
            dashboards_ids = ",".join(dashboards_ids)
        return self.dashboard_controller.get_dashboards_by_ids_using_get(dashboard_ids=dashboards_ids)

    """Device endpoints"""

    def get_device_by_id(self, device_id: DeviceId):
        device_id = self.get_id(device_id)
        return self.device_controller.get_device_by_id_using_get(device_id)

    def save_device(self, device: Device):
        return self.device_controller.save_device_using_post(device)

    def delete_device(self, device_id: DeviceId):
        device_id = self.get_id(device_id)
        return self.device_controller.delete_device_using_delete(device_id)

    def get_device_credentials_by_device_id(self, device_id: DeviceId):
        device_id = self.get_id(device_id)
        return self.device_controller.get_device_credentials_by_device_id_using_get(device_id)

    def save_device_credentials(self, device_credentials: DeviceCredentials):
        return self.device_controller.save_device_credentials_using_post(device_credentials)

    def get_tenant_devices(self, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        return self.device_controller.get_tenant_devices_using_get(page_size=str(page_size),
                                                                   page=str(page),
                                                                   text_search=text_search,
                                                                   sort_property=sort_property,
                                                                   sort_order=sort_order)
    
    def get_tenant_device(self, device_name):
        return self.device_controller.get_tenant_device_using_get(device_name)

    def get_customer_devices(self, customer_id: CustomerId, type=None, page_size=None, page=None, text_search=None, sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
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
        sub_customer_id = self.get_id(sub_customer_id)
        return self.device_controller.claim_device_using_post(device_name, claim_request='{"secret_key": "%s"}' % (secret_key,), sub_customer_id=sub_customer_id)

    def reclaim_device(self, device_name):
        self.device_controller.re_claim_device_using_delete(device_name)

    def get_user_devices(self, device_type, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        return self.device_controller.get_user_devices_using_get(type=device_type,
                                                                 page_size=str(page_size),
                                                                 page=str(page),
                                                                 text_search=text_search,
                                                                 sort_property=sort_property,
                                                                 sort_order=sort_order)

    """Relation endpoints"""

    def save_relation(self, relation: EntityRelation):
        return self.entity_relation_controller.save_relation_using_post(relation)

    def delete_relation(self, from_id, relation_type, to_id, relation_type_group):
        self.entity_relation_controller.delete_relation_using_delete(from_id=from_id.id,
                                                                     from_type=from_id.entity_type,
                                                                     relation_type=relation_type,
                                                                     to_id=to_id.id,
                                                                     to_type=to_id.entity_type,
                                                                     relation_type_group=relation_type_group)

    def delete_relations(self, entity_id: EntityId):
        self.entity_relation_controller.delete_relations_using_delete(entity_id=entity_id.id,
                                                                      entity_type=entity_id.entity_type)

    def get_relations(self, from_id, relation_type, to_id, relation_type_group):
        return self.entity_relation_controller.get_relation_using_get(from_id=from_id.id,
                                                                      from_type=from_id.entity_type,
                                                                      relation_type=relation_type,
                                                                      to_id=to_id.id,
                                                                      to_type=to_id.entity_type,
                                                                      relation_type_group=relation_type_group)

    def find_by_from(self, from_id, relation_type_group, relation_type=None):
        if relation_type is not None:
            return self.entity_relation_controller.find_by_from_using_get(from_id=from_id.id,
                                                                          from_type=from_id.entity_type,
                                                                          relation_type=relation_type,
                                                                          relation_type_group=relation_type_group)
        else:
            return self.entity_relation_controller.find_by_from_using_get1(from_id=from_id.id,
                                                                           from_type=from_id.entity_type,
                                                                           relation_type_group=relation_type_group)

    def find_info_by_from(self, from_id, relation_type_group):
        return self.entity_relation_controller.find_info_by_from_using_get(from_id=from_id.id,
                                                                           from_type=from_id.entity_type,
                                                                           relation_type_group=relation_type_group)

    def find_by_to(self, to_id, relation_type_group, relation_type=None):
        if relation_type is not None:
            return self.entity_relation_controller.find_by_to_using_get(to_id=to_id.id,
                                                                        to_type=to_id.entity_type,
                                                                        relation_type=relation_type,
                                                                        relation_type_group=relation_type_group)
        else:
            return self.entity_relation_controller.find_by_to_using_get1(to_id=to_id.id,
                                                                         to_type=to_id.entity_type,
                                                                         relation_type_group=relation_type_group)

    def find_info_by_to(self, to_id, relation_type_group):
        return self.entity_relation_controller.find_info_by_to_using_get(to_id=to_id.id,
                                                                         to_type=to_id.entity_type,
                                                                         relation_type_group=relation_type_group)

    def find_info_by_query(self, query):
        return self.entity_relation_controller.find_info_by_query_using_post(query=query)

    """Entity view endpoints"""

    def get_entity_view_by_id(self, entity_view_id: EntityViewId):
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.get_entity_view_by_id_using_get(entity_view_id=entity_view_id)

    def save_entity_view(self, entity_view: EntityView):
        return self.entity_view_controller.save_entity_view_using_post(entity_view=entity_view)

    def delete_entity_view(self, entity_view_id: EntityViewId):
        entity_view_id = self.get_id(entity_view_id)
        self.entity_view_controller.delete_entity_view_using_delete(entity_view_id=entity_view_id)

    def get_tenant_entity_view(self, entity_view_name):
        return self.entity_view_controller.get_tenant_entity_view_using_get(entity_view_name=entity_view_name)

    def get_customer_entity_views(self, customer_id: CustomerId, type=None, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
        return self.entity_view_controller.get_customer_entity_views_using_get(customer_id=customer_id,
                                                                               page_size=str(page_size),
                                                                               page=str(page),
                                                                               type=type,
                                                                               text_search=text_search,
                                                                               sort_property=sort_property,
                                                                               sort_order=sort_order)

    def get_tenant_entity_views(self, page_size=10, page=0, type=None, text_search=None, sort_property=None, sort_order=None):
        return self.entity_view_controller.get_tenant_entity_views_using_get(page_size=str(page_size),
                                                                             page=str(page),
                                                                             type=type,
                                                                             text_search=text_search,
                                                                             sort_property=sort_property,
                                                                             sort_order=sort_order)

    def get_user_entity_views(self, entity_view_type, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        entity_view_type = self.get_type(entity_view_type)
        return self.entity_view_controller.get_user_entity_views_using_get(type=entity_view_type,
                                                                           page_size=str(page_size),
                                                                           page=str(page),
                                                                           text_search=text_search,
                                                                           sort_property=sort_property,
                                                                           sort_order=sort_order)

    def get_entity_views_by_ids(self, entity_view_ids):
        return self.entity_view_controller.get_entity_views_by_ids_using_get(entity_view_ids=entity_view_ids)

    def get_entity_view_types(self):
        return self.entity_view_controller.get_entity_view_types_using_get()

    """ Events endpoints """

    def get_events(self, entity_id: EntityId, tenant_id, event_type=None, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None):
        if event_type is not None:
            return self.event_controller.get_events_using_get(entity_type=entity_id.entity_type,
                                                              entity_id=entity_id.id,
                                                              event_type=event_type,
                                                              tenant_id=tenant_id.id,
                                                              page_size=page_size,
                                                              page=page,
                                                              text_search=text_search,
                                                              sort_property=sort_property,
                                                              sort_order=sort_order,
                                                              start_time=start_time,
                                                              end_time=end_time)
        else:
            return self.event_controller.get_events_using_get1(entity_type=entity_id.entity_type,
                                                               entity_id=entity_id.id,
                                                               tenant_id=tenant_id.id,
                                                               page_size=page_size,
                                                               page=page,
                                                               text_search=text_search,
                                                               sort_property=sort_property,
                                                               sort_order=sort_order,
                                                               start_time=start_time,
                                                               end_time=end_time)

    """RPC endpoints"""

    def handle_one_way_device_rpc_request(self, device_id: DeviceId, request_body):
        device_id = self.get_id(device_id)
        self.rpc_controller.handle_one_way_device_rpc_request_using_post(device_id=device_id.id, request_body=request_body)

    def handle_two_way_device_rpc_request(self, device_id: DeviceId, request_body):
        device_id = self.get_id(device_id)
        return self.rpc_controller.handle_two_way_device_rpc_request_using_post(device_id=device_id, request_body=request_body)

    """Rule chain endpoints"""

    def get_rule_chain_by_id(self, rule_chain_id: RuleChainId):
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.get_rule_chain_by_id_using_get(rule_chain_id=rule_chain_id)

    def get_rule_chain_meta_data(self, rule_chain_id: RuleChainId):
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.get_rule_chain_meta_data_using_get(rule_chain_id=rule_chain_id)

    def save_rule_chain(self, rule_chain: RuleChain):
        return self.rule_chain_controller.save_rule_chain_using_post(rule_chain=rule_chain)

    def set_root_rule_chain(self, rule_chain_id: RuleChainId):
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.set_root_rule_chain_using_post(rule_chain_id=rule_chain_id)

    def save_rule_chain_meta_data(self, rule_chain_meta_data: RuleChainMetaData):
        return self.rule_chain_controller.save_rule_chain_meta_data_using_post(rule_chain_meta_data=rule_chain_meta_data)

    def get_rule_chains(self, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        return self.rule_chain_controller.get_rule_chains_using_get(page_size=str(page_size),
                                                                    page=str(page),
                                                                    text_search=text_search,
                                                                    sort_property=sort_property,
                                                                    sort_order=sort_order)

    def delete_rule_chain(self, rule_chain_id: RuleChainId):
        rule_chain_id = self.get_id(rule_chain_id)
        self.rule_chain_controller.delete_rule_chain_using_delete(rule_chain_id)

    def get_latest_rule_node_debug_input(self, rule_node_id: RuleNodeId):
        rule_node_id = self.get_id(rule_node_id)
        return self.rule_chain_controller.get_latest_rule_node_debug_input_using_get(rule_node_id)

    def test_script(self, input_params):
        if isinstance(input_params, dict):
            input_params = dumps(input_params)
        self.rule_chain_controller.test_script_using_post(input_params=input_params)

    """Telemetry endpoints"""

    def get_attribute_keys(self, entity_id: EntityId):
        return self.telemetry_controller.get_attribute_keys_using_get(entity_type=entity_id.entity_type, entity_id=entity_id.id)

    def get_attribute_keys_by_scope(self, entity_id: EntityId, scope):
        return self.telemetry_controller.get_attribute_keys_by_scope_using_get(entity_type=entity_id.entity_type, entity_id=entity_id.id, scope=scope)

    def get_attributes_by_scope(self, entity_id: EntityId, scope, keys=None):
        return self.telemetry_controller.get_attributes_by_scope_using_get(entity_id=entity_id.id, entity_type=entity_id.entity_type, scope=scope, keys=keys)

    def get_timeseries_keys(self, entity_id: EntityId):
        return self.telemetry_controller.get_timeseries_keys_using_get(entity_type=entity_id.entity_type, entity_id=entity_id.id)

    def get_latest_timeseries(self, entity_id: EntityId, keys=None):
        if isinstance(keys, list):
            keys = ",".join(keys)
        return self.telemetry_controller.get_latest_timeseries_using_get(entity_type=entity_id.entity_type, entity_id=entity_id.id, keys=keys)

    def get_timeseries(self, entity_id: EntityId, keys, interval=0, aggregation="NONE", use_strict_data_types=None, start_ts=None, end_ts=None, limit=100):
        if use_strict_data_types is not None:
            return self.telemetry_controller.get_timeseries_using_get(entity_type=entity_id.entity_type,
                                                                      entity_id=entity_id.id,
                                                                      keys=keys,
                                                                      start_ts=start_ts,
                                                                      end_ts=end_ts,
                                                                      interval=interval,
                                                                      limit=limit,
                                                                      agg=aggregation,
                                                                      use_strict_data_types=use_strict_data_types)

    def save_device_attributes(self, device_id, scope, request):
        device_id = self.get_id(device_id)
        return self.telemetry_controller.save_device_attributes_using_post(device_id=device_id, scope=scope, request=request)

    def save_entity_attributes_v1(self, entity_id: EntityId, scope, request):
        return self.telemetry_controller.save_entity_attributes_v1_using_post(entity_type=entity_id.entity_type, entity_id=entity_id.id, scope=scope, request=request)

    def save_entity_attributes_v2(self, entity_id: EntityId, scope, request):
        return self.telemetry_controller.save_entity_attributes_v2_using_post(entity_type=entity_id.entity_type, entity_id=entity_id.id, scope=scope, request=request)

    def save_entity_telemetry(self, entity_id: EntityId, scope, request):
        return self.telemetry_controller.save_entity_telemetry_using_post(entity_type=entity_id.entity_type, entity_id=entity_id.id, scope=scope, request_body=request)

    def save_entity_telemetry_with_ttl(self, entity_id: EntityId, scope, ttl, request):
        return self.telemetry_controller.save_entity_telemetry_with_ttl_using_post(entity_type=entity_id.entity_type, entity_id=entity_id.id, scope=scope, ttl=ttl, request_body=request)

    def delete_entity_timeseries(self, entity_id: EntityId, keys, delete_all_data_for_keys, start_ts, end_ts, rewrite_latest_if_deleted):
        return self.telemetry_controller.delete_entity_timeseries_using_delete(entity_type=entity_id.entity_type,
                                                                               entity_id=entity_id.id,
                                                                               keys=keys,
                                                                               delete_all_data_for_keys=delete_all_data_for_keys,
                                                                               start_ts=start_ts,
                                                                               end_ts=end_ts,
                                                                               rewrite_latest_if_deleted=rewrite_latest_if_deleted)

    def delete_entity_attributes(self, id, scope, keys):
        if isinstance(keys, list):
            keys = ",".join(keys)
        if isinstance(id, DeviceId):
            return self.telemetry_controller.delete_entity_attributes_using_delete(id.id, scope, keys)
        elif isinstance(id, EntityId):
            return self.telemetry_controller.delete_entity_attributes_using_delete1(entity_type=id.entity_type,
                                                                                    entity_id=id.id,
                                                                                    scope=scope,
                                                                                    keys=keys)

    """ Tenant endpoints. """

    def get_tenant_by_id(self, tenant_id: TenantId):
        tenant_id = self.get_id(tenant_id)
        return self.tenant_controller.get_tenant_by_id_using_get(tenant_id=tenant_id)

    def save_tenant(self, tenant: Tenant):
        return self.tenant_controller.save_tenant_using_post(tenant=tenant)

    def delete_tenant(self, tenant_id: TenantId):
        tenant_id = self.get_id(tenant_id)
        self.tenant_controller.delete_tenant_using_delete(tenant_id=tenant_id)

    def get_tenants(self, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        return self.tenant_controller.get_tenants_using_get(page_size=str(page_size),
                                                            page=str(page),
                                                            text_search=text_search,
                                                            sort_property=sort_property,
                                                            sort_order=sort_order)

    def get_tenant_admins(self, tenant_id: TenantId, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        tenant_id = self.get_id(tenant_id)
        return self.user_controller.get_tenant_admins_using_get(tenant_id=tenant_id,
                                                                page_size=str(page_size),
                                                                page=str(page),
                                                                text_search=text_search,
                                                                sort_property=sort_property,
                                                                sort_order=sort_order)

    def get_tenants_by_ids(self, tenant_ids):
        return self.tenant_controller.get_tenants_by_ids_using_get(tenant_ids=tenant_ids)

    """ User endpoints. """

    def get_user_by_id(self, user_id: UserId):
        user_id = self.get_id(user_id)
        return self.user_controller.get_user_by_id_using_get(user_id=user_id)

    def is_user_token_access_enabled(self):
        return self.user_controller.is_user_token_access_enabled_using_get()

    def get_user_token(self, user_id: UserId):
        user_id = self.get_id(user_id)
        return self.user_controller.get_user_token_using_get(user_id=user_id)

    def save_user(self, user: User, send_activation_mail, entity_group_id=None):
        return self.user_controller.save_user_using_post(user=user, send_activation_mail=send_activation_mail, entity_group_id=entity_group_id)

    def send_activation_email(self, email):
        self.user_controller.send_activation_email_using_post(email=email)

    def get_activation_link(self, user_id: UserId):
        user_id = self.get_id(user_id)
        return self.user_controller.get_activation_link_using_get(user_id=user_id)

    def delete_user(self, user_id: UserId):
        user_id = self.get_id(user_id)
        self.user_controller.delete_user_using_delete(user_id=user_id)

    def get_customer_users(self, customer_id: CustomerId, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
        return self.user_controller.get_customer_users_using_get(customer_id=customer_id,
                                                                 page_size=str(page_size),
                                                                 page=str(page),
                                                                 text_search=text_search,
                                                                 sort_property=sort_property,
                                                                 sort_order=sort_order)

    def set_user_credentials_enabled(self, user_id: UserId, user_credentials_enabled):
        user_id = self.get_id(user_id)
        return self.user_controller.set_user_credentials_enabled_using_post(user_id=user_id, user_credentials_enabled=user_credentials_enabled)

    def get_all_customer_users(self, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        return self.user_controller.get_all_customer_users_using_get(page_size=str(page_size),
                                                                     page=str(page),
                                                                     text_search=text_search,
                                                                     sort_property=sort_property,
                                                                     sort_order=sort_order)

    def get_user_users(self, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        return self.user_controller.get_user_users_using_get(page_size=page_size,
                                                             page=page,
                                                             text_search=text_search,
                                                             sort_property=sort_property,
                                                             sort_order=sort_order)

    def get_users_by_ids(self, user_ids):
        return self.user_controller.get_users_by_ids_using_get(user_ids=user_ids)

    def get_allowed_permissions(self):
        return self.user_permissions_controller.get_allowed_permissions_using_get()

    """ Widget endpoints. """

    def get_widgets_budle_by_id(self, widgets_bundle_id: WidgetsBundleId):
        widgets_bundle_id = self.get_id(widgets_bundle_id)
        return self.widgets_bundle_controller.get_widgets_bundle_by_id_using_get(widgets_bundle_id=widgets_bundle_id)

    def save_widgets_bundle(self, widgets_bundle: WidgetsBundle):
        return self.widgets_bundle_controller.save_widgets_bundle_using_post(widgets_bundle=widgets_bundle)

    def delete_widgets_bundle(self, widgets_bundle_id: WidgetsBundleId):
        widgets_bundle_id = self.get_id(widgets_bundle_id)
        self.widgets_bundle_controller.delete_widgets_bundle_using_delete(widgets_bundle_id=widgets_bundle_id)

    def get_widgets_bundles(self, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        return self.widgets_bundle_controller.get_widgets_bundles_using_get(page_size=str(page_size),
                                                                            page=str(page),
                                                                            text_search=text_search,
                                                                            sort_property=sort_property,
                                                                            sort_order=sort_order)

    """ Widget type endpoints"""

    def get_widget_type_by_id(self, widget_type_id: WidgetTypeId):
        widget_type_id = self.get_id(widget_type_id)
        return self.widget_type_controller.get_widget_type_by_id_using_get(widget_type_id=widget_type_id)

    def save_widget_type(self, widget_type: WidgetType):
        return self.widget_type_controller.save_widget_type_using_post(widget_type=widget_type)

    def delete_widget_type(self, widget_type_id: WidgetTypeId):
        widget_type_id = self.get_id(widget_type_id)
        self.widget_type_controller.delete_widget_type_using_delete(widget_type_id=widget_type_id)

    def get_bundle_widget_types(self, is_system, bundle_alias):
        is_system = str(is_system).lower()
        return self.widget_type_controller.get_bundle_widget_types_using_get(is_system=is_system, bundle_alias=bundle_alias)

    def get_widget_type(self, is_system, bundle_alias, alias):
        is_system = str(is_system).lower()
        return self.widget_type_controller.get_widget_type_using_get(is_system=is_system, bundle_alias=bundle_alias, alias=alias)

    """ Blob Entity endpoints"""

    def get_blob_entity_info(self, blob_entity_id: BlobEntityId):
        blob_entity_id = self.get_id(blob_entity_id)
        return self.blob_entity_controller.get_blob_entity_info_by_id_using_get(blob_entity_id=blob_entity_id)

    def download_blob_entity(self, blob_entity_id: BlobEntityId):
        blob_entity_id = self.get_id(blob_entity_id)
        return self.blob_entity_controller.download_blob_entity_using_get(blob_entity_id=blob_entity_id)

    def delete_blob_entity(self, blob_entity_id: BlobEntityId):
        blob_entity_id = self.get_id(blob_entity_id)
        self.blob_entity_controller.delete_blob_entity_using_delete(blob_entity_id=blob_entity_id)

    def get_blob_entities(self, type, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None):
        return self.blob_entity_controller.get_blob_entities_using_get(page_size=page_size,
                                                                       page=page,
                                                                       type=type,
                                                                       text_search=text_search,
                                                                       sort_property=sort_property,
                                                                       sort_order=sort_order,
                                                                       start_time=start_time,
                                                                       end_time=end_time)

    def get_blob_entities_by_ids(self, blob_entity_ids):
        return self.blob_entity_controller.get_blob_entities_by_ids_using_get(blob_entity_ids=blob_entity_ids)

    """ Converter endpoints """

    def get_converter_by_id(self, converter_id: ConverterId):
        converter_id = self.get_id(converter_id)
        return self.converter_controller.get_converter_by_id_using_get(converter_id=converter_id)

    def save_converter(self, converter: Converter):
        return self.converter_controller.save_converter_using_post(converter=converter)

    def get_converters(self, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        return self.converter_controller.get_converters_using_get(page_size=str(page_size),
                                                                  page=str(page),
                                                                  text_search=text_search,
                                                                  sort_property=sort_property,
                                                                  sort_order=sort_order)

    def delete_converter(self, converter_id: ConverterId):
        converter_id = self.get_id(converter_id)
        self.converter_controller.delete_converter_using_delete(converter_id=converter_id)

    def get_latest_converter_debug_input(self, converter_id: ConverterId):
        converter_id = self.get_id(converter_id)
        self.converter_controller.get_latest_converter_debug_input_using_get(converter_id=converter_id)

    def test_uplink_converter(self, input_params):
        return self.converter_controller.test_up_link_converter_using_post(input_params=input_params)

    def test_downlink_converter(self, input_params):
        return self.converter_controller.test_down_link_converter_using_post(input_params=input_params)

    def get_converters_by_ids(self, converter_ids):
        return self.converter_controller.get_converters_by_ids_using_get(converter_ids=converter_ids)

    """ Custom menu endpoints"""

    def get_custom_menu(self):
        return self.custom_menu_controller.get_custom_menu_using_get()

    def get_current_custom_menu(self):
        return self.custom_menu_controller.get_current_custom_menu_using_get()

    def save_custom_menu(self, custom_menu: CustomMenu):
        return self.custom_menu_controller.save_custom_menu_using_post(custom_menu=custom_menu)

    """ Custom translations endpoints"""

    def get_custom_translation(self):
        return self.custom_translation_controller.get_custom_translation_using_get()

    def get_current_custom_translation(self):
        return self.custom_translation_controller.get_current_custom_translation_using_get()

    def save_custom_translation(self, custom_translation: CustomTranslation):
        return self.custom_translation_controller.save_custom_translation_using_post(custom_translation=custom_translation)

    """Entity group endpoints"""

    def get_entity_group_by_id(self, entity_group_id: EntityGroupId):
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.get_entity_group_by_id_using_get(entity_group_id=entity_group_id)

    def save_entity_group(self, entity_group: EntityGroup):
        return self.entity_group_controller.save_entity_group_using_post(entity_group=entity_group)

    def delete_entity_group(self, entity_group_id: EntityGroupId):
        entity_group_id = self.get_id(entity_group_id)
        self.entity_group_controller.delete_entity_group_using_delete(entity_group_id=entity_group_id)

    def get_entity_groups_by_type(self, group_type):
        group_type = self.get_type(group_type)
        self.entity_group_controller.get_entity_groups_by_type_using_get(group_type=group_type)

    def get_entity_groups_by_owner_and_type(self, owner_id, group_type):
        group_type = self.get_type(group_type)
        return self.entity_group_controller.get_entity_groups_by_owner_and_type_using_get(owner_type=owner_id.entity_type,
                                                                                          owner_id=owner_id.id,
                                                                                          group_type=group_type)

    def get_entity_group_all_by_owner_and_type(self, owner_id, group_type):
        group_type = self.get_type(group_type)
        return self.entity_group_controller.get_entity_group_all_by_owner_and_type_using_get(owner_type=owner_id.entity_type,
                                                                                             owner_id=owner_id.id,
                                                                                             group_type=group_type)

    def get_entity_group_info_by_owner_and_name_and_type(self, owner_id, group_type, group_name):
        group_type = self.get_type(group_type)
        return self.entity_group_controller.get_enitity_group_by_owner_and_name_and_type_using_get(owner_type=owner_id.entity_type,
                                                                                                   owner_id=owner_id.id,
                                                                                                   group_type=group_type,
                                                                                                   group_name=group_name)

    def add_entities_to_entity_group(self, entity_group_id: EntityGroupId, entity_ids):
        entity_group_id = self.get_id(entity_group_id)
        self.entity_group_controller.add_entities_to_entity_group_using_post(entity_group_id=entity_group_id,
                                                                             str_entity_ids=entity_ids)

    def remove_entities_from_entity_group(self, entity_group_id: EntityGroupId, entity_ids):
        entity_group_id = self.get_id(entity_group_id)
        self.entity_group_controller.remove_entities_from_entity_group_using_post(entity_group_id=entity_group_id,
                                                                                  str_entity_ids=entity_ids)

    def get_group_entity(self, entity_group_id: EntityGroupId, entity_id):
        entity_group_id = self.get_id(entity_group_id)
        entity_id = self.get_id(entity_id)
        return self.entity_group_controller.get_group_entity_using_get(entity_group_id=entity_group_id,
                                                                       entity_id=entity_id)

    def get_entities(self, entity_group_id: EntityGroupId, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.get_entities_using_get(entity_group_id=entity_group_id,
                                                                   page_size=str(page_size),
                                                                   page=str(page),
                                                                   text_search=text_search,
                                                                   sort_property=sort_property,
                                                                   sort_order=sort_order)

    def get_entity_groups_for_entity(self, entity_id: EntityId):
        entity_id = self.get_id(entity_id)
        return self.get_entity_groups_for_entity(entity_id=entity_id)

    def get_entity_groups_by_ids(self, entity_group_ids):
        return self.entity_group_controller.get_entity_groups_by_ids_using_get(entity_group_ids=entity_group_ids)

    def get_owners(self, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        return self.entity_group_controller.get_owners_using_get(page_size=str(page_size),
                                                                 page=str(page),
                                                                 text_search=text_search,
                                                                 sort_property=sort_property,
                                                                 sort_order=sort_order)

    def make_entity_group_public(self, entity_group_id: EntityGroupId):
        entity_group_id = self.get_id(entity_group_id)
        self.entity_group_controller.make_entity_group_public_using_post(entity_group_id=entity_group_id)

    def make_entity_group_private(self, entity_group_id: EntityGroupId):
        entity_group_id = self.get_id(entity_group_id)
        self.entity_group_controller.make_entity_group_private_using_post(entity_group_id=entity_group_id)

    """ Group permissions endpoints"""

    def get_group_permission_by_id(self, group_permission_id: GroupPermissionId):
        group_permission_id = self.get_id(group_permission_id)
        return self.group_permission_controller.get_group_permission_by_id_using_get(group_permission_id=group_permission_id)

    def save_group_permission(self, group_permission: GroupPermission):
        return self.group_permission_controller.save_group_permission_using_post(group_permission=group_permission)

    def delete_group_permission(self, group_permission_id: GroupPermissionId):
        group_permission_id = self.get_id(group_permission_id)
        self.group_permission_controller.delete_group_permission_using_delete(group_permission_id=group_permission_id)

    def get_user_group_permissions(self, user_group_id):
        user_group_id = self.get_id(user_group_id)
        return self.group_permission_controller.get_user_group_permissions_using_get(user_group_id=user_group_id)

    def get_entity_group_permissions(self, entity_group_id: EntityGroupId):
        entity_group_id = self.get_id(entity_group_id)
        return self.group_permission_controller.get_entity_group_permissions_using_get(entity_group_id=entity_group_id)

    """ Integration endpoints. """

    def get_integration_by_id(self, integration_id: IntegrationId):
        integration_id = self.get_id(integration_id)
        return self.integration_controller.get_integration_by_id_using_get(integration_id=integration_id)

    def get_integration_by_routing_key(self, routing_key):
        return self.integration_controller.get_integration_by_routing_key_using_get(routing_key=routing_key)

    def save_integration(self, integration: Integration):
        return self.integration_controller.save_integration_using_post(integration=integration)

    def get_integrations(self, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        return self.integration_controller.get_integrations_using_get(page_size=str(page_size),
                                                                      page=str(page),
                                                                      text_search=text_search,
                                                                      sort_property=sort_property,
                                                                      sort_order=sort_order)

    def delete_integration(self, integration_id: IntegrationId):
        integration_id = self.get_id(integration_id)
        self.integration_controller.delete_integration_using_delete(integration_id=integration_id)

    def get_integrations_by_ids(self, integration_ids):
        return self.integration_controller.get_integrations_by_ids_using_get(integration_ids=integration_ids)

    """ Owner enpoints"""

    def change_owner_to_tenant(self, owner_id, entity_id):
        owner_id = self.get_id(owner_id)
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        self.owner_controller.change_owner_to_tenant_using_post(owner_id=owner_id, entity_id=entity_id, entity_type=entity_type)

    def change_owner_to_customer(self, owner_id, entity_id):
        owner_id = self.get_id(owner_id)
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        self.owner_controller.change_owner_to_customer_using_post(owner_id=owner_id, entity_id=entity_id, entity_type=entity_type)

    """ Reports endpoints """

    def download_dashboard_report(self, dashboard_id: DashboardId, report_params):
        dashboard_id = self.get_id(dashboard_id)
        return self.report_controller.download_dashboard_report_using_post(dashboard_id=dashboard_id, report_params=report_params)

    def download_test_report(self, report_config, reports_server_endpoint_url):
        return self.report_controller.download_test_report_using_post(report_config=report_config, reports_server_endpoint_url=reports_server_endpoint_url)

    """ Roles endpoints """

    def get_role_by_id(self, role_id: RoleId):
        role_id = self.get_id(role_id)
        return self.role_controller.get_role_by_id_using_get(role_id=role_id)

    def save_role(self, role: Role):
        return self.role_controller.save_role_using_post(role=role)

    def delete_role(self, role_id: RoleId):
        role_id = self.get_id(role_id)
        self.role_controller.delete_role_using_delete(role_id=role_id)

    def get_roles(self, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None):
        return self.role_controller.get_roles_using_get(page_size=str(page_size),
                                                        page=str(page),
                                                        text_search=text_search,
                                                        sort_property=sort_property,
                                                        sort_order=sort_order)

    def get_roles_by_ids(self, roles_ids):
        return self.role_controller.get_roles_by_ids_using_get(role_ids=roles_ids)

    def create_group_role(self, role_name, operations):
        role = Role(type="GROUP", name=role_name, permissions=operations)
        return self.save_role(role=role)

    """ Rule engine endpoints"""

    def handle_rule_engine_request(self, request_body, entity_id=None, timeout=None):
        if entity_id is None and timeout is None:
            return self.rule_engine_controller.handle_rule_engine_request_using_post(request_body=request_body)
        elif timeout is None:
            entity_type = self.get_type(entity_id)
            entity_id = self.get_type(entity_id)
            return self.rule_engine_controller.handle_rule_engine_request_using_post2(entity_id=entity_id, entity_type=entity_type, request_body=request_body)
        else:
            entity_type = self.get_type(entity_id)
            entity_id = self.get_type(entity_id)
            return self.rule_engine_controller.handle_rule_engine_request_using_post1(entity_id=entity_id, entity_type=entity_type, request_body=request_body, timeout=timeout)

    """ Scheduler endpoints """

    def get_scheduler_event_info_by_id(self, scheduler_event_id: SchedulerEventId):
        scheduler_event_id = self.get_id(scheduler_event_id)
        return self.scheduler_event_controller.get_scheduler_event_info_by_id_using_get(scheduler_event_id=scheduler_event_id)

    def get_scheduler_event_by_id(self, scheduler_event_id: SchedulerEventId):
        scheduler_event_id = self.get_id(scheduler_event_id)
        return self.scheduler_event_controller.get_scheduler_event_by_id_using_get(scheduler_event_id=scheduler_event_id)

    def save_scheduler_event(self, scheduler_event: SchedulerEvent):
        return self.scheduler_event_controller.save_scheduler_event_using_post(scheduler_event=scheduler_event)

    def delete_scheduler_event(self, scheduler_event_id: SchedulerEventId):
        scheduler_event_id = self.get_id(scheduler_event_id)
        self.scheduler_event_controller.delete_scheduler_event_using_delete(scheduler_event_id=scheduler_event_id)

    def get_scheduler_events(self, type):
        return self.scheduler_event_controller.get_scheduler_events_using_get(type=type)

    def get_scheduler_events_by_ids(self, scheduler_event_ids):
        return self.scheduler_event_controller.get_scheduler_events_by_ids_using_get(scheduler_event_ids=scheduler_event_ids)

    """ Self registration endpoints. """

    def save_self_registration_params(self, self_registration_params: SelfRegistrationParams):
        return self.self_registration_controller.save_self_registration_params_using_post(self_registration_params=self_registration_params)

    def get_self_registration_params(self):
        return self.self_registration_controller.get_self_registration_params_using_get()

    def get_sign_up_self_registration_params(self):
        return self.self_registration_controller.get_sign_up_self_registration_params_using_get()

    def get_privacy_policy(self):
        return self.self_registration_controller.get_privacy_policy_using_get()

    """ Sign up endpoints. """

    def sign_up(self, sign_up_request: SignUpRequest):
        return self.sign_up_controller.sign_up_using_post(sign_up_request=sign_up_request)
    
    def resend_email_activation(self, email: str):
        return self.sign_up_controller.resend_email_activation_using_post(email=email)
    
    def activate_email(self, email_code):
        return self.sign_up_controller.activate_email_using_get(email_code=email_code)

    def activate_user_by_email_code(self, email_code):
        return self.sign_up_controller.activate_user_by_email_code_using_post(email_code=email_code)

    def privacy_policy_accepted(self):
        return self.sign_up_controller.privacy_policy_accepted_using_get()

    def accept_privace_policy(self):
        return self.sign_up_controller.accept_privacy_policy_using_post()

    """ White label endpoints. """

    def get_white_label_params(self, logo_image_checksum, favicon_checksum):
        return self.white_labeling_controller.get_white_label_params_using_get(logo_image_checksum=logo_image_checksum, favicon_checksum=favicon_checksum)

    def get_login_white_label_params(self, logo_image_checksum, favicon_checksum):
        return self.white_labeling_controller.get_login_white_label_params_using_get(logo_image_checksum=logo_image_checksum, favicon_checksum=favicon_checksum)

    def get_current_white_label_params(self):
        return self.white_labeling_controller.get_current_white_label_params_using_get()

    def get_current_login_white_label_params(self):
        return self.white_labeling_controller.get_current_login_white_label_params_using_get()

    def save_white_label_params(self, white_labeling_params: WhiteLabelingParams):
        return self.white_labeling_controller.save_white_label_params_using_post(white_labeling_params=white_labeling_params)

    def save_login_white_label_params(self, login_white_labeling_params: LoginWhiteLabelingParams):
        return self.white_labeling_controller.save_login_white_label_params_using_post(login_white_labeling_params=login_white_labeling_params)

    def preview_white_label_params(self, white_labeling_params: WhiteLabelingParams):
        return self.white_labeling_controller.preview_white_label_params_using_post(white_labeling_params=white_labeling_params)

    def is_white_labeling_allowed(self):
        return self.white_labeling_controller.is_white_labeling_allowed_using_get()

    def is_customer_white_labeling_allowed(self):
        return self.white_labeling_controller.is_customer_white_labeling_allowed_using_get()

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

    @staticmethod
    def get_type(type):
        return type.entity_type if hasattr(type, "entity_type") else type

    @staticmethod
    def get_id(id):
        return id.id if hasattr(id, "id") else id

if __name__ == '__main__':
    restClient = RestClient("127.0.0.1:8080")
    restClient.start()
    restClient.login("tenant@thingsboard.org", "tenant")
    admin_settings = restClient.get_admin_settings("name")
    restClient.stop()
    logger.error(admin_settings)

