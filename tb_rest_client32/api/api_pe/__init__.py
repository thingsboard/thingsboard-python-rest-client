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

from __future__ import absolute_import

# flake8: noqa

# import apis into api_pe package
from .admin_controller_api import AdminControllerApi
from .alarm_controller_api import AlarmControllerApi
from .asset_controller_api import AssetControllerApi
from .audit_log_controller_api import AuditLogControllerApi
from .auth_controller_api import AuthControllerApi
from .blob_entity_controller_api import BlobEntityControllerApi
from .component_descriptor_controller_api import ComponentDescriptorControllerApi
from .converter_controller_api import ConverterControllerApi
from .custom_menu_controller_api import CustomMenuControllerApi
from .custom_translation_controller_api import CustomTranslationControllerApi
from .customer_controller_api import CustomerControllerApi
from .dashboard_controller_api import DashboardControllerApi
from .device_api_controller_api import DeviceApiControllerApi
from .device_controller_api import DeviceControllerApi
from .device_profile_controller_api import DeviceProfileControllerApi
from .entity_group_controller_api import EntityGroupControllerApi
from .entity_query_controller_api import EntityQueryControllerApi
from .entity_relation_controller_api import EntityRelationControllerApi
from .entity_view_controller_api import EntityViewControllerApi
from .event_controller_api import EventControllerApi
from .group_permission_controller_api import GroupPermissionControllerApi
from .http_integration_controller_api import HttpIntegrationControllerApi
from .integration_controller_api import IntegrationControllerApi
from .o_auth_2_config_template_controller_api import OAuth2ConfigTemplateControllerApi
from .o_auth_2_controller_api import OAuth2ControllerApi
from .ocean_connect_integration_controller_api import OceanConnectIntegrationControllerApi
from .owner_controller_api import OwnerControllerApi
from .queue_controller_api import QueueControllerApi
from .report_controller_api import ReportControllerApi
from .role_controller_api import RoleControllerApi
from .rpc_controller_api import RpcControllerApi
from .rule_chain_controller_api import RuleChainControllerApi
from .rule_engine_controller_api import RuleEngineControllerApi
from .scheduler_event_controller_api import SchedulerEventControllerApi
from .self_registration_controller_api import SelfRegistrationControllerApi
from .sig_fox_integration_controller_api import SigFoxIntegrationControllerApi
from .sign_up_controller_api import SignUpControllerApi
from .t_mobile_iot_cdp_integration_controller_api import TMobileIotCdpIntegrationControllerApi
from .telemetry_controller_api import TelemetryControllerApi
from .tenant_controller_api import TenantControllerApi
from .tenant_profile_controller_api import TenantProfileControllerApi
from .trail_controller_api import TrailControllerApi
from .thing_park_integration_controller_api import ThingParkIntegrationControllerApi
from .user_controller_api import UserControllerApi
from .user_permissions_controller_api import UserPermissionsControllerApi
from .white_labeling_controller_api import WhiteLabelingControllerApi
from .widget_type_controller_api import WidgetTypeControllerApi
from .widgets_bundle_controller_api import WidgetsBundleControllerApi
