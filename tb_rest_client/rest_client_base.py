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

from time import time, sleep
from typing import List

from requests import post
from threading import Thread
from logging import getLogger

from tb_rest_client.api.api_ce import *
from tb_rest_client.models.models_ce import *
from tb_rest_client.models.models_pe import *
from tb_rest_client.configuration import Configuration
from tb_rest_client.api_client import ApiClient

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

        token_json = post(self.base_url + "/api/auth/login", json={"username": username, "password": password},
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

    def delete_client_registration_template(self, client_registration_template_id: EntityId):
        client_registration_template_id = self.get_id(client_registration_template_id)
        return self.o_auth_2_config_template_controller.delete_client_registration_template_using_delete(client_registration_template_id=client_registration_template_id)

    def get_client_registration_templates(self, ):
        return self.o_auth_2_config_template_controller.get_client_registration_templates_using_get()

    def save_client_registration_template(self, body: OAuth2ClientRegistrationTemplate):
        return self.o_auth_2_config_template_controller.save_client_registration_template_using_post(body=body)

    def get_asset_types(self, ):
        return self.asset_controller.get_asset_types_using_get()

    def delete_asset(self, asset_id: AssetId):
        asset_id = self.get_id(asset_id)
        return self.asset_controller.delete_asset_using_delete(asset_id=asset_id)

    def get_customer_assets(self, customer_id: CustomerId, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
        return self.asset_controller.get_customer_assets_using_get(customer_id=customer_id, page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_tenant_asset(self, asset_name: str):
        return self.asset_controller.get_tenant_asset_using_get(asset_name=asset_name)

    def find_by_query(self, body: AssetSearchQuery):
        return self.asset_controller.find_by_query_using_post(body=body)

    def get_tenant_assets(self, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None):
        return self.asset_controller.get_tenant_assets_using_get(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_assets_by_ids(self, asset_ids: list):
        return self.asset_controller.get_assets_by_ids_using_get(asset_ids=asset_ids)

    def get_asset_by_id(self, asset_id: AssetId):
        asset_id = self.get_id(asset_id)
        return self.asset_controller.get_asset_by_id_using_get(asset_id=asset_id)

    def assign_rule_chain_to_edge(self, edge_id: EdgeId, rule_chain_id: RuleChainId):
        edge_id = self.get_id(edge_id)
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.assign_rule_chain_to_edge_using_post(edge_id=edge_id, rule_chain_id=rule_chain_id)

    def delete_rule_chain(self, rule_chain_id: RuleChainId):
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.delete_rule_chain_using_delete(rule_chain_id=rule_chain_id)

    def export_rule_chains(self, limit: str):
        return self.rule_chain_controller.export_rule_chains_using_get(limit=limit)

    def get_auto_assign_to_edge_rule_chains(self, ):
        return self.rule_chain_controller.get_auto_assign_to_edge_rule_chains_using_get()

    def get_edge_rule_chains(self, edge_id: EdgeId, page_size: str, page: str, text_search=None, sort_property=None, sort_order=None):
        edge_id = self.get_id(edge_id)
        return self.rule_chain_controller.get_edge_rule_chains_using_get(edge_id=edge_id, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_latest_rule_node_debug_input(self, rule_node_id: RuleNodeId):
        rule_node_id = self.get_id(rule_node_id)
        return self.rule_chain_controller.get_latest_rule_node_debug_input_using_get(rule_node_id=rule_node_id)

    def get_rule_chain_by_id(self, rule_chain_id: RuleChainId):
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.get_rule_chain_by_id_using_get(rule_chain_id=rule_chain_id)

    def get_rule_chain_meta_data(self, rule_chain_id: RuleChainId):
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.get_rule_chain_meta_data_using_get(rule_chain_id=rule_chain_id)

    def get_rule_chains(self, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None):
        return self.rule_chain_controller.get_rule_chains_using_get(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def import_rule_chains(self, body: RuleChainData, overwrite=None):
        return self.rule_chain_controller.import_rule_chains_using_post(body=body, overwrite=overwrite)

    def save_rule_chain_meta_data(self, body: RuleChainMetaData):
        return self.rule_chain_controller.save_rule_chain_meta_data_using_post(body=body)

    def save_rule_chain(self, body: DefaultRuleChainCreateRequest):
        return self.rule_chain_controller.save_rule_chain_using_post(body=body)

    def save_rule_chain_v1(self, body: RuleChain):
        return self.rule_chain_controller.save_rule_chain_using_post1(body=body)

    def set_auto_assign_to_edge_rule_chain(self, rule_chain_id: RuleChainId):
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.set_auto_assign_to_edge_rule_chain_using_post(rule_chain_id=rule_chain_id)

    def set_edge_template_root_rule_chain(self, rule_chain_id: RuleChainId):
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.set_edge_template_root_rule_chain_using_post(rule_chain_id=rule_chain_id)

    def set_root_rule_chain_v1(self, rule_chain_id: RuleChainId):
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.set_root_rule_chain_using_post1(rule_chain_id=rule_chain_id)

    def test_script(self, body: str):
        return self.rule_chain_controller.test_script_using_post(body=body)

    def unassign_rule_chain_from_edge(self, edge_id: EdgeId, rule_chain_id: RuleChainId):
        edge_id = self.get_id(edge_id)
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.unassign_rule_chain_from_edge_using_delete(edge_id=edge_id, rule_chain_id=rule_chain_id)

    def unset_auto_assign_to_edge_rule_chain(self, rule_chain_id: RuleChainId):
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.unset_auto_assign_to_edge_rule_chain_using_delete(rule_chain_id=rule_chain_id)

    def activate_user(self, body: str, send_activation_mail=None):
        return self.auth_controller.activate_user_using_post(body=body, send_activation_mail=send_activation_mail)

    def change_password(self, body: str):
        return self.auth_controller.change_password_using_post(body=body)

    def check_activate_token(self, activate_token: str):
        return self.auth_controller.check_activate_token_using_get(activate_token=activate_token)

    def check_reset_token(self, reset_token: str):
        return self.auth_controller.check_reset_token_using_get(reset_token=reset_token)

    def get_user_password_policy(self, ):
        return self.auth_controller.get_user_password_policy_using_get()

    def get_user(self, ):
        return self.auth_controller.get_user_using_get()

    def logout(self, ):
        return self.auth_controller.logout_using_post()

    def request_reset_password_by_email(self, body: str):
        return self.auth_controller.request_reset_password_by_email_using_post(body=body)

    def reset_password(self, body: str):
        return self.auth_controller.reset_password_using_post(body=body)

    def get_events_get(self, entity_type: str, entity_id: EntityId, event_type: str, tenant_id: TenantId, page_size: int, page: int, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None):
        entity_id = self.get_id(entity_id)
        tenant_id = self.get_id(tenant_id)
        return self.event_controller.get_events_using_get(entity_type=entity_type, entity_id=entity_id, event_type=event_type, tenant_id=tenant_id, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)

    def get_events_v1_get1(self, entity_type: str, entity_id: EntityId, tenant_id: TenantId, page_size: int, page: int, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None):
        entity_id = self.get_id(entity_id)
        tenant_id = self.get_id(tenant_id)
        return self.event_controller.get_events_using_get1(entity_type=entity_type, entity_id=entity_id, tenant_id=tenant_id, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)

    def get_events_post(self, body: EventFilter, tenant_id: TenantId, page_size: int, page: int, entity_type: str, entity_id: EntityId, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None):
        tenant_id = self.get_id(tenant_id)
        entity_id = self.get_id(entity_id)
        return self.event_controller.get_events_using_post(body=body, tenant_id=tenant_id, page_size=page_size, page=page, entity_type=entity_type, entity_id=entity_id, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)

    def delete_entity_attributes(self, device_id: DeviceId, scope: str, keys: str):
        device_id = self.get_id(device_id)
        return self.telemetry_controller.delete_entity_attributes_using_delete(device_id=device_id, scope=scope, keys=keys)

    def delete_entity_attributes_v1(self, entity_type: str, entity_id: EntityId, scope: str, keys: str):
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.delete_entity_attributes_using_delete1(entity_type=entity_type, entity_id=entity_id, scope=scope, keys=keys)

    def delete_entity_timeseries(self, entity_type: str, entity_id: EntityId, keys: str, delete_all_data_for_keys=None, start_ts=None, end_ts=None, rewrite_latest_if_deleted=None):
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.delete_entity_timeseries_using_delete(entity_type=entity_type, entity_id=entity_id, keys=keys, delete_all_data_for_keys=delete_all_data_for_keys, start_ts=start_ts, end_ts=end_ts, rewrite_latest_if_deleted=rewrite_latest_if_deleted)

    def get_attribute_keys_by_scope(self, entity_type: str, entity_id: EntityId, scope: str):
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.get_attribute_keys_by_scope_using_get(entity_type=entity_type, entity_id=entity_id, scope=scope)

    def get_attribute_keys(self, entity_type: str, entity_id: EntityId):
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.get_attribute_keys_using_get(entity_type=entity_type, entity_id=entity_id)

    def get_attributes_by_scope(self, entity_type: str, entity_id: EntityId, scope: str, keys=None):
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.get_attributes_by_scope_using_get(entity_type=entity_type, entity_id=entity_id, scope=scope, keys=keys)

    def get_attributes(self, entity_type: str, entity_id: EntityId, keys=None):
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.get_attributes_using_get(entity_type=entity_type, entity_id=entity_id, keys=keys)

    def get_latest_timeseries(self, entity_type: str, entity_id: EntityId, keys=None, use_strict_data_types=None):
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.get_latest_timeseries_using_get(entity_type=entity_type, entity_id=entity_id, keys=keys, use_strict_data_types=use_strict_data_types)

    def get_timeseries_keys_v1(self, entity_type: str, entity_id: EntityId):
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.get_timeseries_keys_using_get1(entity_type=entity_type, entity_id=entity_id)

    def get_timeseries(self, entity_type: str, entity_id: EntityId, keys: str, start_ts: str, end_ts: str, interval=None, limit=None, agg=None, order_by=None, use_strict_data_types=None):
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.get_timeseries_using_get(entity_type=entity_type, entity_id=entity_id, keys=keys, start_ts=start_ts, end_ts=end_ts, interval=interval, limit=limit, agg=agg, order_by=order_by, use_strict_data_types=use_strict_data_types)

    def save_device_attributes(self, body: str, device_id: DeviceId, scope: str):
        device_id = self.get_id(device_id)
        return self.telemetry_controller.save_device_attributes_using_post(body=body, device_id=device_id, scope=scope)

    def save_entity_attributes_v1(self, body: str, entity_type: str, entity_id: EntityId, scope: str):
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.save_entity_attributes_v1_using_post(body=body, entity_type=entity_type, entity_id=entity_id, scope=scope)

    def save_entity_attributes_v2(self, body: str, entity_type: str, entity_id: EntityId, scope: str):
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.save_entity_attributes_v2_using_post(body=body, entity_type=entity_type, entity_id=entity_id, scope=scope)

    def save_entity_telemetry(self, body: str, entity_type: str, entity_id: EntityId, scope: str):
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.save_entity_telemetry_using_post(body=body, entity_type=entity_type, entity_id=entity_id, scope=scope)

    def save_entity_telemetry_with_ttl(self, body: str, entity_type: str, entity_id: EntityId, scope: str, ttl: int):
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.save_entity_telemetry_with_ttl_using_post(body=body, entity_type=entity_type, entity_id=entity_id, scope=scope, ttl=ttl)

    def ack_alarm(self, alarm_id: AlarmId):
        alarm_id = self.get_id(alarm_id)
        return self.alarm_controller.ack_alarm_using_post(alarm_id=alarm_id)

    def clear_alarm(self, alarm_id: AlarmId):
        alarm_id = self.get_id(alarm_id)
        return self.alarm_controller.clear_alarm_using_post(alarm_id=alarm_id)

    def delete_alarm(self, alarm_id: AlarmId):
        alarm_id = self.get_id(alarm_id)
        return self.alarm_controller.delete_alarm_using_delete(alarm_id=alarm_id)

    def get_alarm_by_id(self, alarm_id: AlarmId):
        alarm_id = self.get_id(alarm_id)
        return self.alarm_controller.get_alarm_by_id_using_get(alarm_id=alarm_id)

    def get_alarm_info_by_id(self, alarm_id: AlarmId):
        alarm_id = self.get_id(alarm_id)
        return self.alarm_controller.get_alarm_info_by_id_using_get(alarm_id=alarm_id)

    def get_alarms(self, entity_type: str, entity_id: EntityId, page_size: int, page: int, search_status=None, status=None, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None, fetch_originator=None):
        entity_id = self.get_id(entity_id)
        return self.alarm_controller.get_alarms_using_get(entity_type=entity_type, entity_id=entity_id, page_size=page_size, page=page, search_status=search_status, status=status, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time, fetch_originator=fetch_originator)

    def get_all_alarms(self, page_size: int, page: int, search_status=None, status=None, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None, fetch_originator=None):
        return self.alarm_controller.get_all_alarms_using_get(page_size=page_size, page=page, search_status=search_status, status=status, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time, fetch_originator=fetch_originator)

    def get_highest_alarm_severity(self, entity_type: str, entity_id: EntityId, search_status=None, status=None):
        entity_id = self.get_id(entity_id)
        return self.alarm_controller.get_highest_alarm_severity_using_get(entity_type=entity_type, entity_id=entity_id, search_status=search_status, status=status)

    def save_alarm(self, body: Alarm):
        return self.alarm_controller.save_alarm_using_post(body=body)

    def sync_edge(self, edge_id: EdgeId):
        edge_id = self.get_id(edge_id)
        return self.edge_controller.sync_edge_using_post(edge_id=edge_id)

    def get_customer_edges(self, customer_id: CustomerId, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
        return self.edge_controller.get_customer_edges_using_get(customer_id=customer_id, page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_edge_types(self, ):
        return self.edge_controller.get_edge_types_using_get()

    def get_tenant_edge(self, edge_name: str):
        return self.edge_controller.get_tenant_edge_using_get(edge_name=edge_name)

    def check_instance(self, body: object):
        return self.edge_controller.check_instance_using_post(body=body)

    def find_by_query_v2(self, body: EdgeSearchQuery):
        return self.edge_controller.find_by_query_using_post2(body=body)

    def delete_edge(self, edge_id: EdgeId):
        edge_id = self.get_id(edge_id)
        return self.edge_controller.delete_edge_using_delete(edge_id=edge_id)

    def get_edges(self, page_size: str, page: str, text_search=None, sort_property=None, sort_order=None):
        return self.edge_controller.get_edges_using_get(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def is_edges_support_enabled(self, ):
        return self.edge_controller.is_edges_support_enabled_using_get()

    def get_edges_by_ids(self, edge_ids: list):
        return self.edge_controller.get_edges_by_ids_using_get(edge_ids=edge_ids)

    def find_missing_to_related_rule_chains(self, edge_id: EdgeId):
        edge_id = self.get_id(edge_id)
        return self.edge_controller.find_missing_to_related_rule_chains_using_get(edge_id=edge_id)

    def set_root_rule_chain(self, edge_id: EdgeId, rule_chain_id: RuleChainId):
        edge_id = self.get_id(edge_id)
        rule_chain_id = self.get_id(rule_chain_id)
        return self.edge_controller.set_root_rule_chain_using_post(edge_id=edge_id, rule_chain_id=rule_chain_id)

    def get_edge_by_id(self, edge_id: EdgeId):
        edge_id = self.get_id(edge_id)
        return self.edge_controller.get_edge_by_id_using_get(edge_id=edge_id)

    def get_tenant_edges(self, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None):
        return self.edge_controller.get_tenant_edges_using_get(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def activate_instance(self, license_secret: str, release_date: str):
        return self.edge_controller.activate_instance_using_post(license_secret=license_secret, release_date=release_date)

    def get_persisted_rpc(self, rpc_id: RpcId):
        rpc_id = self.get_id(rpc_id)
        return self.rpc_v_2_controller.get_persisted_rpc_using_get(rpc_id=rpc_id)

    def handle_two_way_device_rpc_request_v1(self, body: str, device_id: DeviceId):
        device_id = self.get_id(device_id)
        return self.rpc_v_2_controller.handle_two_way_device_rpc_request_using_post1(body=body, device_id=device_id)

    def delete_resource(self, rpc_id: RpcId):
        rpc_id = self.get_id(rpc_id)
        return self.rpc_v_2_controller.delete_resource_using_delete(rpc_id=rpc_id)

    def handle_one_way_device_rpc_request_v1(self, body: str, device_id: DeviceId):
        device_id = self.get_id(device_id)
        return self.rpc_v_2_controller.handle_one_way_device_rpc_request_using_post1(body=body, device_id=device_id)

    def get_persisted_rpc_by_device(self, device_id: DeviceId, page_size: int, page: int, rpc_status: str, text_search=None, sort_property=None, sort_order=None):
        device_id = self.get_id(device_id)
        return self.rpc_v_2_controller.get_persisted_rpc_by_device_using_get(device_id=device_id, page_size=page_size, page=page, rpc_status=rpc_status, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def delete_customer(self, customer_id: CustomerId):
        customer_id = self.get_id(customer_id)
        return self.customer_controller.delete_customer_using_delete(customer_id=customer_id)

    def get_customer_by_id(self, customer_id: CustomerId):
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_customer_by_id_using_get(customer_id=customer_id)

    def get_short_customer_info_by_id(self, customer_id: CustomerId):
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_short_customer_info_by_id_using_get(customer_id=customer_id)

    def get_customers(self, page_size: str, page: str, text_search=None, sort_property=None, sort_order=None):
        return self.customer_controller.get_customers_using_get(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_customer_title_by_id(self, customer_id: CustomerId):
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_customer_title_by_id_using_get(customer_id=customer_id)

    def get_tenant_customer(self, customer_title: str):
        return self.customer_controller.get_tenant_customer_using_get(customer_title=customer_title)

    def send_activation_email(self, email: str):
        return self.user_controller.send_activation_email_using_post(email=email)

    def get_user_by_id(self, user_id: UserId):
        user_id = self.get_id(user_id)
        return self.user_controller.get_user_by_id_using_get(user_id=user_id)

    def set_user_credentials_enabled(self, user_id: UserId, user_credentials_enabled=None):
        user_id = self.get_id(user_id)
        return self.user_controller.set_user_credentials_enabled_using_post(user_id=user_id, user_credentials_enabled=user_credentials_enabled)

    def get_tenant_admins(self, tenant_id: TenantId, page_size: str, page: str, text_search=None, sort_property=None, sort_order=None):
        tenant_id = self.get_id(tenant_id)
        return self.user_controller.get_tenant_admins_using_get(tenant_id=tenant_id, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_customer_users(self, customer_id: CustomerId, page_size: str, page: str, text_search=None, sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
        return self.user_controller.get_customer_users_using_get(customer_id=customer_id, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_user_token(self, user_id: UserId):
        user_id = self.get_id(user_id)
        return self.user_controller.get_user_token_using_get(user_id=user_id)

    def get_activation_link(self, user_id: UserId):
        user_id = self.get_id(user_id)
        return self.user_controller.get_activation_link_using_get(user_id=user_id)

    def delete_user(self, user_id: UserId):
        user_id = self.get_id(user_id)
        return self.user_controller.delete_user_using_delete(user_id=user_id)

    def is_user_token_access_enabled(self, ):
        return self.user_controller.is_user_token_access_enabled_using_get()

    def get_tenant_queues_by_service_type(self, service_type: str):
        return self.queue_controller.get_tenant_queues_by_service_type_using_get(service_type=service_type)

    def handle_one_way_device_rpc_request(self, body: str, device_id: DeviceId):
        device_id = self.get_id(device_id)
        return self.rpc_v_1_controller.handle_one_way_device_rpc_request_using_post(body=body, device_id=device_id)

    def handle_two_way_device_rpc_request(self, body: str, device_id: DeviceId):
        device_id = self.get_id(device_id)
        return self.rpc_v_1_controller.handle_two_way_device_rpc_request_using_post(body=body, device_id=device_id)

    def get_tenant_devices(self, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None):
        return self.device_controller.get_tenant_devices_using_get(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_tenant_device(self, device_name: str):
        return self.device_controller.get_tenant_device_using_get(device_name=device_name)

    def delete_device(self, device_id: DeviceId):
        device_id = self.get_id(device_id)
        return self.device_controller.delete_device_using_delete(device_id=device_id)

    def re_claim_device(self, device_name: str):
        return self.device_controller.re_claim_device_using_delete(device_name=device_name)

    def count_by_device_profile_and_empty_ota_package(self, ota_package_type: str, device_profile_id: DeviceProfileId):
        device_profile_id = self.get_id(device_profile_id)
        return self.device_controller.count_by_device_profile_and_empty_ota_package_using_get(ota_package_type=ota_package_type, device_profile_id=device_profile_id)

    def get_device_credentials_by_device_id(self, device_id: DeviceId):
        device_id = self.get_id(device_id)
        return self.device_controller.get_device_credentials_by_device_id_using_get(device_id=device_id)

    def find_by_query_v1(self, body: DeviceSearchQuery):
        return self.device_controller.find_by_query_using_post1(body=body)

    def assign_device_to_tenant(self, tenant_id: TenantId, device_id: DeviceId):
        tenant_id = self.get_id(tenant_id)
        device_id = self.get_id(device_id)
        return self.device_controller.assign_device_to_tenant_using_post(tenant_id=tenant_id, device_id=device_id)

    def get_device_types(self, ):
        return self.device_controller.get_device_types_using_get()

    def get_device_by_id(self, device_id: DeviceId):
        device_id = self.get_id(device_id)
        return self.device_controller.get_device_by_id_using_get(device_id=device_id)

    def get_devices_by_ids(self, device_ids: list):
        return self.device_controller.get_devices_by_ids_using_get(device_ids=device_ids)

    def get_customer_devices(self, customer_id: CustomerId, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
        return self.device_controller.get_customer_devices_using_get(customer_id=customer_id, page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def save_device_credentials(self, body: DeviceCredentials):
        return self.device_controller.save_device_credentials_using_post(body=body)

    def delete_relation(self, from_id: EntityId, from_type: str, relation_type: str, to_id: EntityId, to_type: str, relation_type_group=None):
        from_id = self.get_id(from_id)
        to_id = self.get_id(to_id)
        return self.entity_relation_controller.delete_relation_using_delete(from_id=from_id, from_type=from_type, relation_type=relation_type, to_id=to_id, to_type=to_type, relation_type_group=relation_type_group)

    def delete_relations(self, entity_id: EntityId, entity_type: str, id: str, type: str):
        entity_id = self.get_id(entity_id)
        return self.entity_relation_controller.delete_relations_using_delete(entity_id=entity_id, entity_type=entity_type, id=id, type=type)

    def find_by_from(self, from_id: EntityId, from_type: str, relation_type: str, relation_type_group=None):
        from_id = self.get_id(from_id)
        return self.entity_relation_controller.find_by_from_using_get(from_id=from_id, from_type=from_type, relation_type=relation_type, relation_type_group=relation_type_group)

    def find_by_from_v1(self, from_id: EntityId, from_type: str, relation_type_group=None):
        from_id = self.get_id(from_id)
        return self.entity_relation_controller.find_by_from_using_get1(from_id=from_id, from_type=from_type, relation_type_group=relation_type_group)

    def find_by_query_v3(self, body: EntityRelationsQuery):
        return self.entity_relation_controller.find_by_query_using_post3(body=body)

    def find_by_to(self, to_id: EntityId, to_type: str, relation_type: str, relation_type_group=None):
        to_id = self.get_id(to_id)
        return self.entity_relation_controller.find_by_to_using_get(to_id=to_id, to_type=to_type, relation_type=relation_type, relation_type_group=relation_type_group)

    def find_by_to_v1(self, to_id: EntityId, to_type: str, relation_type_group=None):
        to_id = self.get_id(to_id)
        return self.entity_relation_controller.find_by_to_using_get1(to_id=to_id, to_type=to_type, relation_type_group=relation_type_group)

    def find_info_by_from(self, from_id: EntityId, from_type: str, relation_type_group=None):
        from_id = self.get_id(from_id)
        return self.entity_relation_controller.find_info_by_from_using_get(from_id=from_id, from_type=from_type, relation_type_group=relation_type_group)

    def find_info_by_query(self, body: EntityRelationsQuery):
        return self.entity_relation_controller.find_info_by_query_using_post(body=body)

    def find_info_by_to(self, to_id: EntityId, to_type: str, relation_type_group=None):
        to_id = self.get_id(to_id)
        return self.entity_relation_controller.find_info_by_to_using_get(to_id=to_id, to_type=to_type, relation_type_group=relation_type_group)

    def get_relation(self, from_id: EntityId, from_type: str, relation_type: str, to_id: EntityId, to_type: str, relation_type_group=None):
        from_id = self.get_id(from_id)
        to_id = self.get_id(to_id)
        return self.entity_relation_controller.get_relation_using_get(from_id=from_id, from_type=from_type, relation_type=relation_type, to_id=to_id, to_type=to_type, relation_type_group=relation_type_group)

    def save_relation(self, body: EntityRelation):
        return self.entity_relation_controller.save_relation_using_post(body=body)

    def delete_entity_view(self, entity_view_id: EntityViewId):
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.delete_entity_view_using_delete(entity_view_id=entity_view_id)

    def get_tenant_entity_view(self, entity_view_name: str):
        return self.entity_view_controller.get_tenant_entity_view_using_get(entity_view_name=entity_view_name)

    def get_tenant_entity_views(self, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None):
        return self.entity_view_controller.get_tenant_entity_views_using_get(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_entity_view_types(self, ):
        return self.entity_view_controller.get_entity_view_types_using_get()

    def get_customer_entity_views(self, customer_id: CustomerId, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
        return self.entity_view_controller.get_customer_entity_views_using_get(customer_id=customer_id, page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def find_by_query_v4(self, body: EntityViewSearchQuery):
        return self.entity_view_controller.find_by_query_using_post4(body=body)

    def get_entity_view_by_id(self, entity_view_id: EntityViewId):
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.get_entity_view_by_id_using_get(entity_view_id=entity_view_id)

    def check_updates(self, ):
        return self.admin_controller.check_updates_using_get()

    def get_security_settings(self, ):
        return self.admin_controller.get_security_settings_using_get()

    def save_admin_settings(self, body: AdminSettings):
        return self.admin_controller.save_admin_settings_using_post(body=body)

    def send_test_sms(self, body: TestSmsRequest):
        return self.admin_controller.send_test_sms_using_post(body=body)

    def send_test_mail(self, body: AdminSettings):
        return self.admin_controller.send_test_mail_using_post(body=body)

    def save_security_settings(self, body: SecuritySettings):
        return self.admin_controller.save_security_settings_using_post(body=body)

    def sign_up(self, body: SignUpRequest):
        return self.sign_up_controller.sign_up_using_post(body=body)

    def privacy_policy_accepted(self, ):
        return self.sign_up_controller.privacy_policy_accepted_using_get()

    def get_recaptcha_public_key(self, ):
        return self.sign_up_controller.get_recaptcha_public_key_using_get()

    def accept_privacy_policy(self, ):
        return self.sign_up_controller.accept_privacy_policy_using_post()

    def delete_tenant_account(self, ):
        return self.sign_up_controller.delete_tenant_account_using_delete()

    def delete_resource_v1(self, resource_id: EntityId):
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.delete_resource_using_delete1(resource_id=resource_id)

    def download_resource(self, resource_id: EntityId):
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.download_resource_using_get(resource_id=resource_id)

    def get_lwm2m_list_objects_page(self, page_size: int, page: int, text_search=None, sort_property=None, sort_order=None):
        return self.tb_resource_controller.get_lwm2m_list_objects_page_using_get(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_lwm2m_list_objects(self, sort_order: str, sort_property: str, object_ids=None):
        return self.tb_resource_controller.get_lwm2m_list_objects_using_get(sort_order=sort_order, sort_property=sort_property, object_ids=object_ids)

    def get_resource_by_id(self, resource_id: EntityId):
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.get_resource_by_id_using_get(resource_id=resource_id)

    def get_resource_info_by_id(self, resource_id: EntityId):
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.get_resource_info_by_id_using_get(resource_id=resource_id)

    def get_resources(self, page_size: int, page: int, text_search=None, sort_property=None, sort_order=None):
        return self.tb_resource_controller.get_resources_using_get(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def save_resource(self, body: TbResource):
        return self.tb_resource_controller.save_resource_using_post(body=body)

    def get_current_o_auth2_info(self, ):
        return self.o_auth_2_controller.get_current_o_auth2_info_using_get()

    def get_login_processing_url(self, ):
        return self.o_auth_2_controller.get_login_processing_url_using_get()

    def get_o_auth2_clients(self, pkg_name=None, platform=None):
        return self.o_auth_2_controller.get_o_auth2_clients_using_post(pkg_name=pkg_name, platform=platform)

    def save_o_auth2_info(self, body: OAuth2Info):
        return self.o_auth_2_controller.save_o_auth2_info_using_post(body=body)

    def delete_tenant_profile(self, tenant_profile_id: TenantProfileId):
        tenant_profile_id = self.get_id(tenant_profile_id)
        return self.tenant_profile_controller.delete_tenant_profile_using_delete(tenant_profile_id=tenant_profile_id)

    def get_default_tenant_profile_info(self, ):
        return self.tenant_profile_controller.get_default_tenant_profile_info_using_get()

    def get_tenant_profile_by_id(self, tenant_profile_id: TenantProfileId):
        tenant_profile_id = self.get_id(tenant_profile_id)
        return self.tenant_profile_controller.get_tenant_profile_by_id_using_get(tenant_profile_id=tenant_profile_id)

    def get_tenant_profile_info_by_id(self, tenant_profile_id: TenantProfileId):
        tenant_profile_id = self.get_id(tenant_profile_id)
        return self.tenant_profile_controller.get_tenant_profile_info_by_id_using_get(tenant_profile_id=tenant_profile_id)

    def get_tenant_profile_infos(self, page_size: str, page: str, text_search=None, sort_property=None, sort_order=None):
        return self.tenant_profile_controller.get_tenant_profile_infos_using_get(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_tenant_profiles(self, page_size: str, page: str, text_search=None, sort_property=None, sort_order=None):
        return self.tenant_profile_controller.get_tenant_profiles_using_get(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def save_tenant_profile(self, body: TenantProfile):
        return self.tenant_profile_controller.save_tenant_profile_using_post(body=body)

    def set_default_tenant_profile(self, tenant_profile_id: TenantProfileId):
        tenant_profile_id = self.get_id(tenant_profile_id)
        return self.tenant_profile_controller.set_default_tenant_profile_using_post(tenant_profile_id=tenant_profile_id)

    def delete_widgets_bundle(self, widgets_bundle_id: WidgetsBundleId):
        widgets_bundle_id = self.get_id(widgets_bundle_id)
        return self.widgets_bundle_controller.delete_widgets_bundle_using_delete(widgets_bundle_id=widgets_bundle_id)

    def get_widgets_bundle_by_id(self, widgets_bundle_id: WidgetsBundleId):
        widgets_bundle_id = self.get_id(widgets_bundle_id)
        return self.widgets_bundle_controller.get_widgets_bundle_by_id_using_get(widgets_bundle_id=widgets_bundle_id)

    def get_widgets_bundles(self, page_size: str, page: str, text_search=None, sort_property=None, sort_order=None):
        return self.widgets_bundle_controller.get_widgets_bundles_using_get(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_widgets_bundles_v1(self, ):
        return self.widgets_bundle_controller.get_widgets_bundles_using_get1()

    def save_widgets_bundle(self, body: WidgetsBundle):
        return self.widgets_bundle_controller.save_widgets_bundle_using_post(body=body)

    def delete_device_profile(self, device_profile_id: DeviceProfileId):
        device_profile_id = self.get_id(device_profile_id)
        return self.device_profile_controller.delete_device_profile_using_delete(device_profile_id=device_profile_id)

    def get_attributes_keys(self, device_profile_id=None):
        device_profile_id = self.get_id(device_profile_id)
        return self.device_profile_controller.get_attributes_keys_using_get(device_profile_id=device_profile_id)

    def get_default_device_profile_info(self, ):
        return self.device_profile_controller.get_default_device_profile_info_using_get()

    def get_device_profile_by_id(self, device_profile_id: DeviceProfileId):
        device_profile_id = self.get_id(device_profile_id)
        return self.device_profile_controller.get_device_profile_by_id_using_get(device_profile_id=device_profile_id)

    def get_device_profile_info_by_id(self, device_profile_id: DeviceProfileId):
        device_profile_id = self.get_id(device_profile_id)
        return self.device_profile_controller.get_device_profile_info_by_id_using_get(device_profile_id=device_profile_id)

    def get_device_profile_infos(self, page_size: str, page: str, text_search=None, sort_property=None, sort_order=None, transport_type=None):
        return self.device_profile_controller.get_device_profile_infos_using_get(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, transport_type=transport_type)

    def get_device_profiles(self, page_size: str, page: str, text_search=None, sort_property=None, sort_order=None):
        return self.device_profile_controller.get_device_profiles_using_get(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_timeseries_keys(self, device_profile_id=None):
        device_profile_id = self.get_id(device_profile_id)
        return self.device_profile_controller.get_timeseries_keys_using_get(device_profile_id=device_profile_id)

    def save_device_profile(self, body: DeviceProfile):
        return self.device_profile_controller.save_device_profile_using_post(body=body)

    def set_default_device_profile(self, device_profile_id: DeviceProfileId):
        device_profile_id = self.get_id(device_profile_id)
        return self.device_profile_controller.set_default_device_profile_using_post(device_profile_id=device_profile_id)

    def get_tenant_dashboards(self, page_size: str, page: str, mobile=None, text_search=None, sort_property=None, sort_order=None):
        return self.dashboard_controller.get_tenant_dashboards_using_get(page_size=page_size, page=page, mobile=mobile, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def delete_dashboard(self, dashboard_id: DashboardId):
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.delete_dashboard_using_delete(dashboard_id=dashboard_id)

    def get_dashboard_by_id(self, dashboard_id: DashboardId):
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.get_dashboard_by_id_using_get(dashboard_id=dashboard_id)

    def set_tenant_home_dashboard_info(self, body: HomeDashboardInfo):
        return self.dashboard_controller.set_tenant_home_dashboard_info_using_post(body=body)

    def get_server_time(self, ):
        return self.dashboard_controller.get_server_time_using_get()

    def get_home_dashboard_info(self, ):
        return self.dashboard_controller.get_home_dashboard_info_using_get()

    def get_max_datapoints_limit(self, ):
        return self.dashboard_controller.get_max_datapoints_limit_using_get()

    def get_home_dashboard(self, ):
        return self.dashboard_controller.get_home_dashboard_using_get()

    def get_tenant_home_dashboard_info(self, ):
        return self.dashboard_controller.get_tenant_home_dashboard_info_using_get()

    def get_dashboard_info_by_id(self, dashboard_id: DashboardId):
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.get_dashboard_info_by_id_using_get(dashboard_id=dashboard_id)

    def get_tenant_dashboards_v1(self, tenant_id: TenantId, page_size: str, page: str, text_search=None, sort_property=None, sort_order=None):
        tenant_id = self.get_id(tenant_id)
        return self.dashboard_controller.get_tenant_dashboards_using_get1(tenant_id=tenant_id, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def count_entities_by_query(self, body: EntityCountQuery):
        return self.entity_query_controller.count_entities_by_query_using_post(body=body)

    def find_alarm_data_by_query(self, body: AlarmDataQuery):
        return self.entity_query_controller.find_alarm_data_by_query_using_post(body=body)

    def find_entity_data_by_query(self, body: EntityDataQuery):
        return self.entity_query_controller.find_entity_data_by_query_using_post(body=body)

    def find_entity_timeseries_and_attributes_keys_by_query(self, body: EntityDataQuery, timeseries: bool, attributes: bool):
        return self.entity_query_controller.find_entity_timeseries_and_attributes_keys_by_query_using_post(body=body, timeseries=timeseries, attributes=attributes)

    def delete_widget_type(self, widget_type_id: WidgetTypeId):
        widget_type_id = self.get_id(widget_type_id)
        return self.widget_type_controller.delete_widget_type_using_delete(widget_type_id=widget_type_id)

    def get_bundle_widget_types_details(self, is_system: str, bundle_alias: str):
        return self.widget_type_controller.get_bundle_widget_types_details_using_get(is_system=is_system, bundle_alias=bundle_alias)

    def get_bundle_widget_types_infos(self, is_system: str, bundle_alias: str):
        return self.widget_type_controller.get_bundle_widget_types_infos_using_get(is_system=is_system, bundle_alias=bundle_alias)

    def get_bundle_widget_types(self, is_system: str, bundle_alias: str):
        return self.widget_type_controller.get_bundle_widget_types_using_get(is_system=is_system, bundle_alias=bundle_alias)

    def get_widget_type_by_id(self, widget_type_id: WidgetTypeId):
        widget_type_id = self.get_id(widget_type_id)
        return self.widget_type_controller.get_widget_type_by_id_using_get(widget_type_id=widget_type_id)

    def get_widget_type(self, is_system: str, bundle_alias: str, alias: str):
        return self.widget_type_controller.get_widget_type_using_get(is_system=is_system, bundle_alias=bundle_alias, alias=alias)

    def save_widget_type(self, body: WidgetTypeDetails):
        return self.widget_type_controller.save_widget_type_using_post(body=body)

    def get_audit_logs_by_customer_id(self, customer_id: CustomerId, page_size: str, page: str, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None, action_types=None):
        customer_id = self.get_id(customer_id)
        return self.audit_log_controller.get_audit_logs_by_customer_id_using_get(customer_id=customer_id, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time, action_types=action_types)

    def get_audit_logs_by_entity_id(self, entity_type: str, entity_id: EntityId, page_size: str, page: str, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None, action_types=None):
        entity_id = self.get_id(entity_id)
        return self.audit_log_controller.get_audit_logs_by_entity_id_using_get(entity_type=entity_type, entity_id=entity_id, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time, action_types=action_types)

    def get_audit_logs_by_user_id(self, user_id: UserId, page_size: str, page: str, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None, action_types=None):
        user_id = self.get_id(user_id)
        return self.audit_log_controller.get_audit_logs_by_user_id_using_get(user_id=user_id, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time, action_types=action_types)

    def get_audit_logs(self, page_size: str, page: str, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None, action_types=None):
        return self.audit_log_controller.get_audit_logs_using_get(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time, action_types=action_types)

    def get_lwm2m_bootstrap_security_info(self, is_bootstrap_server: bool):
        return self.lwm_2m_controller.get_lwm2m_bootstrap_security_info_using_get(is_bootstrap_server=is_bootstrap_server)

    def get_component_descriptor_by_clazz(self, component_descriptor_clazz: str):
        return self.component_descriptor_controller.get_component_descriptor_by_clazz_using_get(component_descriptor_clazz=component_descriptor_clazz)

    def get_component_descriptors_by_type(self, component_type: str, rule_chain_type=None):
        return self.component_descriptor_controller.get_component_descriptors_by_type_using_get(component_type=component_type, rule_chain_type=rule_chain_type)

    def get_component_descriptors_by_types(self, component_types: str, rule_chain_type=None):
        return self.component_descriptor_controller.get_component_descriptors_by_types_using_get(component_types=component_types, rule_chain_type=rule_chain_type)

    def get_tenants(self, page_size: str, page: str, text_search=None, sort_property=None, sort_order=None):
        return self.tenant_controller.get_tenants_using_get(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_tenant_info_by_id(self, tenant_id: TenantId):
        tenant_id = self.get_id(tenant_id)
        return self.tenant_controller.get_tenant_info_by_id_using_get(tenant_id=tenant_id)

    def delete_tenant(self, tenant_id: TenantId):
        tenant_id = self.get_id(tenant_id)
        return self.tenant_controller.delete_tenant_using_delete(tenant_id=tenant_id)

    def save_tenant(self, body: Tenant):
        return self.tenant_controller.save_tenant_using_post(body=body)

    def get_tenant_infos(self, page_size: str, page: str, text_search=None, sort_property=None, sort_order=None):
        return self.tenant_controller.get_tenant_infos_using_get(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_tenant_by_id(self, tenant_id: TenantId):
        tenant_id = self.get_id(tenant_id)
        return self.tenant_controller.get_tenant_by_id_using_get(tenant_id=tenant_id)

    def save_ota_package_data(self, file: str, checksum_algorithm: str, ota_package_id: OtaPackageId, checksum=None):
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.save_ota_package_data_using_post(file=file, checksum_algorithm=checksum_algorithm, ota_package_id=ota_package_id, checksum=checksum)

    def save_ota_package_info(self, body: SaveOtaPackageInfoRequest):
        return self.ota_package_controller.save_ota_package_info_using_post(body=body)

    def download_ota_package(self, ota_package_id: OtaPackageId):
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.download_ota_package_using_get(ota_package_id=ota_package_id)

    def get_ota_package_info_by_id(self, ota_package_id: OtaPackageId):
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.get_ota_package_info_by_id_using_get(ota_package_id=ota_package_id)

    def delete_ota_package(self, ota_package_id: OtaPackageId):
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.delete_ota_package_using_delete(ota_package_id=ota_package_id)

    def get_ota_package_by_id(self, ota_package_id: OtaPackageId):
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.get_ota_package_by_id_using_get(ota_package_id=ota_package_id)

    def get_ota_packages(self, device_profile_id: DeviceProfileId, type: str, page_size: int, page: int, text_search=None, sort_property=None, sort_order=None):
        device_profile_id = self.get_id(device_profile_id)
        return self.ota_package_controller.get_ota_packages_using_get(device_profile_id=device_profile_id, type=type, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_ota_packages_v1(self, page_size: int, page: int, text_search=None, sort_property=None, sort_order=None):
        return self.ota_package_controller.get_ota_packages_using_get1(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)


    def __load_controllers(self):
        self.audit_log_controller = AuditLogControllerApi(self.api_client)
        self.o_auth2_config_template_controller = OAuth2ConfigTemplateControllerApi(self.api_client)
        self.entity_view_controller = EntityViewControllerApi(self.api_client)
        self.entity_query_controller = EntityQueryControllerApi(self.api_client)
        self.o_auth2_controller = OAuth2ControllerApi(self.api_client)
        self.entity_relation_controller = EntityRelationControllerApi(self.api_client)
        self.rpc_v2_controller = RpcV2ControllerApi(self.api_client)
        self.edge_controller = EdgeControllerApi(self.api_client)
        self.admin_controller = AdminControllerApi(self.api_client)
        self.user_controller = UserControllerApi(self.api_client)
        self.asset_controller = AssetControllerApi(self.api_client)
        self.widgets_bundle_controller = WidgetsBundleControllerApi(self.api_client)
        self.tenant_profile_controller = TenantProfileControllerApi(self.api_client)
        self.event_controller = EventControllerApi(self.api_client)
        self.lwm2m_controller = Lwm2mControllerApi(self.api_client)
        self.dashboard_controller = DashboardControllerApi(self.api_client)
        self.component_descriptor_controller = ComponentDescriptorControllerApi(self.api_client)
        self.device_profile_controller = DeviceProfileControllerApi(self.api_client)
        self.customer_controller = CustomerControllerApi(self.api_client)
        self.telemetry_controller = TelemetryControllerApi(self.api_client)
        self.tenant_controller = TenantControllerApi(self.api_client)
        self.rpc_v1_controller = RpcV1ControllerApi(self.api_client)
        self.widget_type_controller = WidgetTypeControllerApi(self.api_client)
        self.device_controller = DeviceControllerApi(self.api_client)
        self.rule_chain_controller = RuleChainControllerApi(self.api_client)
        self.tb_resource_controller = TbResourceControllerApi(self.api_client)
        self.auth_controller = AuthControllerApi(self.api_client)
        self.queue_controller = QueueControllerApi(self.api_client)
        self.ota_package_controller = OtaPackageControllerApi(self.api_client)
        self.alarm_controller = AlarmControllerApi(self.api_client)
        self.edge_event_controller = EdgeEventControllerApi(self.api_client)
        self.sign_up_controller = SignUpControllerApi(self.api_client)

    @staticmethod
    def get_type(type):
        return type.entity_type if hasattr(type, "entity_type") else type


    @staticmethod
    def get_id(id):
        return id.id if hasattr(id, "id") else id
