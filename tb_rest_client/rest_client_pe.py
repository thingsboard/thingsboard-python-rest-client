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

    """ Tenant endpoints """

    def get_tenants_by_ids(self, tenant_ids):
        return self.tenant_controller.get_tenants_by_ids_using_get(tenant_ids=tenant_ids)

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
        return self.custom_translation_controller.save_custom_translation_using_post(
            custom_translation=custom_translation)

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

    """ Owner enpoints"""

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
