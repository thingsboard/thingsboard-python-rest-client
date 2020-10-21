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
# coding: utf-8


from __future__ import absolute_import

# import models into model package
from .admin_settings import AdminSettings
from .admin_settings_id import AdminSettingsId
from .alarm import Alarm
from .alarm_condition import AlarmCondition
from .alarm_condition_spec import AlarmConditionSpec
from .alarm_data import AlarmData
from .alarm_data_page_link import AlarmDataPageLink
from .alarm_data_query import AlarmDataQuery
from .alarm_id import AlarmId
from .alarm_info import AlarmInfo
from .alarm_rule import AlarmRule
from .alarm_schedule import AlarmSchedule
from .allowed_permissions_info import AllowedPermissionsInfo
from .asset import Asset
from .asset_id import AssetId
from .asset_search_query import AssetSearchQuery
from .attributes_entity_view import AttributesEntityView
from .audit_log import AuditLog
from .audit_log_id import AuditLogId
from .blob_entity_id import BlobEntityId
from .blob_entity_info import BlobEntityInfo
from .blob_entity_with_customer_info import BlobEntityWithCustomerInfo
from .claim_request import ClaimRequest
from .client_registration_dto import ClientRegistrationDto
from .component_descriptor import ComponentDescriptor
from .component_descriptor_id import ComponentDescriptorId
from .contact_basedobject import ContactBasedobject
from .converter import Converter
from .converter_id import ConverterId
from .custom_menu import CustomMenu
from .custom_menu_item import CustomMenuItem
from .custom_translation import CustomTranslation
from .customer import Customer
from .customer_id import CustomerId
from .dashboard import Dashboard
from .dashboard_id import DashboardId
from .dashboard_info import DashboardInfo
from .default_rule_chain_create_request import DefaultRuleChainCreateRequest
from .deferred_result_response_entity import DeferredResultResponseEntity
from .device import Device
from .device_configuration import DeviceConfiguration
from .device_credentials import DeviceCredentials
from .device_credentials_id import DeviceCredentialsId
from .device_data import DeviceData
from .device_id import DeviceId
from .device_profile import DeviceProfile
from .device_profile_alarm import DeviceProfileAlarm
from .device_profile_configuration import DeviceProfileConfiguration
from .device_profile_data import DeviceProfileData
from .device_profile_id import DeviceProfileId
from .device_profile_info import DeviceProfileInfo
from .device_profile_provision_configuration import DeviceProfileProvisionConfiguration
from .device_profile_transport_configuration import DeviceProfileTransportConfiguration
from .device_search_query import DeviceSearchQuery
from .device_transport_configuration import DeviceTransportConfiguration
from .domain_info import DomainInfo
from .entity_count_query import EntityCountQuery
from .entity_data import EntityData
from .entity_data_page_link import EntityDataPageLink
from .entity_data_query import EntityDataQuery
from .entity_data_sort_order import EntityDataSortOrder
from .entity_filter import EntityFilter
from .entity_group import EntityGroup
from .entity_group_id import EntityGroupId
from .entity_group_info import EntityGroupInfo
from .entity_id import EntityId
from .entity_info import EntityInfo
from .entity_key import EntityKey
from .entity_relation import EntityRelation
from .entity_relation_info import EntityRelationInfo
from .entity_relations_query import EntityRelationsQuery
from .entity_subtype import EntitySubtype
from .entity_type_filter import EntityTypeFilter
from .entity_view import EntityView
from .entity_view_id import EntityViewId
from .entity_view_search_query import EntityViewSearchQuery
from .event import Event
from .event_id import EventId
from .favicon import Favicon
from .file import File
from .group_permission import GroupPermission
from .group_permission_id import GroupPermissionId
from .group_permission_info import GroupPermissionInfo
from .input_stream import InputStream
from .integration import Integration
from .integration_id import IntegrationId
from .key_filter import KeyFilter
from .key_filter_predicate import KeyFilterPredicate
from .login_white_labeling_params import LoginWhiteLabelingParams
from .mapstring_ts_value import MapstringTsValue
from .merged_group_permission_info import MergedGroupPermissionInfo
from .merged_group_type_permission_info import MergedGroupTypePermissionInfo
from .merged_user_permissions import MergedUserPermissions
from .node_connection_info import NodeConnectionInfo
from .o_auth2_basic_mapper_config import OAuth2BasicMapperConfig
from .o_auth2_client_info import OAuth2ClientInfo
from .o_auth2_client_registration_template import OAuth2ClientRegistrationTemplate
from .o_auth2_client_registration_template_id import OAuth2ClientRegistrationTemplateId
from .o_auth2_clients_domain_params import OAuth2ClientsDomainParams
from .o_auth2_clients_params import OAuth2ClientsParams
from .o_auth2_custom_mapper_config import OAuth2CustomMapperConfig
from .o_auth2_mapper_config import OAuth2MapperConfig
from .page_data_alarm_data import PageDataAlarmData
from .page_data_alarm_info import PageDataAlarmInfo
from .page_data_asset import PageDataAsset
from .page_data_audit_log import PageDataAuditLog
from .page_data_blob_entity_with_customer_info import PageDataBlobEntityWithCustomerInfo
from .page_data_contact_basedobject import PageDataContactBasedobject
from .page_data_converter import PageDataConverter
from .page_data_customer import PageDataCustomer
from .page_data_dashboard_info import PageDataDashboardInfo
from .page_data_device import PageDataDevice
from .page_data_device_profile import PageDataDeviceProfile
from .page_data_device_profile_info import PageDataDeviceProfileInfo
from .page_data_entity_data import PageDataEntityData
from .page_data_entity_info import PageDataEntityInfo
from .page_data_entity_view import PageDataEntityView
from .page_data_event import PageDataEvent
from .page_data_integration import PageDataIntegration
from .page_data_role import PageDataRole
from .page_data_rule_chain import PageDataRuleChain
from .page_data_short_entity_view import PageDataShortEntityView
from .page_data_tenant import PageDataTenant
from .page_data_tenant_info import PageDataTenantInfo
from .page_data_tenant_profile import PageDataTenantProfile
from .page_data_user import PageDataUser
from .page_data_widgets_bundle import PageDataWidgetsBundle
from .palette import Palette
from .palette_settings import PaletteSettings
from .relations_search_parameters import RelationsSearchParameters
from .report_config import ReportConfig
from .resource import Resource
from .response_entity import ResponseEntity
from .role import Role
from .role_id import RoleId
from .rule_chain import RuleChain
from .rule_chain_connection_info import RuleChainConnectionInfo
from .rule_chain_data import RuleChainData
from .rule_chain_id import RuleChainId
from .rule_chain_meta_data import RuleChainMetaData
from .rule_node import RuleNode
from .rule_node_id import RuleNodeId
from .scheduler_event import SchedulerEvent
from .scheduler_event_id import SchedulerEventId
from .scheduler_event_info import SchedulerEventInfo
from .scheduler_event_with_customer_info import SchedulerEventWithCustomerInfo
from .security_settings import SecuritySettings
from .self_registration_params import SelfRegistrationParams
from .share_group_request import ShareGroupRequest
from .short_customer_info import ShortCustomerInfo
from .short_entity_view import ShortEntityView
from .sign_up_request import SignUpRequest
from .sign_up_self_registration_params import SignUpSelfRegistrationParams
from .telemetry_entity_view import TelemetryEntityView
from .tenant import Tenant
from .tenant_id import TenantId
from .tenant_info import TenantInfo
from .tenant_profile import TenantProfile
from .tenant_profile_data import TenantProfileData
from .tenant_profile_id import TenantProfileId
from .ts_value import TsValue
from .update_message import UpdateMessage
from .uri import URI
from .url import URL
from .user import User
from .user_id import UserId
from .user_password_policy import UserPasswordPolicy
from .white_labeling_params import WhiteLabelingParams
from .widget_type import WidgetType
from .widget_type_id import WidgetTypeId
from .widgets_bundle import WidgetsBundle
from .widgets_bundle_id import WidgetsBundleId