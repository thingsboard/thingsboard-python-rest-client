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
#

from tb_rest_client32.api.api_ce import *
from tb_rest_client32.api.api_pe import *
from tb_rest_client32.models.models_ce import *
from tb_rest_client32.models.models_pe import *
from tb_rest_client32.rest_client_base import *

logger = getLogger(__name__)


class RestClientPE(RestClientBase):
    def __init__(self, base_url):
        super().__init__(base_url)

    def login(self, username, password):
        super(RestClientPE, self).login(username=username, password=password)
        self.__load_controllers()

    def get_assets_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size=100, page=0, **kwargs):
        return self.asset_controller.get_assets_by_entity_group_id_using_get(entity_group_id.id, str(page_size), str(page), **kwargs)

    def get_user_assets(self, page_size=100, page=0, **kwargs):
        return self.asset_controller.get_user_assets_using_get(str(page_size), str(page), **kwargs)

    def get_all_customer_users(self, page_size=100, page=0, **kwargs):
        return self.user_controller.get_all_customer_users_using_get(str(page_size), str(page), **kwargs)

    def get_user_users(self, page_size=100, page=0, **kwargs):
        return self.user_controller.get_user_users_using_get(str(page_size), str(page), **kwargs)

    def get_users_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size=100, page=0, **kwargs):
        return self.user_controller.get_users_by_entity_group_id_using_get(entity_group_id.id, str(page_size), str(page), **kwargs)

    def get_users_by_ids(self, user_ids, **kwargs):
        return self.user_controller.get_users_by_ids_using_get(user_ids, **kwargs)

    def get_devices_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size=100, page=0, **kwargs):
        return self.device_controller.get_devices_by_entity_group_id_using_get(entity_group_id.id, str(page_size), str(page), **kwargs)

    def get_user_devices(self, page_size=100, page=0, **kwargs):
        return self.device_controller.get_user_devices_using_get(str(page_size), str(page), **kwargs)

    """ EntityGroupController endpoints """

    def add_entities_to_entity_group(self, entity_group_id: EntityGroupId, str_entity_ids, **kwargs):
        return self.entity_group_controller.add_entities_to_entity_group_using_post(entity_group_id.id, str_entity_ids, **kwargs)

    def delete_entity_group(self, entity_group_id: EntityGroupId, **kwargs):
        return self.entity_group_controller.delete_entity_group_using_delete(entity_group_id.id, **kwargs)

    def get_entities(self, entity_group_id: EntityGroupId, page_size=100, page=0, **kwargs):
        return self.entity_group_controller.get_entities_using_get(entity_group_id.id, str(page_size), str(page), **kwargs)

    def get_entity_group_all_by_owner_and_type(self, owner_id: EntityId, group_type, **kwargs):
        return self.entity_group_controller.get_entity_group_all_by_owner_and_type_using_get(owner_id.entity_type, owner_id.id, group_type, **kwargs)

    def get_entity_group_by_id(self, entity_group_id: EntityGroupId, **kwargs):
        return self.entity_group_controller.get_entity_group_by_id_using_get(entity_group_id.id, **kwargs)

    def get_entity_group_by_owner_and_name_and_type(self, owner_id: EntityId, group_type, group_name, **kwargs):
        return self.entity_group_controller.get_entity_group_by_owner_and_name_and_type_using_get(owner_id.entity_type, owner_id.id, group_type, group_name, **kwargs)

    def get_entity_groups_by_ids(self, entity_group_ids, **kwargs):
        return self.entity_group_controller.get_entity_groups_by_ids_using_get(entity_group_ids, **kwargs)

    def get_entity_groups_by_owner_and_type(self, owner_id: EntityId, group_type, **kwargs):
        return self.entity_group_controller.get_entity_groups_by_owner_and_type_using_get(owner_id.entity_type, owner_id.id, group_type, **kwargs)

    def get_entity_groups_by_type(self, group_type, **kwargs):
        return self.entity_group_controller.get_entity_groups_by_type_using_get(group_type, **kwargs)

    def get_entity_groups_for_entity(self, entity_id: EntityId, **kwargs):
        return self.entity_group_controller.get_entity_groups_for_entity_using_get(entity_id.entity_type, entity_id.id, **kwargs)

    def get_group_entity(self, entity_group_id: EntityGroupId, entity_id: EntityId, **kwargs):
        return self.entity_group_controller.get_group_entity_using_get(entity_group_id.id, entity_id.id, **kwargs)

    def get_owners(self, page_size=100, page=0, **kwargs):
        return self.entity_group_controller.get_owners_using_get(str(page_size), str(page), **kwargs)

    def make_entity_group_private(self, entity_group_id: EntityGroupId, **kwargs):
        return self.entity_group_controller.make_entity_group_private_using_post(entity_group_id.id, **kwargs)

    def make_entity_group_public(self, entity_group_id: EntityGroupId, **kwargs):
        return self.entity_group_controller.make_entity_group_public_using_post(entity_group_id.id, **kwargs)

    def remove_entities_from_entity_group(self, entity_group_id: EntityGroupId, str_entity_ids, **kwargs):
        return self.entity_group_controller.remove_entities_from_entity_group_using_post(entity_group_id.id, str_entity_ids, **kwargs)

    def save_entity_group(self, entity_group, **kwargs):
        return self.entity_group_controller.save_entity_group_using_post(entity_group, **kwargs)

    def share_entity_group_to_child_owner_user_group(self, entity_group_id: EntityGroupId, user_group_id, role_id: RoleId, **kwargs):
        return self.entity_group_controller.share_entity_group_to_child_owner_user_group_using_post(entity_group_id.id, user_group_id.id, role_id.id, **kwargs)

    def share_entity_group(self, entity_group_id: EntityGroupId, share_group_request, **kwargs):
        return self.entity_group_controller.share_entity_group_using_post(entity_group_id.id, share_group_request, **kwargs)

    ##################################

    """ HttpIntegrationController endpoints """

    def check_status(self, routing_key, request_params, request_headers, **kwargs):
        return self.http_integration_controller.check_status_using_get(routing_key, request_params, request_headers, **kwargs)

    def process_request3(self, routing_key, suffix, request_params, request_headers, **kwargs):
        return self.http_integration_controller.process_request_using_post3(routing_key, suffix, request_params, request_headers, **kwargs)

    def process_request4(self, routing_key, suffix, msg, request_headers, **kwargs):
        return self.http_integration_controller.process_request_using_post4(routing_key, suffix, msg, request_headers, **kwargs)

    """ CustomTranslationController endpoints """

    def get_current_custom_translation(self, **kwargs):
        return self.custom_translation_controller.get_current_custom_translation_using_get(**kwargs)

    def get_custom_translation(self, **kwargs):
        return self.custom_translation_controller.get_custom_translation_using_get(**kwargs)

    def save_custom_translation(self, custom_translation, **kwargs):
        return self.custom_translation_controller.save_custom_translation_using_post(custom_translation, **kwargs)

    """ BlobEntityController endpoints """

    def delete_blob_entity(self, blob_entity_id: BlobEntityId, **kwargs):
        return self.blob_entity_controller.delete_blob_entity_using_delete(blob_entity_id.id, **kwargs)

    def download_blob_entity(self, blob_entity_id: BlobEntityId, **kwargs):
        return self.blob_entity_controller.download_blob_entity_using_get(blob_entity_id.id, **kwargs)

    def get_blob_entities_by_ids(self, blob_entity_ids, **kwargs):
        return self.blob_entity_controller.get_blob_entities_by_ids_using_get(blob_entity_ids, **kwargs)

    def get_blob_entities(self, page_size=100, page=0, **kwargs):
        return self.blob_entity_controller.get_blob_entities_using_get(str(page_size), str(page), **kwargs)

    def get_blob_entity_info_by_id(self, blob_entity_id: BlobEntityId, **kwargs):
        return self.blob_entity_controller.get_blob_entity_info_by_id_using_get(blob_entity_id.id, **kwargs)

    """ TMobileIotCdpIntegrationController endpoints """

    def process_check_using_delete(self, routing_key, **kwargs):
        return self.tmobile_iot_cdp_integration_controller.process_check_using_delete(routing_key, **kwargs)

    def process_check_using_get(self, routing_key, **kwargs):
        return self.tmobile_iot_cdp_integration_controller.process_check_using_get(routing_key, **kwargs)

    def process_check_using_head(self, routing_key, **kwargs):
        return self.tmobile_iot_cdp_integration_controller.process_check_using_head(routing_key, **kwargs)

    def process_check_using_options(self, routing_key, **kwargs):
        return self.tmobile_iot_cdp_integration_controller.process_check_using_options(routing_key, **kwargs)

    def process_check_using_patch(self, routing_key, **kwargs):
        return self.tmobile_iot_cdp_integration_controller.process_check_using_patch(routing_key, **kwargs)

    def process_check(self, routing_key, **kwargs):
        return self.tmobile_iot_cdp_integration_controller.process_check_using_post(routing_key, **kwargs)

    def process_check_using_put(self, routing_key, **kwargs):
        return self.tmobile_iot_cdp_integration_controller.process_check_using_put(routing_key, **kwargs)

    """ UserPermissionsController endpoints """

    def get_allowed_permissions(self, **kwargs):
        return self.user_permissions_controller.get_allowed_permissions_using_get(**kwargs)

    """ OceanConnectIntegrationController endpoints """

    def process_request_using_delete(self, routing_key, msg, request_headers, **kwargs):
        return self.ocean_connect_integration_controller.process_request_using_delete(routing_key, msg, request_headers, **kwargs)

    def process_request_using_get(self, routing_key, msg, request_headers, **kwargs):
        return self.ocean_connect_integration_controller.process_request_using_get(routing_key, msg, request_headers, **kwargs)

    def process_request_using_head(self, routing_key, msg, request_headers, **kwargs):
        return self.ocean_connect_integration_controller.process_request_using_head(routing_key, msg, request_headers, **kwargs)

    def process_request_using_options(self, routing_key, msg, request_headers, **kwargs):
        return self.ocean_connect_integration_controller.process_request_using_options(routing_key, msg, request_headers, **kwargs)

    def process_request_using_patch(self, routing_key, msg, request_headers, **kwargs):
        return self.ocean_connect_integration_controller.process_request_using_patch(routing_key, msg, request_headers, **kwargs)

    def process_request6(self, routing_key, msg, request_headers, **kwargs):
        return self.ocean_connect_integration_controller.process_request_using_post6(routing_key, msg, request_headers, **kwargs)

    def process_request_using_put(self, routing_key, msg, request_headers, **kwargs):
        return self.ocean_connect_integration_controller.process_request_using_put(routing_key, msg, request_headers, **kwargs)

    """ SchedulerEventController endpoints """

    def delete_scheduler_event(self, scheduler_event_id: SchedulerEventId, **kwargs):
        return self.scheduler_event_controller.delete_scheduler_event_using_delete(scheduler_event_id.id, **kwargs)

    def get_scheduler_event_by_id(self, scheduler_event_id: SchedulerEventId, **kwargs):
        return self.scheduler_event_controller.get_scheduler_event_by_id_using_get(scheduler_event_id.id, **kwargs)

    def get_scheduler_event_info_by_id(self, scheduler_event_id: SchedulerEventId, **kwargs):
        return self.scheduler_event_controller.get_scheduler_event_info_by_id_using_get(scheduler_event_id.id, **kwargs)

    def get_scheduler_events_by_ids(self, scheduler_event_ids, **kwargs):
        return self.scheduler_event_controller.get_scheduler_events_by_ids_using_get(scheduler_event_ids, **kwargs)

    def get_scheduler_events(self, **kwargs):
        return self.scheduler_event_controller.get_scheduler_events_using_get(**kwargs)

    def save_scheduler_event(self, scheduler_event, **kwargs):
        return self.scheduler_event_controller.save_scheduler_event_using_post(scheduler_event, **kwargs)

    """ SignUpController endpoints """

    def accept_privacy_policy(self, **kwargs):
        return self.sign_up_controller.accept_privacy_policy_using_post(**kwargs)

    def activate_email(self, email_code, **kwargs):
        return self.sign_up_controller.activate_email_using_get(email_code, **kwargs)

    def activate_user_by_email_code(self, email_code, **kwargs):
        return self.sign_up_controller.activate_user_by_email_code_using_post(email_code, **kwargs)

    def privacy_policy_accepted(self, **kwargs):
        return self.sign_up_controller.privacy_policy_accepted_using_get(**kwargs)

    def resend_email_activation(self, email, **kwargs):
        return self.sign_up_controller.resend_email_activation_using_post(email, **kwargs)

    def sign_up(self, sign_up_request, **kwargs):
        return self.sign_up_controller.sign_up_using_post(sign_up_request, **kwargs)

    """ SelfRegistrationController endpoints """

    def get_privacy_policy(self, **kwargs):
        return self.self_registration_controller.get_privacy_policy_using_get(**kwargs)

    def get_self_registration_params(self, **kwargs):
        return self.self_registration_controller.get_self_registration_params_using_get(**kwargs)

    def get_sign_up_self_registration_params(self, **kwargs):
        return self.self_registration_controller.get_sign_up_self_registration_params_using_get(**kwargs)

    def save_self_registration_params(self, self_registration_params, **kwargs):
        return self.self_registration_controller.save_self_registration_params_using_post(self_registration_params, **kwargs)

    """ WhiteLabelingController endpoints """

    def get_app_theme_css(self, palette_settings, **kwargs):
        return self.white_labeling_controller.get_app_theme_css_using_post(palette_settings, **kwargs)

    def get_current_login_white_label_params(self, **kwargs):
        return self.white_labeling_controller.get_current_login_white_label_params_using_get(**kwargs)

    def get_current_white_label_params(self, **kwargs):
        return self.white_labeling_controller.get_current_white_label_params_using_get(**kwargs)

    def get_login_theme_css(self, palette_settings, **kwargs):
        return self.white_labeling_controller.get_login_theme_css_using_post(palette_settings, **kwargs)

    def get_login_white_label_params(self, **kwargs):
        return self.white_labeling_controller.get_login_white_label_params_using_get(**kwargs)

    def get_white_label_params(self, **kwargs):
        return self.white_labeling_controller.get_white_label_params_using_get(**kwargs)

    def is_customer_white_labeling_allowed(self, **kwargs):
        return self.white_labeling_controller.is_customer_white_labeling_allowed_using_get(**kwargs)

    def is_white_labeling_allowed(self, **kwargs):
        return self.white_labeling_controller.is_white_labeling_allowed_using_get(**kwargs)

    def preview_white_label_params(self, white_labeling_params, **kwargs):
        return self.white_labeling_controller.preview_white_label_params_using_post(white_labeling_params, **kwargs)

    def save_login_white_label_params(self, login_white_labeling_params, **kwargs):
        return self.white_labeling_controller.save_login_white_label_params_using_post(login_white_labeling_params, **kwargs)

    def save_white_label_params(self, white_labeling_params, **kwargs):
        return self.white_labeling_controller.save_white_label_params_using_post(white_labeling_params, **kwargs)

    """ RoleController endpoints """

    def delete_role(self, role_id: RoleId, **kwargs):
        return self.role_controller.delete_role_using_delete(role_id.id, **kwargs)

    def get_role_by_id(self, role_id: RoleId, **kwargs):
        return self.role_controller.get_role_by_id_using_get(role_id.id, **kwargs)

    def get_roles_by_ids(self, role_ids, **kwargs):
        return self.role_controller.get_roles_by_ids_using_get(role_ids, **kwargs)

    def get_roles(self, page_size=100, page=0, **kwargs):
        return self.role_controller.get_roles_using_get(str(page_size), str(page), **kwargs)

    def save_role(self, role, **kwargs):
        return self.role_controller.save_role_using_post(role, **kwargs)

    """ SigFoxIntegrationController endpoints """

    def process_request_using_delete1(self, routing_key, msg, request_headers, **kwargs):
        return self.sigfox_integration_controller.process_request_using_delete1(routing_key, msg, request_headers, **kwargs)

    def process_request_using_get1(self, routing_key, msg, request_headers, **kwargs):
        return self.sigfox_integration_controller.process_request_using_get1(routing_key, msg, request_headers, **kwargs)

    def process_request_using_head1(self, routing_key, msg, request_headers, **kwargs):
        return self.sigfox_integration_controller.process_request_using_head1(routing_key, msg, request_headers, **kwargs)

    def process_request_using_options1(self, routing_key, msg, request_headers, **kwargs):
        return self.sigfox_integration_controller.process_request_using_options1(routing_key, msg, request_headers, **kwargs)

    def process_request_using_patch1(self, routing_key, msg, request_headers, **kwargs):
        return self.sigfox_integration_controller.process_request_using_patch1(routing_key, msg, request_headers, **kwargs)

    def process_request7(self, routing_key, msg, request_headers, **kwargs):
        return self.sigfox_integration_controller.process_request_using_post7(routing_key, msg, request_headers, **kwargs)

    def process_request_using_put1(self, routing_key, msg, request_headers, **kwargs):
        return self.sigfox_integration_controller.process_request_using_put1(routing_key, msg, request_headers, **kwargs)

    """ IntegrationController endpoints """

    def check_integration_connection(self, integration, **kwargs):
        return self.integration_controller.check_integration_connection_using_post(integration, **kwargs)

    def delete_integration(self, integration_id: IntegrationId, **kwargs):
        return self.integration_controller.delete_integration_using_delete(integration_id.id, **kwargs)

    def get_integration_by_id(self, integration_id: IntegrationId, **kwargs):
        return self.integration_controller.get_integration_by_id_using_get(integration_id.id, **kwargs)

    def get_integration_by_routing_key(self, routing_key, **kwargs):
        return self.integration_controller.get_integration_by_routing_key_using_get(routing_key, **kwargs)

    def get_integrations_by_ids(self, integration_ids, **kwargs):
        return self.integration_controller.get_integrations_by_ids_using_get(integration_ids, **kwargs)

    def get_integrations(self, page_size=100, page=0, **kwargs):
        return self.integration_controller.get_integrations_using_get(str(page_size), str(page), **kwargs)

    def save_integration(self, integration, **kwargs):
        return self.integration_controller.save_integration_using_post(integration, **kwargs)

    """ OwnerController endpoints """

    def change_owner_to_customer(self, owner_id, entity_id: EntityId, **kwargs):
        return self.owner_controller.change_owner_to_customer_using_post(owner_id.id, entity_id.entity_type, entity_id.id, **kwargs)

    def change_owner_to_tenant(self, owner_id, entity_id: EntityId, **kwargs):
        return self.owner_controller.change_owner_to_tenant_using_post(owner_id, entity_id.entity_type, entity_id.id, **kwargs)

    """ GroupPermissionController endpoints """

    def delete_group_permission(self, group_permission_id: GroupPermissionId, **kwargs):
        return self.group_permission_controller.delete_group_permission_using_delete(group_permission_id.id, **kwargs)

    def get_entity_group_permissions(self, entity_group_id: EntityGroupId, **kwargs):
        return self.group_permission_controller.get_entity_group_permissions_using_get(entity_group_id.id, **kwargs)

    def get_group_permission_by_id(self, group_permission_id: GroupPermissionId, **kwargs):
        return self.group_permission_controller.get_group_permission_by_id_using_get(group_permission_id.id, **kwargs)

    def get_group_permission_info_by_id(self, group_permission_id: GroupPermissionId, is_user_group, **kwargs):
        return self.group_permission_controller.get_group_permission_info_by_id_using_get(group_permission_id.id, is_user_group, **kwargs)

    def get_user_group_permissions(self, user_group_id, **kwargs):
        return self.group_permission_controller.get_user_group_permissions_using_get(user_group_id.id, **kwargs)

    def load_user_group_permission_infos(self, permissions, **kwargs):
        return self.group_permission_controller.load_user_group_permission_infos_using_post(permissions, **kwargs)

    def save_group_permission(self, group_permission, **kwargs):
        return self.group_permission_controller.save_group_permission_using_post(group_permission, **kwargs)

    """ CustomMenuController endpoints """

    def get_current_custom_menu(self, **kwargs):
        return self.custom_menu_controller.get_current_custom_menu_using_get(**kwargs)

    def get_custom_menu(self, **kwargs):
        return self.custom_menu_controller.get_custom_menu_using_get(**kwargs)

    def save_custom_menu(self, **kwargs):
        return self.custom_menu_controller.save_custom_menu_using_post(**kwargs)

    """ ReportController endpoints """

    def download_dashboard_report(self, dashboard_id: DashboardId, report_params, **kwargs):
        return self.report_controller.download_dashboard_report_using_post(dashboard_id.id, report_params, **kwargs)

    def download_test_report(self, report_config, **kwargs):
        return self.report_controller.download_test_report_using_post(report_config, **kwargs)

    """ RuleEngineController endpoints """

    def handle_rule_engine_request(self, request_body, **kwargs):
        return self.rule_engine_controller.handle_rule_engine_request_using_post(request_body, **kwargs)

    def handle_rule_engine_request1(self, entity_id: EntityId, timeout, request_body, **kwargs):
        return self.rule_engine_controller.handle_rule_engine_request_using_post1(entity_id.entity_type, entity_id.id, timeout, request_body, **kwargs)

    def handle_rule_engine_request2(self, entity_id: EntityId, request_body, **kwargs):
        return self.rule_engine_controller.handle_rule_engine_request_using_post2(entity_id.entity_type, entity_id.id, request_body, **kwargs)

    """ ConverterController endpoints """

    def delete_converter(self, converter_id: ConverterId, **kwargs):
        return self.converter_controller.delete_converter_using_delete(converter_id.id, **kwargs)

    def get_converter_by_id(self, converter_id: ConverterId, **kwargs):
        return self.converter_controller.get_converter_by_id_using_get(converter_id.id, **kwargs)

    def get_converters_by_ids(self, converter_ids, **kwargs):
        return self.converter_controller.get_converters_by_ids_using_get(converter_ids, **kwargs)

    def get_converters(self, page_size=100, page=0, **kwargs):
        return self.converter_controller.get_converters_using_get(str(page_size), str(page), **kwargs)

    def get_latest_converter_debug_input(self, converter_id: ConverterId, **kwargs):
        return self.converter_controller.get_latest_converter_debug_input_using_get(converter_id.id, **kwargs)

    def save_converter(self, converter, **kwargs):
        return self.converter_controller.save_converter_using_post(converter, **kwargs)

    def test_down_link_converter(self, input_params, **kwargs):
        return self.converter_controller.test_down_link_converter_using_post(input_params, **kwargs)

    def test_up_link_converter(self, input_params, **kwargs):
        return self.converter_controller.test_up_link_converter_using_post(input_params, **kwargs)

    """ TrailController endpoints """

    def delete_device1(self, **kwargs):
        return self.trail_controller.delete_device_using_delete1(**kwargs)

    """ ThingParkIntegrationController endpoints """

    def process_request_tpe_using_delete(self, routing_key, all_request_params, msg, request_headers, **kwargs):
        return self.thing_park_integration_controller.process_request_tpe_using_delete(routing_key, all_request_params, msg, request_headers, **kwargs)

    def process_request_tpe_using_get(self, routing_key, all_request_params, msg, request_headers, **kwargs):
        return self.thing_park_integration_controller.process_request_tpe_using_get(routing_key, all_request_params, msg, request_headers, **kwargs)

    def process_request_tpe_using_head(self, routing_key, all_request_params, msg, request_headers, **kwargs):
        return self.thing_park_integration_controller.process_request_tpe_using_head(routing_key, all_request_params, msg, request_headers, **kwargs)

    def process_request_tpe_using_options(self, routing_key, all_request_params, msg, request_headers, **kwargs):
        return self.thing_park_integration_controller.process_request_tpe_using_options(routing_key, all_request_params, msg, request_headers, **kwargs)

    def process_request_tpe_using_patch(self, routing_key, all_request_params, msg, request_headers, **kwargs):
        return self.thing_park_integration_controller.process_request_tpe_using_patch(routing_key, all_request_params, msg, request_headers, **kwargs)

    def process_request_tpe_using_post(self, routing_key, all_request_params, msg, request_headers, **kwargs):
        return self.thing_park_integration_controller.process_request_tpe_using_post(routing_key, all_request_params, msg, request_headers, **kwargs)

    def process_request_tpe_using_put(self, routing_key, all_request_params, msg, request_headers, **kwargs):
        return self.thing_park_integration_controller.process_request_tpe_using_put(routing_key, all_request_params, msg, request_headers, **kwargs)

    def process_request_tpe_using_delete1(self, routing_key, all_request_params, msg, request_headers, **kwargs):
        return self.thing_park_integration_controller.process_request_using_delete3(routing_key, all_request_params, msg, request_headers, **kwargs)

    def process_request_tpe_using_get1(self, routing_key, all_request_params, msg, request_headers, **kwargs):
        return self.thing_park_integration_controller.process_request_using_get3(routing_key, all_request_params, msg, request_headers, **kwargs)

    def process_request_using_head3(self, routing_key, all_request_params, msg, request_headers, **kwargs):
        return self.thing_park_integration_controller.process_request_using_head3(routing_key, all_request_params, msg, request_headers, **kwargs)

    def process_request_using_options3(self, routing_key, all_request_params, msg, request_headers, **kwargs):
        return self.thing_park_integration_controller.process_request_using_options3(routing_key, all_request_params, msg, request_headers, **kwargs)

    def process_request_using_patch3(self, routing_key, all_request_params, msg, request_headers, **kwargs):
        return self.thing_park_integration_controller.process_request_using_patch3(routing_key, all_request_params, msg, request_headers, **kwargs)

    def process_request9(self, routing_key, all_request_params, msg, request_headers, **kwargs):
        return self.thing_park_integration_controller.process_request_using_post9(routing_key, all_request_params, msg, request_headers, **kwargs)

    def process_request_using_put3(self, routing_key, all_request_params, msg, request_headers, **kwargs):
        return self.thing_park_integration_controller.process_request_using_put3(routing_key, all_request_params, msg, request_headers, **kwargs)

    def get_tenants_by_ids(self, tenant_ids, **kwargs):
        return self.tenant_controller.get_tenants_by_ids_using_get(tenant_ids, **kwargs)

    def export_group_dashboards(self, entity_group_id: EntityGroupId, limit, **kwargs):
        return self.dashboard_controller.export_group_dashboards_using_get(entity_group_id.id, limit, **kwargs)

    def get_dashboards_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size=100, page=0, **kwargs):
        return self.dashboard_controller.get_dashboards_by_entity_group_id_using_get(entity_group_id.id, str(page_size), str(page), **kwargs)

    def get_dashboards_by_ids(self, dashboard_ids, **kwargs):
        return self.dashboard_controller.get_dashboards_by_ids_using_get(dashboard_ids, **kwargs)

    def get_group_dashboards(self, entity_group_id: EntityGroupId, page_size=100, page=0, **kwargs):
        return self.dashboard_controller.get_group_dashboards_using_get(entity_group_id.id, str(page_size), str(page), **kwargs)

    def get_user_dashboards(self, page_size=100, page=0, **kwargs):
        return self.dashboard_controller.get_user_dashboards_using_get(str(page_size), str(page), **kwargs)

    def import_group_dashboards(self, entity_group_id: EntityGroupId, dashboard_list, **kwargs):
        return self.dashboard_controller.import_group_dashboards_using_post(entity_group_id.id, dashboard_list, **kwargs)

    def find_by_from(self, from_id, from_type, **kwargs):
        return self.entity_relation_controller.find_by_from_using_get(from_id, from_type, **kwargs)

    def find_by_from1(self, from_id, from_type, relation_type, **kwargs):
        return self.entity_relation_controller.find_by_from_using_get1(from_id, from_type, relation_type, **kwargs)

    def find_by_to(self, to_id, to_type, **kwargs):
        return self.entity_relation_controller.find_by_to_using_get(to_id, to_type, **kwargs)

    def find_by_to1(self, to_id, to_type, relation_type, **kwargs):
        return self.entity_relation_controller.find_by_to_using_get1(to_id, to_type, relation_type, **kwargs)

    def get_entity_views_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size=100, page=0, **kwargs):
        return self.entity_view_controller.get_entity_views_by_entity_group_id_using_get(entity_group_id.id, str(page_size), str(page), **kwargs)

    def get_entity_views_by_ids(self, entity_view_ids, **kwargs):
        return self.entity_view_controller.get_entity_views_by_ids_using_get(entity_view_ids, **kwargs)

    def get_user_entity_views(self, page_size=100, page=0, **kwargs):
        return self.entity_view_controller.get_user_entity_views_using_get(str(page_size), str(page), **kwargs)

    def get_customers_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size=100, page=0, **kwargs):
        return self.customer_controller.get_customers_by_entity_group_id_using_get(entity_group_id.id, str(page_size), str(page), **kwargs)

    def get_customers_by_ids(self, customer_ids, **kwargs):
        return self.customer_controller.get_customers_by_ids_using_get(customer_ids, **kwargs)

    def get_user_customers(self, page_size=100, page=0, **kwargs):
        return self.customer_controller.get_user_customers_using_get(str(page_size), str(page), **kwargs)

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
        self.device_api_controller = DeviceApiControllerApi(self.api_client)
        self.device_controller = DeviceControllerApi(self.api_client)
        self.device_profile_controller = DeviceProfileControllerApi(self.api_client)
        self.entity_group_controller = EntityGroupControllerApi(self.api_client)
        self.entity_query_controller = EntityQueryControllerApi(self.api_client)
        self.entity_relation_controller = EntityRelationControllerApi(self.api_client)
        self.entity_view_controller = EntityViewControllerApi(self.api_client)
        self.event_controller = EventControllerApi(self.api_client)
        self.group_permission_controller = GroupPermissionControllerApi(self.api_client)
        self.http_integration_controller = HttpIntegrationControllerApi(self.api_client)
        self.integration_controller = IntegrationControllerApi(self.api_client)
        self.o_auth_2_config_template_controller = OAuth2ConfigTemplateControllerApi(self.api_client)
        self.o_auth_2_controller = OAuth2ControllerApi(self.api_client)
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
        self.trail_controller = TrailControllerApi(self.api_client)
        self.tenant_profile_controller = TenantProfileControllerApi(self.api_client)
        self.thing_park_integration_controller = ThingParkIntegrationControllerApi(self.api_client)
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
