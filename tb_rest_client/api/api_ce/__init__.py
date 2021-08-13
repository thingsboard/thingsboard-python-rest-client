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
from .component_descriptor_controller_api import ComponentDescriptorControllerApi
from .customer_controller_api import CustomerControllerApi
from .dashboard_controller_api import DashboardControllerApi
from .device_api_controller_api import DeviceApiControllerApi
from .device_profile_controller_api import DeviceProfileControllerApi
from .edge_controller_api import EdgeControllerApi
from .edge_event_controller_api import EdgeEventControllerApi
from .entity_query_controller import EntityQueryControllerApi
from .device_controller_api import DeviceControllerApi
from .entity_relation_controller_api import EntityRelationControllerApi
from .entity_view_controller_api import EntityViewControllerApi
from .event_controller_api import EventControllerApi
from .lwm_2m_controller_api import Lwm2mControllerApi
from .ota_package_controller_api import OtaPackageControllerApi
from .tb_resource_controller_api import TbResourceControllerApi
from .tenant_profile_controller_api import TenantProfileControllerApi
from .queue_controller_api import QueueControllerApi
from .rpc_controller_api import RpcControllerApi
from .rule_chain_controller_api import RuleChainControllerApi
from .telemetry_controller_api import TelemetryControllerApi
from .tenant_controller_api import TenantControllerApi
from .user_controller_api import UserControllerApi
from .widget_type_controller_api import WidgetTypeControllerApi
from .widgets_bundle_controller_api import WidgetsBundleControllerApi
