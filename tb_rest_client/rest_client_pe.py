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

from tb_rest_client.api.api_ce import *
from tb_rest_client.api.api_pe import *
from tb_rest_client.models.models_pe import *

logger = getLogger(__name__)


class RestClientPE(RestClientBase):
    def __init__(self, base_url):
        super().__init__(base_url)

    def login(self, username, password):
        super(RestClientPE, self).login(username=username, password=password)
        self.__load_controllers()

    """ Asset endpoints """

    def save_asset(self, asset: Asset, entity_group_id=None):
        return self.asset_controller.save_asset_using_post(asset, entity_group_id=entity_group_id)

    def get_user_assets(self, page_size: int, page: int, type=None, text_search=None, sort_property=None,
                        sort_order=None):
        return self.asset_controller.get_user_assets_using_get(page_size=str(page_size), page=str(page), type=type,
                                                               text_search=text_search, sort_property=sort_property,
                                                               sort_order=sort_order)

    """ Billing endpoints """

    def send_account_activated_email(self, send_account_activated_email_request):
        return self.billing_endpoint_controller.send_account_activated_email_using_post(
            send_account_activated_email_request=send_account_activated_email_request)

    def send_activation_email(self, send_activation_email_request):
        return self.billing_endpoint_controller.send_activation_email_using_post(
            send_activation_email_request=send_activation_email_request)

    def send_password_was_reset_email(self, send_password_was_reset_email_request):
        return self.billing_endpoint_controller.send_password_was_reset_email_using_post(
            send_password_was_reset_email_request=send_password_was_reset_email_request)

    def send_reset_password_email(self, send_reset_password_email_request):
        return self.billing_endpoint_controller.send_reset_password_email_using_post(
            send_reset_password_email_request=send_reset_password_email_request)

    def tenant_has_billing_read(self):
        return self.billing_endpoint_controller.tenant_has_billing_read_using_get()

    def tenant_has_billing_write(self):
        return self.billing_endpoint_controller.tenant_has_billing_write_using_get()

    def check_tenant_can_update_plan(self, can_update_plan_request):
        return self.billing_endpoint_controller.check_tenant_can_update_plan_using_post(
            can_update_plan_request=can_update_plan_request)

    def notify_tenant_plan_changed(self, tenant_plan_changed_request):
        return self.billing_endpoint_controller.notify_tenant_plan_changed_using_post(
            tenant_plan_changed_request=tenant_plan_changed_request)

    def notify_tenant_state_changed(self, tenant_state_changed_request):
        return self.billing_endpoint_controller.notify_tenant_state_changed_using_post(
            tenant_state_changed_request=tenant_state_changed_request)

    """ Customer endpoints """

    def save_customer(self, customer: Customer, entity_group_id=None):
        return self.customer_controller.save_customer_using_post(customer=customer, entity_group_id=entity_group_id)

    def get_customers_by_ids(self, customer_ids):
        return self.customer_controller.getCustomersByIds(customer_ids=customer_ids)

    def get_customers_by_entity_group_id(self, entity_group_id, page_size: int, page: int, text_search=None,
                                         sort_property=None, sort_order=None):
        return self.customer_controller.get_customers_by_entity_group_id_using_get(entity_group_id=entity_group_id,
                                                                                   page_size=str(page_size),
                                                                                   page=str(page),
                                                                                   text_search=text_search,
                                                                                   sort_property=sort_property,
                                                                                   sort_order=sort_order)

    def get_user_customers(self, page_size: int, page: int, text_search=None, sort_property=None, sort_order=None):
        return self.customer_controller.get_user_customers_using_get(page_size=str(page_size), page=str(page),
                                                                     text_search=text_search,
                                                                     sort_property=sort_property, sort_order=sort_order)

    """ Chirp stack integration endpoints """

    def delete_chirp_stack_process_request(self, routing_key, msg, request_headers):
        return self.chirp_stack_integration_controller.process_request_using_delete(routing_key=routing_key, msg=msg,
                                                                                    request_headers=request_headers)

    def get_chirp_stack_process_request(self, routing_key, msg, request_headers):
        return self.chirp_stack_integration_controller.process_request_using_get(routing_key=routing_key, msg=msg,
                                                                                 request_headers=request_headers)

    def head_chirp_stack_process_request(self, routing_key, msg, request_headers):
        return self.chirp_stack_integration_controller.process_request_using_head(routing_key=routing_key, msg=msg,
                                                                                  request_headers=request_headers)

    def options_chirp_stack_process_request(self, routing_key, msg, request_headers):
        return self.chirp_stack_integration_controller.process_request_using_options(routing_key=routing_key, msg=msg,
                                                                                     request_headers=request_headers)

    def patch_chirp_stack_process_request(self, routing_key, msg, request_headers):
        return self.chirp_stack_integration_controller.process_request_using_patch(routing_key=routing_key, msg=msg,
                                                                                   request_headers=request_headers)

    def post_chirp_stack_process_request(self, routing_key, msg, request_headers):
        return self.chirp_stack_integration_controller.process_request_using_post(routing_key=routing_key, msg=msg,
                                                                                  request_headers=request_headers)

    def put_chirp_stack_process_request(self, routing_key, msg, request_headers):
        return self.chirp_stack_integration_controller.process_request_using_put(routing_key=routing_key, msg=msg,
                                                                                 request_headers=request_headers)

    """ Cloud endpoints """

    def tenant_has_white_label_read(self):
        return self.cloud_endpoint_controller.tenant_has_white_label_read_using_get()

    def tenant_has_white_label_write(self):
        return self.cloud_endpoint_controller.tenant_has_white_label_write_using_get()

    def tenant_white_labeling_allowed(self):
        return self.cloud_endpoint_controller.tenant_white_labeling_allowed_using_get()

    """ Dashboard endpoints """

    def get_user_dashboards(self, user_id: UserId, operation, page_size=10, page=0, text_search=None,
                            sort_property=None, sort_order=None, limit=100000):
        user_id = self.get_id(user_id)
        return self.dashboard_controller.get_user_dashboards_using_get(page_size=str(page_size),
                                                                       page=str(page),
                                                                       text_search=text_search,
                                                                       sort_property=sort_property,
                                                                       sort_order=sort_order, limit=str(limit),
                                                                       operation=operation,
                                                                       user_id=user_id)

    def get_group_dashboards(self, entity_group_id: EntityGroupId, page_size=10, page=0, text_search=None,
                             sort_property=None, sort_order=None, limit=100000):
        entity_group_id = self.get_id(entity_group_id)
        return self.dashboard_controller.get_group_dashboards_using_get(entity_group_id=entity_group_id,
                                                                        page_size=str(page_size),
                                                                        page=str(page),
                                                                        text_search=text_search,
                                                                        sort_property=sort_property,
                                                                        sort_order=sort_order, limit=str(limit))

    def get_dasboards_by_ids(self, dashboards_ids):
        if isinstance(dashboards_ids, list):
            dashboards_ids = ",".join(dashboards_ids)
        return self.dashboard_controller.get_dashboards_by_ids_using_get(dashboard_ids=dashboards_ids)

    def save_dashboard(self, dashboard: Dashboard, entity_group_id=None):
        return self.dashboard_controller.save_dashboard_using_post(dashboard=dashboard, entity_group_id=entity_group_id)

    """ Tenant endpoints """

    def get_tenants_by_ids(self, tenant_ids):
        return self.tenant_controller.get_tenants_by_ids_using_get(tenant_ids=tenant_ids)

    """ Blob Entity endpoints"""

    def get_blob_entity_info_by_id(self, blob_entity_id: BlobEntityId):
        blob_entity_id = self.get_id(blob_entity_id)
        return self.blob_entity_controller.get_blob_entity_info_by_id_using_get(blob_entity_id=blob_entity_id)

    def download_blob_entity(self, blob_entity_id: BlobEntityId):
        blob_entity_id = self.get_id(blob_entity_id)
        return self.blob_entity_controller.download_blob_entity_using_get(blob_entity_id=blob_entity_id)

    def delete_blob_entity(self, blob_entity_id: BlobEntityId):
        blob_entity_id = self.get_id(blob_entity_id)
        self.blob_entity_controller.delete_blob_entity_using_delete(blob_entity_id=blob_entity_id)

    def get_blob_entities(self, type, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None,
                          start_time=None, end_time=None):
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

    def test_up_link_converter(self, input_params):
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
        return self.custom_translation_controller.save_custom_translation_using_post(
            custom_translation=custom_translation)

    """ Entity group endpoints """

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
        return self.entity_group_controller.get_entity_groups_by_type_using_get(group_type=group_type)

    def get_entity_groups_by_owner_and_type(self, owner_id, group_type):
        group_type = self.get_type(group_type)
        return self.entity_group_controller.get_entity_groups_by_owner_and_type_using_get(
            owner_type=owner_id.entity_type,
            owner_id=owner_id.id,
            group_type=group_type)

    def get_entity_group_all_by_owner_and_type(self, owner_id, group_type):
        group_type = self.get_type(group_type)
        return self.entity_group_controller.get_entity_group_all_by_owner_and_type_using_get(
            owner_type=owner_id.entity_type,
            owner_id=owner_id.id,
            group_type=group_type)

    def get_entity_group_info_by_owner_and_name_and_type(self, owner_id, group_type, group_name):
        group_type = self.get_type(group_type)
        return self.entity_group_controller.get_enitity_group_by_owner_and_name_and_type_using_get(
            owner_type=owner_id.entity_type,
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

    def get_entities(self, entity_group_id: EntityGroupId, page_size=10, page=0, text_search=None, sort_property=None,
                     sort_order=None):
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

    def get_entity_group_by_owner_and_name_and_type(self, owner_id, group_type: str, group_name: str):
        return self.entity_group_controller.get_entity_group_by_owner_and_name_and_type_using_get(
            owner_type=owner_id.entity_type, owner_id=owner_id.id, group_type=group_type, group_name=group_name)

    """ Group permissions endpoints"""

    def get_group_permission_by_id(self, group_permission_id: GroupPermissionId):
        group_permission_id = self.get_id(group_permission_id)
        return self.group_permission_controller.get_group_permission_by_id_using_get(
            group_permission_id=group_permission_id)

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

    def get_group_permission_info_by_id(self, group_permission_id: GroupPermissionId, is_user_group: bool):
        group_permission_id = self.get_id(group_permission_id)
        return self.group_permission_controller.get_group_permission_info_by_id_using_get(
            group_permission_id=group_permission_id, is_user_group=str(is_user_group).lower())

    """ Integration endpoints. """

    def get_integration_by_id(self, integration_id: IntegrationId):
        integration_id = self.get_id(integration_id)
        return self.integration_controller.get_integration_by_id_using_get(integration_id=integration_id)

    def get_integration_by_routing_key(self, routing_key):
        return self.integration_controller.get_integration_by_routing_key_using_get(routing_key=routing_key)

    def save_integration(self, integration: Integration):
        return self.integration_controller.save_integration_using_post(integration=integration)

    def check_integration_connection(self, integration: Integration):
        return self.integration_controller.check_integration_connection_using_post(integration=integration)

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

    """ Device endpoints """

    def get_user_devices(self, device_type, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None,
                         limit=100000):
        return self.device_controller.get_user_devices_using_get(type=device_type,
                                                                 page_size=str(page_size),
                                                                 page=str(page),
                                                                 text_search=text_search,
                                                                 sort_property=sort_property,
                                                                 sort_order=sort_order, limit=str(limit))

    """ Entity view endpoints """

    def get_user_entity_views(self, entity_view_type, page_size=10, page=0, text_search=None, sort_property=None,
                              sort_order=None, limit=100000):
        entity_view_type = self.get_type(entity_view_type)
        return self.entity_view_controller.get_user_entity_views_using_get(type=entity_view_type,
                                                                           page_size=str(page_size),
                                                                           page=str(page),
                                                                           text_search=text_search,
                                                                           sort_property=sort_property,
                                                                           sort_order=sort_order, limit=str(limit))

    def get_entity_views_by_ids(self, entity_view_ids):
        return self.entity_view_controller.get_entity_views_by_ids_using_get(entity_view_ids=entity_view_ids)

    def save_entity_view(self, entity_view: EntityView, entity_group_id):
        return self.entity_view_controller.save_entity_view_using_post(entity_view=entity_view,
                                                                       entity_group_id=entity_group_id)

    """ Owner endpoints"""

    def change_owner_to_tenant(self, owner_id, entity_id):
        owner_id = self.get_id(owner_id)
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        self.owner_controller.change_owner_to_tenant_using_post(owner_id=owner_id, entity_id=entity_id,
                                                                entity_type=entity_type)

    def change_owner_to_customer(self, owner_id, entity_id):
        owner_id = self.get_id(owner_id)
        entity_type = self.get_type(entity_id)
        entity_id = self.get_id(entity_id)
        self.owner_controller.change_owner_to_customer_using_post(owner_id=owner_id, entity_id=entity_id,
                                                                  entity_type=entity_type)

    """ Reports endpoints """

    def download_dashboard_report(self, dashboard_id: DashboardId, report_params):
        dashboard_id = self.get_id(dashboard_id)
        return self.report_controller.download_dashboard_report_using_post(dashboard_id=dashboard_id,
                                                                           report_params=report_params)

    def download_test_report(self, report_config, reports_server_endpoint_url):
        return self.report_controller.download_test_report_using_post(report_config=report_config,
                                                                      reports_server_endpoint_url=reports_server_endpoint_url)

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

    """ User endpoints """

    def get_all_customer_users(self, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None,
                               limit=100000):
        return self.user_controller.get_all_customer_users_using_get(page_size=str(page_size),
                                                                     page=str(page),
                                                                     text_search=text_search,
                                                                     sort_property=sort_property,
                                                                     sort_order=sort_order, limit=str(limit))

    def get_user_users(self, page_size=10, page=0, text_search=None, sort_property=None, sort_order=None, limit=100000):
        return self.user_controller.get_user_users_using_get(page_size=page_size,
                                                             page=page,
                                                             text_search=text_search,
                                                             sort_property=sort_property,
                                                             sort_order=sort_order, limit=str(limit))

    def get_users_by_ids(self, user_ids):
        return self.user_controller.get_users_by_ids_using_get(user_ids=user_ids)

    def get_allowed_permissions(self):
        return self.user_permissions_controller.get_allowed_permissions_using_get()

    def save_user(self, user: User, send_activation_mail, entity_group_id=None):
        return self.user_controller.save_user_using_post(user=user, send_activation_mail=send_activation_mail,
                                                         entity_group_id=entity_group_id)

    """ Rule engine endpoints"""

    def handle_rule_engine_request(self, request_body, entity_id=None, timeout=None):
        if entity_id is None and timeout is None:
            return self.rule_engine_controller.handle_rule_engine_request_using_post(request_body=request_body)
        elif timeout is None:
            entity_type = self.get_type(entity_id)
            entity_id = self.get_type(entity_id)
            return self.rule_engine_controller.handle_rule_engine_request_using_post2(entity_id=entity_id,
                                                                                      entity_type=entity_type,
                                                                                      request_body=request_body)
        else:
            entity_type = self.get_type(entity_id)
            entity_id = self.get_type(entity_id)
            return self.rule_engine_controller.handle_rule_engine_request_using_post1(entity_id=entity_id,
                                                                                      entity_type=entity_type,
                                                                                      request_body=request_body,
                                                                                      timeout=timeout)

    """ Scheduler endpoints """

    def get_scheduler_event_info_by_id(self, scheduler_event_id: SchedulerEventId):
        scheduler_event_id = self.get_id(scheduler_event_id)
        return self.scheduler_event_controller.get_scheduler_event_info_by_id_using_get(
            scheduler_event_id=scheduler_event_id)

    def get_scheduler_event_by_id(self, scheduler_event_id: SchedulerEventId):
        scheduler_event_id = self.get_id(scheduler_event_id)
        return self.scheduler_event_controller.get_scheduler_event_by_id_using_get(
            scheduler_event_id=scheduler_event_id)

    def save_scheduler_event(self, scheduler_event: SchedulerEvent):
        return self.scheduler_event_controller.save_scheduler_event_using_post(scheduler_event=scheduler_event)

    def delete_scheduler_event(self, scheduler_event_id: SchedulerEventId):
        scheduler_event_id = self.get_id(scheduler_event_id)
        self.scheduler_event_controller.delete_scheduler_event_using_delete(scheduler_event_id=scheduler_event_id)

    def get_scheduler_events(self, type):
        return self.scheduler_event_controller.get_scheduler_events_using_get(type=type)

    def get_scheduler_events_by_ids(self, scheduler_event_ids):
        return self.scheduler_event_controller.get_scheduler_events_by_ids_using_get(
            scheduler_event_ids=scheduler_event_ids)

    """ Self registration endpoints. """

    def save_self_registration_params(self, self_registration_params: SelfRegistrationParams):
        return self.self_registration_controller.save_self_registration_params_using_post(
            self_registration_params=self_registration_params)

    def get_self_registration_params(self):
        return self.self_registration_controller.get_self_registration_params_using_get()

    def get_sign_up_self_registration_params(self):
        return self.self_registration_controller.get_sign_up_self_registration_params_using_get()

    def get_privacy_policy(self):
        return self.self_registration_controller.get_privacy_policy_using_get()

    def get_terms_of_use(self):
        return self.self_registration_controller.get_terms_of_use_using_get()

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

    def accept_privacy_policy(self):
        return self.sign_up_controller.accept_privacy_policy_using_post()

    """ HTTP integration endpoints """

    def process_http_request(self, routing_key, suffix, request_params, request_headers):
        return self.http_integration_controller.process_request_using_post3(routing_key=routing_key, suffix=suffix,
                                                                            request_params=request_params,
                                                                            request_headers=request_headers)

    def check_http_status(self, routing_key, request_params, request_headers):
        return self.http_integration_controller.check_status_using_get(routing_key=routing_key,
                                                                       request_params=request_params,
                                                                       request_headers=request_headers)

    """ Loriot integration endpoints """

    def delete_loriot_process_request(self, routing_key, msg, request_headers):
        return self.loriot_integration_controller.process_request_using_delete1(routing_key=routing_key, msg=msg,
                                                                                request_headers=request_headers)

    def get_loriot_process_request(self, routing_key, msg, request_headers):
        return self.loriot_integration_controller.process_request_using_get1(routing_key=routing_key, msg=msg,
                                                                             request_headers=request_headers)

    def head_loriot_process_request(self, routing_key, msg, request_headers):
        return self.loriot_integration_controller.process_request_using_head1(routing_key=routing_key, msg=msg,
                                                                              request_headers=request_headers)

    def options_loriot_process_request(self, routing_key, msg, request_headers):
        return self.loriot_integration_controller.process_request_using_options1(routing_key=routing_key, msg=msg,
                                                                                 request_headers=request_headers)

    def patch_loriot_process_request(self, routing_key, msg, request_headers):
        return self.loriot_integration_controller.process_request_using_patch1(routing_key=routing_key, msg=msg,
                                                                               request_headers=request_headers)

    def post_loriot_process_request(self, routing_key, msg, request_headers):
        return self.loriot_integration_controller.process_request_using_post7(routing_key=routing_key, msg=msg,
                                                                              request_headers=request_headers)

    def put_loriot_process_request(self, routing_key, msg, request_headers):
        return self.loriot_integration_controller.process_request_using_put1(routing_key=routing_key, msg=msg,
                                                                             request_headers=request_headers)

    """ Ocean connect endpoints """

    def post_ocean_connect_process_request(self, routing_key, msg, request_headers):
        return self.ocean_connect_integration_controller.process_request_using_post4(routing_key=routing_key, msg=msg,
                                                                                     request_headers=request_headers)

    def delete_ocean_connect_process_request(self, routing_key, msg, request_headers):
        return self.ocean_connect_integration_controller.process_request_using_delete(routing_key=routing_key, msg=msg,
                                                                                      request_headers=request_headers)

    def get_ocean_connect_process_request(self, routing_key, msg, request_headers):
        return self.ocean_connect_integration_controller.process_request_using_get(routing_key=routing_key, msg=msg,
                                                                                   request_headers=request_headers)

    def head_ocean_connect_process_request(self, routing_key, msg, request_headers):
        return self.ocean_connect_integration_controller.process_request_using_head(routing_key=routing_key, msg=msg,
                                                                                    request_headers=request_headers)

    def options_ocean_connect_process_request(self, routing_key, msg, request_headers):
        return self.ocean_connect_integration_controller.process_request_using_options(routing_key=routing_key, msg=msg,
                                                                                       request_headers=request_headers)

    def patch_ocean_connect_process_request(self, routing_key, msg, request_headers):
        return self.ocean_connect_integration_controller.process_request_using_patch(routing_key=routing_key, msg=msg,
                                                                                     request_headers=request_headers)

    def put_ocean_connect_process_request(self, routing_key, msg, request_headers):
        return self.ocean_connect_integration_controller.process_request_using_put(routing_key=routing_key, msg=msg,
                                                                                   request_headers=request_headers)

    """ Sig fox integration endpoints """

    def delete_sig_fox_process_request(self, routing_key, msg, request_headers):
        return self.sigfox_integration_controller.process_request_using_delete1(routing_key=routing_key, msg=msg,
                                                                                request_headers=request_headers)

    def get_sig_fox_process_request(self, routing_key, msg, request_headers):
        return self.sigfox_integration_controller.process_request_using_get1(routing_key=routing_key, msg=msg,
                                                                             request_headers=request_headers)

    def head_sig_fox_process_request(self, routing_key, msg, request_headers):
        return self.sigfox_integration_controller.process_request_using_head1(routing_key=routing_key, msg=msg,
                                                                              request_headers=request_headers)

    def options_sig_fox_process_request(self, routing_key, msg, request_headers):
        return self.sigfox_integration_controller.process_request_using_options1(routing_key=routing_key, msg=msg,
                                                                                 request_headers=request_headers)

    def patch_sig_fox_process_request(self, routing_key, msg, request_headers):
        return self.sigfox_integration_controller.process_request_using_patch1(routing_key=routing_key, msg=msg,
                                                                               request_headers=request_headers)

    def post_sig_fox_process_request(self, routing_key, msg, request_headers):
        return self.sigfox_integration_controller.process_request_using_post5(routing_key=routing_key, msg=msg,
                                                                              request_headers=request_headers)

    def put_sig_fox_process_request(self, routing_key, msg, request_headers):
        return self.sigfox_integration_controller.process_request_using_put1(routing_key=routing_key, msg=msg,
                                                                             request_headers=request_headers)

    """ T mobile iot cdp integration endpoints """

    def delete_t_mobile_iot_cdp_process_request(self, routing_key, msg, request_headers):
        return self.tmobile_iot_cdp_integration_controller.process_request_using_delete2(routing_key=routing_key,
                                                                                         msg=msg,
                                                                                         request_headers=request_headers)

    def get_t_mobile_iot_cdp_process_request(self, routing_key, msg, request_headers):
        return self.tmobile_iot_cdp_integration_controller.process_request_using_get2(routing_key=routing_key,
                                                                                      msg=msg,
                                                                                      request_headers=request_headers)

    def head_t_mobile_iot_cdp_process_request(self, routing_key, msg, request_headers):
        return self.tmobile_iot_cdp_integration_controller.process_request_using_head2(routing_key=routing_key,
                                                                                       msg=msg,
                                                                                       request_headers=request_headers)

    def options_t_mobile_iot_cdp_process_request(self, routing_key, msg, request_headers):
        return self.tmobile_iot_cdp_integration_controller.process_request_using_options2(routing_key=routing_key,
                                                                                          msg=msg,
                                                                                          request_headers=request_headers)

    def patch_t_mobile_iot_cdp_process_request(self, routing_key, msg, request_headers):
        return self.tmobile_iot_cdp_integration_controller.process_request_using_patch2(routing_key=routing_key,
                                                                                        msg=msg,
                                                                                        request_headers=request_headers)

    def post_t_mobile_iot_cdp_process_request(self, routing_key, msg, request_headers):
        return self.tmobile_iot_cdp_integration_controller.process_request_using_post6(routing_key=routing_key,
                                                                                       msg=msg,
                                                                                       request_headers=request_headers)

    def put_t_mobile_iot_cdp_process_request(self, routing_key, msg, request_headers):
        return self.tmobile_iot_cdp_integration_controller.process_request_using_put2(routing_key=routing_key,
                                                                                      msg=msg,
                                                                                      request_headers=request_headers)

    """ Solution endpoints """

    def get_solution_template_details(self, solution_template_id: str):
        return self.solution_controller.get_solution_template_details_using_get(
            solution_template_id=solution_template_id)

    def get_solution_template_infos(self):
        return self.solution_controller.get_solution_template_infos_using_get()

    def get_solution_template_instructions(self, solution_template_id: str):
        return self.solution_controller.get_solution_template_instructions_using_get(
            solution_template_id=solution_template_id)

    def delete_solution_template(self, solution_template_id):
        return self.solution_controller.delete_solution_template_using_delete(solution_template_id=solution_template_id)

    def install_solution_template(self, solution_template_id):
        return self.solution_controller.install_solution_template_using_post(solution_template_id=solution_template_id)

    """ Subscription endpoints """

    def get_tenant_profile_data(self):
        return self.subscription_controller.get_tenant_profile_data_using_get()

    def get_tenant_subscription_usage(self):
        return self.solution_controller.get_tenant_subscription_usage_using_get()

    def get_tenant_profile_data_by_id(self, tenant_profile_id: TenantProfileId):
        tenant_profile_id = self.get_id(tenant_profile_id)
        return self.subscription_controller.get_tenant_profile_data_by_id_using_get(tenant_profile_id=tenant_profile_id)

    """ Thing park integration endpoints """

    def delete_thing_park_process_request(self, routing_key, all_request_params, msg, request_headers):
        return self.thingpark_integration_controller.process_request_using_delete3(routing_key=routing_key,
                                                                                   all_request_params=all_request_params,
                                                                                   msg=msg,
                                                                                   request_headers=request_headers)

    def get_thing_park_process_request(self, routing_key, all_request_params, msg, request_headers):
        return self.thingpark_integration_controller.process_request_using_get3(routing_key=routing_key,
                                                                                all_request_params=all_request_params,
                                                                                msg=msg,
                                                                                request_headers=request_headers)

    def head_thing_park_process_request(self, routing_key, all_request_params, msg, request_headers):
        return self.thingpark_integration_controller.process_request_using_head3(routing_key=routing_key,
                                                                                 all_request_params=all_request_params,
                                                                                 msg=msg,
                                                                                 request_headers=request_headers)

    def options_thing_park_process_request(self, routing_key, all_request_params, msg, request_headers):
        return self.thingpark_integration_controller.process_request_using_options3(routing_key=routing_key,
                                                                                    all_request_params=all_request_params,
                                                                                    msg=msg,
                                                                                    request_headers=request_headers)

    def patch_thing_park_process_request(self, routing_key, all_request_params, msg, request_headers):
        return self.thingpark_integration_controller.process_request_using_patch3(routing_key=routing_key,
                                                                                  all_request_params=all_request_params,
                                                                                  msg=msg,
                                                                                  request_headers=request_headers)

    def post_thing_park_process_request(self, routing_key, all_request_params, msg, request_headers):
        return self.thingpark_integration_controller.process_request_using_post7(routing_key=routing_key,
                                                                                 all_request_params=all_request_params,
                                                                                 msg=msg,
                                                                                 request_headers=request_headers)

    def put_thing_park_process_request(self, routing_key, all_request_params, msg, request_headers):
        return self.thingpark_integration_controller.process_request_using_put3(routing_key=routing_key,
                                                                                all_request_params=all_request_params,
                                                                                msg=msg,
                                                                                request_headers=request_headers)

    def delete_thing_park_process_request_tpe(self, routing_key, all_request_params, msg, request_headers):
        return self.thingpark_integration_controller.process_request_tpe_using_delete(routing_key=routing_key,
                                                                                      all_request_params=all_request_params,
                                                                                      msg=msg,
                                                                                      request_headers=request_headers)

    def get_thing_park_process_request_tpe(self, routing_key, all_request_params, msg, request_headers):
        return self.thingpark_integration_controller.process_request_tpe_using_get(routing_key=routing_key,
                                                                                   all_request_params=all_request_params,
                                                                                   msg=msg,
                                                                                   request_headers=request_headers)

    def head_thing_park_process_request_tpe(self, routing_key, all_request_params, msg, request_headers):
        return self.thingpark_integration_controller.process_request_tpe_using_head(routing_key=routing_key,
                                                                                    all_request_params=all_request_params,
                                                                                    msg=msg,
                                                                                    request_headers=request_headers)

    def options_thing_park_process_request_tpe(self, routing_key, all_request_params, msg, request_headers):
        return self.thingpark_integration_controller.process_request_tpe_using_options(routing_key=routing_key,
                                                                                       all_request_params=all_request_params,
                                                                                       msg=msg,
                                                                                       request_headers=request_headers)

    def patch_thing_park_process_request_tpe(self, routing_key, all_request_params, msg, request_headers):
        return self.thingpark_integration_controller.process_request_tpe_using_patch(routing_key=routing_key,
                                                                                     all_request_params=all_request_params,
                                                                                     msg=msg,
                                                                                     request_headers=request_headers)

    def post_thing_park_process_request_tpe(self, routing_key, all_request_params, msg, request_headers):
        return self.thingpark_integration_controller.process_request_tpe_using_post(routing_key=routing_key,
                                                                                    all_request_params=all_request_params,
                                                                                    msg=msg,
                                                                                    request_headers=request_headers)

    def put_thing_park_process_request_tpe(self, routing_key, all_request_params, msg, request_headers):
        return self.thingpark_integration_controller.process_request_tpe_using_put(routing_key=routing_key,
                                                                                   all_request_params=all_request_params,
                                                                                   msg=msg,
                                                                                   request_headers=request_headers)

    """ White label endpoints. """

    def get_white_label_params(self, logo_image_checksum, favicon_checksum):
        return self.white_labeling_controller.get_white_label_params_using_get(logo_image_checksum=logo_image_checksum,
                                                                               favicon_checksum=favicon_checksum)

    def get_login_white_label_params(self, logo_image_checksum, favicon_checksum):
        return self.white_labeling_controller.get_login_white_label_params_using_get(
            logo_image_checksum=logo_image_checksum, favicon_checksum=favicon_checksum)

    def get_current_white_label_params(self):
        return self.white_labeling_controller.get_current_white_label_params_using_get()

    def get_current_login_white_label_params(self):
        return self.white_labeling_controller.get_current_login_white_label_params_using_get()

    def save_white_label_params(self, white_labeling_params: WhiteLabelingParams):
        return self.white_labeling_controller.save_white_label_params_using_post(
            white_labeling_params=white_labeling_params)

    def save_login_white_label_params(self, login_white_labeling_params: LoginWhiteLabelingParams):
        return self.white_labeling_controller.save_login_white_label_params_using_post(
            login_white_labeling_params=login_white_labeling_params)

    def preview_white_label_params(self, white_labeling_params: WhiteLabelingParams):
        return self.white_labeling_controller.preview_white_label_params_using_post(
            white_labeling_params=white_labeling_params)

    def is_white_labeling_allowed(self):
        return self.white_labeling_controller.is_white_labeling_allowed_using_get()

    def is_customer_white_labeling_allowed(self):
        return self.white_labeling_controller.is_customer_white_labeling_allowed_using_get()

    def get_login_theme_css(self, palette_settings: PaletteSettings, dark_foreground=None):
        return self.white_labeling_controller.get_login_theme_css_using_post(palette_settings=palette_settings,
                                                                             dark_foreground=dark_foreground)

    def get_app_theme_css(self, palette_settings: PaletteSettings):
        return self.white_labeling_controller.get_app_theme_css_using_post(palette_settings=palette_settings)

    def __load_controllers(self):
        self.auth_controller = AuthControllerApi(self.api_client)
        self.admin_controller = AdminControllerApi(self.api_client)
        self.alarm_controller = AlarmControllerApi(self.api_client)
        self.asset_controller = AssetControllerApi(self.api_client)
        self.audit_log_controller = AuditLogControllerApi(self.api_client)
        self.component_descriptor_controller = ComponentDescriptorControllerApi(self.api_client)
        self.customer_controller = CustomerControllerApi(self.api_client)
        self.chirp_stack_integration_controller = ChirpStackIntegrationControllerApi(self.api_client)
        self.cloud_endpoint_controller = CloudEndpointControllerApi(self.api_client)
        self.dashboard_controller = DashboardControllerApi(self.api_client)
        self.device_controller = DeviceControllerApi(self.api_client)
        self.device_profile_controller = DeviceProfileControllerApi(self.api_client)
        self.edge_controller = EdgeControllerApi(self.api_client)
        self.edge_event_controller = EdgeEventControllerApi(self.api_client)
        self.entity_relation_controller = EntityRelationControllerApi(self.api_client)
        self.entity_view_controller = EntityViewControllerApi(self.api_client)
        self.entity_query_controller = EntityQueryControllerApi(self.api_client)
        self.event_controller = EventControllerApi(self.api_client)
        self.queue_controller = QueueControllerApi(self.api_client)
        self.rpc_controller = RpcControllerApi(self.api_client)
        self.lwm_2m_controller = Lwm2mControllerApi(self.api_client)
        self.loriot_integration_controller = LoriotIntegrationControllerApi(self.api_client)
        self.ota_package_controller = OtaPackageControllerApi(self.api_client)
        self.tb_resource_controller = TbResourceControllerApi(self.api_client)
        self.rule_chain_controller = RuleChainControllerApi(self.api_client)
        self.telemetry_controller = TelemetryControllerApi(self.api_client)
        self.tenant_controller = TenantControllerApi(self.api_client)
        self.tenant_profile_controller = TenantProfileControllerApi(self.api_client)
        self.user_controller = UserControllerApi(self.api_client)
        self.solution_controller = SolutionControllerApi(self.api_client)
        self.subscription_controller = SubscriptionControllerApi(self.api_client)
        self.billing_endpoint_controller = BillingEndpointControllerApi(self.api_client)
        self.widget_type_controller = WidgetTypeControllerApi(self.api_client)
        self.widgets_bundle_controller = WidgetsBundleControllerApi(self.api_client)

    @staticmethod
    def get_type(type):
        return type.entity_type if hasattr(type, "entity_type") else type

    @staticmethod
    def get_id(id):
        return id.id if hasattr(id, "id") else id
