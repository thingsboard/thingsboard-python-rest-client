# coding: utf-8
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

from logging import getLogger
from threading import Thread
from time import time, sleep

from requests import post

from tb_rest_client32.api.api_ce import *
from tb_rest_client32.api_client import ApiClient
from tb_rest_client32.configuration import Configuration
from tb_rest_client32.models.models_ce import *

logger = getLogger(__name__)


class RestClientBase(Thread):
    def __init__(self, base_url):
        super().__init__()
        if base_url.startswith("http"):
            self.base_url = base_url
        else:
            self.base_url = "http://" + base_url
        self.token_info = {"token": "", "refreshToken": 0}
        self.api_client = None
        self.username = None
        self.password = None
        self.logged_in = False
        self.stopped = True
        self.configuration = Configuration()
        self.configuration.host = self.base_url

    def run(self):
        self.stopped = False
        while not self.stopped:
            try:
                check_time = time()
                if check_time >= self.token_info["refreshToken"] and self.logged_in:
                    if self.username and self.password:
                        self.login(self.username, self.password)
                    else:
                        logger.error("No username or password provided!")
                sleep(1)
            except Exception as e:
                logger.exception(e)
                break
            except KeyboardInterrupt:
                break

    def stop(self):
        self.stopped = True

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    def login(self, username, password):
        """Authorization on the host and saving the toke information"""
        if self.username is None and self.password is None:
            self.username = username
            self.password = password
            self.logged_in = True

        token_json = post(self.base_url + "/api/auth/login",
                          json={"username": username, "password": password},
                          verify=self.configuration.verify_ssl).json()
        token = None
        if isinstance(token_json, dict) and token_json.get("token") is not None:
            token = token_json["token"]
        self.configuration.api_key_prefix["X-Authorization"] = "Bearer"
        self.configuration.api_key["X-Authorization"] = token

        self.api_client = ApiClient(self.configuration)
        self.__load_controllers()

    def get_token(self):
        return self.token_info["token"]

    def delete_asset(self, asset_id: AssetId, **kwargs):
        return self.asset_controller.delete_asset_using_delete(asset_id.id, **kwargs)

    def get_asset_by_id(self, asset_id: AssetId, **kwargs):
        return self.asset_controller.get_asset_by_id_using_get(asset_id.id, **kwargs)

    def get_asset_types(self, **kwargs):
        return self.asset_controller.get_asset_types_using_get(**kwargs)

    def get_assets_by_ids(self, asset_ids, **kwargs):
        return self.asset_controller.get_assets_by_ids_using_get(asset_ids, **kwargs)

    def get_customer_assets(self, customer_id: CustomerId, page_size=100, page=0, **kwargs):
        return self.asset_controller.get_customer_assets_using_get(customer_id.id, str(page_size), str(page), **kwargs)

    def get_tenant_asset(self, asset_name, **kwargs):
        return self.asset_controller.get_tenant_asset_using_get(asset_name, **kwargs)

    def get_tenant_assets(self, page_size=100, page=0, **kwargs):
        return self.asset_controller.get_tenant_assets_using_get(str(page_size), str(page), **kwargs)

    def save_asset(self, asset, **kwargs):
        return self.asset_controller.save_asset_using_post(asset, **kwargs)

    ##################################

    def delete_user(self, user_id: UserId, **kwargs):
        return self.user_controller.delete_user_using_delete(user_id.id, **kwargs)

    def get_activation_link(self, user_id: UserId, **kwargs):
        return self.user_controller.get_activation_link_using_get(user_id.id, **kwargs)

    def get_customer_users(self, customer_id: CustomerId, page_size=100, page=0, **kwargs):
        return self.user_controller.get_customer_users_using_get(customer_id.id, str(page_size), str(page), **kwargs)

    def get_tenant_admins(self, tenant_id: TenantId, page_size=100, page=0, **kwargs):
        return self.user_controller.get_tenant_admins_using_get(tenant_id.id, str(page_size), str(page), **kwargs)

    def get_user_by_id(self, user_id: UserId, **kwargs):
        return self.user_controller.get_user_by_id_using_get(user_id.id, **kwargs)

    def get_user_token(self, user_id: UserId, **kwargs):
        return self.user_controller.get_user_token_using_get(user_id.id, **kwargs)

    def is_user_token_access_enabled(self, **kwargs):
        return self.user_controller.is_user_token_access_enabled_using_get(**kwargs)

    def save_user(self, user, **kwargs):
        return self.user_controller.save_user_using_post(user, **kwargs)

    def send_activation_email(self, email, **kwargs):
        return self.user_controller.send_activation_email_using_post(email, **kwargs)

    def set_user_credentials_enabled(self, user_id: UserId, **kwargs):
        return self.user_controller.set_user_credentials_enabled_using_post(user_id.id, **kwargs)

    ##################################

    def get_activation_token(self, user_id: UserId):
        user_id = self.get_id(user_id)
        return self.user_controller.get_activation_token_using_get(user_id)

    def activate_user(self, user_id: UserId, password):
        user_id = self.get_id(user_id)
        activation_request = {"activateToken": self.get_activation_token(user_id).replace("'", '"'),
                              "password": password}
        return self.auth_controller.activate_user_using_post(activation_request)

    def change_password(self, change_password_request, **kwargs):
        return self.auth_controller.change_password_using_post(change_password_request, **kwargs)

    def check_activate_token(self, activate_token, **kwargs):
        return self.auth_controller.check_activate_token_using_get(activate_token, **kwargs)

    def check_reset_token(self, reset_token, **kwargs):
        return self.auth_controller.check_reset_token_using_get(reset_token, **kwargs)

    def get_user_password_policy(self, **kwargs):
        return self.auth_controller.get_user_password_policy_using_get(**kwargs)

    def get_user(self, **kwargs):
        return self.auth_controller.get_user_using_get(**kwargs)

    def logout(self, **kwargs):
        return self.auth_controller.logout_using_post(**kwargs)

    def request_reset_password_by_email(self, reset_password_by_email_request, **kwargs):
        return self.auth_controller.request_reset_password_by_email_using_post(reset_password_by_email_request, **kwargs)

    def reset_password(self, reset_password_request, **kwargs):
        return self.auth_controller.reset_password_using_post(reset_password_request, **kwargs)

    ##################################

    def assign_device_to_tenant(self, tenant_id: TenantId, device_id: DeviceId, **kwargs):
        return self.device_controller.assign_device_to_tenant_using_post(tenant_id.id, device_id.id, **kwargs)

    def claim_device1(self, device_name, **kwargs):
        return self.device_controller.claim_device_using_post1(device_name, **kwargs)

    def delete_device(self, device_id: DeviceId, **kwargs):
        return self.device_controller.delete_device_using_delete(device_id.id, **kwargs)

    def get_customer_devices(self, customer_id: CustomerId, page_size=100, page=0, **kwargs):
        return self.device_controller.get_customer_devices_using_get(customer_id.id, str(page_size), str(page), **kwargs)

    def get_device_by_id(self, device_id: DeviceId, **kwargs):
        return self.device_controller.get_device_by_id_using_get(device_id.id, **kwargs)

    def get_device_credentials_by_device_id(self, device_id: DeviceId, **kwargs):
        return self.device_controller.get_device_credentials_by_device_id_using_get(device_id.id, **kwargs)

    def get_device_types(self, **kwargs):
        return self.device_controller.get_device_types_using_get(**kwargs)

    def get_devices_by_ids(self, device_ids, **kwargs):
        return self.device_controller.get_devices_by_ids_using_get(device_ids, **kwargs)

    def get_tenant_device(self, device_name, **kwargs):
        return self.device_controller.get_tenant_device_using_get(device_name, **kwargs)

    def get_tenant_devices(self, page_size=100, page=0, **kwargs):
        return self.device_controller.get_tenant_devices_using_get(str(page_size), str(page), **kwargs)

    def re_claim_device(self, device_name, **kwargs):
        return self.device_controller.re_claim_device_using_delete(device_name, **kwargs)

    def save_device_credentials(self, device_credentials, **kwargs):
        return self.device_controller.save_device_credentials_using_post(device_credentials, **kwargs)

    def save_device(self, device, **kwargs):
        return self.device_controller.save_device_using_post(device, **kwargs)

    ##################################

    def delete_widget_type(self, widget_type_id: WidgetTypeId, **kwargs):
        return self.widget_type_controller.delete_widget_type_using_delete(widget_type_id.id, **kwargs)

    def get_bundle_widget_types(self, is_system, bundle_alias, **kwargs):
        return self.widget_type_controller.get_bundle_widget_types_using_get(is_system, bundle_alias, **kwargs)

    def get_widget_type_by_id(self, widget_type_id: WidgetTypeId, **kwargs):
        return self.widget_type_controller.get_widget_type_by_id_using_get(widget_type_id.id, **kwargs)

    def get_widget_type(self, is_system, bundle_alias, alias, **kwargs):
        return self.widget_type_controller.get_widget_type_using_get(is_system, bundle_alias, alias, **kwargs)

    def save_widget_type(self, widget_type, **kwargs):
        return self.widget_type_controller.save_widget_type_using_post(widget_type, **kwargs)

    ##################################

    def delete_entity_attributes(self, device_id: DeviceId, scope, keys, **kwargs):
        return self.telemetry_controller.delete_entity_attributes_using_delete(device_id.id, scope, keys, **kwargs)

    def delete_entity_attributes1(self, entity_id: EntityId, scope, keys, **kwargs):
        return self.telemetry_controller.delete_entity_attributes_using_delete1(entity_id.entity_type, entity_id.id, scope, keys, **kwargs)

    def delete_entity_timeseries(self, entity_id: EntityId, keys, **kwargs):
        return self.telemetry_controller.delete_entity_timeseries_using_delete(entity_id.entity_type, entity_id.id, keys, **kwargs)

    def get_attribute_keys_by_scope(self, entity_id: EntityId, scope, **kwargs):
        return self.telemetry_controller.get_attribute_keys_by_scope_using_get(entity_id.entity_type, entity_id.id, scope, **kwargs)

    def get_attribute_keys(self, entity_id: EntityId, **kwargs):
        return self.telemetry_controller.get_attribute_keys_using_get(entity_id.entity_type, entity_id.id, **kwargs)

    def get_attributes_by_scope(self, entity_id: EntityId, scope, **kwargs):
        return self.telemetry_controller.get_attributes_by_scope_using_get(entity_id.entity_type, entity_id.id, scope, **kwargs)

    def get_attributes(self, entity_id: EntityId, **kwargs):
        return self.telemetry_controller.get_attributes_using_get(entity_id.entity_type, entity_id.id, **kwargs)

    def get_latest_timeseries(self, entity_id: EntityId, **kwargs):
        return self.telemetry_controller.get_latest_timeseries_using_get(entity_id.entity_type, entity_id.id, **kwargs)

    def get_timeseries_keys(self, entity_id: EntityId, **kwargs):
        return self.telemetry_controller.get_timeseries_keys_using_get(entity_id.entity_type, entity_id.id, **kwargs)

    def get_timeseries(self, entity_id: EntityId, keys, start_ts, end_ts, **kwargs):
        return self.telemetry_controller.get_timeseries_using_get(entity_id.entity_type, entity_id.id, keys, start_ts, end_ts, **kwargs)

    def save_device_attributes(self, device_id: DeviceId, scope, request, **kwargs):
        return self.telemetry_controller.save_device_attributes_using_post(device_id.id, scope, request, **kwargs)

    def save_entity_attributes_v1(self, entity_id: EntityId, scope, request, **kwargs):
        return self.telemetry_controller.save_entity_attributes_v1_using_post(entity_id.entity_type, entity_id.id, scope, request, **kwargs)

    def save_entity_attributes_v2(self, entity_id: EntityId, scope, request, **kwargs):
        return self.telemetry_controller.save_entity_attributes_v2_using_post(entity_id.entity_type, entity_id.id, scope, request, **kwargs)

    def save_entity_telemetry(self, entity_id: EntityId, scope, request_body, **kwargs):
        return self.telemetry_controller.save_entity_telemetry_using_post(entity_id.entity_type, entity_id.id, scope, request_body, **kwargs)

    def save_entity_telemetry_with_ttl(self, entity_id: EntityId, scope, ttl, request_body, **kwargs):
        return self.telemetry_controller.save_entity_telemetry_with_ttl_using_post(entity_id.entity_type, entity_id.id, scope, ttl, request_body, **kwargs)

    ##################################

    def get_tenant_queues_by_service_type(self, service_type, **kwargs):
        return self.queue_controller.get_tenant_queues_by_service_type_using_get(service_type, **kwargs)

    ##################################

    def get_events(self, entity_id: EntityId, event_type, tenant_id: TenantId, page_size=100, page=0, **kwargs):
        return self.event_controller.get_events_using_get(entity_id.entity_type, entity_id.id, event_type, tenant_id.id, str(page_size), str(page), **kwargs)

    def get_events1(self, entity_id: EntityId, tenant_id: TenantId, page_size=100, page=0, **kwargs):
        return self.event_controller.get_events_using_get1(entity_id.entity_type, entity_id.id, tenant_id.id, str(page_size), str(page), **kwargs)

    ##################################

    def delete_rule_chain(self, rule_chain_id: RuleChainId, **kwargs):
        return self.rule_chain_controller.delete_rule_chain_using_delete(rule_chain_id.id, **kwargs)

    def export_rule_chains(self, limit, **kwargs):
        return self.rule_chain_controller.export_rule_chains_using_get(limit, **kwargs)

    def get_latest_rule_node_debug_input(self, rule_node_id: RuleNodeId, **kwargs):
        return self.rule_chain_controller.get_latest_rule_node_debug_input_using_get(rule_node_id.id, **kwargs)

    def get_rule_chain_by_id(self, rule_chain_id: RuleChainId, **kwargs):
        return self.rule_chain_controller.get_rule_chain_by_id_using_get(rule_chain_id.id, **kwargs)

    def get_rule_chain_meta_data(self, rule_chain_id: RuleChainId, **kwargs):
        return self.rule_chain_controller.get_rule_chain_meta_data_using_get(rule_chain_id.id, **kwargs)

    def get_rule_chains(self, page_size=100, page=0, **kwargs):
        return self.rule_chain_controller.get_rule_chains_using_get(str(page_size), str(page), **kwargs)

    def import_rule_chains(self, rule_chain_data, **kwargs):
        return self.rule_chain_controller.import_rule_chains_using_post(rule_chain_data, **kwargs)

    def save_rule_chain_meta_data(self, rule_chain_meta_data, **kwargs):
        return self.rule_chain_controller.save_rule_chain_meta_data_using_post(rule_chain_meta_data, **kwargs)

    def save_rule_chain(self, request, **kwargs):
        return self.rule_chain_controller.save_rule_chain_using_post(request, **kwargs)

    def save_rule_chain1(self, rule_chain, **kwargs):
        return self.rule_chain_controller.save_rule_chain_using_post1(rule_chain, **kwargs)

    def set_root_rule_chain(self, rule_chain_id: RuleChainId, **kwargs):
        return self.rule_chain_controller.set_root_rule_chain_using_post(rule_chain_id.id, **kwargs)

    def test_script(self, input_params, **kwargs):
        return self.rule_chain_controller.test_script_using_post(input_params, **kwargs)

    ##################################

    def count_entities_by_query(self, query, **kwargs):
        return self.entity_query_controller.count_entities_by_query_using_post(query, **kwargs)

    def find_alarm_data_by_query(self, query, **kwargs):
        return self.entity_query_controller.find_alarm_data_by_query_using_post(query, **kwargs)

    def find_entity_data_by_query(self, query, **kwargs):
        return self.entity_query_controller.find_entity_data_by_query_using_post(query, **kwargs)

    ##################################

    def delete_tenant(self, tenant_id: TenantId, **kwargs):
        return self.tenant_controller.delete_tenant_using_delete(tenant_id.id, **kwargs)

    def get_tenant_by_id(self, tenant_id: TenantId, **kwargs):
        return self.tenant_controller.get_tenant_by_id_using_get(tenant_id.id, **kwargs)

    def get_tenant_info_by_id(self, tenant_id: TenantId, **kwargs):
        return self.tenant_controller.get_tenant_info_by_id_using_get(tenant_id.id, **kwargs)

    def get_tenant_infos(self, page_size=100, page=0, **kwargs):
        return self.tenant_controller.get_tenant_infos_using_get(str(page_size), str(page), **kwargs)

    def get_tenants(self, page_size=100, page=0, **kwargs):
        return self.tenant_controller.get_tenants_using_get(str(page_size), str(page), **kwargs)

    def save_tenant(self, tenant, **kwargs):
        return self.tenant_controller.save_tenant_using_post(tenant, **kwargs)

    ##################################

    def delete_device_profile(self, device_profile_id: DeviceProfileId, **kwargs):
        return self.device_profile_controller.delete_device_profile_using_delete(device_profile_id.id, **kwargs)

    def get_default_device_profile_info(self, **kwargs):
        return self.device_profile_controller.get_default_device_profile_info_using_get(**kwargs)

    def get_device_profile_by_id(self, device_profile_id: DeviceProfileId, **kwargs):
        return self.device_profile_controller.get_device_profile_by_id_using_get(device_profile_id.id, **kwargs)

    def get_device_profile_info_by_id(self, device_profile_id: DeviceProfileId, **kwargs):
        return self.device_profile_controller.get_device_profile_info_by_id_using_get(device_profile_id.id, **kwargs)

    def get_device_profile_infos(self, page_size=100, page=0, **kwargs):
        return self.device_profile_controller.get_device_profile_infos_using_get(str(page_size), str(page), **kwargs)

    def get_device_profiles(self, page_size=100, page=0, **kwargs):
        return self.device_profile_controller.get_device_profiles_using_get(str(page_size), str(page), **kwargs)

    def save_device_profile(self, device_profile, **kwargs):
        return self.device_profile_controller.save_device_profile_using_post(device_profile, **kwargs)

    def set_default_device_profile(self, device_profile_id: DeviceProfileId, **kwargs):
        return self.device_profile_controller.set_default_device_profile_using_post(device_profile_id.id, **kwargs)

    ##################################

    def delete_dashboard(self, dashboard_id: DashboardId, **kwargs):
        return self.dashboard_controller.delete_dashboard_using_delete(dashboard_id.id, **kwargs)

    def get_dashboard_by_id(self, dashboard_id: DashboardId, **kwargs):
        return self.dashboard_controller.get_dashboard_by_id_using_get(dashboard_id.id, **kwargs)

    def get_dashboard_info_by_id(self, dashboard_id: DashboardId, **kwargs):
        return self.dashboard_controller.get_dashboard_info_by_id_using_get(dashboard_id.id, **kwargs)

    def get_max_datapoints_limit(self, **kwargs):
        return self.dashboard_controller.get_max_datapoints_limit_using_get(**kwargs)

    def get_server_time(self, **kwargs):
        return self.dashboard_controller.get_server_time_using_get(**kwargs)

    def get_tenant_dashboards(self, page_size=100, page=0, **kwargs):
        return self.dashboard_controller.get_tenant_dashboards_using_get(str(page_size), str(page), **kwargs)

    def get_tenant_dashboards1(self, tenant_id: TenantId, page_size=100, page=0, **kwargs):
        return self.dashboard_controller.get_tenant_dashboards_using_get1(tenant_id.id, str(page_size), str(page), **kwargs)

    def save_dashboard(self, dashboard, **kwargs):
        return self.dashboard_controller.save_dashboard_using_post(dashboard, **kwargs)

    ##################################

    def claim_device(self, device_token, **kwargs):
        return self.device_api_controller.claim_device_using_post(device_token, **kwargs)

    def get_device_attributes(self, device_token, **kwargs):
        return self.device_api_controller.get_device_attributes_using_get(device_token, **kwargs)

    def post_device_attributes(self, device_token, json, **kwargs):
        return self.device_api_controller.post_device_attributes_using_post(device_token, json, **kwargs)

    def post_rpc_request(self, device_token, json, **kwargs):
        return self.device_api_controller.post_rpc_request_using_post(device_token, json, **kwargs)

    def post_telemetry(self, device_token, json, **kwargs):
        return self.device_api_controller.post_telemetry_using_post(device_token, json, **kwargs)

    def provision_device(self, json, **kwargs):
        return self.device_api_controller.provision_device_using_post(json, **kwargs)

    def reply_to_command(self, device_token, request_id, json, **kwargs):
        return self.device_api_controller.reply_to_command_using_post(device_token, request_id, json, **kwargs)

    def subscribe_to_attributes(self, device_token, **kwargs):
        return self.device_api_controller.subscribe_to_attributes_using_get(device_token, **kwargs)

    def subscribe_to_commands(self, device_token, **kwargs):
        return self.device_api_controller.subscribe_to_commands_using_get(device_token, **kwargs)

    ##################################

    def delete_relation(self, from_id, from_type, relation_type, to_id, to_type, **kwargs):
        return self.entity_relation_controller.delete_relation_using_delete(from_id, from_type, relation_type, to_id, to_type, **kwargs)

    def delete_relations(self, entity_id: EntityId, id, type, **kwargs):
        return self.entity_relation_controller.delete_relations_using_delete(entity_id.id, entity_id.entity_type, id, type, **kwargs)

    def find_info_by_from(self, from_id, from_type, **kwargs):
        return self.entity_relation_controller.find_info_by_from_using_get(from_id, from_type, **kwargs)

    def find_info_by_query(self, query, **kwargs):
        return self.entity_relation_controller.find_info_by_query_using_post(query, **kwargs)

    def find_info_by_to(self, to_id, to_type, **kwargs):
        return self.entity_relation_controller.find_info_by_to_using_get(to_id, to_type, **kwargs)

    def get_relation(self, from_id, from_type, relation_type, to_id, to_type, **kwargs):
        return self.entity_relation_controller.get_relation_using_get(from_id, from_type, relation_type, to_id, to_type, **kwargs)

    def save_relation(self, relation, **kwargs):
        return self.entity_relation_controller.save_relation_using_post(relation, **kwargs)

    ##################################

    def handle_one_way_device_rpc_request(self, device_id: DeviceId, request_body, **kwargs):
        return self.rpc_controller.handle_one_way_device_rpc_request_using_post(device_id.id, request_body, **kwargs)

    def handle_two_way_device_rpc_request(self, device_id: DeviceId, request_body, **kwargs):
        return self.rpc_controller.handle_two_way_device_rpc_request_using_post(device_id.id, request_body, **kwargs)

    ##################################

    def ack_alarm(self, alarm_id: AlarmId, **kwargs):
        return self.alarm_controller.ack_alarm_using_post(alarm_id.id, **kwargs)

    def clear_alarm(self, alarm_id: AlarmId, **kwargs):
        return self.alarm_controller.clear_alarm_using_post(alarm_id.id, **kwargs)

    def delete_alarm(self, alarm_id: AlarmId, **kwargs):
        return self.alarm_controller.delete_alarm_using_delete(alarm_id.id, **kwargs)

    def get_alarm_by_id(self, alarm_id: AlarmId, **kwargs):
        return self.alarm_controller.get_alarm_by_id_using_get(alarm_id.id, **kwargs)

    def get_alarm_info_by_id(self, alarm_id: AlarmId, **kwargs):
        return self.alarm_controller.get_alarm_info_by_id_using_get(alarm_id.id, **kwargs)

    def get_alarms(self, entity_id: EntityId, page_size=100, page=0, **kwargs):
        return self.alarm_controller.get_alarms_using_get(entity_id.entity_type, entity_id.id, str(page_size), str(page), **kwargs)

    def get_highest_alarm_severity(self, entity_id: EntityId, **kwargs):
        return self.alarm_controller.get_highest_alarm_severity_using_get(entity_id.entity_type, entity_id.id, **kwargs)

    def save_alarm(self, alarm, **kwargs):
        return self.alarm_controller.save_alarm_using_post(alarm, **kwargs)

    ##################################

    def delete_widgets_bundle(self, widgets_bundle_id: WidgetsBundleId, **kwargs):
        return self.widgets_bundle_controller.delete_widgets_bundle_using_delete(widgets_bundle_id.id, **kwargs)

    def get_widgets_bundle_by_id(self, widgets_bundle_id: WidgetsBundleId, **kwargs):
        return self.widgets_bundle_controller.get_widgets_bundle_by_id_using_get(widgets_bundle_id.id, **kwargs)

    def get_widgets_bundles(self, page_size=100, page=0, **kwargs):
        return self.widgets_bundle_controller.get_widgets_bundles_using_get(str(page_size), str(page), **kwargs)

    def get_widgets_bundles1(self, **kwargs):
        return self.widgets_bundle_controller.get_widgets_bundles_using_get1(**kwargs)

    def save_widgets_bundle(self, widgets_bundle, **kwargs):
        return self.widgets_bundle_controller.save_widgets_bundle_using_post(widgets_bundle, **kwargs)

    ##################################

    def delete_tenant_profile(self, tenant_profile_id: TenantProfileId, **kwargs):
        return self.tenant_profile_controller.delete_tenant_profile_using_delete(tenant_profile_id.id, **kwargs)

    def get_default_tenant_profile_info(self, **kwargs):
        return self.tenant_profile_controller.get_default_tenant_profile_info_using_get(**kwargs)

    def get_tenant_profile_by_id(self, tenant_profile_id: TenantProfileId, **kwargs):
        return self.tenant_profile_controller.get_tenant_profile_by_id_using_get(tenant_profile_id.id, **kwargs)

    def get_tenant_profile_info_by_id(self, tenant_profile_id: TenantProfileId, **kwargs):
        return self.tenant_profile_controller.get_tenant_profile_info_by_id_using_get(tenant_profile_id.id, **kwargs)

    def get_tenant_profile_infos(self, page_size=100, page=0, **kwargs):
        return self.tenant_profile_controller.get_tenant_profile_infos_using_get(str(page_size), str(page), **kwargs)

    def get_tenant_profiles(self, page_size=100, page=0, **kwargs):
        return self.tenant_profile_controller.get_tenant_profiles_using_get(str(page_size), str(page), **kwargs)

    def save_tenant_profile(self, tenant_profile, **kwargs):
        return self.tenant_profile_controller.save_tenant_profile_using_post(tenant_profile, **kwargs)

    def set_default_tenant_profile(self, tenant_profile_id: TenantProfileId, **kwargs):
        return self.tenant_profile_controller.set_default_tenant_profile_using_post(tenant_profile_id.id, **kwargs)

    ##################################

    def get_component_descriptor_by_clazz(self, component_descriptor_clazz, **kwargs):
        return self.component_descriptor_controller.get_component_descriptor_by_clazz_using_get(component_descriptor_clazz, **kwargs)

    def get_component_descriptors_by_type(self, component_type, **kwargs):
        return self.component_descriptor_controller.get_component_descriptors_by_type_using_get(component_type, **kwargs)

    def get_component_descriptors_by_types(self, component_types, **kwargs):
        return self.component_descriptor_controller.get_component_descriptors_by_types_using_get(component_types, **kwargs)

    ##################################

    def get_audit_logs_by_customer_id(self, customer_id: CustomerId, page_size=100, page=0, **kwargs):
        return self.audit_log_controller.get_audit_logs_by_customer_id_using_get(customer_id.id, str(page_size), str(page), **kwargs)

    def get_audit_logs_by_entity_id(self, entity_id: EntityId, page_size=100, page=0, **kwargs):
        return self.audit_log_controller.get_audit_logs_by_entity_id_using_get(entity_id.entity_type, entity_id.id, str(page_size), str(page), **kwargs)

    def get_audit_logs_by_user_id(self, user_id: UserId, page_size=100, page=0, **kwargs):
        return self.audit_log_controller.get_audit_logs_by_user_id_using_get(user_id.id, str(page_size), str(page), **kwargs)

    def get_audit_logs(self, page_size=100, page=0, **kwargs):
        return self.audit_log_controller.get_audit_logs_using_get(str(page_size), str(page), **kwargs)

    ##################################

    def get_current_o_auth2_params(self, **kwargs):
        return self.o_auth_2_controller.get_current_o_auth2_params_using_get(**kwargs)

    def get_login_processing_url(self, **kwargs):
        return self.o_auth_2_controller.get_login_processing_url_using_get(**kwargs)

    def get_o_auth2_clients(self, **kwargs):
        return self.o_auth_2_controller.get_o_auth2_clients_using_post(**kwargs)

    def save_o_auth2_params(self, oauth2_params, **kwargs):
        return self.o_auth_2_controller.save_o_auth2_params_using_post(oauth2_params, **kwargs)

    ##################################

    def delete_client_registration_template(self, client_registration_template_id, **kwargs):
        return self.o_auth_2_config_template_controller.delete_client_registration_template_using_delete(client_registration_template_id, **kwargs)

    def get_client_registration_templates(self, **kwargs):
        return self.o_auth_2_config_template_controller.get_client_registration_templates_using_get(**kwargs)

    def save_client_registration_template(self, client_registration_template, **kwargs):
        return self.o_auth_2_config_template_controller.save_client_registration_template_using_post(client_registration_template, **kwargs)

    ##################################

    def delete_entity_view(self, entity_view_id: EntityViewId, **kwargs):
        return self.entity_view_controller.delete_entity_view_using_delete(entity_view_id.id, **kwargs)

    def get_customer_entity_views(self, customer_id: CustomerId, page_size=100, page=0, **kwargs):
        return self.entity_view_controller.get_customer_entity_views_using_get(customer_id.id, str(page_size), str(page), **kwargs)

    def get_entity_view_by_id(self, entity_view_id: EntityViewId, **kwargs):
        return self.entity_view_controller.get_entity_view_by_id_using_get(entity_view_id.id, **kwargs)

    def get_entity_view_types(self, **kwargs):
        return self.entity_view_controller.get_entity_view_types_using_get(**kwargs)

    def get_tenant_entity_view(self, entity_view_name, **kwargs):
        return self.entity_view_controller.get_tenant_entity_view_using_get(entity_view_name, **kwargs)

    def get_tenant_entity_views(self, page_size=100, page=0, **kwargs):
        return self.entity_view_controller.get_tenant_entity_views_using_get(str(page_size), str(page), **kwargs)

    def save_entity_view(self, entity_view, **kwargs):
        return self.entity_view_controller.save_entity_view_using_post(entity_view, **kwargs)

    ##################################

    def delete_customer(self, customer_id: CustomerId, **kwargs):
        return self.customer_controller.delete_customer_using_delete(customer_id.id, **kwargs)

    def get_customer_by_id(self, customer_id: CustomerId, **kwargs):
        return self.customer_controller.get_customer_by_id_using_get(customer_id.id, **kwargs)

    def get_customer_title_by_id(self, customer_id: CustomerId, **kwargs):
        return self.customer_controller.get_customer_title_by_id_using_get(customer_id.id, **kwargs)

    def get_customers(self, page_size=100, page=0, **kwargs):
        return self.customer_controller.get_customers_using_get(str(page_size), str(page), **kwargs)

    def get_short_customer_info_by_id(self, customer_id: CustomerId, **kwargs):
        return self.customer_controller.get_short_customer_info_by_id_using_get(customer_id.id, **kwargs)

    def get_tenant_customer(self, customer_title, **kwargs):
        return self.customer_controller.get_tenant_customer_using_get(customer_title, **kwargs)

    def save_customer(self, customer, **kwargs):
        return self.customer_controller.save_customer_using_post(customer, **kwargs)

    ##################################

    def check_updates(self, **kwargs):
        return self.admin_controller.check_updates_using_get(**kwargs)

    def get_admin_settings(self, key, **kwargs):
        return self.admin_controller.get_admin_settings_using_get(key, **kwargs)

    def get_security_settings(self, **kwargs):
        return self.admin_controller.get_security_settings_using_get(**kwargs)

    def save_admin_settings(self, admin_settings, **kwargs):
        return self.admin_controller.save_admin_settings_using_post(admin_settings, **kwargs)

    def save_security_settings(self, security_settings, **kwargs):
        return self.admin_controller.save_security_settings_using_post(security_settings, **kwargs)

    def send_test_mail(self, admin_settings, **kwargs):
        return self.admin_controller.send_test_mail_using_post(admin_settings, **kwargs)

    def send_test_sms(self, message, numberTo, providerConfiguration, **kwargs):
        return self.admin_controller.send_test_sms_using_post(message, numberTo, providerConfiguration, **kwargs)

    ##################################

    def find_by_query(self, query, **kwargs):
        if isinstance(query, DeviceSearchQuery):
            return self.device_controller.find_by_query_using_post1(query, **kwargs)
        elif isinstance(query, EntityViewSearchQuery):
            return self.entity_view_controller.find_by_query_using_post3(query, **kwargs)
        elif isinstance(query, AssetSearchQuery):
            return self.asset_controller.find_by_query_using_post(query, **kwargs)
        elif isinstance(query, EntityRelationsQuery):
            return self.entity_relation_controller.find_by_query_using_post2(query, **kwargs)

    def __load_controllers(self):
        self.admin_controller = AdminControllerApi(self.api_client)
        self.alarm_controller = AlarmControllerApi(self.api_client)
        self.asset_controller = AssetControllerApi(self.api_client)
        self.audit_log_controller = AuditLogControllerApi(self.api_client)
        self.auth_controller = AuthControllerApi(self.api_client)
        self.component_descriptor_controller = ComponentDescriptorControllerApi(self.api_client)
        self.customer_controller = CustomerControllerApi(self.api_client)
        self.dashboard_controller = DashboardControllerApi(self.api_client)
        self.device_api_controller = DeviceApiControllerApi(self.api_client)
        self.device_controller = DeviceControllerApi(self.api_client)
        self.device_profile_controller = DeviceProfileControllerApi(self.api_client)
        self.entity_query_controller = EntityQueryControllerApi(self.api_client)
        self.entity_relation_controller = EntityRelationControllerApi(self.api_client)
        self.entity_view_controller = EntityViewControllerApi(self.api_client)
        self.event_controller = EventControllerApi(self.api_client)
        self.o_auth_2_config_template_controller = OAuth2ConfigTemplateControllerApi(self.api_client)
        self.o_auth_2_controller = OAuth2ControllerApi(self.api_client)
        self.queue_controller = QueueControllerApi(self.api_client)
        self.rpc_controller = RpcControllerApi(self.api_client)
        self.rule_chain_controller = RuleChainControllerApi(self.api_client)
        self.telemetry_controller = TelemetryControllerApi(self.api_client)
        self.tenant_controller = TenantControllerApi(self.api_client)
        self.tenant_profile_controller = TenantProfileControllerApi(self.api_client)
        self.user_controller = UserControllerApi(self.api_client)
        self.widget_type_controller = WidgetTypeControllerApi(self.api_client)
        self.widgets_bundle_controller = WidgetsBundleControllerApi(self.api_client)

    @staticmethod
    def get_type(type):
        return type.entity_type if hasattr(type, "entity_type") else type

    @staticmethod
    def get_id(id):
        return id.id if hasattr(id, "id") else id
