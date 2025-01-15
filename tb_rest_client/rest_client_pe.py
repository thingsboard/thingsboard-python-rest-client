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
from tb_rest_client.api.api_pe import *
from tb_rest_client.api.api_pe import DashboardControllerApi
from tb_rest_client.models.models_pe import *

logger = getLogger(__name__)


class RestClientPE(RestClientBase):
    def __init__(self, base_url):
        super().__init__(base_url)

    def login(self, username, password):
        super(RestClientPE, self).login(username=username, password=password)
        self.__load_controllers()

    def public_login(self, public_id):
        super(RestClientPE, self).public_login(public_id=public_id)
        self.__load_controllers()

    def token_login(self, token, refresh_token=None):
        super(RestClientPE, self).token_login(token=token, refresh_token=refresh_token)
        self.__load_controllers()

    # Self Registration Controller
    def get_privacy_policy(self, ) -> str:
        return self.self_registration_controller.get_privacy_policy_using_get()

    def get_self_registration_params(self, ) -> SelfRegistrationParams:
        return self.self_registration_controller.get_self_registration_params_using_get()

    def get_sign_up_self_registration_params(self, pkg_name: Optional[str] = None) -> SignUpSelfRegistrationParams:
        return self.self_registration_controller.get_sign_up_self_registration_params_using_get(pkg_name=pkg_name)

    def get_terms_of_use(self, ) -> str:
        return self.self_registration_controller.get_terms_of_use_using_get()

    def delete_self_registration_params(self, domain_name: str):
        return self.self_registration_controller.delete_self_registration_params_using_delete(domain_name=domain_name)

    def save_self_registration_params(self, body: Optional[SelfRegistrationParams] = None) -> SelfRegistrationParams:
        return self.self_registration_controller.save_self_registration_params_using_post(body=body)

    # O Auth 2 Config Template Controller
    def delete_client_registration_template(self, client_registration_template_id: EntityId) -> None:
        client_registration_template_id = self.get_id(client_registration_template_id)
        return self.o_auth2_config_template_controller.delete_client_registration_template_using_delete(
            client_registration_template_id=client_registration_template_id)

    def get_client_registration_templates(self, ) -> List[OAuth2ClientRegistrationTemplate]:
        return self.o_auth2_config_template_controller.get_client_registration_templates_using_get()

    def save_client_registration_template(self, body: Optional[OAuth2ClientRegistrationTemplate] = None) -> OAuth2ClientRegistrationTemplate:
        return self.o_auth2_config_template_controller.save_client_registration_template_using_post(body=body)

    # HTTP Integration Controller
    def http_check_status_get(self, routing_key: str, request_params: dict, request_headers: dict):
        return self.http_integration_controller.check_status_using_get(routing_key=routing_key,
                                                                       request_params=request_params,
                                                                       request_headers=request_headers)

    def http_process_request_v1_post1(self, routing_key: str, suffix: str):
        return self.http_integration_controller.process_request_using_post1(routing_key=routing_key, suffix=suffix)

    def http_process_request_v2_post2(self, routing_key: str, suffix: str):
        return self.http_integration_controller.process_request_using_post2(routing_key=routing_key, suffix=suffix)

    def get_asset_types(self, ) -> List[EntitySubtype]:
        return self.asset_controller.get_asset_types_using_get()

    def find_by_query(self, body: Optional[AssetSearchQuery] = None) -> List[Asset]:
        return self.asset_controller.find_by_query_using_post(body=body)

    def get_tenant_assets(self, page_size: int, page: int, type: Optional[str] = None,text_search: Optional[str] = None, sort_property: Optional[str] = None,
                          sort_order: Optional[str] = None) -> PageDataAsset:
        return self.asset_controller.get_tenant_assets_using_get(page_size=page_size, page=page, type=type,
                                                                 text_search=text_search, sort_property=sort_property,
                                                                 sort_order=sort_order)

    # Asset Controller
    def process_asset_bulk_import(self, body: Optional[BulkImportRequest] = None) -> BulkImportResultAsset:
        return self.asset_controller.process_asset_bulk_import_using_post(body=body)

    def save_asset(self, body: Optional[Asset] = None, entity_group_id: EntityGroupId = None, entity_group_ids: Optional[str] = None):
        entity_group_id = self.get_id(entity_group_id)
        if entity_group_ids:
            entity_group_ids = ','.join(entity_group_ids)
        return self.asset_controller.save_asset_using_post(body=body, entity_group_id=entity_group_id, entity_group_ids=entity_group_ids)

    def get_all_customer_infos(self, page_size: int, page: int, type: Optional[str] = None,
                               text_search: Optional[str] = None, sort_property: Optional[str] = None,
                               sort_order: Optional[str] = None,
                               include_customers: Optional[bool] = None) -> PageDataCustomerInfo:
        return self.customer_controller.get_all_customer_infos_using_get(page_size=page_size, page=page, type=type,
                                                                         text_search=text_search,
                                                                         sort_property=sort_property,
                                                                         sort_order=sort_order,
                                                                         include_customers=include_customers)

    def get_customer_customer_infos(self, customer_id: CustomerId, page_size: int, page: int,
                                    type: Optional[str] = None,
                                    text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                    sort_order: Optional[str] = None,
                                    include_customers: Optional[bool] = None) -> PageDataCustomerInfo:
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_customer_customer_infos_using_get(page_size=page_size, page=page, type=type,
                                                                              text_search=text_search,
                                                                              sort_property=sort_property,
                                                                              sort_order=sort_order,
                                                                              include_customers=include_customers,
                                                                              customer_id=customer_id)

    def get_customer_info_by_id(self, customer_id: CustomerId) -> CustomerInfo:
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_customer_info_by_id_using_get(customer_id=customer_id)

    def get_assets_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size: int, page: int,text_search: Optional[str] = None,
                                      sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataAsset:
        entity_group_id = self.get_id(entity_group_id)
        return self.asset_controller.get_assets_by_entity_group_id_using_get(entity_group_id=entity_group_id,
                                                                             page_size=page_size, page=page,
                                                                             text_search=text_search,
                                                                             sort_property=sort_property,
                                                                             sort_order=sort_order)

    def get_user_assets(self, page_size: int, page: int, type: Optional[str] = None,text_search: Optional[str] = None, sort_property: Optional[str] = None,
                        sort_order: Optional[str] = None, asset_profile_id: Optional[AssetProfileId] = None) -> PageDataAsset:
        if asset_profile_id:
            asset_profile_id = self.get_id(asset_profile_id)
        return self.asset_controller.get_user_assets_using_get(page_size=page_size, page=page, type=type,
                                                               text_search=text_search, sort_property=sort_property,
                                                               sort_order=sort_order, asset_profile_id=asset_profile_id)

    def delete_device_group_ota_package(self, id: str) -> None:
        return self.device_group_ota_package_controller.delete_device_group_ota_package_using_delete(id=id)

    def get_firmware_by_id(self, group_id: EntityGroupId, firmware_type: str) -> DeviceGroupOtaPackage:
        group_id = self.get_id(group_id)
        return self.device_group_ota_package_controller.get_firmware_by_id_using_get(group_id=group_id,
                                                                                     firmware_type=firmware_type)

    def save_device_group_ota_package(self, body: Optional[DeviceGroupOtaPackage] = None) -> DeviceGroupOtaPackage:
        return self.device_group_ota_package_controller.save_device_group_ota_package_using_post(body=body)

    def find_by_query_v2(self, body: Optional[EdgeSearchQuery] = None) -> List[Edge]:
        return self.edge_controller.find_by_query_using_post2(body=body)

    def check_instance(self, body: Union[dict, str, list, bytes, None, RESTResponse, tuple, Any] = None) -> Union[
            dict, str, list, bytes, None, RESTResponse, tuple, Any]:
        return self.edge_controller.check_instance_using_post(body=body)

    def get_tenant_edges(self, page_size: int, page: int, type: Optional[str] = None,text_search: Optional[str] = None, sort_property: Optional[str] = None,
                         sort_order: Optional[str] = None) -> PageDataEdge:
        return self.edge_controller.get_tenant_edges_using_get(page_size=page_size, page=page, type=type,
                                                               text_search=text_search, sort_property=sort_property,
                                                               sort_order=sort_order)

    def find_missing_to_related_rule_chains(self, edge_id: EdgeId) -> str:
        edge_id = self.get_id(edge_id)
        return self.edge_controller.find_missing_to_related_rule_chains_using_get(edge_id=edge_id)

    def get_customer_edges(self, customer_id: CustomerId, page_size: int, page: int, type: Optional[str] = None,text_search: Optional[str] = None,
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

    def get_user_edges(self, page_size: int, page: int, type: Optional[str] = None,text_search: Optional[str] = None, sort_property: Optional[str] = None,
                       sort_order: Optional[str] = None) -> PageDataEdge:
        return self.edge_controller.get_user_edges_using_get(page_size=page_size, page=page, type=type,
                                                             text_search=text_search, sort_property=sort_property,
                                                             sort_order=sort_order)

    def delete_edge(self, edge_id: EdgeId) -> None:
        edge_id = self.get_id(edge_id)
        return self.edge_controller.delete_edge_using_delete(edge_id=edge_id)

    def save_edge(self, body: Optional[Edge] = None) -> Edge:
        return self.edge_controller.save_edge_using_post(body=body)

    def is_edges_support_enabled(self, ) -> bool:
        return self.edge_controller.is_edges_support_enabled_using_get()

    def get_edges(self, page_size: int, page: int,text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataEdge:
        return self.edge_controller.get_edges_using_get(page_size=page_size, page=page, text_search=text_search,
                                                        sort_property=sort_property, sort_order=sort_order)

    def get_edge_types(self, ) -> List[EntitySubtype]:
        return self.edge_controller.get_edge_types_using_get()

    def set_edge_root_rule_chain(self, edge_id: EdgeId, rule_chain_id: RuleChainId) -> Edge:
        edge_id = self.get_id(edge_id)
        rule_chain_id = self.get_id(rule_chain_id)
        return self.edge_controller.set_edge_root_rule_chain_using_post(edge_id=edge_id, rule_chain_id=rule_chain_id)

    def get_edges_by_ids(self, edge_ids: list) -> List[Edge]:
        return self.edge_controller.get_edges_by_ids_using_get(edge_ids=str(edge_ids))

    def get_allowed_permissions(self, ) -> AllowedPermissionsInfo:
        return self.user_permissions_controller.get_allowed_permissions_using_get()

    def change_owner_to_customer(self, owner_id: UserId, entity_id: EntityId, body: Optional[List[str]] = None) -> None:
        owner_id = self.get_id(owner_id)
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        if body:
            body = ','.join(body)
        return self.owner_controller.change_owner_to_customer_using_post(owner_id=owner_id, entity_type=entity_type,
                                                                         entity_id=entity_id, body=body)

    def change_owner_to_tenant(self, owner_id: UserId, entity_id: EntityId, body: Optional[List[str]] = None) -> None:
        owner_id = self.get_id(owner_id)
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        if body:
            body = ','.join(body)
        return self.owner_controller.change_owner_to_tenant_using_post(owner_id=owner_id, entity_type=entity_type,
                                                                       entity_id=entity_id, body=body)

    def get_persisted_rpc(self, rpc_id: RpcId) -> Rpc:
        rpc_id = self.get_id(rpc_id)
        return self.rpc_v2_controller.get_persisted_rpc_using_get(rpc_id=rpc_id)

    def rpc_v2_get_persisted_rpc(self, rpc_id: RpcId) -> Rpc:
        rpc_id = self.get_id(rpc_id)
        return self.rpc_v2_controller.get_persisted_rpc_using_get(rpc_id=rpc_id)

    def get_user_customers(self, page_size: int, page: int,text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataCustomer:
        return self.customer_controller.get_user_customers_using_get(page_size=page_size, page=page,
                                                                     text_search=text_search,
                                                                     sort_property=sort_property, sort_order=sort_order)

    def handle_one_way_device_rpc_request_v1(self, device_id: DeviceId, body: Optional[str] = None):
        device_id = self.get_id(device_id)
        return self.rpc_v2_controller.handle_one_way_device_rpc_request_using_post1(device_id=device_id, body=body)

    def handle_two_way_device_rpc_request_v1(self, device_id: DeviceId, body: Optional[str] = None):
        device_id = self.get_id(device_id)
        return self.rpc_v2_controller.handle_two_way_device_rpc_request_using_post1(device_id=device_id, body=body)

    def get_persisted_rpc_by_device(self, device_id: DeviceId, page_size: int, page: int, rpc_status: str,
                                   text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None):
        device_id = self.get_id(device_id)
        return self.rpc_v2_controller.get_persisted_rpc_by_device_using_get(device_id=device_id, page_size=page_size,
                                                                            page=page, rpc_status=rpc_status,
                                                                            text_search=text_search,
                                                                            sort_property=sort_property,
                                                                            sort_order=sort_order)

    def get_customers_by_ids(self, customer_ids: str) -> List[Customer]:
        return self.customer_controller.get_customers_by_ids_using_get(customer_ids=customer_ids)

    def get_edge_events(self, edge_id: EdgeId, page_size: int, page: int,text_search: Optional[str] = None, sort_property: Optional[str] = None,
                        sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None) -> PageDataEdgeEvent:
        edge_id = self.get_id(edge_id)
        return self.edge_event_controller.get_edge_events_using_get(edge_id=edge_id, page_size=page_size, page=page,
                                                                    text_search=text_search,
                                                                    sort_property=sort_property, sort_order=sort_order,
                                                                    start_time=start_time, end_time=end_time)

    def get_customers_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size: int, page: int,
                                        text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataCustomer:
        entity_group_id = self.get_id(entity_group_id)
        return self.customer_controller.get_customers_by_entity_group_id_using_get(entity_group_id=entity_group_id,
                                                                                   page_size=page_size, page=page,
                                                                                   text_search=text_search,
                                                                                   sort_property=sort_property,
                                                                                   sort_order=sort_order)

    def get_customer_title_by_id(self, customer_id: CustomerId) -> str:
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_customer_title_by_id_using_get(customer_id=customer_id)

    def get_customers(self, page_size: int, page: int,text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataCustomer:
        return self.customer_controller.get_customers_using_get(page_size=page_size, page=page, text_search=text_search,
                                                                sort_property=sort_property, sort_order=sort_order)

    def get_customer_by_id(self, customer_id: CustomerId) -> Customer:
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_customer_by_id_using_get(customer_id=customer_id)

    def get_short_customer_info_by_id(self, customer_id: CustomerId) -> Union[
            dict, str, list, bytes, None, RESTResponse, tuple, Any]:
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_short_customer_info_by_id_using_get(customer_id=customer_id)

    def save_customer(self, body: Optional[Customer] = None, entity_group_id: Optional[EntityGroupId] = None, entity_group_ids: Optional[List[str]] = None) -> Customer:
        if entity_group_id:
            entity_group_id = self.get_id(entity_group_id)
        if entity_group_ids:
            entity_group_ids = ','.join(entity_group_ids)
        return self.customer_controller.save_customer_using_post(body=body, entity_group_id=entity_group_id, entity_group_ids=entity_group_ids)

    def get_tenant_customer(self, customer_title: str) -> Customer:
        return self.customer_controller.get_tenant_customer_using_get(customer_title=customer_title)

    def delete_customer(self, customer_id: CustomerId) -> None:
        customer_id = self.get_id(customer_id)
        return self.customer_controller.delete_customer_using_delete(customer_id=customer_id)

    def get_user_token(self, user_id: UserId) -> None:
        user_id = self.get_id(user_id)
        return self.user_controller.get_user_token_using_get(user_id=user_id)

    def get_activation_link(self, user_id: UserId) -> str:
        user_id = self.get_id(user_id)
        return self.user_controller.get_activation_link_using_get(user_id=user_id)

    def get_user_users(self, page_size: int, page: int,text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataUser:
        return self.user_controller.get_user_users_using_get(page_size=page_size, page=page, text_search=text_search,
                                                             sort_property=sort_property, sort_order=sort_order)

    def delete_user(self, user_id: UserId) -> None:
        user_id = self.get_id(user_id)
        return self.user_controller.delete_user_using_delete(user_id=user_id)

    def get_all_customer_users(self, page_size: int, page: int,text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataUser:
        return self.user_controller.get_all_customer_users_using_get(page_size=page_size, page=page,
                                                                     text_search=text_search,
                                                                     sort_property=sort_property, sort_order=sort_order)

    def set_user_credentials_enabled(self, user_id: UserId, user_credentials_enabled: Optional[bool] = None) -> None:
        user_id = self.get_id(user_id)
        return self.user_controller.set_user_credentials_enabled_using_post(user_id=user_id,
                                                                            user_credentials_enabled=user_credentials_enabled)

    def get_customer_users(self, customer_id: CustomerId, page_size: int, page: int,text_search: Optional[str] = None,
                           sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataUser:
        customer_id = self.get_id(customer_id)
        return self.user_controller.get_customer_users_using_get(customer_id=customer_id, page_size=page_size,
                                                                 page=page, text_search=text_search,
                                                                 sort_property=sort_property, sort_order=sort_order)

    def get_user_by_id(self, user_id: UserId) -> User:
        user_id = self.get_id(user_id)
        return self.user_controller.get_user_by_id_using_get(user_id=user_id)

    def get_tenant_admins(self, tenant_id: TenantId, page_size: int, page: int,text_search: Optional[str] = None, sort_property: Optional[str] = None,
                          sort_order: Optional[str] = None,) -> PageDataUser:
        tenant_id = self.get_id(tenant_id)
        return self.user_controller.get_tenant_admins_using_get(tenant_id=tenant_id, page_size=page_size, page=page,
                                                                text_search=text_search, sort_property=sort_property,
                                                                sort_order=sort_order)

    def is_user_token_access_enabled(self, ) -> bool:
        return self.user_controller.is_user_token_access_enabled_using_get()

    def get_users_by_ids(self, user_ids: list) -> List[User]:
        return self.user_controller.get_users_by_ids_using_get(user_ids=str(user_ids))

    def save_user(self, body: Optional[User] = None, send_activation_mail: Optional[bool] = None,
                  entity_group_id: Optional[EntityGroupId] = None,
                  entity_group_ids: Optional[List[str]] = None) -> User:
        if entity_group_id:
            entity_group_id = self.get_id(entity_group_id)

        if entity_group_ids:
            entity_group_ids = ','.join(entity_group_ids)

        return self.user_controller.save_user_using_post(body=body,
                                                         send_activation_mail=send_activation_mail,
                                                         entity_group_id=entity_group_id,
                                                         entity_group_ids=entity_group_ids)

    def send_activation_email(self, email: str) -> None:
        return self.user_controller.send_activation_email_using_post(email=email)

    def get_users_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size: int, page: int,text_search: Optional[str] = None,
                                     sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataUser:
        entity_group_id = self.get_id(entity_group_id)
        return self.user_controller.get_users_by_entity_group_id_using_get(entity_group_id=entity_group_id,
                                                                           page_size=page_size, page=page,
                                                                           text_search=text_search,
                                                                           sort_property=sort_property,
                                                                           sort_order=sort_order)

    def delete_group_permission(self, group_permission_id: GroupPermissionId) -> None:
        group_permission_id = self.get_id(group_permission_id)
        return self.group_permission_controller.delete_group_permission_using_delete(
            group_permission_id=group_permission_id)

    def get_entity_group_permissions(self, entity_group_id: EntityGroupId) -> List[GroupPermissionInfo]:
        entity_group_id = self.get_id(entity_group_id)
        return self.group_permission_controller.get_entity_group_permissions_using_get(entity_group_id=entity_group_id)

    def get_group_permission_by_id(self, group_permission_id: GroupPermissionId) -> GroupPermission:
        group_permission_id = self.get_id(group_permission_id)
        return self.group_permission_controller.get_group_permission_by_id_using_get(
            group_permission_id=group_permission_id)

    def get_group_permission_info_by_id(self, group_permission_id: GroupPermissionId,
                                        is_user_group: bool) -> GroupPermissionInfo:
        group_permission_id = self.get_id(group_permission_id)
        return self.group_permission_controller.get_group_permission_info_by_id_using_get(
            group_permission_id=group_permission_id, is_user_group=is_user_group)

    def get_user_group_permissions(self, user_group_id: EntityId) -> List[GroupPermissionInfo]:
        user_group_id = self.get_id(user_group_id)
        return self.group_permission_controller.get_user_group_permissions_using_get(user_group_id=user_group_id)

    def load_user_group_permission_infos(self, body: Optional[List[GroupPermission]] = None) -> List[GroupPermissionInfo]:
        return self.group_permission_controller.load_user_group_permission_infos_using_post(body=body)

    def save_group_permission(self, body: Optional[GroupPermission] = None) -> GroupPermission:
        return self.group_permission_controller.save_group_permission_using_post(body=body)

    def get_device_types(self, ) -> List[EntitySubtype]:
        return self.device_controller.get_device_types_using_get()

    def process_devices_bulk_import(self, body: Optional[BulkImportRequest] = None) -> BulkImportResultDevice:
        return self.device_controller.process_devices_bulk_import_using_post(body=body)

    def count_by_device_profile_and_empty_ota_package(self, ota_package_type: str,
                                                      device_profile_id: DeviceProfileId) -> int:
        device_profile_id = self.get_id(device_profile_id)
        return self.device_controller.count_by_device_profile_and_empty_ota_package_using_get(
            ota_package_type=ota_package_type, device_profile_id=device_profile_id)

    def get_devices_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size: int, page: int,
                                      text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                       sort_order: Optional[str] = None,) -> PageDataDevice:
        entity_group_id = self.get_id(entity_group_id)
        return self.device_controller.get_devices_by_entity_group_id_using_get(entity_group_id=entity_group_id,
                                                                               page_size=page_size, page=page,
                                                                               text_search=text_search,
                                                                               sort_property=sort_property,
                                                                               sort_order=sort_order)

    def get_devices_by_ids(self, device_ids: list) -> List[Device]:
        device_ids = ','.join(device_ids)
        return self.device_controller.get_devices_by_ids_using_get(device_ids=device_ids)

    def get_user_devices(self, page_size: int, page: int, type: Optional[str] = None,text_search: Optional[str] = None,
                         sort_property: Optional[str] = None,
                         sort_order: Optional[str] = None,) -> PageDataDevice:
        return self.device_controller.get_user_devices_using_get(page_size=page_size, page=page, type=type,
                                                                 text_search=text_search, sort_property=sort_property,
                                                                 sort_order=sort_order)

    def save_device_with_credentials(self, body: Optional[SaveDeviceWithCredentialsRequest] = None,
                                     entity_group_id: Optional[str] = None,
                                     entity_group_ids: Optional[str] = None) -> Device:
        return self.device_controller.save_device_with_credentials_using_post(body=body,
                                                                              entity_group_id=entity_group_id,
                                                                              entity_group_ids=entity_group_ids)

    def update_device_credentials(self, body: Optional[DeviceCredentials] = None) -> DeviceCredentials:
        return self.device_controller.update_device_credentials_using_post(body=body)

    def save_device(self, body: Optional[Device], access_token: Optional[str] = None) -> Device:
        return self.device_controller.save_device_using_post(body=body, access_token=access_token)

    def get_device_by_id(self, device_id: DeviceId) -> Device:
        device_id = self.get_id(device_id)
        return self.device_controller.get_device_by_id_using_get(device_id=device_id)

    def get_tenant_devices(self, page_size: int, page: int, type: Optional[str] = None,text_search: Optional[str] = None, sort_property: Optional[str] = None,
                           sort_order: Optional[str] = None,) -> PageDataDevice:
        return self.device_controller.get_tenant_devices_using_get(page_size=page_size, page=page, type=type,
                                                                   text_search=text_search, sort_property=sort_property,
                                                                   sort_order=sort_order)

    def get_customer_devices(self, customer_id: CustomerId, page_size: int, page: int, type: Optional[str] = None,text_search: Optional[str] = None,
                             sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataDevice:
        customer_id = self.get_id(customer_id)
        return self.device_controller.get_customer_devices_using_get(customer_id=customer_id, page_size=page_size,
                                                                     page=page, type=type, text_search=text_search,
                                                                     sort_property=sort_property, sort_order=sort_order)

    def assign_device_to_tenant(self, tenant_id: TenantId, device_id: DeviceId) -> Device:
        tenant_id = self.get_id(tenant_id)
        device_id = self.get_id(device_id)
        return self.device_controller.assign_device_to_tenant_using_post(tenant_id=tenant_id, device_id=device_id)

    def find_by_query_v1(self, body: Optional[DeviceSearchQuery] = None) -> List[Device]:
        return self.device_controller.find_by_query_using_post1(body=body)

    def count_by_device_group_and_empty_ota_package(self, ota_package_type: str, ota_package_id: OtaPackageId,
                                                    entity_group_id: EntityGroupId) -> int:
        ota_package_id = self.get_id(ota_package_id)
        entity_group_id = self.get_id(entity_group_id)
        return self.device_controller.count_by_device_group_and_empty_ota_package_using_get(
            ota_package_type=ota_package_type, ota_package_id=ota_package_id, entity_group_id=entity_group_id)

    def delete_device(self, device_id: DeviceId) -> None:
        device_id = self.get_id(device_id)
        return self.device_controller.delete_device_using_delete(device_id=device_id)

    def re_claim_device(self, device_name: str):
        return self.device_controller.re_claim_device_using_delete(device_name=device_name)

    def get_tenant_device(self, device_name: str) -> Device:
        return self.device_controller.get_tenant_device_using_get(device_name=device_name)

    def get_device_credentials_by_device_id(self, device_id: DeviceId) -> DeviceCredentials:
        device_id = self.get_id(device_id)
        return self.device_controller.get_device_credentials_by_device_id_using_get(device_id=device_id)

    def delete_converter(self, converter_id: ConverterId) -> None:
        converter_id = self.get_id(converter_id)
        return self.converter_controller.delete_converter_using_delete(converter_id=converter_id)

    def get_converter_by_id(self, converter_id: ConverterId) -> Converter:
        converter_id = self.get_id(converter_id)
        return self.converter_controller.get_converter_by_id_using_get(converter_id=converter_id)

    def get_converters_by_ids(self, converter_ids: list) -> List[Converter]:
        converter_ids = ','.join(converter_ids)
        return self.converter_controller.get_converters_by_ids_using_get(converter_ids=converter_ids)

    def get_converters(self, page_size: int, page: int, is_edge_template: Optional[bool] = None,
                       text_search: Optional[str] = None, sort_property: Optional[str] = None,
                       sort_order: Optional[str] = None) -> PageDataConverter:
        return self.converter_controller.get_converters_using_get(page_size=page_size, page=page,
                                                                  is_edge_template=is_edge_template,
                                                                  text_search=text_search, sort_property=sort_property,
                                                                  sort_order=sort_order)

    def get_latest_converter_debug_input(self, converter_id: ConverterId, integration: Optional[Integration] = None) -> \
    Union[
        dict, str, list, bytes, None, RESTResponse, tuple, Any]:
        converter_id = self.get_id(converter_id)

        integration_type = None
        integration_name = None
        if integration:
            integration_type = self.get_type(integration)
            integration_name = self.get_id(integration)

        return self.converter_controller.get_latest_converter_debug_input_using_get(converter_id=converter_id,
                                                                                    integration_type=integration_type,
                                                                                    integration_name=integration_name)

    def assign_integration_to_edge(self, edge_id: EdgeId, integration_id: IntegrationId) -> Integration:
        edge_id = self.get_id(edge_id)
        integration_id = self.get_id(integration_id)
        return self.integration_controller.assign_integration_to_edge_using_post(edge_id=edge_id,
                                                                                 integration_id=integration_id)

    def unassign_integration_from_edge(self, edge_id: EdgeId, integration_id: IntegrationId) -> Integration:
        edge_id = self.get_id(edge_id)
        integration_id = self.get_id(integration_id)
        return self.integration_controller.unassign_integration_from_edge_using_delete(edge_id=edge_id,
                                                                                       integration_id=integration_id)

    def get_edge_integrations(self, edge_id: EdgeId, page_size: int, page: int, text_search: Optional[str] = None,
                              sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataIntegration:
        edge_id = self.get_id(edge_id)
        return self.integration_controller.get_edge_integrations_using_get(edge_id=edge_id, page_size=page_size,
                                                                           page=page, text_search=text_search,
                                                                           sort_property=sort_property,
                                                                           sort_order=sort_order)

    def find_all_related_edges_missing_attributes(self, integration_id: IntegrationId) -> str:
        integration_id = self.get_id(integration_id)
        return self.integration_controller.find_all_related_edges_missing_attributes_using_get(
            integration_id=integration_id)

    def get_edge_integration_infos(self, edge_id: EdgeId, page_size: int, page: int, text_search: Optional[str] = None,
                                   sort_property: Optional[str] = None,
                                   sort_order: Optional[str] = None, ) -> PageDataIntegrationInfo:
        edge_id = self.get_id(edge_id)
        return self.integration_controller.get_edge_integration_infos_using_get(edge_id=edge_id, page_size=page_size,
                                                                                page=page, text_search=text_search,
                                                                                sort_property=sort_property,
                                                                                sort_order=sort_order)

    def find_edge_missing_attributes_get(self, edge_id: EdgeId, integration_ids: str) -> str:
        edge_id = self.get_id(edge_id)
        return self.integration_controller.find_edge_missing_attributes_using_get(edge_id=edge_id,
                                                                                  integration_ids=integration_ids)

    def get_integrations_converters_info(self):
        return self.integration_controller.get_integrations_converters_info()

    def save_converter(self, body: Optional[Converter] = None) -> Converter:
        return self.converter_controller.save_converter_using_post(body=body)

    def test_down_link_converter(self, body: Union[dict, str, list, bytes, None, RESTResponse, tuple, Any] = None,
                                 script_lang: Optional[str] = None) -> Union[
            dict, str, list, bytes, None, RESTResponse, tuple, Any]:
        return self.converter_controller.test_down_link_converter_using_post(body=body, script_lang=script_lang)

    def test_up_link_converter(self, body: Union[dict, str, list, bytes, None, RESTResponse, tuple, Any] = None,
                               script_lang: Optional[str] = None) -> Union[
            dict, str, list, bytes, None, RESTResponse, tuple, Any]:
        return self.converter_controller.test_up_link_converter_using_post(body=body, script_lang=script_lang)

    def get_entity_view_types(self, ) -> List[EntitySubtype]:
        return self.entity_view_controller.get_entity_view_types_using_get()

    def delete_entity_view(self, entity_view_id: EntityViewId) -> None:
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.delete_entity_view_using_delete(entity_view_id=entity_view_id)

    def get_entity_view_by_id(self, entity_view_id: EntityViewId) -> EntityView:
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.get_entity_view_by_id_using_get(entity_view_id=entity_view_id)

    def get_tenant_entity_view(self, entity_view_name: str) -> EntityView:
        return self.entity_view_controller.get_tenant_entity_view_using_get(entity_view_name=entity_view_name)

    def get_user_entity_views(self, page_size: int, page: int, type: Optional[str] = None,
                              text_search: Optional[str] = None, sort_property: Optional[str] = None,
                              sort_order: Optional[str] = None,) -> PageDataEntityView:
        return self.entity_view_controller.get_user_entity_views_using_get(page_size=page_size, page=page, type=type,
                                                                           text_search=text_search,
                                                                           sort_property=sort_property,
                                                                           sort_order=sort_order)

    def get_entity_views_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size: int, page: int,
                                           text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                            sort_order: Optional[str] = None,) -> PageDataEntityView:
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_view_controller.get_entity_views_by_entity_group_id_using_get(
            entity_group_id=entity_group_id, page_size=page_size, page=page, text_search=text_search,
            sort_property=sort_property, sort_order=sort_order)

    def get_entity_views_by_ids(self, entity_view_ids: list) -> List[EntityView]:
        entity_view_ids = ','.join(entity_view_ids)
        return self.entity_view_controller.get_entity_views_by_ids_using_get(entity_view_ids=entity_view_ids)

    def save_entity_view(self, body: Optional[EntityView] = None, entity_group_id: Optional[EntityGroupId] = None,
                         entity_group_ids: Optional[List[str]] = None) -> EntityView:
        if entity_group_id:
            entity_group_id = self.get_id(entity_group_id)
        if entity_group_ids:
            entity_group_ids = ','.join(entity_group_ids)
        return self.entity_view_controller.save_entity_view_using_post(body=body, entity_group_id=entity_group_id, entity_group_ids=entity_group_ids)

    def get_tenant_entity_views(self, page_size: int, page: int, type: Optional[str] = None,text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                sort_order: Optional[str] = None,) -> PageDataEntityView:
        return self.entity_view_controller.get_tenant_entity_views_using_get(page_size=page_size, page=page, type=type,
                                                                             text_search=text_search,
                                                                             sort_property=sort_property,
                                                                             sort_order=sort_order)

    def find_by_query_v4(self, body: Optional[EntityViewSearchQuery] = None) -> List[EntityView]:
        return self.entity_view_controller.find_by_query_using_post4(body=body)

    def get_customer_entity_views(self, customer_id: CustomerId, page_size: int, page: int, type: Optional[str] = None,text_search: Optional[str] = None,
                                  sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataEntityView:
        customer_id = self.get_id(customer_id)
        return self.entity_view_controller.get_customer_entity_views_using_get(customer_id=customer_id,
                                                                               page_size=page_size, page=page,
                                                                               type=type, text_search=text_search,
                                                                               sort_property=sort_property,
                                                                               sort_order=sort_order)

    def handle_rule_engine_request(self, entity_id: EntityId, timeout: int, body: Optional[str] = None):
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.rule_engine_controller.handle_rule_engine_request_using_post(entity_type=entity_type,
                                                                                 entity_id=entity_id, timeout=timeout,
                                                                                 body=body)

    def handle_rule_engine_request_v1(self, entity_id: EntityId, body: Optional[str] = None,
                                      queue_name: Optional[str] = None,
                                      timeout: Optional[int] = None) -> DeferredResultResponseEntity:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.rule_engine_controller.handle_rule_engine_request_using_post1(entity_type=entity_type,
                                                                                  entity_id=entity_id, body=body,
                                                                                  queue_name=queue_name, timeout=timeout)

    def handle_rule_engine_request_v2(self, entity_id: EntityId, body: Optional[str] = None):
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.rule_engine_controller.handle_rule_engine_request_using_post2(entity_type=entity_type,
                                                                                  entity_id=entity_id, body=body)

    def get_admin_settings(self, key: str, system_by_default=None) -> AdminSettings:
        return self.admin_controller.get_admin_settings_using_get(key=key, system_by_default=system_by_default)

    def t_mobile_iot_cdp_process_request_v4_delete4(self, body: str, request_headers: dict, routing_key: str):
        return self.t_mobile_iot_cdp_integration_controller.process_request_using_delete4(body=body,
                                                                                          request_headers=request_headers,
                                                                                          routing_key=routing_key)

    def t_mobile_iot_cdp_process_request_v4_get4(self, body: str, request_headers: dict, routing_key: str):
        return self.t_mobile_iot_cdp_integration_controller.process_request_using_get4(body=body,
                                                                                       request_headers=request_headers,
                                                                                       routing_key=routing_key)

    def t_mobile_iot_cdp_process_request_v4_head4(self, body: str, request_headers: dict, routing_key: str):
        return self.t_mobile_iot_cdp_integration_controller.process_request_using_head4(body=body,
                                                                                        request_headers=request_headers,
                                                                                        routing_key=routing_key)

    def t_mobile_iot_cdp_process_request_v4_options4(self, body: str, request_headers: dict, routing_key: str):
        return self.t_mobile_iot_cdp_integration_controller.process_request_using_options4(body=body,
                                                                                           request_headers=request_headers,
                                                                                           routing_key=routing_key)

    def t_mobile_iot_cdp_process_request_v4_patch4(self, body: str, request_headers: dict, routing_key: str):
        return self.t_mobile_iot_cdp_integration_controller.process_request_using_patch4(body=body,
                                                                                         request_headers=request_headers,
                                                                                         routing_key=routing_key)

    def t_mobile_iot_cdp_process_request_v12_post12(self, body: str, request_headers: dict, routing_key: str):
        return self.t_mobile_iot_cdp_integration_controller.process_request_using_post12(body=body,
                                                                                         request_headers=request_headers,
                                                                                         routing_key=routing_key)

    def t_mobile_iot_cdp_process_request_v4_put4(self, body: str, request_headers: dict, routing_key: str):
        return self.t_mobile_iot_cdp_integration_controller.process_request_using_put4(body=body,
                                                                                       request_headers=request_headers,
                                                                                       routing_key=routing_key)

    def sign_up(self, body: Optional[SignUpRequest] = None) -> str:
        return self.sign_up_controller.sign_up_using_post(body=body)

    def resend_email_activation(self, email: str, pkg_name: Optional[str] = None) -> None:
        return self.sign_up_controller.resend_email_activation_using_post(email=email, pkg_name=pkg_name)

    def activate_user_by_email_code(self, email_code: str, pkg_name: Optional[str] = None) -> Union[
            dict, str, list, bytes, None, RESTResponse, tuple, Any]:
        return self.sign_up_controller.activate_user_by_email_code_using_post(email_code=email_code, pkg_name=pkg_name)

    def privacy_policy_accepted(self, ) -> bool:
        return self.sign_up_controller.privacy_policy_accepted_using_get()

    def accept_terms_of_use(self, ) -> Union[
            dict, str, list, bytes, None, RESTResponse, tuple, Any]:
        return self.sign_up_controller.accept_terms_of_use_using_post()

    def activate_email(self, email_code: str, pkg_name: Optional[str] = None) -> str:
        return self.sign_up_controller.activate_email_using_get(email_code=email_code, pkg_name=pkg_name)

    def mobile_login(self, pkg_name: str) -> str:
        return self.sign_up_controller.mobile_login_using_get(pkg_name=pkg_name)

    def terms_of_use_accepted(self, ) -> bool:
        return self.sign_up_controller.terms_of_use_accepted_using_get()

    def get_device_profiles_by_ids(self, device_profile_ids: list) -> List[DeviceProfileInfo]:
        device_profile_ids = ','.join(device_profile_ids)
        return self.device_profile_controller.get_device_profiles_by_ids_using_get(
            device_profile_ids=device_profile_ids)

    def thing_park_process_request_tpe_delete(self, body: str, request_headers: dict, all_request_params: dict,
                                              routing_key: str):
        return self.thing_park_integration_controller.process_request_tpe_using_delete(body=body,
                                                                                       request_headers=request_headers,
                                                                                       all_request_params=all_request_params,
                                                                                       routing_key=routing_key)

    def thing_park_process_request_tpe_get(self, body: str, request_headers: dict, all_request_params: dict,
                                           routing_key: str):
        return self.thing_park_integration_controller.process_request_tpe_using_get(body=body,
                                                                                    request_headers=request_headers,
                                                                                    all_request_params=all_request_params,
                                                                                    routing_key=routing_key)

    def thing_park_process_request_tpe_head(self, body: str, request_headers: dict, all_request_params: dict,
                                            routing_key: str):
        return self.thing_park_integration_controller.process_request_tpe_using_head(body=body,
                                                                                     request_headers=request_headers,
                                                                                     all_request_params=all_request_params,
                                                                                     routing_key=routing_key)

    def thing_park_process_request_tpe_options(self, body: str, request_headers: dict, all_request_params: dict,
                                               routing_key: str):
        return self.thing_park_integration_controller.process_request_tpe_using_options(body=body,
                                                                                        request_headers=request_headers,
                                                                                        all_request_params=all_request_params,
                                                                                        routing_key=routing_key)

    def thing_park_process_request_tpe_patch(self, body: str, request_headers: dict, all_request_params: dict,
                                             routing_key: str):
        return self.thing_park_integration_controller.process_request_tpe_using_patch(body=body,
                                                                                      request_headers=request_headers,
                                                                                      all_request_params=all_request_params,
                                                                                      routing_key=routing_key)

    def thing_park_process_request_tpe_post(self, body: str, request_headers: dict, all_request_params: dict,
                                            routing_key: str):
        return self.thing_park_integration_controller.process_request_tpe_using_post(body=body,
                                                                                     request_headers=request_headers,
                                                                                     all_request_params=all_request_params,
                                                                                     routing_key=routing_key)

    def thing_park_process_request_tpe_put(self, body: str, request_headers: dict, all_request_params: dict,
                                           routing_key: str):
        return self.thing_park_integration_controller.process_request_tpe_using_put(body=body,
                                                                                    request_headers=request_headers,
                                                                                    all_request_params=all_request_params,
                                                                                    routing_key=routing_key)

    def thing_park_process_request_v5_delete5(self, body: str, request_headers: dict, all_request_params: dict,
                                              routing_key: str):
        return self.thing_park_integration_controller.process_request_using_delete5(body=body,
                                                                                    request_headers=request_headers,
                                                                                    all_request_params=all_request_params,
                                                                                    routing_key=routing_key)

    def thing_park_process_request_v5_get5(self, body: str, request_headers: dict, all_request_params: dict,
                                           routing_key: str):
        return self.thing_park_integration_controller.process_request_using_get5(body=body,
                                                                                 request_headers=request_headers,
                                                                                 all_request_params=all_request_params,
                                                                                 routing_key=routing_key)

    def thing_park_process_request_v5_head5(self, body: str, request_headers: dict, all_request_params: dict,
                                            routing_key: str):
        return self.thing_park_integration_controller.process_request_using_head5(body=body,
                                                                                  request_headers=request_headers,
                                                                                  all_request_params=all_request_params,
                                                                                  routing_key=routing_key)

    def thing_park_process_request_v5_options5(self, body: str, request_headers: dict, all_request_params: dict,
                                               routing_key: str):
        return self.thing_park_integration_controller.process_request_using_options5(body=body,
                                                                                     request_headers=request_headers,
                                                                                     all_request_params=all_request_params,
                                                                                     routing_key=routing_key)

    def thing_park_process_request_v5_patch5(self, body: str, request_headers: dict, all_request_params: dict,
                                             routing_key: str):
        return self.thing_park_integration_controller.process_request_using_patch5(body=body,
                                                                                   request_headers=request_headers,
                                                                                   all_request_params=all_request_params,
                                                                                   routing_key=routing_key)

    def thing_park_process_request_v13_post13(self, body: str, request_headers: dict, all_request_params: dict,
                                              routing_key: str):
        return self.thing_park_integration_controller.process_request_using_post13(body=body,
                                                                                   request_headers=request_headers,
                                                                                   all_request_params=all_request_params,
                                                                                   routing_key=routing_key)

    def thing_park_process_request_v5_put5(self, body: str, request_headers: dict, all_request_params: dict,
                                           routing_key: str):
        return self.thing_park_integration_controller.process_request_using_put5(body=body,
                                                                                 request_headers=request_headers,
                                                                                 all_request_params=all_request_params,
                                                                                 routing_key=routing_key)

    def sig_fox_process_request_v3_delete3(self, body: str, request_headers: dict, routing_key: str):
        return self.sig_fox_integration_controller.process_request_using_delete3(body=body,
                                                                                 request_headers=request_headers,
                                                                                 routing_key=routing_key)

    def sig_fox_process_request_v3_get3(self, body: str, request_headers: dict, routing_key: str):
        return self.sig_fox_integration_controller.process_request_using_get3(body=body,
                                                                              request_headers=request_headers,
                                                                              routing_key=routing_key)

    def sig_fox_process_request_v3_head3(self, body: str, request_headers: dict, routing_key: str):
        return self.sig_fox_integration_controller.process_request_using_head3(body=body,
                                                                               request_headers=request_headers,
                                                                               routing_key=routing_key)

    def sig_fox_process_request_v3_options3(self, body: str, request_headers: dict, routing_key: str):
        return self.sig_fox_integration_controller.process_request_using_options3(body=body,
                                                                                  request_headers=request_headers,
                                                                                  routing_key=routing_key)

    def sig_fox_process_request_v3_patch3(self, body: str, request_headers: dict, routing_key: str):
        return self.sig_fox_integration_controller.process_request_using_patch3(body=body,
                                                                                request_headers=request_headers,
                                                                                routing_key=routing_key)

    def sig_fox_process_request_v11_post11(self, body: str, request_headers: dict, routing_key: str):
        return self.sig_fox_integration_controller.process_request_using_post11(body=body,
                                                                                request_headers=request_headers,
                                                                                routing_key=routing_key)

    def sig_fox_process_request_v3_put3(self, body: str, request_headers: dict, routing_key: str):
        return self.sig_fox_integration_controller.process_request_using_put3(body=body,
                                                                              request_headers=request_headers,
                                                                              routing_key=routing_key)

    def assign_scheduler_event_to_edge(self, edge_id: EdgeId, scheduler_event_id: SchedulerEventId) -> SchedulerEventInfo:
        edge_id = self.get_id(edge_id)
        scheduler_event_id = self.get_id(scheduler_event_id)
        return self.scheduler_event_controller.assign_scheduler_event_to_edge_using_post(edge_id=edge_id,
                                                                                         scheduler_event_id=scheduler_event_id)

    def delete_scheduler_event(self, scheduler_event_id: SchedulerEventId) -> None:
        scheduler_event_id = self.get_id(scheduler_event_id)
        return self.scheduler_event_controller.delete_scheduler_event_using_delete(
            scheduler_event_id=scheduler_event_id)

    def get_all_scheduler_events(self, edge_id: EdgeId) -> List[SchedulerEventInfo]:
        edge_id = self.get_id(edge_id)
        return self.scheduler_event_controller.get_all_scheduler_events_using_get(edge_id=edge_id)

    def get_edge_scheduler_events(self, edge_id: EdgeId, page_size: int, page: int,text_search: Optional[str] = None,
                                  sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataSchedulerEventInfo:
        edge_id = self.get_id(edge_id)
        return self.scheduler_event_controller.get_edge_scheduler_events_using_get(edge_id=edge_id, page_size=page_size,
                                                                                   page=page, text_search=text_search,
                                                                                   sort_property=sort_property,
                                                                                   sort_order=sort_order)

    def get_scheduler_event_by_id(self, scheduler_event_id: SchedulerEventId) -> SchedulerEvent:
        scheduler_event_id = self.get_id(scheduler_event_id)
        return self.scheduler_event_controller.get_scheduler_event_by_id_using_get(
            scheduler_event_id=scheduler_event_id)

    def get_scheduler_event_info_by_id(self, scheduler_event_id: SchedulerEventId) -> SchedulerEventWithCustomerInfo:
        scheduler_event_id = self.get_id(scheduler_event_id)
        return self.scheduler_event_controller.get_scheduler_event_info_by_id_using_get(
            scheduler_event_id=scheduler_event_id)

    def get_scheduler_events_by_ids(self, scheduler_event_ids: list) -> List[SchedulerEventInfo]:
        return self.scheduler_event_controller.get_scheduler_events_by_ids_using_get(
            scheduler_event_ids=str(scheduler_event_ids))

    def get_scheduler_events(self, type: Optional[str] = None) -> List[SchedulerEventWithCustomerInfo]:
        return self.scheduler_event_controller.get_scheduler_events_using_get(type=type)

    def save_scheduler_event(self, body: Optional[SchedulerEvent] = None) -> SchedulerEvent:
        return self.scheduler_event_controller.save_scheduler_event_using_post(body=body)

    def unassign_scheduler_event_from_edge(self, edge_id: EdgeId, scheduler_event_id: SchedulerEventId) -> SchedulerEventInfo:
        edge_id = self.get_id(edge_id)
        scheduler_event_id = self.get_id(scheduler_event_id)
        return self.scheduler_event_controller.unassign_scheduler_event_from_edge_using_delete(edge_id=edge_id,
                                                                                               scheduler_event_id=scheduler_event_id)

    def download_dashboard_report(self, dashboard_id: DashboardId,
                                  body: Union[dict, str, list, bytes, None, RESTResponse, tuple, Any] = None):
        dashboard_id = self.get_id(dashboard_id)
        return self.report_controller.download_dashboard_report_using_post(dashboard_id=dashboard_id, body=body)

    def download_test_report(self, body: Optional[ReportConfig], reports_server_endpoint_url: Optional[str] = None):
        return self.report_controller.download_test_report_using_post(body=body,
                                                                      reports_server_endpoint_url=reports_server_endpoint_url)

    def get_server_time(self, ) -> int:
        return self.dashboard_controller.get_server_time_using_get()

    def get_dashboards_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size: int, page: int,
                                         text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataDashboardInfo:
        entity_group_id = self.get_id(entity_group_id)
        return self.dashboard_controller.get_dashboards_by_entity_group_id_using_get(entity_group_id=entity_group_id,
                                                                                     page_size=page_size, page=page,
                                                                                     text_search=text_search,
                                                                                     sort_property=sort_property,
                                                                                     sort_order=sort_order)

    def delete_dashboard(self, dashboard_id: DashboardId) -> None:
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.delete_dashboard_using_delete(dashboard_id=dashboard_id)

    def save_dashboard(self, body: Optional[Dashboard] = None) -> Dashboard:
        return self.dashboard_controller.save_dashboard_using_post(body=body)

    def get_home_dashboard_info(self, ) -> HomeDashboardInfo:
        return self.dashboard_controller.get_home_dashboard_info_using_get()

    def get_tenant_home_dashboard_info(self, ) -> HomeDashboardInfo:
        return self.dashboard_controller.get_tenant_home_dashboard_info_using_get()

    def set_customer_home_dashboard_info(self, body: Optional[HomeDashboardInfo] = None) -> None:
        return self.dashboard_controller.set_customer_home_dashboard_info_using_post(body=body)

    def get_tenant_dashboards_v1(self, tenant_id: TenantId, page_size: int, page: int,text_search: Optional[str] = None,
                                 sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataDashboardInfo:
        tenant_id = self.get_id(tenant_id)
        return self.dashboard_controller.get_tenant_dashboards_using_get1(tenant_id=tenant_id, page_size=page_size,
                                                                          page=page, text_search=text_search,
                                                                          sort_property=sort_property,
                                                                          sort_order=sort_order)

    def get_dashboard_info_by_id(self, dashboard_id: DashboardId) -> DashboardInfo:
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.get_dashboard_info_by_id_using_get(dashboard_id=dashboard_id)

    def get_home_dashboard(self, ) -> HomeDashboard:
        return self.dashboard_controller.get_home_dashboard_using_get()

    def get_max_datapoints_limit(self, ) -> int:
        return self.dashboard_controller.get_max_datapoints_limit_using_get()

    def get_dashboards_by_ids(self, dashboard_ids: list) -> List[DashboardInfo]:
        dashboard_ids = ','.join(dashboard_ids)
        return self.dashboard_controller.get_dashboards_by_ids_using_get(dashboard_ids=dashboard_ids)

    def get_customer_home_dashboard_info(self, ) -> HomeDashboardInfo:
        return self.dashboard_controller.get_customer_home_dashboard_info_using_get()

    def get_tenant_dashboards(self, page_size: int, page: int, mobile: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None,
                              sort_order: Optional[str] = None) -> PageDataDashboardInfo:
        return self.dashboard_controller.get_tenant_dashboards_using_get(page_size=page_size, page=page, mobile=mobile,
                                                                         text_search=text_search,
                                                                         sort_property=sort_property,
                                                                         sort_order=sort_order)

    def get_user_dashboards(self, page_size: int, page: int, mobile: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None,
                            sort_order: Optional[str] = None, operation: Optional[str] = None, user_id: Optional[str] = None) -> PageDataDashboardInfo:
        user_id = self.get_id(user_id)
        return self.dashboard_controller.get_user_dashboards_using_get(page_size=page_size, page=page, mobile=mobile,
                                                                       text_search=text_search,
                                                                       sort_property=sort_property,
                                                                       sort_order=sort_order, operation=operation,
                                                                       user_id=user_id)

    def import_group_dashboards(self, entity_group_id: EntityGroupId, body: Optional[List[Dashboard]] = None, overwrite: Optional[bool] = None) -> None:
        entity_group_id = self.get_id(entity_group_id)
        return self.dashboard_controller.import_group_dashboards_using_post(entity_group_id=entity_group_id, body=body,
                                                                            overwrite=overwrite)

    def set_tenant_home_dashboard_info(self, body: Optional[HomeDashboardInfo] = None) -> None:
        return self.dashboard_controller.set_tenant_home_dashboard_info_using_post(body=body)

    def export_group_dashboards(self, entity_group_id: EntityGroupId, limit: int) -> List[Dashboard]:
        entity_group_id = self.get_id(entity_group_id)
        return self.dashboard_controller.export_group_dashboards_using_get(entity_group_id=entity_group_id, limit=limit)

    def check_integration_connection(self, body: Optional[Integration] = None) -> None:
        return self.integration_controller.check_integration_connection_using_post(body=body)

    def delete_integration(self, integration_id: IntegrationId) -> None:
        integration_id = self.get_id(integration_id)
        return self.integration_controller.delete_integration_using_delete(integration_id=integration_id)

    def get_integration_by_id(self, integration_id: IntegrationId) -> Integration:
        integration_id = self.get_id(integration_id)
        return self.integration_controller.get_integration_by_id_using_get(integration_id=integration_id)

    def get_integration_by_routing_key(self, routing_key: str) -> Integration:
        return self.integration_controller.get_integration_by_routing_key_using_get(routing_key=routing_key)

    def get_integrations_by_ids(self, integration_ids: list) -> List[Integration]:
        integration_ids = ','.join(integration_ids)
        return self.integration_controller.get_integrations_by_ids_using_get(integration_ids=integration_ids)

    def get_integration_infos(self, page_size: int, page: int, is_edge_template: Optional[bool],
                              text_search: Optional[str] = None,
                              sort_property: Optional[str] = None,
                              sort_order: Optional[str] = None) -> PageDataIntegrationInfo:
        return self.integration_controller.get_integration_infos_using_get(page_size=page_size, page=page,
                                                                           is_edge_template=is_edge_template,
                                                                           text_search=text_search,
                                                                           sort_property=sort_property,
                                                                           sort_order=sort_order)

    def get_integrations(self, page_size: int, page: int, is_edge_template: Optional[bool], text_search: Optional[str] = None,
                             sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataIntegration:
        return self.integration_controller.get_integrations_using_get(page_size=page_size, page=page,
                                                                      is_edge_template=is_edge_template,
                                                                      text_search=text_search,
                                                                      sort_property=sort_property,
                                                                      sort_order=sort_order)

    def save_integration(self, body: Optional[Integration] = None) -> Integration:
        return self.integration_controller.save_integration_using_post(body=body)

    def get_custom_menu(self, ) -> CustomMenu:
        return self.custom_menu_controller.get_custom_menu_using_get()

    def create_custom_menu(self, body: Optional[CustomMenuInfo] = None, assign_to_list: Optional[List[str]] = None, force: Optional[bool] = None) -> CustomMenu:
        if assign_to_list is not None:
            assign_to_list = '.'.join(assign_to_list)

        return self.custom_menu_controller.create_custom_menu(body=body, assign_to_list=assign_to_list, force=force)

    def delete_custom_menu(self, custom_menu_id: CustomMenuId, force: Optional[bool] = None) -> None:
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

    def get_custom_menu_infos(self, page_size: int, page: int, scope: Optional[str] = None, assignee_type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None):
        return self.custom_menu_controller.get_custom_menu_infos(page_size=page_size, page=page, scope=scope, assignee_type=assignee_type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def update_custom_menu_assignee_list(self, id: CustomMenuId, assignee_type: str, body: List[str], force: Optional[bool] = None):
        id = self.get_id(id)
        return self.custom_menu_controller.update_custom_menu_assignee_list(id=id, assignee_type=assignee_type, body=body, force=force)

    def update_custom_menu_config(self, id: CustomMenuId, body: CustomMenuConfig) -> CustomMenu:
        id = self.get_id(id)
        return self.custom_menu_controller.update_custom_menu_config(custom_menu_id=id, body=body)

    def update_custom_menu_name(self, id: CustomMenuId, body: str):
        id = self.get_id(id)
        return self.custom_menu_controller.update_custom_menu_name(custom_menu_id=id, body=body)

    def get_lwm2m_bootstrap_security_info(self, is_bootstrap_server: bool) -> ServerSecurityConfig:
        return self.lwm2m_controller.get_lwm2m_bootstrap_security_info_using_get(
            is_bootstrap_server=is_bootstrap_server)

    def get_custom_translation(self, locale_code: str) -> CustomTranslation:
        return self.custom_translation_controller.get_custom_translation_using_get(locale_code=locale_code)

    def save_custom_translation(self, locale_code: str, body: CustomTranslation) -> CustomTranslation:
        return self.custom_translation_controller.save_custom_translation_using_post(body=body, locale_code=locale_code)

    def delete_custom_translation(self, locale_code: str) -> None:
        return self.custom_translation_controller.delete_custom_translation(locale_code=locale_code)

    def delete_custom_translation_key(self, locale_code: str, key_path: str):
        return self.custom_translation_controller.delete_custom_translation_key(locale_code=locale_code,
                                                                                key_path=key_path)

    def patch_custom_translation(self, body: CustomTranslation, locale_code: str):
        return self.custom_translation_controller.patch_custom_translation(body=body, locale_code=locale_code)

    def upload_custom_translation(self, locale_code: str, file):
        return self.custom_translation_controller.upload_custom_translation(locale_code=locale_code, file=file)

    def get_merged_custom_translation(self, locale_code: str) -> CustomTranslation:
        return self.custom_translation_controller.get_merged_custom_translation(locale_code=locale_code)

    def delete_role(self, role_id: RoleId) -> None:
        role_id = self.get_id(role_id)
        return self.role_controller.delete_role_using_delete(role_id=role_id)

    def get_role_by_id(self, role_id: RoleId) -> Role:
        role_id = self.get_id(role_id)
        return self.role_controller.get_role_by_id_using_get(role_id=role_id)

    def get_roles_by_ids(self, role_ids: list) -> List[Role]:
        role_ids = ','.join(role_ids)
        return self.role_controller.get_roles_by_ids_using_get(role_ids=role_ids)

    def get_roles(self, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None,
                  sort_property: Optional[str] = None, sort_order: Optional[str] = None, ) -> PageDataRole:
        return self.role_controller.get_roles_using_get(page_size=page_size, page=page, type=type,
                                                        text_search=text_search, sort_property=sort_property,
                                                        sort_order=sort_order)

    def save_role(self, body: Optional[Role] = None) -> Role:
        return self.role_controller.save_role_using_post(body=body)

    def delete_blob_entity(self, blob_entity_id: BlobEntityId) -> None:
        blob_entity_id = self.get_id(blob_entity_id)
        return self.blob_entity_controller.delete_blob_entity_using_delete(blob_entity_id=blob_entity_id)

    def download_blob_entity(self, blob_entity_id: BlobEntityId) -> Resource:
        blob_entity_id = self.get_id(blob_entity_id)
        return self.blob_entity_controller.download_blob_entity_using_get(blob_entity_id=blob_entity_id)

    def get_blob_entities_by_ids(self, blob_entity_ids: list) -> List[BlobEntityInfo]:
        return self.blob_entity_controller.get_blob_entities_by_ids_using_get(blob_entity_ids=str(blob_entity_ids))

    def get_blob_entities(self, page_size: int, page: int, type: Optional[str] = None,text_search: Optional[str] = None, sort_property: Optional[str] = None,
                          sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None) -> PageDataBlobEntityWithCustomerInfo:
        return self.blob_entity_controller.get_blob_entities_using_get(page_size=page_size, page=page, type=type,
                                                                       text_search=text_search,
                                                                       sort_property=sort_property,
                                                                       sort_order=sort_order, start_time=start_time,
                                                                       end_time=end_time)

    def get_blob_entity_info_by_id(self, blob_entity_id: BlobEntityId) -> BlobEntityWithCustomerInfo:
        blob_entity_id = self.get_id(blob_entity_id)
        return self.blob_entity_controller.get_blob_entity_info_by_id_using_get(blob_entity_id=blob_entity_id)

    def get_tenant_infos(self, page_size: int, page: int,text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataTenantInfo:
        return self.tenant_controller.get_tenant_infos_using_get(page_size=page_size, page=page,
                                                                 text_search=text_search, sort_property=sort_property,
                                                                 sort_order=sort_order)

    def get_tenant_by_id(self, tenant_id: TenantId) -> Tenant:
        tenant_id = self.get_id(tenant_id)
        return self.tenant_controller.get_tenant_by_id_using_get(tenant_id=tenant_id)

    def save_tenant(self, body: Optional[Tenant] = None) -> Tenant:
        return self.tenant_controller.save_tenant_using_post(body=body)

    def get_tenants(self, page_size: int, page: int,text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataTenant:
        return self.tenant_controller.get_tenants_using_get(page_size=page_size, page=page, text_search=text_search,
                                                            sort_property=sort_property, sort_order=sort_order)

    def get_tenants_by_ids(self, tenant_ids: list) -> List[Tenant]:
        return self.tenant_controller.get_tenants_by_ids_using_get(tenant_ids=str(tenant_ids))

    def get_tenant_info_by_id(self, tenant_id: TenantId) -> TenantInfo:
        tenant_id = self.get_id(tenant_id)
        return self.tenant_controller.get_tenant_info_by_id_using_get(tenant_id=tenant_id)

    def delete_tenant(self, tenant_id: TenantId) -> None:
        tenant_id = self.get_id(tenant_id)
        return self.tenant_controller.delete_tenant_using_delete(tenant_id=tenant_id)

    def chirp_stack_process_request_delete(self, body: str, request_headers: dict, routing_key: str):
        return self.chirp_stack_integration_controller.process_request_using_delete(body=body,
                                                                                    request_headers=request_headers,
                                                                                    routing_key=routing_key)

    def chirp_stack_process_request_get(self, body: str, request_headers: dict, routing_key: str):
        return self.chirp_stack_integration_controller.process_request_using_get(body=body,
                                                                                 request_headers=request_headers,
                                                                                 routing_key=routing_key)

    def chirp_stack_process_request_head(self, body: str, request_headers: dict, routing_key: str):
        return self.chirp_stack_integration_controller.process_request_using_head(body=body,
                                                                                  request_headers=request_headers,
                                                                                  routing_key=routing_key)

    def chirp_stack_process_request_options(self, body: str, request_headers: dict, routing_key: str):
        return self.chirp_stack_integration_controller.process_request_using_options(body=body,
                                                                                     request_headers=request_headers,
                                                                                     routing_key=routing_key)

    def chirp_stack_process_request_patch(self, body: str, request_headers: dict, routing_key: str):
        return self.chirp_stack_integration_controller.process_request_using_patch(body=body,
                                                                                   request_headers=request_headers,
                                                                                   routing_key=routing_key)

    def chirp_stack_process_request_post(self, body: str, request_headers: dict, routing_key: str):
        return self.chirp_stack_integration_controller.process_request_using_post(body=body,
                                                                                  request_headers=request_headers,
                                                                                  routing_key=routing_key)

    def chirp_stack_process_request_put(self, body: str, request_headers: dict, routing_key: str):
        return self.chirp_stack_integration_controller.process_request_using_put(body=body,
                                                                                 request_headers=request_headers,
                                                                                 routing_key=routing_key)

    def get_current_login_white_label_params(self, ) -> LoginWhiteLabelingParams:
        return self.white_labeling_controller.get_current_login_white_label_params_using_get()

    def get_current_white_label_params(self, ) -> WhiteLabelingParams:
        return self.white_labeling_controller.get_current_white_label_params_using_get()

    def get_login_white_label_params(self, logo_image_checksum: str, favicon_checksum: str) -> LoginWhiteLabelingParams:
        return self.white_labeling_controller.get_login_white_label_params_using_get(
            logo_image_checksum=logo_image_checksum, favicon_checksum=favicon_checksum)

    def get_white_label_params(self, logo_image_checksum: str, favicon_checksum: str) -> WhiteLabelingParams:
        return self.white_labeling_controller.get_white_label_params_using_get(logo_image_checksum=logo_image_checksum,
                                                                               favicon_checksum=favicon_checksum)

    def get_widgets_bundles_by_ids(self, widget_bundle_ids: List[str]) -> List[WidgetsBundle]:
        widget_bundle_ids = ','.join(widget_bundle_ids)
        return self.widgets_bundle_controller.get_widgets_bundles_by_ids_using_get(widget_bundle_ids=widget_bundle_ids)

    def is_customer_white_labeling_allowed(self, ) -> bool:
        return self.white_labeling_controller.is_customer_white_labeling_allowed_using_get()

    def is_white_labeling_allowed(self, ) -> bool:
        return self.white_labeling_controller.is_white_labeling_allowed_using_get()

    def preview_white_label_params(self, body: Optional[WhiteLabelingParams] = None) -> WhiteLabelingParams:
        return self.white_labeling_controller.preview_white_label_params_using_post(body=body)

    def save_login_white_label_params(self, body: Optional[LoginWhiteLabelingParams] = None) -> LoginWhiteLabelingParams:
        return self.white_labeling_controller.save_login_white_label_params_using_post(body=body)

    def save_white_label_params(self, body: Optional[WhiteLabelingParams] = None) -> WhiteLabelingParams:
        return self.white_labeling_controller.save_white_label_params_using_post(body=body)

    def delete_ota_package(self, ota_package_id: OtaPackageId) -> None:
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.delete_ota_package_using_delete(ota_package_id=ota_package_id)

    def get_ota_packages_v1(self, device_profile_id: DeviceProfileId, type: str, page_size: int, page: int,
                           text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataOtaPackageInfo:
        device_profile_id = self.get_id(device_profile_id)
        return self.ota_package_controller.get_ota_packages_using_get1(device_profile_id=device_profile_id, type=type,
                                                                       page_size=page_size, page=page,
                                                                       text_search=text_search,
                                                                       sort_property=sort_property,
                                                                       sort_order=sort_order)

    def save_ota_package_data(self, ota_package_id: OtaPackageId, checksum=None, checksum_algorithm: str = None, file=None) -> OtaPackageInfo:
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.save_ota_package_data_using_post(checksum_algorithm=checksum_algorithm,
                                                                            ota_package_id=ota_package_id, file=file,
                                                                            checksum=checksum)

    def save_ota_package_info(self, body: Optional[SaveOtaPackageInfoRequest] = None) -> OtaPackageInfo:
        return self.ota_package_controller.save_ota_package_info_using_post(body=body)

    def get_ota_packages(self, page_size: int, page: int,text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataOtaPackageInfo:
        return self.ota_package_controller.get_ota_packages_using_get(page_size=page_size, page=page,
                                                                      text_search=text_search,
                                                                      sort_property=sort_property,
                                                                      sort_order=sort_order)

    def get_ota_package_by_id(self, ota_package_id: OtaPackageId) -> OtaPackage:
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.get_ota_package_by_id_using_get(ota_package_id=ota_package_id)

    def get_group_ota_packages(self, group_id: EntityGroupId, type: str, page_size: int, page: int,text_search: Optional[str] = None,
                               sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> PageDataOtaPackageInfo:
        group_id = self.get_id(group_id)
        return self.ota_package_controller.get_group_ota_packages_using_get(group_id=group_id, type=type,
                                                                            page_size=page_size, page=page,
                                                                            text_search=text_search,
                                                                            sort_property=sort_property,
                                                                            sort_order=sort_order)

    def download_ota_package(self, ota_package_id: OtaPackageId) -> Resource:
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.download_ota_package_using_get(ota_package_id=ota_package_id)

    def get_ota_package_info_by_id(self, ota_package_id: OtaPackageId) -> OtaPackageInfo:
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.get_ota_package_info_by_id_using_get(ota_package_id=ota_package_id)

    def add_entities_to_entity_group(self, entity_group_id: EntityGroupId, body: Optional[List[str]] = None) -> None:
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.add_entities_to_entity_group_using_post(entity_group_id=entity_group_id,
                                                                                    body=body)

    def assign_entity_group_to_edge(self, edge_id: EdgeId, group_type: str,
                                    entity_group_id: EntityGroupId) -> EntityGroup:
        edge_id = self.get_id(edge_id)
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.assign_entity_group_to_edge_using_post(edge_id=edge_id,
                                                                                   group_type=group_type,
                                                                                   entity_group_id=entity_group_id)

    def delete_entity_group(self, entity_group_id: EntityGroupId) -> None:
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.delete_entity_group_using_delete(entity_group_id=entity_group_id)

    def get_all_edge_entity_groups(self, edge_id: EdgeId, group_type: str) -> List[EntityGroupInfo]:
        edge_id = self.get_id(edge_id)
        return self.entity_group_controller.get_all_edge_entity_groups_using_get(edge_id=edge_id, group_type=group_type)

    def get_edge_entity_groups(self, edge_id: EdgeId, group_type: str, page_size: int, page: int, sort_property: Optional[str] = None,
                               sort_order: Optional[str] = None,) -> PageDataEntityGroupInfo:
        edge_id = self.get_id(edge_id)
        return self.entity_group_controller.get_edge_entity_groups_using_get(edge_id=edge_id, group_type=group_type,
                                                                             page_size=page_size, page=page,
                                                                             sort_property=sort_property,
                                                                             sort_order=sort_order)

    def get_entities(self, entity_group_id: EntityGroupId, page_size: int, page: int,text_search: Optional[str] = None,
                     sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataShortEntityView:
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.get_entities_using_get(entity_group_id=entity_group_id, page_size=page_size,
                                                                   page=page, text_search=text_search,
                                                                   sort_property=sort_property, sort_order=sort_order)

    def get_entity_group_all_by_owner_and_type(self, owner_type: str, owner_id: UserId,
                                               group_type: str) -> EntityGroupInfo:
        owner_id = self.get_id(owner_id)
        return self.entity_group_controller.get_entity_group_all_by_owner_and_type_using_get(owner_type=owner_type,
                                                                                             owner_id=owner_id,
                                                                                             group_type=group_type)

    def get_entity_groups_by_owner_and_type_and_page_link(self, owner_type: str, owner_id: UserId, group_type: str,
                                                          page_size: int, page: int, text_search: Optional[str] = None,
                                                          sort_property: Optional[str] = None,
                                                          sort_order: Optional[str] = None) -> PageDataEntityGroupInfo:
        owner_id = self.get_id(owner_id)
        return self.entity_group_controller.get_entity_groups_by_owner_and_type_and_page_link_using_get(
            owner_type=owner_type,
            owner_id=owner_id,
            group_type=group_type, page_size=page_size,
            page=page, text_search=text_search,
            sort_property=sort_property, sort_order=sort_order)

    def get_entity_group_by_id(self, entity_group_id: EntityGroupId) -> EntityGroupInfo:
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.get_entity_group_by_id_using_get(entity_group_id=entity_group_id)

    def get_entity_group_by_owner_and_name_and_type(self, owner_id: UserId, group_type: str,
                                                    group_name: str) -> EntityGroupInfo:
        owner_type = self.get_type(owner_id)
        owner_id = self.get_id(owner_id)
        return self.entity_group_controller.get_entity_group_by_owner_and_name_and_type_using_get(owner_type=owner_type,
                                                                                                  owner_id=owner_id,
                                                                                                  group_type=group_type,
                                                                                                  group_name=group_name)

    def get_entity_groups_by_ids(self, entity_group_ids: List[str]) -> List[EntityGroupInfo]:
        entity_group_ids = ','.join(entity_group_ids)
        return self.entity_group_controller.get_entity_groups_by_ids_using_get(entity_group_ids=entity_group_ids)

    def get_entity_groups_by_owner_and_type(self, owner_type: str, owner_id: UserId,
                                            group_type: str) -> List[EntityGroupInfo]:
        owner_id = self.get_id(owner_id)
        return self.entity_group_controller.get_entity_groups_by_owner_and_type_using_get(owner_type=owner_type,
                                                                                          owner_id=owner_id,
                                                                                          group_type=group_type)

    def get_entity_groups_by_type(self, group_type: str,
                                  include_shared: Optional[bool] = None) -> List[EntityGroupInfo]:
        return self.entity_group_controller.get_entity_groups_by_type_using_get(group_type=group_type, include_shared=include_shared)

    def get_entity_groups_for_entity(self, entity_id: EntityId) -> List[EntityGroupId]:
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        return self.entity_group_controller.get_entity_groups_for_entity_using_get(entity_type=entity_type,
                                                                                   entity_id=entity_id)

    def get_group_entity(self, entity_group_id: EntityGroupId, entity_id: EntityId) -> ShortEntityView:
        entity_group_id = self.get_id(entity_group_id)
        entity_id = self.get_id(entity_id)
        return self.entity_group_controller.get_group_entity_using_get(entity_group_id=entity_group_id,
                                                                       entity_id=entity_id)

    def get_owners(self, page_size: int, page: int, text_search: Optional[str] = None,
                   sort_property: Optional[str] = None, sort_order: Optional[str] = None,) -> PageDataContactBasedobject:
        return self.entity_group_controller.get_owners_using_get(page_size=page_size, page=page,
                                                                 text_search=text_search, sort_property=sort_property,
                                                                 sort_order=sort_order)

    def make_entity_group_private(self, entity_group_id: EntityGroupId) -> None:
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.make_entity_group_private_using_post(entity_group_id=entity_group_id)

    def make_entity_group_public(self, entity_group_id: EntityGroupId) -> None:
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.make_entity_group_public_using_post(entity_group_id=entity_group_id)

    def remove_entities_from_entity_group(self, entity_group_id: EntityGroupId,
                                          body: Optional[List[str]] = None) -> None:
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.remove_entities_from_entity_group_using_post(
            entity_group_id=entity_group_id, body=body)

    def save_entity_group(self, body: Optional[EntityGroup] = None) -> EntityGroupInfo:
        return self.entity_group_controller.save_entity_group_using_post(body=body)

    def share_entity_group_to_child_owner_user_group(self, entity_group_id: EntityGroupId, user_group_id: EntityId,
                                                     role_id: RoleId) -> None:
        entity_group_id = self.get_id(entity_group_id)
        user_group_id = self.get_id(user_group_id)
        role_id = self.get_id(role_id)
        return self.entity_group_controller.share_entity_group_to_child_owner_user_group_using_post(
            entity_group_id=entity_group_id, user_group_id=user_group_id, role_id=role_id)

    def share_entity_group(self, entity_group_id: EntityGroupId, body: Optional[ShareGroupRequest] = None) -> None:
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.share_entity_group_using_post(entity_group_id=entity_group_id, body=body)

    def unassign_entity_group_from_edge(self, edge_id: EdgeId,
                                        group_type: str,
                                        entity_group_id: EntityGroupId) -> EntityGroup:
        edge_id = self.get_id(edge_id)
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.unassign_entity_group_from_edge_using_delete(edge_id=edge_id,
                                                                                         group_type=group_type,
                                                                                         entity_group_id=entity_group_id)

    # Subscription Controller
    def get_tenant_profile_data_by_id(self, tenant_profile_id: TenantProfileId) -> TenantProfileData:
        tenant_profile_id = self.get_id(tenant_profile_id)
        return self.subscription_controller.get_tenant_profile_data_by_id_using_get(tenant_profile_id=tenant_profile_id)

    def get_tenant_profile_data(self, ) -> TenantProfileData:
        return self.subscription_controller.get_tenant_profile_data_using_get()

    def get_tenant_subscription_usage(self) -> SubscriptionUsage:
        return self.subscription_controller.get_tenant_subscription_usage_using_get()

    # Solution Controller
    def get_solution_template_details(self, solution_template_id) -> TenantSolutionTemplateDetails:
        return self.solution_controller.get_solution_template_details_using_get(
            solution_template_id=solution_template_id)

    def get_solution_template_infos(self) -> List[TenantSolutionTemplateInfo]:
        return self.solution_controller.get_solution_template_infos_using_get()

    def get_solution_template_instructions(self, solution_template_id) -> TenantSolutionTemplateInstructions:
        return self.solution_controller.get_solution_template_instructions_using_get(
            solution_template_id=solution_template_id)

    def install_solution_template(self, solution_template_id) -> SolutionInstallResponse:
        return self.solution_controller.install_solution_template_using_post(solution_template_id=solution_template_id)

    def uninstall_solution_template(self, solution_template_id) -> None:
        return self.solution_controller.uninstall_solution_template_using_delete(
            solution_template_id=solution_template_id)

    # Asset Profile Controller
    def delete_asset_profile(self, asset_profile_id: AssetProfileId):
        asset_profile_id = self.get_id(asset_profile_id)
        return self.asset_profile_controller.delete_asset_profile_using_delete(asset_profile_id=asset_profile_id)

    def get_asset_profile_info_by_id(self, asset_profile_id: AssetProfileId) -> AssetProfileInfo:
        asset_profile_id = self.get_id(asset_profile_id)
        return self.asset_profile_controller.get_asset_profile_info_by_id_using_get(asset_profile_id=asset_profile_id)

    def get_asset_profile_infos(self, page_size: int, page: int, text_search: Optional[str] = None,
                                sort_property: Optional[str] = None,
                                sort_order: Optional[str] = None) -> PageDataAssetProfileInfo:
        return self.asset_profile_controller.get_asset_profile_infos_using_get(page_size=page_size, page=page,
                                                                               text_search=text_search,
                                                                               sort_property=sort_property,
                                                                               sort_order=sort_order)

    def get_asset_profiles_by_ids(self, asset_profile_ids: List[str]) -> List[AssetProfileInfo]:
        asset_profile_ids = ','.join(asset_profile_ids)
        return self.asset_profile_controller.get_asset_profiles_by_ids_using_get(asset_profile_ids=asset_profile_ids)

    def get_asset_profiles(self, page_size: int, page: int, text_search: Optional[str] = None,
                           sort_property: Optional[str] = None,
                           sort_order: Optional[str] = None) -> PageDataAssetProfile:
        return self.asset_profile_controller.get_asset_profiles_using_get(page_size=page_size, page=page,
                                                                          text_search=text_search,
                                                                          sort_property=sort_property,
                                                                          sort_order=sort_order)

    def get_default_asset_profile_info(self) -> AssetProfileInfo:
        return self.asset_profile_controller.get_default_asset_profile_info_using_get()

    def save_asset_profile(self, body: AssetProfile) -> AssetProfile:
        return self.asset_profile_controller.save_asset_profile_using_post(body=body)

    def set_default_asset_profile(self, asset_profile_id: AssetProfileId) -> AssetProfile:
        asset_profile_id = self.get_id(asset_profile_id)
        return self.asset_profile_controller.set_default_asset_profile_using_post(asset_profile_id=asset_profile_id)

    def get_features_info(self) -> FeaturesInfo:
        return self.admin_controller.get_features_info_using_get()

    def get_license_usage_info(self) -> LicenseUsageInfo:
        return self.admin_controller.get_license_usage_info_using_get()

    def get_system_info(self) -> SystemInfo:
        return self.admin_controller.get_system_info_using_get()

    def assign_alarm(self, alarm_id: AlarmId, assignee_id: str) -> Alarm:
        alarm_id = self.get_id(alarm_id)
        return self.alarm_controller.assign_alarm_using_post(alarm_id=alarm_id, assignee_id=assignee_id)

    def get_all_asset_infos(self, page_size: int, page: int, text_search: Optional[str] = None,
                            sort_property: Optional[str] = None,
                            sort_order: Optional[str] = None, include_customers: Optional[bool] = None,
                            asset_profile_id: Optional[AssetProfileId] = None) -> PageDataAssetInfo:
        asset_profile_id = self.get_id(asset_profile_id)
        return self.asset_controller.get_all_asset_infos_using_get(page_size=page_size, page=page,
                                                                   text_search=text_search,
                                                                   sort_property=sort_property,
                                                                   sort_order=sort_order,
                                                                   include_customers=include_customers,
                                                                   asset_profile_id=asset_profile_id)

    def get_all_dashboards(self, page_size: int, page: int, text_search: Optional[str] = None,
                           sort_property: Optional[str] = None,
                           sort_order: Optional[str] = None,
                           include_customers: Optional[bool] = None) -> PageDataDashboardInfo:
        return self.dashboard_controller.get_all_dashboards_using_get(page_size=page_size, page=page,
                                                                      text_search=text_search,
                                                                      sort_property=sort_property,
                                                                      sort_order=sort_order,
                                                                      include_customers=include_customers)

    def get_all_device_infos(self, page_size: int, page: int, text_search: Optional[str] = None,
                             sort_property: Optional[str] = None,
                             sort_order: Optional[str] = None,
                             include_customers: Optional[bool] = None,
                             device_profile_id: Optional[DeviceProfileId] = None) -> PageDataDeviceInfo:
        if device_profile_id:
            device_profile_id = self.get_id(device_profile_id)

        return self.device_controller.get_all_device_infos_using_get(page_size=page_size, page=page,
                                                                     text_search=text_search,
                                                                     sort_property=sort_property,
                                                                     sort_order=sort_order,
                                                                     include_customers=include_customers,
                                                                     device_profile_id=device_profile_id)

    def get_customer_device_infos(self, customer_id: CustomerId, page_size: int, page: int, type: Optional[str] = None,
                                  device_profile_id: Optional[DeviceProfileId] = None,
                                  text_search: Optional[str] = None,
                                  sort_property: Optional[str] = None, sort_order: Optional[str] = None,
                                  active: Optional[bool] = None,
                                  include_customers: Optional[bool] = None) -> PageDataDeviceInfo:
        customer_id = self.get_id(customer_id)
        device_profile_id = self.get_id(device_profile_id)
        return self.device_controller.get_customer_device_infos_using_get(customer_id=customer_id, page_size=page_size,
                                                                          page=page, type=type,
                                                                          device_profile_id=device_profile_id,
                                                                          text_search=text_search,
                                                                          sort_property=sort_property,
                                                                          sort_order=sort_order, active=active,
                                                                          include_customers=include_customers)

    def get_entity_group_entity_info_by_id(self, entity_group_id: EntityGroupId) -> EntityInfo:
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.get_entity_group_entity_info_by_id_using_get(entity_group_id=entity_group_id)

    def get_entity_group_entity_infos_by_ids(self, entity_group_ids: List[str]) -> List[EntityInfo]:
        entity_group_ids = ','.join(entity_group_ids)
        return self.entity_group_controller.get_entity_group_entity_infos_by_ids_using_get(entity_group_ids=entity_group_ids)

    def get_entity_group_entity_infos_by_owner_and_type_and_page_link(self, owner_id: str, owner_type: str,
                                                                      group_type: str, page_size: int, page: int,
                                                                      text_search: Optional[str] = None,
                                                                      sort_property: Optional[str] = None,
                                                                      sort_order: Optional[
                                                                          str] = None) -> PageDataEntityInfo:
        return self.entity_group_controller.get_entity_group_entity_infos_by_owner_and_type_and_page_link_using_get(
            owner_id=owner_id, owner_type=owner_type, group_type=group_type, page_size=page_size, page=page,
            text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_entity_group_entity_infos_by_type_and_page_link(self, group_type: str, page_size: int, page: int,
                                                            text_search: Optional[str] = None,
                                                            sort_property: Optional[str] = None,
                                                            sort_order: Optional[
                                                                str] = None) -> PageDataEntityInfo:
        return self.entity_group_controller.get_entity_group_entity_infos_by_type_and_page_link_using_get(
            group_type=group_type, page_size=page_size, page=page,
            text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_entity_group_entity_infos_hierarchy_by_owner_and_type_and_page_link(self, owner_id: str, owner_type: str,
                                                                                group_type: str, page_size: int,
                                                                                page: int,
                                                                                text_search: Optional[str] = None,
                                                                                sort_property: Optional[str] = None,
                                                                                sort_order: Optional[
                                                                                    str] = None) -> PageDataEntityInfo:
        return self.entity_group_controller.get_entity_group_entity_infos_hierarchy_by_owner_and_type_and_page_link_using_get(
            owner_id=owner_id, owner_type=owner_type, group_type=group_type, page_size=page_size, page=page,
            text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_entity_groups_by_type_and_page_link(self, group_type: str, page_size: int, page: int,
                                                text_search: Optional[str] = None,
                                                sort_property: Optional[str] = None,
                                                sort_order: Optional[
                                                    str] = None) -> PageDataEntityGroupInfo:
        return self.entity_group_controller.get_entity_groups_by_type_and_page_link_using_get(group_type=group_type,
                                                                                              page_size=page_size,
                                                                                              page=page,
                                                                                              text_search=text_search,
                                                                                              sort_property=sort_property,
                                                                                              sort_order=sort_order)

    def get_entity_groups_hierarchy_by_owner_and_type_and_page_link(self, owner_id: str, owner_type: str,
                                                                    group_type: str, page_size: int,
                                                                    page: int,
                                                                    text_search: Optional[str] = None,
                                                                    sort_property: Optional[str] = None,
                                                                    sort_order: Optional[
                                                                        str] = None) -> PageDataEntityGroupInfo:
        return self.entity_group_controller.get_entity_groups_hierarchy_by_owner_and_type_and_page_link_using_get(
            owner_id=owner_id, owner_type=owner_type, group_type=group_type, page_size=page_size, page=page,
            text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_owner_info(self, owner_type: str, owner_id: str) -> EntityInfo:
        return self.entity_group_controller.get_owner_info_using_get(owner_type=owner_type, owner_id=owner_id)

    def get_owner_infos(self, page_size: int,
                        page: int,
                        text_search: Optional[str] = None,
                        sort_property: Optional[str] = None,
                        sort_order: Optional[
                            str] = None) -> PageDataEntityInfo:
        return self.entity_group_controller.get_owner_infos_using_get(page_size=page_size, page=page,
                                                                      text_search=text_search,
                                                                      sort_property=sort_property,
                                                                      sort_order=sort_order)

    def get_shared_entity_group_entity_infos_by_type_and_page_link(self, group_type: str, page_size: int,
                                                                   page: int,
                                                                   text_search: Optional[str] = None,
                                                                   sort_property: Optional[str] = None,
                                                                   sort_order: Optional[
                                                                       str] = None) -> PageDataEntityInfo:
        return self.entity_group_controller.get_shared_entity_group_entity_infos_by_type_and_page_link_using_get(
            group_type=group_type, page_size=page_size, page=page,
            text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_shared_entity_groups_by_type_and_page_link(self, group_type: str, page_size: int,
                                                       page: int,
                                                       text_search: Optional[str] = None,
                                                       sort_property: Optional[str] = None,
                                                       sort_order: Optional[
                                                           str] = None) -> PageDataEntityGroupInfo:
        return self.entity_group_controller.get_shared_entity_groups_by_type_and_page_link_using_get(
            group_type=group_type, page_size=page_size, page=page,
            text_search=text_search, sort_property=sort_property, sort_order=sort_order)

    def get_shared_entity_groups_by_type(self, group_type: str) -> List[EntityGroupInfo]:
        return self.entity_group_controller.get_shared_entity_groups_by_type_using_get(group_type=group_type)

    def get_all_entity_view_infos(self, page_size: int,
                                  page: int,
                                  include_customers: Optional[bool] = None,
                                  type: Optional[str] = None,
                                  text_search: Optional[str] = None,
                                  sort_property: Optional[str] = None,
                                  sort_order: Optional[
                                      str] = None) -> PageDataEntityViewInfo:
        return self.entity_view_controller.get_all_entity_view_infos_using_get(page_size=page_size, page=page,
                                                                               text_search=text_search,
                                                                               sort_property=sort_property,
                                                                               sort_order=sort_order,
                                                                               include_customers=include_customers,
                                                                               type=type)

    def get_customer_entity_view_infos(self, customer_id: CustomerId, page_size: int, page: int,
                                       type: Optional[str] = None,
                                       text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                       sort_order: Optional[str] = None, include_customers: Optional[bool] = None):
        customer_id = self.get_id(customer_id)
        return self.entity_view_controller.get_customer_entity_view_infos_using_get(customer_id=customer_id,
                                                                                    page_size=page_size, page=page,
                                                                                    type=type, text_search=text_search,
                                                                                    sort_property=sort_property,
                                                                                    sort_order=sort_order,
                                                                                    include_customers=include_customers)

    def get_all_user_infos(self, page_size: int, page: int,
                           type: Optional[str] = None,
                           text_search: Optional[str] = None, sort_property: Optional[str] = None,
                           sort_order: Optional[str] = None,
                           include_customers: Optional[bool] = None) -> PageDataUserInfo:
        return self.user_controller.get_all_user_infos_using_get(page_size=page_size, page=page,
                                                                 type=type, text_search=text_search,
                                                                 sort_property=sort_property,
                                                                 sort_order=sort_order,
                                                                 include_customers=include_customers)

    def get_customer_user_infos(self, customer_id: CustomerId, page_size: int, page: int,
                                text_search: Optional[str] = None, sort_property: Optional[str] = None,
                                sort_order: Optional[str] = None,
                                include_customers: Optional[bool] = None) -> PageDataUserInfo:
        customer_id = self.get_id(customer_id)
        return self.user_controller.get_customer_user_infos_using_get(customer_id=customer_id,
                                                                      page_size=page_size, page=page,
                                                                      text_search=text_search,
                                                                      sort_property=sort_property,
                                                                      sort_order=sort_order,
                                                                      include_customers=include_customers)

    def get_user_info_by_id(self, user_id: UserId) -> UserInfo:
        user_id = self.get_id(user_id)
        return self.user_controller.get_user_info_by_id_using_get(user_id=user_id)

    def download_login_favicon(self, type: str, key: str, if_none_match: str) -> ByteArrayResource:
        return self.image_controller.download_login_favicon_using_get(type=type, key=key, if_none_match=if_none_match)

    def download_login_logo(self, type: str, key: str, if_none_match: str) -> ByteArrayResource:
        return self.image_controller.download_login_logo_using_get(type=type, key=key, if_none_match=if_none_match)

    def enable_scheduler_event(self, scheduler_event_id: SchedulerEventId, enabled_value: bool) -> SchedulerEvent:
        scheduler_event_id = self.get_id(scheduler_event_id)
        return self.scheduler_event_controller.enable_scheduler_event_using_put(scheduler_event_id=scheduler_event_id,
                                                                                enabled_value=enabled_value)

    def get_merged_mobile_app_settings(self) -> MobileAppSettings:
        return self.mobile_application_controller.get_merged_mobile_app_settings()

    def download_full_translation(self, locale_code: str) -> str:
        return self.translation_controller.download_full_translation(locale_code=locale_code)

    def get_available_java_locales(self) -> JsonNode:
        return self.translation_controller.get_available_java_locales()

    def get_available_locales(self) -> JsonNode:
        return self.translation_controller.get_available_locales()

    def get_full_translation(self, locale_code: str, if_none_match: Optional[str] = None,
                             accept_encoding: Optional[str] = None):
        return self.translation_controller.get_full_translation(locale_code=locale_code, if_none_match=if_none_match,
                                                                accept_encoding=accept_encoding)

    def get_login_page_translation(self, locale_code: str, if_none_match: Optional[str] = None,
                                   accept_encoding: Optional[str] = None):
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

    def get_vendor_models(self, integration_type: str, vendor_name: str, converter_type: str) -> List[Model]:
        return self.converter_library_controller.get_vendor_models(integration_type=integration_type,
                                                                   vendor_name=vendor_name,
                                                                   converter_type=converter_type)

    def get_vendors(self, integration_type: str) -> List[JsonNode]:
        return self.converter_library_controller.get_vendors(integration_type=integration_type)

    def check_tenant_can_update_plan(self, body):
        return self.billing_endpoint_controller.check_tenant_can_update_plan_using_post(body=body)

    def notify_tenant_plan_changed(self, body):
        return self.billing_endpoint_controller.notify_tenant_plan_changed_using_post(body=body)

    def notify_tenant_state_changed(self, body):
        return self.billing_endpoint_controller.notify_tenant_state_changed_using_post(body=body)

    def send_password_was_reset_email(self, body):
        return self.billing_endpoint_controller.send_password_was_reset_email_using_post(body=body)

    def send_reset_password_email(self, body):
        return self.billing_endpoint_controller.send_reset_password_email_using_post(body=body)

    def tenant_has_billing_read(self) -> bool:
        return self.billing_endpoint_controller.tenant_has_billing_read_using_get()

    def tenant_has_billing_write(self) -> bool:
        return self.billing_endpoint_controller.tenant_has_billing_write_using_get()

    def tenant_has_white_label_read(self) -> bool:
        return self.cloud_endpoint_controller.tenant_has_white_label_read_using_get()

    def tenant_has_white_label_write(self) -> bool:
        return self.cloud_endpoint_controller.tenant_has_white_label_write_using_get()

    def tenant_white_labeling_allowed(self):
        return self.cloud_endpoint_controller.tenant_white_labeling_allowed_using_get()

    def __load_controllers(self):
        self.dashboard_controller = DashboardControllerApi(self.api_client)
        self.device_profile_controller = DeviceProfileControllerApi(self.api_client)
        self.http_integration_controller = HttpIntegrationControllerApi(self.api_client)
        self.user_permissions_controller = UserPermissionsControllerApi(self.api_client)
        self.device_group_ota_package_controller = DeviceGroupOtaPackageControllerApi(self.api_client)
        self.converter_controller = ConverterControllerApi(self.api_client)
        self.t_mobile_iot_cdp_integration_controller = TMobileIotCdpIntegrationControllerApi(self.api_client)
        self.customer_controller = CustomerControllerApi(self.api_client)
        self.role_controller = RoleControllerApi(self.api_client)
        self.entity_group_controller = EntityGroupControllerApi(self.api_client)
        self.admin_controller = AdminControllerApi(self.api_client)
        self.edge_controller = EdgeControllerApi(self.api_client)
        self.tenant_controller = TenantControllerApi(self.api_client)
        self.report_controller = ReportControllerApi(self.api_client)
        self.entity_view_controller = EntityViewControllerApi(self.api_client)
        self.rpc_v2_controller = RpcV2ControllerApi(self.api_client)
        self.lwm2m_controller = Lwm2mControllerApi(self.api_client)
        self.scheduler_event_controller = SchedulerEventControllerApi(self.api_client)
        self.custom_menu_controller = CustomMenuControllerApi(self.api_client)
        self.thing_park_integration_controller = ThingParkIntegrationControllerApi(self.api_client)
        self.rule_engine_controller = RuleEngineControllerApi(self.api_client)
        self.integration_controller = IntegrationControllerApi(self.api_client)
        self.custom_translation_controller = CustomTranslationControllerApi(self.api_client)
        self.ota_package_controller = OtaPackageControllerApi(self.api_client)
        self.edge_event_controller = EdgeEventControllerApi(self.api_client)
        self.device_controller = DeviceControllerApi(self.api_client)
        self.group_permission_controller = GroupPermissionControllerApi(self.api_client)
        self.chirp_stack_integration_controller = ChirpStackIntegrationControllerApi(self.api_client)
        self.user_controller = UserControllerApi(self.api_client)
        self.white_labeling_controller = WhiteLabelingControllerApi(self.api_client)
        self.sign_up_controller = SignUpControllerApi(self.api_client)
        self.blob_entity_controller = BlobEntityControllerApi(self.api_client)
        self.owner_controller = OwnerControllerApi(self.api_client)
        self.self_registration_controller = SelfRegistrationControllerApi(self.api_client)
        self.sig_fox_integration_controller = SigFoxIntegrationControllerApi(self.api_client)
        self.asset_controller = AssetControllerApi(self.api_client)
        self.subscription_controller = SubscriptionControllerApi(self.api_client)
        self.solution_controller = SolutionControllerApi(self.api_client)
        self.asset_profile_controller = AssetProfileControllerApi(self.api_client)
        self.image_controller = ImageControllerApi(self.api_client)
        self.mobile_application_controller = MobileApplicationControllerApi(self.api_client)
        self.translation_controller = TranslationControllerApi(self.api_client)
        self.converter_library_controller = ConverterLibraryControllerApi(self.api_client)
        self.billing_endpoint_controller = BillingEndpointControllerApi(self.api_client)
        self.cloud_endpoint_controller = CloudEndpointControllerApi(self.api_client)
