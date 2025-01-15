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


from tb_rest_client.rest_client_base import *

logger = getLogger(__name__)


class RestClientCE(RestClientBase):
    def __init__(self, base_url):
        super().__init__(base_url)

    # O Auth 2 Config Template Controller
    def delete_client_registration_template(self, client_registration_template_id: EntityId) -> None:
        client_registration_template_id = self.get_id(client_registration_template_id)
        return self.o_auth2_config_template_controller.delete_client_registration_template_using_delete(
            client_registration_template_id=client_registration_template_id)

    def get_client_registration_templates(self) -> List[OAuth2ClientRegistrationTemplate]:
        return self.o_auth2_config_template_controller.get_client_registration_templates_using_get()

    def save_client_registration_template(self, body: Optional[
            OAuth2ClientRegistrationTemplate] = None) -> OAuth2ClientRegistrationTemplate:
        return self.o_auth2_config_template_controller.save_client_registration_template_using_post(body=body)

    # Asset Controller
    def assign_asset_to_edge(self, edge_id: EdgeId, asset_id: AssetId) -> Asset:
        edge_id = self.get_id(edge_id)
        asset_id = self.get_id(asset_id)
        return self.asset_controller.assign_asset_to_edge_using_post(edge_id=edge_id, asset_id=asset_id)

    def get_tenant_asset_infos(self, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None,
                               sort_property: Optional[str] = None,
                               sort_order: Optional[str] = None, asset_profile_id: Optional[AssetProfileId] = None) -> PageDataAssetInfo:

        if asset_profile_id:
            asset_profile_id = self.get_id(asset_profile_id)
        return self.asset_controller.get_tenant_asset_infos_using_get(page_size=page_size, page=page, type=type,
                                                                      text_search=text_search,
                                                                      sort_property=sort_property,
                                                                      sort_order=sort_order, asset_profile_id=asset_profile_id)

    def process_assets_bulk_import(self, body: BulkImportRequest) -> BulkImportResultAsset:
        return self.asset_controller.process_assets_bulk_import_using_post(body=body)

    def unassign_asset_from_edge(self, edge_id: EdgeId, asset_id: AssetId) -> Asset:
        edge_id = self.get_id(edge_id)
        asset_id = self.get_id(asset_id)
        return self.asset_controller.unassign_asset_from_edge_using_delete(edge_id=edge_id, asset_id=asset_id)

    def get_edge_assets(self, edge_id: EdgeId, page_size: int, page: int, type: Optional[str] = None,
                        text_search: Optional[str] = None,
                        sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None,
                        end_time: Optional[int] = None) -> PageDataAsset:
        edge_id = self.get_id(edge_id)
        return self.asset_controller.get_edge_assets_using_get(edge_id=edge_id, page_size=page_size, page=page,
                                                               type=type, text_search=text_search,
                                                               sort_property=sort_property, sort_order=sort_order,
                                                               start_time=start_time, end_time=end_time)

    def assign_asset_to_customer(self, customer_id: CustomerId, asset_id: AssetId) -> Asset:
        customer_id = self.get_id(customer_id)
        asset_id = self.get_id(asset_id)
        return self.asset_controller.assign_asset_to_customer_using_post(customer_id=customer_id, asset_id=asset_id)

    def unassign_asset_from_customer(self, asset_id: AssetId) -> Asset:
        asset_id = self.get_id(asset_id)
        return self.asset_controller.unassign_asset_from_customer_using_delete(asset_id=asset_id)

    def assign_asset_to_public_customer(self, asset_id: AssetId) -> Asset:
        asset_id = self.get_id(asset_id)
        return self.asset_controller.assign_asset_to_public_customer_using_post(asset_id=asset_id)

    def save_asset(self, body: Optional[Asset] = None) -> Asset:
        return self.asset_controller.save_asset_using_post(body=body)

    # Edge Controller
    def get_tenant_edge_infos(self, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None,
                              sort_property: Optional[str] = None,
                              sort_order: Optional[str] = None) -> PageDataEdgeInfo:
        return self.edge_controller.get_tenant_edge_infos_using_get(page_size=page_size, page=page, type=type,
                                                                    text_search=text_search,
                                                                    sort_property=sort_property, sort_order=sort_order)

    def get_edge_info_by_id(self, edge_id: EdgeId) -> EdgeInfo:
        edge_id = self.get_id(edge_id)
        return self.edge_controller.get_edge_info_by_id_using_get(edge_id=edge_id)

    def get_customer_edge_infos(self, customer_id: CustomerId, page_size: int, page: int, type: Optional[str] = None,
                                text_search: Optional[str] = None,
                                sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataEdgeInfo:
        customer_id = self.get_id(customer_id)
        return self.edge_controller.get_customer_edge_infos_using_get(customer_id=customer_id, page_size=page_size,
                                                                      page=page, type=type, text_search=text_search,
                                                                      sort_property=sort_property,
                                                                      sort_order=sort_order)

    def assign_edge_to_customer(self, customer_id: CustomerId, edge_id: EdgeId) -> Edge:
        customer_id = self.get_id(customer_id)
        edge_id = self.get_id(edge_id)
        return self.edge_controller.assign_edge_to_customer_using_post(customer_id=customer_id, edge_id=edge_id)

    def find_by_query_v2(self, body: Optional[EdgeSearchQuery] = None) -> List[Edge]:
        return self.edge_controller.find_by_query_using_post2(body=body)

    def get_tenant_edges(self, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None,
                         sort_property: Optional[str] = None,
                         sort_order: Optional[str] = None) -> PageDataEdge:
        return self.edge_controller.get_tenant_edges_using_get(page_size=page_size, page=page, type=type,
                                                               text_search=text_search, sort_property=sort_property,
                                                               sort_order=sort_order)

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

    def process_edges_bulk_import(self, body: Optional[BulkImportRequest] = None) -> BulkImportResultEdge:
        return self.edge_controller.process_edges_bulk_import_using_post(body=body)

    def activate_instance(self, license_secret: str, release_date: str) -> Union[
            dict, str, list, bytes, None, RESTResponse, tuple, Any]:
        return self.edge_controller.activate_instance_using_post(license_secret=license_secret,
                                                                 release_date=release_date)

    def get_tenant_edge(self, edge_name: str) -> Edge:
        return self.edge_controller.get_tenant_edge_using_get(edge_name=edge_name)

    def get_edge_by_id(self, edge_id: EdgeId) -> Edge:
        edge_id = self.get_id(edge_id)
        return self.edge_controller.get_edge_by_id_using_get(edge_id=edge_id)

    def delete_edge(self, edge_id: EdgeId) -> None:
        edge_id = self.get_id(edge_id)
        return self.edge_controller.delete_edge_using_delete(edge_id=edge_id)

    def save_edge(self, body: Optional[Edge] = None) -> Edge:
        return self.edge_controller.save_edge_using_post(body=body)

    def is_edges_support_enabled(self, ) -> bool:
        return self.edge_controller.is_edges_support_enabled_using_get()

    def get_edges(self, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None,
                  sort_order: Optional[str] = None) -> PageDataEdge:
        return self.edge_controller.get_edges_using_get(page_size=page_size, page=page, text_search=text_search,
                                                        sort_property=sort_property, sort_order=sort_order)

    def unassign_edge_from_customer(self, edge_id: EdgeId) -> Edge:
        edge_id = self.get_id(edge_id)
        return self.edge_controller.unassign_edge_from_customer_using_delete(edge_id=edge_id)

    def assign_edge_to_public_customer(self, edge_id: EdgeId) -> Edge:
        edge_id = self.get_id(edge_id)
        return self.edge_controller.assign_edge_to_public_customer_using_post(edge_id=edge_id)

    def get_edge_types(self, ) -> List[EntitySubtype]:
        return self.edge_controller.get_edge_types_using_get()

    def set_edge_root_rule_chain(self, edge_id: EdgeId, rule_chain_id: RuleChainId) -> Edge:
        edge_id = self.get_id(edge_id)
        rule_chain_id = self.get_id(rule_chain_id)
        return self.edge_controller.set_edge_root_rule_chain_using_post(edge_id=edge_id, rule_chain_id=rule_chain_id)

    def get_edges_by_ids(self, edge_ids: list) -> List[Edge]:
        return self.edge_controller.get_edges_by_ids_using_get(edge_ids=edge_ids)

    # Rule Chain Controller
    def export_rule_chains(self, limit: int) -> RuleChainData:
        return self.rule_chain_controller.export_rule_chains_using_get(limit=limit)

    def delete_rule_chain(self, rule_chain_id: RuleChainId) -> None:
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.delete_rule_chain_using_delete(rule_chain_id=rule_chain_id)

    def set_edge_template_root_rule_chain(self, rule_chain_id: RuleChainId) -> RuleChain:
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.set_edge_template_root_rule_chain_using_post(rule_chain_id=rule_chain_id)

    def save_rule_chain(self, body: Optional[DefaultRuleChainCreateRequest] = None) -> RuleChain:
        return self.rule_chain_controller.save_rule_chain_using_post(body=body)

    def assign_rule_chain_to_edge(self, edge_id: EdgeId, rule_chain_id: RuleChainId) -> RuleChain:
        edge_id = self.get_id(edge_id)
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.assign_rule_chain_to_edge_using_post(edge_id=edge_id,
                                                                               rule_chain_id=rule_chain_id)

    def unassign_rule_chain_from_edge(self, edge_id: EdgeId, rule_chain_id: RuleChainId) -> RuleChain:
        edge_id = self.get_id(edge_id)
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.unassign_rule_chain_from_edge_using_delete(edge_id=edge_id,
                                                                                     rule_chain_id=rule_chain_id)

    def unset_auto_assign_to_edge_rule_chain(self, rule_chain_id: RuleChainId) -> RuleChain:
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.unset_auto_assign_to_edge_rule_chain_using_delete(rule_chain_id=rule_chain_id)

    def get_rule_chain_by_id(self, rule_chain_id: RuleChainId) -> RuleChain:
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.get_rule_chain_by_id_using_get(rule_chain_id=rule_chain_id)

    def test_script(self, body: Union[dict, str, list, bytes, None, RESTResponse, tuple, Any] = None) -> Union[
            dict, str, list, bytes, None, RESTResponse, tuple, Any]:
        return self.rule_chain_controller.test_script_using_post(body=body)

    def save_rule_chain_v1(self, body: Optional[RuleChain] = None) -> RuleChain:
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

    def import_rule_chains(self, body: Optional[RuleChainData] = None, overwrite: Optional[bool] = None) -> List[
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

    def get_auto_assign_to_edge_rule_chains(self, ) -> List[RuleChain]:
        return self.rule_chain_controller.get_auto_assign_to_edge_rule_chains_using_get()

    def get_latest_rule_node_debug_input(self, rule_node_id: RuleNodeId) -> Union[
            dict, str, list, bytes, None, RESTResponse, tuple, Any]:
        rule_node_id = self.get_id(rule_node_id)
        return self.rule_chain_controller.get_latest_rule_node_debug_input_using_get(rule_node_id=rule_node_id)

    def get_rule_chain_meta_data(self, rule_chain_id: RuleChainId) -> RuleChainMetaData:
        rule_chain_id = self.get_id(rule_chain_id)
        return self.rule_chain_controller.get_rule_chain_meta_data_using_get(rule_chain_id=rule_chain_id)

    # Auth Controller
    def get_user(self, ) -> User:
        return self.auth_controller.get_user_using_get()

    def change_password(self, body: Optional[ChangePasswordRequest] = None) -> ObjectNode:
        return self.auth_controller.change_password_using_post(body=body)

    def logout(self, ) -> None:
        return self.auth_controller.logout_using_post()

    def check_reset_token(self, reset_token: str) -> str:
        return self.auth_controller.check_reset_token_using_get(reset_token=reset_token)

    def get_user_password_policy(self, ) -> UserPasswordPolicy:
        return self.auth_controller.get_user_password_policy_using_get()

    def check_activate_token(self, activate_token: str) -> str:
        return self.auth_controller.check_activate_token_using_get(activate_token=activate_token)

    def request_reset_password_by_email(self, body: Optional[ResetPasswordEmailRequest] = None) -> None:
        return self.auth_controller.request_reset_password_by_email_using_post(body=body)

    # Event Controller
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

    # Telemetry Controller
    def get_attribute_keys_by_scope(self, entity_id: EntityId, scope: str):
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.get_attribute_keys_by_scope_using_get(entity_type=entity_type,
                                                                               entity_id=entity_id, scope=scope)

    def delete_device_attributes(self, device_id: DeviceId, scope: str, keys: str):
        device_id = self.get_id(device_id)
        return self.telemetry_controller.delete_device_attributes_using_delete(device_id=device_id, scope=scope,
                                                                               keys=keys)

    def save_entity_attributes_v1(self, entity_id: EntityId, scope: str,
                                  body: Union[dict, str, list, bytes, None, RESTResponse, tuple, Any] = None) -> Union[
            dict, str, list, bytes, None, RESTResponse, tuple, Any]:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.telemetry_controller.save_entity_attributes_v1_using_post(entity_type=entity_type,
                                                                              entity_id=entity_id, scope=scope,
                                                                              body=body)

    def save_device_attributes(self, device_id: DeviceId, scope: str,
                               body: Union[dict, str, list, bytes, None, RESTResponse, tuple, Any] = None) -> Union[
            dict, str, list, bytes, None, RESTResponse, tuple, Any]:
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
                                  body: Union[dict, str, list, bytes, None, RESTResponse, tuple, Any] = None) -> Union[
            dict, str, list, bytes, None, RESTResponse, tuple, Any]:
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
    def clear_alarm(self, alarm_id: AlarmId) -> None:
        alarm_id = self.get_id(alarm_id)
        return self.alarm_controller.clear_alarm_using_post(alarm_id=alarm_id)

    # RPC v2 Controller
    def get_persisted_rpc(self, rpc_id: RpcId) -> Rpc:
        rpc_id = self.get_id(rpc_id)
        return self.rpc_v2_controller.get_persisted_rpc_using_get(rpc_id=rpc_id)

    def handle_one_way_device_rpc_request_v1(self, device_id: DeviceId,
                                             body: Optional[str] = None):
        device_id = self.get_id(device_id)
        return self.rpc_v2_controller.handle_one_way_device_rpc_request_using_post1(device_id=device_id, body=body)

    def handle_two_way_device_rpc_request_v1(self, device_id: DeviceId,
                                             body: Optional[str] = None):
        device_id = self.get_id(device_id)
        return self.rpc_v2_controller.handle_two_way_device_rpc_request_using_post1(device_id=device_id, body=body)

    def get_persisted_rpc_by_device(self, device_id: DeviceId, page_size: int, page: int, rpc_status: Optional[str] = None,
                                    text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                    sort_order: Optional[str] = None):
        device_id = self.get_id(device_id)
        return self.rpc_v2_controller.get_persisted_rpc_by_device_using_get(device_id=device_id, page_size=page_size,
                                                                            page=page, rpc_status=rpc_status,
                                                                            text_search=text_search,
                                                                            sort_property=sort_property,
                                                                            sort_order=sort_order)

    def delete_resource(self, rpc_id: RpcId) -> None:
        rpc_id = self.get_id(rpc_id)
        return self.rpc_v2_controller.delete_resource_using_delete(rpc_id=rpc_id)

    # Edge Event Controller
    def get_edge_events(self, edge_id: EdgeId, page_size: int, page: int, text_search: Optional[str] = None,
                        sort_property: Optional[str] = None,
                        sort_order: Optional[str] = None, start_time: Optional[int] = None,
                        end_time: Optional[int] = None) -> PageDataEdgeEvent:
        edge_id = self.get_id(edge_id)
        return self.edge_event_controller.get_edge_events_using_get(edge_id=edge_id, page_size=page_size, page=page,
                                                                    text_search=text_search,
                                                                    sort_property=sort_property, sort_order=sort_order,
                                                                    start_time=start_time, end_time=end_time)

    # Customer Controller
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

    def save_customer(self, body: Optional[Customer] = None) -> Customer:
        return self.customer_controller.save_customer_using_post(body=body)

    def get_tenant_customer(self, customer_title: str) -> Customer:
        return self.customer_controller.get_tenant_customer_using_get(customer_title=customer_title)

    def delete_customer(self, customer_id: CustomerId) -> None:
        customer_id = self.get_id(customer_id)
        return self.customer_controller.delete_customer_using_delete(customer_id=customer_id)

    # User Controller
    def get_user_token(self, user_id: UserId) -> JwtPair:
        user_id = self.get_id(user_id)
        return self.user_controller.get_user_token_using_get(user_id=user_id)

    def get_activation_link(self, user_id: UserId) -> str:
        user_id = self.get_id(user_id)
        return self.user_controller.get_activation_link_using_get(user_id=user_id)

    def delete_user(self, user_id: UserId) -> None:
        user_id = self.get_id(user_id)
        return self.user_controller.delete_user_using_delete(user_id=user_id)

    def get_users(self, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None,
                  sort_order: Optional[str] = None) -> PageDataUser:
        return self.user_controller.get_users_using_get(page_size=page_size, page=page, text_search=text_search,
                                                        sort_property=sort_property, sort_order=sort_order)

    def set_user_credentials_enabled(self, user_id: UserId, user_credentials_enabled: Optional[bool] = None) -> None:
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

    def is_user_token_access_enabled(self, ) -> bool:
        return self.user_controller.is_user_token_access_enabled_using_get()

    def save_user(self, body: Optional[User] = None, send_activation_mail: Optional[bool] = None) -> User:
        return self.user_controller.save_user_using_post(body=body, send_activation_mail=send_activation_mail)

    def send_activation_email(self, email: str) -> None:
        return self.user_controller.send_activation_email_using_post(email=email)

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
    def get_device_types(self, ) -> List[EntitySubtype]:
        return self.device_controller.get_device_types_using_get()

    def process_devices_bulk_import(self, body: Optional[BulkImportRequest] = None) -> BulkImportResultDevice:
        return self.device_controller.process_devices_bulk_import_using_post(body=body)

    def count_by_device_profile_and_empty_ota_package(self, ota_package_type: str,
                                                      device_profile_id: DeviceProfileId) -> int:
        device_profile_id = self.get_id(device_profile_id)
        return self.device_controller.count_by_device_profile_and_empty_ota_package_using_get(
            ota_package_type=ota_package_type, device_profile_id=device_profile_id)

    def get_devices_by_ids(self, device_ids: list) -> List[Device]:
        device_ids = ','.join(device_ids)
        return self.device_controller.get_devices_by_ids_using_get(device_ids=device_ids)

    def save_device_with_credentials(self, body: Optional[SaveDeviceWithCredentialsRequest] = None) -> Device:
        return self.device_controller.save_device_with_credentials_using_post(body=body)

    def update_device_credentials(self, body: Optional[DeviceCredentials] = None) -> DeviceCredentials:
        return self.device_controller.update_device_credentials_using_post(body=body)

    def save_device(self, body: Optional[Device] = None, access_token: Optional[str] = None) -> Device:
        return self.device_controller.save_device_using_post(body=body, access_token=access_token)

    def assign_device_to_public_customer(self, device_id: DeviceId) -> Device:
        device_id = self.get_id(device_id)
        return self.device_controller.assign_device_to_public_customer_using_post(device_id=device_id)

    def unassign_device_from_customer(self, device_id: DeviceId) -> Device:
        device_id = self.get_id(device_id)
        return self.device_controller.unassign_device_from_customer_using_delete(device_id=device_id)

    def get_device_by_id(self, device_id: DeviceId) -> Device:
        device_id = self.get_id(device_id)
        return self.device_controller.get_device_by_id_using_get(device_id=device_id)

    def get_tenant_device_infos(self, page_size: int, page: int, type: Optional[str] = None,
                                device_profile_id: Optional[DeviceProfileId] = None, text_search: Optional[str] = None,
                                sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                                active: Optional[bool] = None) -> PageDataDeviceInfo:
        device_profile_id = self.get_id(device_profile_id)
        return self.device_controller.get_tenant_device_infos_using_get(page_size=page_size, page=page, type=type,
                                                                        device_profile_id=device_profile_id,
                                                                        text_search=text_search,
                                                                        sort_property=sort_property,
                                                                        sort_order=sort_order, active=active)

    def get_customer_device_infos(self, customer_id: CustomerId, page_size: int, page: int, type: Optional[str] = None,
                                  device_profile_id: Optional[DeviceProfileId] = None,
                                  text_search: Optional[str] = None,
                                  sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                                  active: Optional[bool] = None) -> PageDataDeviceInfo:
        customer_id = self.get_id(customer_id)
        device_profile_id = self.get_id(device_profile_id)
        return self.device_controller.get_customer_device_infos_using_get(customer_id=customer_id, page_size=page_size,
                                                                          page=page, type=type,
                                                                          device_profile_id=device_profile_id,
                                                                          text_search=text_search,
                                                                          sort_property=sort_property,
                                                                          sort_order=sort_order, active=active)

    def get_tenant_devices(self, page_size: int, page: int, type: Optional[str] = None,
                           text_search: Optional[str] = None,
                           sort_property: Optional[str] = None,
                           sort_order: Optional[str] = None) -> PageDataDevice:
        return self.device_controller.get_tenant_devices_using_get(page_size=page_size, page=page, type=type,
                                                                   text_search=text_search, sort_property=sort_property,
                                                                   sort_order=sort_order)

    def get_customer_devices(self, customer_id: CustomerId, page_size: int, page: int, type: Optional[str] = None,
                             text_search: Optional[str] = None,
                             sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataDevice:
        customer_id = self.get_id(customer_id)
        return self.device_controller.get_customer_devices_using_get(customer_id=customer_id, page_size=page_size,
                                                                     page=page, type=type, text_search=text_search,
                                                                     sort_property=sort_property, sort_order=sort_order)

    def unassign_device_from_edge(self, edge_id: EdgeId, device_id: DeviceId) -> Device:
        edge_id = self.get_id(edge_id)
        device_id = self.get_id(device_id)
        return self.device_controller.unassign_device_from_edge_using_delete(edge_id=edge_id, device_id=device_id)

    def assign_device_to_tenant(self, tenant_id: TenantId, device_id: DeviceId) -> Device:
        tenant_id = self.get_id(tenant_id)
        device_id = self.get_id(device_id)
        return self.device_controller.assign_device_to_tenant_using_post(tenant_id=tenant_id, device_id=device_id)

    def assign_device_to_edge(self, edge_id: EdgeId, device_id: DeviceId) -> Device:
        edge_id = self.get_id(edge_id)
        device_id = self.get_id(device_id)
        return self.device_controller.assign_device_to_edge_using_post(edge_id=edge_id, device_id=device_id)

    def delete_device(self, device_id: DeviceId) -> None:
        device_id = self.get_id(device_id)
        return self.device_controller.delete_device_using_delete(device_id=device_id)

    def re_claim_device(self, device_name: str):
        return self.device_controller.re_claim_device_using_delete(device_name=device_name)

    def assign_device_to_customer(self, customer_id: CustomerId, device_id: DeviceId) -> Device:
        customer_id = self.get_id(customer_id)
        device_id = self.get_id(device_id)
        return self.device_controller.assign_device_to_customer_using_post(customer_id=customer_id, device_id=device_id)

    def get_edge_devices(self, edge_id: EdgeId, page_size: int, page: int, type: Optional[str] = None,
                         text_search: Optional[str] = None,
                         sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None,
                         end_time: Optional[int] = None, device_profile_id: Optional[DeviceProfileId] = None, active: Optional[bool] = None) -> PageDataDevice:
        edge_id = self.get_id(edge_id)

        if device_profile_id:
            device_profile_id = self.get_id(device_profile_id)
        return self.device_controller.get_edge_devices_using_get(edge_id=edge_id, page_size=page_size, page=page,
                                                                 type=type, text_search=text_search,
                                                                 sort_property=sort_property, sort_order=sort_order,
                                                                 start_time=start_time, end_time=end_time, device_profile_id=device_profile_id, active=active)

    def get_tenant_device(self, device_name: str) -> Device:
        return self.device_controller.get_tenant_device_using_get(device_name=device_name)

    def get_device_credentials_by_device_id(self, device_id: DeviceId) -> DeviceCredentials:
        device_id = self.get_id(device_id)
        return self.device_controller.get_device_credentials_by_device_id_using_get(device_id=device_id)

    # Entity View Controller
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

    def find_by_from_v1(self, from_id: EntityId, from_type: str,
                        relation_type_group: Optional[str] = None) -> List[EntityRelation]:
        from_id = self.get_id(from_id)
        return self.entity_relation_controller.find_by_from_using_get1(from_id=from_id, from_type=from_type,
                                                                       relation_type_group=relation_type_group)

    def save_relation(self, body: Optional[EntityRelation] = None) -> None:
        return self.entity_relation_controller.save_relation_using_post(body=body)

    def find_by_to(self, to_id: EntityId, relation_type: str,
                   relation_type_group: Optional[str] = None) -> List[EntityRelation]:
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

    def find_by_from(self, from_id: EntityId, relation_type: str,
                     relation_type_group: Optional[str] = None) -> List[EntityRelation]:
        from_type = self.get_type(from_id)
        from_id = self.get_id(from_id)
        return self.entity_relation_controller.find_by_from_using_get(from_id=from_id, from_type=from_type,
                                                                      relation_type=relation_type,
                                                                      relation_type_group=relation_type_group)

    def assign_entity_view_to_edge(self, edge_id: EdgeId, entity_view_id: EntityViewId) -> EntityView:
        edge_id = self.get_id(edge_id)
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.assign_entity_view_to_edge_using_post(edge_id=edge_id,
                                                                                 entity_view_id=entity_view_id)

    def get_entity_view_types(self, ) -> List[EntitySubtype]:
        return self.entity_view_controller.get_entity_view_types_using_get()

    def delete_entity_view(self, entity_view_id: EntityViewId) -> None:
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.delete_entity_view_using_delete(entity_view_id=entity_view_id)

    def assign_entity_view_to_customer(self, customer_id: CustomerId, entity_view_id: EntityViewId) -> EntityView:
        customer_id = self.get_id(customer_id)
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.assign_entity_view_to_customer_using_post(customer_id=customer_id,
                                                                                     entity_view_id=entity_view_id)

    def get_entity_view_by_id(self, entity_view_id: EntityViewId) -> EntityView:
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.get_entity_view_by_id_using_get(entity_view_id=entity_view_id)

    def get_customer_entity_view_infos(self, customer_id: CustomerId, page_size: int, page: int, type: Optional[str] = None,
                                       text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                       sort_order: Optional[str] = None) -> PageDataEntityViewInfo:
        customer_id = self.get_id(customer_id)
        return self.entity_view_controller.get_customer_entity_view_infos_using_get(customer_id=customer_id,
                                                                                    page_size=page_size, page=page,
                                                                                    type=type, text_search=text_search,
                                                                                    sort_property=sort_property,
                                                                                    sort_order=sort_order)

    def get_tenant_entity_view_infos(self, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None,
                                     sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataEntityViewInfo:
        return self.entity_view_controller.get_tenant_entity_view_infos_using_get(page_size=page_size, page=page,
                                                                                  type=type, text_search=text_search,
                                                                                  sort_property=sort_property,
                                                                                  sort_order=sort_order)

    def get_tenant_entity_view(self, entity_view_name: str) -> EntityView:
        return self.entity_view_controller.get_tenant_entity_view_using_get(entity_view_name=entity_view_name)

    def get_edge_entity_views(self, edge_id: EdgeId, page: int, page_size: int, type: Optional[str] = None,
                              text_search: Optional[str] = None,
                              sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None,
                              end_time: Optional[int] = None) -> PageDataEntityView:
        edge_id = self.get_id(edge_id)
        return self.entity_view_controller.get_edge_entity_views_using_get(edge_id=edge_id, page=page,
                                                                           page_size=page_size, type=type,
                                                                           text_search=text_search,
                                                                           sort_property=sort_property,
                                                                           sort_order=sort_order, start_time=start_time,
                                                                           end_time=end_time)

    def unassign_entity_view_from_customer(self, entity_view_id: EntityViewId) -> EntityView:
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.unassign_entity_view_from_customer_using_delete(
            entity_view_id=entity_view_id)

    def save_entity_view(self, body: Optional[EntityView] = None) -> EntityView:
        return self.entity_view_controller.save_entity_view_using_post(body=body)

    def unassign_entity_view_from_edge(self, edge_id: EdgeId, entity_view_id: EntityViewId) -> EntityView:
        edge_id = self.get_id(edge_id)
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.unassign_entity_view_from_edge_using_delete(edge_id=edge_id,
                                                                                       entity_view_id=entity_view_id)

    def get_tenant_entity_views(self, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None,
                                sort_property: Optional[str] = None,
                                sort_order: Optional[str] = None) -> PageDataEntityView:
        return self.entity_view_controller.get_tenant_entity_views_using_get(page_size=page_size, page=page, type=type,
                                                                             text_search=text_search,
                                                                             sort_property=sort_property,
                                                                             sort_order=sort_order)

    def assign_entity_view_to_public_customer(self, entity_view_id: EntityViewId) -> EntityView:
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.assign_entity_view_to_public_customer_using_post(
            entity_view_id=entity_view_id)

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
    def get_admin_settings(self, key: str) -> AdminSettings:
        return self.admin_controller.get_admin_settings_using_get(key=key)

    # TB Resource Controller
    def get_resource_info_by_id(self, resource_id: EntityId) -> TbResourceInfo:
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.get_resource_info_by_id_using_get(resource_id=resource_id)

    def delete_resource_v1(self, resource_id: EntityId) -> None:
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.delete_resource_using_delete1(resource_id=resource_id)

    def get_resource_by_id(self, resource_id: EntityId) -> TbResource:
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.get_resource_by_id_using_get(resource_id=resource_id)

    def save_resource(self, body=None):
        return self.tb_resource_controller.save_resource_using_post(body=body)

    def get_resources(self, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None,
                      sort_order: Optional[str] = None) -> PageDataTbResourceInfo:
        return self.tb_resource_controller.get_resources_using_get(page_size=page_size, page=page,
                                                                   text_search=text_search, sort_property=sort_property,
                                                                   sort_order=sort_order)

    def get_lwm2m_list_objects(self, sort_order: str, sort_property: str, object_ids: list) -> List[LwM2mObject]:
        return self.tb_resource_controller.get_lwm2m_list_objects_using_get(sort_order=sort_order,
                                                                            sort_property=sort_property,
                                                                            object_ids=object_ids)

    def download_resource(self, resource_id: EntityId) -> Resource:
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.download_resource_using_get(resource_id=resource_id)

    def get_lwm2m_list_objects_page(self, page_size: int, page: int, text_search: Optional[str] = None,
                                    sort_property: Optional[str] = None,
                                    sort_order: Optional[str] = None) -> List[LwM2mObject]:
        return self.tb_resource_controller.get_lwm2m_list_objects_page_using_get(page_size=page_size, page=page,
                                                                                 text_search=text_search,
                                                                                 sort_property=sort_property,
                                                                                 sort_order=sort_order)

    def get_features_info(self) -> FeaturesInfo:
        return self.admin_controller.get_features_info_using_get()

    def get_system_info(self) -> SystemInfo:
        return self.admin_controller.get_system_info_using_get()

    # O Auth 2 Controller
    def get_login_processing_url(self, ) -> str:
        return self.o_auth2_controller.get_login_processing_url_using_get()

    def save_o_auth2_info(self, body: Optional[OAuth2Info] = None) -> OAuth2Info:
        return self.o_auth2_controller.save_o_auth2_info_using_post(body=body)

    def get_o_auth2_clients(self, pkg_name: Optional[str] = None, platform: Optional[str] = None) -> List[OAuth2ClientInfo]:
        return self.o_auth2_controller.get_o_auth2_clients_using_post(pkg_name=pkg_name, platform=platform)

    def get_current_o_auth2_info(self, ) -> OAuth2Info:
        return self.o_auth2_controller.get_current_o_auth2_info_using_get()

    # Tenant Profile Controller
    def get_default_tenant_profile_info(self, ) -> EntityInfo:
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
    def save_widgets_bundle(self, body: Optional[WidgetsBundle] = None) -> WidgetsBundle:
        return self.widgets_bundle_controller.save_widgets_bundle_using_post(body=body)

    def delete_widgets_bundle(self, widgets_bundle_id: WidgetsBundleId) -> None:
        widgets_bundle_id = self.get_id(widgets_bundle_id)
        return self.widgets_bundle_controller.delete_widgets_bundle_using_delete(widgets_bundle_id=widgets_bundle_id)

    def get_widgets_bundles(self, ) -> List[WidgetsBundle]:
        return self.widgets_bundle_controller.get_widgets_bundles_using_get()

    # Device Profile Controller
    def get_device_profile_infos(self, page_size: int, page: int, text_search: Optional[str] = None,
                                 sort_property: Optional[str] = None,
                                 sort_order: Optional[str] = None, transport_type: Optional[str] = None) -> PageDataDeviceProfileInfo:
        return self.device_profile_controller.get_device_profile_infos_using_get(page_size=page_size, page=page,
                                                                                 text_search=text_search,
                                                                                 sort_property=sort_property,
                                                                                 sort_order=sort_order,
                                                                                 transport_type=transport_type)

    def set_default_device_profile(self, device_profile_id: DeviceProfileId) -> DeviceProfile:
        device_profile_id = self.get_id(device_profile_id)
        return self.device_profile_controller.set_default_device_profile_using_post(device_profile_id=device_profile_id)

    def get_attributes_keys(self, device_profile_id: Optional[DeviceProfileId] = None) -> List[str]:
        device_profile_id = self.get_id(device_profile_id)
        return self.device_profile_controller.get_attributes_keys_using_get(device_profile_id=device_profile_id)

    def delete_device_profile(self, device_profile_id: DeviceProfileId) -> None:
        device_profile_id = self.get_id(device_profile_id)
        return self.device_profile_controller.delete_device_profile_using_delete(device_profile_id=device_profile_id)

    def save_device_profile(self, body: Optional[DeviceProfile] = None) -> DeviceProfile:
        return self.device_profile_controller.save_device_profile_using_post(body=body)

    def get_default_device_profile_info(self, ) -> DeviceProfileInfo:
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

    # Dashboard Controller
    def add_dashboard_customers(self, dashboard_id: DashboardId, body: Optional[List[str]] = None) -> Dashboard:
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.add_dashboard_customers_using_post(dashboard_id=dashboard_id, body=body)

    def assign_dashboard_to_edge(self, edge_id: EdgeId, dashboard_id: DashboardId) -> Dashboard:
        edge_id = self.get_id(edge_id)
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.assign_dashboard_to_edge_using_post(edge_id=edge_id, dashboard_id=dashboard_id)

    def remove_dashboard_customers(self, dashboard_id: DashboardId, body: Optional[List[str]] = None) -> Dashboard:
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.remove_dashboard_customers_using_post(dashboard_id=dashboard_id, body=body)

    def get_server_time(self, ) -> int:
        return self.dashboard_controller.get_server_time_using_get()

    def assign_dashboard_to_public_customer(self, dashboard_id: DashboardId) -> Dashboard:
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.assign_dashboard_to_public_customer_using_post(dashboard_id=dashboard_id)

    def delete_dashboard(self, dashboard_id: DashboardId) -> None:
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.delete_dashboard_using_delete(dashboard_id=dashboard_id)

    def update_dashboard_customers(self, dashboard_id: DashboardId, body: Optional[List[str]] = None) -> Dashboard:
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.update_dashboard_customers_using_post(dashboard_id=dashboard_id, body=body)

    def unassign_dashboard_from_public_customer(self, dashboard_id: DashboardId) -> Dashboard:
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.unassign_dashboard_from_public_customer_using_delete(dashboard_id=dashboard_id)

    def save_dashboard(self, body: Optional[Dashboard] = None) -> Dashboard:
        return self.dashboard_controller.save_dashboard_using_post(body=body)

    def get_home_dashboard_info(self, ) -> HomeDashboardInfo:
        return self.dashboard_controller.get_home_dashboard_info_using_get()

    def get_tenant_home_dashboard_info(self, ) -> HomeDashboardInfo:
        return self.dashboard_controller.get_tenant_home_dashboard_info_using_get()

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

    def unassign_dashboard_from_edge(self, edge_id: EdgeId, dashboard_id: DashboardId) -> Dashboard:
        edge_id = self.get_id(edge_id)
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.unassign_dashboard_from_edge_using_delete(edge_id=edge_id,
                                                                                   dashboard_id=dashboard_id)

    def get_home_dashboard(self, ) -> HomeDashboard:
        return self.dashboard_controller.get_home_dashboard_using_get()

    def get_max_datapoints_limit(self, ) -> int:
        return self.dashboard_controller.get_max_datapoints_limit_using_get()

    def get_tenant_dashboards(self, page_size: int, page: int, mobile: Optional[bool] = None, text_search: Optional[str] = None,
                              sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataDashboardInfo:
        return self.dashboard_controller.get_tenant_dashboards_using_get(page_size=page_size, page=page, mobile=mobile,
                                                                         text_search=text_search,
                                                                         sort_property=sort_property,
                                                                         sort_order=sort_order)

    def assign_dashboard_to_customer(self, customer_id: CustomerId, dashboard_id: DashboardId) -> Dashboard:
        customer_id = self.get_id(customer_id)
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.assign_dashboard_to_customer_using_post(customer_id=customer_id,
                                                                                 dashboard_id=dashboard_id)

    def set_tenant_home_dashboard_info(self, body: Optional[HomeDashboardInfo] = None) -> None:
        return self.dashboard_controller.set_tenant_home_dashboard_info_using_post(body=body)

    def get_edge_dashboards(self, edge_id: EdgeId, page_size: int, page: int, text_search: Optional[str] = None,
                            sort_property: Optional[str] = None,
                            sort_order: Optional[str] = None) -> PageDataDashboardInfo:
        edge_id = self.get_id(edge_id)
        return self.dashboard_controller.get_edge_dashboards_using_get(edge_id=edge_id, page_size=page_size, page=page,
                                                                       text_search=text_search,
                                                                       sort_property=sort_property,
                                                                       sort_order=sort_order)

    def unassign_dashboard_from_customer(self, customer_id: CustomerId, dashboard_id: DashboardId) -> Dashboard:
        customer_id = self.get_id(customer_id)
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.unassign_dashboard_from_customer_using_delete(customer_id=customer_id,
                                                                                       dashboard_id=dashboard_id)

    # Entity Query Controller
    def find_alarm_data_by_query(self, body: Optional[AlarmDataQuery] = None) -> PageDataAlarmData:
        return self.entity_query_controller.find_alarm_data_by_query_using_post(body=body)

    def find_entity_data_by_query(self, body: Optional[EntityDataQuery] = None) -> PageDataEntityData:
        return self.entity_query_controller.find_entity_data_by_query_using_post(body=body)

    # Widget Type Controller
    def delete_widget_type(self, widget_type_id: WidgetTypeId) -> None:
        widget_type_id = self.get_id(widget_type_id)
        return self.widget_type_controller.delete_widget_type_using_delete(widget_type_id=widget_type_id)

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
                                  sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                                  start_time: Optional[int] = None, end_time: Optional[int] = None,
                                  action_types: Optional[str] = None) -> PageDataAuditLog:
        user_id = self.get_id(user_id)
        return self.audit_log_controller.get_audit_logs_by_user_id_using_get(user_id=user_id, page_size=page_size,
                                                                             page=page, text_search=text_search,
                                                                             sort_property=sort_property,
                                                                             sort_order=sort_order,
                                                                             start_time=start_time, end_time=end_time,
                                                                             action_types=action_types)

    def get_audit_logs_by_entity_id(self, entity_id: EntityId, page_size: int, page: int,
                                    text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                                    start_time: Optional[int] = None, end_time: Optional[int] = None,
                                    action_types: Optional[str] = None) -> PageDataAuditLog:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.audit_log_controller.get_audit_logs_by_entity_id_using_get(entity_type=entity_type,
                                                                               entity_id=entity_id, page_size=page_size,
                                                                               page=page, text_search=text_search,
                                                                               sort_property=sort_property,
                                                                               sort_order=sort_order,
                                                                               start_time=start_time, end_time=end_time,
                                                                               action_types=action_types)

    # Lwm2m Controller
    def get_lwm2m_bootstrap_security_info(self, is_bootstrap_server: bool):
        return self.lwm2m_controller.get_lwm2m_bootstrap_security_info_using_get(
            is_bootstrap_server=is_bootstrap_server)

    # UI Controller
    def get_help_base_url(self, ) -> str:
        return self.ui_settings_controller.get_help_base_url_using_get()

    # Component Descriptor Controller
    def get_component_descriptors_by_types(self, component_types: str, rule_chain_type: Optional[str] = None) -> List[
        ComponentDescriptor]:
        return self.component_descriptor_controller.get_component_descriptors_by_types_using_get(
            component_types=component_types, rule_chain_type=rule_chain_type)

    def get_component_descriptor_by_clazz(self, component_descriptor_clazz: str) -> ComponentDescriptor:
        return self.component_descriptor_controller.get_component_descriptor_by_clazz_using_get(
            component_descriptor_clazz=component_descriptor_clazz)

    def get_component_descriptors_by_type(self, component_type: str, rule_chain_type: Optional[str] = None) -> List[
        ComponentDescriptor]:
        return self.component_descriptor_controller.get_component_descriptors_by_type_using_get(
            component_type=component_type, rule_chain_type=rule_chain_type)

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

    def get_ota_packages_v1(self, device_profile_id: DeviceProfileId, type: str, page_size: int, page: int,
                            text_search: Optional[str] = None, sort_property: Optional[str] = None,
                            sort_order: Optional[str] = None) -> PageDataOtaPackageInfo:
        device_profile_id = self.get_id(device_profile_id)
        return self.ota_package_controller.get_ota_packages_using_get1(device_profile_id=device_profile_id, type=type,
                                                                       page_size=page_size, page=page,
                                                                       text_search=text_search,
                                                                       sort_property=sort_property,
                                                                       sort_order=sort_order)

    def save_ota_package_data(self, ota_package_id: OtaPackageId, checksum: Optional[str] = None,
                              checksum_algorithm: Optional[str] = None, file: Optional[str] = None) -> OtaPackageInfo:
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.save_ota_package_data_using_post(ota_package_id=ota_package_id,
                                                                            checksum=checksum,
                                                                            checksum_algorithm=checksum_algorithm,
                                                                            file=file)

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

    def assign_alarm(self, alarm_id: AlarmId, assignee_id: str) -> Alarm:
        alarm_id = self.get_id(alarm_id)
        return self.alarm_controller.assign_alarm_using_post(alarm_id=alarm_id, assignee_id=assignee_id)

    # Asset Profile Controller
    def delete_asset_profile(self, asset_profile_id: str):
        return self.asset_profile_controller.delete_asset_profile_using_delete(asset_profile_id=asset_profile_id)

    def get_asset_profile_info_by_id(self, asset_profile_id: str) -> AssetProfileInfo:
        return self.asset_profile_controller.get_asset_profile_info_by_id_using_get(asset_profile_id=asset_profile_id)

    def get_asset_profile_infos(self, page_size: int, page: int, text_search: Optional[str] = None,
                                sort_property: Optional[str] = None,
                                sort_order: Optional[str] = None) -> PageDataAssetProfileInfo:
        return self.asset_profile_controller.get_asset_profile_infos_using_get(page_size=page_size,
                                                                               page=page,
                                                                               text_search=text_search,
                                                                               sort_property=sort_property,
                                                                               sort_order=sort_order)

    def get_asset_profiles(self, page_size: int, page: int, text_search: Optional[str] = None,
                           sort_property: Optional[str] = None,
                           sort_order: Optional[str] = None) -> PageDataAssetProfile:
        return self.asset_profile_controller.get_asset_profiles_using_get(page_size=page_size,
                                                                          page=page,
                                                                          text_search=text_search,
                                                                          sort_property=sort_property,
                                                                          sort_order=sort_order)

    def get_default_asset_profile_info(self) -> AssetProfileInfo:
        return self.asset_profile_controller.get_default_asset_profile_info_using_get()

    def save_asset_profile(self, body: AssetProfile) -> AssetProfile:
        return self.asset_profile_controller.save_asset_profile_using_post(body=body)

    def set_default_asset_profile(self, asset_profile_id: str) -> AssetProfile:
        return self.asset_profile_controller.set_default_asset_profile_using_post(asset_profile_id=asset_profile_id)

    # Rule Engine Controller

    def handle_rule_engine_request(self, body, entity_id: EntityId):
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.rule_engine_controller.handle_rule_engine_request_using_post(body=body, entity_type=entity_type,
                                                                                 entity_id=entity_id)

    def handle_rule_engine_request1(self, body, entity_id: EntityId, timeout: int):
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.rule_engine_controller.handle_rule_engine_request_using_post1(body=body, entity_type=entity_type,
                                                                                  entity_id=entity_id, timeout=timeout)

    def handle_rule_engine_request2(self, body, entity_id: EntityId, timeout: int, queue_name: str):
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.rule_engine_controller.handle_rule_engine_request_using_post2(body=body, entity_type=entity_type,
                                                                                  entity_id=entity_id, timeout=timeout,
                                                                                  queue_name=queue_name)

    def handle_rule_engine_request3(self, body):
        return self.rule_engine_controller.handle_rule_engine_request_using_post3(body=body)
