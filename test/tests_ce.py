#  Copyright 2024. ThingsBoard
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

import unittest

from tb_rest_client.rest_client_ce import *
from tb_rest_client.rest_client_base import *
from tb_rest_client.models.models_ce import *


TB_URL_CE = 'http://0.0.0.0:8080'

TB_TENANT_USERNAME_CE = 'tenant@thingsboard.org'
TB_TENANT_PASSWORD_CE = 'tenant'

TB_SYSADMIN_USERNAME_CE = 'sysadmin@thingsboard.org'
TB_SYSADMIN_PASSWORD_CE = 'sysadmin'


class TBClientCETests(unittest.TestCase):
    client = None

    @classmethod
    def setUpClass(cls) -> None:
        # ThingsBoard REST API URL
        url = TB_URL_CE

        # Default Tenant Administrator credentials
        username = TB_TENANT_USERNAME_CE
        password = TB_TENANT_PASSWORD_CE

        with RestClientCE(url) as cls.client:
            cls.client.login(username, password)


class AlarmControllerTests(TBClientCETests):
    test_alarm = None
    device = None
    device_profile_id = None

    @classmethod
    def setUpClass(cls) -> None:
        super(AlarmControllerTests, cls).setUpClass()

        cls.device_profile_id = cls.client.get_default_device_profile_info().id

        cls.device = Device(name='Test', label='Test', device_profile_id=cls.device_profile_id)
        cls.device = cls.client.save_device(body=cls.device)

        cls.test_alarm = Alarm(name='Test', type='default',
                               originator=cls.device.id,
                               severity='CRITICAL', status='CLEARED_UNACK', acknowledged=False, cleared=False)
        cls.test_alarm = cls.client.save_alarm(cls.test_alarm)
        assert isinstance(cls.test_alarm, Alarm)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_alarm(cls.test_alarm.id)
        cls.client.delete_device(cls.device.id)

    def test_get_all_alarms(self):
        self.assertIsInstance(self.client.get_all_alarms(10, 0), PageDataAlarmInfo)

    def test_get_alarm_info_by_id(self):
        self.assertIsInstance(self.client.get_alarm_info_by_id(self.test_alarm.id), AlarmInfo)

    def test_get_alarms(self):
        self.assertIsInstance(self.client.get_alarms(self.device.id, 10, 0), PageDataAlarmInfo)

    def test_clear_alarm(self):
        self.assertIsInstance(self.client.clear_alarm(self.test_alarm.id), AlarmInfo)

    def test_ack_alarm(self):
        self.assertIsInstance(self.client.ack_alarm(self.test_alarm.id), AlarmInfo)

    def test_get_alarm_by_id(self):
        self.assertIsInstance(self.client.get_alarm_by_id(self.test_alarm.id), Alarm)


class AlarmCommentControllerTests(TBClientCETests):
    alarm = None
    alarm_comment = None
    device_profile_id = None
    device = None

    @classmethod
    def setUpClass(cls) -> None:
        super(AlarmCommentControllerTests, cls).setUpClass()

        cls.device_profile_id = cls.client.get_default_device_profile_info().id

        cls.device = Device(name='Test', label='Test', device_profile_id=cls.device_profile_id)
        cls.device = cls.client.save_device(body=cls.device)

        cls.test_alarm = cls.client.save_alarm(Alarm(name='Test', type='default',
                                                     originator=cls.device.id,
                                                     severity='CRITICAL', status='CLEARED_UNACK', acknowledged=False,
                                                     cleared=False))
        cls.alarm = cls.client.get_all_alarms(10, 0).data[0]
        cls.alarm_comment = cls.client.save_alarm_comment(cls.alarm.id,
                                                          AlarmComment(name='Test Comment', comment='Test comment'))

    def test_get_alarm_comments(self):
        self.assertIsInstance(self.client.get_alarm_comments(self.alarm.id, 10, 0), PageDataAlarmCommentInfo)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_alarm_comment(cls.alarm.id, cls.alarm_comment.id)
        cls.client.delete_alarm(cls.alarm.id)
        cls.client.delete_device(cls.device.id)


class AssetControllerTests(TBClientCETests):
    test_asset = None
    asset_profile_id = None

    @classmethod
    def setUpClass(cls) -> None:
        super(AssetControllerTests, cls).setUpClass()

        cls.asset_profile_id = cls.client.get_default_asset_profile_info().id
        cls.test_asset = Asset(name="Test Asset", asset_profile_id=cls.asset_profile_id)
        cls.test_asset = cls.client.save_asset(body=cls.test_asset)
        cls.customer = cls.client.get_customers(10, 0).data[0]

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_asset(cls.test_asset.id)

    def test_get_tenant_assets(self):
        self.assertIsInstance(self.client.get_tenant_assets(10, 0), PageDataAsset)

    def test_get_tenant_asset(self):
        self.assertIsInstance(self.client.get_tenant_asset(self.test_asset.name), Asset)

    def test_get_tenant_asset_infos(self):
        self.assertIsInstance(self.client.get_tenant_asset_infos(10, 0), PageDataAssetInfo)

    def test_get_customer_assets(self):
        self.assertIsInstance(self.client.get_customer_assets(self.customer.id, 10, 0), PageDataAsset)

    def test_get_customer_asset_infos(self):
        self.assertIsInstance(self.client.get_customer_asset_infos(self.customer.id, 10, 0), PageDataAssetInfo)

    def test_get_assets_by_ids(self):
        self.assertIsInstance(self.client.get_assets_by_ids([self.test_asset.id.id]), list)

    def test_get_asset_types(self):
        self.assertIsInstance(self.client.get_asset_types(), list)

    def test_get_asset_info_by_id(self):
        self.assertIsInstance(self.client.get_asset_info_by_id(self.test_asset.id), AssetInfo)

    def test_get_asset_by_id(self):
        self.assertIsInstance(self.client.get_asset_by_id(self.test_asset.id), Asset)


class AssetProfileControllerTests(TBClientCETests):
    asset_profile = None

    @classmethod
    def setUpClass(cls) -> None:
        super(AssetProfileControllerTests, cls).setUpClass()

        cls.asset_profile = AssetProfile(name='Test Asset', default=False)
        cls.asset_profile = cls.client.save_asset_profile(cls.asset_profile)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_asset_profile(cls.asset_profile.id)

    def test_get_asset_profile_by_id(self):
        self.assertIsInstance(self.client.get_asset_profile_by_id(self.asset_profile.id), AssetProfile)

    def test_get_asset_profile_info_by_id(self):
        self.assertIsInstance(self.client.get_asset_profile_info_by_id(self.asset_profile.id), AssetProfileInfo)

    def test_get_default_asset_profile_info(self):
        self.assertIsInstance(self.client.get_default_asset_profile_info(), AssetProfileInfo)

    def test_get_asset_profile_infos(self):
        self.assertIsInstance(self.client.get_asset_profile_infos(10, 0), PageDataAssetProfileInfo)

    def test_get_asset_profiles(self):
        self.assertIsInstance(self.client.get_asset_profiles(10, 0), PageDataAssetProfile)


class AuditLogControllerTests(TBClientCETests):
    customer = None
    device = None

    @classmethod
    def setUpClass(cls) -> None:
        super(AuditLogControllerTests, cls).setUpClass()

        cls.customer = cls.client.get_customers(10, 0).data[0]

    def test_get_audit_logs(self):
        self.assertIsInstance(self.client.get_audit_logs(10, 0), PageDataAuditLog)

    def test_get_audit_logs_by_customer_id(self):
        self.assertIsInstance(self.client.get_audit_logs_by_customer_id(self.customer.id, 10, 0), PageDataAuditLog)

    def test_get_audit_logs_by_entity_id(self):
        self.assertIsInstance(self.client.get_audit_logs_by_entity_id(EntityId(self.customer.id, 'CUSTOMER'), 10, 0),
                              PageDataAuditLog)

    def test_get_audit_logs_by_user_id(self):
        self.assertIsInstance(self.client.get_audit_logs_by_user_id(UserId(self.customer.id, 'USER'), 10, 0),
                              PageDataAuditLog)


class TelemetryControllerTests(TBClientCETests):
    device = None
    device_profile_id = None

    @classmethod
    def setUpClass(cls) -> None:
        super(TelemetryControllerTests, cls).setUpClass()

        cls.device_profile_id = cls.client.get_default_device_profile_info().id
        cls.device = Device(name='Test CE', device_profile_id=cls.device_profile_id)
        cls.device = cls.client.save_device(cls.device)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_device(cls.device.id)

    def test_get_latest_timeseries(self):
        self.assertIsInstance(self.client.get_latest_timeseries(self.device.id), dict)

    def test_get_timeseries(self):
        self.assertIsInstance(self.client.get_timeseries(self.device.id, 'string_read3', 164999693900, 168999693900),
                              dict)

    def test_get_attributes_by_scope(self):
        self.assertIsInstance(self.client.get_attributes_by_scope(self.device.id, 'SHARED_SCOPE'), list)

    def test_get_attributes(self):
        self.assertIsInstance(self.client.get_attributes(self.device.id), list)

    def test_delete_entity_timeseries(self):
        self.assertIsInstance(
            self.client.delete_entity_timeseries(self.device.id,
                                                 'combination',
                                                 delete_all_data_for_keys=True), bytes)

    def test_save_entity_telemetry(self):
        self.assertEqual(
            self.client.save_entity_telemetry(self.device.id, 'ANY',
                                              body={"ts": 1634712287000,
                                                    "values": {"temperature": 26, "humidity": 87}}), b'')

    def test_save_entity_telemetry_with_ttl(self):
        self.assertEqual(
            self.client.save_entity_telemetry_with_ttl(self.device.id,
                                                       'ANY', body={"temperature": 26, "humidity": 87},
                                                       ttl=100), b'')

    def test_get_timeseries_keys(self):
        self.assertIsInstance(
            self.client.get_timeseries_keys(self.device_profile_id.id),
            list)

    def test_get_attribute_keys_by_scope(self):
        self.assertIsInstance(
            self.client.get_attribute_keys_by_scope(self.device.id,
                                                    'SHARED_SCOPE'), list)

    def test_get_attribute_keys(self):
        self.assertIsInstance(
            self.client.get_attribute_keys(self.device.id), list)

    def test_save_entity_attributes_v2(self):
        self.assertEqual(
            self.client.save_entity_attributes_v2(self.device.id,
                                                  'SHARED_SCOPE', {'shared1': 12}), b'')

    def test_delete_entity_attributes(self):
        self.assertEqual(
            self.client.delete_entity_attributes(self.device.id,
                                                 'SHARED_SCOPE', 'shared1'), b'')

    def test_save_entity_attributes_v1(self):
        self.assertEqual(
            self.client.save_entity_attributes_v1(self.device.id,
                                                  'SHARED_SCOPE', {'shared1': 12}), b'')

    def test_delete_device_attributes(self):
        self.assertEqual(
            self.client.delete_device_attributes(self.device.id,
                                                 'SHARED_SCOPE', 'shared1'), b'')

    def test_save_device_attributes(self):
        self.assertEqual(self.client.save_device_attributes(self.device.id,
                                                            'SHARED_SCOPE', {'shared1': 12}), b'')


class DeviceControllerTests(TBClientCETests):
    device = None
    device_profile_id = None
    customer = None

    @classmethod
    def setUpClass(cls) -> None:
        super(DeviceControllerTests, cls).setUpClass()

        cls.customer = cls.client.get_customers(10, 0).data[0]
        cls.device_profile_id = cls.device_profile_id = cls.client.get_default_device_profile_info().id
        cls.device = Device(name='Test', device_profile_id=cls.device_profile_id)
        cls.device = cls.client.save_device(cls.device)
        cls.cred = cls.client.get_device_credentials_by_device_id(cls.device.id)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_device(cls.device.id)

    def test_get_tenant_devices(self):
        self.assertIsInstance(self.client.get_tenant_devices(10, 0), PageDataDevice)
        sleep(1)

    def test_get_tenant_device(self):
        self.assertIsInstance(self.client.get_tenant_device(self.device.name), Device)

    def test_get_tenant_device_infos(self):
        self.assertIsInstance(self.client.get_tenant_device_infos(10, 0), PageDataDeviceInfo)

    def test_assign_device_to_tenant(self):
        tenant_id = self.client.get_user().tenant_id
        self.assertIsInstance(self.client.assign_device_to_tenant(tenant_id, self.device.id), Device)

    def test_count_by_device_profile_and_empty_ota_package(self):
        self.assertIsInstance(
            self.client.count_by_device_profile_and_empty_ota_package('FIRMWARE', self.device_profile_id.id), int)
        sleep(1)

    def test_get_devices_by_ids(self):
        self.assertIsInstance(
            self.client.get_devices_by_ids([self.device.id.id]), list)

    def test_get_device_types(self):
        self.assertIsInstance(self.client.get_device_types(), list)

    def test_get_device_credentials_by_device_id(self):
        self.assertIsInstance(self.client.get_device_credentials_by_device_id(self.device.id), DeviceCredentials)

    def test_update_device_credentials(self):
        self.assertIsInstance(self.client.update_device_credentials(
            DeviceCredentials(self.cred.id,
                              device_id=self.device.id,
                              credentials_id=self.cred.credentials_id, credentials_type='ACCESS_TOKEN',
                              credentials_value='fffadsfsdgsfddsfdddsdfsf')), DeviceCredentials)

    def test_get_device_by_id(self):
        self.assertIsInstance(self.client.get_device_by_id(self.device.id), Device)

    def test_re_claim_device(self):
        self.assertEqual(self.client.re_claim_device(self.device.name), b'')

    def test_get_customer_devices(self):
        self.assertIsInstance(self.client.get_customer_devices(self.customer.id, 10, 0), PageDataDevice)

    def test_save_device_with_credentials(self):
        test_device = Device(name='Test 1', type='default', device_profile_id=self.device_profile_id)
        test_device = self.client.save_device_with_credentials(
            SaveDeviceWithCredentialsRequest(test_device, DeviceCredentials(credentials_type='ACCESS_TOKEN',
                                                                            credentials_id='sdfsdfsdfsdfsdfsdf')))
        self.assertIsInstance(test_device, Device)
        self.client.delete_device(test_device.id)


class CustomerControllerTests(TBClientCETests):
    test_customer = None

    @classmethod
    def setUpClass(cls) -> None:
        super(CustomerControllerTests, cls).setUpClass()
        cls.test_customer = Customer(title='Test from test', name='Test')
        cls.test_customer = cls.client.save_customer(body=cls.test_customer)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_customer(cls.test_customer.id)

    def test_get_tenant_customer(self):
        self.assertIsInstance(self.client.get_tenant_customer(self.test_customer.title), Customer)

    def test_get_customers(self):
        self.assertIsInstance(self.client.get_customers(10, 0), PageDataCustomer)

    def test_get_customer_title_by_id(self):
        self.assertIsInstance(
            self.client.get_customer_title_by_id(self.test_customer.id), str)

    def test_get_short_customer_info_by_id(self):
        self.assertIsInstance(self.client.get_short_customer_info_by_id(self.test_customer.id), dict)

    def test_get_customer_by_id(self):
        self.assertIsInstance(self.client.get_customer_by_id(self.test_customer.id), Customer)


class DashboardControllerTests(TBClientCETests):
    test_dashboard = None
    customer = None

    @classmethod
    def setUpClass(cls) -> None:
        super(DashboardControllerTests, cls).setUpClass()

        cls.customer = cls.client.get_customers(10, 0).data[0]
        cls.test_dashboard = Dashboard(name='Test from test', title='Test from test')
        cls.client.save_dashboard(body=cls.test_dashboard)
        cls.test_dashboard = list(filter(lambda x: x.name == cls.test_dashboard.name,
                                         cls.client.get_tenant_dashboards(10, 0).data))[0]
        cls.client.set_tenant_home_dashboard_info(
            HomeDashboardInfo(cls.test_dashboard.id, hide_dashboard_toolbar=False))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_dashboard(cls.test_dashboard.id)

    def test_get_tenant_dashboards(self):
        self.assertIsInstance(self.client.get_tenant_dashboards(10, 0), PageDataDashboardInfo)

    def test_get_tenant_home_dashboard_info(self):
        self.assertIsInstance(self.client.get_tenant_home_dashboard_info(), HomeDashboardInfo)

    def test_set_tenant_home_dashboard_info(self):
        self.assertEqual(self.client.set_tenant_home_dashboard_info(
            HomeDashboardInfo(self.test_dashboard.id, hide_dashboard_toolbar=False)), None)

    def test_get_server_time(self):
        self.assertIsInstance(self.client.get_server_time(), int)

    def test_get_max_datapoints_limit(self):
        self.assertIsInstance(self.client.get_max_datapoints_limit(), int)

    def test_get_dashboard_info_by_id(self):
        self.assertIsInstance(
            self.client.get_dashboard_info_by_id(self.test_dashboard.id),
            DashboardInfo)

    def test_get_home_dashboard_info(self):
        self.assertIsInstance(self.client.get_home_dashboard_info(), HomeDashboardInfo)

    def test_get_home_dashboard(self):
        self.assertIsInstance(self.client.get_home_dashboard(), HomeDashboard)

    def test_get_dashboard_by_id(self):
        self.assertIsInstance(
            self.client.get_dashboard_by_id(self.test_dashboard.id), Dashboard)

    def test_get_customer_dashboards(self):
        self.assertIsInstance(self.client.get_customer_dashboards(self.customer.id, 10, 0), PageDataDashboardInfo)


class DeviceProfileControllerTests(TBClientCETests):
    test_device_profile = None

    @classmethod
    def setUpClass(cls) -> None:
        super(DeviceProfileControllerTests, cls).setUpClass()
        cls.test_device_profile = DeviceProfile(name='Test', type='DEFAULT', transport_type='MQTT',
                                                provision_type='ALLOW_CREATE_NEW_DEVICES',
                                                profile_data=DeviceProfileData(
                                                    configuration={"type": "DEFAULT"}, transport_configuration={
                                                        "type": "MQTT",
                                                        "deviceTelemetryTopic": "v1/devices/me/telemetry",
                                                        "deviceAttributesTopic": "v1/devices/me/attributes",
                                                        "transportPayloadTypeConfiguration": {
                                                            "transportPayloadType": "PROTOBUF",
                                                            "deviceTelemetryProtoSchema": "syntax =\"proto3\";\npackage telemetry;\n\nmessage SensorDataReading {\n\n  optional double temperature = 1;\n  optional double humidity = 2;\n  InnerObject innerObject = 3;\n\n  message InnerObject {\n    optional string key1 = 1;\n    optional bool key2 = 2;\n    optional double key3 = 3;\n    optional int32 key4 = 4;\n    optional string key5 = 5;\n  }\n}",
                                                            "deviceAttributesProtoSchema": "syntax =\"proto3\";\npackage attributes;\n\nmessage SensorConfiguration {\n  optional string firmwareVersion = 1;\n  optional string serialNumber = 2;\n}",
                                                            "deviceRpcRequestProtoSchema": "syntax =\"proto3\";\npackage rpc;\n\nmessage RpcRequestMsg {\n  optional string method = 1;\n  optional int32 requestId = 2;\n  optional string params = 3;\n}",
                                                            "deviceRpcResponseProtoSchema": "syntax =\"proto3\";\npackage rpc;\n\nmessage RpcResponseMsg {\n  optional string payload = 1;\n}"
                                                        }
                                                    }))
        cls.test_device_profile = cls.client.save_device_profile(cls.test_device_profile)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_device_profile(cls.test_device_profile.id)

    def test_get_device_profiles(self):
        self.assertIsInstance(self.client.get_device_profiles(10, 0), PageDataDeviceProfile)

    def test_get_device_profile_infos(self):
        self.assertIsInstance(self.client.get_device_profile_infos(10, 0), PageDataDeviceProfileInfo)

    def test_get_default_device_profile_info(self):
        self.assertIsInstance(self.client.get_default_device_profile_info(), DeviceProfileInfo)

    def test_get_device_profile_info_by_id(self):
        self.assertIsInstance(self.client.get_device_profile_info_by_id(self.test_device_profile.id), DeviceProfileInfo)

    def test_get_device_profile_by_id(self):
        self.assertIsInstance(self.client.get_device_profile_by_id(self.test_device_profile.id), DeviceProfile)


class EntityQueryControllerTests(TBClientCETests):
    user = None
    @classmethod
    def setUpClass(cls) -> None:
        super(EntityQueryControllerTests, cls).setUpClass()

        cls.user = cls.client.get_user()

    def test_count_alarms_by_query(self):
        self.assertIsInstance(self.client.count_alarms_by_query(AlarmCountQuery(assignee_id=self.user.id, key_filters=[
            KeyFilter(key={'key': 'temperature', 'type': 'TIME_SERIES'}, value_type='BOOLEAN')],
                                                                                search_propagated_alarms=True,
                                                                                severity_list=['CRITICAL'])), int)

    def test_find_alarms_by_query(self):
        alarm_query = AlarmDataQuery(alarm_fields=[{'key': 'createdTime', 'type': 'ALARM_FIELD'}],
                                     entity_fields=[{'key': 'name', 'type': 'ENTITY_FIELD'}],
                                     entity_filter=EntityFilter(type='entityType', resolve_multiple=True,
                                                                entity_type='DEVICE'), key_filters=[
                KeyFilter(key={'key': 'temperature', 'type': 'TIME_SERIES'}, value_type='BOOLEAN',
                          predicate={"operation": "GREATER",
                                     "value": {
                                         "defaultValue": 0,
                                         "dynamicValue": None
                                     },
                                     "type": "NUMERIC"})],
                                     latest_values=[{'key': 'model', 'type': 'ATTRIBUTE'}],
                                     page_link=AlarmDataPageLink(dynamic=True,
                                                                 search_propagated_alarms=True,
                                                                 severity_list=[
                                                                     'CRITICAL'], page_size=10))
        self.assertIsInstance(self.client.find_alarm_data_by_query(alarm_query), PageDataAlarmData)

    def test_count_entities_by_query(self):
        entity_count_query = EntityCountQuery(entity_filter=EntityFilter(type='entityType', entity_type='DEVICE'),
                                              key_filters=[KeyFilter(key={"type": "ATTRIBUTE",
                                                                          "key": "active"}, value_type='BOOLEAN',
                                                                     predicate={"operation": "EQUAL",
                                                                                "value": {
                                                                                    "defaultValue": True,
                                                                                    "dynamicValue": None
                                                                                },
                                                                                "type": "BOOLEAN"})])
        self.assertIsInstance(self.client.count_entities_by_query(entity_count_query), int)

    def test_find_entity_data_by_query(self):
        entity_data_query = EntityDataQuery(
            entity_filter=EntityFilter(type='entityType', resolve_multiple=True, entity_type='DEVICE'),
            key_filters=[KeyFilter(key={"type": "TIME_SERIES",
                                        "key": "temperature"},
                                   value_type='NUMERIC',
                                   predicate={"operation": "GREATER",
                                              "value": {
                                                  "defaultValue": 0,
                                                  "dynamicValue": {
                                                      "sourceType": "CURRENT_USER",
                                                      "sourceAttribute": "temperatureThreshold",
                                                      "inherit": False
                                                  }
                                              },
                                              "type": "NUMERIC"})],
            entity_fields=[{"type": "ENTITY_FIELD",
                            "key": "name"}],
            latest_values=[{
                "type": "ATTRIBUTE",
                "key": "model"
            }],
            page_link={"page": 0,
                       "pageSize": 10,
                       "sortOrder": {
                           "key": {
                               "key": "name",
                               "type": "ENTITY_FIELD"
                           },
                           "direction": "ASC"
                       }})
        self.assertIsInstance(self.client.find_entity_data_by_query(entity_data_query), PageDataEntityData)

    def test_find_entity_keys_by_query(self):
        entity_data_query = EntityDataQuery(
            entity_filter=EntityFilter(type='entityType', resolve_multiple=True, entity_type='DEVICE'),
            key_filters=[KeyFilter(key={"type": "TIME_SERIES",
                                        "key": "temperature"},
                                   value_type='NUMERIC',
                                   predicate={"operation": "GREATER",
                                              "value": {
                                                  "defaultValue": 0,
                                                  "dynamicValue": {
                                                      "sourceType": "CURRENT_USER",
                                                      "sourceAttribute": "temperatureThreshold",
                                                      "inherit": False
                                                  }
                                              },
                                              "type": "NUMERIC"})],
            entity_fields=[{"type": "ENTITY_FIELD",
                            "key": "name"}],
            latest_values=[{
                "type": "ATTRIBUTE",
                "key": "model"
            }],
            page_link={"page": 0,
                       "pageSize": 10,
                       "sortOrder": {
                           "key": {
                               "key": "name",
                               "type": "ENTITY_FIELD"
                           },
                           "direction": "ASC"
                       }})
        self.assertIsInstance(
            self.client.find_entity_timeseries_and_attributes_keys_by_query(timeseries=True, attributes=True,
                                                                            body=entity_data_query), dict)


class EntityRelationControllerTests(TBClientCETests):
    test_relation = None
    test_asset = None
    test_device = None
    device_profile_id = None
    asset_device_profile_id = None

    @classmethod
    def setUpClass(cls) -> None:
        super(EntityRelationControllerTests, cls).setUpClass()

        cls.device_profile_id = cls.client.get_default_device_profile_info().id

        cls.test_device = Device(name='Test from test 1', device_profile_id=cls.device_profile_id)
        cls.test_device = cls.client.save_device(cls.test_device)

        cls.asset_device_profile_id = cls.client.get_default_asset_profile_info().id
        cls.test_asset = Asset(name="Test Asset", asset_profile_id=cls.asset_device_profile_id)
        cls.test_asset = cls.client.save_asset(body=cls.test_asset)

        cls.test_relation = EntityRelation(_from=cls.test_asset.id, to=cls.test_device.id, type="Contains")
        cls.client.save_relation(cls.test_relation)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_relation(from_id=cls.test_asset.id, to_id=cls.test_device.id, relation_type='Contains')
        cls.client.delete_asset(cls.test_asset.id)
        cls.client.delete_device(cls.test_device.id)

    def test_find_info_by_to(self):
        self.assertIsInstance(self.client.find_info_by_to(self.test_device.id, 'DEVICE'), list)

    def test_find_info_by_from(self):
        self.assertIsInstance(self.client.find_info_by_from(self.test_asset.id), list)

    def test_find_by_to(self):
        self.assertIsInstance(self.client.find_by_to(self.test_device.id, 'Contains'), list)

    def test_find_by_from(self):
        self.assertIsInstance(self.client.find_by_from(self.test_asset.id, 'Contains'), list)

    def test_get_relation(self):
        self.assertIsInstance(self.client.get_relation(self.test_asset.id, 'Contains', self.test_device.id),
                              EntityRelation)


class EntityViewControllerTests(TBClientCETests):
    test_entity_view = None
    device = None
    device_profile_id = None
    customer = None

    @classmethod
    def setUpClass(cls) -> None:
        super(EntityViewControllerTests, cls).setUpClass()

        cls.customer = cls.client.get_customers(10, 0).data[0]

        cls.device_profile_id = cls.client.get_default_device_profile_info().id

        cls.device = Device(name='Test', device_profile_id=cls.device_profile_id)
        cls.device = cls.client.save_device(cls.device)

        cls.test_entity_view = EntityView(name='Test', type='default',
                                          entity_id=cls.device.id,
                                          keys=TelemetryEntityView(timeseries=['temp'],
                                                                   attributes=AttributesEntityView(cs=['fff'],
                                                                                                   sh=['shared'],
                                                                                                   ss=['active'])))
        cls.test_entity_view = cls.client.save_entity_view(cls.test_entity_view)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_entity_view(cls.test_entity_view.id)
        cls.client.delete_device(cls.device.id)

    def test_get_tenant_entity_views(self):
        self.assertIsInstance(self.client.get_tenant_entity_views(10, 0), PageDataEntityView)

    def test_get_tenant_entity_view(self):
        self.assertIsInstance(self.client.get_tenant_entity_view(self.test_entity_view.name), EntityView)

    def test_get_entity_view_types(self):
        self.assertIsInstance(self.client.get_entity_view_types(), list)

    def test_get_entity_view_by_id(self):
        self.assertIsInstance(self.client.get_entity_view_by_id(self.test_entity_view.id), EntityView)

    def test_get_customer_entity_views(self):
        self.assertIsInstance(self.client.get_customer_entity_views(self.customer.id, 10, 0), PageDataEntityView)


class UserControllerTests(TBClientCETests):
    test_user = None
    customer = None
    test_mobile_session = None
    mobile_token = None

    @classmethod
    def setUpClass(cls) -> None:
        super(UserControllerTests, cls).setUpClass()

        cls.customer = cls.client.get_customers(10, 0).data[0]
        cls.test_user = User(name='Test User', email='admin11@gmail.com', authority='TENANT_ADMIN')
        cls.test_user = cls.client.save_user(cls.test_user, send_activation_mail=False)

        cls.mobile_token = "test_token"
        cls.test_mobile_session = cls.client.save_mobile_session(x_mobile_token=cls.mobile_token, body=MobileSessionInfo(fcm_token_timestamp=0))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_user(cls.test_user.id)
        cls.client.remove_mobile_session(cls.mobile_token)

    def test_get_users(self):
        self.assertIsInstance(self.client.get_users(10, 0), PageDataUser)

    def test_is_user_token_access_enabled(self):
        self.assertIsInstance(self.client.is_user_token_access_enabled(), bool)

    def test_get_user_token(self):
        self.assertIsInstance(self.client.get_user_token(self.test_user.id), JwtPair)

    def test_get_activation_link(self):
        self.assertIsInstance(self.client.get_activation_link(self.test_user.id), str)

    def test_get_user_by_id(self):
        self.assertIsInstance(self.client.get_user_by_id(self.test_user.id), User)

    def test_get_customer_users(self):
        self.assertIsInstance(self.client.get_customer_users(self.customer.id, 10, 0), PageDataUser)

    def test_get_mobile_session(self):
        self.assertIsInstance(self.client.get_mobile_session(self.mobile_token), MobileSessionInfo)


class NotificationControllerTests(TBClientCETests):
    notification = None
    template = None
    notification_target = None

    @classmethod
    def setUpClass(cls) -> None:
        super(NotificationControllerTests, cls).setUpClass()

        cls.notification_target = NotificationTarget(name='Test CE',
                                                     configuration=NotificationTargetConfig(type='PLATFORM_USERS',
                                                                                            description='test',
                                                                                            users_filter={
                                                                                                'type': 'ALL_USERS'}))
        cls.notification_target = cls.client.save_notification_target(cls.notification_target)

        cls.template = cls.client.get_notification_templates(10, 0).data[0]

        cls.notification = NotificationRequest(additional_config=NotificationRequestConfig(sending_delay_in_sec=0),
                                               targets=[cls.notification_target.id.id], template_id=cls.template.id,
                                               status='PROCESSING')
        cls.notification = cls.client.create_notification_request(cls.notification)

    def test_get_available_delivery_methods(self):
        self.assertIsInstance(self.client.get_available_delivery_methods(), list)

    def test_get_notification_request_by_id(self):
        self.assertIsInstance(self.client.get_notification_request_by_id(self.notification.id), NotificationRequestInfo)

    def test_get_notification_requests(self):
        self.assertIsInstance(self.client.get_notification_requests(10, 0), PageDataNotificationRequestInfo)

    def test_get_notification_settings(self):
        self.assertIsInstance(self.client.get_notification_settings(), NotificationSettings)

    def test_get_notifications(self):
        self.assertIsInstance(self.client.get_notifications(10, 0), PageDataNotification)

    def test_get_unread_notifications_count(self):
        self.assertIsInstance(self.client.get_unread_notifications_count(), int)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_notification(cls.notification.id)
        cls.client.delete_notification_target_by_id(cls.notification_target.id)


class NotificationTemplateControllerTests(TBClientCETests):
    template = None

    @classmethod
    def setUpClass(cls) -> None:
        super(NotificationTemplateControllerTests, cls).setUpClass()

        cls.template = NotificationTemplate(name='Hello to all my users', configuration=NotificationTemplateConfig(
            delivery_methods_templates={
                'WEB': {'method': 'WEB', 'subject': 'Hello', 'body': 'Hello', 'enabled': True}}),
                                            notification_type='GENERAL')
        cls.template = cls.client.save_notification_template(cls.template)

    def test_get_notification_template_by_id(self):
        self.assertIsInstance(self.client.get_notification_template_by_id(self.template.id), NotificationTemplate)

    def test_get_notification_templates(self):
        self.assertIsInstance(self.client.get_notification_templates(10, 0), PageDataNotificationTemplate)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_notification_template_by_id(cls.template.id)


class NotificationTargetControllerTests(TBClientCETests):
    notification_target = None

    @classmethod
    def setUpClass(cls) -> None:
        super(NotificationTargetControllerTests, cls).setUpClass()

        cls.notification_target = NotificationTarget(name='Test CE',
                                                     configuration=NotificationTargetConfig(type='PLATFORM_USERS',
                                                                                            description='test',
                                                                                            users_filter={
                                                                                                'type': 'ALL_USERS'}))
        cls.notification_target = cls.client.save_notification_target(cls.notification_target)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_notification_target_by_id(cls.notification_target.id)

    def test_get_notification_target_by_id(self):
        self.assertIsInstance(self.client.get_notification_target_by_id(self.notification_target.id),
                              NotificationTarget)

    def test_get_notification_targets_by_ids(self):
        self.assertIsInstance(self.client.get_notification_targets_by_ids([self.notification_target.id.id]), list)

    def test_get_notification_targets_by_supported_notification_type(self):
        self.assertIsInstance(self.client.get_notification_targets_by_supported_notification_type('ALARM', 10, 0),
                              PageDataNotificationTarget)

    def test_get_notification_targets(self):
        self.assertIsInstance(self.client.get_notification_targets(10, 0), PageDataNotificationTarget)


class NotificationRuleControllerTests(TBClientCETests):
    rule = None
    template = None

    @classmethod
    def setUpClass(cls) -> None:
        super(NotificationRuleControllerTests, cls).setUpClass()

        cls.template = NotificationTemplate(name='Hello to all my users', configuration=NotificationTemplateConfig(
            delivery_methods_templates={
                'WEB': {'method': 'WEB', 'subject': 'Hello', 'body': 'Hello', 'enabled': True}}),
                                            notification_type='GENERAL')
        cls.template = cls.client.save_notification_template(cls.template)

        cls.rule = NotificationRule(name='Test', trigger_type='ALARM',
                                    recipients_config={'triggerType': 'ALARM', 'escalationTable': {'0': []}},
                                    trigger_config=NotificationRuleTriggerConfig(trigger_type='ALARM', notify_on=['CREATED']),
                                    template_id=cls.template.id)
        cls.rule = cls.client.save_notification_rule(cls.rule)
        print(cls.rule)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_notification_rule(cls.rule.id)
        cls.client.delete_notification_template_by_id(cls.template.id)

    def test_get_notification_rule_by_id(self):
        self.assertIsInstance(self.client.get_notification_rule_by_id(self.rule.id), NotificationRuleInfo)

    def test_get_notification_rules(self):
        self.assertIsInstance(self.client.get_notification_rules(10, 0), PageDataNotificationRuleInfo)


class TenantControllerTests(TBClientCETests):
    tenant = None
    tenant_profile_id = None

    @classmethod
    def setUpClass(cls) -> None:
        # ThingsBoard REST API URL
        url = TB_URL_CE

        # Default Tenant Administrator credentials
        username = TB_SYSADMIN_USERNAME_CE
        password = TB_SYSADMIN_PASSWORD_CE

        with RestClientCE(url) as cls.client:
            cls.client.login(username, password)

        cls.tenant_profile_id = cls.client.get_default_tenant_profile_info().id
        cls.tenant = Tenant(tenant_profile_id=cls.tenant_profile_id, email='test@test.org', title='Test')
        cls.tenant = cls.client.save_tenant(cls.tenant)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_tenant(cls.tenant.id)

    def test_get_tenant_by_id(self):
        self.assertIsInstance(self.client.get_tenant_by_id(self.tenant.id), Tenant)

    def test_get_tenant_info_by_id(self):
        self.assertIsInstance(self.client.get_tenant_info_by_id(self.tenant.id), TenantInfo)

    def test_get_tenants(self):
        self.assertIsInstance(self.client.get_tenants(10, 0), PageDataTenant)


class TenantProfileControllerTests(TBClientCETests):
    tenant_profile = None

    @classmethod
    def setUpClass(cls) -> None:
        # ThingsBoard REST API URL
        url = TB_URL_CE

        # Default Tenant Administrator credentials
        username = TB_SYSADMIN_USERNAME_CE
        password = TB_SYSADMIN_PASSWORD_CE

        with RestClientCE(url) as cls.client:
            cls.client.login(username, password)

        cls.tenant_profile = TenantProfile(default=False, isolated_tb_rule_engine=False, name='Test')
        cls.tenant_profile = cls.client.save_tenant_profile(cls.tenant_profile)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_tenant_profile(cls.tenant_profile.id)

    def test_get_tenant_profile_by_id(self):
        self.assertIsInstance(self.client.get_tenant_profile_by_id(self.tenant_profile.id), TenantProfile)

    def test_get_tenant_profile_info_by_id(self):
        self.assertIsInstance(self.client.get_tenant_profile_info_by_id(self.tenant_profile.id), EntityInfo)

    def test_get_default_tenant_profile_info(self):
        self.assertIsInstance(self.client.get_default_tenant_profile_info(), EntityInfo)

    def test_get_tenant_profile_infos(self):
        self.assertIsInstance(self.client.get_tenant_profile_infos(10, 0), PageDataEntityInfo)

    def test_get_tenant_profiles_by_ids(self):
        self.assertIsInstance(self.client.get_tenant_profiles_by_ids([self.tenant_profile.id.id]), list)

    def test_get_tenant_profiles(self):
        self.assertIsInstance(self.client.get_tenant_profiles(10, 0), PageDataTenantProfile)


class UiSettingsControllerTests(TBClientCETests):
    def test_get_help_base_url(self):
        self.assertIsInstance(self.client.get_help_base_url(), str)


class UsageInfoControllerTests(TBClientCETests):
    def test_get_tenant_usage_info(self):
        self.assertIsInstance(self.client.get_tenant_usage_info(), UsageInfo)


class WidgetBundleControllerTests(TBClientCETests):
    widget_bundle = None

    @classmethod
    def setUpClass(cls) -> None:
        super(WidgetBundleControllerTests, cls).setUpClass()

        cls.widget_bundle = WidgetsBundle(name='Test', alias='test', title='Test')
        cls.widget_bundle = cls.client.save_widgets_bundle(cls.widget_bundle)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_widgets_bundle(cls.widget_bundle.id)

    def test_get_widgets_bundle_by_id(self):
        self.assertIsInstance(self.client.get_widgets_bundle_by_id(self.widget_bundle.id), WidgetsBundle)

    def test_get_all_widgets_bundles(self):
        self.assertIsInstance(self.client.get_widgets_bundles(), list)

    def test_get_widget_bundles(self):
        self.assertIsInstance(self.client.get_widgets_bundles_v1(10, 0), PageDataWidgetsBundle)


class WidgetTypeControllerTests(TBClientCETests):
    widget_bundle = None
    widget_type = None

    @classmethod
    def setUpClass(cls) -> None:
        super(WidgetTypeControllerTests, cls).setUpClass()

        cls.widget_bundle = WidgetsBundle(name='Test', alias='test', title='Test')
        cls.widget_bundle = cls.client.save_widgets_bundle(cls.widget_bundle)

        cls.widget_type = WidgetType(descriptor={'controllerScript': '', 'dataKeySettingsSchema': {}, 'defaultConfig': {}}, name='Test')
        cls.widget_type = cls.client.save_widget_type(cls.widget_type)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_widget_type(cls.widget_type.id)

    def test_get_widget_type_by_id(self):
        self.assertIsInstance(self.client.get_widget_type_by_id(self.widget_type.id), WidgetTypeDetails)

    def test_get_bundle_widget_types(self):
        self.assertIsInstance(self.client.get_bundle_widget_types(self.widget_bundle.id), list)

    def test_get_bundle_widget_types_infos(self):
        self.assertIsInstance(self.client.get_bundle_widget_types_infos(self.widget_bundle.id, 10, 0),
                              PageDataWidgetTypeInfo)

    @unittest.skip("TB bug")
    def test_get_widget_types(self):
        self.assertIsInstance(self.client.get_widget_type('horizontal_humidity_card'), WidgetType)


class DeviceConnectivityControllerTests(TBClientCETests):
    device_profile_id = None
    device = None

    @classmethod
    def setUpClass(cls) -> None:
        super(DeviceConnectivityControllerTests, cls).setUpClass()

        cls.device_profile_id = cls.client.get_default_device_profile_info().id

        cls.device = Device(name='Test', label='Test', device_profile_id=cls.device_profile_id)
        cls.device = cls.client.save_device(body=cls.device)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_device(cls.device.id)

    def test_get_device_publish_telemetry_commands(self):
        self.assertIsInstance(self.client.get_device_publish_telemetry_commands(self.device.id), dict)

class AdminControllerTests(TBClientCETests):
    @classmethod
    def setUpClass(cls) -> None:
        # ThingsBoard REST API URL
        url = TB_URL_CE

        # Default Tenant Administrator credentials
        username = TB_SYSADMIN_USERNAME_CE
        password = TB_SYSADMIN_PASSWORD_CE

        with RestClientCE(url) as cls.client:
            cls.client.login(username, password)

    def test_get_authorization_url(self):
        self.assertIsInstance(self.client.get_authorization_url(), str)

    def test_get_mail_processing_url(self):
        self.assertIsInstance(self.client.get_mail_processing_url(), str)


class ImageControllerTests(TBClientCETests):
    image_info = None

    @classmethod
    def setUpClass(cls) -> None:
        super(ImageControllerTests, cls).setUpClass()

        cls.image_info = cls.client.upload_image('test', 'data/images/task_done.png')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_image('tenant', 'task_done.png')

    def test_upload_image(self):
        self.assertIsInstance(self.client.upload_image('tenant', 'data/images/task_done.png'), TbResourceInfo)

    def test_update_image(self):
        self.assertIsInstance(self.client.update_image('tenant', 'task_done.png', 'data/images/task_done.png'),
                              TbResourceInfo)

    def test_get_image_info(self):
        self.assertIsInstance(self.client.get_image_info('tenant', 'task_done.png'), TbResourceInfo)

    def test_get_images(self):
        self.assertIsInstance(self.client.get_images(10, 0), PageDataTbResourceInfo)

    def test_download_image(self):
        self.assertIsInstance(self.client.download_image('tenant', 'task_done.png'), str)


class MobileApplicationControllerTests(TBClientCETests):
    @classmethod
    def setUpClass(cls) -> None:
        super(MobileApplicationControllerTests, cls).setUpClass()

    def test_get_mobile_app_deep_link(self):
        self.assertIsInstance(self.client.get_mobile_app_deep_link(), str)

    def test_get_mobile_app_settings(self):
        self.assertIsInstance(self.client.get_mobile_app_settings(), MobileAppSettings)


class QueueStatsControllerTests(TBClientCETests):
    queue_stats = None

    @classmethod
    def setUpClass(cls) -> None:
        super(QueueStatsControllerTests, cls).setUpClass()

        cls.queue_stats = cls.client.get_tenant_queue_stats(10, 0).data[0]
        assert cls.queue_stats is not None

    def test_get_tenant_queue_stats(self):
        s = self.client.get_tenant_queue_stats(10, 0)
        self.assertIsInstance(self.client.get_tenant_queue_stats(10, 0), PageDataQueueStats)

    def test_get_queue_stats_by_id(self):
        self.assertIsInstance(self.client.get_queue_stats_by_id(self.queue_stats.id.id), QueueStats)

    def test_get_queue_stats_by_ids(self):
        self.assertIsInstance(self.client.get_queue_stats_by_ids([self.queue_stats.id.id]), list)


if __name__ == '__main__':
    unittest.main()
