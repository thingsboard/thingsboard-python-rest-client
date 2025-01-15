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


import jwt
from time import time, sleep

from requests import post
from threading import Thread
from logging import getLogger

from typing import List, Optional, Union, Any, Dict

from tb_rest_client.models.models_ce import *
from tb_rest_client.rest import RESTResponse
from tb_rest_client.api.api_ce.two_factor_auth_controller_api import TwoFactorAuthControllerApi
from tb_rest_client.api.api_ce.entities_version_control_controller_api import EntitiesVersionControlControllerApi
from tb_rest_client.api.api_ce.admin_controller_api import AdminControllerApi
from tb_rest_client.api.api_ce.alarm_controller_api import AlarmControllerApi
from tb_rest_client.api.api_ce.asset_controller_api import AssetControllerApi
from tb_rest_client.api.api_ce.audit_log_controller_api import AuditLogControllerApi
from tb_rest_client.api.api_ce.auth_controller_api import AuthControllerApi
from tb_rest_client.api.api_ce.component_descriptor_controller_api import ComponentDescriptorControllerApi
from tb_rest_client.api.api_ce.customer_controller_api import CustomerControllerApi
from tb_rest_client.api.api_ce.dashboard_controller_api import DashboardControllerApi
from tb_rest_client.api.api_ce.device_controller_api import DeviceControllerApi
from tb_rest_client.api.api_ce.device_api_controller_api import DeviceApiControllerApi
from tb_rest_client.api.api_ce.device_profile_controller_api import DeviceProfileControllerApi
from tb_rest_client.api.api_ce.edge_controller_api import EdgeControllerApi
from tb_rest_client.api.api_ce.edge_event_controller_api import EdgeEventControllerApi
from tb_rest_client.api.api_ce.entity_query_controller_api import EntityQueryControllerApi
from tb_rest_client.api.api_ce.entity_relation_controller_api import EntityRelationControllerApi
from tb_rest_client.api.api_ce.entity_view_controller_api import EntityViewControllerApi
from tb_rest_client.api.api_ce.event_controller_api import EventControllerApi
from tb_rest_client.api.api_ce.lwm_2m_controller_api import Lwm2mControllerApi
from tb_rest_client.api.api_ce.o_auth_2_config_template_controller_api import OAuth2ConfigTemplateControllerApi
from tb_rest_client.api.api_ce.o_auth_2_controller_api import OAuth2ControllerApi
from tb_rest_client.api.api_ce.ota_package_controller_api import OtaPackageControllerApi
from tb_rest_client.api.api_ce.queue_controller_api import QueueControllerApi
from tb_rest_client.api.api_ce.rpc_v_1_controller_api import RpcV1ControllerApi
from tb_rest_client.api.api_ce.rpc_v_2_controller_api import RpcV2ControllerApi
from tb_rest_client.api.api_ce.rule_chain_controller_api import RuleChainControllerApi
from tb_rest_client.api.api_ce.tb_resource_controller_api import TbResourceControllerApi
from tb_rest_client.api.api_ce.telemetry_controller_api import TelemetryControllerApi
from tb_rest_client.api.api_ce.tenant_controller_api import TenantControllerApi
from tb_rest_client.api.api_ce.tenant_profile_controller_api import TenantProfileControllerApi
from tb_rest_client.api.api_ce.user_controller_api import UserControllerApi
from tb_rest_client.api.api_ce.widget_type_controller_api import WidgetTypeControllerApi
from tb_rest_client.api.api_ce.widgets_bundle_controller_api import WidgetsBundleControllerApi
from tb_rest_client.api.api_ce.ui_settings_controller_api import UiSettingsControllerApi
from tb_rest_client.api.api_ce.alarm_comment_controller_api import AlarmCommentControllerApi
from tb_rest_client.api.api_ce.notification_target_controller_api import NotificationTargetControllerApi
from tb_rest_client.api.api_ce.usage_info_controller_api import UsageInfoControllerApi
from tb_rest_client.api.api_ce.notification_rule_controller_api import NotificationRuleControllerApi
from tb_rest_client.api.api_ce.notification_controller_api import NotificationControllerApi
from tb_rest_client.api.api_ce.notification_template_controller_api import NotificationTemplateControllerApi
from tb_rest_client.api.api_ce.asset_profile_controller_api import AssetProfileControllerApi
from tb_rest_client.api.api_ce.two_factor_auth_config_controller_api import TwoFactorAuthConfigControllerApi
from tb_rest_client.api.api_ce.device_connectivity_controller_api import DeviceConnectivityControllerApi
from tb_rest_client.api.api_ce.mail_config_template_controller_api import MailConfigTemplateControllerApi
from tb_rest_client.api.api_ce.image_controller_api import ImageControllerApi
from tb_rest_client.api.api_ce.mobile_application_controller_api import MobileApplicationControllerApi
from tb_rest_client.api.api_ce.queue_stats_controller_api import QueueStatsControllerApi
from tb_rest_client.api.api_ce.domain_controller_api import DomainControllerApi
from tb_rest_client.api.api_ce import MobileAppControllerApi
from tb_rest_client.api.api_ce import MobileAppBundleControllerApi
from tb_rest_client.api.api_ce import RuleEngineControllerApi
from tb_rest_client.api.api_ce import QrCodeSettingsControllerApi
# from tb_rest_client.models.models_pe import *
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
        self.token_info = {"token": "", "refreshToken": "", "exp": 0}
        self.api_client = None
        self.logged_in = False
        self.stopped = True
        self.configuration = Configuration()
        self.configuration.host = self.base_url

    def run(self):
        self.stopped = False
        while not self.stopped:
            try:
                check_time = time()
                if check_time >= self.token_info["exp"] and self.logged_in:
                    if self.token_info["refreshToken"]:
                        self.refresh()
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
        token_json = post(self.base_url + "/api/auth/login", json={"username": username, "password": password},
                          verify=self.configuration.verify_ssl).json()
        self.__save_token(token_json)

        self.logged_in = True

        self.__load_configuration()

    def public_login(self, public_id):
        token_json = post(self.base_url + "/api/auth/login/public", json={"publicId": public_id},
                          verify=self.configuration.verify_ssl).json()

        self.__save_token(token_json)
        self.__load_configuration()

    def token_login(self, token, refresh_token=None):
        token_json = {
            "token": token,
            "refreshToken": refresh_token,
        }

        self.__save_token(token_json)
        self.__load_configuration()

    def refresh(self):
        if not self.token_info["refreshToken"]:
            return

        token_json = post(self.base_url + "/api/auth/token", json={"refreshToken": self.token_info["refreshToken"]},
                          verify=self.configuration.verify_ssl).json()

        self.__save_token(token_json)
        self.__load_configuration()

    def __save_token(self, token_json):
        token = None
        refresh_token = None
        if isinstance(token_json, dict) and token_json.get("token") is not None:
            token = token_json["token"]
            refresh_token = token_json["refreshToken"]
        self.configuration.api_key_prefix["X-Authorization"] = "Bearer"
        self.configuration.api_key["X-Authorization"] = token
        self.token_info['token'] = token
        self.token_info['refreshToken'] = refresh_token
        try:
            parsed_token = jwt.decode(token, options={"verify_signature": False})
            self.token_info['exp'] = parsed_token['exp']
        except Exception:
            return

    def __load_configuration(self):
        self.api_client = ApiClient(self.configuration)
        self.__load_controllers()

    def get_token(self):
        return self.token_info["token"]

    # OAuth2 Controller
    def delete_client_registration_template(self, client_registration_template_id: EntityId):
        client_registration_template_id = self.get_id(client_registration_template_id)
        return self.o_auth2_config_template_controller.delete_client_registration_template_using_delete(
            client_registration_template_id=client_registration_template_id)

    def get_client_registration_templates1(self) -> List[OAuth2ClientRegistrationTemplate]:
        return self.o_auth2_config_template_controller.get_client_registration_templates_using_get1()

    def save_client_registration_template(self,
                                          body: Optional[OAuth2ClientRegistrationTemplate]) -> OAuth2ClientRegistrationTemplate:
        return self.o_auth2_config_template_controller.save_client_registration_template_using_post(body=body)

    # Asset Controller
    def get_customer_assets(self, customer_id: CustomerId, page_size: int, page: int, type: Optional[str] = None,
                            text_search: Optional[str] = None,
                            sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataAsset:
        customer_id = self.get_id(customer_id)
        return self.asset_controller.get_customer_assets_using_get(customer_id=customer_id, page_size=page_size,
                                                                   page=page, type=type, text_search=text_search,
                                                                   sort_property=sort_property, sort_order=sort_order)

    def get_tenant_asset(self, asset_name: str) -> Asset:
        return self.asset_controller.get_tenant_asset_using_get(asset_name=asset_name)

    def delete_asset(self, asset_id: AssetId) -> None:
        asset_id = self.get_id(asset_id)
        return self.asset_controller.delete_asset_using_delete(asset_id=asset_id)

    def get_assets_by_ids(self, asset_ids: list) -> List[Asset]:
        asset_ids = ','.join(asset_ids)
        return self.asset_controller.get_assets_by_ids_using_get(asset_ids=asset_ids)

    def get_tenant_assets(self, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None,
                          sort_property: Optional[str] = None,
                          sort_order: Optional[str] = None) -> PageDataAsset:
        return self.asset_controller.get_tenant_assets_using_get(page_size=page_size, page=page, type=type,
                                                                 text_search=text_search, sort_property=sort_property,
                                                                 sort_order=sort_order)

    def get_asset_types(self) -> List[EntitySubtype]:
        return self.asset_controller.get_asset_types_using_get()

    def find_by_query(self, body: Optional[AssetSearchQuery]) -> List[Asset]:
        return self.asset_controller.find_by_query_using_post(body=body)

    def get_asset_by_id(self, asset_id: AssetId) -> Asset:
        asset_id = self.get_id(asset_id)
        return self.asset_controller.get_asset_by_id_using_get(asset_id=asset_id)

    # Rule Chain Controller
    def export_rule_chains(self, limit: int) -> RuleChainData:
        return self.rule_chain_controller.export_rule_chains_using_get(limit=limit)

    def delete_rule_chain(self, rule_chain_id: RuleChainId) -> None:
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.delete_rule_chain_using_delete(rule_chain_id=rule_chain_id)

    def set_edge_template_root_rule_chain(self, rule_chain_id: RuleChainId) -> RuleChain:
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.set_edge_template_root_rule_chain_using_post(rule_chain_id=rule_chain_id)

    def save_rule_chain(self, body: Optional[DefaultRuleChainCreateRequest]) -> RuleChain:
        return self.rule_chain_controller.save_rule_chain_using_post(body=body)

    def unassign_rule_chain_from_edge(self, edge_id: EdgeId, rule_chain_id: RuleChainId) -> RuleChain:
        edge_id = self.get_id(edge_id)
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.unassign_rule_chain_from_edge_using_delete(edge_id=edge_id,
                                                                                     rule_chain_id=rule_chain_id)

    def assign_rule_chain_to_edge(self, edge_id: EdgeId, rule_chain_id: RuleChainId) -> RuleChain:
        edge_id = self.get_id(edge_id)
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.assign_rule_chain_to_edge_using_post(edge_id=edge_id,
                                                                               rule_chain_id=rule_chain_id)

    def unset_auto_assign_to_edge_rule_chain(self, rule_chain_id: RuleChainId) -> RuleChain:
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.unset_auto_assign_to_edge_rule_chain_using_delete(rule_chain_id=rule_chain_id)

    def get_rule_chain_by_id(self, rule_chain_id: RuleChainId) -> RuleChain:
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.get_rule_chain_by_id_using_get(rule_chain_id=rule_chain_id)

    def test_script(self, body: Optional[RuleChain]) -> Union[
            dict, str, list, bytes, None, RESTResponse, tuple, Any]:
        return self.rule_chain_controller.test_script_using_post(body=body)

    def save_rule_chain_v1(self, body: Optional[RuleChain]) -> RuleChain:
        return self.rule_chain_controller.save_rule_chain_using_post1(body=body)

    def get_edge_rule_chains(self, edge_id: EdgeId, page_size: int, page: int, text_search: Optional[str] = None,
                             sort_property: Optional[str] = None,
                             sort_order: Optional[str] = None) -> PageDataRuleChain:
        edge_id = self.get_id(edge_id)
        return self.rule_chain_controller.get_edge_rule_chains_using_get(edge_id=edge_id, page_size=page_size,
                                                                         page=page, text_search=text_search,
                                                                         sort_property=sort_property,
                                                                         sort_order=sort_order)

    def set_auto_assign_to_edge_rule_chain(self, rule_chain_id: RuleChainId) -> RuleChain:
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.set_auto_assign_to_edge_rule_chain_using_post(rule_chain_id=rule_chain_id)

    def import_rule_chains(self, body: Optional[RuleChainData], overwrite: Optional[bool] = None) -> List[
        RuleChainImportResult]:
        return self.rule_chain_controller.import_rule_chains_using_post(body=body, overwrite=overwrite)

    def set_root_rule_chain(self, rule_chain_id: RuleChainId) -> RuleChain:
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.set_root_rule_chain_using_post(rule_chain_id=rule_chain_id)

    def get_rule_chains(self, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None,
                        sort_property: Optional[str] = None,
                        sort_order: Optional[str] = None) -> PageDataRuleChain:
        return self.rule_chain_controller.get_rule_chains_using_get(page_size=page_size, page=page, type=type,
                                                                    text_search=text_search,
                                                                    sort_property=sort_property, sort_order=sort_order)

    def get_auto_assign_to_edge_rule_chains(self) -> List[RuleChain]:
        return self.rule_chain_controller.get_auto_assign_to_edge_rule_chains_using_get()

    def get_latest_rule_node_debug_input(self, rule_node_id: RuleNodeId) -> Union[
            dict, str, list, bytes, None, RESTResponse, tuple, Any]:
        rule_node_id = self.get_id(rule_node_id)
        return self.rule_chain_controller.get_latest_rule_node_debug_input_using_get(rule_node_id=rule_node_id)

    def get_rule_chain_meta_data(self, rule_chain_id: RuleChainId) -> RuleChainMetaData:
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.get_rule_chain_meta_data_using_get(rule_chain_id=rule_chain_id)

    # Auth Controller
    def get_user(self) -> User:
        return self.auth_controller.get_user_using_get()

    def change_password(self, body: Optional[ChangePasswordRequest] = None) -> ObjectNode:
        return self.auth_controller.change_password_using_post(body=body)

    def logout(self) -> None:
        return self.auth_controller.logout_using_post()

    def check_reset_token(self, reset_token: str) -> str:
        return self.auth_controller.check_reset_token_using_get(reset_token=reset_token)

    def reset_password(self, body: Optional[ResetPasswordRequest] = None) -> JwtPair:
        return self.auth_controller.reset_password_using_post(body=body)

    def activate_user(self, body: Optional[ActivateUserRequest], send_activation_mail: bool) -> JwtPair:
        return self.auth_controller.activate_user_using_post(body=body, send_activation_mail=send_activation_mail)

    def get_user_password_policy(self) -> UserPasswordPolicy:
        return self.auth_controller.get_user_password_policy_using_get()

    def check_activate_token(self, activate_token: str) -> str:
        return self.auth_controller.check_activate_token_using_get(activate_token=activate_token)

    def request_reset_password_by_email(self, body: Optional[ResetPasswordEmailRequest] = None) -> None:
        return self.auth_controller.request_reset_password_by_email_using_post(body=body)

    # Event Controller #
    def get_events_post(self, tenant_id: TenantId, page_size: int, page: int, entity_id: EntityId,
                        body: Optional[EventFilter], text_search: Optional[str] = None, sort_property: Optional[str] = None,
                        sort_order: Optional[str] = None, start_time: Optional[int] = None,
                        end_time: Optional[int] = None) -> PageDataEventInfo:
        tenant_id = self.get_id(tenant_id)
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.event_controller.get_events_using_post(tenant_id=tenant_id, page_size=page_size, page=page,
                                                           entity_type=entity_type, entity_id=entity_id, body=body,
                                                           text_search=text_search, sort_property=sort_property,
                                                           sort_order=sort_order, start_time=start_time,
                                                           end_time=end_time)

    def get_events_v1_get1(self, entity_id: EntityId, event_type: str, tenant_id: TenantId,
                           page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None,
                           sort_order: Optional[str] = None,
                           start_time: Optional[int] = None, end_time: Optional[int] = None) -> PageDataEvent:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        tenant_id = self.get_id(tenant_id)
        return self.event_controller.get_events_using_get1(entity_type=entity_type, entity_id=entity_id,
                                                           event_type=event_type, tenant_id=tenant_id,
                                                           page_size=page_size, page=page, text_search=text_search,
                                                           sort_property=sort_property, sort_order=sort_order,
                                                           start_time=start_time, end_time=end_time)

    def clear_events_post(self, entity_id: EntityId, body: Optional[EntityIdClearstartTimeendTimeBody] = None, start_time: Optional[int] = None,
                          end_time: Optional[int] = None):
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.event_controller.clear_events_using_post(entity_type=entity_type, entity_id=entity_id, body=body,
                                                             start_time=start_time, end_time=end_time)

    def get_events_get(self, entity_id: EntityId, tenant_id: TenantId, page_size: int, page: int,
                       text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                       start_time: Optional[int] = None,
                       end_time: Optional[int] = None) -> PageDataEventInfo:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        tenant_id = self.get_id(tenant_id)
        return self.event_controller.get_events_using_get(entity_type=entity_type, entity_id=entity_id,
                                                          tenant_id=tenant_id, page_size=page_size, page=page,
                                                          text_search=text_search, sort_property=sort_property,
                                                          sort_order=sort_order, start_time=start_time,
                                                          end_time=end_time)

    # Telemetry Controller #
    def get_attribute_keys_by_scope(self, entity_id: EntityId, scope: str):
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.get_attribute_keys_by_scope_using_get(entity_type=entity_type,
                                                                               entity_id=entity_id, scope=scope)

    def get_timeseries(self, entity_id: EntityId, keys: str, start_ts: int, end_ts: int,
                       interval_type: Optional[str] = None, interval: Optional[int] = None,
                       time_zone: Optional[str] = None, limit: Optional[int] = None, agg: Optional[str] = None,
                       order_by: Optional[str] = None, use_strict_data_types: Optional[bool] = None):
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.get_timeseries_using_get(entity_type=entity_type, entity_id=entity_id,
                                                                  keys=keys, start_ts=start_ts, end_ts=end_ts,
                                                                  interval=interval, limit=limit, agg=agg,
                                                                  order_by=order_by, interval_type=interval_type,
                                                                  use_strict_data_types=use_strict_data_types, time_zone=time_zone)

    def delete_device_attributes(self, device_id: DeviceId, scope: str, keys: str):
        device_id = self.get_id(device_id)
        return self.telemetry_controller.delete_device_attributes_using_delete(device_id=device_id, scope=scope,
                                                                               keys=keys)

    def save_entity_attributes_v1(self, entity_id: EntityId, scope: str,
                                  body: Union[dict, str, list, bytes, None, RESTResponse, tuple, Any] = None):
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.save_entity_attributes_v1_using_post(entity_type=entity_type,
                                                                              entity_id=entity_id, scope=scope,
                                                                              body=body)

    def delete_entity_timeseries(self, entity_id: EntityId, keys: str, delete_all_data_for_keys: Optional[bool] = None,
                                 start_ts: Optional[int] = None, end_ts: Optional[int] = None,
                                 delete_latest: Optional[bool] = None,
                                 rewrite_latest_if_deleted: Optional[bool] = None):
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.delete_entity_timeseries_using_delete(entity_type=entity_type,
                                                                               entity_id=entity_id, keys=keys,
                                                                               delete_all_data_for_keys=delete_all_data_for_keys,
                                                                               start_ts=start_ts, end_ts=end_ts,
                                                                               delete_latest=delete_latest,
                                                                               rewrite_latest_if_deleted=rewrite_latest_if_deleted)

    def save_device_attributes(self, device_id: DeviceId, scope: str,
                               body: Union[dict, str, list, bytes, None, RESTResponse, tuple, Any] = None):
        device_id = self.get_id(device_id)
        return self.telemetry_controller.save_device_attributes_using_post(device_id=device_id, scope=scope, body=body)

    def get_latest_timeseries(self, entity_id: EntityId, keys: Optional[str] = None,
                              use_strict_data_types: Optional[bool] = None):
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.get_latest_timeseries_using_get(entity_type=entity_type, entity_id=entity_id,
                                                                         keys=keys,
                                                                         use_strict_data_types=use_strict_data_types)

    def get_timeseries_keys_v1(self, entity_id: EntityId):
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.get_timeseries_keys_using_get1(entity_type=entity_type, entity_id=entity_id)

    def get_attributes_by_scope(self, entity_id: EntityId, scope: str,
                                keys: Optional[str] = None):
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.get_attributes_by_scope_using_get(entity_type=entity_type, entity_id=entity_id,
                                                                           scope=scope, keys=keys)

    def get_attribute_keys(self, entity_id: EntityId):
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.get_attribute_keys_using_get(entity_type=entity_type, entity_id=entity_id)

    def save_entity_attributes_v2(self, entity_id: EntityId, scope: str,
                                  body: Union[dict, str, list, bytes, None, RESTResponse, tuple, Any] = None):
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.save_entity_attributes_v2_using_post(entity_type=entity_type,
                                                                              entity_id=entity_id, scope=scope,
                                                                              body=body)

    def save_entity_telemetry(self, entity_id: EntityId, scope: str,
                              body: Optional[dict] = None):
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.save_entity_telemetry_using_post(entity_type=entity_type, entity_id=entity_id,
                                                                          scope=scope, body=body)

    def save_entity_telemetry_with_ttl(self, entity_id: EntityId, scope: str, ttl: int,
                                       body: Optional[dict] = None):
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        ttl = str(ttl)
        return self.telemetry_controller.save_entity_telemetry_with_ttl_using_post(entity_type=entity_type,
                                                                                   entity_id=entity_id, scope=scope,
                                                                                   ttl=ttl, body=body)

    def get_attributes(self, entity_id: EntityId, keys: Optional[str] = None):
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.get_attributes_using_get(entity_type=entity_type, entity_id=entity_id,
                                                                  keys=keys)

    def delete_entity_attributes(self, entity_id: EntityId, scope: str, keys: str):
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.delete_entity_attributes_using_delete(entity_type=entity_type,
                                                                               entity_id=entity_id, scope=scope,
                                                                               keys=keys)

    # Alarm Controller
    def ack_alarm(self, alarm_id: AlarmId) -> AlarmInfo:
        alarm_id = self.get_id(alarm_id)
        return self.alarm_controller.ack_alarm_using_post(alarm_id=alarm_id)

    def get_alarm_info_by_id(self, alarm_id: AlarmId) -> AlarmInfo:
        alarm_id = self.get_id(alarm_id)
        return self.alarm_controller.get_alarm_info_by_id_using_get(alarm_id=alarm_id)

    def delete_alarm(self, alarm_id: AlarmId) -> bool:
        alarm_id = self.get_id(alarm_id)
        return self.alarm_controller.delete_alarm_using_delete(alarm_id=alarm_id)

    def clear_alarm(self, alarm_id: AlarmId) -> AlarmInfo:
        alarm_id = self.get_id(alarm_id)
        return self.alarm_controller.clear_alarm_using_post(alarm_id=alarm_id)

    def save_alarm(self, body: Alarm) -> Alarm:
        return self.alarm_controller.save_alarm_using_post(body=body)

    def get_alarms(self, entity_id: EntityId, page_size: int, page: int, search_status: Optional[str] = None,
                   status: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None,
                   sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None,
                   fetch_originator: Optional[bool] = None, assignee_id: Optional[str] = None) -> PageDataAlarmInfo:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.alarm_controller.get_alarms_using_get(entity_type=entity_type, entity_id=entity_id,
                                                          page_size=page_size, page=page, search_status=search_status,
                                                          status=status, text_search=text_search,
                                                          sort_property=sort_property, sort_order=sort_order,
                                                          start_time=start_time, end_time=end_time,
                                                          fetch_originator=fetch_originator, assignee_id=assignee_id)

    def unassign_alarm(self, id: AlarmId) -> Alarm:
        id = self.get_id(id)
        return self.alarm_controller.unassign_alarm_using_delete(alarm_id=id)

    def get_asset_info_by_id(self, asset_id: AssetId) -> AssetInfo:
        asset_id = self.get_id(asset_id)
        return self.asset_controller.get_asset_info_by_id_using_get(asset_id=asset_id)

    def get_customer_asset_infos(self, customer_id: CustomerId, page_size: int, page: int, type: Optional[str] = None,
                                 text_search: Optional[str] = None,
                                 sort_property: Optional[str] = None, sort_order: Optional[str] = None, asset_profile_id: Optional[AssetProfileId] = None) -> PageDataAssetInfo:
        customer_id = self.get_id(customer_id)

        if asset_profile_id:
            asset_profile_id = self.get_id(asset_profile_id)
        return self.asset_controller.get_customer_asset_infos_using_get(customer_id=customer_id, page_size=page_size,
                                                                        page=page, type=type, text_search=text_search,
                                                                        sort_property=sort_property,
                                                                        sort_order=sort_order, asset_profile_id=asset_profile_id)

    def count_alarms_by_query(self, body: AlarmCountQuery) -> int:
        return self.entity_query_controller.count_alarms_by_query_using_post(body=body)

    def get_customer_dashboards(self, customer_id: CustomerId, page_size: int, page: int, mobile: Optional[bool] = None,
                                text_search: Optional[str] = None,
                                sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataDashboardInfo:
        customer_id = self.get_id(customer_id)
        return self.dashboard_controller.get_customer_dashboards_using_get(customer_id=customer_id, page_size=page_size,
                                                                           page=page, mobile=mobile,
                                                                           text_search=text_search,
                                                                           sort_property=sort_property,
                                                                           sort_order=sort_order)

    def get_user_settings(self) -> JsonNode:
        return self.user_controller.get_user_settings_using_get()

    def get_tenant_usage_info(self) -> UsageInfo:
        return self.usage_info_controller.get_tenant_usage_info_using_get()

    def save_user_settings(self, body: JsonNode) -> JsonNode:
        return self.user_controller.save_user_settings_using_post(body=body)

    def put_user_settings(self, body: JsonNode):
        return self.user_controller.put_user_settings_using_put(body=body)

    def report_user_dashboard_action(self, dashboard_id: DashboardId, action: str) -> UserDashboardsInfo:
        dashboard_id = self.get_id(dashboard_id)
        return self.user_controller.report_user_dashboard_action_using_get(dashboard_id=dashboard_id, action=action)

    def get_users_for_assign(self, alarm_id: AlarmId, page_size: int, page: int, text_search: Optional[str] = None,
                             sort_property: Optional[str] = None,
                             sort_order: Optional[str] = None) -> PageDataUserEmailInfo:
        alarm_id = self.get_id(alarm_id)
        return self.user_controller.get_users_for_assign_using_get(alarm_id=alarm_id, page_size=page_size, page=page,
                                                                   text_search=text_search,
                                                                   sort_property=sort_property,
                                                                   sort_order=sort_order)

    def find_users_by_query(self, page_size: int, page: int, text_search: Optional[str] = None,
                            sort_property: Optional[str] = None,
                            sort_order: Optional[str] = None) -> PageDataUserEmailInfo:
        return self.user_controller.find_users_by_query_using_get(page_size=page_size, page=page,
                                                                  text_search=text_search,
                                                                  sort_property=sort_property,
                                                                  sort_order=sort_order)

    def get_user_dashboards_info(self) -> UserDashboardsInfo:
        return self.user_controller.get_user_dashboards_info_using_get()

    def delete_user_settings(self, paths: List[str], type: str):
        paths = ','.join(paths)
        return self.user_controller.delete_user_settings_using_delete(paths=paths, type=type)

    def get_mobile_session(self, x_mobile_token: str) -> MobileSessionInfo:
        return self.user_controller.get_mobile_session_using_get(x_mobile_token=x_mobile_token)

    def remove_mobile_session(self, x_mobile_token: str) -> None:
        return self.user_controller.remove_mobile_session_using_delete(x_mobile_token=x_mobile_token)

    def save_mobile_session(self, x_mobile_token: str, body: MobileSessionInfo):
        return self.user_controller.save_mobile_session_using_post(x_mobile_token=x_mobile_token, body=body)

    def get_tenant_profiles_by_ids(self, ids: List[str]) -> List[TenantProfile]:
        ids = ','.join(ids)
        return self.tenant_profile_controller.get_tenant_profiles_by_ids_using_get(ids=ids)

    def get_entity_view_info_by_id(self, entity_view_id: EntityViewId) -> EntityViewInfo:
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.get_entity_view_info_by_id_using_get(entity_view_id=entity_view_id)

    def get_device_info_by_id(self, device_id: DeviceId) -> DeviceInfo:
        device_id = self.get_id(device_id)
        return self.device_controller.get_device_info_by_id_using_get(device_id=device_id)

    def get_alarm_by_id(self, alarm_id: AlarmId) -> Alarm:
        alarm_id = self.get_id(alarm_id)
        return self.alarm_controller.get_alarm_by_id_using_get(alarm_id=alarm_id)

    def get_all_alarms(self, page_size: int, page: int, search_status: Optional[str] = None, status: Optional[str] = None,
                       text_search: Optional[str] = None,
                       sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None,
                       end_time: Optional[int] = None,
                       fetch_originator: Optional[bool] = None) -> PageDataAlarmInfo:
        return self.alarm_controller.get_all_alarms_using_get(page_size=page_size, page=page,
                                                              search_status=search_status, status=status,
                                                              text_search=text_search, sort_property=sort_property,
                                                              sort_order=sort_order, start_time=start_time,
                                                              end_time=end_time, fetch_originator=fetch_originator)

    # Alarm Comment Controller
    def delete_alarm_comment(self, alarm_id: AlarmId, comment_id: AlarmCommentId):
        alarm_id = self.get_id(alarm_id)
        comment_id = self.get_id(comment_id)
        return self.alarm_comment_controller.delete_alarm_comment_using_delete(alarm_id=alarm_id, comment_id=comment_id)

    def get_alarm_comments(self, alarm_id: AlarmId, page_size: int, page: int, sort_property: Optional[str] = None,
                           sort_order: Optional[str] = None) -> PageDataAlarmCommentInfo:
        alarm_id = self.get_id(alarm_id)
        return self.alarm_comment_controller.get_alarm_comments_using_get(alarm_id=alarm_id, page_size=page_size,
                                                                          page=page, sort_property=sort_property,
                                                                          sort_order=sort_order)

    def save_alarm_comment(self, alarm_id: AlarmId, body: Optional[AlarmComment] = None) -> AlarmComment:
        alarm_id = self.get_id(alarm_id)
        return self.alarm_comment_controller.save_alarm_comment_using_post(alarm_id=alarm_id, body=body)

    # Edge Controller #
    def get_tenant_edge(self, edge_name: str) -> Edge:
        return self.edge_controller.get_tenant_edge_using_get(edge_name=edge_name)

    def delete_edge(self, edge_id: EdgeId) -> None:
        edge_id = self.get_id(edge_id)
        return self.edge_controller.delete_edge_using_delete(edge_id=edge_id)

    def is_edges_support_enabled(self) -> bool:
        return self.edge_controller.is_edges_support_enabled_using_get()

    def get_edge_by_id(self, edge_id: EdgeId) -> Edge:
        edge_id = self.get_id(edge_id)
        return self.edge_controller.get_edge_by_id_using_get(edge_id=edge_id)

    def sync_edge(self, edge_id: EdgeId) -> DeferredResultResponseEntity:
        edge_id = self.get_id(edge_id)
        return self.edge_controller.sync_edge_using_post(edge_id=edge_id)

    def get_tenant_edges(self, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None,
                         sort_property: Optional[str] = None,
                         sort_order: Optional[str] = None) -> PageDataEdge:
        return self.edge_controller.get_tenant_edges_using_get(page_size=page_size, page=page, type=type,
                                                               text_search=text_search, sort_property=sort_property,
                                                               sort_order=sort_order)

    def find_by_query_v2(self, body: Optional[EdgeSearchQuery] = None) -> List[Edge]:
        return self.edge_controller.find_by_query_using_post2(body=body)

    def get_edges(self, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None,
                  sort_order: Optional[str] = None) -> PageDataEdge:
        return self.edge_controller.get_edges_using_get(page_size=page_size, page=page, text_search=text_search,
                                                        sort_property=sort_property, sort_order=sort_order)

    def get_edge_types(self) -> List[EntitySubtype]:
        return self.edge_controller.get_edge_types_using_get()

    def set_edge_root_rule_chain(self, edge_id: EdgeId, rule_chain_id: RuleChainId) -> Edge:
        edge_id = self.get_id(edge_id)
        rule_chain_id = self.get_id(rule_chain_id)
        return self.edge_controller.set_edge_root_rule_chain_using_post(edge_id=edge_id, rule_chain_id=rule_chain_id)

    def find_missing_to_related_rule_chains(self, edge_id: EdgeId) -> str:
        edge_id = self.get_id(edge_id)
        return self.edge_controller.find_missing_to_related_rule_chains_using_get(edge_id=edge_id)

    def get_customer_edges(self, customer_id: CustomerId, page_size: int, page: int, type: Optional[str] = None,
                           text_search: Optional[str] = None,
                           sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataEdge:
        customer_id = self.get_id(customer_id)
        return self.edge_controller.get_customer_edges_using_get(customer_id=customer_id, page_size=page_size,
                                                                 page=page, type=type, text_search=text_search,
                                                                 sort_property=sort_property, sort_order=sort_order)

    def get_edges_by_ids(self, edge_ids: list) -> List[Edge]:
        return self.edge_controller.get_edges_by_ids_using_get(edge_ids=str(edge_ids))

    def process_edges_bulk_import(self, body: Optional[BulkImportRequest] = None) -> BulkImportResultEdge:
        return self.edge_controller.process_edges_bulk_import_using_post(body=body)

    def get_edge_events(self, edge_id: EdgeId, page_size: int, page: int, text_search: Optional[str] = None,
                        sort_property: Optional[str] = None,
                        sort_order: Optional[str] = None, start_time: Optional[int] = None,
                        end_time: Optional[int] = None) -> PageDataEdgeEvent:
        edge_id = self.get_id(edge_id)
        return self.edge_event_controller.get_edge_events_using_get(edge_id=edge_id, page_size=page_size, page=page,
                                                                    text_search=text_search,
                                                                    sort_property=sort_property, sort_order=sort_order,
                                                                    start_time=start_time, end_time=end_time)

    # RPC v2 Controller
    def get_persisted_rpc(self, rpc_id: RpcId) -> Rpc:
        rpc_id = self.get_id(rpc_id)
        return self.rpc_v2_controller.get_persisted_rpc_using_get(rpc_id=rpc_id)

    def handle_one_way_device_rpc_request_v1(self, device_id: DeviceId, body: Optional[str] = None):
        device_id = self.get_id(device_id)
        return self.rpc_v2_controller.handle_one_way_device_rpc_request_using_post1(device_id=device_id, body=body)

    def handle_two_way_device_rpc_request_v1(self, device_id: DeviceId, body: Optional[str] = None):
        device_id = self.get_id(device_id)
        return self.rpc_v2_controller.handle_two_way_device_rpc_request_using_post1(device_id=device_id, body=body)

    def get_persisted_rpc_by_device(self, device_id: DeviceId, page_size: int, page: int, rpc_status: str,
                                    text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                    sort_order: Optional[str] = None):
        device_id = self.get_id(device_id)
        return self.rpc_v2_controller.get_persisted_rpc_by_device_using_get(device_id=device_id, page_size=page_size,
                                                                            page=page, rpc_status=rpc_status,
                                                                            text_search=text_search,
                                                                            sort_property=sort_property,
                                                                            sort_order=sort_order)
    def get_rule_chain_output_labels_usage(self, rule_chain_id: RuleChainId) -> List[RuleChainOutputLabelsUsage]:
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.get_rule_chain_output_labels_usage_using_get(rule_chain_id=rule_chain_id)

    def get_rule_chain_output_labels(self, rule_chain_id: RuleChainId) -> List[str]:
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.get_rule_chain_output_labels_using_get(rule_chain_id=rule_chain_id)

    def is_tbel_enabled(self) -> bool:
        return self.rule_chain_controller.is_tbel_enabled_using_get()

    def save_rule_chain_meta_data(self, body: Optional[RuleChainMetaData] = None,
                                  update_related: Optional[bool] = None) -> RuleChainMetaData:
        return self.rule_chain_controller.save_rule_chain_meta_data_using_post(body=body, update_related=update_related)

    def delete_rpc(self, rpc_id: RpcId) -> None:
        rpc_id = self.get_id(rpc_id)
        return self.rpc_v2_controller.delete_rpc_using_delete(rpc_id=rpc_id)

    # Customer Controller #
    def get_customer_title_by_id(self, customer_id: CustomerId) -> str:
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_customer_title_by_id_using_get(customer_id=customer_id)

    def get_customers(self, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None,
                      sort_order: Optional[str] = None) -> PageDataCustomer:
        return self.customer_controller.get_customers_using_get(page_size=page_size, page=page, text_search=text_search,
                                                                sort_property=sort_property, sort_order=sort_order)

    def get_customer_by_id(self, customer_id: CustomerId) -> Customer:
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_customer_by_id_using_get(customer_id=customer_id)

    def get_short_customer_info_by_id(self, customer_id: CustomerId) -> Union[
            dict, str, list, bytes, None, RESTResponse, tuple, Any]:
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_short_customer_info_by_id_using_get(customer_id=customer_id)

    def get_tenant_customer(self, customer_title: str) -> Customer:
        return self.customer_controller.get_tenant_customer_using_get(customer_title=customer_title)

    def delete_customer(self, customer_id: CustomerId) -> None:
        customer_id = self.get_id(customer_id)
        return self.customer_controller.delete_customer_using_delete(customer_id=customer_id)

    # User Controller #
    def get_user_token(self, user_id: UserId) -> JwtPair:
        user_id = self.get_id(user_id)
        return self.user_controller.get_user_token_using_get(user_id=user_id)

    def get_activation_link(self, user_id: UserId) -> str:
        user_id = self.get_id(user_id)
        return self.user_controller.get_activation_link_using_get(user_id=user_id)

    def delete_user(self, user_id: UserId) -> None:
        user_id = self.get_id(user_id)
        return self.user_controller.delete_user_using_delete(user_id=user_id)

    def set_user_credentials_enabled(self, user_id: UserId, user_credentials_enabled: bool) -> None:
        user_id = self.get_id(user_id)
        return self.user_controller.set_user_credentials_enabled_using_post(user_id=user_id,
                                                                            user_credentials_enabled=user_credentials_enabled)

    def get_customer_users(self, customer_id: CustomerId, page_size: int, page: int, text_search: Optional[str] = None,
                           sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataUser:
        customer_id = self.get_id(customer_id)
        return self.user_controller.get_customer_users_using_get(customer_id=customer_id, page_size=page_size,
                                                                 page=page, text_search=text_search,
                                                                 sort_property=sort_property, sort_order=sort_order)

    def get_user_by_id(self, user_id: UserId) -> User:
        user_id = self.get_id(user_id)
        return self.user_controller.get_user_by_id_using_get(user_id=user_id)

    def get_tenant_admins(self, tenant_id: TenantId, page_size: int, page: int, text_search: Optional[str] = None,
                          sort_property: Optional[str] = None,
                          sort_order: Optional[str] = None) -> PageDataUser:
        tenant_id = self.get_id(tenant_id)
        return self.user_controller.get_tenant_admins_using_get(tenant_id=tenant_id, page_size=page_size, page=page,
                                                                text_search=text_search, sort_property=sort_property,
                                                                sort_order=sort_order)

    def is_user_token_access_enabled(self) -> bool:
        return self.user_controller.is_user_token_access_enabled_using_get()

    def send_activation_email(self, email: str) -> None:
        return self.user_controller.send_activation_email_using_post(email=email)

    def get_activation_link_info(self, user_id: UserId) -> UserActivationLink:
        user_id = self.get_id(user_id)
        return self.user_controller.get_activation_link_using_get(user_id=user_id)

    # Queue Controller
    def get_tenant_queues_by_service_type(self, service_type: str, page_size: int, page: int,
                                          type: Optional[str] = None,
                                          text_search: Optional[str] = None,
                                          sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> List[str]:
        return self.queue_controller.get_tenant_queues_by_service_type_using_get(service_type=service_type,
                                                                                 page_size=page_size,
                                                                                 page=page, type=type,
                                                                                 text_search=text_search,
                                                                                 sort_property=sort_property,
                                                                                 sort_order=sort_order)

    def save_queue(self, service_type: str, body: Optional[Queue] = None) -> Queue:
        return self.queue_controller.save_queue_using_post(service_type=service_type, body=body)

    # RPC v1 Controller
    def handle_one_way_device_rpc_request(self, device_id: DeviceId,
                                          body: Optional[str] = None):
        device_id = self.get_id(device_id)
        return self.rpc_v1_controller.handle_one_way_device_rpc_request_using_post(device_id=device_id, body=body)

    def handle_two_way_device_rpc_request(self, device_id: DeviceId,
                                          body: Optional[Dict] = None):
        device_id = self.get_id(device_id)
        return self.rpc_v1_controller.handle_two_way_device_rpc_request_using_post(device_id=device_id, body=body)

    # Device Controller
    def get_device_types(self) -> List[EntitySubtype]:
        return self.device_controller.get_device_types_using_get()

    def update_device_credentials(self, body: Optional[DeviceCredentials] = None) -> DeviceCredentials:
        return self.device_controller.update_device_credentials_using_post(body=body)

    def delete_device(self, device_id: DeviceId) -> None:
        device_id = self.get_id(device_id)
        return self.device_controller.delete_device_using_delete(device_id=device_id)

    def assign_device_to_tenant(self, tenant_id: TenantId, device_id: DeviceId) -> Device:
        tenant_id = self.get_id(tenant_id)
        device_id = self.get_id(device_id)
        return self.device_controller.assign_device_to_tenant_using_post(tenant_id=tenant_id, device_id=device_id)

    def re_claim_device(self, device_name: str):
        return self.device_controller.re_claim_device_using_delete(device_name=device_name)

    def process_devices_bulk_import(self, body: Optional[BulkImportRequest] = None) -> BulkImportResultDevice:
        return self.device_controller.process_devices_bulk_import_using_post(body=body)

    def count_by_device_profile_and_empty_ota_package(self, ota_package_type: str,
                                                      device_profile_id: DeviceProfileId) -> int:
        device_profile_id = self.get_id(device_profile_id)
        return self.device_controller.count_by_device_profile_and_empty_ota_package_using_get(
            ota_package_type=ota_package_type, device_profile_id=device_profile_id)

    def get_devices_by_ids(self, device_ids: list) -> List[Device]:
        return self.device_controller.get_devices_by_ids_using_get(device_ids=str(device_ids))

    def get_device_by_id(self, device_id: DeviceId) -> Device:
        device_id = self.get_id(device_id)
        return self.device_controller.get_device_by_id_using_get(device_id=device_id)

    def find_by_query_v1(self, body: DeviceSearchQuery) -> List[Device]:
        return self.device_controller.find_by_query_using_post1(body=body)

    def get_customer_devices(self, customer_id: CustomerId, page_size: int, page: int, type: Optional[str] = None,
                             text_search: Optional[str] = None,
                             sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataDevice:
        customer_id = self.get_id(customer_id)
        return self.device_controller.get_customer_devices_using_get(customer_id=customer_id, page_size=page_size,
                                                                     page=page, type=type, text_search=text_search,
                                                                     sort_property=sort_property, sort_order=sort_order)

    def get_tenant_devices(self, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None,
                           sort_property: Optional[str] = None,
                           sort_order: Optional[str] = None) -> PageDataDevice:
        return self.device_controller.get_tenant_devices_using_get(page_size=page_size, page=page, type=type,
                                                                   text_search=text_search, sort_property=sort_property,
                                                                   sort_order=sort_order)

    def get_tenant_device(self, device_name: str) -> Device:
        return self.device_controller.get_tenant_device_using_get(device_name=device_name)

    def get_device_credentials_by_device_id(self, device_id: DeviceId) -> DeviceCredentials:
        device_id = self.get_id(device_id)
        return self.device_controller.get_device_credentials_by_device_id_using_get(device_id=device_id)

    # Entity Relation Controller
    def find_by_to_v1(self, to_id: EntityId, to_type: str, relation_type_group: Optional[str] = None) -> List[EntityRelation]:
        to_id = self.get_id(to_id)
        return self.entity_relation_controller.find_by_to_using_get1(to_id=to_id, to_type=to_type,
                                                                     relation_type_group=relation_type_group)

    def find_info_by_to(self, to_id: EntityId, to_type: str, relation_type_group: Optional[str] = None) -> List[
        EntityRelationInfo]:
        to_id = self.get_id(to_id)
        return self.entity_relation_controller.find_info_by_to_using_get(to_id=to_id, to_type=to_type,
                                                                         relation_type_group=relation_type_group)

    def delete_relations(self, entity_id: EntityId) -> None:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.entity_relation_controller.delete_relations_using_delete(entity_id=entity_id,
                                                                             entity_type=entity_type)

    def delete_relation(self, from_id: EntityId, relation_type: str, to_id: EntityId,
                        relation_type_group: Optional[str] = None) -> None:
        from_type = self.get_type(from_id)
        from_id = self.get_id(from_id)

        to_type = self.get_type(to_id)
        to_id = self.get_id(to_id)
        return self.entity_relation_controller.delete_relation_using_delete(from_id=from_id, from_type=from_type,
                                                                            relation_type=relation_type, to_id=to_id,
                                                                            to_type=to_type,
                                                                            relation_type_group=relation_type_group)

    def find_info_by_query(self, body: EntityRelationsQuery) -> List[EntityRelationInfo]:
        return self.entity_relation_controller.find_info_by_query_using_post(body=body)

    def find_by_query_v3(self, body: EntityRelationsQuery) -> List[EntityRelation]:
        return self.entity_relation_controller.find_by_query_using_post3(body=body)

    def save_relation(self, body: Optional[EntityRelation] = None) -> None:
        return self.entity_relation_controller.save_relation_using_post(body=body)

    def find_by_to(self, to_id: EntityId, relation_type: str, relation_type_group: Optional[str] = None) -> List[
        EntityRelation]:
        to_type = self.get_type(to_id)
        to_id = self.get_id(to_id)
        return self.entity_relation_controller.find_by_to_using_get(to_id=to_id, to_type=to_type,
                                                                    relation_type=relation_type,
                                                                    relation_type_group=relation_type_group)

    def find_info_by_from(self, from_id: EntityId,
                          relation_type_group: Optional[str] = None) -> List[EntityRelationInfo]:
        from_type = self.get_type(from_id)
        from_id = self.get_id(from_id)
        return self.entity_relation_controller.find_info_by_from_using_get(from_id=from_id, from_type=from_type,
                                                                           relation_type_group=relation_type_group)

    def get_relation(self, from_id: EntityId, relation_type: str, to_id: EntityId,
                     relation_type_group: Optional[str] = None) -> EntityRelation:
        from_type = self.get_type(from_id)
        from_id = self.get_id(from_id)

        to_type = self.get_type(to_id)
        to_id = self.get_id(to_id)
        return self.entity_relation_controller.get_relation_using_get(from_id=from_id, from_type=from_type,
                                                                      relation_type=relation_type, to_id=to_id,
                                                                      to_type=to_type,
                                                                      relation_type_group=relation_type_group)

    def find_by_from_v1(self, from_id: EntityId, from_type: str, relation_type_group: Optional[str] = None) -> List[
        EntityRelation]:
        from_id = self.get_id(from_id)
        return self.entity_relation_controller.find_by_from_using_get1(from_id=from_id, from_type=from_type,
                                                                       relation_type_group=relation_type_group)

    def find_by_from(self, from_id: EntityId, relation_type: str,
                     relation_type_group: Optional[str] = None) -> List[EntityRelation]:
        from_type = self.get_type(from_id)
        from_id = self.get_id(from_id)
        return self.entity_relation_controller.find_by_from_using_get(from_id=from_id, from_type=from_type,
                                                                      relation_type=relation_type,
                                                                      relation_type_group=relation_type_group)

    # Entity View Controller
    def get_tenant_entity_view(self, entity_view_name: str) -> EntityView:
        return self.entity_view_controller.get_tenant_entity_view_using_get(entity_view_name=entity_view_name)

    def get_tenant_entity_views(self, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None,
                                sort_property: Optional[str] = None,
                                sort_order: Optional[str] = None) -> PageDataEntityView:
        return self.entity_view_controller.get_tenant_entity_views_using_get(page_size=page_size, page=page, type=type,
                                                                             text_search=text_search,
                                                                             sort_property=sort_property,
                                                                             sort_order=sort_order)

    def get_entity_view_by_id(self, entity_view_id: EntityViewId) -> EntityView:
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.get_entity_view_by_id_using_get(entity_view_id=entity_view_id)

    def find_by_query_v4(self, body: EntityViewSearchQuery) -> List[EntityView]:
        return self.entity_view_controller.find_by_query_using_post4(body=body)

    def get_entity_view_types(self) -> List[EntitySubtype]:
        return self.entity_view_controller.get_entity_view_types_using_get()

    def delete_entity_view(self, entity_view_id: EntityViewId) -> None:
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.delete_entity_view_using_delete(entity_view_id=entity_view_id)

    def get_customer_entity_views(self, customer_id: CustomerId, page_size: int, page: int, type: Optional[str] = None,
                                  text_search: Optional[str] = None,
                                  sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataEntityView:
        customer_id = self.get_id(customer_id)
        return self.entity_view_controller.get_customer_entity_views_using_get(customer_id=customer_id,
                                                                               page_size=page_size, page=page,
                                                                               type=type, text_search=text_search,
                                                                               sort_property=sort_property,
                                                                               sort_order=sort_order)

    # Admin Controller
    def send_test_sms(self, body: Optional[TestSmsRequest] = None) -> None:
        return self.admin_controller.send_test_sms_using_post(body=body)

    def check_updates(self) -> UpdateMessage:
        return self.admin_controller.check_updates_using_get()

    def get_security_settings(self) -> SecuritySettings:
        return self.admin_controller.get_security_settings_using_get()

    def send_test_mail(self, body: Optional[AdminSettings] = None) -> None:
        return self.admin_controller.send_test_mail_using_post(body=body)

    def save_admin_settings(self, body: Optional[AdminSettings] = None) -> AdminSettings:
        return self.admin_controller.save_admin_settings_using_post(body=body)

    def save_security_settings(self, body: Optional[SecuritySettings] = None) -> SecuritySettings:
        return self.admin_controller.save_security_settings_using_post(body=body)

    def get_repository_settings(self) -> RepositorySettings:
        return self.admin_controller.get_repository_settings_using_get()

    def save_repository_settings(self, body: Optional[RepositorySettings] = None) -> DeferredResultRepositorySettings:
        return self.admin_controller.save_repository_settings_using_post(body=body)

    def delete_repository_settings(self) -> DeferredResultVoid:
        return self.admin_controller.delete_repository_settings_using_delete()

    def repository_settings_exists(self) -> bool:
        return self.admin_controller.repository_settings_exists_using_get()

    def check_repository_access(self, body: Optional[RepositorySettings] = None) -> DeferredResultVoid:
        return self.admin_controller.check_repository_access_using_post(body=body)

    def delete_auto_commit_settings(self) -> None:
        return self.admin_controller.delete_auto_commit_settings_using_delete()

    def auto_commit_settings_exists(self) -> bool:
        return self.admin_controller.auto_commit_settings_exists_using_get()

    def save_auto_commit_settings(self, body: Optional[Dict[str, AutoVersionCreateConfig]] = None) -> Dict[str, AutoVersionCreateConfig]:
        return self.admin_controller.save_auto_commit_settings_using_post(body=body)

    def get_auto_commit_settings(self) -> Dict[str, AutoVersionCreateConfig]:
        return self.admin_controller.get_auto_commit_settings_using_get()

    def get_jwt_setting(self) -> JwtSettings:
        return self.admin_controller.get_jwt_settings_using_get()

    def save_jwt_settings(self, body: Optional[JwtSettings] = None) -> JwtPair:
        return self.admin_controller.save_jwt_settings_using_post(body=body)

    # TB Resource Controller
    def get_resource_info_by_id(self, resource_id: EntityId) -> TbResourceInfo:
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.get_resource_info_by_id_using_get(resource_id=resource_id)

    def save_resource(self, body: Optional[TbResource] = None) -> TbResourceInfo:
        return self.tb_resource_controller.save_resource_using_post(body=body)

    def get_resources(self, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None,
                      sort_order: Optional[str] = None) -> PageDataTbResourceInfo:
        return self.tb_resource_controller.get_resources_using_get(page_size=page_size, page=page,
                                                                   text_search=text_search, sort_property=sort_property,
                                                                   sort_order=sort_order)

    def get_lwm2m_list_objects(self, sort_order: str, sort_property: str, object_ids: list) -> List[LwM2mObject]:
        return self.tb_resource_controller.get_lwm2m_list_objects_using_get(sort_order=sort_order,
                                                                            sort_property=sort_property,
                                                                            object_ids=str(object_ids))

    def download_resource(self, resource_id: EntityId) -> ByteArrayResource:
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.download_resource_using_get(resource_id=resource_id)

    def get_lwm2m_list_objects_page(self, page_size: int, page: int, text_search: Optional[str] = None,
                                    sort_property: Optional[str] = None,
                                    sort_order: Optional[str] = None) -> List[LwM2mObject]:
        return self.tb_resource_controller.get_lwm2m_list_objects_page_using_get(page_size=page_size, page=page,
                                                                                 text_search=text_search,
                                                                                 sort_property=sort_property,
                                                                                 sort_order=sort_order)

    def get_tenant_resources(self, page_size: int, page: int, text_search: Optional[str] = None,
                             sort_property: Optional[str] = None,
                             sort_order: Optional[str] = None) -> PageDataTbResourceInfo:
        return self.tb_resource_controller.get_tenant_resources_using_get(page_size=page_size, page=page,
                                                                          text_search=text_search,
                                                                          sort_property=sort_property,
                                                                          sort_order=sort_order)

    def code_processing_url(self, code: str, state: str):
        return self.admin_controller.code_processing_url_using_get(code=code, state=state)

    def get_authorization_url(self) -> str:
        return self.admin_controller.get_authorization_url_using_get()

    def get_mail_processing_url(self) -> str:
        return self.admin_controller.get_mail_processing_url_using_get()

    def download_jks_resource_if_changed(self, resource_id: EntityId,
                                         if_none_match: Optional[str] = '') -> ByteArrayResource:
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.download_jks_resource_if_changed_using_get(resource_id=resource_id,
                                                                                      if_none_match=if_none_match)

    def download_js_resource_if_changed(self, resource_id: EntityId, if_none_match: Optional[str] = '') -> ByteArrayResource:
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.download_js_resource_if_changed_using_get(resource_id=resource_id,
                                                                                     if_none_match=if_none_match)

    def download_lwm2m_resource_if_changed(self, resource_id: EntityId,
                                           if_none_match: Optional[str] = '') -> ByteArrayResource:
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.download_lwm2m_resource_if_changed_using_get(resource_id=resource_id,
                                                                                        if_none_match=if_none_match)

    def download_pkcs12_resource_if_changed(self, resource_id: EntityId,
                                            if_none_match: Optional[str] = '') -> ByteArrayResource:
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.download_pkcs12_resource_if_changed_using_get(resource_id=resource_id,
                                                                                         if_none_match=if_none_match)

    def get_resource_by_id(self, resource_id: EntityId) -> TbResource:
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.get_resource_by_id(resource_id=resource_id)

    def get_repository_settings_info(self) -> RepositorySettingsInfo:
        return self.admin_controller.get_repository_settings_info_using_get()

    # O Auth 2 Controller
    def get_login_processing_url(self) -> str:
        return self.o_auth2_controller.get_login_processing_url_using_get()

    def get_current_o_auth2_info(self) -> OAuth2Info:
        return self.o_auth2_controller.get_current_o_auth2_info_using_get()

    def save_o_auth2_info(self, body: Optional[OAuth2Info] = None) -> OAuth2Info:
        return self.o_auth2_controller.save_o_auth2_info_using_post(body=body)

    def get_o_auth2_clients(self, pkg_name: Optional[str] = None, platform: Optional[str] = None) -> List[OAuth2ClientInfo]:
        return self.o_auth2_controller.get_o_auth2_clients_using_post(pkg_name=pkg_name, platform=platform)

    def delete_oauth2_client(self, id: OAuth2ClientId) -> None:
        id = self.get_id(id)
        return self.o_auth2_controller.delete_oauth2_client(id=id)

    def find_tenant_o_auth2_client_infos(self, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataOAuth2ClientInfo:
        return self.o_auth2_controller.find_tenant_o_auth2_client_infos(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def find_tenant_o_auth2_client_infos_by_ids(self, ids: List[str]) -> List[OAuth2ClientInfo]:
        ids = ','.join(ids)
        return self.o_auth2_controller.find_tenant_o_auth2_client_infos_by_ids(client_ids=ids)

    def get_o_auth2_client_by_id(self, id: OAuth2ClientId) -> OAuth2ClientInfo:
        id = self.get_id(id)
        return self.o_auth2_controller.get_o_auth2_client_by_id(id=id)

    def save_o_auth2_client(self, body: Optional[OAuth2Client] = None) -> OAuth2Client:
        return self.o_auth2_controller.save_o_auth2_client(body=body)

    # Tenant Profile Controller
    def get_default_tenant_profile_info(self) -> EntityInfo:
        return self.tenant_profile_controller.get_default_tenant_profile_info_using_get()

    def save_tenant_profile(self, body: Optional[TenantProfile] = None) -> TenantProfile:
        return self.tenant_profile_controller.save_tenant_profile_using_post(body=body)

    def get_tenant_profiles(self, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None,
                            sort_order: Optional[str] = None) -> PageDataTenantProfile:
        return self.tenant_profile_controller.get_tenant_profiles_using_get(page_size=page_size, page=page,
                                                                            text_search=text_search,
                                                                            sort_property=sort_property,
                                                                            sort_order=sort_order)

    def delete_tenant_profile(self, tenant_profile_id: TenantProfileId) -> None:
        tenant_profile_id = self.get_id(tenant_profile_id)
        return self.tenant_profile_controller.delete_tenant_profile_using_delete(tenant_profile_id=tenant_profile_id)

    def get_tenant_profile_info_by_id(self, tenant_profile_id: TenantProfileId) -> EntityInfo:
        tenant_profile_id = self.get_id(tenant_profile_id)
        return self.tenant_profile_controller.get_tenant_profile_info_by_id_using_get(
            tenant_profile_id=tenant_profile_id)

    def get_tenant_profile_by_id(self, tenant_profile_id: TenantProfileId) -> TenantProfile:
        tenant_profile_id = self.get_id(tenant_profile_id)
        return self.tenant_profile_controller.get_tenant_profile_by_id_using_get(tenant_profile_id=tenant_profile_id)

    def set_default_tenant_profile(self, tenant_profile_id: TenantProfileId) -> TenantProfile:
        tenant_profile_id = self.get_id(tenant_profile_id)
        return self.tenant_profile_controller.set_default_tenant_profile_using_post(tenant_profile_id=tenant_profile_id)

    def get_tenant_profile_infos(self, page_size: int, page: int, text_search: Optional[str] = None,
                                 sort_property: Optional[str] = None,
                                 sort_order: Optional[str] = None) -> PageDataEntityInfo:
        return self.tenant_profile_controller.get_tenant_profile_infos_using_get(page_size=page_size, page=page,
                                                                                 text_search=text_search,
                                                                                 sort_property=sort_property,
                                                                                 sort_order=sort_order)

    # Widgets Bundle Controller
    def update_widgets_bundle_widget_fqns(self, widgets_bundle_id: WidgetsBundleId, body: List[str]):
        widgets_bundle_id = self.get_id(widgets_bundle_id)
        body = ','.join(body)
        return self.widgets_bundle_controller.update_widgets_bundle_widget_fqns_using_post(
            widgets_bundle_id=widgets_bundle_id, body=body)

    def update_widgets_bundle_widget_types(self, widgets_bundle_id: WidgetsBundleId, body: List[str]):
        widgets_bundle_id = self.get_id(widgets_bundle_id)
        body = ','.join(body)
        return self.widgets_bundle_controller.update_widgets_bundle_widget_types_using_post(
            widgets_bundle_id=widgets_bundle_id, body=body)

    def get_widgets_bundle_by_id(self, widgets_bundle_id: WidgetsBundleId,
                                 inline_images: Optional[bool] = None) -> WidgetsBundle:
        widgets_bundle_id = self.get_id(widgets_bundle_id)
        return self.widgets_bundle_controller.get_widgets_bundle_by_id_using_get(widgets_bundle_id=widgets_bundle_id,
                                                                                 inline_images=inline_images)

    def save_widgets_bundle(self, body: Optional[WidgetsBundle] = None) -> WidgetsBundle:
        return self.widgets_bundle_controller.save_widgets_bundle_using_post(body=body)

    def get_widgets_bundles_v1(self, page_size: int, page: int, text_search: Optional[str] = None,
                               sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                               tenant_only: Optional[bool] = None,
                               full_search: Optional[bool] = None) -> PageDataWidgetsBundle:
        return self.widgets_bundle_controller.get_widgets_bundles_using_get1(page_size=page_size, page=page,
                                                                             text_search=text_search,
                                                                             sort_property=sort_property,
                                                                             sort_order=sort_order,
                                                                             tenant_only=tenant_only,
                                                                             full_search=full_search)

    def delete_widgets_bundle(self, widgets_bundle_id: WidgetsBundleId) -> None:
        widgets_bundle_id = self.get_id(widgets_bundle_id)
        return self.widgets_bundle_controller.delete_widgets_bundle_using_delete(widgets_bundle_id=widgets_bundle_id)

    def get_widgets_bundles(self, ):
        return self.widgets_bundle_controller.get_widgets_bundles_using_get()

    # Device Profile Controller
    def get_device_profile_infos(self, page_size: int, page: int, text_search: Optional[str] = None,
                                 sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                                 transport_type: Optional[str] = None) -> PageDataDeviceProfileInfo:
        return self.device_profile_controller.get_device_profile_infos_using_get(page_size=page_size, page=page,
                                                                                 text_search=text_search,
                                                                                 sort_property=sort_property,
                                                                                 sort_order=sort_order,
                                                                                 transport_type=transport_type)

    def set_default_device_profile(self, device_profile_id: DeviceProfileId) -> DeviceProfile:
        device_profile_id = self.get_id(device_profile_id)
        return self.device_profile_controller.set_default_device_profile_using_post(device_profile_id=device_profile_id)

    def delete_device_profile(self, device_profile_id: DeviceProfileId) -> None:
        device_profile_id = self.get_id(device_profile_id)
        return self.device_profile_controller.delete_device_profile_using_delete(device_profile_id=device_profile_id)

    def get_attributes_keys(self, device_profile_id: Optional[DeviceProfileId] = None) -> List[str]:
        device_profile_id = self.get_id(device_profile_id)
        return self.device_profile_controller.get_attributes_keys_using_get(device_profile_id=device_profile_id)

    def save_device_profile(self, body: Optional[DeviceProfile] = None) -> DeviceProfile:
        return self.device_profile_controller.save_device_profile_using_post(body=body)

    def get_default_device_profile_info(self) -> DeviceProfileInfo:
        return self.device_profile_controller.get_default_device_profile_info_using_get()

    def get_timeseries_keys(self, device_profile_id: Optional[DeviceProfileId] = None) -> List[str]:
        device_profile_id = self.get_id(device_profile_id)
        return self.device_profile_controller.get_timeseries_keys_using_get(device_profile_id=device_profile_id)

    def get_device_profile_info_by_id(self, device_profile_id: DeviceProfileId) -> DeviceProfileInfo:
        device_profile_id = self.get_id(device_profile_id)
        return self.device_profile_controller.get_device_profile_info_by_id_using_get(
            device_profile_id=device_profile_id)

    def get_device_profiles(self, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None,
                            sort_order: Optional[str] = None) -> PageDataDeviceProfile:
        return self.device_profile_controller.get_device_profiles_using_get(page_size=page_size, page=page,
                                                                            text_search=text_search,
                                                                            sort_property=sort_property,
                                                                            sort_order=sort_order)

    def get_device_profile_by_id(self, device_profile_id: DeviceProfileId,
                                 inline_images: Optional[bool] = None) -> DeviceProfile:
        device_profile_id = self.get_id(device_profile_id)
        return self.device_profile_controller.get_device_profile_by_id_using_get(device_profile_id=device_profile_id,
                                                                                 inline_images=inline_images)

    # Dashboard Controller
    def get_tenant_dashboards_v1(self, tenant_id: TenantId, page_size: int, page: int, text_search: Optional[str] = None,
                                 sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataDashboardInfo:
        tenant_id = self.get_id(tenant_id)
        return self.dashboard_controller.get_tenant_dashboards_using_get1(tenant_id=tenant_id, page_size=page_size,
                                                                          page=page, text_search=text_search,
                                                                          sort_property=sort_property,
                                                                          sort_order=sort_order)

    def get_dashboard_info_by_id(self, dashboard_id: DashboardId) -> DashboardInfo:
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.get_dashboard_info_by_id_using_get(dashboard_id=dashboard_id)

    def get_home_dashboard(self) -> HomeDashboard:
        return self.dashboard_controller.get_home_dashboard_using_get()

    def set_tenant_home_dashboard_info(self, body: Optional[HomeDashboardInfo] = None) -> None:
        return self.dashboard_controller.set_tenant_home_dashboard_info_using_post(body=body)

    def get_server_time(self) -> int:
        return self.dashboard_controller.get_server_time_using_get()

    def get_highest_alarm_severity(self, entity_id: EntityId, search_status: Optional[str] = None,
                                   status: Optional[str] = None, assignee_id: Optional[str] = None) -> str:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.alarm_controller.get_highest_alarm_severity_using_get(entity_id=entity_id, entity_type=entity_type,
                                                                          search_status=search_status, status=status,
                                                                          assignee_id=assignee_id)

    def get_alarm_types(self, page_size: int, page: int,
                        text_search: Optional[str] = None, sort_order: Optional[str] = None):
        return self.alarm_controller.get_alarm_types_using_get(page_size=page_size, page=page, text_search=text_search,
                                                               sort_order=sort_order)

    def get_max_datapoints_limit(self) -> int:
        return self.dashboard_controller.get_max_datapoints_limit_using_get()

    def get_home_dashboard_info(self) -> HomeDashboardInfo:
        return self.dashboard_controller.get_home_dashboard_info_using_get()

    def get_dashboard_by_id(self, dashboard_id: DashboardId, inline_images: Optional[bool] = None) -> Dashboard:
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.get_dashboard_by_id_using_get(dashboard_id=dashboard_id,
                                                                       inline_images=inline_images)

    def get_tenant_dashboards(self, page_size: int, page: int, mobile: Optional[bool] = None, text_search: Optional[str] = None,
                              sort_property: Optional[str] = None,
                              sort_order: Optional[str] = None) -> PageDataDashboardInfo:
        return self.dashboard_controller.get_tenant_dashboards_using_get(page_size=page_size, page=page, mobile=mobile,
                                                                         text_search=text_search,
                                                                         sort_property=sort_property,
                                                                         sort_order=sort_order)

    def delete_dashboard(self, dashboard_id: DashboardId) -> None:
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.delete_dashboard_using_delete(dashboard_id=dashboard_id)

    def get_tenant_home_dashboard_info(self) -> HomeDashboardInfo:
        return self.dashboard_controller.get_tenant_home_dashboard_info_using_get()

    # Entity Query Controller
    def find_entity_timeseries_and_attributes_keys_by_query(self, timeseries: bool, attributes: bool, body: Optional[
        EntityDataQuery], scope: Optional[str] = None) -> DeferredResultResponseEntity:
        return self.entity_query_controller.find_entity_timeseries_and_attributes_keys_by_query_using_post(
            timeseries=timeseries, attributes=attributes, body=body, scope=scope)

    def find_alarm_data_by_query(self, body: Optional[AlarmDataQuery] = None) -> PageDataAlarmData:
        return self.entity_query_controller.find_alarm_data_by_query_using_post(body=body)

    def find_entity_data_by_query(self, body: Optional[EntityDataQuery] = None) -> PageDataEntityData:
        return self.entity_query_controller.find_entity_data_by_query_using_post(body=body)

    # Widget Type Controller
    def get_bundle_widget_type_fqns(self, widgets_bundle_id: WidgetsBundleId) -> List[str]:
        widgets_bundle_id = self.get_id(widgets_bundle_id)
        return self.widget_type_controller.get_bundle_widget_type_fqns_using_get(widgets_bundle_id=widgets_bundle_id)

    def get_bundle_widget_types_by_bundle_alias(self, is_system: bool, bundle_alias: str) -> List[WidgetType]:
        return self.widget_type_controller.get_bundle_widget_types_by_bundle_alias_using_get(is_system=is_system,
                                                                                             bundle_alias=bundle_alias)

    def get_bundle_widget_types_details_by_bundle_alias(self, is_system: bool, bundle_alias: str) -> List[
        WidgetTypeDetails]:
        return self.widget_type_controller.get_bundle_widget_types_details_by_bundle_alias_using_get(
            is_system=is_system, bundle_alias=bundle_alias)

    def get_bundle_widget_types_infos_by_bundle_alias(self, is_system: bool, bundle_alias: str) -> List[WidgetTypeInfo]:
        return self.widget_type_controller.get_bundle_widget_types_infos_by_bundle_alias_using_get(is_system=is_system,
                                                                                                   bundle_alias=bundle_alias)

    def get_widget_type_by_bundle_alias_and_type_alias(self, is_system: bool, bundle_alias: str, alias: str):
        return self.widget_type_controller.get_widget_type_by_bundle_alias_and_type_alias_using_get(is_system=is_system,
                                                                                                    bundle_alias=bundle_alias,
                                                                                                    alias=alias)

    def get_widget_types(self, page_size: int, page: int,
                         text_search: Optional[str] = None,
                         sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                         tenant_only: Optional[bool] = None, full_search: Optional[bool] = None,
                         deprecated_filter: Optional[str] = None, widget_type_list: Optional[List[str]] = None):
        if widget_type_list:
            widget_type_list = ','.join(widget_type_list)
        return self.widget_type_controller.get_widget_types_using_get(page_size=page_size, page=page,
                                                                      text_search=text_search,
                                                                      sort_property=sort_property,
                                                                      sort_order=sort_order, tenant_only=tenant_only,
                                                                      full_search=full_search,
                                                                      deprecated_filter=deprecated_filter,
                                                                      widget_type_list=widget_type_list)

    def get_widget_type_info_by_id(self, widget_type_id: WidgetTypeId) -> WidgetTypeInfo:
        widget_type_id = self.get_id(widget_type_id)
        return self.widget_type_controller.get_widget_type_info_by_id_using_get(widget_type_id=widget_type_id)

    def get_widget_type(self, fqn) -> WidgetType:
        fqn = str(fqn)
        return self.widget_type_controller.get_widget_type(fqn=fqn)

    def get_bundle_widget_types_infos(self, widgets_bundle_id: WidgetsBundleId, page_size: int, page: int,
                                      text_search: Optional[str] = None,
                                      sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                                      full_search: Optional[bool] = None, deprecated_filter: Optional[str] = None,
                                      widget_type_list: Optional[List[str]] = None) -> List[WidgetTypeInfo]:
        widgets_bundle_id = self.get_id(widgets_bundle_id)

        if widget_type_list:
            widget_type_list = ','.join(widget_type_list)

        return self.widget_type_controller.get_bundle_widget_types_infos_using_get(widgets_bundle_id=widgets_bundle_id,
                                                                                   page_size=page_size, page=page,
                                                                                   text_search=text_search,
                                                                                   sort_property=sort_property,
                                                                                   sort_order=sort_order,
                                                                                   full_search=full_search,
                                                                                   deprecated_filter=deprecated_filter,
                                                                                   widget_type_list=widget_type_list)

    def get_bundle_widget_types_details(self, widgets_bundle_id: WidgetsBundleId,
                                        inline_images: Optional[bool] = None) -> List[WidgetTypeDetails]:
        widgets_bundle_id = self.get_id(widgets_bundle_id)
        return self.widget_type_controller.get_bundle_widget_types_details_using_get(
            widgets_bundle_id=widgets_bundle_id, inline_images=inline_images)

    def delete_widget_type(self, widget_type_id: WidgetTypeId) -> None:
        widget_type_id = self.get_id(widget_type_id)
        return self.widget_type_controller.delete_widget_type_using_delete(widget_type_id=widget_type_id)

    def save_widget_type(self, body: Optional[WidgetTypeDetails] = None,
                         update_existing_by_fqn: Optional[bool] = None) -> WidgetTypeDetails:
        return self.widget_type_controller.save_widget_type_using_post(body=body,
                                                                       update_existing_by_fqn=update_existing_by_fqn)

    def get_bundle_widget_types(self, widgets_bundle_id: WidgetsBundleId) -> List[WidgetType]:
        widgets_bundle_id = self.get_id(widgets_bundle_id)
        return self.widget_type_controller.get_bundle_widget_types_using_get(widgets_bundle_id=widgets_bundle_id)

    def get_widget_type_by_id(self, widget_type_id: WidgetTypeId, inline_images: Optional[bool] = None) -> WidgetType:
        widget_type_id = self.get_id(widget_type_id)
        return self.widget_type_controller.get_widget_type_by_id_using_get(widget_type_id=widget_type_id,
                                                                           inline_images=inline_images)

    # Audit Log Controller
    def get_audit_logs_by_customer_id(self, customer_id: CustomerId, page_size: int, page: int,
                                      text_search: Optional[str] = None,
                                      sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                                      start_time: Optional[int] = None, end_time: Optional[int] = None,
                                      action_types: Optional[str] = None) -> PageDataAuditLog:
        customer_id = self.get_id(customer_id)
        return self.audit_log_controller.get_audit_logs_by_customer_id_using_get(customer_id=customer_id,
                                                                                 page_size=page_size, page=page,
                                                                                 text_search=text_search,
                                                                                 sort_property=sort_property,
                                                                                 sort_order=sort_order,
                                                                                 start_time=start_time,
                                                                                 end_time=end_time,
                                                                                 action_types=action_types)

    def get_audit_logs_by_user_id(self, user_id: UserId, page_size: int, page: int, text_search: Optional[str] = None,
                                  sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None,
                                  end_time: Optional[int] = None,
                                  action_types: Optional[str] = None) -> PageDataAuditLog:
        user_id = self.get_id(user_id)
        return self.audit_log_controller.get_audit_logs_by_user_id_using_get(user_id=user_id, page_size=page_size,
                                                                             page=page, text_search=text_search,
                                                                             sort_property=sort_property,
                                                                             sort_order=sort_order,
                                                                             start_time=start_time, end_time=end_time,
                                                                             action_types=action_types)

    def get_audit_logs(self, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None,
                       sort_order: Optional[str] = None,
                       start_time: Optional[int] = None, end_time: Optional[int] = None,
                       action_types: Optional[str] = None) -> PageDataAuditLog:
        return self.audit_log_controller.get_audit_logs_using_get(page_size=page_size, page=page,
                                                                  text_search=text_search, sort_property=sort_property,
                                                                  sort_order=sort_order, start_time=start_time,
                                                                  end_time=end_time, action_types=action_types)

    def get_audit_logs_by_entity_id(self, entity_id: EntityId, page_size: int, page: int,
                                    text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                                    start_time: Optional[int] = None,
                                    end_time: Optional[int] = None, action_types: Optional[str] = None) -> PageDataAuditLog:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.audit_log_controller.get_audit_logs_by_entity_id_using_get(entity_type=entity_type,
                                                                               entity_id=entity_id, page_size=page_size,
                                                                               page=page, text_search=text_search,
                                                                               sort_property=sort_property,
                                                                               sort_order=sort_order,
                                                                               start_time=start_time, end_time=end_time,
                                                                               action_types=action_types)

    # Lwm2M Controller
    def get_lwm2m_bootstrap_security_info(self, is_bootstrap_server: bool) -> ServerSecurityConfig:
        return self.lwm2m_controller.get_lwm2m_bootstrap_security_info_using_get(
            is_bootstrap_server=is_bootstrap_server)

    # Component Descriptor Controller
    def get_component_descriptors_by_type(self, component_type: str,
                                          rule_chain_type: Optional[str] = None) -> List[ComponentDescriptor]:
        return self.component_descriptor_controller.get_component_descriptors_by_type_using_get(
            component_type=component_type, rule_chain_type=rule_chain_type)

    def get_component_descriptor_by_clazz(self, component_descriptor_clazz: str) -> ComponentDescriptor:
        return self.component_descriptor_controller.get_component_descriptor_by_clazz_using_get(
            component_descriptor_clazz=component_descriptor_clazz)

    def get_component_descriptors_by_types(self, component_types: str,
                                           rule_chain_type: Optional[str] = None) -> List[ComponentDescriptor]:
        return self.component_descriptor_controller.get_component_descriptors_by_types_using_get(
            component_types=component_types, rule_chain_type=rule_chain_type)

    # UI Controller
    def get_help_base_url(self) -> str:
        return self.ui_settings_controller.get_help_base_url_using_get()

    # Device API Controller
    def subscribe_to_attributes(self, device_token: str, timeout: Optional[int] = None) -> DeferredResultResponseEntity:
        return self.device_api_controller.subscribe_to_attributes_using_get(device_token=device_token, timeout=timeout)

    def subscribe_to_commands(self, device_token: str, timeout: Optional[int] = None) -> DeferredResultResponseEntity:
        return self.device_api_controller.subscribe_to_commands_using_get(device_token=device_token, timeout=timeout)

    def get_device_attributes(self, device_token: str, client_keys: str,
                              shared_keys: str) -> DeferredResultResponseEntity:
        return self.device_api_controller.get_device_attributes_using_get(device_token=device_token,
                                                                          client_keys=client_keys,
                                                                          shared_keys=shared_keys)

    def get_firmware(self, device_token: str, title: str, version: str, size: Optional[int] = None,
                     chunk: Optional[int] = None) -> DeferredResultResponseEntity:
        return self.device_api_controller.get_firmware_using_get(device_token=device_token, title=title,
                                                                 version=version, size=size, chunk=chunk)

    def reply_to_command(self, device_token: str, request_id: int,
                         body: Optional[str] = None) -> DeferredResultResponseEntity:
        return self.device_api_controller.reply_to_command_using_post(device_token=device_token, request_id=request_id,
                                                                      body=body)

    def get_software(self, device_token: str, title: str, version: str, size: Optional[int] = None,
                     chunk: Optional[int] = None) -> DeferredResultResponseEntity:
        return self.device_api_controller.get_software_using_get(device_token=device_token, title=title,
                                                                 version=version, size=size, chunk=chunk)

    def post_telemetry(self, device_token: str, body: Optional[str] = None) -> DeferredResultResponseEntity:
        return self.device_api_controller.post_telemetry_using_post(device_token=device_token, body=body)

    def claim_device(self, device_token: str, body: Optional[str] = None) -> DeferredResultResponseEntity:
        return self.device_api_controller.claim_device_using_post(device_token=device_token, body=body)

    def post_rpc_request(self, device_token: str, body: Optional[Dict] = None) -> DeferredResultResponseEntity:
        return self.device_api_controller.post_rpc_request_using_post(device_token=device_token, body=body)

    def provision_device(self, body: Optional[str] = None) -> DeferredResultResponseEntity:
        return self.device_api_controller.provision_device_using_post(body=body)

    def post_device_attributes(self, device_token: str, body: Optional[str] = None) -> DeferredResultResponseEntity:
        return self.device_api_controller.post_device_attributes_using_post(device_token=device_token, body=body)

    # Tenant Controller
    def get_tenant_infos(self, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None,
                         sort_order: Optional[str] = None) -> PageDataTenantInfo:
        return self.tenant_controller.get_tenant_infos_using_get(page_size=page_size, page=page,
                                                                 text_search=text_search, sort_property=sort_property,
                                                                 sort_order=sort_order)

    def get_tenant_by_id(self, tenant_id: TenantId) -> Tenant:
        tenant_id = self.get_id(tenant_id)
        return self.tenant_controller.get_tenant_by_id_using_get(tenant_id=tenant_id)

    def save_tenant(self, body: Optional[Tenant] = None) -> Tenant:
        return self.tenant_controller.save_tenant_using_post(body=body)

    def get_tenants(self, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None,
                    sort_order: Optional[str] = None) -> PageDataTenant:
        return self.tenant_controller.get_tenants_using_get(page_size=page_size, page=page, text_search=text_search,
                                                            sort_property=sort_property, sort_order=sort_order)

    def get_tenant_info_by_id(self, tenant_id: TenantId) -> TenantInfo:
        tenant_id = self.get_id(tenant_id)
        return self.tenant_controller.get_tenant_info_by_id_using_get(tenant_id=tenant_id)

    def delete_tenant(self, tenant_id: TenantId) -> None:
        tenant_id = self.get_id(tenant_id)
        return self.tenant_controller.delete_tenant_using_delete(tenant_id=tenant_id)

    # OTA Package Controller
    def delete_ota_package(self, ota_package_id: OtaPackageId) -> None:
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.delete_ota_package_using_delete(ota_package_id=ota_package_id)

    def save_ota_package_data(self, ota_package_id: OtaPackageId, checksum: Optional[str] = None,
                              checksum_algorithm: Optional[str] = None, file: Optional[str] = None) -> OtaPackageInfo:
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.save_ota_package_data_using_post(ota_package_id=ota_package_id,
                                                                            checksum=checksum,
                                                                            checksum_algorithm=checksum_algorithm,
                                                                            file=file)

    def get_ota_packages_v1(self, device_profile_id: DeviceProfileId, type: str, page_size: int, page: int,
                            text_search: Optional[str] = None, sort_property: Optional[str] = None,
                            sort_order: Optional[str] = None) -> PageDataOtaPackageInfo:
        device_profile_id = self.get_id(device_profile_id)
        return self.ota_package_controller.get_ota_packages_using_get1(device_profile_id=device_profile_id, type=type,
                                                                       page_size=page_size, page=page,
                                                                       text_search=text_search,
                                                                       sort_property=sort_property,
                                                                       sort_order=sort_order)

    def save_ota_package_info(self, body: Optional[SaveOtaPackageInfoRequest] = None) -> OtaPackageInfo:
        return self.ota_package_controller.save_ota_package_info_using_post(body=body)

    def get_ota_packages(self, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None,
                         sort_order: Optional[str] = None) -> PageDataOtaPackageInfo:
        return self.ota_package_controller.get_ota_packages_using_get(page_size=page_size, page=page,
                                                                      text_search=text_search,
                                                                      sort_property=sort_property,
                                                                      sort_order=sort_order)

    def get_ota_package_by_id(self, ota_package_id: OtaPackageId) -> OtaPackage:
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.get_ota_package_by_id_using_get(ota_package_id=ota_package_id)

    def download_ota_package(self, ota_package_id: OtaPackageId) -> Resource:
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.download_ota_package_using_get(ota_package_id=ota_package_id)

    def get_ota_package_info_by_id(self, ota_package_id: OtaPackageId) -> OtaPackageInfo:
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.get_ota_package_info_by_id_using_get(ota_package_id=ota_package_id)

    def save_entities_version(self, body: Optional[VersionCreateRequest] = None) -> str:
        return self.entities_version_control_controller.save_entities_version_using_post(body=body)

    def get_version_load_request_status(self, request_id: str) -> VersionLoadResult:
        return self.entities_version_control_controller.get_version_load_request_status_using_get(request_id=request_id)

    def list_branches(self):
        return self.entities_version_control_controller.list_branches_using_get()

    def list_entity_versions(self, entity_type: str, external_entity_uuid: str, branch: str, page_size: int, page: int,
                             text_search: Optional[str] = None, sort_property: Optional[str] = None,
                             sort_order: Optional[str] = None):
        return self.entities_version_control_controller.list_entity_versions_using_get(entity_type=entity_type,
                                                                                       external_entity_uuid=external_entity_uuid,
                                                                                       branch=branch,
                                                                                       page_size=page_size, page=page,
                                                                                       text_search=text_search,
                                                                                       sort_property=sort_property,
                                                                                       sort_order=sort_order)

    def get_entity_data_info(self, version_id: str, entity_id: EntityId):
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.entities_version_control_controller.get_entity_data_info_using_get(version_id=version_id,
                                                                                       entity_type=entity_type,
                                                                                       external_entity_uuid=entity_id)

    def get_version_create_request_status(self, request_id: str) -> VersionCreationResult:
        return self.entities_version_control_controller.get_version_create_request_status_using_get(
            request_id=request_id)

    def load_entities_version(self, body: Optional[VersionLoadRequest] = None) -> str:
        return self.entities_version_control_controller.load_entities_version_using_post(body=body)

    def list_entity_type_versions(self, entity_type: str, branch: str, page_size: int, page: int,
                                  text_search: Optional[str] = None,
                                  sort_property: Optional[str] = None,
                                  sort_order: Optional[str] = None):
        return self.entities_version_control_controller.list_entity_type_versions_using_get(entity_type=entity_type,
                                                                                            branch=branch,
                                                                                            page_size=page_size,
                                                                                            page=page,
                                                                                            text_search=text_search,
                                                                                            sort_property=sort_property,
                                                                                            sort_order=sort_order)

    def list_entities_at_version(self, entity_type: str, version_id: str):
        return self.entities_version_control_controller.list_entities_at_version_using_get(entity_type=entity_type,
                                                                                           version_id=version_id)

    def list_all_entities_at_version(self, version_id: str):
        return self.entities_version_control_controller.list_all_entities_at_version_using_get(version_id=version_id)

    def compare_entity_data_to_version(self, entity_id: EntityId,
                                       version_id: str):
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.entities_version_control_controller.compare_entity_data_to_version_using_get(
            entity_type=entity_type, internal_entity_uuid=entity_id, version_id=version_id)

    def list_versions(self, branch: str, page_size: int, page: int, text_search: Optional[str] = None,
                      sort_property: Optional[str] = None,
                      sort_order: Optional[str] = None):
        return self.entities_version_control_controller.list_versions_using_get(branch=branch, page_size=page_size,
                                                                                page=page, text_search=text_search,
                                                                                sort_property=sort_property,
                                                                                sort_order=sort_order)

    def delete_queue(self, queue_id: QueueId) -> None:
        queue_id = self.get_id(queue_id)
        return self.queue_controller.delete_queue_using_delete(queue_id=queue_id)

    def get_queue_by_id(self, queue_id: QueueId) -> Queue:
        queue_id = self.get_id(queue_id)
        return self.queue_controller.get_queue_by_id_using_get(queue_id=queue_id)

    def get_queue_by_name(self, queue_name: str) -> Queue:
        return self.queue_controller.get_queue_by_name_using_get(queue_name=queue_name)

    # Two-Factor Auth Controller
    def check_two_fa_verification_code(self, provider_type: str, verification_code: str) -> JwtPair:
        return self.two_factor_auth_controller.check_two_fa_verification_code_using_post(provider_type=provider_type,
                                                                                         verification_code=verification_code)

    def get_available_two_fa_providers_v1(self, ) -> List[TwoFaProviderInfo]:
        return self.two_factor_auth_controller.get_available_two_fa_providers_using_get1()

    def request_two_fa_verification_code(self, provider_type: str) -> None:
        return self.two_factor_auth_controller.request_two_fa_verification_code_using_post(provider_type=provider_type)

    # Tow Factor Auth Config Controller
    def delete_two_fa_account_config(self, provider_type: str) -> AccountTwoFaSettings:
        return self.two_factor_auth_config_controller.delete_two_fa_account_config_using_delete(provider_type=provider_type)

    def generate_two_fa_account_config(self, provider_type: str) -> TwoFaAccountConfig:
        return self.two_factor_auth_config_controller.generate_two_fa_account_config_using_post(provider_type=provider_type)

    def get_account_two_fa_settings(self) -> AccountTwoFaSettings:
        return self.two_factor_auth_config_controller.get_account_two_fa_settings_using_get()

    def get_available_two_fa_providers(self) -> List[str]:
        return self.two_factor_auth_config_controller.get_available_two_fa_providers_using_get()

    def get_platform_two_fa_settings(self) -> PlatformTwoFaSettings:
        return self.two_factor_auth_config_controller.get_platform_two_fa_settings_using_get()

    def save_platform_two_fa_settings(self, body: PlatformTwoFaSettings) -> PlatformTwoFaSettings:
        return self.two_factor_auth_config_controller.save_platform_two_fa_settings_using_post(body=body)

    def submit_two_fa_account_config(self, body: TwoFaAccountConfig):
        return self.two_factor_auth_config_controller.submit_two_fa_account_config_using_post(body=body)

    def update_two_fa_account_config(self, provider_type: str,
                                     body: TwoFaAccountConfigUpdateRequest) -> AccountTwoFaSettings:
        return self.two_factor_auth_config_controller.update_two_fa_account_config_using_put(
            provider_type=provider_type, body=body)

    def verify_and_save_two_fa_account_config(self, body: TwoFaAccountConfig,
                                              verification_code: str) -> AccountTwoFaSettings:
        return self.two_factor_auth_config_controller.verify_and_save_two_fa_account_config_using_post(body=body,
                                                                                                       verification_code=verification_code)

    def create_notification_request(self, body: NotificationRequest) -> NotificationRequest:
        return self.notification_controller.create_notification_request_using_post(body=body)

    def delete_notification_request(self, id: str):
        return self.notification_controller.delete_notification_request_using_delete(id=id)

    def delete_notification(self, id: str):
        return self.notification_controller.delete_notification_using_delete(id=id)

    def get_available_delivery_methods(self) -> List[str]:
        return self.notification_controller.get_available_delivery_methods_using_get()

    def get_notification_request_by_id(self, id: str) -> NotificationRequestInfo:
        return self.notification_controller.get_notification_request_by_id_using_get(id=id)

    def get_notification_request_preview(self, body: NotificationRequest,
                                         recipients_preview_size: Optional[int] = None):
        return self.notification_controller.get_notification_request_preview_using_post(body=body,
                                                                                        recipients_preview_size=recipients_preview_size)

    def get_notification_requests(self, page_size: int, page: int, text_search: Optional[str] = None,
                                  sort_property: Optional[str] = None,
                                  sort_order: Optional[str] = None) -> PageDataNotificationRequestInfo:
        return self.notification_controller.get_notification_requests_using_get(page_size=page_size, page=page,
                                                                                text_search=text_search,
                                                                                sort_property=sort_property,
                                                                                sort_order=sort_order)

    def get_notification_settings(self) -> NotificationSettings:
        return self.notification_controller.get_notification_settings_using_get()

    def get_notifications(self, page_size: int, page: int, text_search: Optional[str] = None,
                          sort_property: Optional[str] = None,
                          sort_order: Optional[str] = None, delivery_method: Optional[str] = None) -> PageDataNotification:
        return self.notification_controller.get_notifications_using_get(page_size=page_size, page=page,
                                                                        text_search=text_search,
                                                                        sort_property=sort_property,
                                                                        sort_order=sort_order,
                                                                        delivery_method=delivery_method)

    def get_unread_notifications_count(self, delivery_method: Optional[str] = None) -> int:
        return self.notification_controller.get_unread_notifications_count(delivery_method=delivery_method)

    def mark_all_notifications_as_read(self):
        return self.notification_controller.mark_all_notifications_as_read_using_put()

    def mark_notification_as_read(self, id: str):
        return self.notification_controller.mark_notification_as_read_using_put(id=id)

    def save_notification_settings(self, body: NotificationSettings) -> NotificationSettings:
        return self.notification_controller.save_notification_settings_using_post(body=body)

    def get_user_notification_settings(self) -> UserNotificationSettings:
        return self.notification_controller.get_user_notification_settings_using_get()

    def save_user_notification_settings(self, body: UserNotificationSettings) -> UserNotificationSettings:
        return self.notification_controller.save_user_notification_settings_using_post(body=body)

    def delete_notification_rule(self, id: str):
        return self.notification_rule_controller.delete_notification_rule_using_delete(id=id)

    def get_notification_rule_by_id(self, id: str) -> NotificationRuleInfo:
        return self.notification_rule_controller.get_notification_rule_by_id_using_get(id=id)

    def get_notification_rules(self, page_size: int, page: int, text_search: Optional[str] = None,
                               sort_property: Optional[str] = None,
                               sort_order: Optional[str] = None) -> PageDataNotificationRuleInfo:
        return self.notification_rule_controller.get_notification_rules_using_get(page_size=page_size, page=page,
                                                                                  text_search=text_search,
                                                                                  sort_property=sort_property,
                                                                                  sort_order=sort_order)

    def save_notification_rule(self, body: NotificationRule) -> NotificationRule:
        return self.notification_rule_controller.save_notification_rule_using_post(body=body)

    def delete_notification_target_by_id(self, id: str):
        return self.notification_target_controller.delete_notification_target_by_id_using_delete(id=id)

    def get_notification_target_by_id(self, id: str) -> NotificationTarget:
        return self.notification_target_controller.get_notification_target_by_id_using_get(id=id)

    def get_notification_targets_by_ids(self, ids: list) -> List[NotificationTarget]:
        ids = ','.join(ids)
        return self.notification_target_controller.get_notification_targets_by_ids_using_get(ids=ids)

    def get_notification_targets_by_supported_notification_type(self, notification_type: str, page_size: int, page: int,
                                                                text_search: Optional[str] = None,
                                                                sort_property: Optional[str] = None,
                                                                sort_order: Optional[
                                                                    str] = None) -> PageDataNotificationTarget:
        return self.notification_target_controller.get_notification_targets_by_supported_notification_type_using_get(
            notification_type=notification_type, page_size=page_size, page=page, text_search=text_search,
            sort_property=sort_property, sort_order=sort_order)

    def get_notification_targets(self, page_size: int, page: int, text_search: Optional[str] = None,
                                 sort_property: Optional[str] = None,
                                 sort_order: Optional[str] = None) -> PageDataNotificationTarget:
        return self.notification_target_controller.get_notification_targets_using_get(page_size=page_size, page=page,
                                                                                      text_search=text_search,
                                                                                      sort_property=sort_property,
                                                                                      sort_order=sort_order)

    def get_recipients_for_notification_target_config(self, page_size: int, page: int):
        return self.notification_target_controller.get_recipients_for_notification_target_config_using_post(
            page_size=page_size, page=page)

    def save_notification_target(self, body: NotificationTarget) -> NotificationTarget:
        return self.notification_target_controller.save_notification_target_using_post(body=body)

    def delete_notification_template_by_id(self, id: str):
        return self.notification_template_controller.delete_notification_template_by_id_using_delete(id=id)

    def get_notification_template_by_id(self, id: str) -> NotificationTemplate:
        return self.notification_template_controller.get_notification_template_by_id_using_get(id=id)

    def get_notification_templates(self, page_size: int, page: int, text_search: Optional[str] = None,
                                   sort_property: Optional[str] = None,
                                   sort_order: Optional[str] = None) -> PageDataNotificationTemplate:
        return self.notification_template_controller.get_notification_templates_using_get(page_size=page_size,
                                                                                          page=page,
                                                                                          text_search=text_search,
                                                                                          sort_property=sort_property,
                                                                                          sort_order=sort_order)

    def list_slack_conversations(self, type: str, token: Optional[str] = None) -> List[SlackConversation]:
        return self.notification_template_controller.list_slack_conversations_using_get(type=type, token=token)

    def save_notification_template(self, body: NotificationTemplate) -> NotificationTemplate:
        return self.notification_template_controller.save_notification_template_using_post(body=body)

    def count_entities_by_query(self, body: Optional[EntityCountQuery] = None) -> int:
        return self.entity_query_controller.count_entities_by_query_using_post(body=body)

    # Device Connectivity Controller
    def download_server_certificate(self, protocol: str) -> Resource:
        return self.device_connectivity_controller.download_server_certificate_using_get(protocol=protocol)

    def get_device_publish_telemetry_commands(self, device_id: DeviceId):
        device_id = self.get_id(device_id)
        return self.device_connectivity_controller.get_device_publish_telemetry_commands_using_get(device_id=device_id)

    # Mail Config Template Controller
    def get_client_registration_templates_mail(self):
        return self.mail_config_template_controller.get_client_registration_templates_using_get()

    # Image Controller
    def delete_image(self, _type: str, key: str, force: Optional[bool] = None) -> TbImageDeleteResult:
        return self.image_controller.delete_image_using_delete(type=_type, key=key, force=force)

    def download_image_preview(self, _type: str, key: str, if_none_match: Optional[str] = '') -> ByteArrayResource:
        return self.image_controller.download_image_preview_using_get(type=_type, key=key, if_none=if_none_match)

    def download_image(self, _type: str, key: str, if_none_match: Optional[str] = '') -> ByteArrayResource:
        return self.image_controller.download_image_using_get(type=_type, key=key, if_none_match=if_none_match)

    def download_public_image(self, public_resource_key: str, if_none_match: Optional[str] = '') -> ByteArrayResource:
        return self.image_controller.download_public_image_using_get(public_resource_key=public_resource_key,
                                                                     if_none_match=if_none_match)

    def export_image(self, _type: str, key: str) -> ImageExportData:
        return self.image_controller.export_image_using_get(type=_type, key=key)

    def get_image_info(self, _type: str, key: str) -> TbResourceInfo:
        return self.image_controller.get_image_info_using_get(type=_type, key=key)

    def get_images(self, page_size: int, page: int, text_search: Optional[str] = None,
                   include_system_images: Optional[bool] = None,
                   sort_property: Optional[str] = None,
                   sort_order: Optional[str] = None) -> PageDataTbResourceInfo:
        return self.image_controller.get_images_using_get(page_size=page_size, page=page, text_search=text_search,
                                                          include_system_images=include_system_images,
                                                          sort_order=sort_order, sort_property=sort_property)

    def import_image(self, body: ImageExportData) -> TbResourceInfo:
        return self.image_controller.import_image_using_put(body=body)

    def update_image_info(self, _type: str, key: str, body: TbResourceInfo) -> TbResourceInfo:
        return self.image_controller.update_image_info_using_put(type=_type, key=key, body=body)

    def update_image_public_status(self, _type: str, key: str, is_public: Optional[bool] = None) -> TbResourceInfo:
        return self.image_controller.update_image_public_status_using_put(type=_type, key=key, is_public=is_public)

    def update_image(self, _type: str, key: str, file: str) -> TbResourceInfo:
        return self.image_controller.update_image_using_put(type=_type, key=key, file=file)

    def upload_image(self, title: str, file: str) -> TbResourceInfo:
        return self.image_controller.upload_image_using_post(title=title, file=file)

    def get_asset_profile_by_id(self, asset_profile_id: str, inline_images: Optional[bool] = None) -> AssetProfile:
        return self.asset_profile_controller.get_asset_profile_by_id_using_get(asset_profile_id=asset_profile_id,
                                                                               inline_images=inline_images)

    def get_asset_profile_by_names(self, active_only: Optional[bool]) -> List[EntityInfo]:
        return self.asset_profile_controller.get_asset_profile_names_using_get(active_only=active_only)

    def download_gateway_docker_compose(self, device_id: DeviceId) -> Resource:
        device_id = self.get_id(device_id)
        return self.device_connectivity_controller.download_gateway_docker_compose_using_get(device_id=device_id)

    def get_device_profile_names(self, active_only: Optional[bool]) -> List[EntityInfo]:
        return self.device_profile_controller.get_device_profile_names_using_get(active_only=active_only)

    def get_edge_install_instructions(self, edge_id: EdgeId, method: str) -> EdgeInstructions:
        edge_id = self.get_id(edge_id)
        return self.edge_controller.get_edge_install_instructions_using_get(edge_id=edge_id, method=method)

    def get_edge_upgrade_instructions(self, edge_version: str, method: str) -> EdgeInstructions:
        return self.edge_controller.get_edge_upgrade_instructions_using_get(edge_version=edge_version, method=method)

    def is_edge_upgrade_available(self, edge_id: EdgeId) -> bool:
        edge_id = self.get_id(edge_id)
        return self.edge_controller.is_edge_upgrade_available_using_get(edge_id=edge_id)

    def get_application_redirect(self, user_agent: str):
        return self.mobile_application_controller.get_application_redirect(user_agent=user_agent)

    def get_mobile_app_deep_link(self) -> str:
        return self.mobile_application_controller.get_mobile_app_deep_link()

    def get_mobile_app_settings(self) -> MobileAppSettings:
        return self.mobile_application_controller.get_mobile_app_settings()

    def get_user_token_by_mobile_secret(self, secret: str) -> JwtPair:
        return self.mobile_application_controller.get_user_token_by_mobile_secret(secret=secret)

    def save_mobile_app_settings(self, body: MobileAppSettings) -> MobileAppSettings:
        return self.mobile_application_controller.save_mobile_app_settings(body=body)

    def get_queue_stats_by_id(self, queue_stats_id: QueueId) -> QueueStats:
        queue_stats_id = self.get_id(queue_stats_id)
        return self.queue_stats_controller.get_queue_stats_by_id(queue_stats_id=queue_stats_id)

    def get_queue_stats_by_ids(self, queue_stats_ids: List[str]) -> List[QueueStats]:
        queue_stats_ids = ','.join(queue_stats_ids)
        return self.queue_stats_controller.get_queue_stats_by_ids(queue_stats_ids=queue_stats_ids)

    def get_tenant_queue_stats(self, page_size: int, page: int, text_search: Optional[str] = None,
                               sort_property: Optional[str] = None,
                               sort_order: Optional[str] = None) -> List[QueueStats]:
        return self.queue_stats_controller.get_tenant_queue_stats(page_size=page_size, page=page,
                                                                  text_search=text_search, sort_property=sort_property,
                                                                  sort_order=sort_order)

    def delete_domain(self, domain_id: DomainId) -> None:
        domain_id = self.get_id(domain_id)
        return self.domain_controller.delete_domain(id=domain_id)

    def get_domain_info_by_id(self, domain_id: DomainId) -> DomainInfo:
        domain_id = self.get_id(domain_id)
        return self.domain_controller.get_domain_info_by_id(id=domain_id)

    def get_tenant_domain_infos(self, page_size: int, page: int, text_search: Optional[str] = None,
                                sort_property: Optional[str] = None,
                                sort_order: Optional[str] = None) -> PageDataDomainInfo:
        return self.domain_controller.get_tenant_domain_infos(page_size=page_size, page=page, text_search=text_search,
                                                              sort_property=sort_property, sort_order=sort_order)

    def save_domain(self, body: Domain, oauth2_client_ids: Optional[str] = None) -> Domain:
        if oauth2_client_ids is not None:
            oauth2_client_ids = ','.join(oauth2_client_ids)
        return self.domain_controller.save_domain(body=body, oauth2_client_ids=oauth2_client_ids)

    def update_oauth2_clients(self, body: List[str], id: str):
        return self.domain_controller.update_oauth2_clients(body=body, id=id)

    def delete_mobile_app(self, mobile_app_id: MobileAppId) -> None:
        mobile_app_id = self.get_id(mobile_app_id)
        return self.mobile_app_controller.delete_mobile_app(id=mobile_app_id)

    def get_mobile_app_info_by_id(self, mobile_app_id: MobileAppId) -> MobileAppInfo:
        mobile_app_id = self.get_id(mobile_app_id)
        return self.mobile_app_controller.get_mobile_app_info_by_id(id=mobile_app_id)

    def get_tenant_mobile_app_infos(self, page_size: int, page: int, text_search: Optional[str] = None,
                                    sort_property: Optional[str] = None,
                                    sort_order: Optional[str] = None) -> PageDataMobileAppInfo:
        return self.mobile_app_controller.get_tenant_mobile_app_infos(page_size=page_size, page=page,
                                                                      text_search=text_search,
                                                                      sort_property=sort_property,
                                                                      sort_order=sort_order)

    def save_mobile_app(self, body: MobileApp, oauth2_client_ids: Optional[str] = None) -> MobileApp:
        if oauth2_client_ids is not None:
            oauth2_client_ids = ','.join(oauth2_client_ids)
        return self.mobile_app_controller.save_mobile_app(body=body, oauth2_client_ids=oauth2_client_ids)

    def mobile_app_update_oauth2_clients(self, body: List[str], id: str):
        return self.mobile_app_controller.update_oauth2_clients(body=body, id=id)

    def get_qr_code_settings(self) -> QrCodeSettings:
        return self.qr_code_settings_controller.get_qr_code_settings()

    def save_qr_code_settings(self, body: QrCodeSettings) -> QrCodeSettings:
        return self.qr_code_settings_controller.save_qr_code_settings(body=body)

    def delete_mobile_app_bundle(self, mobile_app_bundle_id: MobileAppBundleId):
        mobile_app_bundle_id = self.get_id(mobile_app_bundle_id)
        return self.mobile_app_bundle_controller.delete_mobile_app_bundle(id=mobile_app_bundle_id)

    def get_mobile_app_bundle_info_by_id(self, mobile_app_bundle_id: MobileAppBundleId) -> MobileAppBundleInfo:
        mobile_app_bundle_id = self.get_id(mobile_app_bundle_id)
        return self.mobile_app_bundle_controller.get_mobile_app_bundle_info_by_id(id=mobile_app_bundle_id)

    def get_tenant_mobile_app_bundle_infos(self, page_size: int, page: int, text_search: Optional[str] = None,
                                           sort_property: Optional[str] = None,
                                           sort_order: Optional[str] = None) -> PageDataMobileAppBundleInfo:
        return self.mobile_app_bundle_controller.get_tenant_mobile_app_bundle_infos(page_size=page_size, page=page,
                                                                                    text_search=text_search,
                                                                                    sort_property=sort_property,
                                                                                    sort_order=sort_order)

    def save_mobile_app_bundle(self, body: MobileAppBundle, oauth2_client_ids: Optional[List] = None) -> MobileAppBundle:
        if oauth2_client_ids:
            oauth2_client_ids = ','.join(oauth2_client_ids)

        return self.mobile_app_bundle_controller.save_mobile_app_bundle(body=body, oauth2_client_ids=oauth2_client_ids)

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
        self.device_api_controller = DeviceApiControllerApi(self.api_client)
        self.rule_chain_controller = RuleChainControllerApi(self.api_client)
        self.tb_resource_controller = TbResourceControllerApi(self.api_client)
        self.auth_controller = AuthControllerApi(self.api_client)
        self.queue_controller = QueueControllerApi(self.api_client)
        self.ota_package_controller = OtaPackageControllerApi(self.api_client)
        self.alarm_controller = AlarmControllerApi(self.api_client)
        self.edge_event_controller = EdgeEventControllerApi(self.api_client)
        self.ui_settings_controller = UiSettingsControllerApi(self.api_client)
        self.entities_version_control_controller = EntitiesVersionControlControllerApi(self.api_client)
        self.two_factor_auth_controller = TwoFactorAuthControllerApi(self.api_client)
        self.alarm_comment_controller = AlarmCommentControllerApi(self.api_client)
        self.notification_target_controller = NotificationTargetControllerApi(self.api_client)
        self.usage_info_controller = UsageInfoControllerApi(self.api_client)
        self.notification_rule_controller = NotificationRuleControllerApi(self.api_client)
        self.notification_controller = NotificationControllerApi(self.api_client)
        self.notification_template_controller = NotificationTemplateControllerApi(self.api_client)
        self.asset_profile_controller = AssetProfileControllerApi(self.api_client)
        self.two_factor_auth_config_controller = TwoFactorAuthConfigControllerApi(self.api_client)
        self.device_connectivity_controller = DeviceConnectivityControllerApi(self.api_client)
        self.mail_config_template_controller = MailConfigTemplateControllerApi(self.api_client)
        self.image_controller = ImageControllerApi(self.api_client)
        self.mobile_application_controller = MobileApplicationControllerApi(self.api_client)
        self.queue_stats_controller = QueueStatsControllerApi(self.api_client)
        self.domain_controller = DomainControllerApi(self.api_client)
        self.mobile_app_controller = MobileAppControllerApi(self.api_client)
        self.mobile_app_bundle_controller = MobileAppBundleControllerApi(self.api_client)
        self.rule_engine_controller = RuleEngineControllerApi(self.api_client)
        self.qr_code_settings_controller = QrCodeSettingsControllerApi(self.api_client)

    @staticmethod
    def get_type(type):
        return type.entity_type if hasattr(type, "entity_type") else type

    @staticmethod
    def get_id(id):
        return id.id if hasattr(id, "id") else id
