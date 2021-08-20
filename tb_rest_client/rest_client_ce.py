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

from tb_rest_client.rest_client_base import *

logger = getLogger(__name__)


class RestClientCE(RestClientBase):
    def __init__(self, base_url):
        super().__init__(base_url)

    def get_asset_types(self, ):
        return self.asset_controller.get_asset_types_using_get()

    def get_edge_assets(self, edge_id: EdgeId, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None):
        edge_id = self.get_id(edge_id)
        return self.asset_controller.get_edge_assets_using_get(edge_id=edge_id, page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)

    def get_asset_info_by_id(self, asset_id: AssetId):
        asset_id = self.get_id(asset_id)
        return self.asset_controller.get_asset_info_by_id_using_get(asset_id=asset_id)

    def assign_asset_to_public_customer(self, asset_id: AssetId):
        asset_id = self.get_id(asset_id)
        return self.asset_controller.assign_asset_to_public_customer_using_post(asset_id=asset_id)

    def find_by_query(self, body: AssetSearchQuery):
        return self.asset_controller.find_by_query_using_post(body=body)

    def get_tenant_assets(self, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None):
        return self.asset_controller.get_tenant_assets_using_get(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def save_asset(self, body: Asset):
        return self.asset_controller.save_asset_using_post(body=body)

    def get_assets_by_ids(self, asset_ids: list):
        return self.asset_controller.get_assets_by_ids_using_get(asset_ids=asset_ids)

    def get_customer_asset_infos(self, customer_id: CustomerId, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
        return self.asset_controller.get_customer_asset_infos_using_get(customer_id=customer_id, page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_asset_by_id(self, asset_id: AssetId):
        asset_id = self.get_id(asset_id)
        return self.asset_controller.get_asset_by_id_using_get(asset_id=asset_id)

    def get_tenant_asset_infos(self, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None):
        return self.asset_controller.get_tenant_asset_infos_using_get(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def assign_asset_to_edge(self, edge_id: EdgeId, asset_id: AssetId):
        edge_id = self.get_id(edge_id)
        asset_id = self.get_id(asset_id)
        return self.asset_controller.assign_asset_to_edge_using_post(edge_id=edge_id, asset_id=asset_id)

    def unassign_asset_from_customer(self, asset_id: AssetId):
        asset_id = self.get_id(asset_id)
        return self.asset_controller.unassign_asset_from_customer_using_delete(asset_id=asset_id)

    def unassign_asset_from_edge(self, edge_id: EdgeId, asset_id: AssetId):
        edge_id = self.get_id(edge_id)
        asset_id = self.get_id(asset_id)
        return self.asset_controller.unassign_asset_from_edge_using_delete(edge_id=edge_id, asset_id=asset_id)

    def delete_asset(self, asset_id: AssetId):
        asset_id = self.get_id(asset_id)
        return self.asset_controller.delete_asset_using_delete(asset_id=asset_id)

    def get_customer_assets(self, customer_id: CustomerId, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
        return self.asset_controller.get_customer_assets_using_get(customer_id=customer_id, page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_tenant_asset(self, asset_name: str):
        return self.asset_controller.get_tenant_asset_using_get(asset_name=asset_name)

    def assign_asset_to_customer(self, customer_id: CustomerId, asset_id: AssetId):
        customer_id = self.get_id(customer_id)
        asset_id = self.get_id(asset_id)
        return self.asset_controller.assign_asset_to_customer_using_post(customer_id=customer_id, asset_id=asset_id)

    def sync_edge(self, edge_id: EdgeId):
        edge_id = self.get_id(edge_id)
        return self.edge_controller.sync_edge_using_post(edge_id=edge_id)

    def get_edge_types(self, ):
        return self.edge_controller.get_edge_types_using_get()

    def save_edge(self, body: Edge):
        return self.edge_controller.save_edge_using_post(body=body)

    def unassign_edge_from_customer(self, edge_id: EdgeId):
        edge_id = self.get_id(edge_id)
        return self.edge_controller.unassign_edge_from_customer_using_delete(edge_id=edge_id)

    def get_customer_edges(self, customer_id: CustomerId, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
        return self.edge_controller.get_customer_edges_using_get(customer_id=customer_id, page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_customer_edge_infos(self, customer_id: CustomerId, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
        return self.edge_controller.get_customer_edge_infos_using_get(customer_id=customer_id, page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def check_instance(self, body: object):
        return self.edge_controller.check_instance_using_post(body=body)

    def is_edges_support_enabled(self, ):
        return self.edge_controller.is_edges_support_enabled_using_get()

    def get_edges_by_ids(self, edge_ids: list):
        return self.edge_controller.get_edges_by_ids_using_get(edge_ids=edge_ids)

    def find_missing_to_related_rule_chains(self, edge_id: EdgeId):
        edge_id = self.get_id(edge_id)
        return self.edge_controller.find_missing_to_related_rule_chains_using_get(edge_id=edge_id)

    def get_tenant_edges(self, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None):
        return self.edge_controller.get_tenant_edges_using_get(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def delete_edge(self, edge_id: EdgeId):
        edge_id = self.get_id(edge_id)
        return self.edge_controller.delete_edge_using_delete(edge_id=edge_id)

    def find_by_query_v2(self, body: EdgeSearchQuery):
        return self.edge_controller.find_by_query_using_post2(body=body)

    def set_root_rule_chain(self, edge_id: EdgeId, rule_chain_id: RuleChainId):
        edge_id = self.get_id(edge_id)
        rule_chain_id = self.get_id(rule_chain_id)
        return self.edge_controller.set_root_rule_chain_using_post(edge_id=edge_id, rule_chain_id=rule_chain_id)

    def assign_edge_to_public_customer(self, edge_id: EdgeId):
        edge_id = self.get_id(edge_id)
        return self.edge_controller.assign_edge_to_public_customer_using_post(edge_id=edge_id)

    def get_tenant_edge_infos(self, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None):
        return self.edge_controller.get_tenant_edge_infos_using_get(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_edge_by_id(self, edge_id: EdgeId):
        edge_id = self.get_id(edge_id)
        return self.edge_controller.get_edge_by_id_using_get(edge_id=edge_id)

    def get_tenant_edge(self, edge_name: str):
        return self.edge_controller.get_tenant_edge_using_get(edge_name=edge_name)

    def get_edge_info_by_id(self, edge_id: EdgeId):
        edge_id = self.get_id(edge_id)
        return self.edge_controller.get_edge_info_by_id_using_get(edge_id=edge_id)

    def get_edges(self, page_size: str, page: str, text_search=None, sort_property=None, sort_order=None):
        return self.edge_controller.get_edges_using_get(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def assign_edge_to_customer(self, customer_id: CustomerId, edge_id: EdgeId):
        customer_id = self.get_id(customer_id)
        edge_id = self.get_id(edge_id)
        return self.edge_controller.assign_edge_to_customer_using_post(customer_id=customer_id, edge_id=edge_id)

    def activate_instance(self, license_secret: str, release_date: str):
        return self.edge_controller.activate_instance_using_post(license_secret=license_secret, release_date=release_date)

    def get_persisted_rpc(self, rpc_id: RpcId):
        rpc_id = self.get_id(rpc_id)
        return self.rpc_v_2_controller.get_persisted_rpc_using_get(rpc_id=rpc_id)

    def handle_two_way_device_rpc_request_v1(self, body: str, device_id: DeviceId):
        device_id = self.get_id(device_id)
        return self.rpc_v_2_controller.handle_two_way_device_rpc_request_using_post1(body=body, device_id=device_id)

    def handle_one_way_device_rpc_request_v1(self, body: str, device_id: DeviceId):
        device_id = self.get_id(device_id)
        return self.rpc_v_2_controller.handle_one_way_device_rpc_request_using_post1(body=body, device_id=device_id)

    def delete_resource(self, rpc_id: RpcId):
        rpc_id = self.get_id(rpc_id)
        return self.rpc_v_2_controller.delete_resource_using_delete(rpc_id=rpc_id)

    def get_persisted_rpc_by_device(self, device_id: DeviceId, page_size: int, page: int, rpc_status: str, text_search=None, sort_property=None, sort_order=None):
        device_id = self.get_id(device_id)
        return self.rpc_v_2_controller.get_persisted_rpc_by_device_using_get(device_id=device_id, page_size=page_size, page=page, rpc_status=rpc_status, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_edge_events(self, edge_id: EdgeId, page_size: int, page: int, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None):
        edge_id = self.get_id(edge_id)
        return self.edge_event_controller.get_edge_events_using_get(edge_id=edge_id, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)

    def delete_customer(self, customer_id: CustomerId):
        customer_id = self.get_id(customer_id)
        return self.customer_controller.delete_customer_using_delete(customer_id=customer_id)

    def get_short_customer_info_by_id(self, customer_id: CustomerId):
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_short_customer_info_by_id_using_get(customer_id=customer_id)

    def get_tenant_customer(self, customer_title: str):
        return self.customer_controller.get_tenant_customer_using_get(customer_title=customer_title)

    def get_customers(self, page_size: str, page: str, text_search=None, sort_property=None, sort_order=None):
        return self.customer_controller.get_customers_using_get(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_customer_title_by_id(self, customer_id: CustomerId):
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_customer_title_by_id_using_get(customer_id=customer_id)

    def get_customer_by_id(self, customer_id: CustomerId):
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_customer_by_id_using_get(customer_id=customer_id)

    def save_customer(self, body: Customer):
        return self.customer_controller.save_customer_using_post(body=body)

    def get_user_by_id(self, user_id: UserId):
        user_id = self.get_id(user_id)
        return self.user_controller.get_user_by_id_using_get(user_id=user_id)

    def send_activation_email(self, email: str):
        return self.user_controller.send_activation_email_using_post(email=email)

    def set_user_credentials_enabled(self, user_id: UserId, user_credentials_enabled=None):
        user_id = self.get_id(user_id)
        return self.user_controller.set_user_credentials_enabled_using_post(user_id=user_id, user_credentials_enabled=user_credentials_enabled)

    def get_customer_users(self, customer_id: CustomerId, page_size: str, page: str, text_search=None, sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
        return self.user_controller.get_customer_users_using_get(customer_id=customer_id, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_tenant_admins(self, tenant_id: TenantId, page_size: str, page: str, text_search=None, sort_property=None, sort_order=None):
        tenant_id = self.get_id(tenant_id)
        return self.user_controller.get_tenant_admins_using_get(tenant_id=tenant_id, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_user_token(self, user_id: UserId):
        user_id = self.get_id(user_id)
        return self.user_controller.get_user_token_using_get(user_id=user_id)

    def get_activation_link(self, user_id: UserId):
        user_id = self.get_id(user_id)
        return self.user_controller.get_activation_link_using_get(user_id=user_id)

    def delete_user(self, user_id: UserId):
        user_id = self.get_id(user_id)
        return self.user_controller.delete_user_using_delete(user_id=user_id)

    def save_user(self, body: User, send_activation_mail=None):
        return self.user_controller.save_user_using_post(body=body, send_activation_mail=send_activation_mail)

    def is_user_token_access_enabled(self, ):
        return self.user_controller.is_user_token_access_enabled_using_get()

    def get_users(self, page_size: str, page: str, text_search=None, sort_property=None, sort_order=None):
        return self.user_controller.get_users_using_get(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def delete_device(self, device_id: DeviceId):
        device_id = self.get_id(device_id)
        return self.device_controller.delete_device_using_delete(device_id=device_id)

    def claim_device(self, device_name: str, body=None):
        return self.device_controller.claim_device_using_post(device_name=device_name, body=body)

    def count_by_device_profile_and_empty_ota_package(self, ota_package_type: str, device_profile_id: DeviceProfileId):
        device_profile_id = self.get_id(device_profile_id)
        return self.device_controller.count_by_device_profile_and_empty_ota_package_using_get(ota_package_type=ota_package_type, device_profile_id=device_profile_id)

    def assign_device_to_tenant(self, tenant_id: TenantId, device_id: DeviceId):
        tenant_id = self.get_id(tenant_id)
        device_id = self.get_id(device_id)
        return self.device_controller.assign_device_to_tenant_using_post(tenant_id=tenant_id, device_id=device_id)

    def get_edge_devices(self, edge_id: EdgeId, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None):
        edge_id = self.get_id(edge_id)
        return self.device_controller.get_edge_devices_using_get(edge_id=edge_id, page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)

    def unassign_device_from_edge(self, edge_id: EdgeId, device_id: DeviceId):
        edge_id = self.get_id(edge_id)
        device_id = self.get_id(device_id)
        return self.device_controller.unassign_device_from_edge_using_delete(edge_id=edge_id, device_id=device_id)

    def get_tenant_devices(self, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None):
        return self.device_controller.get_tenant_devices_using_get(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def re_claim_device(self, device_name: str):
        return self.device_controller.re_claim_device_using_delete(device_name=device_name)

    def assign_device_to_edge(self, edge_id: EdgeId, device_id: DeviceId):
        edge_id = self.get_id(edge_id)
        device_id = self.get_id(device_id)
        return self.device_controller.assign_device_to_edge_using_post(edge_id=edge_id, device_id=device_id)

    def get_device_credentials_by_device_id(self, device_id: DeviceId):
        device_id = self.get_id(device_id)
        return self.device_controller.get_device_credentials_by_device_id_using_get(device_id=device_id)

    def get_device_info_by_id(self, device_id: DeviceId):
        device_id = self.get_id(device_id)
        return self.device_controller.get_device_info_by_id_using_get(device_id=device_id)

    def get_device_by_id(self, device_id: DeviceId):
        device_id = self.get_id(device_id)
        return self.device_controller.get_device_by_id_using_get(device_id=device_id)

    def get_customer_device_infos(self, customer_id: CustomerId, page_size: str, page: str, type=None, device_profile_id=None, text_search=None, sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
        device_profile_id = self.get_id(device_profile_id)
        return self.device_controller.get_customer_device_infos_using_get(customer_id=customer_id, page_size=page_size, page=page, type=type, device_profile_id=device_profile_id, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def assign_device_to_customer(self, customer_id: CustomerId, device_id: DeviceId):
        customer_id = self.get_id(customer_id)
        device_id = self.get_id(device_id)
        return self.device_controller.assign_device_to_customer_using_post(customer_id=customer_id, device_id=device_id)

    def find_by_query_v1(self, body: DeviceSearchQuery):
        return self.device_controller.find_by_query_using_post1(body=body)

    def get_tenant_device_infos(self, page_size: str, page: str, type=None, device_profile_id=None, text_search=None, sort_property=None, sort_order=None):
        device_profile_id = self.get_id(device_profile_id)
        return self.device_controller.get_tenant_device_infos_using_get(page_size=page_size, page=page, type=type, device_profile_id=device_profile_id, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_tenant_device(self, device_name: str):
        return self.device_controller.get_tenant_device_using_get(device_name=device_name)

    def save_device(self, body: Device, access_token=None):
        return self.device_controller.save_device_using_post(body=body, access_token=access_token)

    def assign_device_to_public_customer(self, device_id: DeviceId):
        device_id = self.get_id(device_id)
        return self.device_controller.assign_device_to_public_customer_using_post(device_id=device_id)

    def get_device_types(self, ):
        return self.device_controller.get_device_types_using_get()

    def unassign_device_from_customer(self, device_id: DeviceId):
        device_id = self.get_id(device_id)
        return self.device_controller.unassign_device_from_customer_using_delete(device_id=device_id)

    def get_devices_by_ids(self, device_ids: list):
        return self.device_controller.get_devices_by_ids_using_get(device_ids=device_ids)

    def get_customer_devices(self, customer_id: CustomerId, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
        return self.device_controller.get_customer_devices_using_get(customer_id=customer_id, page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def save_device_credentials(self, body: DeviceCredentials):
        return self.device_controller.save_device_credentials_using_post(body=body)

    def get_tenant_entity_views(self, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None):
        return self.entity_view_controller.get_tenant_entity_views_using_get(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def find_by_query_v4(self, body: EntityViewSearchQuery):
        return self.entity_view_controller.find_by_query_using_post4(body=body)

    def assign_entity_view_to_customer(self, customer_id: CustomerId, entity_view_id: EntityViewId):
        customer_id = self.get_id(customer_id)
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.assign_entity_view_to_customer_using_post(customer_id=customer_id, entity_view_id=entity_view_id)

    def unassign_entity_view_from_edge(self, edge_id: EdgeId, entity_view_id: EntityViewId):
        edge_id = self.get_id(edge_id)
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.unassign_entity_view_from_edge_using_delete(edge_id=edge_id, entity_view_id=entity_view_id)

    def get_entity_view_types(self, ):
        return self.entity_view_controller.get_entity_view_types_using_get()

    def get_entity_view_by_id(self, entity_view_id: EntityViewId):
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.get_entity_view_by_id_using_get(entity_view_id=entity_view_id)

    def get_customer_entity_view_infos(self, customer_id: CustomerId, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
        return self.entity_view_controller.get_customer_entity_view_infos_using_get(customer_id=customer_id, page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def delete_entity_view(self, entity_view_id: EntityViewId):
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.delete_entity_view_using_delete(entity_view_id=entity_view_id)

    def save_entity_view(self, body: EntityView):
        return self.entity_view_controller.save_entity_view_using_post(body=body)

    def get_tenant_entity_view(self, entity_view_name: str):
        return self.entity_view_controller.get_tenant_entity_view_using_get(entity_view_name=entity_view_name)

    def get_customer_entity_views(self, customer_id: CustomerId, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
        return self.entity_view_controller.get_customer_entity_views_using_get(customer_id=customer_id, page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def assign_entity_view_to_public_customer(self, entity_view_id: EntityViewId):
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.assign_entity_view_to_public_customer_using_post(entity_view_id=entity_view_id)

    def get_edge_entity_views(self, edge_id: EdgeId, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None):
        edge_id = self.get_id(edge_id)
        return self.entity_view_controller.get_edge_entity_views_using_get(edge_id=edge_id, page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)

    def unassign_entity_view_from_customer(self, entity_view_id: EntityViewId):
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.unassign_entity_view_from_customer_using_delete(entity_view_id=entity_view_id)

    def assign_entity_view_to_edge(self, edge_id: EdgeId, entity_view_id: EntityViewId):
        edge_id = self.get_id(edge_id)
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.assign_entity_view_to_edge_using_post(edge_id=edge_id, entity_view_id=entity_view_id)

    def get_entity_view_info_by_id(self, entity_view_id: EntityViewId):
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.get_entity_view_info_by_id_using_get(entity_view_id=entity_view_id)

    def get_tenant_entity_view_infos(self, page_size: str, page: str, type=None, text_search=None, sort_property=None, sort_order=None):
        return self.entity_view_controller.get_tenant_entity_view_infos_using_get(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

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

    def get_admin_settings(self, key: str):
        return self.admin_controller.get_admin_settings_using_get(key=key)

    def sign_up(self, body: SignUpRequest):
        return self.sign_up_controller.sign_up_using_post(body=body)

    def resend_email_activation(self, email: str):
        return self.sign_up_controller.resend_email_activation_using_post(email=email)

    def activate_email(self, email_code: str):
        return self.sign_up_controller.activate_email_using_get(email_code=email_code)

    def privacy_policy_accepted(self, ):
        return self.sign_up_controller.privacy_policy_accepted_using_get()

    def activate_user_by_email_code(self, email_code: str):
        return self.sign_up_controller.activate_user_by_email_code_using_post(email_code=email_code)

    def get_recaptcha_public_key(self, ):
        return self.sign_up_controller.get_recaptcha_public_key_using_get()

    def accept_privacy_policy(self, ):
        return self.sign_up_controller.accept_privacy_policy_using_post()

    def delete_tenant_account(self, ):
        return self.sign_up_controller.delete_tenant_account_using_delete()

    def unassign_dashboard_from_public_customer(self, dashboard_id: DashboardId):
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.unassign_dashboard_from_public_customer_using_delete(dashboard_id=dashboard_id)

    def get_dashboard_by_id(self, dashboard_id: DashboardId):
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.get_dashboard_by_id_using_get(dashboard_id=dashboard_id)

    def get_edge_dashboards(self, edge_id: EdgeId, page_size: str, page: str, text_search=None, sort_property=None, sort_order=None, start_time=None, end_time=None):
        edge_id = self.get_id(edge_id)
        return self.dashboard_controller.get_edge_dashboards_using_get(edge_id=edge_id, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)

    def set_tenant_home_dashboard_info(self, body: HomeDashboardInfo):
        return self.dashboard_controller.set_tenant_home_dashboard_info_using_post(body=body)

    def get_home_dashboard(self, ):
        return self.dashboard_controller.get_home_dashboard_using_get()

    def add_dashboard_customers(self, body: list[str], dashboard_id: DashboardId):
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.add_dashboard_customers_using_post(body=body, dashboard_id=dashboard_id)

    def get_tenant_dashboards_v1(self, tenant_id: TenantId, page_size: str, page: str, text_search=None, sort_property=None, sort_order=None):
        tenant_id = self.get_id(tenant_id)
        return self.dashboard_controller.get_tenant_dashboards_using_get1(tenant_id=tenant_id, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def assign_dashboard_to_customer(self, customer_id: CustomerId, dashboard_id: DashboardId):
        customer_id = self.get_id(customer_id)
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.assign_dashboard_to_customer_using_post(customer_id=customer_id, dashboard_id=dashboard_id)

    def get_tenant_dashboards(self, page_size: str, page: str, mobile=None, text_search=None, sort_property=None, sort_order=None):
        return self.dashboard_controller.get_tenant_dashboards_using_get(page_size=page_size, page=page, mobile=mobile, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def save_dashboard(self, body: Dashboard):
        return self.dashboard_controller.save_dashboard_using_post(body=body)

    def get_home_dashboard_info(self, ):
        return self.dashboard_controller.get_home_dashboard_info_using_get()

    def get_max_datapoints_limit(self, ):
        return self.dashboard_controller.get_max_datapoints_limit_using_get()

    def update_dashboard_customers(self, dashboard_id: DashboardId, body=None):
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.update_dashboard_customers_using_post(dashboard_id=dashboard_id, body=body)

    def get_dashboard_info_by_id(self, dashboard_id: DashboardId):
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.get_dashboard_info_by_id_using_get(dashboard_id=dashboard_id)

    def delete_dashboard(self, dashboard_id: DashboardId):
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.delete_dashboard_using_delete(dashboard_id=dashboard_id)

    def get_customer_dashboards(self, customer_id: CustomerId, page_size: str, page: str, mobile=None, text_search=None, sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
        return self.dashboard_controller.get_customer_dashboards_using_get(customer_id=customer_id, page_size=page_size, page=page, mobile=mobile, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def remove_dashboard_customers(self, body: list[str], dashboard_id: DashboardId):
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.remove_dashboard_customers_using_post(body=body, dashboard_id=dashboard_id)

    def unassign_dashboard_from_edge(self, edge_id: EdgeId, dashboard_id: DashboardId):
        edge_id = self.get_id(edge_id)
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.unassign_dashboard_from_edge_using_delete(edge_id=edge_id, dashboard_id=dashboard_id)

    def assign_dashboard_to_edge(self, edge_id: EdgeId, dashboard_id: DashboardId):
        edge_id = self.get_id(edge_id)
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.assign_dashboard_to_edge_using_post(edge_id=edge_id, dashboard_id=dashboard_id)

    def assign_dashboard_to_public_customer(self, dashboard_id: DashboardId):
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.assign_dashboard_to_public_customer_using_post(dashboard_id=dashboard_id)

    def get_server_time(self, ):
        return self.dashboard_controller.get_server_time_using_get()

    def get_tenant_home_dashboard_info(self, ):
        return self.dashboard_controller.get_tenant_home_dashboard_info_using_get()

    def unassign_dashboard_from_customer(self, customer_id: CustomerId, dashboard_id: DashboardId):
        customer_id = self.get_id(customer_id)
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.unassign_dashboard_from_customer_using_delete(customer_id=customer_id, dashboard_id=dashboard_id)

    def get_lwm2m_bootstrap_security_info(self, is_bootstrap_server: bool):
        return self.lwm_2m_controller.get_lwm2m_bootstrap_security_info_using_get(is_bootstrap_server=is_bootstrap_server)

    def save_device_with_credentials(self, object=None):
        return self.lwm_2m_controller.save_device_with_credentials_using_post(object=object)

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



