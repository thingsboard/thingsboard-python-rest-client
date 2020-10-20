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



    def export_group_dashboards(self, entity_group_id: EntityGroupId, limit, **kwargs):
        return self.dashboard_controller.export_group_dashboards_using_get(entity_group_id, limit, **kwargs)

    def get_dashboards_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size=100, page=0, **kwargs):
        return self.dashboard_controller.get_dashboards_by_entity_group_id_using_get(entity_group_id, str(page_size), str(page), **kwargs)

    def get_dashboards_by_ids(self, dashboard_ids, **kwargs):
        return self.dashboard_controller.get_dashboards_by_ids_using_get(dashboard_ids, **kwargs)

    def get_group_dashboards(self, entity_group_id: EntityGroupId, page_size=100, page=0, **kwargs):
        return self.dashboard_controller.get_group_dashboards_using_get(entity_group_id, str(page_size), str(page), **kwargs)

    def get_user_dashboards(self, page_size=100, page=0, **kwargs):
        return self.dashboard_controller.get_user_dashboards_using_get(str(page_size), str(page), **kwargs)

    def import_group_dashboards(self, entity_group_id: EntityGroupId, dashboard_list, **kwargs):
        return self.dashboard_controller.import_group_dashboards_using_post(entity_group_id, dashboard_list, **kwargs)

    def get_all_customer_users(self, page_size=100, page=0, **kwargs):
        return self.user_controller.get_all_customer_users_using_get(str(page_size), str(page), **kwargs)

    def get_user_users(self, page_size=100, page=0, **kwargs):
        return self.user_controller.get_user_users_using_get(str(page_size), str(page), **kwargs)

    def get_users_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size=100, page=0, **kwargs):
        return self.user_controller.get_users_by_entity_group_id_using_get(entity_group_id, str(page_size), str(page), **kwargs)

    def get_users_by_ids(self, user_ids, **kwargs):
        return self.user_controller.get_users_by_ids_using_get(user_ids, **kwargs)

    def get_tenants_by_ids(self, tenant_ids, **kwargs):
        return self.tenant_controller.get_tenants_by_ids_using_get(tenant_ids, **kwargs)

    def get_entity_views_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size=100, page=0, **kwargs):
        return self.entity_view_controller.get_entity_views_by_entity_group_id_using_get(entity_group_id, str(page_size), str(page), **kwargs)

    def get_entity_views_by_ids(self, entity_view_ids, **kwargs):
        return self.entity_view_controller.get_entity_views_by_ids_using_get(entity_view_ids, **kwargs)

    def get_user_entity_views(self, page_size=100, page=0, **kwargs):
        return self.entity_view_controller.get_user_entity_views_using_get(str(page_size), str(page), **kwargs)

    def get_assets_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size=100, page=0, **kwargs):
        return self.asset_controller.get_assets_by_entity_group_id_using_get(entity_group_id, str(page_size), str(page), **kwargs)

    def get_user_assets(self, page_size=100, page=0, **kwargs):
        return self.asset_controller.get_user_assets_using_get(str(page_size), str(page), **kwargs)

    def get_customers_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size=100, page=0, **kwargs):
        return self.customer_controller.get_customers_by_entity_group_id_using_get(entity_group_id, str(page_size), str(page), **kwargs)

    def get_customers_by_ids(self, customer_ids, **kwargs):
        return self.customer_controller.get_customers_by_ids_using_get(customer_ids, **kwargs)

    def get_user_customers(self, page_size=100, page=0, **kwargs):
        return self.customer_controller.get_user_customers_using_get(str(page_size), str(page), **kwargs)

    def find_by_from(self, from_id, from_type, **kwargs):
        return self.entity_relation_controller.find_by_from_using_get(from_id, from_type, **kwargs)

    def find_by_from1(self, from_id, from_type, relation_type, **kwargs):
        return self.entity_relation_controller.find_by_from_using_get1(from_id, from_type, relation_type, **kwargs)

    def find_by_to(self, to_id, to_type, **kwargs):
        return self.entity_relation_controller.find_by_to_using_get(to_id, to_type, **kwargs)

    def find_by_to1(self, to_id, to_type, relation_type, **kwargs):
        return self.entity_relation_controller.find_by_to_using_get1(to_id, to_type, relation_type, **kwargs)

    def get_devices_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size=100, page=0, **kwargs):
        return self.device_controller.get_devices_by_entity_group_id_using_get(entity_group_id, str(page_size), str(page), **kwargs)

    def get_user_devices(self, page_size=100, page=0, **kwargs):
        return self.device_controller.get_user_devices_using_get(str(page_size), str(page), **kwargs)

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
