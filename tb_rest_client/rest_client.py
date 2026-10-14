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


from __future__ import annotations

import json
import jwt
from time import time, sleep

from requests import post
from threading import Thread, Event
from logging import getLogger

from typing import List, Optional, Union, Any, Dict

from tb_rest_client.models import *
from tb_rest_client.rest import RESTResponse
from tb_rest_client.configuration import Configuration
from tb_rest_client.api_client import ApiClient

from tb_rest_client.api.admin_controller_api import AdminControllerApi
from tb_rest_client.api.ai_model_controller_api import AiModelControllerApi
from tb_rest_client.api.alarm_comment_controller_api import AlarmCommentControllerApi
from tb_rest_client.api.alarm_controller_api import AlarmControllerApi
from tb_rest_client.api.asset_controller_api import AssetControllerApi
from tb_rest_client.api.asset_profile_controller_api import AssetProfileControllerApi
from tb_rest_client.api.audit_log_controller_api import AuditLogControllerApi
from tb_rest_client.api.auth_controller_api import AuthControllerApi
from tb_rest_client.api.blob_entity_controller_api import BlobEntityControllerApi
from tb_rest_client.api.calculated_field_controller_api import CalculatedFieldControllerApi
from tb_rest_client.api.component_descriptor_controller_api import ComponentDescriptorControllerApi
from tb_rest_client.api.converter_controller_api import ConverterControllerApi
from tb_rest_client.api.converter_library_controller_api import ConverterLibraryControllerApi
from tb_rest_client.api.custom_menu_controller_api import CustomMenuControllerApi
from tb_rest_client.api.custom_translation_controller_api import CustomTranslationControllerApi
from tb_rest_client.api.customer_controller_api import CustomerControllerApi
from tb_rest_client.api.dashboard_controller_api import DashboardControllerApi
from tb_rest_client.api.dashboard_report_controller_api import DashboardReportControllerApi
from tb_rest_client.api.device_api_controller_api import DeviceApiControllerApi
from tb_rest_client.api.device_connectivity_controller_api import DeviceConnectivityControllerApi
from tb_rest_client.api.device_controller_api import DeviceControllerApi
from tb_rest_client.api.device_group_ota_package_controller_api import DeviceGroupOtaPackageControllerApi
from tb_rest_client.api.device_profile_controller_api import DeviceProfileControllerApi
from tb_rest_client.api.domain_controller_api import DomainControllerApi
from tb_rest_client.api.edge_controller_api import EdgeControllerApi
from tb_rest_client.api.edge_event_controller_api import EdgeEventControllerApi
from tb_rest_client.api.entities_version_control_controller_api import EntitiesVersionControlControllerApi
from tb_rest_client.api.entity_group_controller_api import EntityGroupControllerApi
from tb_rest_client.api.entity_query_controller_api import EntityQueryControllerApi
from tb_rest_client.api.entity_relation_controller_api import EntityRelationControllerApi
from tb_rest_client.api.entity_view_controller_api import EntityViewControllerApi
from tb_rest_client.api.event_controller_api import EventControllerApi
from tb_rest_client.api.group_permission_controller_api import GroupPermissionControllerApi
from tb_rest_client.api.image_controller_api import ImageControllerApi
from tb_rest_client.api.integration_controller_api import IntegrationControllerApi
from tb_rest_client.api.job_controller_api import JobControllerApi
from tb_rest_client.api.lwm_2m_controller_api import Lwm2mControllerApi
from tb_rest_client.api.mail_config_template_controller_api import MailConfigTemplateControllerApi
from tb_rest_client.api.mobile_app_bundle_controller_api import MobileAppBundleControllerApi
from tb_rest_client.api.mobile_app_controller_api import MobileAppControllerApi
from tb_rest_client.api.notification_controller_api import NotificationControllerApi
from tb_rest_client.api.notification_rule_controller_api import NotificationRuleControllerApi
from tb_rest_client.api.notification_target_controller_api import NotificationTargetControllerApi
from tb_rest_client.api.notification_template_controller_api import NotificationTemplateControllerApi
from tb_rest_client.api.o_auth_2_config_template_controller_api import OAuth2ConfigTemplateControllerApi
from tb_rest_client.api.o_auth_2_controller_api import OAuth2ControllerApi
from tb_rest_client.api.ota_package_controller_api import OtaPackageControllerApi
from tb_rest_client.api.owner_controller_api import OwnerControllerApi
from tb_rest_client.api.qr_code_settings_controller_api import QrCodeSettingsControllerApi
from tb_rest_client.api.queue_controller_api import QueueControllerApi
from tb_rest_client.api.queue_stats_controller_api import QueueStatsControllerApi
from tb_rest_client.api.report_controller_api import ReportControllerApi
from tb_rest_client.api.report_template_controller_api import ReportTemplateControllerApi
from tb_rest_client.api.role_controller_api import RoleControllerApi
from tb_rest_client.api.rpc_v_1_controller_api import RpcV1ControllerApi
from tb_rest_client.api.rpc_v_2_controller_api import RpcV2ControllerApi
from tb_rest_client.api.rule_chain_controller_api import RuleChainControllerApi
from tb_rest_client.api.rule_engine_controller_api import RuleEngineControllerApi
from tb_rest_client.api.scheduler_event_controller_api import SchedulerEventControllerApi
from tb_rest_client.api.secret_controller_api import SecretControllerApi
from tb_rest_client.api.self_registration_controller_api import SelfRegistrationControllerApi
from tb_rest_client.api.sign_up_controller_api import SignUpControllerApi
from tb_rest_client.api.tb_resource_controller_api import TbResourceControllerApi
from tb_rest_client.api.telemetry_controller_api import TelemetryControllerApi
from tb_rest_client.api.tenant_controller_api import TenantControllerApi
from tb_rest_client.api.tenant_profile_controller_api import TenantProfileControllerApi
from tb_rest_client.api.translation_controller_api import TranslationControllerApi
from tb_rest_client.api.trendz_api_controller_api import TrendzApiControllerApi
from tb_rest_client.api.trendz_controller_api import TrendzControllerApi
from tb_rest_client.api.two_factor_auth_config_controller_api import TwoFactorAuthConfigControllerApi
from tb_rest_client.api.two_factor_auth_controller_api import TwoFactorAuthControllerApi
from tb_rest_client.api.ui_settings_controller_api import UiSettingsControllerApi
from tb_rest_client.api.usage_info_controller_api import UsageInfoControllerApi
from tb_rest_client.api.user_controller_api import UserControllerApi
from tb_rest_client.api.user_permissions_controller_api import UserPermissionsControllerApi
from tb_rest_client.api.white_labeling_controller_api import WhiteLabelingControllerApi
from tb_rest_client.api.widget_type_controller_api import WidgetTypeControllerApi
from tb_rest_client.api.widgets_bundle_controller_api import WidgetsBundleControllerApi
from tb_rest_client.api.agent_app_profile_controller_api import AgentAppProfileControllerApi
from tb_rest_client.api.agent_app_template_controller_api import AgentAppTemplateControllerApi
from tb_rest_client.api.agent_application_controller_api import AgentApplicationControllerApi
from tb_rest_client.api.agent_bulk_action_controller_api import AgentBulkActionControllerApi
from tb_rest_client.api.agent_controller_api import AgentControllerApi
from tb_rest_client.api.agent_profile_controller_api import AgentProfileControllerApi
from tb_rest_client.api.ai_chat_controller_api import AiChatControllerApi
from tb_rest_client.api.ai_device_dashboard_controller_api import AiDeviceDashboardControllerApi
from tb_rest_client.api.ai_solution_controller_api import AiSolutionControllerApi
from tb_rest_client.api.ai_tool_controller_api import AiToolControllerApi
from tb_rest_client.api.alarm_rule_controller_api import AlarmRuleControllerApi
from tb_rest_client.api.api_key_controller_api import ApiKeyControllerApi
from tb_rest_client.api.solution_export_import_controller_api import SolutionExportImportControllerApi


logger = getLogger(__name__)


class RestClient(Thread):
    def __init__(self, base_url, timeout=(10, None)):
        """timeout: seconds for every request, a number or a (connect, read) pair. The default limits connecting
        (the TLS handshake included) to 10 s and lets an answer take as long as it needs; None waits forever."""
        super().__init__()
        if base_url.startswith("http"):
            self.base_url = base_url
        else:
            self.base_url = "http://" + base_url
        self.token_info = {"token": "", "refreshToken": "", "exp": 0}
        self.api_client = None
        self.logged_in = False
        self.stopped = True
        self.refresh_retry_delay = 5
        self.__stop_event = Event()
        self.configuration = Configuration()
        self.configuration.host = self.base_url
        self.configuration.timeout = timeout

    def run(self):
        self.stopped = False
        failures = 0
        while not self.stopped:
            delay = 1
            try:
                check_time = time()
                if check_time >= self.token_info["exp"] and self.logged_in:
                    if self.token_info["refreshToken"]:
                        self.refresh()
                        if failures:
                            logger.info("Token refreshed after %d failed attempts", failures)
                            failures = 0
                    else:
                        logger.error("No username or password provided!")
            except Exception as e:
                if failures:
                    logger.error("Token refresh failed again, retrying in %s s: %s", self.refresh_retry_delay, e)
                else:
                    logger.exception(e)
                failures += 1
                delay = self.refresh_retry_delay
            except KeyboardInterrupt:
                break
            self.__stop_event.wait(delay)

    def stop(self):
        self.stopped = True
        self.__stop_event.set()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    def login(self, username, password):
        """Authorization on the host and saving the toke information"""
        token_json = post(self.base_url + "/api/auth/login", json={"username": username, "password": password},
                          verify=self.configuration.verify_ssl, timeout=self.configuration.timeout).json()
        self.__save_token(token_json)

        self.logged_in = True

        self.__load_configuration()

    def public_login(self, public_id):
        token_json = post(self.base_url + "/api/auth/login/public", json={"publicId": public_id},
                          verify=self.configuration.verify_ssl, timeout=self.configuration.timeout).json()

        self.__save_token(token_json)
        self.__load_configuration()

    def api_key_login(self, api_key: str):
        self.configuration.api_key_prefix["X-Authorization"] = "ApiKey"
        self.configuration.api_key["X-Authorization"] = api_key
        self.__load_configuration()

    def token_login(self, token, refresh_token=None):
        token_json = {
            "token": token,
            "refreshToken": refresh_token,
        }

        self.__save_token(token_json)
        self.logged_in = True
        self.__load_configuration()

    def refresh(self):
        if not self.token_info["refreshToken"]:
            return

        token_json = post(self.base_url + "/api/auth/token", json={"refreshToken": self.token_info["refreshToken"]},
                          verify=self.configuration.verify_ssl, timeout=self.configuration.timeout).json()

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
    def delete_client_registration_template(self, client_registration_template_id: EntityId) -> None:
        client_registration_template_id = self.get_id(client_registration_template_id)
        return self.o_auth2_config_template_controller.delete_client_registration_template(
            client_registration_template_id=client_registration_template_id)

    def get_client_registration_templates1(self) -> List[OAuth2ClientRegistrationTemplate]:
        return self.o_auth2_config_template_controller.get_o_auth2_client_registration_templates()

    def save_client_registration_template(self,
                                          body: OAuth2ClientRegistrationTemplate) -> OAuth2ClientRegistrationTemplate:
        return self.o_auth2_config_template_controller.save_client_registration_template(body=body)

    # Asset Controller
    def get_customer_assets(self, customer_id: CustomerId, page_size: int, page: int, type: Optional[str] = None,
                            text_search: Optional[str] = None,
                            sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataAsset:
        customer_id = self.get_id(customer_id)
        return self.asset_controller.get_customer_assets(customer_id=customer_id, page_size=page_size,
                                                         page=page, type=type, text_search=text_search,
                                                         sort_property=sort_property, sort_order=sort_order)

    def get_tenant_asset(self, asset_name: str) -> Asset:
        return self.asset_controller.get_tenant_asset_by_name(asset_name=asset_name)

    def delete_asset(self, asset_id: AssetId) -> None:
        asset_id = self.get_id(asset_id)
        return self.asset_controller.delete_asset(asset_id=asset_id)

    def get_assets_by_ids(self, asset_ids: list) -> List[Asset]:
        asset_ids = ','.join(asset_ids)
        return self.asset_controller.get_assets_by_ids(asset_ids=asset_ids)

    def get_tenant_assets(self, page_size: int, page: int, type: Optional[str] = None,text_search: Optional[str] = None, sort_property: Optional[str] = None,
                          sort_order: Optional[str] = None) -> PageDataAsset:
        return self.asset_controller.get_tenant_assets(page_size=page_size, page=page, type=type,
                                                       text_search=text_search, sort_property=sort_property,
                                                       sort_order=sort_order)

    def get_asset_types(self, ) -> List[EntitySubtype]:
        return self.asset_controller.get_asset_types()

    def find_by_query(self, body: AssetSearchQuery) -> List[Asset]:
        return self.asset_controller.find_assets_by_query(body=body)

    def get_asset_by_id(self, asset_id: AssetId) -> Asset:
        asset_id = self.get_id(asset_id)
        return self.asset_controller.get_asset_by_id(asset_id=asset_id)

    # Rule Chain Controller
    def export_rule_chains(self, limit: int) -> RuleChainData:
        return self.rule_chain_controller.export_rule_chains(limit=limit)

    def delete_rule_chain(self, rule_chain_id: RuleChainId) -> None:
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.delete_rule_chain(rule_chain_id=rule_chain_id)

    def set_edge_template_root_rule_chain(self, rule_chain_id: RuleChainId) -> RuleChain:
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.set_edge_template_root_rule_chain(rule_chain_id=rule_chain_id)

    def save_rule_chain(self, body: DefaultRuleChainCreateRequest) -> RuleChain:
        return self.rule_chain_controller.set_device_default_rule_chain(body=body)

    def unassign_rule_chain_from_edge(self, edge_id: EdgeId, rule_chain_id: RuleChainId) -> RuleChain:
        edge_id = self.get_id(edge_id)
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.unassign_rule_chain_from_edge(edge_id=edge_id,
                                                                        rule_chain_id=rule_chain_id)

    def assign_rule_chain_to_edge(self, edge_id: EdgeId, rule_chain_id: RuleChainId) -> RuleChain:
        edge_id = self.get_id(edge_id)
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.assign_rule_chain_to_edge(edge_id=edge_id,
                                                                    rule_chain_id=rule_chain_id)

    def unset_auto_assign_to_edge_rule_chain(self, rule_chain_id: RuleChainId) -> RuleChain:
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.unset_auto_assign_to_edge_rule_chain(rule_chain_id=rule_chain_id)

    def get_rule_chain_by_id(self, rule_chain_id: RuleChainId) -> RuleChain:
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.get_rule_chain_by_id(rule_chain_id=rule_chain_id)

    def test_script(self, body: Union[dict, str, list, bytes, None, RESTResponse, tuple, Any],
                    script_lang: Optional[str] = None) -> Union[
            dict, str, list, bytes, None, RESTResponse, tuple, Any]:
        return self.rule_chain_controller.test_rule_chain_script(body=body,
                                                                 script_lang=script_lang)

    def save_rule_chain_v1(self, body: RuleChain) -> RuleChain:
        return self.rule_chain_controller.save_rule_chain(body=body)

    def get_edge_rule_chains(self, edge_id: EdgeId, page_size: int, page: int, text_search: Optional[str] = None,
                             sort_property: Optional[str] = None,
                             sort_order: Optional[str] = None) -> PageDataRuleChain:
        edge_id = self.get_id(edge_id)
        return self.rule_chain_controller.get_edge_rule_chains(edge_id=edge_id, page_size=page_size,
                                                               page=page, text_search=text_search,
                                                               sort_property=sort_property,
                                                               sort_order=sort_order)

    def set_auto_assign_to_edge_rule_chain(self, rule_chain_id: RuleChainId) -> RuleChain:
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.set_auto_assign_to_edge_rule_chain(rule_chain_id=rule_chain_id)

    def import_rule_chains(self, body: RuleChainData, overwrite: Optional[bool] = None) -> List[
        RuleChainImportResult]:
        return self.rule_chain_controller.import_rule_chains(body=body, overwrite=overwrite)

    def set_root_rule_chain(self, rule_chain_id: RuleChainId) -> RuleChain:
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.set_root_rule_chain(rule_chain_id=rule_chain_id)

    def get_rule_chains(self, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None,
                        sort_property: Optional[str] = None,
                        sort_order: Optional[str] = None) -> PageDataRuleChain:
        return self.rule_chain_controller.get_rule_chains(page_size=page_size, page=page, type=type,
                                                          text_search=text_search,
                                                          sort_property=sort_property, sort_order=sort_order)

    def get_auto_assign_to_edge_rule_chains(self, ) -> List[RuleChain]:
        return self.rule_chain_controller.get_auto_assign_to_edge_rule_chains()

    def get_latest_rule_node_debug_input(self, rule_node_id: RuleNodeId) -> Union[
            dict, str, list, bytes, None, RESTResponse, tuple, Any]:
        rule_node_id = self.get_id(rule_node_id)
        return self.rule_chain_controller.get_latest_rule_node_debug_input(rule_node_id=rule_node_id)

    def get_rule_chain_meta_data(self, rule_chain_id: RuleChainId) -> RuleChainMetaData:
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.get_rule_chain_meta_data(rule_chain_id=rule_chain_id)

    # Auth Controller
    def get_user(self, ) -> User:
        return self.auth_controller.get_user()

    def change_password(self, body: ChangePasswordRequest) -> JwtPair:
        return self.auth_controller.change_password(body=body)

    def logout(self, ) -> None:
        return self.auth_controller.logout()

    def check_reset_token(self, reset_token: str) -> str:
        return self.auth_controller.check_reset_token(reset_token=reset_token)

    def reset_password(self, body: ResetPasswordRequest) -> None:
        return self.auth_controller.reset_password(body=body)

    def activate_user(self, body: Optional[ActivateUserRequest],
                      send_activation_mail: Optional[bool] = None) -> JwtPair:
        return self.auth_controller.activate_user(body=body, send_activation_mail=send_activation_mail)

    def get_user_password_policy(self, ) -> UserPasswordPolicy:
        return self.auth_controller.get_user_password_policy()

    def check_activate_token(self, activate_token: str) -> str:
        return self.auth_controller.check_activate_token(activate_token=activate_token)

    def request_reset_password_by_email(self, body: ResetPasswordEmailRequest) -> None:
        return self.auth_controller.request_reset_password_by_email(body=body)

    # Event Controller #
    def get_events_post(self, tenant_id: TenantId, page_size: int, page: int, entity_id: EntityId,
                        body: Optional[EventFilter], text_search: Optional[str] = None, sort_property: Optional[str] = None,
                        sort_order: Optional[str] = None, start_time: Optional[int] = None,
                        end_time: Optional[int] = None) -> PageDataEventInfo:
        tenant_id = self.get_id(tenant_id)
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.event_controller.get_events_by_filter(tenant_id=tenant_id, page_size=page_size, page=page,
                                                          entity_type=entity_type, entity_id=entity_id, body=body,
                                                          text_search=text_search, sort_property=sort_property,
                                                          sort_order=sort_order, start_time=start_time,
                                                          end_time=end_time)

    def get_events_v1_get1(self, entity_id: EntityId, event_type: str, tenant_id: TenantId, page_size: int, page: int,
                           text_search: Optional[str] = None, sort_property: Optional[str] = None,
                           sort_order: Optional[str] = None, start_time: Optional[int] = None,
                           end_time: Optional[int] = None) -> PageDataEventInfo:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        tenant_id = self.get_id(tenant_id)
        return self.event_controller.get_events_by_type(entity_type=entity_type, entity_id=entity_id,
                                                        event_type=event_type, tenant_id=tenant_id, page_size=page_size,
                                                        page=page, text_search=text_search, sort_property=sort_property,
                                                        sort_order=sort_order, start_time=start_time, end_time=end_time)

    def clear_events_post(self, entity_id: EntityId, body: EventFilter, start_time: Optional[int] = None,
                          end_time: Optional[int] = None) -> None:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.event_controller.clear_events(entity_type=entity_type, entity_id=entity_id, body=body,
                                                  start_time=start_time, end_time=end_time)

    # Telemetry Controller #
    def get_attribute_keys_by_scope(self, entity_id: EntityId, scope: str) -> List[str]:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.get_attribute_keys_by_scope(entity_type=entity_type,
                                                                     entity_id=entity_id, scope=scope)

    def get_timeseries(self, entity_id: EntityId, start_ts: int, end_ts: int, keys: Optional[str] = None,
                       interval_type: Optional[str] = None, interval: Optional[int] = None,
                       time_zone: Optional[str] = None, limit: Optional[int] = None, agg: Optional[str] = None,
                       order_by: Optional[str] = None, use_strict_data_types: Optional[bool] = None,
                       key: Optional[List[str]] = None) -> Dict[str, List[TsData]]:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.get_timeseries_history(entity_type=entity_type, entity_id=entity_id, keys=keys,
                                                                start_ts=start_ts, end_ts=end_ts, interval=interval,
                                                                limit=limit, agg=agg, order_by=order_by,
                                                                interval_type=interval_type,
                                                                use_strict_data_types=use_strict_data_types,
                                                                time_zone=time_zone, key=key)

    def delete_device_attributes(self, device_id: DeviceId, scope: str, keys: Optional[str] = None,
                                 key: Optional[List[str]] = None) -> None:
        device_id = self.get_id(device_id)
        return self.telemetry_controller.delete_device_attributes(device_id=device_id, scope=scope,
                                                                  keys=keys,
                                                                  key=key)

    def save_entity_attributes_v1(self, entity_id: EntityId, scope: str,
                                  body: Union[dict, str, list, bytes, None, RESTResponse, tuple, Any]) -> None:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.save_entity_attributes_v1(entity_type=entity_type,
                                                                   entity_id=entity_id, scope=scope,
                                                                   body=body)

    def delete_entity_timeseries(self, entity_id: EntityId, keys: Optional[str] = None,
                                 delete_all_data_for_keys: Optional[bool] = None, start_ts: Optional[int] = None,
                                 end_ts: Optional[int] = None, delete_latest: Optional[bool] = None,
                                 rewrite_latest_if_deleted: Optional[bool] = None,
                                 key: Optional[List[str]] = None) -> None:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.delete_entity_timeseries(entity_type=entity_type, entity_id=entity_id,
                                                                  keys=keys,
                                                                  delete_all_data_for_keys=delete_all_data_for_keys,
                                                                  start_ts=start_ts, end_ts=end_ts,
                                                                  delete_latest=delete_latest,
                                                                  rewrite_latest_if_deleted=rewrite_latest_if_deleted,
                                                                  key=key)

    def save_device_attributes(self, device_id: DeviceId, scope: str,
                               body: Union[dict, str, list, bytes, None, RESTResponse, tuple, Any]) -> None:
        device_id = self.get_id(device_id)
        return self.telemetry_controller.save_device_attributes(device_id=device_id, scope=scope, body=body)

    def get_latest_timeseries(self, entity_id: EntityId, keys: Optional[str] = None,
                              use_strict_data_types: Optional[bool] = None,
                              key: Optional[List[str]] = None) -> Dict[str, List[TsData]]:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.get_latest_timeseries(entity_type=entity_type, entity_id=entity_id,
                                                               keys=keys,
                                                               use_strict_data_types=use_strict_data_types,
                                                               key=key)

    def get_timeseries_keys_v1(self, entity_id: EntityId) -> List[str]:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.get_timeseries_keys(entity_type=entity_type, entity_id=entity_id)

    def get_attributes_by_scope(self, entity_id: EntityId, scope: str,
                                keys: Optional[str] = None,
                                key: Optional[List[str]] = None) -> List[AttributeData]:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.get_attributes_by_scope(entity_type=entity_type, entity_id=entity_id,
                                                                 scope=scope, keys=keys,
                                                                 key=key)

    def get_attribute_keys(self, entity_id: EntityId) -> List[str]:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.get_attribute_keys(entity_type=entity_type, entity_id=entity_id)

    def save_entity_attributes_v2(self, entity_id: EntityId, scope: str,
                                  body: Union[dict, str, list, bytes, None, RESTResponse, tuple, Any]) -> None:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.save_entity_attributes_v2(entity_type=entity_type,
                                                                   entity_id=entity_id, scope=scope,
                                                                   body=body)

    def save_entity_telemetry(self, entity_id: EntityId, scope: str, body: dict) -> None:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.save_entity_telemetry(entity_type=entity_type, entity_id=entity_id,
                                                               scope=scope, body=body)

    def save_entity_telemetry_with_ttl(self, entity_id: EntityId, scope: str, ttl: int, body: dict) -> None:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        ttl = str(ttl)
        return self.telemetry_controller.save_entity_telemetry_with_ttl(entity_type=entity_type,
                                                                        entity_id=entity_id, scope=scope,
                                                                        ttl=ttl, body=body)

    def get_attributes(self, entity_id: EntityId, keys: Optional[str] = None,
                       key: Optional[List[str]] = None) -> List[AttributeData]:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.get_attributes(entity_type=entity_type, entity_id=entity_id,
                                                        keys=keys,
                                                        key=key)

    def delete_entity_attributes(self, entity_id: EntityId, scope: str, keys: Optional[str] = None,
                                 key: Optional[List[str]] = None) -> None:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.delete_entity_attributes(entity_type=entity_type,
                                                                  entity_id=entity_id, scope=scope,
                                                                  keys=keys,
                                                                  key=key)

    # Alarm Controller
    def ack_alarm(self, alarm_id: AlarmId) -> AlarmInfo:
        alarm_id = self.get_id(alarm_id)
        return self.alarm_controller.ack_alarm(alarm_id=alarm_id)

    def get_alarm_info_by_id(self, alarm_id: AlarmId) -> AlarmInfo:
        alarm_id = self.get_id(alarm_id)
        return self.alarm_controller.get_alarm_info_by_id(alarm_id=alarm_id)

    def delete_alarm(self, alarm_id: AlarmId) -> bool:
        alarm_id = self.get_id(alarm_id)
        return self.alarm_controller.delete_alarm(alarm_id=alarm_id)

    def clear_alarm(self, alarm_id: AlarmId) -> AlarmInfo:
        alarm_id = self.get_id(alarm_id)
        return self.alarm_controller.clear_alarm(alarm_id=alarm_id)

    def save_alarm(self, body: Alarm) -> Alarm:
        return self.alarm_controller.save_alarm(body=body)

    def get_alarms(self, entity_id: EntityId, page_size: int, page: int, search_status: Optional[str] = None,
                   status: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None,
                   sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None,
                   fetch_originator: Optional[bool] = None, assignee_id: Optional[str] = None) -> PageDataAlarmInfo:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.alarm_controller.get_alarms_by_entity(entity_type=entity_type, entity_id=entity_id,
                                                          page_size=page_size, page=page, search_status=search_status,
                                                          status=status, text_search=text_search,
                                                          sort_property=sort_property, sort_order=sort_order,
                                                          start_time=start_time, end_time=end_time,
                                                          fetch_originator=fetch_originator, assignee_id=assignee_id)

    def unassign_alarm(self, id: AlarmId) -> Alarm:
        id = self.get_id(id)
        return self.alarm_controller.unassign_alarm(alarm_id=id)

    def get_asset_info_by_id(self, asset_id: AssetId) -> AssetInfo:
        asset_id = self.get_id(asset_id)
        return self.asset_controller.get_asset_info_by_id(asset_id=asset_id)

    def get_customer_asset_infos(self, customer_id: CustomerId, page_size: int, page: int,
                                 include_customers: Optional[bool] = None,
                                 asset_profile_id: Optional[AssetProfileId] = None, text_search: Optional[str] = None,
                                 sort_property: Optional[str] = None,
                                 sort_order: Optional[str] = None) -> PageDataAssetInfo:
        customer_id = self.get_id(customer_id)
        asset_profile_id = self.get_id(asset_profile_id)
        return self.asset_controller.get_customer_asset_infos(customer_id=customer_id, page_size=page_size, page=page,
                                                              include_customers=include_customers,
                                                              asset_profile_id=asset_profile_id,
                                                              text_search=text_search, sort_property=sort_property,
                                                              sort_order=sort_order)

    def count_alarms_by_query(self, body: AlarmCountQuery) -> int:
        return self.entity_query_controller.count_alarms_by_query(body=body)

    def get_customer_dashboards(self, customer_id: CustomerId, page_size: int, page: int,
                                include_customers: Optional[bool] = None, text_search: Optional[str] = None,
                                sort_property: Optional[str] = None,
                                sort_order: Optional[str] = None) -> PageDataDashboardInfo:
        customer_id = self.get_id(customer_id)
        return self.dashboard_controller.get_customer_dashboards(customer_id=customer_id, page_size=page_size,
                                                                 page=page, include_customers=include_customers,
                                                                 text_search=text_search, sort_property=sort_property,
                                                                 sort_order=sort_order)

    def get_user_settings(self) -> JsonNode:
        return self.user_controller.get_general_user_settings()

    def get_tenant_usage_info(self) -> UsageInfo:
        return self.usage_info_controller.get_tenant_usage_info()

    def save_user_settings(self, body: JsonNode) -> JsonNode:
        return self.user_controller.save_user_settings(body=body)

    def put_user_settings(self, body: JsonNode) -> None:
        return self.user_controller.put_general_user_settings(body=body)

    def report_user_dashboard_action(self, dashboard_id: DashboardId, action: str) -> UserDashboardsInfo:
        dashboard_id = self.get_id(dashboard_id)
        return self.user_controller.report_user_dashboard_action(dashboard_id=dashboard_id, action=action)

    def get_users_for_assign(self, alarm_id: AlarmId, page_size: int, page: int, text_search: Optional[str] = None,
                             sort_property: Optional[str] = None,
                             sort_order: Optional[str] = None) -> PageDataUserEmailInfo:
        alarm_id = self.get_id(alarm_id)
        return self.user_controller.get_users_for_assign(alarm_id=alarm_id, page_size=page_size, page=page,
                                                         text_search=text_search,
                                                         sort_property=sort_property,
                                                         sort_order=sort_order)

    def find_users_by_query(self, page_size: int, page: int, text_search: Optional[str] = None,
                            sort_property: Optional[str] = None,
                            sort_order: Optional[str] = None) -> PageDataUserEmailInfo:
        return self.user_controller.find_users_by_query(page_size=page_size, page=page,
                                                        text_search=text_search,
                                                        sort_property=sort_property,
                                                        sort_order=sort_order)

    def get_user_dashboards_info(self) -> UserDashboardsInfo:
        return self.user_controller.get_last_visited_dashboards()

    def delete_user_settings(self, paths: List[str], type: str) -> None:
        paths = ','.join(paths)
        return self.user_controller.delete_user_settings_by_type(paths=paths, type=type)

    def get_mobile_session(self, x_mobile_token: str) -> MobileSessionInfo:
        return self.user_controller.get_mobile_session(x_mobile_token=x_mobile_token)

    def remove_mobile_session(self, x_mobile_token: str) -> None:
        return self.user_controller.remove_mobile_session(x_mobile_token=x_mobile_token)

    def save_mobile_session(self, x_mobile_token: str, body: MobileSessionInfo) -> None:
        return self.user_controller.save_mobile_session(x_mobile_token=x_mobile_token, body=body)

    def get_tenant_profiles_by_ids(self, ids: List[str]) -> List[TenantProfile]:
        ids = ','.join(ids)
        return self.tenant_profile_controller.get_tenant_profile_list(ids=ids)

    def get_entity_view_info_by_id(self, entity_view_id: EntityViewId) -> EntityViewInfo:
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.get_entity_view_info_by_id(entity_view_id=entity_view_id)

    def get_device_info_by_id(self, device_id: DeviceId) -> DeviceInfo:
        device_id = self.get_id(device_id)
        return self.device_controller.get_device_info_by_id(device_id=device_id)

    def get_alarm_by_id(self, alarm_id: AlarmId) -> Alarm:
        alarm_id = self.get_id(alarm_id)
        return self.alarm_controller.get_alarm_by_id(alarm_id=alarm_id)

    def get_all_alarms(self, page_size: int, page: int, search_status: Optional[str] = None,
                       status: Optional[str] = None, text_search: Optional[str] = None,
                       sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                       start_time: Optional[int] = None, end_time: Optional[int] = None,
                       fetch_originator: Optional[bool] = None, assignee_id: Optional[str] = None) -> PageDataAlarmInfo:
        return self.alarm_controller.get_all_alarms(page_size=page_size, page=page, search_status=search_status,
                                                    status=status, text_search=text_search, sort_property=sort_property,
                                                    sort_order=sort_order, start_time=start_time, end_time=end_time,
                                                    fetch_originator=fetch_originator, assignee_id=assignee_id)

    # Alarm Comment Controller
    def delete_alarm_comment(self, alarm_id: AlarmId, comment_id: AlarmCommentId) -> None:
        alarm_id = self.get_id(alarm_id)
        comment_id = self.get_id(comment_id)
        return self.alarm_comment_controller.delete_alarm_comment(alarm_id=alarm_id, comment_id=comment_id)

    def get_alarm_comments(self, alarm_id: AlarmId, page_size: int, page: int, sort_property: Optional[str] = None,
                           sort_order: Optional[str] = None) -> PageDataAlarmCommentInfo:
        alarm_id = self.get_id(alarm_id)
        return self.alarm_comment_controller.get_alarm_comments(alarm_id=alarm_id, page_size=page_size,
                                                                page=page, sort_property=sort_property,
                                                                sort_order=sort_order)

    def save_alarm_comment(self, alarm_id: AlarmId, body: AlarmComment) -> AlarmComment:
        alarm_id = self.get_id(alarm_id)
        return self.alarm_comment_controller.save_alarm_comment(alarm_id=alarm_id, body=body)

    # Edge Controller #
    def get_tenant_edge(self, edge_name: str) -> Edge:
        return self.edge_controller.get_tenant_edge_by_name(edge_name=edge_name)

    def delete_edge(self, edge_id: EdgeId) -> None:
        edge_id = self.get_id(edge_id)
        return self.edge_controller.delete_edge(edge_id=edge_id)

    def is_edges_support_enabled(self, ) -> bool:
        return self.edge_controller.is_edges_support_enabled()

    def get_edge_by_id(self, edge_id: EdgeId) -> Edge:
        edge_id = self.get_id(edge_id)
        return self.edge_controller.get_edge_by_id(edge_id=edge_id)

    def sync_edge(self, edge_id: EdgeId) -> Any:
        edge_id = self.get_id(edge_id)
        return self.edge_controller.sync_edge(edge_id=edge_id)

    def get_tenant_edges(self, page_size: int, page: int, type: Optional[str] = None,text_search: Optional[str] = None, sort_property: Optional[str] = None,
                         sort_order: Optional[str] = None) -> PageDataEdge:
        return self.edge_controller.get_tenant_edges(page_size=page_size, page=page, type=type,
                                                     text_search=text_search, sort_property=sort_property,
                                                     sort_order=sort_order)

    def find_by_query_v2(self, body: EdgeSearchQuery) -> List[Edge]:
        return self.edge_controller.find_edges_by_query(body=body)

    def get_edges(self, page_size: int, page: int,text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataEdge:
        return self.edge_controller.get_edges(page_size=page_size, page=page, text_search=text_search,
                                              sort_property=sort_property, sort_order=sort_order)

    def get_edge_types(self, ) -> List[EntitySubtype]:
        return self.edge_controller.get_edge_types()

    def set_edge_root_rule_chain(self, edge_id: EdgeId, rule_chain_id: RuleChainId) -> Edge:
        edge_id = self.get_id(edge_id)
        rule_chain_id = self.get_id(rule_chain_id)
        return self.edge_controller.set_edge_root_rule_chain(edge_id=edge_id, rule_chain_id=rule_chain_id)

    def find_missing_to_related_rule_chains(self, edge_id: EdgeId) -> Dict:
        edge_id = self.get_id(edge_id)
        return self.edge_controller.find_missing_to_related_rule_chains(edge_id=edge_id)

    def get_customer_edges(self, customer_id: CustomerId, page_size: int, page: int, type: Optional[str] = None,text_search: Optional[str] = None,
                           sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataEdge:
        customer_id = self.get_id(customer_id)
        return self.edge_controller.get_customer_edges(customer_id=customer_id, page_size=page_size,
                                                       page=page, type=type, text_search=text_search,
                                                       sort_property=sort_property, sort_order=sort_order)

    def get_edges_by_ids(self, edge_ids: list) -> List[Edge]:
        return self.edge_controller.get_edge_list(edge_ids=','.join(edge_ids))

    def process_edges_bulk_import(self, body: BulkImportRequest) -> BulkImportResultEdge:
        return self.edge_controller.process_edges_bulk_import(body=body)

    def get_edge_events(self, edge_id: EdgeId, page_size: int, page: int,text_search: Optional[str] = None, sort_property: Optional[str] = None,
                        sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None) -> PageDataEdgeEvent:
        edge_id = self.get_id(edge_id)
        return self.edge_event_controller.get_edge_events(edge_id=edge_id, page_size=page_size, page=page,
                                                          text_search=text_search,
                                                          sort_property=sort_property, sort_order=sort_order,
                                                          start_time=start_time, end_time=end_time)

    # RPC v2 Controller
    def get_persisted_rpc(self, rpc_id: RpcId) -> Rpc:
        rpc_id = self.get_id(rpc_id)
        return self.rpc_v2_controller.get_persisted_rpc(rpc_id=rpc_id)

    def handle_one_way_device_rpc_request_v1(self, device_id: DeviceId, body: str) -> Any:
        device_id = self.get_id(device_id)
        return self.rpc_v2_controller.handle_one_way_device_rpc_request_v2(device_id=device_id, body=body)

    def handle_two_way_device_rpc_request_v1(self, device_id: DeviceId, body: str) -> Any:
        device_id = self.get_id(device_id)
        return self.rpc_v2_controller.handle_two_way_device_rpc_request_v2(device_id=device_id, body=body)

    def get_persisted_rpc_by_device(self, device_id: DeviceId, page_size: int, page: int,
                                    rpc_status: Optional[str] = None, text_search: Optional[str] = None,
                                    sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> Dict:
        device_id = self.get_id(device_id)
        return self.rpc_v2_controller.get_persisted_rpc_by_device(device_id=device_id, page_size=page_size,
                                                                  page=page, rpc_status=rpc_status,
                                                                  text_search=text_search,
                                                                  sort_property=sort_property,
                                                                  sort_order=sort_order)
    def get_rule_chain_output_labels_usage(self, rule_chain_id: RuleChainId) -> List[RuleChainOutputLabelsUsage]:
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.get_rule_chain_output_labels_usage(rule_chain_id=rule_chain_id)

    def get_rule_chain_output_labels(self, rule_chain_id: RuleChainId) -> List[str]:
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.get_rule_chain_output_labels(rule_chain_id=rule_chain_id)

    def is_tbel_enabled(self) -> bool:
        return self.rule_chain_controller.is_tbel_enabled()

    def save_rule_chain_meta_data(self, body: RuleChainMetaData,
                                  update_related: Optional[bool] = None) -> RuleChainMetaData:
        return self.rule_chain_controller.save_rule_chain_meta_data(body=body, update_related=update_related)

    def get_rule_chains_by_ids(self, rule_chain_ids: List[str]) -> List[RuleChain]:
        rule_chain_ids = ','.join(rule_chain_ids)
        return self.rule_chain_controller.get_rule_chains_by_ids(rule_chain_ids=rule_chain_ids)

    def delete_rpc(self, rpc_id: RpcId) -> None:
        rpc_id = self.get_id(rpc_id)
        return self.rpc_v2_controller.delete_rpc(rpc_id=rpc_id)

    # Customer Controller #
    def get_customer_title_by_id(self, customer_id: CustomerId) -> str:
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_customer_title_by_id(customer_id=customer_id)

    def get_customers(self, page_size: int, page: int,text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataCustomer:
        return self.customer_controller.get_customers(page_size=page_size, page=page, text_search=text_search,
                                                      sort_property=sort_property, sort_order=sort_order)

    def get_customer_by_id(self, customer_id: CustomerId) -> Customer:
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_customer_by_id(customer_id=customer_id)

    def get_short_customer_info_by_id(self, customer_id: CustomerId) -> Union[
            dict, str, list, bytes, None, RESTResponse, tuple, Any]:
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_short_customer_info_by_id(customer_id=customer_id)

    def get_tenant_customer(self, customer_title: str) -> Customer:
        return self.customer_controller.get_tenant_customer(customer_title=customer_title)

    def delete_customer(self, customer_id: CustomerId) -> None:
        customer_id = self.get_id(customer_id)
        return self.customer_controller.delete_customer(customer_id=customer_id)

    def get_customers_by_ids(self, customer_ids: str) -> List[Customer]:
        return self.customer_controller.get_customers_by_ids(customer_ids=customer_ids)

    # User Controller #
    def get_user_token(self, user_id: UserId) -> JwtPair:
        user_id = self.get_id(user_id)
        return self.user_controller.get_user_token(user_id=user_id)

    def get_activation_link(self, user_id: UserId) -> str:
        user_id = self.get_id(user_id)
        return self.user_controller.get_activation_link(user_id=user_id)

    def delete_user(self, user_id: UserId) -> None:
        user_id = self.get_id(user_id)
        return self.user_controller.delete_user(user_id=user_id)

    def set_user_credentials_enabled(self, user_id: UserId, user_credentials_enabled: Optional[bool] = None) -> None:
        user_id = self.get_id(user_id)
        return self.user_controller.set_user_credentials_enabled(user_id=user_id,
                                                                 user_credentials_enabled=user_credentials_enabled)

    def get_customer_users(self, customer_id: CustomerId, page_size: int, page: int,text_search: Optional[str] = None,
                           sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataUser:
        customer_id = self.get_id(customer_id)
        return self.user_controller.get_customer_users(customer_id=customer_id, page_size=page_size,
                                                       page=page, text_search=text_search,
                                                       sort_property=sort_property, sort_order=sort_order)

    def get_user_by_id(self, user_id: UserId) -> User:
        user_id = self.get_id(user_id)
        return self.user_controller.get_user_by_id(user_id=user_id)

    def get_tenant_admins(self, tenant_id: TenantId, page_size: int, page: int,text_search: Optional[str] = None, sort_property: Optional[str] = None,
                          sort_order: Optional[str] = None,) -> PageDataUser:
        tenant_id = self.get_id(tenant_id)
        return self.user_controller.get_tenant_admins(tenant_id=tenant_id, page_size=page_size, page=page,
                                                      text_search=text_search, sort_property=sort_property,
                                                      sort_order=sort_order)

    def is_user_token_access_enabled(self, ) -> bool:
        return self.user_controller.is_user_token_access_enabled()

    def send_activation_email(self, email: str) -> None:
        return self.user_controller.send_activation_email(email=email)

    def get_activation_link_info(self, user_id: UserId) -> UserActivationLink:
        user_id = self.get_id(user_id)
        return self.user_controller.get_activation_link_info(user_id=user_id)

    def get_users_by_ids(self, user_ids: list) -> List[User]:
        return self.user_controller.get_users_by_ids(user_ids=','.join(user_ids))

    # Queue Controller
    def get_tenant_queues_by_service_type(self, service_type: str, page_size: int, page: int,
                                          text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                          sort_order: Optional[str] = None) -> PageDataQueue:
        return self.queue_controller.get_tenant_queues_by_service_type(service_type=service_type, page_size=page_size,
                                                                       page=page, text_search=text_search,
                                                                       sort_property=sort_property,
                                                                       sort_order=sort_order)

    def save_queue(self, service_type: str, body: Queue) -> Queue:
        return self.queue_controller.save_queue(service_type=service_type, body=body)

    # RPC v1 Controller
    def handle_one_way_device_rpc_request(self, device_id: DeviceId, body: str) -> Any:
        device_id = self.get_id(device_id)
        return self.rpc_v1_controller.handle_one_way_device_rpc_request_v1(device_id=device_id, body=body)

    def handle_two_way_device_rpc_request(self, device_id: DeviceId, body: Dict) -> Any:
        device_id = self.get_id(device_id)
        return self.rpc_v1_controller.handle_two_way_device_rpc_request_v1(device_id=device_id, body=body)

    # Device Controller
    def get_device_types(self, ) -> List[EntitySubtype]:
        return self.device_controller.get_device_types()

    def update_device_credentials(self, body: DeviceCredentials) -> DeviceCredentials:
        return self.device_controller.update_device_credentials(body=body)

    def delete_device(self, device_id: DeviceId) -> None:
        device_id = self.get_id(device_id)
        return self.device_controller.delete_device(device_id=device_id)

    def assign_device_to_tenant(self, tenant_id: TenantId, device_id: DeviceId) -> Device:
        tenant_id = self.get_id(tenant_id)
        device_id = self.get_id(device_id)
        return self.device_controller.assign_device_to_tenant(tenant_id=tenant_id, device_id=device_id)

    def re_claim_device(self, device_name: str) -> Any:
        return self.device_controller.re_claim_device(device_name=device_name)

    def process_devices_bulk_import(self, body: BulkImportRequest) -> BulkImportResultDevice:
        return self.device_controller.process_devices_bulk_import(body=body)

    def count_by_device_profile_and_empty_ota_package(self, ota_package_type: str,
                                                      device_profile_id: DeviceProfileId) -> int:
        device_profile_id = self.get_id(device_profile_id)
        return self.device_controller.count_by_device_profile_and_empty_ota_package(
            ota_package_type=ota_package_type, device_profile_id=device_profile_id)

    def get_devices_by_ids(self, device_ids: list) -> List[Device]:
        device_ids = ','.join(device_ids)
        return self.device_controller.get_devices_by_ids(device_ids=device_ids)

    def get_device_by_id(self, device_id: DeviceId) -> Device:
        device_id = self.get_id(device_id)
        return self.device_controller.get_device_by_id(device_id=device_id)

    def find_by_query_v1(self, body: DeviceSearchQuery) -> List[Device]:
        return self.device_controller.find_devices_by_query(body=body)

    def get_customer_devices(self, customer_id: CustomerId, page_size: int, page: int, type: Optional[str] = None,text_search: Optional[str] = None,
                             sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataDevice:
        customer_id = self.get_id(customer_id)
        return self.device_controller.get_customer_devices(customer_id=customer_id, page_size=page_size,
                                                           page=page, type=type, text_search=text_search,
                                                           sort_property=sort_property, sort_order=sort_order)

    def get_tenant_devices(self, page_size: int, page: int, type: Optional[str] = None,text_search: Optional[str] = None, sort_property: Optional[str] = None,
                           sort_order: Optional[str] = None,) -> PageDataDevice:
        return self.device_controller.get_tenant_devices(page_size=page_size, page=page, type=type,
                                                         text_search=text_search, sort_property=sort_property,
                                                         sort_order=sort_order)

    def get_tenant_device(self, device_name: str) -> Device:
        return self.device_controller.get_tenant_device_by_name(device_name=device_name)

    def get_device_credentials_by_device_id(self, device_id: DeviceId) -> DeviceCredentials:
        device_id = self.get_id(device_id)
        return self.device_controller.get_device_credentials_by_device_id(device_id=device_id)

    # Entity Relation Controller
    def find_by_to_v1(self, to_id: EntityId, to_type: str, relation_type_group: Optional[str] = None) -> List[EntityRelation]:
        to_id = self.get_id(to_id)
        return self.entity_relation_controller.find_entity_relations_by_to(to_id=to_id, to_type=to_type,
                                                                           relation_type_group=relation_type_group)

    def find_info_by_to(self, to_id: EntityId, to_type: str, relation_type_group: Optional[str] = None) -> List[
        EntityRelationInfo]:
        to_id = self.get_id(to_id)
        return self.entity_relation_controller.find_entity_relation_infos_by_to(to_id=to_id, to_type=to_type,
                                                                                relation_type_group=relation_type_group)

    def delete_relations(self, entity_id: EntityId) -> None:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.entity_relation_controller.delete_relations(entity_id=entity_id,
                                                                entity_type=entity_type)

    def delete_relation(self, from_id: EntityId, relation_type: str, to_id: EntityId,
                        relation_type_group: Optional[str] = None) -> EntityRelation:
        from_type = self.get_type(from_id)
        from_id = self.get_id(from_id)

        to_type = self.get_type(to_id)
        to_id = self.get_id(to_id)
        return self.entity_relation_controller.delete_relation(from_id=from_id, from_type=from_type,
                                                               relation_type=relation_type, to_id=to_id,
                                                               to_type=to_type,
                                                               relation_type_group=relation_type_group)

    def find_info_by_query(self, body: EntityRelationsQuery) -> List[EntityRelationInfo]:
        return self.entity_relation_controller.find_entity_relation_infos_by_query(body=body)

    def find_by_query_v3(self, body: EntityRelationsQuery) -> List[EntityRelation]:
        return self.entity_relation_controller.find_entity_relations_by_query(body=body)

    def save_relation(self, body: EntityRelation) -> EntityRelation:
        return self.entity_relation_controller.save_relation(body=body)

    def find_by_to(self, to_id: EntityId, relation_type: str,
                   relation_type_group: Optional[str] = None) -> List[EntityRelation]:
        to_type = self.get_type(to_id)
        to_id = self.get_id(to_id)
        return self.entity_relation_controller.find_entity_relations_by_to_and_relation_type(
            to_id=to_id, to_type=to_type, relation_type=relation_type, relation_type_group=relation_type_group)

    def find_info_by_from(self, from_id: EntityId,
                          relation_type_group: Optional[str] = None) -> List[EntityRelationInfo]:
        from_type = self.get_type(from_id)
        from_id = self.get_id(from_id)
        return self.entity_relation_controller.find_entity_relation_infos_by_from(from_id=from_id, from_type=from_type,
                                                                                  relation_type_group=relation_type_group)

    def get_relation(self, from_id: EntityId, relation_type: str, to_id: EntityId,
                     relation_type_group: Optional[str] = None) -> EntityRelation:
        from_type = self.get_type(from_id)
        from_id = self.get_id(from_id)

        to_type = self.get_type(to_id)
        to_id = self.get_id(to_id)
        return self.entity_relation_controller.get_relation(from_id=from_id, from_type=from_type,
                                                            relation_type=relation_type, to_id=to_id,
                                                            to_type=to_type,
                                                            relation_type_group=relation_type_group)

    def find_by_from_v1(self, from_id: EntityId, from_type: str,
                        relation_type_group: Optional[str] = None) -> List[EntityRelation]:
        from_id = self.get_id(from_id)
        return self.entity_relation_controller.find_entity_relations_by_from(from_id=from_id, from_type=from_type,
                                                                             relation_type_group=relation_type_group)

    def find_by_from(self, from_id: EntityId, relation_type: str,
                     relation_type_group: Optional[str] = None) -> List[EntityRelation]:
        from_type = self.get_type(from_id)
        from_id = self.get_id(from_id)
        return self.entity_relation_controller.find_entity_relations_by_from_and_relation_type(
            from_id=from_id, from_type=from_type, relation_type=relation_type, relation_type_group=relation_type_group)

    # Entity View Controller
    def get_tenant_entity_view(self, entity_view_name: str) -> EntityView:
        return self.entity_view_controller.get_tenant_entity_view_by_name(entity_view_name=entity_view_name)

    def get_tenant_entity_views(self, page_size: int, page: int, type: Optional[str] = None,text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                sort_order: Optional[str] = None,) -> PageDataEntityView:
        return self.entity_view_controller.get_tenant_entity_views(page_size=page_size, page=page, type=type,
                                                                   text_search=text_search,
                                                                   sort_property=sort_property,
                                                                   sort_order=sort_order)

    def get_entity_view_by_id(self, entity_view_id: EntityViewId) -> EntityView:
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.get_entity_view_by_id(entity_view_id=entity_view_id)

    def find_by_query_v4(self, body: EntityViewSearchQuery) -> List[EntityView]:
        return self.entity_view_controller.find_entity_views_by_query(body=body)

    def get_entity_view_types(self, ) -> List[EntitySubtype]:
        return self.entity_view_controller.get_entity_view_types()

    def delete_entity_view(self, entity_view_id: EntityViewId) -> None:
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.delete_entity_view(entity_view_id=entity_view_id)

    def get_customer_entity_views(self, customer_id: CustomerId, page_size: int, page: int, type: Optional[str] = None,text_search: Optional[str] = None,
                                  sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataEntityView:
        customer_id = self.get_id(customer_id)
        return self.entity_view_controller.get_customer_entity_views(customer_id=customer_id,
                                                                     page_size=page_size, page=page,
                                                                     type=type, text_search=text_search,
                                                                     sort_property=sort_property,
                                                                     sort_order=sort_order)

    def get_entity_views_by_ids(self, entity_view_ids: list) -> List[EntityView]:
        entity_view_ids = ','.join(entity_view_ids)
        return self.entity_view_controller.get_entity_views_by_ids(entity_view_ids=entity_view_ids)

    # Admin Controller
    def send_test_sms(self, body: TestSmsRequest) -> None:
        return self.admin_controller.send_test_sms(body=body)

    def check_updates(self) -> UpdateMessage:
        return self.admin_controller.check_updates()

    def get_security_settings(self) -> SecuritySettings:
        return self.admin_controller.get_security_settings()

    def send_test_mail(self, body: AdminSettings) -> None:
        return self.admin_controller.send_test_mail(body=body)

    def save_admin_settings(self, body: AdminSettings) -> AdminSettings:
        return self.admin_controller.save_admin_settings(body=body)

    def save_security_settings(self, body: SecuritySettings) -> SecuritySettings:
        return self.admin_controller.save_security_settings(body=body)

    def get_repository_settings(self) -> RepositorySettings:
        return self.admin_controller.get_repository_settings()

    def save_repository_settings(self, body: RepositorySettings) -> RepositorySettings:
        return self.admin_controller.save_repository_settings(body=body)

    def delete_repository_settings(self) -> None:
        return self.admin_controller.delete_repository_settings()

    def repository_settings_exists(self) -> bool:
        return self.admin_controller.repository_settings_exists()

    def check_repository_access(self, body: RepositorySettings) -> None:
        return self.admin_controller.check_repository_access(body=body)

    def delete_auto_commit_settings(self) -> None:
        return self.admin_controller.delete_auto_commit_settings()

    def auto_commit_settings_exists(self) -> bool:
        return self.admin_controller.auto_commit_settings_exists()

    def save_auto_commit_settings(self, body: Dict[str, AutoVersionCreateConfig]) -> Dict[str, AutoVersionCreateConfig]:
        return self.admin_controller.save_auto_commit_settings(body=body)

    def get_auto_commit_settings(self) -> Dict[str, AutoVersionCreateConfig]:
        return self.admin_controller.get_auto_commit_settings()

    def get_jwt_setting(self) -> JwtSettings:
        return self.admin_controller.get_jwt_settings()

    def save_jwt_settings(self, body: JwtSettings) -> JwtPair:
        return self.admin_controller.save_jwt_settings(body=body)

    # TB Resource Controller
    def get_resource_info_by_id(self, resource_id: EntityId) -> TbResourceInfo:
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.get_resource_info_by_id(resource_id=resource_id)

    def save_resource(self, body) -> TbResourceInfo:
        return self.tb_resource_controller.save_resource(body=body)

    def get_resources(self, page_size: int, page: int, text_search: Optional[str] = None,
                      sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                      resource_type: Optional[List[str]] = None,
                      resource_sub_type: Optional[str] = None) -> PageDataTbResourceInfo:
        return self.tb_resource_controller.get_resources(page_size=page_size, page=page, text_search=text_search,
                                                         sort_property=sort_property, sort_order=sort_order,
                                                         resource_type=resource_type,
                                                         resource_sub_type=resource_sub_type)

    def get_lwm2m_list_objects(self, sort_order: str, sort_property: str, object_ids: list) -> List[LwM2mObject]:
        return self.tb_resource_controller.get_lwm2m_list_objects(sort_order=sort_order,
                                                                  sort_property=sort_property,
                                                                  object_ids=object_ids)

    def download_resource(self, resource_id: EntityId) -> bytes:
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.download_resource(resource_id=resource_id)

    def get_lwm2m_list_objects_page(self, page_size: int, page: int, text_search: Optional[str] = None,
                                    sort_property: Optional[str] = None,
                                    sort_order: Optional[str] = None) -> List[LwM2mObject]:
        return self.tb_resource_controller.get_lwm2m_list_objects_page(page_size=page_size, page=page,
                                                                       text_search=text_search,
                                                                       sort_property=sort_property,
                                                                       sort_order=sort_order)

    def get_tenant_resources(self, page_size: int, page: int, text_search: Optional[str] = None,
                             sort_property: Optional[str] = None,
                             sort_order: Optional[str] = None) -> PageDataTbResourceInfo:
        return self.tb_resource_controller.get_tenant_resources(page_size=page_size, page=page,
                                                                text_search=text_search,
                                                                sort_property=sort_property,
                                                                sort_order=sort_order)

    def get_system_or_tenant_resources_by_ids(self, resource_ids: list[EntityId]) -> List[TbResourceInfo]:
        return self.tb_resource_controller.get_system_or_tenant_resources_by_ids(resource_ids=','.join(resource_ids))

    def code_processing_url(self, code: str, state: str) -> None:
        return self.admin_controller.handle_mail_o_auth2_callback(code=code, state=state)

    def get_authorization_url(self) -> str:
        return self.admin_controller.get_mail_o_auth2_authorization_url()

    def get_mail_processing_url(self) -> str:
        return self.admin_controller.get_mail_processing_url()

    def download_jks_resource_if_changed(self, resource_id: EntityId,
                                         if_none_match: Optional[str] = '') -> bytes:
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.download_jks_resource_if_changed(resource_id=resource_id,
                                                                            if_none_match=if_none_match)

    def download_js_resource_if_changed(self, resource_id: EntityId, if_none_match: Optional[str] = '') -> bytes:
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.download_js_resource_if_changed(resource_id=resource_id,
                                                                           if_none_match=if_none_match)

    def download_lwm2m_resource_if_changed(self, resource_id: EntityId,
                                           if_none_match: Optional[str] = '') -> bytes:
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.download_lwm2m_resource_if_changed(resource_id=resource_id,
                                                                              if_none_match=if_none_match)

    def download_pkcs12_resource_if_changed(self, resource_id: EntityId,
                                            if_none_match: Optional[str] = '') -> bytes:
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.download_pkcs12_resource_if_changed(resource_id=resource_id,
                                                                               if_none_match=if_none_match)

    def get_resource_by_id(self, resource_id: EntityId) -> TbResource:
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.get_resource_by_id(resource_id=resource_id)

    def download_resource_if_changed(self, resource_type: str, scope: str, key: str,
                                     if_none_match: Optional[str] = '') -> bytes:
        return self.tb_resource_controller.download_resource_if_changed(resource_type=resource_type, scope=scope,
                                                                        key=key, if_none_match=if_none_match)

    def upload_resource(self, resource_type, file, title=None, descriptor=None,
                        resource_sub_type=None) -> TbResourceInfo:
        return self.tb_resource_controller.upload_resource(title=title, resource_type=resource_type,
                                                           descriptor=descriptor, resource_sub_type=resource_sub_type,
                                                           file=file)

    def update_resource_info(self, body: TbResourceInfo, resource_id: EntityId) -> TbResourceInfo:
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.update_resource_info(id=resource_id, body=body)

    def update_resource_data(self, id: EntityId, file: str) -> TbResourceInfo:
        id = self.get_id(id)
        return self.tb_resource_controller.update_resource_data(id=id, file=file)

    def get_repository_settings_info(self) -> RepositorySettingsInfo:
        return self.admin_controller.get_repository_settings_info()

    # O Auth 2 Controller
    def get_login_processing_url(self, ) -> str:
        return self.o_auth2_controller.get_login_processing_url()

    def get_o_auth2_clients(self, pkg_name: Optional[str] = None,
                            platform: Optional[str] = None) -> List[OAuth2ClientLoginInfo]:
        return self.o_auth2_controller.get_o_auth2_clients(pkg_name=pkg_name, platform=platform)

    def delete_oauth2_client(self, id: OAuth2ClientId) -> None:
        id = self.get_id(id)
        return self.o_auth2_controller.delete_oauth2_client(id=id)

    def find_tenant_o_auth2_client_infos(self, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataOAuth2ClientInfo:
        return self.o_auth2_controller.find_o_auth2_client_infos(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def find_tenant_o_auth2_client_infos_by_ids(self, ids: List[str]) -> List[OAuth2ClientInfo]:
        ids = ','.join(ids)
        return self.o_auth2_controller.find_tenant_o_auth2_client_infos_by_ids(client_ids=ids)

    def get_o_auth2_client_by_id(self, id: OAuth2ClientId) -> OAuth2Client:
        id = self.get_id(id)
        return self.o_auth2_controller.get_o_auth2_client_by_id(id=id)

    def save_o_auth2_client(self, body: OAuth2Client) -> OAuth2Client:
        return self.o_auth2_controller.save_o_auth2_client(body=body)

    # Tenant Profile Controller
    def get_default_tenant_profile_info(self, ) -> EntityInfo:
        return self.tenant_profile_controller.get_default_tenant_profile_info()

    def save_tenant_profile(self, body: TenantProfile) -> TenantProfile:
        return self.tenant_profile_controller.save_tenant_profile(body=body)

    def get_tenant_profiles(self, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None,
                            sort_order: Optional[str] = None) -> PageDataTenantProfile:
        return self.tenant_profile_controller.get_tenant_profiles(page_size=page_size, page=page,
                                                                  text_search=text_search,
                                                                  sort_property=sort_property,
                                                                  sort_order=sort_order)

    def delete_tenant_profile(self, tenant_profile_id: TenantProfileId) -> None:
        tenant_profile_id = self.get_id(tenant_profile_id)
        return self.tenant_profile_controller.delete_tenant_profile(tenant_profile_id=tenant_profile_id)

    def get_tenant_profile_info_by_id(self, tenant_profile_id: TenantProfileId) -> EntityInfo:
        tenant_profile_id = self.get_id(tenant_profile_id)
        return self.tenant_profile_controller.get_tenant_profile_info_by_id(
            tenant_profile_id=tenant_profile_id)

    def get_tenant_profile_by_id(self, tenant_profile_id: TenantProfileId) -> TenantProfile:
        tenant_profile_id = self.get_id(tenant_profile_id)
        return self.tenant_profile_controller.get_tenant_profile_by_id(tenant_profile_id=tenant_profile_id)

    def set_default_tenant_profile(self, tenant_profile_id: TenantProfileId) -> TenantProfile:
        tenant_profile_id = self.get_id(tenant_profile_id)
        return self.tenant_profile_controller.set_default_tenant_profile(tenant_profile_id=tenant_profile_id)

    def get_tenant_profile_infos(self, page_size: int, page: int, text_search: Optional[str] = None,
                                 sort_property: Optional[str] = None,
                                 sort_order: Optional[str] = None) -> PageDataEntityInfo:
        return self.tenant_profile_controller.get_tenant_profile_infos(page_size=page_size, page=page,
                                                                       text_search=text_search,
                                                                       sort_property=sort_property,
                                                                       sort_order=sort_order)

    # Widgets Bundle Controller
    def update_widgets_bundle_widget_fqns(self, widgets_bundle_id: WidgetsBundleId, body: List[str]) -> None:
        widgets_bundle_id = self.get_id(widgets_bundle_id)
        body = ','.join(body)
        return self.widgets_bundle_controller.update_widgets_bundle_widget_fqns(
            widgets_bundle_id=widgets_bundle_id, body=body)

    def update_widgets_bundle_widget_types(self, widgets_bundle_id: WidgetsBundleId, body: List[str]) -> None:
        widgets_bundle_id = self.get_id(widgets_bundle_id)
        body = ','.join(body)
        return self.widgets_bundle_controller.update_widgets_bundle_widget_types(
            widgets_bundle_id=widgets_bundle_id, body=body)

    def get_widgets_bundle_by_id(self, widgets_bundle_id: WidgetsBundleId,
                                 inline_images: Optional[bool] = None) -> WidgetsBundle:
        widgets_bundle_id = self.get_id(widgets_bundle_id)
        return self.widgets_bundle_controller.get_widgets_bundle_by_id(widgets_bundle_id=widgets_bundle_id,
                                                                       inline_images=inline_images)

    def save_widgets_bundle(self, body: WidgetsBundle) -> WidgetsBundle:
        return self.widgets_bundle_controller.save_widgets_bundle(body=body)

    def get_widgets_bundles_v1(self, page_size: int, page: int, text_search: Optional[str] = None,
                               sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                               tenant_only: Optional[bool] = None,
                               full_search: Optional[bool] = None,
                               scada_first: Optional[bool] = None) -> PageDataWidgetsBundle:
        return self.widgets_bundle_controller.get_widgets_bundles(page_size=page_size, page=page,
                                                                  text_search=text_search,
                                                                  sort_property=sort_property,
                                                                  sort_order=sort_order,
                                                                  tenant_only=tenant_only,
                                                                  full_search=full_search,
                                                                  scada_first=scada_first)

    def delete_widgets_bundle(self, widgets_bundle_id: WidgetsBundleId) -> None:
        widgets_bundle_id = self.get_id(widgets_bundle_id)
        return self.widgets_bundle_controller.delete_widgets_bundle(widgets_bundle_id=widgets_bundle_id)

    def get_widgets_bundles(self, page_size: int, page: int, text_search: Optional[str] = None,
                            sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                            tenant_only: Optional[bool] = None, full_search: Optional[bool] = None,
                            scada_first: Optional[bool] = None) -> PageDataWidgetsBundle:
        return self.widgets_bundle_controller.get_widgets_bundles(page_size=page_size, page=page,
                                                                  text_search=text_search,
                                                                  sort_property=sort_property, sort_order=sort_order,
                                                                  tenant_only=tenant_only, full_search=full_search,
                                                                  scada_first=scada_first)

    def get_widgets_bundles_by_ids(self, widget_bundle_ids: List[str]) -> List[WidgetsBundle]:
        widget_bundle_ids = ','.join(widget_bundle_ids)
        return self.widgets_bundle_controller.get_widgets_bundles_list(widgets_bundle_ids=widget_bundle_ids)

    # Device Profile Controller
    def get_device_profile_infos(self, page_size: int, page: int, text_search: Optional[str] = None,
                                 sort_property: Optional[str] = None,
                                 sort_order: Optional[str] = None, transport_type: Optional[str] = None) -> PageDataDeviceProfileInfo:
        return self.device_profile_controller.get_device_profile_infos(page_size=page_size, page=page,
                                                                       text_search=text_search,
                                                                       sort_property=sort_property,
                                                                       sort_order=sort_order,
                                                                       transport_type=transport_type)

    def set_default_device_profile(self, device_profile_id: DeviceProfileId) -> DeviceProfile:
        device_profile_id = self.get_id(device_profile_id)
        return self.device_profile_controller.set_default_device_profile(device_profile_id=device_profile_id)

    def delete_device_profile(self, device_profile_id: DeviceProfileId) -> None:
        device_profile_id = self.get_id(device_profile_id)
        return self.device_profile_controller.delete_device_profile(device_profile_id=device_profile_id)

    def get_attributes_keys(self, device_profile_id: Optional[DeviceProfileId] = None) -> List[str]:
        device_profile_id = self.get_id(device_profile_id)
        return self.device_profile_controller.get_attributes_keys(device_profile_id=device_profile_id)

    def save_device_profile(self, body: DeviceProfile) -> DeviceProfile:
        return self.device_profile_controller.save_device_profile(body=body)

    def get_default_device_profile_info(self, ) -> DeviceProfileInfo:
        return self.device_profile_controller.get_default_device_profile_info()

    def get_timeseries_keys(self, device_profile_id: Optional[DeviceProfileId] = None) -> List[str]:
        device_profile_id = self.get_id(device_profile_id)
        return self.device_profile_controller.get_device_profile_timeseries_keys(device_profile_id=device_profile_id)

    def get_device_profile_info_by_id(self, device_profile_id: DeviceProfileId) -> DeviceProfileInfo:
        device_profile_id = self.get_id(device_profile_id)
        return self.device_profile_controller.get_device_profile_info_by_id(
            device_profile_id=device_profile_id)

    def get_device_profiles(self, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None,
                            sort_order: Optional[str] = None) -> PageDataDeviceProfile:
        return self.device_profile_controller.get_device_profiles(page_size=page_size, page=page,
                                                                  text_search=text_search,
                                                                  sort_property=sort_property,
                                                                  sort_order=sort_order)

    def get_device_profile_by_id(self, device_profile_id: DeviceProfileId,
                                 inline_images: Optional[bool] = None) -> DeviceProfile:
        device_profile_id = self.get_id(device_profile_id)
        return self.device_profile_controller.get_device_profile_by_id(device_profile_id=device_profile_id,
                                                                       inline_images=inline_images)

    # Dashboard Controller
    def get_tenant_dashboards_v1(self, tenant_id: TenantId, page_size: int, page: int,text_search: Optional[str] = None,
                                 sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataDashboardInfo:
        tenant_id = self.get_id(tenant_id)
        return self.dashboard_controller.get_tenant_dashboards_by_tenant_id(tenant_id=tenant_id, page_size=page_size,
                                                                            page=page, text_search=text_search,
                                                                            sort_property=sort_property,
                                                                            sort_order=sort_order)

    def get_dashboard_info_by_id(self, dashboard_id: DashboardId) -> DashboardInfo:
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.get_dashboard_info_by_id(dashboard_id=dashboard_id)

    def get_home_dashboard(self, accept_encoding: Optional[str] = None) -> HomeDashboard:
        return self.dashboard_controller.get_home_dashboard(accept_encoding=accept_encoding)

    def set_tenant_home_dashboard_info(self, body: HomeDashboardInfo) -> None:
        return self.dashboard_controller.set_tenant_home_dashboard_info(body=body)

    def get_server_time(self, ) -> int:
        return self.dashboard_controller.get_server_time()

    def get_highest_alarm_severity(self, entity_id: EntityId, search_status: Optional[str] = None,
                                   status: Optional[str] = None, assignee_id: Optional[str] = None) -> str:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.alarm_controller.get_highest_alarm_severity(entity_id=entity_id, entity_type=entity_type,
                                                                search_status=search_status, status=status,
                                                                assignee_id=assignee_id)

    def get_alarm_types(self, page_size: int, page: int,
                        text_search: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataEntitySubtype:
        return self.alarm_controller.get_alarm_types(page_size=page_size, page=page, text_search=text_search,
                                                     sort_order=sort_order)

    def get_max_datapoints_limit(self, ) -> int:
        return self.dashboard_controller.get_max_datapoints_limit()

    def get_home_dashboard_info(self, ) -> HomeDashboardInfo:
        return self.dashboard_controller.get_home_dashboard_info()

    def get_dashboard_by_id(self, dashboard_id: DashboardId, include_resources: Optional[bool] = None,
                            accept_encoding: Optional[str] = None) -> Dashboard:
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.get_dashboard_by_id(dashboard_id=dashboard_id,
                                                             include_resources=include_resources,
                                                             accept_encoding=accept_encoding)

    def get_tenant_dashboards(self, page_size: int, page: int, mobile: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None,
                              sort_order: Optional[str] = None) -> PageDataDashboardInfo:
        return self.dashboard_controller.get_tenant_dashboards(page_size=page_size, page=page, mobile=mobile,
                                                               text_search=text_search,
                                                               sort_property=sort_property,
                                                               sort_order=sort_order)

    def delete_dashboard(self, dashboard_id: DashboardId) -> None:
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.delete_dashboard(dashboard_id=dashboard_id)

    def get_tenant_home_dashboard_info(self, ) -> HomeDashboardInfo:
        return self.dashboard_controller.get_tenant_home_dashboard_info()

    # Entity Query Controller
    def find_entity_timeseries_and_attributes_keys_by_query(self, timeseries: bool, attributes: bool, body: Optional[
        EntityDataQuery], scope: Optional[str] = None) -> AvailableEntityKeys:
        return self.entity_query_controller.find_available_entity_keys_by_query(
            timeseries=timeseries, attributes=attributes, body=body, scope=scope)

    def find_alarm_data_by_query(self, body: AlarmDataQuery) -> PageDataAlarmData:
        return self.entity_query_controller.find_alarm_data_by_query(body=body)

    def find_entity_data_by_query(self, body: EntityDataQuery) -> PageDataEntityData:
        return self.entity_query_controller.find_entity_data_by_query(body=body)

    def process_system_edqs_request(self, body: ToCoreEdqsRequest) -> None:
        return self.entity_query_controller.process_system_edqs_request(body=body)

    def get_edqs_state(self) -> EdqsState:
        return self.entity_query_controller.get_edqs_state()

    def find_available_entity_keys_by_query(self, body: EntityDataQuery, timeseries: bool, attributes: bool,
                                            scope: Optional[str] = None) -> AvailableEntityKeys:
        return self.entity_query_controller.find_available_entity_keys_by_query(body=body, timeseries=timeseries,
                                                                                attributes=attributes, scope=scope)

    # Widget Type Controller
    def get_bundle_widget_type_fqns(self, widgets_bundle_id: WidgetsBundleId) -> List[str]:
        widgets_bundle_id = self.get_id(widgets_bundle_id)
        return self.widget_type_controller.get_bundle_widget_type_fqns(widgets_bundle_id=widgets_bundle_id)

    def get_widget_types(self, page_size: int, page: int,
                         text_search: Optional[str] = None,
                         sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                         tenant_only: Optional[bool] = None, full_search: Optional[bool] = None,
                         deprecated_filter: Optional[str] = None, widget_type_list: Optional[List[str]] = None,
                         scada_first: Optional[bool] = None) -> PageDataWidgetTypeInfo:
        if widget_type_list:
            widget_type_list = ','.join(widget_type_list)
        return self.widget_type_controller.get_widget_types(page_size=page_size, page=page,
                                                            text_search=text_search,
                                                            sort_property=sort_property,
                                                            sort_order=sort_order, tenant_only=tenant_only,
                                                            full_search=full_search,
                                                            deprecated_filter=deprecated_filter,
                                                            widget_type_list=widget_type_list,
                                                            scada_first=scada_first)

    def get_widget_type_info_by_id(self, widget_type_id: WidgetTypeId) -> WidgetTypeInfo:
        widget_type_id = self.get_id(widget_type_id)
        return self.widget_type_controller.get_widget_type_info_by_id(widget_type_id=widget_type_id)

    def get_widget_type(self, fqn) -> WidgetType:
        fqn = str(fqn)
        return self.widget_type_controller.get_widget_type(fqn=fqn)

    def get_bundle_widget_types_infos(self, widgets_bundle_id: WidgetsBundleId, page_size: int, page: int,
                                      text_search: Optional[str] = None,
                                      sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                                      full_search: Optional[bool] = None, deprecated_filter: Optional[str] = None,
                                      widget_type_list: Optional[List[str]] = None) -> PageDataWidgetTypeInfo:
        widgets_bundle_id = self.get_id(widgets_bundle_id)

        if widget_type_list:
            widget_type_list = ','.join(widget_type_list)

        return self.widget_type_controller.get_bundle_widget_types_infos(widgets_bundle_id=widgets_bundle_id,
                                                                         page_size=page_size, page=page,
                                                                         text_search=text_search,
                                                                         sort_property=sort_property,
                                                                         sort_order=sort_order,
                                                                         full_search=full_search,
                                                                         deprecated_filter=deprecated_filter,
                                                                         widget_type_list=widget_type_list)

    def get_bundle_widget_types_details(self, widgets_bundle_id: WidgetsBundleId,
                                        include_resources: Optional[bool] = None) -> List[WidgetTypeDetails]:
        widgets_bundle_id = self.get_id(widgets_bundle_id)
        return self.widget_type_controller.get_bundle_widget_types_details(widgets_bundle_id=widgets_bundle_id,
                                                                           include_resources=include_resources)

    def delete_widget_type(self, widget_type_id: WidgetTypeId) -> None:
        widget_type_id = self.get_id(widget_type_id)
        return self.widget_type_controller.delete_widget_type(widget_type_id=widget_type_id)

    def save_widget_type(self, body: WidgetTypeDetails,
                         update_existing_by_fqn: Optional[bool] = None) -> WidgetTypeDetails:
        return self.widget_type_controller.save_widget_type(body=body, update_existing_by_fqn=update_existing_by_fqn)

    def get_bundle_widget_types(self, widgets_bundle_id: WidgetsBundleId) -> List[WidgetType]:
        widgets_bundle_id = self.get_id(widgets_bundle_id)
        return self.widget_type_controller.get_bundle_widget_types(widgets_bundle_id=widgets_bundle_id)

    def get_widget_type_by_id(self, widget_type_id: WidgetTypeId,
                              include_resources: Optional[bool] = None) -> WidgetTypeDetails:
        widget_type_id = self.get_id(widget_type_id)
        return self.widget_type_controller.get_widget_type_by_id(widget_type_id=widget_type_id,
                                                                 include_resources=include_resources)

    # Audit Log Controller
    def get_audit_logs_by_customer_id(self, customer_id: CustomerId, page_size: int, page: int,
                                      text_search: Optional[str] = None,
                                      sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                                      start_time: Optional[int] = None, end_time: Optional[int] = None,
                                      action_types: Optional[str] = None) -> PageDataAuditLog:
        customer_id = self.get_id(customer_id)
        return self.audit_log_controller.get_audit_logs_by_customer_id(customer_id=customer_id,
                                                                       page_size=page_size, page=page,
                                                                       text_search=text_search,
                                                                       sort_property=sort_property,
                                                                       sort_order=sort_order,
                                                                       start_time=start_time,
                                                                       end_time=end_time,
                                                                       action_types=action_types)

    def get_audit_logs_by_user_id(self, user_id: UserId, page_size: int, page: int, text_search: Optional[str] = None,
                                  sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                                  start_time: Optional[int] = None, end_time: Optional[int] = None,
                                  action_types: Optional[str] = None) -> PageDataAuditLog:
        user_id = self.get_id(user_id)
        return self.audit_log_controller.get_audit_logs_by_user_id(user_id=user_id, page_size=page_size,
                                                                   page=page, text_search=text_search,
                                                                   sort_property=sort_property,
                                                                   sort_order=sort_order,
                                                                   start_time=start_time, end_time=end_time,
                                                                   action_types=action_types)

    def get_audit_logs(self, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None,
                       sort_order: Optional[str] = None,
                       start_time: Optional[int] = None, end_time: Optional[int] = None,
                       action_types: Optional[str] = None) -> PageDataAuditLog:
        return self.audit_log_controller.get_audit_logs(page_size=page_size, page=page,
                                                        text_search=text_search, sort_property=sort_property,
                                                        sort_order=sort_order, start_time=start_time,
                                                        end_time=end_time, action_types=action_types)

    def get_audit_logs_by_entity_id(self, entity_id: EntityId, page_size: int, page: int,
                                    text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                                    start_time: Optional[int] = None, end_time: Optional[int] = None,
                                    action_types: Optional[str] = None) -> PageDataAuditLog:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.audit_log_controller.get_audit_logs_by_entity_id(entity_type=entity_type,
                                                                     entity_id=entity_id, page_size=page_size,
                                                                     page=page, text_search=text_search,
                                                                     sort_property=sort_property,
                                                                     sort_order=sort_order,
                                                                     start_time=start_time, end_time=end_time,
                                                                     action_types=action_types)

    # Lwm2M Controller
    def get_lwm2m_bootstrap_security_info(self, is_bootstrap_server: bool) -> LwM2MServerSecurityConfigDefault:
        return self.lwm2m_controller.get_lwm2m_bootstrap_security_info(
            is_bootstrap_server=is_bootstrap_server)

    def save_device_with_credentials(self, body: SaveDeviceWithCredentialsRequest,
                                     entity_group_id: Optional[str] = None, entity_group_ids: Optional[str] = None,
                                     name_conflict_policy: Optional[str] = None,
                                     uniquify_separator: Optional[str] = None,
                                     uniquify_strategy: Optional[str] = None) -> Device:
        return self.device_controller.save_device_with_credentials(body=body, entity_group_id=entity_group_id,
                                                                   entity_group_ids=entity_group_ids,
                                                                   name_conflict_policy=name_conflict_policy,
                                                                   uniquify_separator=uniquify_separator,
                                                                   uniquify_strategy=uniquify_strategy)

    # Component Descriptor Controller
    def get_component_descriptors_by_type(self, component_type: str, rule_chain_type: Optional[str] = None) -> List[
        ComponentDescriptor]:
        return self.component_descriptor_controller.get_component_descriptors_by_type(
            component_type=component_type, rule_chain_type=rule_chain_type)

    def get_component_descriptor_by_clazz(self, component_descriptor_clazz: str) -> ComponentDescriptor:
        return self.component_descriptor_controller.get_component_descriptor_by_clazz(
            component_descriptor_clazz=component_descriptor_clazz)

    def get_component_descriptors_by_types(self, component_types: str, rule_chain_type: Optional[str] = None) -> List[
        ComponentDescriptor]:
        return self.component_descriptor_controller.get_component_descriptors_by_types(
            component_types=component_types, rule_chain_type=rule_chain_type)

    # UI Controller
    def get_help_base_url(self, ) -> str:
        return self.ui_settings_controller.get_help_base_url()

    # Device API Controller
    def subscribe_to_attributes(self, device_token: str, timeout: Optional[int] = None) -> Dict:
        return self.device_api_controller.subscribe_to_attributes(device_token=device_token, timeout=timeout)

    def subscribe_to_commands(self, device_token: str, timeout: Optional[int] = None) -> Dict:
        return self.device_api_controller.subscribe_to_commands(device_token=device_token, timeout=timeout)

    def get_device_attributes(self, device_token: str, client_keys: Optional[str] = None,
                              shared_keys: Optional[str] = None, all_client_keys: Optional[bool] = None,
                              all_shared_keys: Optional[bool] = None) -> Dict:
        return self.device_api_controller.get_device_attributes(device_token=device_token, client_keys=client_keys,
                                                                shared_keys=shared_keys,
                                                                all_client_keys=all_client_keys,
                                                                all_shared_keys=all_shared_keys)

    def get_firmware(self, device_token: str, title: str, version: str, size: Optional[int] = None,
                     chunk: Optional[int] = None) -> bytes:
        return self.device_api_controller.get_firmware(device_token=device_token, title=title,
                                                       version=version, size=size, chunk=chunk)

    def reply_to_command(self, device_token: str, request_id: int, body: str) -> None:
        return self.device_api_controller.reply_to_command(device_token=device_token, request_id=request_id,
                                                           body=body)

    def get_software(self, device_token: str, title: str, version: str, size: Optional[int] = None,
                     chunk: Optional[int] = None) -> bytes:
        return self.device_api_controller.get_software(device_token=device_token, title=title,
                                                       version=version, size=size, chunk=chunk)

    def post_telemetry(self, device_token: str, body: str) -> None:
        return self.device_api_controller.post_telemetry(device_token=device_token, body=body)

    def claim_device(self, device_token: str, body: Optional[str] = None) -> None:
        return self.device_api_controller.save_claiming_info(device_token=device_token, body=body)

    def post_rpc_request(self, device_token: str, body: Dict) -> Any:
        return self.device_api_controller.post_rpc_request(device_token=device_token, body=body)

    def provision_device(self, body: str) -> Dict:
        return self.device_api_controller.provision_device(body=body)

    def post_device_attributes(self, device_token: str, body: str) -> None:
        return self.device_api_controller.post_device_attributes(device_token=device_token, body=body)

    # Tenant Controller
    def get_tenant_infos(self, page_size: int, page: int,text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataTenantInfo:
        return self.tenant_controller.get_tenant_infos(page_size=page_size, page=page,
                                                       text_search=text_search, sort_property=sort_property,
                                                       sort_order=sort_order)

    def get_tenant_by_id(self, tenant_id: TenantId) -> Tenant:
        tenant_id = self.get_id(tenant_id)
        return self.tenant_controller.get_tenant_by_id(tenant_id=tenant_id)

    def save_tenant(self, body: Tenant) -> Tenant:
        return self.tenant_controller.save_tenant(body=body)

    def get_tenants(self, page_size: int, page: int,text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataTenant:
        return self.tenant_controller.get_tenants(page_size=page_size, page=page, text_search=text_search,
                                                  sort_property=sort_property, sort_order=sort_order)

    def get_tenant_info_by_id(self, tenant_id: TenantId) -> TenantInfo:
        tenant_id = self.get_id(tenant_id)
        return self.tenant_controller.get_tenant_info_by_id(tenant_id=tenant_id)

    def delete_tenant(self, tenant_id: TenantId) -> None:
        tenant_id = self.get_id(tenant_id)
        return self.tenant_controller.delete_tenant(tenant_id=tenant_id)

    def get_tenants_by_ids(self, tenant_ids: list) -> List[Tenant]:
        tenant_ids = ','.join(tenant_ids)
        return self.tenant_controller.get_tenants_by_ids(tenant_ids=str(tenant_ids))

    # OTA Package Controller
    def delete_ota_package(self, ota_package_id: OtaPackageId) -> None:
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.delete_ota_package(ota_package_id=ota_package_id)

    def save_ota_package_data(self, ota_package_id: OtaPackageId, checksum_algorithm: str, file,
                              checksum=None) -> OtaPackageInfo:
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.save_ota_package_data(checksum_algorithm=checksum_algorithm,
                                                                 ota_package_id=ota_package_id, file=file,
                                                                 checksum=checksum)

    def get_ota_packages_v1(self, device_profile_id: DeviceProfileId, type: str, page_size: int, page: int,
                           text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataOtaPackageInfo:
        device_profile_id = self.get_id(device_profile_id)
        return self.ota_package_controller.get_ota_packages_by_device_profile_and_type(device_profile_id=device_profile_id, type=type,
                                                                                       page_size=page_size, page=page,
                                                                                       text_search=text_search,
                                                                                       sort_property=sort_property,
                                                                                       sort_order=sort_order)

    def save_ota_package_info(self, body: SaveOtaPackageInfoRequest) -> OtaPackageInfo:
        return self.ota_package_controller.save_ota_package_info(body=body)

    def get_ota_packages(self, page_size: int, page: int,text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataOtaPackageInfo:
        return self.ota_package_controller.get_ota_packages(page_size=page_size, page=page,
                                                            text_search=text_search,
                                                            sort_property=sort_property,
                                                            sort_order=sort_order)

    def get_ota_package_by_id(self, ota_package_id: OtaPackageId) -> OtaPackage:
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.get_ota_package_by_id(ota_package_id=ota_package_id)

    def download_ota_package(self, ota_package_id: OtaPackageId) -> bytes:
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.download_ota_package(ota_package_id=ota_package_id)

    def get_ota_package_info_by_id(self, ota_package_id: OtaPackageId) -> OtaPackageInfo:
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.get_ota_package_info_by_id(ota_package_id=ota_package_id)

    def save_entities_version(self, body: VersionCreateRequest) -> str:
        return self.entities_version_control_controller.save_entities_version(body=body)

    def get_version_load_request_status(self, request_id: str) -> VersionLoadResult:
        return self.entities_version_control_controller.get_version_load_request_status(request_id=request_id)

    def list_branches(self) -> List[BranchInfo]:
        return self.entities_version_control_controller.list_branches()

    def list_entity_versions(self, entity_type: str, external_entity_uuid: str, branch: str, page_size: int, page: int,
                             text_search: Optional[str] = None, sort_property: Optional[str] = None,
                             sort_order: Optional[str] = None,
                             internal_entity_id: Optional[str] = None) -> PageDataEntityVersion:
        return self.entities_version_control_controller.list_entity_versions(entity_type=entity_type,
                                                                             external_entity_uuid=external_entity_uuid,
                                                                             branch=branch,
                                                                             page_size=page_size, page=page,
                                                                             text_search=text_search,
                                                                             sort_property=sort_property,
                                                                             sort_order=sort_order,
                                                                             internal_entity_id=internal_entity_id)

    def get_entity_data_info(self, version_id: str, entity_id: EntityId,
                             internal_entity_id: Optional[str] = None) -> EntityDataInfo:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.entities_version_control_controller.get_entity_data_info(version_id=version_id,
                                                                             entity_type=entity_type,
                                                                             external_entity_uuid=entity_id,
                                                                             internal_entity_id=internal_entity_id)

    def get_version_create_request_status(self, request_id: str) -> VersionCreationResult:
        return self.entities_version_control_controller.get_version_create_request_status(
            request_id=request_id)

    def load_entities_version(self, body: VersionLoadRequest) -> str:
        return self.entities_version_control_controller.load_entities_version(body=body)

    def list_entity_type_versions(self, entity_type: str, branch: str, page_size: int, page: int,
                                  text_search: Optional[str] = None,
                                  sort_property: Optional[str] = None,
                                  sort_order: Optional[str] = None) -> PageDataEntityVersion:
        return self.entities_version_control_controller.list_entity_type_versions(entity_type=entity_type,
                                                                                  branch=branch,
                                                                                  page_size=page_size,
                                                                                  page=page,
                                                                                  text_search=text_search,
                                                                                  sort_property=sort_property,
                                                                                  sort_order=sort_order)

    def list_entities_at_version(self, entity_type: str, version_id: str) -> List[VersionedEntityInfo]:
        return self.entities_version_control_controller.list_entities_at_version(entity_type=entity_type,
                                                                                 version_id=version_id)

    def list_all_entities_at_version(self, version_id: str) -> List[VersionedEntityInfo]:
        return self.entities_version_control_controller.list_all_entities_at_version(version_id=version_id)

    def compare_entity_data_to_version(self, entity_id: EntityId,
                                       version_id: str) -> EntityDataDiff:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.entities_version_control_controller.compare_entity_data_to_version(
            entity_type=entity_type, internal_entity_uuid=entity_id, version_id=version_id)

    def list_versions(self, branch: str, page_size: int, page: int, text_search: Optional[str] = None,
                      sort_property: Optional[str] = None,
                      sort_order: Optional[str] = None) -> PageDataEntityVersion:
        return self.entities_version_control_controller.list_versions(branch=branch, page_size=page_size,
                                                                      page=page, text_search=text_search,
                                                                      sort_property=sort_property,
                                                                      sort_order=sort_order)

    def delete_queue(self, queue_id: QueueId) -> None:
        queue_id = self.get_id(queue_id)
        return self.queue_controller.delete_queue(queue_id=queue_id)

    def get_queue_by_id(self, queue_id: QueueId) -> Queue:
        queue_id = self.get_id(queue_id)
        return self.queue_controller.get_queue_by_id(queue_id=queue_id)

    def get_queue_by_name(self, queue_name: str) -> Queue:
        return self.queue_controller.get_queue_by_name(queue_name=queue_name)

    # Two-Factor Auth Controller
    def check_two_fa_verification_code(self, provider_type: str, verification_code: str) -> JwtPair:
        return self.two_factor_auth_controller.check_two_fa_verification_code(provider_type=provider_type,
                                                                              verification_code=verification_code)

    def get_available_two_fa_providers_v1(self, ) -> List[TwoFaProviderInfo]:
        return self.two_factor_auth_controller.get_available_two_fa_provider_infos()

    def request_two_fa_verification_code(self, provider_type: str) -> None:
        return self.two_factor_auth_controller.request_two_fa_verification_code(provider_type=provider_type)

    def authenticate_by_two_fa_configuration_token(self) -> JwtPair:
        return self.two_factor_auth_controller.authenticate_by_two_fa_configuration_token()

    # Tow Factor Auth Config Controller
    def delete_two_fa_account_config(self, provider_type: str) -> AccountTwoFaSettings:
        return self.two_factor_auth_config_controller.delete_two_fa_account_config(provider_type=provider_type)

    def generate_two_fa_account_config(self, provider_type: str) -> TwoFaAccountConfig:
        return self.two_factor_auth_config_controller.generate_two_fa_account_config(provider_type=provider_type)

    def get_account_two_fa_settings(self) -> AccountTwoFaSettings:
        return self.two_factor_auth_config_controller.get_account_two_fa_settings()

    def get_available_two_fa_providers(self) -> List[str]:
        return self.two_factor_auth_config_controller.get_available_two_fa_provider_types()

    def get_platform_two_fa_settings(self) -> PlatformTwoFaSettings:
        return self.two_factor_auth_config_controller.get_platform_two_fa_settings()

    def save_platform_two_fa_settings(self, body: PlatformTwoFaSettings) -> PlatformTwoFaSettings:
        return self.two_factor_auth_config_controller.save_platform_two_fa_settings(body=body)

    def submit_two_fa_account_config(self, body: TwoFaAccountConfig) -> None:
        return self.two_factor_auth_config_controller.submit_two_fa_account_config(body=body)

    def update_two_fa_account_config(self, provider_type: str,
                                     body: TwoFaAccountConfigUpdateRequest) -> AccountTwoFaSettings:
        return self.two_factor_auth_config_controller.update_two_fa_account_config(
            provider_type=provider_type, body=body)

    def verify_and_save_two_fa_account_config(self, body: TwoFaAccountConfig,
                                              verification_code: Optional[str] = None) -> AccountTwoFaSettings:
        return self.two_factor_auth_config_controller.verify_and_save_two_fa_account_config(
            body=body, verification_code=verification_code)

    def create_notification_request(self, body: NotificationRequest) -> NotificationRequest:
        return self.notification_controller.create_notification_request(body=body)

    def delete_notification_request(self, id: str) -> None:
        return self.notification_controller.delete_notification_request(id=id)

    def delete_notification(self, id: str) -> None:
        return self.notification_controller.delete_notification(id=id)

    def get_available_delivery_methods(self) -> List[str]:
        return self.notification_controller.get_available_delivery_methods()

    def get_notification_request_by_id(self, id: str) -> NotificationRequestInfo:
        return self.notification_controller.get_notification_request_by_id(id=id)

    def get_notification_request_preview(self, body: NotificationRequest,
                                         recipients_preview_size: Optional[int] = None) -> NotificationRequestPreview:
        return self.notification_controller.get_notification_request_preview(
            body=body, recipients_preview_size=recipients_preview_size)

    def get_notification_requests(self, page_size: int, page: int, text_search: Optional[str] = None,
                                  sort_property: Optional[str] = None,
                                  sort_order: Optional[str] = None) -> PageDataNotificationRequestInfo:
        return self.notification_controller.get_notification_requests(page_size=page_size, page=page,
                                                                      text_search=text_search,
                                                                      sort_property=sort_property,
                                                                      sort_order=sort_order)

    def get_notification_settings(self) -> NotificationSettings:
        return self.notification_controller.get_notification_settings()

    def get_notifications(self, page_size: int, page: int, text_search: Optional[str] = None,
                          sort_property: Optional[str] = None,
                          sort_order: Optional[str] = None, delivery_method: Optional[str] = None,
                          unread_only: Optional[bool] = None) -> PageDataNotification:
        return self.notification_controller.get_notifications(page_size=page_size, page=page,
                                                              text_search=text_search,
                                                              sort_property=sort_property,
                                                              sort_order=sort_order,
                                                              delivery_method=delivery_method,
                                                              unread_only=unread_only)

    def get_unread_notifications_count(self, delivery_method: Optional[str] = None) -> int:
        return self.notification_controller.get_unread_notifications_count(delivery_method=delivery_method)

    def mark_all_notifications_as_read(self,
                                       delivery_method: Optional[str] = None) -> None:
        return self.notification_controller.mark_all_notifications_as_read(delivery_method=delivery_method)

    def mark_notification_as_read(self, id: str) -> None:
        return self.notification_controller.mark_notification_as_read(id=id)

    def save_notification_settings(self, body: NotificationSettings) -> NotificationSettings:
        return self.notification_controller.save_notification_settings(body=body)

    def get_user_notification_settings(self) -> UserNotificationSettings:
        return self.notification_controller.get_user_notification_settings()

    def save_user_notification_settings(self, body: UserNotificationSettings) -> UserNotificationSettings:
        return self.notification_controller.save_user_notification_settings(body=body)

    def send_entities_limit_increase_request(self, entity_type: str,
                                             subscription_violation: Optional[bool] = None) -> None:
        return self.notification_controller.send_entities_limit_increase_request(
            entity_type=entity_type, subscription_violation=subscription_violation)

    def delete_notification_rule(self, id: str) -> None:
        return self.notification_rule_controller.delete_notification_rule(id=id)

    def get_notification_rule_by_id(self, id: str) -> NotificationRuleInfo:
        return self.notification_rule_controller.get_notification_rule_by_id(id=id)

    def get_notification_rules(self, page_size: int, page: int, text_search: Optional[str] = None,
                               sort_property: Optional[str] = None,
                               sort_order: Optional[str] = None) -> PageDataNotificationRuleInfo:
        return self.notification_rule_controller.get_notification_rules(page_size=page_size, page=page,
                                                                        text_search=text_search,
                                                                        sort_property=sort_property,
                                                                        sort_order=sort_order)

    def save_notification_rule(self, body: NotificationRule) -> NotificationRule:
        return self.notification_rule_controller.save_notification_rule(body=body)

    def delete_notification_target_by_id(self, id: str) -> None:
        return self.notification_target_controller.delete_notification_target_by_id(id=id)

    def get_notification_target_by_id(self, id: str) -> NotificationTarget:
        return self.notification_target_controller.get_notification_target_by_id(id=id)

    def get_notification_targets_by_ids(self, ids: list) -> List[NotificationTarget]:
        ids = ','.join(ids)
        return self.notification_target_controller.get_notification_targets_by_ids(ids=ids)

    def get_notification_targets_by_supported_notification_type(self, notification_type: str, page_size: int, page: int,
                                                                text_search: Optional[str] = None,
                                                                sort_property: Optional[str] = None,
                                                                sort_order: Optional[
                                                                    str] = None) -> PageDataNotificationTarget:
        return self.notification_target_controller.get_notification_targets_by_supported_notification_type(
            notification_type=notification_type, page_size=page_size, page=page, text_search=text_search,
            sort_property=sort_property, sort_order=sort_order)

    def get_notification_targets(self, page_size: int, page: int, text_search: Optional[str] = None,
                                 sort_property: Optional[str] = None,
                                 sort_order: Optional[str] = None) -> PageDataNotificationTarget:
        return self.notification_target_controller.get_notification_targets(page_size=page_size, page=page,
                                                                            text_search=text_search,
                                                                            sort_property=sort_property,
                                                                            sort_order=sort_order)

    def get_recipients_for_notification_target_config(self, body: NotificationTarget, page_size: int,
                                                      page: int) -> PageDataUser:
        return self.notification_target_controller.get_recipients_for_notification_target_config(
            body=body, page_size=page_size, page=page)

    def save_notification_target(self, body: NotificationTarget) -> NotificationTarget:
        return self.notification_target_controller.save_notification_target(body=body)

    def delete_notification_template_by_id(self, id: str) -> None:
        return self.notification_template_controller.delete_notification_template_by_id(id=id)

    def get_notification_template_by_id(self, id: str) -> NotificationTemplate:
        return self.notification_template_controller.get_notification_template_by_id(id=id)

    def get_notification_templates(self, page_size: int, page: int, text_search: Optional[str] = None,
                                   sort_property: Optional[str] = None,
                                   sort_order: Optional[str] = None,
                                   notification_types: Optional[List[str]] = None) -> PageDataNotificationTemplate:
        return self.notification_template_controller.get_notification_templates(page_size=page_size,
                                                                                page=page,
                                                                                text_search=text_search,
                                                                                sort_property=sort_property,
                                                                                sort_order=sort_order,
                                                                                notification_types=notification_types)

    def list_slack_conversations(self, type: str, token: Optional[str] = None) -> List[SlackConversation]:
        return self.notification_template_controller.list_slack_conversations(type=type, token=token)

    def save_notification_template(self, body: NotificationTemplate) -> NotificationTemplate:
        return self.notification_template_controller.save_notification_template(body=body)

    def count_entities_by_query(self, body: EntityCountQuery) -> int:
        return self.entity_query_controller.count_entities_by_query(body=body)

    # Device Connectivity Controller
    def download_server_certificate(self, protocol: str) -> bytes:
        return self.device_connectivity_controller.download_server_certificate(protocol=protocol)

    def get_device_publish_telemetry_commands(self, device_id: DeviceId) -> JsonNode:
        device_id = self.get_id(device_id)
        return self.device_connectivity_controller.get_device_publish_telemetry_commands(device_id=device_id)

    # Mail Config Template Controller
    def get_client_registration_templates_mail(self) -> JsonNode:
        return self.mail_config_template_controller.get_mail_config_templates()

    # Image Controller
    def delete_image(self, _type: str, key: str, force: Optional[bool] = None) -> TbImageDeleteResult:
        return self.image_controller.delete_image(type=_type, key=key, force=force)

    def download_image_preview(self, type: str, key: str, if_none_match: Optional[str] = None,
                               accept_encoding: Optional[str] = None) -> bytes:
        return self.image_controller.download_image_preview(type=type, key=key, if_none_match=if_none_match,
                                                            accept_encoding=accept_encoding)

    def download_image(self, _type: str, key: str, if_none_match: Optional[str] = '',
                       accept_encoding: Optional[str] = None) -> bytes:
        return self.image_controller.download_image(type=_type, key=key, if_none_match=if_none_match,
                                                    accept_encoding=accept_encoding)

    def download_public_image(self, public_resource_key: str, if_none_match: Optional[str] = '',
                              accept_encoding: Optional[str] = None) -> bytes:
        return self.image_controller.download_public_image(public_resource_key=public_resource_key,
                                                           if_none_match=if_none_match,
                                                           accept_encoding=accept_encoding)

    def export_image(self, _type: str, key: str) -> ResourceExportData:
        return self.image_controller.export_image(type=_type, key=key)

    def get_image_info(self, _type: str, key: str) -> TbResourceInfo:
        return self.image_controller.get_image_info(type=_type, key=key)

    def get_images(self, page_size: int, page: int, text_search: Optional[str] = None,
                   include_system_images: Optional[bool] = None,
                   sort_property: Optional[str] = None,
                   sort_order: Optional[str] = None,
                   image_sub_type: Optional[str] = None) -> PageDataTbResourceInfo:
        return self.image_controller.get_images(page_size=page_size, page=page, text_search=text_search,
                                                include_system_images=include_system_images,
                                                sort_order=sort_order, sort_property=sort_property,
                                                image_sub_type=image_sub_type)

    def import_image(self, body: ResourceExportData) -> TbResourceInfo:
        return self.image_controller.import_image(body=body)

    def update_image_info(self, _type: str, key: str, body: TbResourceInfo) -> TbResourceInfo:
        return self.image_controller.update_image_info(type=_type, key=key, body=body)

    def update_image_public_status(self, _type: str, key: str, is_public: bool) -> TbResourceInfo:
        return self.image_controller.update_image_public_status(type=_type, key=key, is_public=is_public)

    def update_image(self, _type: str, key: str, file: str) -> TbResourceInfo:
        return self.image_controller.update_image(type=_type, key=key, file=file)

    def upload_image(self, file: str, title: Optional[str] = None,
                     image_sub_type: Optional[str] = None) -> TbResourceInfo:
        return self.image_controller.upload_image(title=title, file=file, image_sub_type=image_sub_type)

    def get_asset_profile_by_id(self, asset_profile_id: str, inline_images: Optional[bool] = None) -> AssetProfile:
        return self.asset_profile_controller.get_asset_profile_by_id(asset_profile_id=asset_profile_id,
                                                                     inline_images=inline_images)

    def get_asset_profile_by_names(self, active_only: Optional[bool] = None) -> List[EntityInfo]:
        return self.asset_profile_controller.get_asset_profile_names(active_only=active_only)

    def get_asset_profiles_by_ids(self, asset_profile_ids: List[str]) -> List[AssetProfileInfo]:
        asset_profile_ids = ','.join(asset_profile_ids)
        return self.asset_profile_controller.get_asset_profiles_by_ids(asset_profile_ids=asset_profile_ids)

    def download_gateway_docker_compose(self, device_id: DeviceId) -> bytes:
        device_id = self.get_id(device_id)
        return self.device_connectivity_controller.download_gateway_docker_compose(device_id=device_id)

    def get_device_profile_names(self, active_only: Optional[bool] = None) -> List[EntityInfo]:
        return self.device_profile_controller.get_device_profile_names(active_only=active_only)

    def get_edge_install_instructions(self, edge_id: EdgeId, method: str) -> EdgeInstructions:
        edge_id = self.get_id(edge_id)
        return self.edge_controller.get_edge_install_instructions(edge_id=edge_id, method=method)

    def get_edge_upgrade_instructions(self, edge_version: str, method: str) -> EdgeInstructions:
        return self.edge_controller.get_edge_upgrade_instructions(edge_version=edge_version, method=method)

    def is_edge_upgrade_available(self, edge_id: EdgeId) -> bool:
        edge_id = self.get_id(edge_id)
        return self.edge_controller.is_edge_upgrade_available(edge_id=edge_id)

    def get_queue_stats_by_id(self, queue_stats_id: QueueId) -> QueueStats:
        queue_stats_id = self.get_id(queue_stats_id)
        return self.queue_stats_controller.get_queue_stats_by_id(queue_stats_id=queue_stats_id)

    def get_queue_stats_by_ids(self, queue_stats_ids: List[str]) -> List[QueueStats]:
        queue_stats_ids = ','.join(queue_stats_ids)
        return self.queue_stats_controller.get_queue_stats_by_ids(queue_stats_ids=queue_stats_ids)

    def get_tenant_queue_stats(self, page_size: int, page: int, text_search: Optional[str] = None,
                               sort_property: Optional[str] = None,
                               sort_order: Optional[str] = None) -> PageDataQueueStats:
        return self.queue_stats_controller.get_tenant_queue_stats(page_size=page_size, page=page,
                                                                  text_search=text_search, sort_property=sort_property,
                                                                  sort_order=sort_order)

    def delete_domain(self, domain_id: DomainId) -> None:
        domain_id = self.get_id(domain_id)
        return self.domain_controller.delete_domain(id=domain_id)

    def get_domain_infos(self, page_size: int, page: int, text_search: Optional[str] = None,
                               sort_property: Optional[str] = None,
                               sort_order: Optional[str] = None) -> PageDataDomainInfo:
        return self.domain_controller.get_domain_infos(page_size=page_size, page=page,
                                                                  text_search=text_search, sort_property=sort_property,
                                                                  sort_order=sort_order)

    def get_domain_info_by_id(self, domain_id: DomainId) -> DomainInfo:
        domain_id = self.get_id(domain_id)
        return self.domain_controller.get_domain_info_by_id(id=domain_id)

    def get_tenant_domain_infos(self, page_size: int, page: int, text_search: Optional[str] = None,
                                sort_property: Optional[str] = None,
                                sort_order: Optional[str] = None) -> PageDataDomainInfo:
        return self.domain_controller.get_domain_infos(page_size=page_size, page=page, text_search=text_search,
                                                       sort_property=sort_property, sort_order=sort_order)

    def save_domain(self, body: Domain, oauth2_client_ids: Optional[str] = None) -> Domain:
        if oauth2_client_ids is not None:
            oauth2_client_ids = ','.join(oauth2_client_ids)
        return self.domain_controller.save_domain(body=body, oauth2_client_ids=oauth2_client_ids)

    def update_oauth2_clients(self, body: List[str], id: str) -> None:
        return self.domain_controller.update_domain_oauth2_clients(body=body, id=id)

    def delete_mobile_app(self, mobile_app_id: MobileAppId) -> None:
        mobile_app_id = self.get_id(mobile_app_id)
        return self.mobile_app_controller.delete_mobile_app(id=mobile_app_id)

    def get_mobile_app_info_by_id(self, mobile_app_id: MobileAppId) -> MobileApp:
        mobile_app_id = self.get_id(mobile_app_id)
        return self.mobile_app_controller.get_mobile_app_by_id(id=mobile_app_id)

    def get_tenant_mobile_app_infos(self, page_size: int, page: int, text_search: Optional[str] = None,
                                    sort_property: Optional[str] = None,
                                    sort_order: Optional[str] = None,
                                    platform_type: Optional[str] = None) -> PageDataMobileApp:
        return self.mobile_app_controller.get_tenant_mobile_apps(page_size=page_size, page=page,
                                                                 text_search=text_search,
                                                                 sort_property=sort_property,
                                                                 sort_order=sort_order,
                                                                 platform_type=platform_type)

    def save_mobile_app(self, body: MobileApp) -> MobileApp:
        return self.mobile_app_controller.save_mobile_app(body=body)

    def get_login_mobile_info(self, pkg_name: str, platform: str) -> LoginMobileInfo:
        return self.mobile_app_controller.get_login_mobile_info(pkg_name=pkg_name, platform=platform)

    def get_mobile_app_by_id(self, mobile_app_id: MobileAppId) -> MobileApp:
        mobile_app_id = self.get_id(mobile_app_id)
        return self.mobile_app_controller.get_mobile_app_by_id(id=mobile_app_id)

    def get_tenant_mobile_apps(self, page_size: int, page: int, text_search: Optional[str] = None,
                               sort_property: Optional[str] = None,
                               sort_order: Optional[str] = None,
                               platform_type: Optional[str] = None) -> PageDataMobileApp:
        return self.mobile_app_controller.get_tenant_mobile_apps(page_size=page_size, page=page,
                                                                 text_search=text_search,
                                                                 sort_property=sort_property,
                                                                 sort_order=sort_order,
                                                                 platform_type=platform_type)

    def get_user_mobile_info(self, pkg_name: str, platform: str) -> UserMobileInfo:
        return self.mobile_app_controller.get_user_mobile_info(pkg_name=pkg_name, platform=platform)

    def get_qr_code_settings(self) -> QrCodeSettings:
        return self.qr_code_settings_controller.get_qr_code_settings()

    def save_qr_code_settings(self, body: QrCodeSettings) -> QrCodeSettings:
        return self.qr_code_settings_controller.save_qr_code_settings(body=body)

    def delete_mobile_app_bundle(self, mobile_app_bundle_id: MobileAppBundleId) -> None:
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

    # Calculated Field Controller
    def delete_calculated_field(self, calculated_field_id) -> None:
        calculated_field_id = self.get_id(calculated_field_id)
        return self.calculated_field_controller.delete_calculated_field(calculated_field_id=calculated_field_id)

    def get_calculated_field_by_id(self, calculated_field_id) -> CalculatedField:
        calculated_field_id = self.get_id(calculated_field_id)
        return self.calculated_field_controller.get_calculated_field_by_id(calculated_field_id=calculated_field_id)

    def get_calculated_fields_by_entity_id(self, entity_id: EntityId, page_size: int, page: int,
                                           text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                           sort_order: Optional[str] = None,
                                           type: Optional[str] = None) -> PageDataCalculatedField:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.calculated_field_controller.get_calculated_fields_by_entity_id(entity_id=entity_id,
                                                                                   entity_type=entity_type,
                                                                                   page_size=page_size, page=page,
                                                                                   text_search=text_search,
                                                                                   sort_property=sort_property,
                                                                                   sort_order=sort_order,
                                                                                   type=type)

    def get_latest_calculated_field_debug_event(self, calculated_field_id: CalculatedFieldId) -> JsonNode:
        calculated_field_id = self.get_id(calculated_field_id)
        return self.calculated_field_controller.get_latest_calculated_field_debug_event(calculated_field_id=calculated_field_id)

    def save_calculated_field(self, body: CalculatedField) -> CalculatedField:
        return self.calculated_field_controller.save_calculated_field(body=body)

    def get_calculated_field_names(self, calculated_filed_type: str, page_size: int, page: int,
                                   text_search: Optional[str] = None,
                                   sort_order: Optional[str] = None) -> PageDataString:
        return self.calculated_field_controller.get_calculated_field_names(type=calculated_filed_type,
                                                                           page_size=page_size, page=page,
                                                                           text_search=text_search,
                                                                           sort_order=sort_order)

    # Job Controller
    def cancel_job(self, id: JobId) -> None:
        id = self.get_id(id)
        return self.job_controller.cancel_job(id=id)

    def delete_job(self, id: JobId) -> None:
        id = self.get_id(id)
        return self.job_controller.delete_job(id=id)

    def get_job_by_id(self, id: JobId) -> Job:
        id = self.get_id(id)
        return self.job_controller.get_job_by_id(id=id)

    def get_jobs(self, page_size: int, page: int, text_search: Optional[str] = None,
                 sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                 start_time: Optional[int] = None, end_time: Optional[int] = None, types: Optional[List[str]] = None,
                 statuses: Optional[List[str]] = None, entities: Optional[List[str]] = None,
                 include_customers: Optional[bool] = None) -> PageDataJob:
        return self.job_controller.get_jobs(page_size=page_size, page=page, text_search=text_search,
                                            sort_property=sort_property, sort_order=sort_order, start_time=start_time,
                                            end_time=end_time, types=types, statuses=statuses, entities=entities,
                                            include_customers=include_customers)

    def reprocess_job(self, id: JobId) -> None:
        id = self.get_id(id)
        return self.job_controller.reprocess_job(id=id)

    # AI Model Controller
    def delete_ai_model_by_id(self, ai_model_id: AiModelId) -> bool:
        ai_model_id = self.get_id(ai_model_id)
        return self.ai_model_controller.delete_ai_model_by_id(model_uuid=ai_model_id)

    def get_ai_model_by_id(self, ai_model_id: AiModelId) -> AiModel:
        ai_model_id = self.get_id(ai_model_id)
        return self.ai_model_controller.get_ai_model_by_id(model_uuid=ai_model_id)

    def get_ai_models(self, page_size: int, page: int, text_search: Optional[str] = None,
                        sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataAiModel:
        return self.ai_model_controller.get_ai_models(page_size=page_size, page=page, text_search=text_search,
                                                     sort_property=sort_property, sort_order=sort_order)

    def save_ai_model(self, body: AiModel) -> AiModel:
        return self.ai_model_controller.save_ai_model(body=body)

    def send_chat_request(self, body: TbChatRequest) -> TbChatResponse:
        return self.ai_model_controller.send_chat_request(body=body)

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
        self.owner_controller = OwnerControllerApi(self.api_client)
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
        self.queue_stats_controller = QueueStatsControllerApi(self.api_client)
        self.domain_controller = DomainControllerApi(self.api_client)
        self.mobile_app_controller = MobileAppControllerApi(self.api_client)
        self.mobile_app_bundle_controller = MobileAppBundleControllerApi(self.api_client)
        self.rule_engine_controller = RuleEngineControllerApi(self.api_client)
        self.qr_code_settings_controller = QrCodeSettingsControllerApi(self.api_client)
        self.calculated_field_controller = CalculatedFieldControllerApi(self.api_client)
        self.trendz_controller = TrendzControllerApi(self.api_client)
        self.job_controller = JobControllerApi(self.api_client)
        self.ai_model_controller = AiModelControllerApi(self.api_client)
        self.user_permissions_controller = UserPermissionsControllerApi(self.api_client)
        self.device_group_ota_package_controller = DeviceGroupOtaPackageControllerApi(self.api_client)
        self.converter_controller = ConverterControllerApi(self.api_client)
        self.role_controller = RoleControllerApi(self.api_client)
        self.entity_group_controller = EntityGroupControllerApi(self.api_client)
        self.report_controller = ReportControllerApi(self.api_client)
        self.scheduler_event_controller = SchedulerEventControllerApi(self.api_client)
        self.custom_menu_controller = CustomMenuControllerApi(self.api_client)
        self.integration_controller = IntegrationControllerApi(self.api_client)
        self.custom_translation_controller = CustomTranslationControllerApi(self.api_client)
        self.group_permission_controller = GroupPermissionControllerApi(self.api_client)
        self.white_labeling_controller = WhiteLabelingControllerApi(self.api_client)
        self.sign_up_controller = SignUpControllerApi(self.api_client)
        self.blob_entity_controller = BlobEntityControllerApi(self.api_client)
        self.self_registration_controller = SelfRegistrationControllerApi(self.api_client)
        self.translation_controller = TranslationControllerApi(self.api_client)
        self.converter_library_controller = ConverterLibraryControllerApi(self.api_client)
        self.secret_controller = SecretControllerApi(self.api_client)
        self.dashboard_report_controller = DashboardReportControllerApi(self.api_client)
        self.report_template_controller = ReportTemplateControllerApi(self.api_client)
        self.trendz_api_controller = TrendzApiControllerApi(self.api_client)
        self.agent_app_profile_controller = AgentAppProfileControllerApi(self.api_client)
        self.agent_app_template_controller = AgentAppTemplateControllerApi(self.api_client)
        self.agent_application_controller = AgentApplicationControllerApi(self.api_client)
        self.agent_bulk_action_controller = AgentBulkActionControllerApi(self.api_client)
        self.agent_controller = AgentControllerApi(self.api_client)
        self.agent_profile_controller = AgentProfileControllerApi(self.api_client)
        self.ai_chat_controller = AiChatControllerApi(self.api_client)
        self.ai_device_dashboard_controller = AiDeviceDashboardControllerApi(self.api_client)
        self.ai_solution_controller = AiSolutionControllerApi(self.api_client)
        self.ai_tool_controller = AiToolControllerApi(self.api_client)
        self.alarm_rule_controller = AlarmRuleControllerApi(self.api_client)
        self.api_key_controller = ApiKeyControllerApi(self.api_client)
        self.solution_export_import_controller = SolutionExportImportControllerApi(self.api_client)

    @staticmethod
    def get_type(type):
        return type.entity_type if hasattr(type, "entity_type") else type

    @staticmethod
    def get_id(id):
        return id.id if hasattr(id, "id") else id

    # Asset Controller
    def get_tenant_asset_infos(self, page_size: int, page: int, include_customers: Optional[bool] = None,
                               asset_profile_id: Optional[AssetProfileId] = None, text_search: Optional[str] = None,
                               sort_property: Optional[str] = None,
                               sort_order: Optional[str] = None) -> PageDataAssetInfo:
        asset_profile_id = self.get_id(asset_profile_id)
        return self.asset_controller.get_all_asset_infos(page_size=page_size, page=page,
                                                         include_customers=include_customers,
                                                         asset_profile_id=asset_profile_id, text_search=text_search,
                                                         sort_property=sort_property, sort_order=sort_order)

    def process_assets_bulk_import(self, body: BulkImportRequest) -> BulkImportResultAsset:
        return self.asset_controller.process_asset_bulk_import(body=body)

    # Since 4.4 entities are not assigned to customers: the customer becomes the owner instead.
    # The wrappers keep their 4.3 signatures and return the updated entity, as before.
    def _assign_to_customer(self, customer_id: CustomerId, entity_type: str, entity_id: EntityId):
        self.owner_controller.change_owner_to_customer(owner_id=self.get_id(customer_id), entity_type=entity_type,
                                                       entity_id=self.get_id(entity_id))

    def _unassign_from_customer(self, entity_type: str, entity_id: EntityId):
        tenant_id = self.get_user().tenant_id
        self.owner_controller.change_owner_to_tenant(owner_id=self.get_id(tenant_id), entity_type=entity_type,
                                                     entity_id=self.get_id(entity_id))

    def assign_asset_to_customer(self, customer_id: CustomerId, asset_id: AssetId) -> Asset:
        self._assign_to_customer(customer_id, 'ASSET', asset_id)
        return self.get_asset_by_id(asset_id)

    def unassign_asset_from_customer(self, asset_id: AssetId) -> Asset:
        self._unassign_from_customer('ASSET', asset_id)
        return self.get_asset_by_id(asset_id)

    # Edge Controller
    def get_tenant_edge_infos(self, page_size: int, page: int, type: Optional[str] = None,
                              text_search: Optional[str] = None, sort_property: Optional[str] = None,
                              sort_order: Optional[str] = None,
                              include_customers: Optional[bool] = None) -> PageDataEdgeInfo:
        return self.edge_controller.get_all_edge_infos(page_size=page_size, page=page, type=type,
                                                       text_search=text_search, sort_property=sort_property,
                                                       sort_order=sort_order, include_customers=include_customers)

    def get_edge_info_by_id(self, edge_id: EdgeId) -> EdgeInfo:
        edge_id = self.get_id(edge_id)
        return self.edge_controller.get_edge_info_by_id(edge_id=edge_id)

    def get_customer_edge_infos(self, customer_id: CustomerId, page_size: int, page: int, type: Optional[str] = None,
                                text_search: Optional[str] = None,
                                sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                                include_customers: Optional[bool] = None) -> PageDataEdgeInfo:
        customer_id = self.get_id(customer_id)
        return self.edge_controller.get_customer_edge_infos(customer_id=customer_id, page_size=page_size,
                                                            page=page, type=type, text_search=text_search,
                                                            sort_property=sort_property,
                                                            sort_order=sort_order,
                                                            include_customers=include_customers)

    def assign_edge_to_customer(self, customer_id: CustomerId, edge_id: EdgeId) -> Edge:
        self._assign_to_customer(customer_id, 'EDGE', edge_id)
        return self.get_edge_by_id(edge_id)

    def unassign_edge_from_customer(self, edge_id: EdgeId) -> Edge:
        self._unassign_from_customer('EDGE', edge_id)
        return self.get_edge_by_id(edge_id)

    def get_users(self, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None,
                  sort_order: Optional[str] = None) -> PageDataUser:
        return self.user_controller.get_user_users(page_size=page_size, page=page, text_search=text_search,
                                                   sort_property=sort_property, sort_order=sort_order)

    def unassign_device_from_customer(self, device_id: DeviceId) -> Device:
        self._unassign_from_customer('DEVICE', device_id)
        return self.get_device_by_id(device_id)

    def get_tenant_device_infos(self, page_size: int, page: int, include_customers: Optional[bool] = None,
                                device_profile_id: Optional[DeviceProfileId] = None, active: Optional[bool] = None,
                                text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                sort_order: Optional[str] = None) -> PageDataDeviceInfo:
        device_profile_id = self.get_id(device_profile_id)
        return self.device_controller.get_all_device_infos(page_size=page_size, page=page,
                                                           include_customers=include_customers,
                                                           device_profile_id=device_profile_id, active=active,
                                                           text_search=text_search, sort_property=sort_property,
                                                           sort_order=sort_order)

    def assign_device_to_customer(self, customer_id: CustomerId, device_id: DeviceId) -> Device:
        self._assign_to_customer(customer_id, 'DEVICE', device_id)
        return self.get_device_by_id(device_id)

    def assign_entity_view_to_customer(self, customer_id: CustomerId, entity_view_id: EntityViewId) -> EntityView:
        self._assign_to_customer(customer_id, 'ENTITY_VIEW', entity_view_id)
        return self.get_entity_view_by_id(entity_view_id)

    def get_tenant_entity_view_infos(self, page_size: int, page: int, type: Optional[str] = None,
                                     text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                     sort_order: Optional[str] = None,
                                     include_customers: Optional[bool] = None) -> PageDataEntityViewInfo:
        return self.entity_view_controller.get_all_entity_view_infos(page_size=page_size, page=page, type=type,
                                                                     text_search=text_search,
                                                                     sort_property=sort_property, sort_order=sort_order,
                                                                     include_customers=include_customers)

    def unassign_entity_view_from_customer(self, entity_view_id: EntityViewId) -> EntityView:
        self._unassign_from_customer('ENTITY_VIEW', entity_view_id)
        return self.get_entity_view_by_id(entity_view_id)

    def delete_resource_v1(self, resource_id: EntityId,
                           force: Optional[bool] = None) -> TbResourceDeleteResult:
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.delete_resource(resource_id=resource_id,
                                                           force=force)

    def get_device_profile_infos_by_ids(self, device_profile_ids: list[str]) -> List[DeviceProfileInfo]:
        device_profile_ids = ','.join(device_profile_ids)
        return self.device_profile_controller.get_device_profile_infos_by_ids(device_profile_ids=device_profile_ids)

    # Dashboard Controller
    def assign_dashboard_to_customer(self, customer_id: CustomerId, dashboard_id: DashboardId) -> Dashboard:
        self._assign_to_customer(customer_id, 'DASHBOARD', dashboard_id)
        return self.get_dashboard_by_id(dashboard_id)

    def unassign_dashboard_from_customer(self, customer_id: CustomerId, dashboard_id: DashboardId) -> Dashboard:
        self._unassign_from_customer('DASHBOARD', dashboard_id)
        return self.get_dashboard_by_id(dashboard_id)

    # Self Registration Controller
    def get_privacy_policy(self, pkg_name: Optional[str] = None, platform: Optional[str] = None) -> str:
        return self.self_registration_controller.get_privacy_policy(pkg_name=pkg_name, platform=platform)

    def get_self_registration_params(self, ) -> SelfRegistrationParams:
        return self.self_registration_controller.get_web_self_registration_params()

    def get_sign_up_self_registration_params(self, pkg_name: Optional[str] = None,
                                             platform_type: Optional[str] = None) -> SignUpSelfRegistrationParams:
        return self.self_registration_controller.get_sign_up_self_registration_params(pkg_name=pkg_name,
                                                                                      platform_type=platform_type)

    def get_terms_of_use(self, pkg_name: Optional[str] = None, platform: Optional[str] = None) -> str:
        return self.self_registration_controller.get_terms_of_use(pkg_name=pkg_name, platform=platform)

    def save_self_registration_params(self, body: SelfRegistrationParams) -> WebSelfRegistrationParams:
        return self.self_registration_controller.save_web_self_registration_params(body=body)

    def delete_web_self_registration_params(self) -> None:
        return self.self_registration_controller.delete_web_self_registration_params()

    def get_web_self_registration_params(self) -> SelfRegistrationParams:
        return self.self_registration_controller.get_web_self_registration_params()

    def save_web_self_registration_params(self, body) -> WebSelfRegistrationParams:
        return self.self_registration_controller.save_web_self_registration_params(body=body)

    def get_client_registration_templates(self, ) -> List[OAuth2ClientRegistrationTemplate]:
        return self.o_auth2_config_template_controller.get_o_auth2_client_registration_templates()

    # Asset Controller
    def process_asset_bulk_import(self, body: BulkImportRequest) -> BulkImportResultAsset:
        return self.asset_controller.process_asset_bulk_import(body=body)

    def save_asset(self, body: Asset, entity_group_id: EntityGroupId = None, entity_group_ids: Optional[str] = None,
                   name_conflict_policy: Optional[str] = None, uniquify_separator: Optional[str] = None,
                   uniquify_strategy: Optional[str] = None) -> Asset:
        entity_group_id = self.get_id(entity_group_id)
        if entity_group_ids:
            entity_group_ids = ','.join(entity_group_ids)
        return self.asset_controller.save_asset(body=body, entity_group_id=entity_group_id,
                                                entity_group_ids=entity_group_ids,
                                                name_conflict_policy=name_conflict_policy,
                                                uniquify_separator=uniquify_separator,
                                                uniquify_strategy=uniquify_strategy)

    def get_all_customer_infos(self, page_size: int, page: int, include_customers: Optional[bool] = None,
                               text_search: Optional[str] = None, sort_property: Optional[str] = None,
                               sort_order: Optional[str] = None) -> PageDataCustomerInfo:
        return self.customer_controller.get_all_customer_infos(page_size=page_size, page=page,
                                                               include_customers=include_customers,
                                                               text_search=text_search, sort_property=sort_property,
                                                               sort_order=sort_order)

    def get_customer_customer_infos(self, customer_id: CustomerId, page_size: int, page: int,
                                    include_customers: Optional[bool] = None, text_search: Optional[str] = None,
                                    sort_property: Optional[str] = None,
                                    sort_order: Optional[str] = None) -> PageDataCustomerInfo:
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_customer_customer_infos(customer_id=customer_id, page_size=page_size,
                                                                    page=page, include_customers=include_customers,
                                                                    text_search=text_search,
                                                                    sort_property=sort_property,
                                                                    sort_order=sort_order)

    def get_customer_info_by_id(self, customer_id: CustomerId) -> CustomerInfo:
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_customer_info_by_id(customer_id=customer_id)

    def get_assets_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size: int, page: int,text_search: Optional[str] = None,
                                      sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataAsset:
        entity_group_id = self.get_id(entity_group_id)
        return self.asset_controller.get_assets_by_entity_group_id(entity_group_id=entity_group_id,
                                                                   page_size=page_size, page=page,
                                                                   text_search=text_search,
                                                                   sort_property=sort_property,
                                                                   sort_order=sort_order)

    def get_user_assets(self, page_size: int, page: int, type: Optional[str] = None,text_search: Optional[str] = None, sort_property: Optional[str] = None,
                        sort_order: Optional[str] = None, asset_profile_id: Optional[AssetProfileId] = None) -> PageDataAsset:
        if asset_profile_id:
            asset_profile_id = self.get_id(asset_profile_id)
        return self.asset_controller.get_user_assets(page_size=page_size, page=page, type=type,
                                                     text_search=text_search, sort_property=sort_property,
                                                     sort_order=sort_order, asset_profile_id=asset_profile_id)

    def delete_device_group_ota_package(self, id: str) -> None:
        return self.device_group_ota_package_controller.delete_device_group_ota_package(id=id)

    def get_firmware_by_id(self, group_id: EntityGroupId, firmware_type: str) -> DeviceGroupOtaPackage:
        group_id = self.get_id(group_id)
        return self.device_group_ota_package_controller.get_firmware_by_id(group_id=group_id,
                                                                           firmware_type=firmware_type)

    def save_device_group_ota_package(self, body: DeviceGroupOtaPackage) -> DeviceGroupOtaPackage:
        return self.device_group_ota_package_controller.save_device_group_ota_package(body=body)

    def check_instance(self, body: Union[dict, str, list, bytes, None, RESTResponse, tuple, Any]) -> Union[
            dict, str, list, bytes, None, RESTResponse, tuple, Any]:
        return self.edge_controller.check_instance(body=body)

    def activate_instance(self, license_secret: str, release_date: str) -> Union[
            dict, str, list, bytes, None, RESTResponse, tuple, Any]:
        return self.edge_controller.activate_instance(license_secret=license_secret,
                                                      release_date=release_date)

    def get_user_edges(self, page_size: int, page: int, type: Optional[str] = None,text_search: Optional[str] = None, sort_property: Optional[str] = None,
                       sort_order: Optional[str] = None) -> PageDataEdge:
        return self.edge_controller.get_user_edges(page_size=page_size, page=page, type=type,
                                                   text_search=text_search, sort_property=sort_property,
                                                   sort_order=sort_order)

    def save_edge(self, body: Edge, entity_group_id: Optional[str] = None,
                  entity_group_ids: Optional[List[str]] = None) -> Edge:
        return self.edge_controller.save_edge(body=body, entity_group_id=entity_group_id,
                                              entity_group_ids=entity_group_ids)

    def get_allowed_permissions(self, ) -> AllowedPermissionsInfo:
        return self.user_permissions_controller.get_allowed_permissions()

    def has_entity_permission(self, entity_id: EntityId, operation: str) -> bool:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.user_permissions_controller.has_entity_permission(entity_id=entity_id, entity_type=entity_type,
                                                                      operation=operation)

    def change_owner_to_customer(self, owner_id: UserId, entity_id: EntityId, body: Optional[List[str]] = None) -> None:
        owner_id = self.get_id(owner_id)
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        if body:
            body = ','.join(body)
        return self.owner_controller.change_owner_to_customer(owner_id=owner_id, entity_type=entity_type,
                                                              entity_id=entity_id, body=body)

    def change_owner_to_tenant(self, owner_id: UserId, entity_id: EntityId, body: Optional[List[str]] = None) -> None:
        owner_id = self.get_id(owner_id)
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        if body:
            body = ','.join(body)
        return self.owner_controller.change_owner_to_tenant(owner_id=owner_id, entity_type=entity_type,
                                                            entity_id=entity_id, body=body)

    def rpc_v2_get_persisted_rpc(self, rpc_id: RpcId) -> Rpc:
        rpc_id = self.get_id(rpc_id)
        return self.rpc_v2_controller.get_persisted_rpc(rpc_id=rpc_id)

    def get_user_customers(self, page_size: int, page: int,text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataCustomer:
        return self.customer_controller.get_user_customers(page_size=page_size, page=page,
                                                           text_search=text_search,
                                                           sort_property=sort_property, sort_order=sort_order)

    def get_customers_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size: int, page: int,
                                        text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataCustomer:
        entity_group_id = self.get_id(entity_group_id)
        return self.customer_controller.get_customers_by_entity_group_id(entity_group_id=entity_group_id,
                                                                         page_size=page_size, page=page,
                                                                         text_search=text_search,
                                                                         sort_property=sort_property,
                                                                         sort_order=sort_order)

    def save_customer(self, body: Customer, entity_group_id: Optional[EntityGroupId] = None,
                      entity_group_ids: Optional[List[str]] = None, name_conflict_policy: Optional[str] = None,
                      uniquify_separator: Optional[str] = None, uniquify_strategy: Optional[str] = None) -> Customer:
        if entity_group_id:
            entity_group_id = self.get_id(entity_group_id)
        if entity_group_ids:
            entity_group_ids = ','.join(entity_group_ids)
        return self.customer_controller.save_customer(body=body, entity_group_id=entity_group_id,
                                                      entity_group_ids=entity_group_ids,
                                                      name_conflict_policy=name_conflict_policy,
                                                      uniquify_separator=uniquify_separator,
                                                      uniquify_strategy=uniquify_strategy)

    def get_user_users(self, page_size: int, page: int,text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataUser:
        return self.user_controller.get_user_users(page_size=page_size, page=page, text_search=text_search,
                                                   sort_property=sort_property, sort_order=sort_order)

    def get_all_customer_users(self, page_size: int, page: int,text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataUser:
        return self.user_controller.get_all_customer_users(page_size=page_size, page=page,
                                                           text_search=text_search,
                                                           sort_property=sort_property, sort_order=sort_order)

    def save_user(self, body: User, send_activation_mail: Optional[bool] = None,
                  entity_group_id: Optional[EntityGroupId] = None,
                  entity_group_ids: Optional[List[str]] = None) -> User:
        if entity_group_id:
            entity_group_id = self.get_id(entity_group_id)
        if entity_group_ids:
            entity_group_ids = ','.join(entity_group_ids)
        return self.user_controller.save_user(body=body, send_activation_mail=send_activation_mail,
                                              entity_group_id=entity_group_id, entity_group_ids=entity_group_ids)

    def get_users_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size: int, page: int,text_search: Optional[str] = None,
                                     sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataUser:
        entity_group_id = self.get_id(entity_group_id)
        return self.user_controller.get_users_by_entity_group_id(entity_group_id=entity_group_id,
                                                                 page_size=page_size, page=page,
                                                                 text_search=text_search,
                                                                 sort_property=sort_property,
                                                                 sort_order=sort_order)

    def delete_group_permission(self, group_permission_id: GroupPermissionId) -> None:
        group_permission_id = self.get_id(group_permission_id)
        return self.group_permission_controller.delete_group_permission(
            group_permission_id=group_permission_id)

    def get_entity_group_permissions(self, entity_group_id: EntityGroupId) -> List[GroupPermissionInfo]:
        entity_group_id = self.get_id(entity_group_id)
        return self.group_permission_controller.get_entity_group_permissions(entity_group_id=entity_group_id)

    def get_group_permission_by_id(self, group_permission_id: GroupPermissionId) -> GroupPermission:
        group_permission_id = self.get_id(group_permission_id)
        return self.group_permission_controller.get_group_permission_by_id(
            group_permission_id=group_permission_id)

    def get_group_permission_info_by_id(self, group_permission_id: GroupPermissionId,
                                        is_user_group: bool) -> GroupPermissionInfo:
        group_permission_id = self.get_id(group_permission_id)
        return self.group_permission_controller.get_group_permission_info_by_id(
            group_permission_id=group_permission_id, is_user_group=is_user_group)

    def get_user_group_permissions(self, user_group_id: EntityId) -> List[GroupPermissionInfo]:
        user_group_id = self.get_id(user_group_id)
        return self.group_permission_controller.get_user_group_permissions(user_group_id=user_group_id)

    def load_user_group_permission_infos(self, body: List[GroupPermission]) -> List[GroupPermissionInfo]:
        return self.group_permission_controller.load_user_group_permission_infos(body=body)

    def save_group_permission(self, body: GroupPermission) -> GroupPermission:
        return self.group_permission_controller.save_group_permission(body=body)

    def get_devices_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size: int, page: int,
                                      text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                       sort_order: Optional[str] = None,) -> PageDataDevice:
        entity_group_id = self.get_id(entity_group_id)
        return self.device_controller.get_devices_by_entity_group_id(entity_group_id=entity_group_id,
                                                                     page_size=page_size, page=page,
                                                                     text_search=text_search,
                                                                     sort_property=sort_property,
                                                                     sort_order=sort_order)

    def get_user_devices(self, page_size: int, page: int, type: Optional[str] = None,text_search: Optional[str] = None,
                         sort_property: Optional[str] = None,
                         sort_order: Optional[str] = None,) -> PageDataDevice:
        return self.device_controller.get_user_devices(page_size=page_size, page=page, type=type,
                                                       text_search=text_search, sort_property=sort_property,
                                                       sort_order=sort_order)

    def save_device(self, body: Optional[Device], access_token: Optional[str] = None,
                    entity_group_id: Optional[str] = None, entity_group_ids: Optional[List[str]] = None,
                    name_conflict_policy: Optional[str] = None, uniquify_separator: Optional[str] = None,
                    uniquify_strategy: Optional[str] = None) -> Device:
        return self.device_controller.save_device(body=body, access_token=access_token, entity_group_id=entity_group_id,
                                                  entity_group_ids=entity_group_ids,
                                                  name_conflict_policy=name_conflict_policy,
                                                  uniquify_separator=uniquify_separator,
                                                  uniquify_strategy=uniquify_strategy)

    def count_by_device_group_and_empty_ota_package(self, ota_package_type: str, ota_package_id: OtaPackageId,
                                                    entity_group_id: EntityGroupId) -> int:
        ota_package_id = self.get_id(ota_package_id)
        entity_group_id = self.get_id(entity_group_id)
        return self.device_controller.count_by_device_group_and_empty_ota_package(
            ota_package_type=ota_package_type, ota_package_id=ota_package_id, entity_group_id=entity_group_id)

    def delete_converter(self, converter_id: ConverterId) -> None:
        converter_id = self.get_id(converter_id)
        return self.converter_controller.delete_converter(converter_id=converter_id)

    def get_converter_by_id(self, converter_id: ConverterId) -> Converter:
        converter_id = self.get_id(converter_id)
        return self.converter_controller.get_converter_by_id(converter_id=converter_id)

    def get_converters_by_ids(self, converter_ids: list) -> List[Converter]:
        converter_ids = ','.join(converter_ids)
        return self.converter_controller.get_converters_by_ids(converter_ids=converter_ids)

    def get_converters(self, page_size: int, page: int, is_edge_template: Optional[bool] = None,
                       text_search: Optional[str] = None, sort_property: Optional[str] = None,
                       sort_order: Optional[str] = None,
                       integration_type: Optional[str] = None) -> PageDataConverter:
        return self.converter_controller.get_converters(page_size=page_size, page=page,
                                                        is_edge_template=is_edge_template,
                                                        text_search=text_search, sort_property=sort_property,
                                                        sort_order=sort_order,
                                                        integration_type=integration_type)

    def get_latest_converter_debug_input(
            self, converter_id: ConverterId, integration: Optional[Integration] = None,
            converter_type: Optional[str] = None,
            converter_version: Optional[int] = None) -> Union[dict, str, list, bytes, None, RESTResponse, tuple, Any]:
        converter_id = self.get_id(converter_id)
        integration_type = None
        integration_name = None
        if integration:
            integration_type = self.get_type(integration)
            integration_name = self.get_id(integration)
        return self.converter_controller.get_latest_converter_debug_input(converter_id=converter_id,
                                                                          integration_type=integration_type,
                                                                          integration_name=integration_name,
                                                                          converter_type=converter_type,
                                                                          converter_version=converter_version)

    def assign_integration_to_edge(self, edge_id: EdgeId, integration_id: IntegrationId) -> Integration:
        edge_id = self.get_id(edge_id)
        integration_id = self.get_id(integration_id)
        return self.integration_controller.assign_integration_to_edge(edge_id=edge_id,
                                                                      integration_id=integration_id)

    def unassign_integration_from_edge(self, edge_id: EdgeId, integration_id: IntegrationId) -> Integration:
        edge_id = self.get_id(edge_id)
        integration_id = self.get_id(integration_id)
        return self.integration_controller.unassign_integration_from_edge(edge_id=edge_id,
                                                                          integration_id=integration_id)

    def get_edge_integrations(self, edge_id: EdgeId, page_size: int, page: int, text_search: Optional[str] = None,
                              sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataIntegration:
        edge_id = self.get_id(edge_id)
        return self.integration_controller.get_edge_integrations(edge_id=edge_id, page_size=page_size,
                                                                 page=page, text_search=text_search,
                                                                 sort_property=sort_property,
                                                                 sort_order=sort_order)

    def find_all_related_edges_missing_attributes(self, integration_id: IntegrationId) -> Any:
        integration_id = self.get_id(integration_id)
        return self.integration_controller.find_all_related_edges_missing_attributes(
            integration_id=integration_id)

    def get_edge_integration_infos(self, edge_id: EdgeId, page_size: int, page: int, text_search: Optional[str] = None,
                                   sort_property: Optional[str] = None,
                                   sort_order: Optional[str] = None, ) -> PageDataIntegrationInfo:
        edge_id = self.get_id(edge_id)
        return self.integration_controller.get_edge_integration_infos(edge_id=edge_id, page_size=page_size,
                                                                      page=page, text_search=text_search,
                                                                      sort_property=sort_property,
                                                                      sort_order=sort_order)

    def find_edge_missing_attributes_get(self, edge_id: EdgeId, integration_ids: str) -> Any:
        edge_id = self.get_id(edge_id)
        return self.integration_controller.find_edge_missing_attributes(edge_id=edge_id,
                                                                        integration_ids=integration_ids)

    def get_integrations_converters_info(self) -> Dict[str, IntegrationConvertersInfo]:
        return self.integration_controller.get_integrations_converters_info()

    def save_converter(self, body: Converter) -> Converter:
        return self.converter_controller.save_converter(body=body)

    def test_down_link_converter(self, body: Union[dict, str, list, bytes, None, RESTResponse, tuple, Any],
                                 script_lang: Optional[str] = None) -> Union[
            dict, str, list, bytes, None, RESTResponse, tuple, Any]:
        return self.converter_controller.test_down_link_converter(body=body, script_lang=script_lang)

    def test_up_link_converter(self, body: Union[dict, str, list, bytes, None, RESTResponse, tuple, Any],
                               script_lang: Optional[str] = None) -> Union[
            dict, str, list, bytes, None, RESTResponse, tuple, Any]:
        return self.converter_controller.test_up_link_converter(body=body, script_lang=script_lang)

    def get_user_entity_views(self, page_size: int, page: int, type: Optional[str] = None,
                              text_search: Optional[str] = None, sort_property: Optional[str] = None,
                              sort_order: Optional[str] = None,) -> PageDataEntityView:
        return self.entity_view_controller.get_user_entity_views(page_size=page_size, page=page, type=type,
                                                                 text_search=text_search,
                                                                 sort_property=sort_property,
                                                                 sort_order=sort_order)

    def get_entity_views_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size: int, page: int,
                                           text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                            sort_order: Optional[str] = None,) -> PageDataEntityView:
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_view_controller.get_entity_views_by_entity_group_id(
            entity_group_id=entity_group_id, page_size=page_size, page=page, text_search=text_search,
            sort_property=sort_property, sort_order=sort_order)

    def save_entity_view(self, body: EntityView, entity_group_id: Optional[EntityGroupId] = None,
                         entity_group_ids: Optional[List[str]] = None, name_conflict_policy: Optional[str] = None,
                         uniquify_separator: Optional[str] = None,
                         uniquify_strategy: Optional[str] = None) -> EntityView:
        if entity_group_id:
            entity_group_id = self.get_id(entity_group_id)
        if entity_group_ids:
            entity_group_ids = ','.join(entity_group_ids)
        return self.entity_view_controller.save_entity_view(body=body, entity_group_id=entity_group_id,
                                                            entity_group_ids=entity_group_ids,
                                                            name_conflict_policy=name_conflict_policy,
                                                            uniquify_separator=uniquify_separator,
                                                            uniquify_strategy=uniquify_strategy)

    def get_admin_settings(self, key: str, system_by_default=None) -> AdminSettings:
        return self.admin_controller.get_admin_settings(key=key, system_by_default=system_by_default)

    def sign_up(self, body: SignUpRequest) -> str:
        return self.sign_up_controller.sign_up(body=body)

    def resend_email_activation(self, email: str, pkg_name: Optional[str] = None,
                                platform: Optional[str] = None) -> None:
        return self.sign_up_controller.resend_email_activation(email=email, pkg_name=pkg_name,
                                                               platform=platform)

    def activate_user_by_email_code(self, email_code: str, pkg_name: Optional[str] = None,
                                    platform: Optional[str] = None) -> JwtPair:
        return self.sign_up_controller.activate_user_by_email_code(email_code=email_code, pkg_name=pkg_name,
                                                                   platform=platform)

    def privacy_policy_accepted(self, ) -> bool:
        return self.sign_up_controller.privacy_policy_accepted()

    def accept_terms_of_use(self, ) -> Union[
            dict, str, list, bytes, None, RESTResponse, tuple, Any]:
        return self.sign_up_controller.accept_terms_of_use()

    def activate_email(self, email_code: str, pkg_name: Optional[str] = None,
                       platform: Optional[str] = None) -> str:
        return self.sign_up_controller.activate_email(email_code=email_code, pkg_name=pkg_name,
                                                      platform=platform)

    def mobile_login(self, pkg_name: str, platform: str) -> str:
        return self.sign_up_controller.mobile_login(pkg_name=pkg_name, platform=platform)

    def terms_of_use_accepted(self, ) -> bool:
        return self.sign_up_controller.terms_of_use_accepted()

    def get_device_profiles_by_ids(self, device_profile_ids: list) -> List[DeviceProfileInfo]:
        device_profile_ids = ','.join(device_profile_ids)
        return self.device_profile_controller.get_device_profile_infos_by_ids(
            device_profile_ids=device_profile_ids)

    def assign_scheduler_event_to_edge(self, edge_id: EdgeId, scheduler_event_id: SchedulerEventId) -> SchedulerEventInfo:
        edge_id = self.get_id(edge_id)
        scheduler_event_id = self.get_id(scheduler_event_id)
        return self.scheduler_event_controller.assign_scheduler_event_to_edge(edge_id=edge_id,
                                                                              scheduler_event_id=scheduler_event_id)

    def delete_scheduler_event(self, scheduler_event_id: SchedulerEventId) -> None:
        scheduler_event_id = self.get_id(scheduler_event_id)
        return self.scheduler_event_controller.delete_scheduler_event(
            scheduler_event_id=scheduler_event_id)

    def get_all_scheduler_events(self, edge_id: EdgeId) -> List[SchedulerEventInfo]:
        edge_id = self.get_id(edge_id)
        return self.scheduler_event_controller.get_all_edge_scheduler_events(edge_id=edge_id)

    def get_edge_scheduler_events(self, edge_id: EdgeId, page_size: int, page: int,text_search: Optional[str] = None,
                                  sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataSchedulerEventInfo:
        edge_id = self.get_id(edge_id)
        return self.scheduler_event_controller.get_edge_scheduler_events(edge_id=edge_id, page_size=page_size,
                                                                         page=page, text_search=text_search,
                                                                         sort_property=sort_property,
                                                                         sort_order=sort_order)

    def get_scheduler_event_by_id(self, scheduler_event_id: SchedulerEventId) -> SchedulerEvent:
        scheduler_event_id = self.get_id(scheduler_event_id)
        return self.scheduler_event_controller.get_scheduler_event_by_id(
            scheduler_event_id=scheduler_event_id)

    def get_scheduler_event_info_by_id(self, scheduler_event_id: SchedulerEventId) -> SchedulerEventWithCustomerInfo:
        scheduler_event_id = self.get_id(scheduler_event_id)
        return self.scheduler_event_controller.get_scheduler_event_info_by_id(
            scheduler_event_id=scheduler_event_id)

    def get_scheduler_events_by_ids(self, scheduler_event_ids: list) -> List[SchedulerEventInfo]:
        return self.scheduler_event_controller.get_scheduler_events_by_ids(
            scheduler_event_ids=','.join(scheduler_event_ids))

    def get_scheduler_events(self, page_size: int, page: int, text_search: Optional[str] = None,
                             sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                             type: Optional[str] = None,
                             edge_id: Optional[EdgeId] = None) -> PageDataSchedulerEventWithCustomerInfo:
        edge_id = self.get_id(edge_id)
        return self.scheduler_event_controller.get_scheduler_events(page_size=page_size, page=page,
                                                                    text_search=text_search,
                                                                    sort_property=sort_property,
                                                                    sort_order=sort_order, type=type, edge_id=edge_id)

    def save_scheduler_event(self, body: SchedulerEvent) -> SchedulerEvent:
        return self.scheduler_event_controller.save_scheduler_event(body=body)

    def unassign_scheduler_event_from_edge(self, edge_id: EdgeId, scheduler_event_id: SchedulerEventId) -> SchedulerEventInfo:
        edge_id = self.get_id(edge_id)
        scheduler_event_id = self.get_id(scheduler_event_id)
        return self.scheduler_event_controller.unassign_scheduler_event_from_edge(edge_id=edge_id,
                                                                                  scheduler_event_id=scheduler_event_id)

    def get_all_edge_scheduler_events(self, edge_id: EdgeId) -> List[SchedulerEventInfo]:
        edge_id = self.get_id(edge_id)
        return self.scheduler_event_controller.get_all_edge_scheduler_events(edge_id=edge_id)

    def get_scheduled_report_events(self, page_size: int, page: int,
                                    report_template_id: Optional[ReportTemplateId] = None,
                                    user_id: Optional[UserId] = None, include_customers: Optional[bool] = None,
                                    text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                    sort_order: Optional[str] = None) -> PageDataScheduledReportInfo:
        if report_template_id is not None:
            report_template_id = self.get_id(report_template_id)

        if user_id is not None:
            user_id = self.get_id(user_id)

        return self.scheduler_event_controller.get_scheduled_report_events(page_size=page_size, page=page,
                                                                           report_template_id=report_template_id,
                                                                           user_id=user_id,
                                                                           include_customers=include_customers,
                                                                           text_search=text_search,
                                                                           sort_property=sort_property,
                                                                           sort_order=sort_order)

    def download_dashboard_report(self, dashboard_id: DashboardId,
                                  body: Union[dict, str, list, bytes, None, RESTResponse, tuple, Any]) -> bytes:
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_report_controller.download_dashboard_report(dashboard_id=dashboard_id, body=body)

    def download_test_report(self, body: Optional[DashboardReportConfig],
                             reports_server_endpoint_url: Optional[str] = None) -> bytes:
        return self.dashboard_report_controller.download_test_report(
            body=body, reports_server_endpoint_url=reports_server_endpoint_url)

    def get_dashboards_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size: int, page: int,
                                         text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataDashboardInfo:
        entity_group_id = self.get_id(entity_group_id)
        return self.dashboard_controller.get_dashboards_by_entity_group_id(entity_group_id=entity_group_id,
                                                                           page_size=page_size, page=page,
                                                                           text_search=text_search,
                                                                           sort_property=sort_property,
                                                                           sort_order=sort_order)

    def save_dashboard(self, body: Dashboard, accept_encoding: Optional[str] = None,
                       entity_group_id: Optional[str] = None,
                       entity_group_ids: Optional[List[str]] = None) -> Dashboard:
        return self.dashboard_controller.save_dashboard(body=body, accept_encoding=accept_encoding,
                                                        entity_group_id=entity_group_id,
                                                        entity_group_ids=entity_group_ids)

    def set_customer_home_dashboard_info(self, body: HomeDashboardInfo) -> None:
        return self.dashboard_controller.set_customer_home_dashboard_info(body=body)

    def get_dashboards_by_ids(self, dashboard_ids: list) -> List[DashboardInfo]:
        dashboard_ids = ','.join(dashboard_ids)
        return self.dashboard_controller.get_dashboards_by_ids(dashboard_ids=dashboard_ids)

    def get_customer_home_dashboard_info(self, ) -> HomeDashboardInfo:
        return self.dashboard_controller.get_customer_home_dashboard_info()

    def get_user_dashboards(self, page_size: int, page: int, mobile: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None,
                            sort_order: Optional[str] = None, operation: Optional[str] = None, user_id: Optional[str] = None) -> PageDataDashboardInfo:
        user_id = self.get_id(user_id)
        return self.dashboard_controller.get_user_dashboards(page_size=page_size, page=page, mobile=mobile,
                                                             text_search=text_search,
                                                             sort_property=sort_property,
                                                             sort_order=sort_order, operation=operation,
                                                             user_id=user_id)

    def import_group_dashboards(self, entity_group_id: EntityGroupId, body: List[Dashboard],
                                overwrite: Optional[bool] = None) -> None:
        entity_group_id = self.get_id(entity_group_id)
        return self.dashboard_controller.import_group_dashboards(entity_group_id=entity_group_id, body=body,
                                                                 overwrite=overwrite)

    def export_group_dashboards(self, entity_group_id: EntityGroupId, limit: int,
                                accept_encoding: Optional[str] = None) -> List[Dashboard]:
        entity_group_id = self.get_id(entity_group_id)
        return self.dashboard_controller.export_group_dashboards(entity_group_id=entity_group_id, limit=limit,
                                                                 accept_encoding=accept_encoding)

    def check_integration_connection(self, body: Integration) -> None:
        return self.integration_controller.check_integration_connection(body=body)

    def delete_integration(self, integration_id: IntegrationId) -> None:
        integration_id = self.get_id(integration_id)
        return self.integration_controller.delete_integration(integration_id=integration_id)

    def get_integration_by_id(self, integration_id: IntegrationId) -> Integration:
        integration_id = self.get_id(integration_id)
        return self.integration_controller.get_integration_by_id(integration_id=integration_id)

    def get_integration_by_routing_key(self, routing_key: str) -> Integration:
        return self.integration_controller.get_integration_by_routing_key(routing_key=routing_key)

    def get_integrations_by_ids(self, integration_ids: list) -> List[Integration]:
        integration_ids = ','.join(integration_ids)
        return self.integration_controller.get_integrations_by_ids(integration_ids=integration_ids)

    def get_integration_infos(self, page_size: int, page: int, is_edge_template: Optional[bool] = None,
                              text_search: Optional[str] = None, sort_property: Optional[str] = None,
                              sort_order: Optional[str] = None) -> PageDataIntegrationInfo:
        return self.integration_controller.get_integration_infos(page_size=page_size, page=page,
                                                                 is_edge_template=is_edge_template,
                                                                 text_search=text_search,
                                                                 sort_property=sort_property,
                                                                 sort_order=sort_order)

    def get_integrations(self, page_size: int, page: int, is_edge_template: Optional[bool] = None,
                         text_search: Optional[str] = None, sort_property: Optional[str] = None,
                         sort_order: Optional[str] = None) -> PageDataIntegration:
        return self.integration_controller.get_integrations(page_size=page_size, page=page,
                                                            is_edge_template=is_edge_template,
                                                            text_search=text_search,
                                                            sort_property=sort_property,
                                                            sort_order=sort_order)

    def save_integration(self, body: Integration) -> Integration:
        return self.integration_controller.save_integration(body=body)

    def get_custom_menu(self, if_none_match: Optional[str] = None) -> CustomMenuConfig:
        return self.custom_menu_controller.get_custom_menu(if_none_match=if_none_match)

    def create_custom_menu(self, body: CustomMenuInfo, assign_to_list: Optional[List[str]] = None,
                           force: Optional[bool] = None) -> CustomMenu:
        if assign_to_list is not None:
            assign_to_list = '.'.join(assign_to_list)

        return self.custom_menu_controller.create_custom_menu(body=body, assign_to_list=assign_to_list, force=force)

    def delete_custom_menu(self, custom_menu_id: CustomMenuId, force: Optional[bool] = None) -> CustomMenuDeleteResult:
        custom_menu_id = self.get_id(custom_menu_id)
        return self.custom_menu_controller.delete_custom_menu(custom_menu_id=custom_menu_id, force=force)

    def get_custom_menu_assignee_list(self, custom_menu_id: CustomMenuId) -> List[EntityInfo]:
        custom_menu_id = self.get_id(custom_menu_id)
        return self.custom_menu_controller.get_custom_menu_assignee_list(custom_menu_id=custom_menu_id)

    def get_custom_menu_config(self, custom_menu_id: CustomMenuId) -> CustomMenuConfig:
        custom_menu_id = self.get_id(custom_menu_id)
        return self.custom_menu_controller.get_custom_menu_config(custom_menu_id=custom_menu_id)

    def get_custom_menu_info_by_id(self, custom_menu_id: CustomMenuId) -> CustomMenuInfo:
        custom_menu_id = self.get_id(custom_menu_id)
        return self.custom_menu_controller.get_custom_menu_info_by_id(custom_menu_id=custom_menu_id)

    def get_custom_menu_infos(self, page_size: int, page: int, scope: Optional[str] = None,
                              assignee_type: Optional[str] = None, text_search: Optional[str] = None,
                              sort_property: Optional[str] = None,
                              sort_order: Optional[str] = None) -> PageDataCustomMenuInfo:
        return self.custom_menu_controller.get_custom_menu_infos(page_size=page_size, page=page, scope=scope,
                                                                 assignee_type=assignee_type, text_search=text_search,
                                                                 sort_property=sort_property, sort_order=sort_order)

    def update_custom_menu_assignee_list(self, id: CustomMenuId, assignee_type: str, body: Optional[List[str]] = None,
                                         force: Optional[bool] = None) -> None:
        id = self.get_id(id)
        return self.custom_menu_controller.update_custom_menu_assignee_list(id=id, assignee_type=assignee_type,
                                                                            body=body, force=force)

    def update_custom_menu_config(self, id: CustomMenuId, body: CustomMenuConfig) -> CustomMenu:
        id = self.get_id(id)
        return self.custom_menu_controller.update_custom_menu_config(custom_menu_id=id, body=body)

    def update_custom_menu_name(self, id: CustomMenuId, body: str) -> None:
        id = self.get_id(id)
        return self.custom_menu_controller.update_custom_menu_name(custom_menu_id=id, body=body)

    def get_custom_translation(self, locale_code: str) -> JsonNode:
        return self.custom_translation_controller.get_custom_translation(locale_code=locale_code)

    def save_custom_translation(self, locale_code: str, body: object) -> None:
        return self.custom_translation_controller.save_custom_translation(body=body, locale_code=locale_code)

    def delete_custom_translation(self, locale_code: str) -> None:
        return self.custom_translation_controller.delete_custom_translation(locale_code=locale_code)

    def delete_custom_translation_key(self, locale_code: str, key_path: str) -> None:
        return self.custom_translation_controller.delete_custom_translation_key(locale_code=locale_code,
                                                                                key_path=key_path)

    def patch_custom_translation(self, body: object, locale_code: str) -> None:
        return self.custom_translation_controller.patch_custom_translation(body=body, locale_code=locale_code)

    def upload_custom_translation(self, locale_code: str, file) -> None:
        return self.custom_translation_controller.upload_custom_translation(locale_code=locale_code, file=file)

    def get_merged_custom_translation(self, locale_code: str) -> JsonNode:
        return self.custom_translation_controller.get_merged_custom_translation(locale_code=locale_code)

    def delete_role(self, role_id: RoleId) -> None:
        role_id = self.get_id(role_id)
        return self.role_controller.delete_role(role_id=role_id)

    def get_role_by_id(self, role_id: RoleId) -> Role:
        role_id = self.get_id(role_id)
        return self.role_controller.get_role_by_id(role_id=role_id)

    def get_roles_by_ids(self, role_ids: list) -> List[Role]:
        role_ids = ','.join(role_ids)
        return self.role_controller.get_roles_by_ids(role_ids=role_ids)

    def get_roles(self, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None,
                  sort_property: Optional[str] = None, sort_order: Optional[str] = None, ) -> PageDataRole:
        return self.role_controller.get_roles(page_size=page_size, page=page, type=type,
                                              text_search=text_search, sort_property=sort_property,
                                              sort_order=sort_order)

    def save_role(self, body: Role) -> Role:
        return self.role_controller.save_role(body=body)

    def delete_blob_entity(self, blob_entity_id: BlobEntityId) -> None:
        blob_entity_id = self.get_id(blob_entity_id)
        return self.blob_entity_controller.delete_blob_entity(blob_entity_id=blob_entity_id)

    def download_blob_entity(self, blob_entity_id: BlobEntityId) -> bytes:
        blob_entity_id = self.get_id(blob_entity_id)
        return self.blob_entity_controller.download_blob_entity(blob_entity_id=blob_entity_id)

    def get_blob_entities_by_ids(self, blob_entity_ids: list) -> List[BlobEntityInfo]:
        return self.blob_entity_controller.get_blob_entities_by_ids(blob_entity_ids=','.join(blob_entity_ids))

    def get_blob_entities(self, page_size: int, page: int, type: Optional[str] = None,text_search: Optional[str] = None, sort_property: Optional[str] = None,
                          sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None) -> PageDataBlobEntityWithCustomerInfo:
        return self.blob_entity_controller.get_blob_entities(page_size=page_size, page=page, type=type,
                                                             text_search=text_search,
                                                             sort_property=sort_property,
                                                             sort_order=sort_order, start_time=start_time,
                                                             end_time=end_time)

    def get_blob_entity_info_by_id(self, blob_entity_id: BlobEntityId) -> BlobEntityWithCustomerInfo:
        blob_entity_id = self.get_id(blob_entity_id)
        return self.blob_entity_controller.get_blob_entity_info_by_id(blob_entity_id=blob_entity_id)

    def get_current_login_white_label_params(self, customer_id: Optional[str] = None) -> LoginWhiteLabelingParams:
        return self.white_labeling_controller.get_current_login_white_label_params(customer_id=customer_id)

    def get_current_white_label_params(self, customer_id: Optional[str] = None) -> WhiteLabelingParams:
        return self.white_labeling_controller.get_current_white_label_params(customer_id=customer_id)

    def get_login_white_label_params(self) -> LoginWhiteLabelingParams:
        return self.white_labeling_controller.get_login_white_label_params()

    def get_white_label_params(self) -> WhiteLabelingParams:
        return self.white_labeling_controller.get_white_label_params()

    def is_customer_white_labeling_allowed(self, ) -> bool:
        return self.white_labeling_controller.is_customer_white_labeling_allowed()

    def is_white_labeling_allowed(self, ) -> bool:
        return self.white_labeling_controller.is_white_labeling_allowed()

    def preview_white_label_params(self, body: WhiteLabelingParams) -> WhiteLabelingParams:
        return self.white_labeling_controller.preview_white_label_params(body=body)

    def save_login_white_label_params(self, body: LoginWhiteLabelingParams,
                                      customer_id: Optional[str] = None) -> LoginWhiteLabelingParams:
        return self.white_labeling_controller.save_login_white_label_params(body=body, customer_id=customer_id)

    def save_white_label_params(self, body: WhiteLabelingParams,
                                customer_id: Optional[str] = None) -> WhiteLabelingParams:
        return self.white_labeling_controller.save_white_label_params(body=body, customer_id=customer_id)

    def delete_current_login_white_label_params(self, customer_id: Optional[CustomerId] = None) -> None:
        customer_id = self.get_id(customer_id)
        return self.white_labeling_controller.delete_current_login_white_label_params(customer_id=customer_id)

    def delete_current_white_label_params(self, customer_id: Optional[CustomerId] = None) -> None:
        customer_id = self.get_id(customer_id)
        return self.white_labeling_controller.delete_current_white_label_params(customer_id=customer_id)

    def get_group_ota_packages(self, group_id: EntityGroupId, type: str, page_size: int, page: int,text_search: Optional[str] = None,
                               sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataOtaPackageInfo:
        group_id = self.get_id(group_id)
        return self.ota_package_controller.get_group_ota_packages(group_id=group_id, type=type,
                                                                  page_size=page_size, page=page,
                                                                  text_search=text_search,
                                                                  sort_property=sort_property,
                                                                  sort_order=sort_order)

    def add_entities_to_entity_group(self, entity_group_id: EntityGroupId, body: List[str]) -> None:
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.add_entities_to_entity_group(entity_group_id=entity_group_id,
                                                                         body=body)

    def assign_entity_group_to_edge(self, edge_id: EdgeId, group_type: str,
                                    entity_group_id: EntityGroupId) -> EntityGroup:
        edge_id = self.get_id(edge_id)
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.assign_entity_group_to_edge(edge_id=edge_id,
                                                                        group_type=group_type,
                                                                        entity_group_id=entity_group_id)

    def delete_entity_group(self, entity_group_id: EntityGroupId) -> None:
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.delete_entity_group(entity_group_id=entity_group_id)

    def get_all_edge_entity_groups(self, edge_id: EdgeId, group_type: str) -> List[EntityGroupInfo]:
        edge_id = self.get_id(edge_id)
        return self.entity_group_controller.get_all_edge_entity_groups(edge_id=edge_id, group_type=group_type)

    def get_edge_entity_groups(self, edge_id: EdgeId, group_type: str, page_size: int, page: int,
                               sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                               text_search: Optional[str] = None) -> PageDataEntityGroupInfo:
        edge_id = self.get_id(edge_id)
        return self.entity_group_controller.get_edge_entity_groups(edge_id=edge_id, group_type=group_type,
                                                                   page_size=page_size, page=page,
                                                                   sort_property=sort_property, sort_order=sort_order,
                                                                   text_search=text_search)

    def get_entities(self, entity_group_id: EntityGroupId, page_size: int, page: int,text_search: Optional[str] = None,
                     sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataShortEntityView:
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.get_entities(entity_group_id=entity_group_id, page_size=page_size,
                                                         page=page, text_search=text_search,
                                                         sort_property=sort_property, sort_order=sort_order)

    def get_entity_group_all_by_owner_and_type(self, owner_type: str, owner_id: UserId,
                                               group_type: str) -> EntityGroupInfo:
        owner_id = self.get_id(owner_id)
        return self.entity_group_controller.get_entity_group_all_by_owner_and_type(owner_type=owner_type,
                                                                                   owner_id=owner_id,
                                                                                   group_type=group_type)

    def get_entity_groups_by_owner_and_type_and_page_link(self, owner_type: str, owner_id: UserId, group_type: str,
                                                          page_size: int, page: int, text_search: Optional[str] = None,
                                                          sort_property: Optional[str] = None,
                                                          sort_order: Optional[str] = None) -> PageDataEntityGroupInfo:
        owner_id = self.get_id(owner_id)
        return self.entity_group_controller.get_entity_groups_by_owner_and_type_and_page_link(
            owner_type=owner_type,
            owner_id=owner_id,
            group_type=group_type, page_size=page_size,
            page=page, text_search=text_search,
            sort_property=sort_property, sort_order=sort_order)

    def get_entity_group_by_id(self, entity_group_id: EntityGroupId) -> EntityGroupInfo:
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.get_entity_group_by_id(entity_group_id=entity_group_id)

    def get_entity_group_by_owner_and_name_and_type(self, owner_id: UserId, group_type: str,
                                                    group_name: str) -> EntityGroupInfo:
        owner_type = self.get_type(owner_id)
        owner_id = self.get_id(owner_id)
        return self.entity_group_controller.get_entity_group_by_owner_and_name_and_type(owner_type=owner_type,
                                                                                        owner_id=owner_id,
                                                                                        group_type=group_type,
                                                                                        group_name=group_name)

    def get_entity_groups_by_ids(self, entity_group_ids: List[str]) -> List[EntityGroupInfo]:
        entity_group_ids = ','.join(entity_group_ids)
        return self.entity_group_controller.get_entity_groups_by_ids(entity_group_ids=entity_group_ids)

    def get_entity_groups_by_owner_and_type(self, owner_type: str, owner_id: UserId,
                                            group_type: str) -> List[EntityGroupInfo]:
        owner_id = self.get_id(owner_id)
        return self.entity_group_controller.get_all_entity_groups_by_owner_and_type(owner_type=owner_type,
                                                                                    owner_id=owner_id,
                                                                                    group_type=group_type)

    def get_entity_groups_by_type(self, group_type: str,
                                  include_shared: Optional[bool] = None) -> List[EntityGroupInfo]:
        return self.entity_group_controller.get_all_entity_groups_by_type(group_type=group_type, include_shared=include_shared)

    def get_entity_groups_for_entity(self, entity_id: EntityId) -> List[EntityGroupId]:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.entity_group_controller.get_entity_groups_for_entity(entity_type=entity_type,
                                                                         entity_id=entity_id)

    def get_group_entity(self, entity_group_id: EntityGroupId, entity_id: EntityId) -> ShortEntityView:
        entity_group_id = self.get_id(entity_group_id)
        entity_id = self.get_id(entity_id)
        return self.entity_group_controller.get_group_entity(entity_group_id=entity_group_id,
                                                             entity_id=entity_id)

    def get_owners(self, page_size: int, page: int, text_search: Optional[str] = None,
                   sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataContactBasedObject:
        return self.entity_group_controller.get_owners(page_size=page_size, page=page, text_search=text_search,
                                                       sort_property=sort_property, sort_order=sort_order)

    def make_entity_group_private(self, entity_group_id: EntityGroupId) -> None:
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.make_entity_group_private(entity_group_id=entity_group_id)

    def make_entity_group_public(self, entity_group_id: EntityGroupId) -> None:
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.make_entity_group_public(entity_group_id=entity_group_id)

    def remove_entities_from_entity_group(self, entity_group_id: EntityGroupId, body: List[str]) -> None:
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.remove_entities_from_entity_group(
            entity_group_id=entity_group_id, body=body)

    def save_entity_group(self, body: EntityGroup) -> EntityGroupInfo:
        return self.entity_group_controller.save_entity_group(body=body)

    def share_entity_group_to_child_owner_user_group(self, entity_group_id: EntityGroupId, user_group_id: EntityId,
                                                     role_id: RoleId) -> None:
        entity_group_id = self.get_id(entity_group_id)
        user_group_id = self.get_id(user_group_id)
        role_id = self.get_id(role_id)
        return self.entity_group_controller.share_entity_group_to_child_owner_user_group(
            entity_group_id=entity_group_id, user_group_id=user_group_id, role_id=role_id)

    def share_entity_group(self, entity_group_id: EntityGroupId, body: ShareGroupRequest) -> None:
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.share_entity_group(entity_group_id=entity_group_id, body=body)

    def unassign_entity_group_from_edge(self, edge_id: EdgeId,
                                        group_type: str,
                                        entity_group_id: EntityGroupId) -> EntityGroup:
        edge_id = self.get_id(edge_id)
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.unassign_entity_group_from_edge(edge_id=edge_id,
                                                                            group_type=group_type,
                                                                            entity_group_id=entity_group_id)

    # Asset Profile Controller
    def delete_asset_profile(self, asset_profile_id: AssetProfileId) -> None:
        asset_profile_id = self.get_id(asset_profile_id)
        return self.asset_profile_controller.delete_asset_profile(asset_profile_id=asset_profile_id)

    def get_asset_profile_info_by_id(self, asset_profile_id: AssetProfileId) -> AssetProfileInfo:
        asset_profile_id = self.get_id(asset_profile_id)
        return self.asset_profile_controller.get_asset_profile_info_by_id(asset_profile_id=asset_profile_id)

    def get_asset_profile_infos(self, page_size: int, page: int, text_search: Optional[str] = None,
                                sort_property: Optional[str] = None,
                                sort_order: Optional[str] = None) -> PageDataAssetProfileInfo:
        return self.asset_profile_controller.get_asset_profile_infos(page_size=page_size, page=page,
                                                                     text_search=text_search,
                                                                     sort_property=sort_property,
                                                                     sort_order=sort_order)

    def get_asset_profiles(self, page_size: int, page: int, text_search: Optional[str] = None,
                           sort_property: Optional[str] = None,
                           sort_order: Optional[str] = None) -> PageDataAssetProfile:
        return self.asset_profile_controller.get_asset_profiles(page_size=page_size, page=page,
                                                                text_search=text_search,
                                                                sort_property=sort_property,
                                                                sort_order=sort_order)

    def get_default_asset_profile_info(self) -> AssetProfileInfo:
        return self.asset_profile_controller.get_default_asset_profile_info()

    def save_asset_profile(self, body: AssetProfile) -> AssetProfile:
        return self.asset_profile_controller.save_asset_profile(body=body)

    def set_default_asset_profile(self, asset_profile_id: AssetProfileId) -> AssetProfile:
        asset_profile_id = self.get_id(asset_profile_id)
        return self.asset_profile_controller.set_default_asset_profile(asset_profile_id=asset_profile_id)

    def get_features_info(self) -> FeaturesInfo:
        return self.admin_controller.get_features_info()

    def get_license_usage_info(self) -> LicenseUsageInfo:
        return self.admin_controller.get_license_usage_info()

    def get_system_info(self) -> SystemInfo:
        return self.admin_controller.get_system_info()

    def assign_alarm(self, alarm_id: AlarmId, assignee_id: str) -> Alarm:
        alarm_id = self.get_id(alarm_id)
        return self.alarm_controller.assign_alarm(alarm_id=alarm_id, assignee_id=assignee_id)

    def get_all_asset_infos(self, page_size: int, page: int, text_search: Optional[str] = None,
                            sort_property: Optional[str] = None,
                            sort_order: Optional[str] = None, include_customers: Optional[bool] = None,
                            asset_profile_id: Optional[AssetProfileId] = None) -> PageDataAssetInfo:
        asset_profile_id = self.get_id(asset_profile_id)
        return self.asset_controller.get_all_asset_infos(page_size=page_size, page=page,
                                                         text_search=text_search,
                                                         sort_property=sort_property,
                                                         sort_order=sort_order,
                                                         include_customers=include_customers,
                                                         asset_profile_id=asset_profile_id)

    def get_all_dashboards(self, page_size: int, page: int, text_search: Optional[str] = None,
                           sort_property: Optional[str] = None,
                           sort_order: Optional[str] = None,
                           include_customers: Optional[bool] = None) -> PageDataDashboardInfo:
        return self.dashboard_controller.get_all_dashboards(page_size=page_size, page=page,
                                                            text_search=text_search,
                                                            sort_property=sort_property,
                                                            sort_order=sort_order,
                                                            include_customers=include_customers)

    def get_all_device_infos(self, page_size: int, page: int, text_search: Optional[str] = None,
                             sort_property: Optional[str] = None,
                             sort_order: Optional[str] = None,
                             include_customers: Optional[bool] = None,
                             device_profile_id: Optional[DeviceProfileId] = None,
                             active: Optional[bool] = None) -> PageDataDeviceInfo:
        if device_profile_id:
            device_profile_id = self.get_id(device_profile_id)

        return self.device_controller.get_all_device_infos(page_size=page_size, page=page,
                                                           text_search=text_search,
                                                           sort_property=sort_property,
                                                           sort_order=sort_order,
                                                           include_customers=include_customers,
                                                           device_profile_id=device_profile_id,
                                                           active=active)

    def get_customer_device_infos(self, customer_id: CustomerId, page_size: int, page: int,
                                  include_customers: Optional[bool] = None,
                                  device_profile_id: Optional[DeviceProfileId] = None, active: Optional[bool] = None,
                                  text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                  sort_order: Optional[str] = None) -> PageDataDeviceInfo:
        customer_id = self.get_id(customer_id)
        device_profile_id = self.get_id(device_profile_id)
        return self.device_controller.get_customer_device_infos(customer_id=customer_id, page_size=page_size,
                                                                page=page, include_customers=include_customers,
                                                                device_profile_id=device_profile_id, active=active,
                                                                text_search=text_search, sort_property=sort_property,
                                                                sort_order=sort_order)

    def get_entity_group_entity_info_by_id(self, entity_group_id: EntityGroupId) -> EntityInfo:
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.get_entity_group_entity_info_by_id(entity_group_id=entity_group_id)

    def get_entity_group_entity_infos_by_ids(self, entity_group_ids: List[str]) -> List[EntityInfo]:
        entity_group_ids = ','.join(entity_group_ids)
        return self.entity_group_controller.get_entity_group_entity_infos_by_ids(entity_group_ids=entity_group_ids)

    def get_entity_group_entity_infos_by_owner_and_type_and_page_link(self, owner_id: str, owner_type: str,
                                                                      group_type: str, page_size: int, page: int,
                                                                      text_search: Optional[str] = None,
                                                                      sort_property: Optional[str] = None,
                                                                      sort_order: Optional[
                                                                          str] = None) -> PageDataEntityInfo:
        return self.entity_group_controller.get_entity_group_entity_infos_by_owner_and_type_and_page_link(
            owner_id=owner_id, owner_type=owner_type, group_type=group_type, page_size=page_size, page=page,
            text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_entity_group_entity_infos_by_type_and_page_link(
            self, group_type: str, page_size: int, page: int, text_search: Optional[str] = None,
            sort_property: Optional[str] = None, sort_order: Optional[str] = None,
            include_shared: Optional[bool] = None) -> PageDataEntityInfo:
        return self.entity_group_controller.get_entity_group_entity_infos_by_type_and_page_link(
            group_type=group_type, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property,
            sort_order=sort_order, include_shared=include_shared)

    def get_entity_group_entity_infos_hierarchy_by_owner_and_type_and_page_link(self, owner_id: str, owner_type: str,
                                                                                group_type: str, page_size: int,
                                                                                page: int,
                                                                                text_search: Optional[str] = None,
                                                                                sort_property: Optional[str] = None,
                                                                                sort_order: Optional[
                                                                                    str] = None) -> PageDataEntityInfo:
        return self.entity_group_controller.get_entity_group_entity_infos_hierarchy_by_owner_and_type_and_page_link(
            owner_id=owner_id, owner_type=owner_type, group_type=group_type, page_size=page_size, page=page,
            text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_entity_groups_by_type_and_page_link(self, group_type: str, page_size: int, page: int,
                                                text_search: Optional[str] = None,
                                                sort_property: Optional[str] = None,
                                                sort_order: Optional[
                                                    str] = None,
                                                include_shared: Optional[bool] = None) -> PageDataEntityGroupInfo:
        return self.entity_group_controller.get_entity_groups_by_type_and_page_link(group_type=group_type,
                                                                                    page_size=page_size,
                                                                                    page=page,
                                                                                    text_search=text_search,
                                                                                    sort_property=sort_property,
                                                                                    sort_order=sort_order,
                                                                                    include_shared=include_shared)

    def get_entity_groups_hierarchy_by_owner_and_type_and_page_link(self, owner_id: str, owner_type: str,
                                                                    group_type: str, page_size: int,
                                                                    page: int,
                                                                    text_search: Optional[str] = None,
                                                                    sort_property: Optional[str] = None,
                                                                    sort_order: Optional[
                                                                        str] = None) -> PageDataEntityGroupInfo:
        return self.entity_group_controller.get_entity_groups_hierarchy_by_owner_and_type_and_page_link(
            owner_id=owner_id, owner_type=owner_type, group_type=group_type, page_size=page_size, page=page,
            text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_owner_info(self, owner_type: str, owner_id: str) -> EntityInfo:
        return self.entity_group_controller.get_owner_info(owner_type=owner_type, owner_id=owner_id)

    def get_owner_infos(self, page_size: int,
                        page: int,
                        text_search: Optional[str] = None,
                        sort_property: Optional[str] = None,
                        sort_order: Optional[
                            str] = None) -> PageDataEntityInfo:
        return self.entity_group_controller.get_owner_infos(page_size=page_size, page=page,
                                                            text_search=text_search,
                                                            sort_property=sort_property,
                                                            sort_order=sort_order)

    def get_shared_entity_group_entity_infos_by_type_and_page_link(self, group_type: str, page_size: int,
                                                                   page: int,
                                                                   text_search: Optional[str] = None,
                                                                   sort_property: Optional[str] = None,
                                                                   sort_order: Optional[
                                                                       str] = None) -> PageDataEntityInfo:
        return self.entity_group_controller.get_shared_entity_group_entity_infos_by_type_and_page_link(
            group_type=group_type, page_size=page_size, page=page,
            text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_shared_entity_groups_by_type_and_page_link(self, group_type: str, page_size: int,
                                                       page: int,
                                                       text_search: Optional[str] = None,
                                                       sort_property: Optional[str] = None,
                                                       sort_order: Optional[
                                                           str] = None) -> PageDataEntityGroupInfo:
        return self.entity_group_controller.get_shared_entity_groups_by_type_and_page_link(
            group_type=group_type, page_size=page_size, page=page,
            text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_shared_entity_groups_by_type(self, group_type: str) -> List[EntityGroupInfo]:
        return self.entity_group_controller.get_all_shared_entity_groups(group_type=group_type)

    def get_all_entity_view_infos(self, page_size: int,
                                  page: int,
                                  include_customers: Optional[bool] = None,
                                  type: Optional[str] = None,
                                  text_search: Optional[str] = None,
                                  sort_property: Optional[str] = None,
                                  sort_order: Optional[
                                      str] = None) -> PageDataEntityViewInfo:
        return self.entity_view_controller.get_all_entity_view_infos(page_size=page_size, page=page,
                                                                     text_search=text_search,
                                                                     sort_property=sort_property,
                                                                     sort_order=sort_order,
                                                                     include_customers=include_customers,
                                                                     type=type)

    def get_customer_entity_view_infos(self, customer_id: CustomerId, page_size: int, page: int,
                                       type: Optional[str] = None, text_search: Optional[str] = None,
                                       sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                                       include_customers: Optional[bool] = None) -> PageDataEntityViewInfo:
        customer_id = self.get_id(customer_id)
        return self.entity_view_controller.get_customer_entity_view_infos(customer_id=customer_id, page_size=page_size,
                                                                          page=page, type=type, text_search=text_search,
                                                                          sort_property=sort_property,
                                                                          sort_order=sort_order,
                                                                          include_customers=include_customers)

    def get_all_user_infos(self, page_size: int, page: int, include_customers: Optional[bool] = None,
                           text_search: Optional[str] = None, sort_property: Optional[str] = None,
                           sort_order: Optional[str] = None) -> PageDataUserInfo:
        return self.user_controller.get_all_user_infos(page_size=page_size, page=page,
                                                       include_customers=include_customers, text_search=text_search,
                                                       sort_property=sort_property, sort_order=sort_order)

    def get_customer_user_infos(self, customer_id: CustomerId, page_size: int, page: int,
                                text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                sort_order: Optional[str] = None,
                                include_customers: Optional[bool] = None) -> PageDataUserInfo:
        customer_id = self.get_id(customer_id)
        return self.user_controller.get_customer_user_infos(customer_id=customer_id,
                                                            page_size=page_size, page=page,
                                                            text_search=text_search,
                                                            sort_property=sort_property,
                                                            sort_order=sort_order,
                                                            include_customers=include_customers)

    def get_user_info_by_id(self, user_id: UserId) -> UserInfo:
        user_id = self.get_id(user_id)
        return self.user_controller.get_user_info_by_id(user_id=user_id)

    def download_login_favicon(self, type: str, key: str, if_none_match: Optional[str] = None,
                               accept_encoding: Optional[str] = None) -> bytes:
        return self.image_controller.download_login_favicon(type=type, key=key, if_none_match=if_none_match,
                                                            accept_encoding=accept_encoding)

    def download_login_logo(self, type: str, key: str, if_none_match: Optional[str] = None,
                            accept_encoding: Optional[str] = None) -> bytes:
        return self.image_controller.download_login_logo(type=type, key=key, if_none_match=if_none_match,
                                                         accept_encoding=accept_encoding)

    def enable_scheduler_event(self, scheduler_event_id: SchedulerEventId, enabled_value: bool) -> SchedulerEvent:
        scheduler_event_id = self.get_id(scheduler_event_id)
        return self.scheduler_event_controller.enable_scheduler_event(scheduler_event_id=scheduler_event_id,
                                                                      enabled_value=enabled_value)

    def download_full_translation(self, locale_code: str) -> bytes:
        return self.translation_controller.download_full_translation(locale_code=locale_code)

    def get_available_java_locales(self) -> JsonNode:
        return self.translation_controller.get_available_java_locales()

    def get_available_locales(self) -> JsonNode:
        return self.translation_controller.get_available_locales()

    def get_full_translation(self, locale_code: str, if_none_match: Optional[str] = None,
                             accept_encoding: Optional[str] = None) -> JsonNode:
        return self.translation_controller.get_full_translation(locale_code=locale_code, if_none_match=if_none_match,
                                                                accept_encoding=accept_encoding)

    def get_login_page_translation(self, locale_code: str, if_none_match: Optional[str] = None,
                                   accept_encoding: Optional[str] = None) -> JsonNode:
        return self.translation_controller.get_login_page_translation(locale_code=locale_code,
                                                                      if_none_match=if_none_match,
                                                                      accept_encoding=accept_encoding)

    def get_translation_for_basic_edit(self, locale_code: str) -> JsonNode:
        return self.translation_controller.get_translation_for_basic_edit(locale_code=locale_code)

    def get_translation_infos(self) -> List[TranslationInfo]:
        return self.translation_controller.get_translation_infos()

    def get_downlink_converter(self, integration_type: str, vendor_name: str, model: str) -> str:
        return self.converter_library_controller.get_downlink_converter(integration_type=integration_type,
                                                                        vendor_name=vendor_name, model=model)

    def get_downlink_converter_metadata(self, integration_type: str, vendor_name: str, model: str) -> str:
        return self.converter_library_controller.get_downlink_converter_metadata(integration_type=integration_type,
                                                                                 vendor_name=vendor_name, model=model)

    def get_downlink_payload(self, integration_type: str, vendor_name: str, model: str) -> str:
        return self.converter_library_controller.get_downlink_payload(integration_type=integration_type,
                                                                      vendor_name=vendor_name, model=model)

    def get_uplink_converter(self, integration_type: str, vendor_name: str, model: str) -> str:
        return self.converter_library_controller.get_uplink_converter(integration_type=integration_type,
                                                                      vendor_name=vendor_name, model=model)

    def get_uplink_converter_metadata(self, integration_type: str, vendor_name: str, model: str) -> str:
        return self.converter_library_controller.get_uplink_converter_metadata(integration_type=integration_type,
                                                                               vendor_name=vendor_name, model=model)

    def get_uplink_payload(self, integration_type: str, vendor_name: str, model: str) -> str:
        return self.converter_library_controller.get_uplink_payload(integration_type=integration_type,
                                                                    vendor_name=vendor_name, model=model)

    def get_vendor_models(self, integration_type: str, vendor_name: str, converter_type: Optional[str] = None,
                          page: Optional[int] = None, page_size: Optional[int] = None,
                          load_images: Optional[bool] = None) -> List[Model]:
        return self.converter_library_controller.get_vendor_models(integration_type=integration_type,
                                                                   vendor_name=vendor_name,
                                                                   converter_type=converter_type, page=page,
                                                                   page_size=page_size, load_images=load_images)

    def get_vendors(self, integration_type: str, converter_type: Optional[str] = None, page: Optional[int] = None,
                    page_size: Optional[int] = None, load_images: Optional[bool] = None) -> List[Vendor]:
        return self.converter_library_controller.get_vendors(integration_type=integration_type,
                                                             converter_type=converter_type, page=page,
                                                             page_size=page_size, load_images=load_images)

    # Secret Controller
    def delete_secret(self, secret_id: SecretId) -> TbSecretDeleteResult:
        secret_id = self.get_id(secret_id)
        return self.secret_controller.delete_secret(id=secret_id)

    def get_secret_info_by_id(self, secret_id: SecretId) -> SecretInfo:
        secret_id = self.get_id(secret_id)
        return self.secret_controller.get_secret_info_by_id(id=secret_id)

    def get_secret_info_by_name(self, name: str) -> SecretInfo:
        return self.secret_controller.get_secret_info_by_name(name=name)

    def get_secret_infos(self, page_size: int, page: int,text_search: Optional[str] = None,
                         sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataSecretInfo:
        return self.secret_controller.get_secret_infos(page_size=page_size, page=page,
                                                       text_search=text_search, sort_property=sort_property,
                                                       sort_order=sort_order)

    def get_secret_names(self) -> List[str]:
        return self.secret_controller.get_secret_names()

    def save_secret(self, body: Secret) -> SecretInfo:
        return self.secret_controller.save_secret(body=body)

    def update_secret_description(self, id: SecretId, description: Optional[str] = None) -> SecretInfo:
        id = self.get_id(id)
        return self.secret_controller.update_secret_description(id=id, body=description)

    def update_secret_value(self, id: SecretId, value: str) -> SecretInfo:
        id = self.get_id(id)
        return self.secret_controller.update_secret_value(id=id, body=value)

    # Calculated Field Controller
    def get_last_calculated_field_reprocessing_job(self, id: CalculatedFieldId) -> Job:
        id = self.get_id(id)
        return self.calculated_field_controller.get_last_calculated_field_reprocessing_job(calculated_field_id=id)

    def reprocess_calculated_field(self, id: CalculatedFieldId, start_ts: int, end_ts: int) -> Job:
        id = self.get_id(id)
        return self.calculated_field_controller.reprocess_calculated_field(calculated_field_id=id, start_ts=start_ts,
                                                                           end_ts=end_ts)

    def validate_calculated_field_reprocessing(self, id: CalculatedFieldId) -> CfReprocessingValidationResult:
        id = self.get_id(id)
        return self.calculated_field_controller.validate_calculated_field_reprocessing(calculated_field_id=id)

    # Report Template Controller
    def delete_report_template(self, report_template_id: ReportTemplateId) -> None:
        report_template_id = self.get_id(report_template_id)
        return self.report_template_controller.delete_report_template(report_template_id=report_template_id)

    def get_all_report_template_infos(self, page_size: int, page: int, text_search: Optional[str] = None,
                                      sort_property: Optional[str] = None,
                                      sort_order: Optional[str] = None,
                                      type_list: Optional[str] = None,
                                      format_list: Optional[str] = None,
                                      include_customers: Optional[bool] = None) -> PageDataReportTemplateInfo:
        return self.report_template_controller.get_all_report_template_infos(page_size=page_size, page=page,
                                                                            text_search=text_search,
                                                                            sort_property=sort_property,
                                                                            sort_order=sort_order,
                                                                            type_list=type_list,
                                                                            format_list=format_list,
                                                                            include_customers=include_customers)

    def get_report_template_by_id(self, report_template_id: ReportTemplateId) -> ReportTemplate:
        report_template_id = self.get_id(report_template_id)
        return self.report_template_controller.get_report_template_by_id(report_template_id=report_template_id)

    def get_report_template_info_by_id(self, report_template_id: ReportTemplateId) -> ReportTemplateInfo:
        report_template_id = self.get_id(report_template_id)
        return self.report_template_controller.get_report_template_info_by_id(report_template_id=report_template_id)

    def get_report_templates_by_ids(self, report_template_ids: List[str]) -> List[ReportTemplateInfo]:
        report_template_ids = ','.join(report_template_ids)
        return self.report_template_controller.get_report_templates_by_ids(report_template_ids=report_template_ids)

    def save_report_template(self, body: ReportTemplate) -> ReportTemplate:
        return self.report_template_controller.save_report_template(body=body)

    def send_addon_access_error(self, addon_type: str) -> None:
        return self.notification_controller.send_addon_access_error(addon_type=addon_type)

    def test_report_and_download(self, body: ReportRequest) -> bytes:
        return self.report_controller.test_report_and_download(body=body)

    def get_timeseries_by_read_ts_kv_queries(self, body, entity_id: EntityId) -> List[ReadTsKvQueryResult]:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)

        return self.telemetry_controller.get_timeseries_by_read_ts_kv_queries(body=body, entity_id=entity_id,
                                                                              entity_type=entity_type)

    def get_trendz_summary(self) -> TrendzSummary:
        return self.trendz_api_controller.get_trendz_summary()

    def get_trendz_usage(self) -> TrendzUsage:
        return self.trendz_api_controller.get_trendz_usage()

    def get_trendz_view_by_id(self, view_id) -> TrendzViewConfig:
        view_id = self.get_id(view_id)
        return self.trendz_api_controller.get_trendz_view_by_id(view_id=view_id)

    def get_trendz_views(self, page_size: int, page: int, text_search: Optional[str] = None,
                         sort_property: Optional[str] = None,
                         sort_order: Optional[str] = None) -> PageDataTrendzViewConfigLite:
        return self.trendz_api_controller.get_trendz_views(page_size=page_size, page=page,
                                                           text_search=text_search,
                                                           sort_property=sort_property,
                                                           sort_order=sort_order)

    def connect_to_trendz(self) -> TrendzSynchronizationResult:
        return self.trendz_controller.connect_to_trendz()

    def get_trendz_config(self) -> TrendzConfiguration:
        return self.trendz_controller.get_trendz_config()

    def get_trendz_sync_result(self) -> TrendzSynchronizationResult:
        return self.trendz_controller.get_trendz_sync_result()

    def perform_trendz_healthcheck(self) -> TrendzHealthcheckResult:
        return self.trendz_controller.perform_trendz_healthcheck()

    def public_connect_to_trendz(self) -> None:
        return self.trendz_controller.public_connect_to_trendz()

    def save_trendz_config(self, body: TrendzConfiguration) -> TrendzConfiguration:
        return self.trendz_controller.save_trendz_config(body=body)

    # Rule Engine Controller
    def handle_rule_engine_request_for_entity(self, entity_id: EntityId, body: Any) -> Any:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.rule_engine_controller.handle_rule_engine_request_for_entity(body=body, entity_type=entity_type,
                                                                                 entity_id=entity_id)

    def handle_rule_engine_request_for_entity_with_timeout(self, entity_id: EntityId, timeout: int, body: Any) -> Any:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.rule_engine_controller.handle_rule_engine_request_for_entity_with_timeout(
            body=body, entity_type=entity_type, entity_id=entity_id, timeout=timeout)

    def handle_rule_engine_request_for_entity_with_queue_and_timeout(self, entity_id: EntityId, queue_name: str,
                                                                     timeout: int, body: Any) -> Any:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.rule_engine_controller.handle_rule_engine_request_for_entity_with_queue_and_timeout(
            body=body, entity_type=entity_type, entity_id=entity_id, queue_name=queue_name, timeout=timeout)

    def handle_rule_engine_request_for_user(self, body: Any) -> Any:
        return self.rule_engine_controller.handle_rule_engine_request_for_user(body=body)

    # Admin Controller
    def get_subscription_info(self) -> SubscriptionInfo:
        return self.admin_controller.get_subscription_info()

    def refresh_license(self) -> SubscriptionInfo:
        return self.admin_controller.refresh_license()

    # Agent App Profile Controller
    def delete_agent_app_profile(self, profile_id: AgentAppProfileId) -> None:
        profile_id = self.get_id(profile_id)
        return self.agent_app_profile_controller.delete_agent_app_profile(profile_id=profile_id)

    def get_agent_app_profile_by_id(self, profile_id: AgentAppProfileId) -> AgentAppProfile:
        profile_id = self.get_id(profile_id)
        return self.agent_app_profile_controller.get_agent_app_profile_by_id(profile_id=profile_id)

    def get_agent_app_profile_info_by_id(self, profile_id: AgentAppProfileId) -> AgentAppProfileInfo:
        profile_id = self.get_id(profile_id)
        return self.agent_app_profile_controller.get_agent_app_profile_info_by_id(profile_id=profile_id)

    def get_agent_app_profiles_by_app_type(self, app_type: str) -> List[AgentAppProfileInfo]:
        return self.agent_app_profile_controller.get_agent_app_profiles_by_app_type(app_type=app_type)

    def get_agent_app_profiles_by_ids(self, agent_app_profile_ids: List[str]) -> List[AgentAppProfile]:
        return self.agent_app_profile_controller.get_agent_app_profiles_by_ids(
            agent_app_profile_ids=agent_app_profile_ids)

    def get_tenant_agent_app_profiles(self, page_size: int, page: int, text_search: Optional[str] = None,
                                      sort_property: Optional[str] = None,
                                      sort_order: Optional[str] = None) -> PageDataAgentAppProfile:
        return self.agent_app_profile_controller.get_tenant_agent_app_profiles(page_size=page_size, page=page,
                                                                               text_search=text_search,
                                                                               sort_property=sort_property,
                                                                               sort_order=sort_order)

    def materialize_agent_app_profile(self, app_type: str, template_version: str,
                                      compose_type: Optional[str] = None) -> AgentAppProfile:
        return self.agent_app_profile_controller.materialize_agent_app_profile(app_type=app_type,
                                                                               template_version=template_version,
                                                                               compose_type=compose_type)

    def merge_agent_app_profile_for_preview(self, body: AgentAppProfile, template_version: str,
                                            compose_type: Optional[str] = None, action_type: Optional[str] = None,
                                            set_host_values: Optional[bool] = None) -> AgentAppProfile:
        return self.agent_app_profile_controller.merge_agent_app_profile_for_preview(body=body,
                                                                                     template_version=template_version,
                                                                                     compose_type=compose_type,
                                                                                     action_type=action_type,
                                                                                     set_host_values=set_host_values)

    def save_agent_app_profile(self, body: AgentAppProfile) -> AgentAppProfile:
        return self.agent_app_profile_controller.save_agent_app_profile(body=body)

    # Agent App Template Controller
    def get_agent_app_template_by_current_version(self, app_type: str, config_type: str,
                                                  current_version: str) -> AgentAppTemplate:
        return self.agent_app_template_controller.get_agent_app_template_by_current_version(
            app_type=app_type, config_type=config_type, current_version=current_version)

    def get_agent_app_templates(self) -> List[AgentAppTemplate]:
        return self.agent_app_template_controller.get_agent_app_templates()

    def get_agent_app_templates_by_app_type(self, app_type: str, config_type: str) -> List[AgentAppTemplate]:
        return self.agent_app_template_controller.get_agent_app_templates_by_app_type(app_type=app_type,
                                                                                      config_type=config_type)

    def get_latest_agent_app_template_by_app_type_and_config_type(self, app_type: str,
                                                                  config_type: str) -> AgentAppTemplate:
        return self.agent_app_template_controller.get_latest_agent_app_template_by_app_type_and_config_type(
            app_type=app_type, config_type=config_type)

    # Agent Application Controller
    def assign_related_entity_to_agent_app(self, agent_application_id: AgentApplicationId,
                                           entity_id: EntityId) -> AgentApplication:
        agent_application_id = self.get_id(agent_application_id)
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.agent_application_controller.assign_related_entity_to_agent_app(
            agent_application_id=agent_application_id, entity_type=entity_type, entity_id=entity_id)

    def attach_to_profile(self, agent_application_id: AgentApplicationId, profile_id: str) -> AgentApplication:
        agent_application_id = self.get_id(agent_application_id)
        return self.agent_application_controller.attach_to_profile(agent_application_id=agent_application_id,
                                                                   profile_id=profile_id)

    def cancel_agent_app_event(self, agent_application_id: AgentApplicationId,
                               agent_app_event_id: AgentAppEventId) -> None:
        agent_application_id = self.get_id(agent_application_id)
        agent_app_event_id = self.get_id(agent_app_event_id)
        return self.agent_application_controller.cancel_agent_app_event(agent_application_id=agent_application_id,
                                                                        agent_app_event_id=agent_app_event_id)

    def create_agent_app_event(self, body: AgentAppEventRequest,
                               agent_application_id: AgentApplicationId) -> AgentAppEvent:
        agent_application_id = self.get_id(agent_application_id)
        return self.agent_application_controller.create_agent_app_event(body=body,
                                                                        agent_application_id=agent_application_id)

    def detach_from_profile(self, agent_application_id: AgentApplicationId) -> AgentApplication:
        agent_application_id = self.get_id(agent_application_id)
        return self.agent_application_controller.detach_from_profile(agent_application_id=agent_application_id)

    def get_agent_app_event_by_id(self, agent_app_event_id: AgentAppEventId) -> AgentAppEvent:
        agent_app_event_id = self.get_id(agent_app_event_id)
        return self.agent_application_controller.get_agent_app_event_by_id(agent_app_event_id=agent_app_event_id)

    def get_agent_app_events(self, agent_application_id: AgentApplicationId, page_size: int, page: int,
                             text_search: Optional[str] = None, action_type: Optional[str] = None,
                             processing_status: Optional[str] = None, sort_property: Optional[str] = None,
                             sort_order: Optional[str] = None) -> PageDataAgentAppEvent:
        agent_application_id = self.get_id(agent_application_id)
        return self.agent_application_controller.get_agent_app_events(agent_application_id=agent_application_id,
                                                                      page_size=page_size, page=page,
                                                                      text_search=text_search, action_type=action_type,
                                                                      processing_status=processing_status,
                                                                      sort_property=sort_property,
                                                                      sort_order=sort_order)

    def get_agent_app_units(self, agent_application_id: AgentApplicationId, page_size: int, page: int,
                            text_search: Optional[str] = None, type: Optional[str] = None,
                            sort_property: Optional[str] = None,
                            sort_order: Optional[str] = None) -> PageDataAgentAppUnit:
        agent_application_id = self.get_id(agent_application_id)
        return self.agent_application_controller.get_agent_app_units(agent_application_id=agent_application_id,
                                                                     page_size=page_size, page=page,
                                                                     text_search=text_search, type=type,
                                                                     sort_property=sort_property, sort_order=sort_order)

    def get_agent_application_by_id(self, agent_application_id: AgentApplicationId) -> AgentApplicationInfo:
        agent_application_id = self.get_id(agent_application_id)
        return self.agent_application_controller.get_agent_application_by_id(agent_application_id=agent_application_id)

    def get_agent_application_by_related_entity(self, entity_id: EntityId) -> AgentApplication:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.agent_application_controller.get_agent_application_by_related_entity(entity_type=entity_type,
                                                                                         entity_id=entity_id)

    def get_agent_applications_by_agent_id(self, agent_id: AgentId, page_size: int, page: int,
                                           text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                           sort_order: Optional[str] = None) -> PageDataAgentApplicationInfo:
        agent_id = self.get_id(agent_id)
        return self.agent_application_controller.get_agent_applications_by_agent_id(agent_id=agent_id,
                                                                                    page_size=page_size, page=page,
                                                                                    text_search=text_search,
                                                                                    sort_property=sort_property,
                                                                                    sort_order=sort_order)

    def get_managed_related_entity_ids(self, entity_type: str) -> List[EntityId]:
        return self.agent_application_controller.get_managed_related_entity_ids(entity_type=entity_type)

    def get_related_entity_candidates(self, entity_type: str, page_size: int, page: int,
                                      text_search: Optional[str] = None,
                                      current_entity_id: Optional[str] = None) -> PageDataEntityInfo:
        return self.agent_application_controller.get_related_entity_candidates(entity_type=entity_type,
                                                                               page_size=page_size, page=page,
                                                                               text_search=text_search,
                                                                               current_entity_id=current_entity_id)

    def install_agent_app(self, body: AgentAppEventRequest) -> AgentAppInstallResponse:
        return self.agent_application_controller.install_agent_app(body=body)

    def merge_agent_application_for_preview(self, template_version: str, body: Optional[AgentApplication] = None,
                                            app_type: Optional[str] = None, compose_type: Optional[str] = None,
                                            action_type: Optional[str] = None, set_host_values: Optional[bool] = None,
                                            related_entity_type: Optional[str] = None,
                                            related_entity_id: Optional[str] = None) -> AgentApplication:
        return self.agent_application_controller.merge_agent_application_for_preview(
            template_version=template_version, body=body, app_type=app_type, compose_type=compose_type,
            action_type=action_type, set_host_values=set_host_values, related_entity_type=related_entity_type,
            related_entity_id=related_entity_id)

    def unassign_related_entity_from_agent_app(self, agent_application_id: AgentApplicationId) -> AgentApplication:
        agent_application_id = self.get_id(agent_application_id)
        return self.agent_application_controller.unassign_related_entity_from_agent_app(
            agent_application_id=agent_application_id)

    def update_agent_application(self, body: AgentApplication) -> AgentApplication:
        return self.agent_application_controller.update_agent_application(body=body)

    # Agent Bulk Action Controller
    def get_agent_bulk_action(self, bulk_action_id: AgentBulkActionId) -> AgentBulkAction:
        bulk_action_id = self.get_id(bulk_action_id)
        return self.agent_bulk_action_controller.get_agent_bulk_action(bulk_action_id=bulk_action_id)

    def get_agent_bulk_action_event_stats(self, bulk_action_id: AgentBulkActionId) -> AgentBulkActionEventStats:
        bulk_action_id = self.get_id(bulk_action_id)
        return self.agent_bulk_action_controller.get_agent_bulk_action_event_stats(bulk_action_id=bulk_action_id)

    def get_agent_bulk_action_events(self, bulk_action_id: AgentBulkActionId, page_size: int, page: int,
                                     text_search: Optional[str] = None, action_type: Optional[str] = None,
                                     processing_status: Optional[str] = None, sort_property: Optional[str] = None,
                                     sort_order: Optional[str] = None) -> PageDataAgentAppEventInfo:
        bulk_action_id = self.get_id(bulk_action_id)
        return self.agent_bulk_action_controller.get_agent_bulk_action_events(bulk_action_id=bulk_action_id,
                                                                              page_size=page_size, page=page,
                                                                              text_search=text_search,
                                                                              action_type=action_type,
                                                                              processing_status=processing_status,
                                                                              sort_property=sort_property,
                                                                              sort_order=sort_order)

    # Agent Controller
    def delete_agent(self, agent_id: AgentId) -> None:
        agent_id = self.get_id(agent_id)
        return self.agent_controller.delete_agent(agent_id=agent_id)

    def get_agent_app_event_infos_by_agent_id(self, agent_id: AgentId, page_size: int, page: int,
                                              text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                              sort_order: Optional[str] = None, action_type: Optional[str] = None,
                                              processing_status: Optional[str] = None) -> PageDataAgentAppEventInfo:
        agent_id = self.get_id(agent_id)
        return self.agent_controller.get_agent_app_event_infos_by_agent_id(agent_id=agent_id, page_size=page_size,
                                                                           page=page, text_search=text_search,
                                                                           sort_property=sort_property,
                                                                           sort_order=sort_order,
                                                                           action_type=action_type,
                                                                           processing_status=processing_status)

    def get_agent_app_events_by_agent_id(self, agent_id: AgentId, page_size: int, page: int,
                                         text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                         sort_order: Optional[str] = None) -> PageDataAgentAppEvent:
        agent_id = self.get_id(agent_id)
        return self.agent_controller.get_agent_app_events_by_agent_id(agent_id=agent_id, page_size=page_size,
                                                                      page=page, text_search=text_search,
                                                                      sort_property=sort_property,
                                                                      sort_order=sort_order)

    def get_agent_by_id(self, agent_id: AgentId) -> Agent:
        agent_id = self.get_id(agent_id)
        return self.agent_controller.get_agent_by_id(agent_id=agent_id)

    def get_agent_info_by_id(self, agent_id: AgentId) -> AgentInfo:
        agent_id = self.get_id(agent_id)
        return self.agent_controller.get_agent_info_by_id(agent_id=agent_id)

    def get_agent_infos_by_ids(self, agent_ids: List[str]) -> List[AgentInfo]:
        return self.agent_controller.get_agent_infos_by_ids(agent_ids=agent_ids)

    def get_agent_install_instructions(self, agent_id: AgentId, method: str) -> AgentInstructions:
        agent_id = self.get_id(agent_id)
        return self.agent_controller.get_agent_install_instructions(agent_id=agent_id, method=method)

    def get_agent_upgrade_target(self, agent_id: AgentId) -> str:
        agent_id = self.get_id(agent_id)
        return self.agent_controller.get_agent_upgrade_target(agent_id=agent_id)

    def get_customer_agent_infos(self, customer_id: CustomerId, page_size: int, page: int,
                                 text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                 sort_order: Optional[str] = None) -> PageDataAgentInfo:
        customer_id = self.get_id(customer_id)
        return self.agent_controller.get_customer_agent_infos(customer_id=customer_id, page_size=page_size, page=page,
                                                              text_search=text_search, sort_property=sort_property,
                                                              sort_order=sort_order)

    def get_customer_agents(self, customer_id: CustomerId, page_size: int, page: int,
                            text_search: Optional[str] = None, sort_property: Optional[str] = None,
                            sort_order: Optional[str] = None) -> PageDataAgent:
        customer_id = self.get_id(customer_id)
        return self.agent_controller.get_customer_agents(customer_id=customer_id, page_size=page_size, page=page,
                                                         text_search=text_search, sort_property=sort_property,
                                                         sort_order=sort_order)

    def get_latest_agent_image_ref(self) -> str:
        return self.agent_controller.get_latest_agent_image_ref()

    def get_tenant_agent_infos(self, page_size: int, page: int, text_search: Optional[str] = None,
                               sort_property: Optional[str] = None,
                               sort_order: Optional[str] = None) -> PageDataAgentInfo:
        return self.agent_controller.get_tenant_agent_infos(page_size=page_size, page=page, text_search=text_search,
                                                            sort_property=sort_property, sort_order=sort_order)

    def get_tenant_agents(self, page_size: int, page: int, text_search: Optional[str] = None,
                          sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataAgent:
        return self.agent_controller.get_tenant_agents(page_size=page_size, page=page, text_search=text_search,
                                                       sort_property=sort_property, sort_order=sort_order)

    def is_agent_upgrade_available(self, agent_id: AgentId) -> bool:
        agent_id = self.get_id(agent_id)
        return self.agent_controller.is_agent_upgrade_available(agent_id=agent_id)

    def save_agent(self, body: Agent, entity_group_id: Optional[EntityGroupId] = None,
                   entity_group_ids: Optional[List[str]] = None) -> Agent:
        entity_group_id = self.get_id(entity_group_id)
        return self.agent_controller.save_agent(body=body, entity_group_id=entity_group_id,
                                                entity_group_ids=entity_group_ids)

    def upgrade_agent(self, body: AgentUpgradeRequest, agent_id: AgentId) -> AgentAppEvent:
        agent_id = self.get_id(agent_id)
        return self.agent_controller.upgrade_agent(body=body, agent_id=agent_id)

    # Agent Profile Controller
    def assign_app_profile_to_agent_profile(self, agent_profile_id: AgentProfileId,
                                            application_profile_id: str) -> None:
        agent_profile_id = self.get_id(agent_profile_id)
        return self.agent_profile_controller.assign_app_profile_to_agent_profile(
            agent_profile_id=agent_profile_id, application_profile_id=application_profile_id)

    def assign_app_profiles_to_agent_profile(self, agent_profile_id: AgentProfileId,
                                             app_profile_ids: Optional[List[str]] = None) -> None:
        agent_profile_id = self.get_id(agent_profile_id)
        return self.agent_profile_controller.assign_app_profiles_to_agent_profile(agent_profile_id=agent_profile_id,
                                                                                  app_profile_ids=app_profile_ids)

    def bulk_operation(self, body: BulkOperationRequest, agent_profile_id: AgentProfileId,
                       application_profile_id: str) -> AgentBulkAction:
        agent_profile_id = self.get_id(agent_profile_id)
        return self.agent_profile_controller.bulk_operation(body=body, agent_profile_id=agent_profile_id,
                                                            application_profile_id=application_profile_id)

    def delete_agent_profile(self, agent_profile_id: AgentProfileId) -> None:
        agent_profile_id = self.get_id(agent_profile_id)
        return self.agent_profile_controller.delete_agent_profile(agent_profile_id=agent_profile_id)

    def get_agent_profile_app_profile_bulk_actions(self, agent_profile_id: AgentProfileId, application_profile_id: str,
                                                   page_size: int, page: int, sort_property: Optional[str] = None,
                                                   sort_order: Optional[str] = None) -> PageDataAgentBulkAction:
        agent_profile_id = self.get_id(agent_profile_id)
        return self.agent_profile_controller.get_agent_profile_app_profile_bulk_actions(
            agent_profile_id=agent_profile_id, application_profile_id=application_profile_id, page_size=page_size,
            page=page, sort_property=sort_property, sort_order=sort_order)

    def get_agent_profile_app_profile_infos(self,
                                            agent_profile_id: AgentProfileId) -> List[AgentAppProfileRelationInfo]:
        agent_profile_id = self.get_id(agent_profile_id)
        return self.agent_profile_controller.get_agent_profile_app_profile_infos(agent_profile_id=agent_profile_id)

    def get_agent_profile_bulk_actions(self, agent_profile_id: AgentProfileId, page_size: int, page: int,
                                       sort_property: Optional[str] = None,
                                       sort_order: Optional[str] = None) -> PageDataAgentBulkAction:
        agent_profile_id = self.get_id(agent_profile_id)
        return self.agent_profile_controller.get_agent_profile_bulk_actions(agent_profile_id=agent_profile_id,
                                                                            page_size=page_size, page=page,
                                                                            sort_property=sort_property,
                                                                            sort_order=sort_order)

    def get_agent_profile_by_id(self, agent_profile_id: AgentProfileId) -> AgentProfile:
        agent_profile_id = self.get_id(agent_profile_id)
        return self.agent_profile_controller.get_agent_profile_by_id(agent_profile_id=agent_profile_id)

    def get_agent_profile_info_by_id(self, agent_profile_id: AgentProfileId) -> AgentProfileInfo:
        agent_profile_id = self.get_id(agent_profile_id)
        return self.agent_profile_controller.get_agent_profile_info_by_id(agent_profile_id=agent_profile_id)

    def get_agent_provision_instructions(self, agent_profile_id: AgentProfileId, method: str) -> AgentInstructions:
        agent_profile_id = self.get_id(agent_profile_id)
        return self.agent_profile_controller.get_agent_provision_instructions(agent_profile_id=agent_profile_id,
                                                                              method=method)

    def get_default_agent_profile_info(self) -> AgentProfileInfo:
        return self.agent_profile_controller.get_default_agent_profile_info()

    def get_tenant_agent_profile_infos(self, page_size: int, page: int, text_search: Optional[str] = None,
                                       sort_property: Optional[str] = None,
                                       sort_order: Optional[str] = None) -> PageDataAgentProfileInfo:
        return self.agent_profile_controller.get_tenant_agent_profile_infos(page_size=page_size, page=page,
                                                                            text_search=text_search,
                                                                            sort_property=sort_property,
                                                                            sort_order=sort_order)

    def get_tenant_agent_profiles(self, page_size: int, page: int, text_search: Optional[str] = None,
                                  sort_property: Optional[str] = None,
                                  sort_order: Optional[str] = None) -> PageDataAgentProfile:
        return self.agent_profile_controller.get_tenant_agent_profiles(page_size=page_size, page=page,
                                                                       text_search=text_search,
                                                                       sort_property=sort_property,
                                                                       sort_order=sort_order)

    def preview_bulk_operation(self, body: BulkOperationRequest, agent_profile_id: AgentProfileId,
                               application_profile_id: str) -> BulkOperationPreview:
        agent_profile_id = self.get_id(agent_profile_id)
        return self.agent_profile_controller.preview_bulk_operation(body=body, agent_profile_id=agent_profile_id,
                                                                    application_profile_id=application_profile_id)

    def save_agent_profile(self, body: AgentProfile, app_profile_ids: Optional[List[str]] = None) -> AgentProfile:
        return self.agent_profile_controller.save_agent_profile(body=body, app_profile_ids=app_profile_ids)

    def set_app_profile_relates_on_auto_discovery(self, agent_profile_id: AgentProfileId, application_profile_id: str,
                                                  relate: bool) -> None:
        agent_profile_id = self.get_id(agent_profile_id)
        return self.agent_profile_controller.set_app_profile_relates_on_auto_discovery(
            agent_profile_id=agent_profile_id, application_profile_id=application_profile_id, relate=relate)

    def set_default_agent_profile(self, agent_profile_id: AgentProfileId) -> AgentProfile:
        agent_profile_id = self.get_id(agent_profile_id)
        return self.agent_profile_controller.set_default_agent_profile(agent_profile_id=agent_profile_id)

    def unassign_app_profile_from_agent_profile(self, agent_profile_id: AgentProfileId,
                                                application_profile_id: str) -> None:
        agent_profile_id = self.get_id(agent_profile_id)
        return self.agent_profile_controller.unassign_app_profile_from_agent_profile(
            agent_profile_id=agent_profile_id, application_profile_id=application_profile_id)

    # AI Chat Controller
    def create_chat(self, body: Any) -> JsonNode:
        return self.ai_chat_controller.create_chat(body=body)

    def delete_chat(self, chat_id: str) -> None:
        return self.ai_chat_controller.delete_chat(chat_id=chat_id)

    def get_chat_messages(self, chat_id: str) -> JsonNode:
        return self.ai_chat_controller.get_chat_messages(chat_id=chat_id)

    def list_chats(self) -> JsonNode:
        return self.ai_chat_controller.list_chats()

    def update_chat(self, body: Any, chat_id: str) -> None:
        return self.ai_chat_controller.update_chat(body=body, chat_id=chat_id)

    # AI Device Dashboard Controller
    def generate_dashboard(self, body: Any, device_id: DeviceId) -> JsonNode:
        device_id = self.get_id(device_id)
        return self.ai_device_dashboard_controller.generate_dashboard(
            body=body, x_authorization=self.configuration.get_api_key_with_prefix('X-Authorization'),
            device_id=device_id)

    # AI Solution Controller
    def chat(self, body: str, solution_id: str, step: str) -> JsonNode:
        return self.ai_solution_controller.chat(body=body, solution_id=solution_id, step=step)

    def clear_step(self, solution_id: str, step: str) -> None:
        return self.ai_solution_controller.clear_step(solution_id=solution_id, step=step)

    def create_solution(self, solution_id: str) -> JsonNode:
        return self.ai_solution_controller.create_solution(solution_id=solution_id)

    def delete_solution(self, solution_id: str) -> None:
        return self.ai_solution_controller.delete_solution(solution_id=solution_id)

    def get_solution(self, solution_id: str) -> JsonNode:
        return self.ai_solution_controller.get_solution(solution_id=solution_id)

    def get_solutions(self) -> JsonNode:
        return self.ai_solution_controller.get_solutions()

    def install_solution(self, solution_id: str) -> JsonNode:
        return self.ai_solution_controller.install_solution(
            solution_id=solution_id, x_authorization=self.configuration.get_api_key_with_prefix('X-Authorization'))

    def start_new(self) -> JsonNode:
        return self.ai_solution_controller.start_new()

    def uninstall_solution(self, solution_id: str) -> JsonNode:
        return self.ai_solution_controller.uninstall_solution(
            solution_id=solution_id, x_authorization=self.configuration.get_api_key_with_prefix('X-Authorization'))

    def update_data(self, body: Any, solution_id: str, data_key: str) -> JsonNode:
        return self.ai_solution_controller.update_data(body=body, solution_id=solution_id, data_key=data_key)

    # AI Tool Controller
    def resolve_tool_approval(self, body: Any) -> JsonNode:
        return self.ai_tool_controller.resolve_tool_approval(body=body)

    # Alarm Controller
    def get_alarms_v2(self, entity_id: EntityId, page_size: int, page: int, status_list: Optional[List[str]] = None,
                      severity_list: Optional[List[str]] = None, type_list: Optional[List[str]] = None,
                      assignee_id: Optional[str] = None, text_search: Optional[str] = None,
                      sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                      start_time: Optional[int] = None, end_time: Optional[int] = None) -> PageDataAlarmInfo:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.alarm_controller.get_alarms_v2(entity_type=entity_type, entity_id=entity_id, page_size=page_size,
                                                   page=page, status_list=status_list, severity_list=severity_list,
                                                   type_list=type_list, assignee_id=assignee_id,
                                                   text_search=text_search, sort_property=sort_property,
                                                   sort_order=sort_order, start_time=start_time, end_time=end_time)

    def get_all_alarms_v2(self, page_size: int, page: int, status_list: Optional[List[str]] = None,
                          severity_list: Optional[List[str]] = None, type_list: Optional[List[str]] = None,
                          assignee_id: Optional[str] = None, text_search: Optional[str] = None,
                          sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                          start_time: Optional[int] = None, end_time: Optional[int] = None) -> PageDataAlarmInfo:
        return self.alarm_controller.get_all_alarms_v2(page_size=page_size, page=page, status_list=status_list,
                                                       severity_list=severity_list, type_list=type_list,
                                                       assignee_id=assignee_id, text_search=text_search,
                                                       sort_property=sort_property, sort_order=sort_order,
                                                       start_time=start_time, end_time=end_time)

    # Alarm Rule Controller
    def delete_alarm_rule(self, alarm_rule_id: str) -> None:
        return self.alarm_rule_controller.delete_alarm_rule(alarm_rule_id=alarm_rule_id)

    def get_alarm_rule_by_id(self, alarm_rule_id: str) -> AlarmRuleDefinition:
        return self.alarm_rule_controller.get_alarm_rule_by_id(alarm_rule_id=alarm_rule_id)

    def get_alarm_rule_names(self, page_size: int, page: int, text_search: Optional[str] = None,
                             sort_order: Optional[str] = None) -> PageDataString:
        return self.alarm_rule_controller.get_alarm_rule_names(page_size=page_size, page=page, text_search=text_search,
                                                               sort_order=sort_order)

    def get_alarm_rules(self, page_size: int, page: int, entity_type: Optional[str] = None,
                        entities: Optional[List[str]] = None, text_search: Optional[str] = None,
                        sort_property: Optional[str] = None,
                        sort_order: Optional[str] = None) -> PageDataAlarmRuleDefinitionInfo:
        return self.alarm_rule_controller.get_alarm_rules(page_size=page_size, page=page, entity_type=entity_type,
                                                          entities=entities, text_search=text_search,
                                                          sort_property=sort_property, sort_order=sort_order)

    def get_alarm_rules_by_entity_id(self, entity_id: EntityId, page_size: int, page: int,
                                     text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                     sort_order: Optional[str] = None) -> PageDataAlarmRuleDefinition:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.alarm_rule_controller.get_alarm_rules_by_entity_id(entity_type=entity_type, entity_id=entity_id,
                                                                       page_size=page_size, page=page,
                                                                       text_search=text_search,
                                                                       sort_property=sort_property,
                                                                       sort_order=sort_order)

    def get_latest_alarm_rule_debug_event(self, alarm_rule_id: str) -> JsonNode:
        return self.alarm_rule_controller.get_latest_alarm_rule_debug_event(alarm_rule_id=alarm_rule_id)

    def save_alarm_rule(self, body: AlarmRuleDefinition) -> AlarmRuleDefinition:
        return self.alarm_rule_controller.save_alarm_rule(body=body)

    def test_alarm_rule_script(self, body: Any) -> JsonNode:
        return self.alarm_rule_controller.test_alarm_rule_script(body=body)

    # API Key Controller
    def delete_api_key(self, id: ApiKeyId) -> None:
        id = self.get_id(id)
        return self.api_key_controller.delete_api_key(id=id)

    def enable_api_key(self, id: ApiKeyId, enabled_value: bool) -> ApiKeyInfo:
        id = self.get_id(id)
        return self.api_key_controller.enable_api_key(id=id, enabled_value=enabled_value)

    def get_user_api_keys(self, user_id: UserId, page_size: int, page: int, text_search: Optional[str] = None,
                          sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataApiKeyInfo:
        user_id = self.get_id(user_id)
        return self.api_key_controller.get_user_api_keys(user_id=user_id, page_size=page_size, page=page,
                                                         text_search=text_search, sort_property=sort_property,
                                                         sort_order=sort_order)

    def save_api_key(self, body: ApiKeyInfo) -> ApiKey:
        return self.api_key_controller.save_api_key(body=body)

    def update_api_key_description(self, id: ApiKeyId, body: Optional[str] = None) -> ApiKeyInfo:
        id = self.get_id(id)
        return self.api_key_controller.update_api_key_description(id=id, body=body)

    # Calculated Field Controller
    def get_calculated_fields(self, page_size: int, page: int, types: Optional[List[str]] = None,
                              entity_type: Optional[str] = None, entities: Optional[List[str]] = None,
                              text_search: Optional[str] = None, sort_property: Optional[str] = None,
                              sort_order: Optional[str] = None,
                              name: Optional[List[str]] = None) -> PageDataCalculatedFieldInfo:
        return self.calculated_field_controller.get_calculated_fields(page_size=page_size, page=page, types=types,
                                                                      entity_type=entity_type, entities=entities,
                                                                      text_search=text_search,
                                                                      sort_property=sort_property,
                                                                      sort_order=sort_order, name=name)

    def reprocess_calculated_field_and_wait(self, calculated_field_id: CalculatedFieldId, start_ts: int,
                                            end_ts: int) -> None:
        calculated_field_id = self.get_id(calculated_field_id)
        return self.calculated_field_controller.reprocess_calculated_field_and_wait(
            calculated_field_id=calculated_field_id, start_ts=start_ts, end_ts=end_ts)

    def test_calculated_field_script(self, body: Any) -> JsonNode:
        return self.calculated_field_controller.test_calculated_field_script(body=body)

    # Converter Controller
    def unwrap_raw_payload(self, body: Any, integration_type: str) -> JsonNode:
        return self.converter_controller.unwrap_raw_payload(body=body, integration_type=integration_type)

    # Device Controller
    def claim_device_by_name(self, device_name: str, body: Optional[ClaimRequest] = None,
                             sub_customer_id: Optional[str] = None) -> Any:
        return self.device_controller.claim_device(device_name=device_name, body=body, sub_customer_id=sub_customer_id)

    # Edge Controller
    def get_edges_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size: str, page: str,
                                     text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                     sort_order: Optional[str] = None) -> PageDataEdge:
        entity_group_id = self.get_id(entity_group_id)
        return self.edge_controller.get_edges_by_entity_group_id(entity_group_id=entity_group_id, page_size=page_size,
                                                                 page=page, text_search=text_search,
                                                                 sort_property=sort_property, sort_order=sort_order)

    # Entity Group Controller
    def share_entity_group_to_child_owner_user_group_v2(self, body: ShareGroupRequest,
                                                        entity_group_id: EntityGroupId) -> None:
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.share_entity_group_to_child_owner_user_group_v2(
            body=body, entity_group_id=entity_group_id)

    # Entity Query Controller
    def find_available_entity_keys_by_query_v2(self, body: EntityDataQuery, include_timeseries: Optional[bool] = None,
                                               include_attributes: Optional[bool] = None, scopes: Optional[str] = None,
                                               include_samples: Optional[bool] = None) -> AvailableEntityKeysV2:
        return self.entity_query_controller.find_available_entity_keys_by_query_v2(
            body=body, include_timeseries=include_timeseries, include_attributes=include_attributes, scopes=scopes,
            include_samples=include_samples)

    # Integration Controller
    def export_integration_package(self, integration_id: IntegrationId) -> bytes:
        integration_id = self.get_id(integration_id)
        return self.integration_controller.export_integration_package(integration_id=integration_id)

    # Mobile App Bundle Controller
    def update_mobile_app_bundle_oauth2_clients(self, body: List[str], id: MobileAppBundleId) -> None:
        id = self.get_id(id)
        return self.mobile_app_bundle_controller.update_mobile_app_bundle_oauth2_clients(body=body, id=id)

    # Notification Controller
    def send_addon_access_request(self, addon_type: str) -> None:
        return self.notification_controller.send_addon_access_request(addon_type=addon_type)

    def send_plan_upgrade_request(self, plan_name: str) -> None:
        return self.notification_controller.send_plan_upgrade_request(plan_name=plan_name)

    # Report Controller
    def create_report(self, file: str, info: Union[str, Dict]) -> Report:
        # multipart: the report file and its info as JSON (the spec says application/json, the server
        # accepts only multipart/form-data)
        if not isinstance(info, str):
            info = json.dumps(self.api_client.sanitize_for_serialization(info))
        return self.report_controller.create_report(file=file, info=info)

    def delete_report(self, report_id: ReportId) -> None:
        report_id = self.get_id(report_id)
        return self.report_controller.delete_report(report_id=report_id)

    def download_report(self, report_id: ReportId) -> bytes:
        report_id = self.get_id(report_id)
        return self.report_controller.download_report(report_id=report_id)

    def download_report_by_public_key(self, public_key: str) -> bytes:
        return self.report_controller.download_report_by_public_key(public_key=public_key)

    def get_report_by_id(self, report_id: ReportId) -> Report:
        report_id = self.get_id(report_id)
        return self.report_controller.get_report_by_id(report_id=report_id)

    def get_report_infos(self, page_size: int, page: int, report_template_id: Optional[ReportTemplateId] = None,
                         user_id: Optional[UserId] = None, include_customers: Optional[bool] = None,
                         text_search: Optional[str] = None, sort_property: Optional[str] = None,
                         sort_order: Optional[str] = None) -> PageDataReportInfo:
        report_template_id = self.get_id(report_template_id)
        user_id = self.get_id(user_id)
        return self.report_controller.get_report_infos(page_size=page_size, page=page,
                                                       report_template_id=report_template_id, user_id=user_id,
                                                       include_customers=include_customers, text_search=text_search,
                                                       sort_property=sort_property, sort_order=sort_order)

    def get_report_infos_by_ids(self, str_report_ids: List[str]) -> List[ReportInfo]:
        return self.report_controller.get_report_infos_by_ids(str_report_ids=str_report_ids)

    def get_reports(self, page_size: int, page: int, text_search: Optional[str] = None,
                    sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                    include_customers: Optional[bool] = None) -> PageDataReport:
        return self.report_controller.get_reports(page_size=page_size, page=page, text_search=text_search,
                                                  sort_property=sort_property, sort_order=sort_order,
                                                  include_customers=include_customers)

    def request_report(self, body: ReportRequest) -> Job:
        return self.report_controller.request_report(body=body)

    def update_report_public_status(self, report_id: ReportId, is_public: bool) -> Report:
        report_id = self.get_id(report_id)
        return self.report_controller.update_report_public_status(report_id=report_id, is_public=is_public)

    # Scheduler Event Controller
    def get_scheduler_events_all(self, type: Optional[str] = None) -> List[SchedulerEventWithCustomerInfo]:
        return self.scheduler_event_controller.get_all_scheduler_events(type=type)

    def get_scheduler_events_by_range(self, start_time: int, end_time: int, type: Optional[str] = None,
                                      edge_id: Optional[EdgeId] = None,
                                      text_search: Optional[str] = None) -> List[SchedulerEventWithCustomerInfo]:
        edge_id = self.get_id(edge_id)
        return self.scheduler_event_controller.get_scheduler_events_by_range(start_time=start_time, end_time=end_time,
                                                                             type=type, edge_id=edge_id,
                                                                             text_search=text_search)

    # Sign Up Controller
    def accept_privacy_policy(self) -> JsonNode:
        return self.sign_up_controller.accept_privacy_policy()

    # Solution Export Import Controller
    def export_solution(self, body: SolutionExportRequest) -> SolutionExportResponse:
        return self.solution_export_import_controller.export_solution(body=body)

    def import_solution(self, body: SolutionData) -> SolutionImportResult:
        return self.solution_export_import_controller.import_solution(body=body)

    def validate_solution(self, body: SolutionData) -> SolutionValidationResult:
        return self.solution_export_import_controller.validate_solution(body=body)

    # TB Resource Controller
    def get_resource_info(self, resource_type: str, scope: str, key: str) -> TbResourceInfo:
        return self.tb_resource_controller.get_resource_info(resource_type=resource_type, scope=scope, key=key)

    # User Controller
    def delete_general_user_settings(self, paths: str) -> None:
        return self.user_controller.delete_general_user_settings(paths=paths)

    def get_user_settings_by_type(self, type: str) -> JsonNode:
        return self.user_controller.get_user_settings(type=type)

    def put_user_settings_by_type(self, body: Any, type: str) -> None:
        return self.user_controller.put_user_settings(body=body, type=type)

    # White Labeling Controller
    def get_mail_templates(self, system_by_default: Optional[bool] = None) -> JsonNode:
        return self.white_labeling_controller.get_mail_templates(system_by_default=system_by_default)

    def save_mail_templates(self, body: Any) -> JsonNode:
        return self.white_labeling_controller.save_mail_templates(body=body)

    # Widgets Bundle Controller
    def get_all_widgets_bundles(self) -> List[WidgetsBundle]:
        return self.widgets_bundle_controller.get_all_widgets_bundles()
