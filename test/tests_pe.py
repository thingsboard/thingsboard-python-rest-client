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

from tb_rest_client.rest_client_pe import *
from tb_rest_client.rest_client_base import *
from tb_rest_client.models.models_pe import *


class TBClientPETests(unittest.TestCase):
    client = None

    @classmethod
    def setUpClass(cls) -> None:
        # ThingsBoard REST API URL
        url = "http://0.0.0.0:8080"

        # Default Tenant Administrator credentials
        username = "tenant@thingsboard.org"
        password = "tenant"

        with RestClientPE(url) as cls.client:
            cls.client.login(username, password)


class DeviceConnectivityControllerTests(TBClientPETests):
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

class AdminControllerTests(TBClientPETests):

    def test_get_mail_processing_url(self):
        self.assertIsInstance(self.client.get_mail_processing_url(), str)


class AlarmCommentControllerTests(TBClientPETests):
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


class TelemetryControllerTests(TBClientPETests):
    device = None
    device_profile_id = None

    @classmethod
    def setUpClass(cls) -> None:
        super(TelemetryControllerTests, cls).setUpClass()

        cls.device_profile_id = cls.client.get_default_device_profile_info().id
        cls.device = Device(name='Test PE', device_profile_id=cls.device_profile_id)
        cls.device = cls.client.save_device(cls.device)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_device(cls.device.id)

    def test_get_latest_timeseries(self):
        self.assertIsInstance(
            self.client.get_latest_timeseries(self.device.id), dict)

    def test_get_timeseries(self):
        self.assertIsInstance(
            self.client.get_timeseries(self.device.id, 'string_read3',
                                       164999693900, 168999693900), dict)

    def test_get_attributes_by_scope(self):
        self.assertIsInstance(
            self.client.get_attributes_by_scope(self.device.id,
                                                'SHARED_SCOPE'), list)

    def test_get_attributes(self):
        self.assertIsInstance(self.client.get_attributes(self.device.id),
                              list)

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
                                                       scope='ANY', ttl=1000, body={"temperature": 26, "humidity": 87}),
            b'')

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


class DeviceControllerTest(TBClientPETests):
    device = None
    device_profile_id = None
    ota_package_request = None

    @classmethod
    def setUpClass(cls) -> None:
        super(DeviceControllerTest, cls).setUpClass()
        cls.device_profile_id = cls.client.get_default_device_profile_info().id

        cls.device = Device(name='Test PE', device_profile_id=cls.device_profile_id)
        cls.device = cls.client.save_device(cls.device)
        cls.cred = cls.client.get_device_credentials_by_device_id(cls.device.id)

        cls.ota_package_request = cls.client.save_ota_package_info(
            SaveOtaPackageInfoRequest(device_profile_id=cls.device_profile_id, title='Test OTA', version=1,
                                      type='FIRMWARE', file_name='tests_pe.py'))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_device(cls.device.id)
        cls.client.delete_ota_package(cls.ota_package_request.id)

    def test_get_user_devices(self):
        devices = self.client.get_user_devices(10, 0)
        self.assertIsInstance(devices, PageDataDevice)

    def test_get_tenant_devices(self):
        self.assertIsInstance(self.client.get_tenant_devices(10, 0), PageDataDevice)
        sleep(1)

    def test_get_tenant_device(self):
        self.assertIsInstance(self.client.get_tenant_device(self.device.name), Device)

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
        self.assertIsInstance(
            self.client.get_device_credentials_by_device_id(self.device.id),
            DeviceCredentials)

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
        customer = self.client.get_customers(10, 0).data[0]
        self.assertIsInstance(
            self.client.get_customer_devices(customer.id, 10, 0),
            PageDataDevice)

    def test_count_by_device_group_and_empty_ota_package(self):
        entity_group = self.client.get_entity_groups_by_type('DEVICE')[0]
        ota_package = self.client.get_ota_packages(10, 0).data[0]
        self.assertIsInstance(
            self.client.count_by_device_group_and_empty_ota_package('FIRMWARE', ota_package.id, entity_group.id), int)

    def test_get_devices_by_entity_group_id(self):
        entity_group = self.client.get_entity_groups_by_type('DEVICE')[0]
        self.assertIsInstance(
            self.client.get_devices_by_entity_group_id(entity_group.id, 10, 0), PageDataDevice)

    def test_save_device_with_credentials(self):
        test_device = Device(name='Test 1', device_profile_id=self.device_profile_id)
        test_device = self.client.save_device_with_credentials(
            SaveDeviceWithCredentialsRequest(test_device, DeviceCredentials(credentials_type='ACCESS_TOKEN',
                                                                            credentials_id='sdfsdfsdfsdfsdfsdf')))
        self.assertIsInstance(test_device, Device)
        self.client.delete_device(test_device.id)
        sleep(0.5)


class AssetControllerTests(TBClientPETests):
    test_asset = None
    test_entity_group = None
    asset_profile_id = None

    @classmethod
    def setUpClass(cls) -> None:
        super(AssetControllerTests, cls).setUpClass()

        cls.test_entity_group = cls.client.get_entity_groups_by_type('ASSET')[0]

        cls.asset_profile_id = cls.client.get_default_asset_profile_info().id
        cls.test_asset = Asset(name="Test Asset", asset_profile_id=cls.asset_profile_id)
        cls.test_asset = cls.client.save_asset(body=cls.test_asset,
                                               entity_group_id=cls.test_entity_group.id)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_asset(cls.test_asset.id)

    def test_get_user_assets(self):
        self.assertIsInstance(self.client.get_user_assets(10, 0), PageDataAsset)

    def test_get_tenant_assets(self):
        self.assertIsInstance(self.client.get_tenant_assets(10, 0), PageDataAsset)

    def test_get_tenant_asset(self):
        self.assertIsInstance(self.client.get_tenant_asset(self.test_asset.name), Asset)

    def test_get_assets_by_entity_group_id(self):
        entity_group = self.client.get_entity_groups_by_type('ASSET')[0]
        self.assertIsInstance(
            self.client.get_assets_by_entity_group_id(entity_group.id, 10, 0), PageDataAsset)

    def test_get_customer_assets(self):
        customer = self.client.get_customers(10, 0).data[0]
        self.assertIsInstance(self.client.get_customer_assets(customer.id, 10, 0), PageDataAsset)

    def test_get_assets_by_ids(self):
        self.assertIsInstance(self.client.get_assets_by_ids([self.test_asset.id.id]), list)

    def test_get_asset_types(self):
        self.assertIsInstance(self.client.get_asset_types(), list)

    def test_get_asset_by_id(self):
        self.assertIsInstance(self.client.get_asset_by_id(self.test_asset.id), Asset)


class AssetProfileControllerTests(TBClientPETests):
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


class AuditLogControllerTests(TBClientPETests):
    customer = None
    device = None
    user = None

    @classmethod
    def setUpClass(cls) -> None:
        super(AuditLogControllerTests, cls).setUpClass()

        cls.customer = cls.client.get_customers(10, 0).data[0]
        cls.user = cls.client.get_user()

    def test_get_audit_logs(self):
        self.assertIsInstance(self.client.get_audit_logs(10, 0), PageDataAuditLog)

    def test_get_audit_logs_by_customer_id(self):
        self.assertIsInstance(self.client.get_audit_logs_by_customer_id(self.customer.id, 10, 0), PageDataAuditLog)

    def test_get_audit_logs_by_entity_id(self):
        self.assertIsInstance(self.client.get_audit_logs_by_entity_id(EntityId(self.customer.id, 'CUSTOMER'), 10, 0),
                              PageDataAuditLog)

    def test_get_audit_logs_by_user_id(self):
        self.assertIsInstance(self.client.get_audit_logs_by_user_id(self.user.id, 10, 0), PageDataAuditLog)


class EntityGroupControllerTests(TBClientPETests):
    test_entity_group: EntityGroup = None
    asset_profile_id = None
    test_asset = None
    customer = None
    user = None
    user_group = None
    role = None

    @classmethod
    def setUpClass(cls) -> None:
        super(EntityGroupControllerTests, cls).setUpClass()

        cls.user = cls.client.get_user()
        cls.customer = cls.client.get_customers(10, 0).data[0]
        cls.user_group = cls.client.get_entity_groups_by_owner_and_type('TENANT', cls.user.owner_id, 'USER')[-1]

        cls.role = Role(name='Test PE EGC', type='GROUP', permissions=['ALL'])
        cls.role = cls.client.save_role(cls.role)

        cls.test_entity_group = EntityGroup(name='Test 4', type='ASSET')
        cls.test_entity_group = cls.client.save_entity_group(cls.test_entity_group)

        cls.asset_profile_id = cls.client.get_default_asset_profile_info().id
        cls.test_asset = Asset(name="Test Asset", asset_profile_id=cls.asset_profile_id)
        cls.test_asset = cls.client.save_asset(body=cls.test_asset,
                                               entity_group_id=cls.test_entity_group.id)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_asset(cls.test_asset.id)
        cls.client.delete_entity_group(cls.test_entity_group.id)
        cls.client.delete_role(cls.role.id)

    def test_get_entity_groups_by_type(self):
        self.assertIsInstance(self.client.get_entity_groups_by_type('DEVICE'), list)

    def test_get_entity_group_by_owner_and_name_and_type(self):
        self.assertIsInstance(
            self.client.get_entity_group_by_owner_and_name_and_type(self.customer.id, 'ASSET', 'All'),
            EntityGroupInfo)

    def test_get_entity_groups_by_owner_and_type(self):
        customer = self.client.get_customers(10, 0).data[0]
        self.assertIsInstance(self.client.get_entity_groups_by_owner_and_type('CUSTOMER', customer.id, 'ASSET'), list)

    def test_get_entity_groups_for_entity(self):
        self.assertIsInstance(self.client.get_entity_groups_for_entity(self.test_asset.id), list)

    def test_get_entity_groups_by_ids(self):
        self.assertIsInstance(self.client.get_entity_groups_by_ids([self.test_entity_group.id.id]), list)

    def test_make_entity_group_public(self):
        self.assertEqual(self.client.make_entity_group_public(self.test_entity_group.id), None)

    def test_make_entity_group_private(self):
        self.client.make_entity_group_public(self.test_entity_group.id)
        self.assertEqual(
            self.client.make_entity_group_private(self.test_entity_group.id), None)

    def test_remove_entities_from_entity_group(self):
        self.client.add_entities_to_entity_group(self.test_entity_group.id,
                                                 [self.test_asset.id.id])
        self.assertEqual(self.client.remove_entities_from_entity_group(
            self.test_entity_group.id, [self.test_asset.id.id]),
            None)

    def test_add_entities_to_entity_group(self):
        self.assertEqual(
            self.client.add_entities_to_entity_group(self.test_entity_group.id,
                                                     [self.test_asset.id.id]), None)

    def test_get_entity_group_by_id(self):
        self.assertIsInstance(
            self.client.get_entity_group_by_id(self.test_entity_group.id),
            EntityGroupInfo)

    def test_get_owners(self):
        self.assertIsInstance(self.client.get_owners(1, 0), PageDataContactBasedobject)

    def test_share_entity_group_to_child_owner_user_group(self):
        self.assertEqual(
            self.client.share_entity_group_to_child_owner_user_group(self.test_entity_group.id, self.user_group.id,
                                                                     self.role.id), None)

    def test_get_entities(self):
        self.assertIsInstance(self.client.get_entities(self.test_entity_group.id, 10, 0),
                              PageDataShortEntityView)

    def test_get_group_entity(self):
        self.assertIsInstance(self.client.get_group_entity(self.test_entity_group.id, self.test_asset.id),
                              ShortEntityView)


class CustomerControllerTests(TBClientPETests):
    test_customer = None

    @classmethod
    def setUpClass(cls) -> None:
        super(CustomerControllerTests, cls).setUpClass()
        cls.test_customer = Customer(name='Test from test', title='Test from test')
        cls.test_customer = cls.client.save_customer(body=cls.test_customer)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_customer(cls.test_customer.id)

    def test_get_user_customers(self):
        self.assertIsInstance(self.client.get_user_customers(10, 0), PageDataCustomer)

    def test_get_tenant_customer(self):
        self.assertIsInstance(self.client.get_tenant_customer('Test from test'), Customer)

    def test_get_customers_by_entity_group_id(self):
        entity_group = self.client.get_entity_groups_by_type('CUSTOMER')[0]
        self.assertIsInstance(self.client.get_customers_by_entity_group_id(entity_group.id, 10, 0), PageDataCustomer)

    def test_get_customers(self):
        self.assertIsInstance(self.client.get_customers(10, 0), PageDataCustomer)

    def test_get_customer_title_by_id(self):
        self.assertIsInstance(
            self.client.get_customer_title_by_id(self.test_customer.id), str)

    def test_get_short_customer_info_by_id(self):
        self.assertIsInstance(self.client.get_short_customer_info_by_id(self.test_customer.id), dict)

    def test_get_customer_by_id(self):
        self.assertIsInstance(self.client.get_customer_by_id(self.test_customer.id), Customer)


class DashboardControllerTests(TBClientPETests):
    test_dashboard = None

    @classmethod
    def setUpClass(cls) -> None:
        super(DashboardControllerTests, cls).setUpClass()

        cls.test_dashboard = Dashboard(name='Test PE', title='Test PE')
        cls.client.save_dashboard(body=cls.test_dashboard)
        cls.test_dashboard = list(filter(lambda x: x.name == cls.test_dashboard.name,
                                         cls.client.get_user_dashboards(100, 0).data))[0]
        cls.client.set_tenant_home_dashboard_info(
            HomeDashboardInfo(cls.test_dashboard.id, hide_dashboard_toolbar=False))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_dashboard(cls.test_dashboard.id)

    def test_get_user_dashboards(self):
        self.assertIsInstance(self.client.get_user_dashboards(10, 0), PageDataDashboardInfo)

    def test_get_tenant_dashboards(self):
        self.assertIsInstance(self.client.get_tenant_dashboards(10, 0), PageDataDashboardInfo)

    def test_get_tenant_home_dashboard_info(self):
        self.assertIsInstance(self.client.get_tenant_home_dashboard_info(), HomeDashboardInfo)

    def test_set_tenant_home_dashboard_info(self):
        self.assertEqual(self.client.set_tenant_home_dashboard_info(
            HomeDashboardInfo(self.test_dashboard.id, hide_dashboard_toolbar=False)), None)

    @unittest.skip('unstable')
    def test_export_group_dashboards(self):
        entity_group = self.client.get_entity_groups_by_type('DASHBOARD')[0]
        dashboards = None
        for _ in range(3):
            try:
                dashboards = self.client.export_group_dashboards(entity_group.id, 1)
            except Exception:
                sleep(60)
            else:
                break

        self.assertIsInstance(dashboards, list)

    def test_get_dashboards_by_entity_group_id(self):
        entity_group = self.client.get_entity_groups_by_type('DASHBOARD')[0]
        self.assertIsInstance(self.client.get_dashboards_by_entity_group_id(entity_group.id, 10, 0),
                              PageDataDashboardInfo)

    def test_get_dashboards_by_ids(self):
        self.assertIsInstance(self.client.get_dashboards_by_ids([self.test_dashboard.id.id]), list)

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


class ConverterControllerTests(TBClientPETests):
    test_converter = None

    @classmethod
    def setUpClass(cls) -> None:
        super(ConverterControllerTests, cls).setUpClass()
        cls.test_converter = Converter(name='Test PE', type='UPLINK', configuration={
            "decoder": "// Decode an uplink message from a buffer\n// payload - array of bytes\n// metadata - key/value object\n\n/** Decoder **/\n\n// decode payload to string\nvar payloadStr = decodeToString(payload);\n\n// decode payload to JSON\n// var data = decodeToJson(payload);\n\nvar deviceName = 'Device A';\nvar deviceType = 'thermostat';\nvar customerName = 'customer';\nvar groupName = 'thermostat devices';\n// use assetName and assetType instead of deviceName and deviceType\n// to automatically create assets instead of devices.\n// var assetName = 'Asset A';\n// var assetType = 'building';\n\n// Result object with device/asset attributes/telemetry data\nvar result = {\n// Use deviceName and deviceType or assetName and assetType, but not both.\n   deviceName: deviceName,\n   deviceType: deviceType,\n// assetName: assetName,\n// assetType: assetType,\n   customerName: customerName,\n   groupName: groupName,\n   attributes: {\n       model: 'Model A',\n       serialNumber: 'SN111',\n       integrationName: metadata['integrationName']\n   },\n   telemetry: {\n       temperature: 42,\n       humidity: 80,\n       rawData: payloadStr\n   }\n};\n\n/** Helper functions **/\n\nfunction decodeToString(payload) {\n   return String.fromCharCode.apply(String, payload);\n}\n\nfunction decodeToJson(payload) {\n   // covert payload to string.\n   var str = decodeToString(payload);\n\n   // parse string to JSON\n   var data = JSON.parse(str);\n   return data;\n}\n\nreturn result;",
            "encoder": None
        })
        cls.test_converter = cls.client.save_converter(cls.test_converter)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_converter(cls.test_converter.id)

    def test_get_converters(self):
        self.assertIsInstance(self.client.get_converters(10, 0), PageDataConverter)

    def test_get_converters_by_ids(self):
        self.assertIsInstance(self.client.get_converters_by_ids([self.test_converter.id.id]), list)

    def test_get_latest_converter_debug_input(self):
        self.assertIsInstance(self.client.get_latest_converter_debug_input(
            self.test_converter.id), bytes)

    def test_get_converter_by_id(self):
        self.assertIsInstance(self.client.get_converter_by_id(self.test_converter.id), Converter)

    def test_test_up_link_converter(self):
        self.assertIsInstance(self.client.test_up_link_converter({
            "metadata": {
            },
            "payload": "ewogICAgImRhdGEiOiAiZGF0YSIKfQ==",
            "decoder": "// Decode an uplink message from a buffer\n// payload - array of bytes\n// metadata - key/value object\n\n/** Decoder **/\n\n// decode payload to string\nvar payloadStr = decodeToString(payload);\n\n// decode payload to JSON\n// var data = decodeToJson(payload);\n\nvar deviceName = 'Device A';\nvar deviceType = 'thermostat';\nvar customerName = 'customer';\nvar groupName = 'thermostat devices';\n// use assetName and assetType instead of deviceName and deviceType\n// to automatically create assets instead of devices.\n// var assetName = 'Asset A';\n// var assetType = 'building';\n\n// Result object with device/asset attributes/telemetry data\nvar result = {\n// Use deviceName and deviceType or assetName and assetType, but not both.\n   deviceName: deviceName,\n   deviceType: deviceType,\n// assetName: assetName,\n// assetType: assetType,\n   customerName: customerName,\n   groupName: groupName,\n   attributes: {\n       model: 'Model A',\n       serialNumber: 'SN111',\n       integrationName: metadata['integrationName']\n   },\n   telemetry: {\n       temperature: 42,\n       humidity: 80,\n       rawData: payloadStr\n   }\n};\n\n/** Helper functions **/\n\nfunction decodeToString(payload) {\n   return String.fromCharCode.apply(String, payload);\n}\n\nfunction decodeToJson(payload) {\n   // covert payload to string.\n   var str = decodeToString(payload);\n\n   // parse string to JSON\n   var data = JSON.parse(str);\n   return data;\n}\n\nreturn result;"
        }), dict)

    def test_test_down_link_converter(self):
        self.assertIsInstance(self.client.test_down_link_converter({
            "metadata": {
                "data": "40"
            },
            "msg": "{\n    \"temp\": 42,\n    \"humidity\": 77\n}",
            "msgType": "POST_TELEMETRY_REQUEST",
            "integrationMetadata": {
                "integrationName": "Integration"
            },
            "encoder": "// Encode downlink data from incoming Rule Engine message\n\n// msg - JSON message payload downlink message json\n// msgType - type of message, for ex. 'ATTRIBUTES_UPDATED', 'POST_TELEMETRY_REQUEST', etc.\n// metadata - list of key-value pairs with additional data about the message\n// integrationMetadata - list of key-value pairs with additional data defined in Integration executing this converter\n\n/** Encoder **/\n\nvar data = {};\n\n// Process data from incoming message and metadata\n\ndata.tempValue = msg.temp;\ndata.humValue = msg.humidity;\n\ndata.devSerialNumber = metadata['ss_serialNumber'];\n\n// Result object with encoded downlink payload\nvar result = {\n\n    // downlink data content type: JSON, TEXT or BINARY (base64 format)\n    contentType: \"JSON\",\n\n    // downlink data\n    data: JSON.stringify(data),\n\n    // Optional metadata object presented in key/value format\n    metadata: {\n            topic: metadata['deviceType']+'/'+metadata['deviceName']+'/upload'\n    }\n\n};\n\nreturn result;"
        }), dict)


class IntegrationControllerTests(TBClientPETests):
    test_converter = None
    integration = None

    @classmethod
    def setUpClass(cls) -> None:
        super(IntegrationControllerTests, cls).setUpClass()

        cls.test_converter = Converter(name='Test PE', type='UPLINK', configuration={
            "decoder": "// Decode an uplink message from a buffer\n// payload - array of bytes\n// metadata - key/value object\n\n/** Decoder **/\n\n// decode payload to string\nvar payloadStr = decodeToString(payload);\n\n// decode payload to JSON\n// var data = decodeToJson(payload);\n\nvar deviceName = 'Device A';\nvar deviceType = 'thermostat';\nvar customerName = 'customer';\nvar groupName = 'thermostat devices';\n// use assetName and assetType instead of deviceName and deviceType\n// to automatically create assets instead of devices.\n// var assetName = 'Asset A';\n// var assetType = 'building';\n\n// Result object with device/asset attributes/telemetry data\nvar result = {\n// Use deviceName and deviceType or assetName and assetType, but not both.\n   deviceName: deviceName,\n   deviceType: deviceType,\n// assetName: assetName,\n// assetType: assetType,\n   customerName: customerName,\n   groupName: groupName,\n   attributes: {\n       model: 'Model A',\n       serialNumber: 'SN111',\n       integrationName: metadata['integrationName']\n   },\n   telemetry: {\n       temperature: 42,\n       humidity: 80,\n       rawData: payloadStr\n   }\n};\n\n/** Helper functions **/\n\nfunction decodeToString(payload) {\n   return String.fromCharCode.apply(String, payload);\n}\n\nfunction decodeToJson(payload) {\n   // covert payload to string.\n   var str = decodeToString(payload);\n\n   // parse string to JSON\n   var data = JSON.parse(str);\n   return data;\n}\n\nreturn result;",
            "encoder": None
        })
        cls.test_converter = cls.client.save_converter(cls.test_converter)
        cls.integration = Integration(name='HTTP Test', type='HTTP', enabled=True, debug_mode=True,
                                      allow_create_devices_or_assets=True, default_converter_id=cls.test_converter.id,
                                      secret='6uy2p5s0aspoqb6glhva', routing_key='ea150eb3-df46-1321-826c-9d924ed5d88a',
                                      configuration={'baseUrl': 'https://thingsboard.cloud', 'enableSecurity': False})
        cls.integration = cls.client.save_integration(cls.integration)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_integration(cls.integration.id)
        cls.client.delete_converter(cls.test_converter.id)

    def test_get_integration_by_id(self):
        self.assertIsInstance(self.client.get_integration_by_id(self.integration.id), Integration)

    def test_get_integration_by_routing_key(self):
        self.assertIsInstance(self.client.get_integration_by_routing_key(self.integration.routing_key), Integration)

    def test_get_integration_infos(self):
        self.assertIsInstance(self.client.get_integration_infos(10, 0, False), PageDataIntegrationInfo)

    def test_get_integrations_by_ids(self):
        self.assertIsInstance(self.client.get_integrations_by_ids([self.integration.id.id]), list)

    def test_get_integrations(self):
        self.assertIsInstance(self.client.get_integrations(10, 0, False), PageDataIntegration)


class AlarmControllerTests(TBClientPETests):
    test_alarm = None
    device = None
    device_profile_id = None

    @classmethod
    def setUpClass(cls) -> None:
        super(AlarmControllerTests, cls).setUpClass()

        cls.device_profile_id = cls.client.get_default_device_profile_info().id
        cls.device = Device(name='Test PE 1', device_profile_id=cls.device_profile_id)
        cls.device = cls.client.save_device(cls.device)

        cls.test_alarm = Alarm(name='Test PE', type='default',
                               originator=cls.device.id,
                               severity='CRITICAL', status='CLEARED_UNACK', acknowledged=False, cleared=False)
        cls.test_alarm = cls.client.save_alarm(cls.test_alarm)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_alarm(cls.test_alarm.id)
        cls.client.delete_device(cls.device.id)

    def test_get_all_alarms(self):
        self.assertIsInstance(self.client.get_all_alarms(10, 0), PageDataAlarmInfo)

    def test_get_alarm_info_by_id(self):
        self.assertIsInstance(self.client.get_alarm_info_by_id(self.test_alarm.id), AlarmInfo)

    def test_get_highest_alarm_severity(self):
        self.assertIsInstance(
            self.client.get_highest_alarm_severity(self.device.id), str)

    def test_get_alarms(self):
        self.assertIsInstance(self.client.get_alarms(self.device.id, 10, 0),
                              PageDataAlarmInfo)

    def test_clear_alarm(self):
        self.assertIsInstance(self.client.clear_alarm(self.test_alarm.id), AlarmInfo)

    def test_ack_alarm(self):
        self.assertIsInstance(self.client.ack_alarm(self.test_alarm.id), AlarmInfo)

    def test_get_alarm_by_id(self):
        self.assertIsInstance(self.client.get_alarm_by_id(self.test_alarm.id), Alarm)

    def test_get_alarm_types_using_get(self):
        self.assertIsInstance(self.client.get_alarm_types(10, 0), PageDataEntitySubtype)


class DeviceProfileControllerTests(TBClientPETests):
    test_device_profile = None

    @classmethod
    def setUpClass(cls) -> None:
        super(DeviceProfileControllerTests, cls).setUpClass()
        cls.test_device_profile = DeviceProfile(name='Test PE 1', type='DEFAULT', transport_type='MQTT',
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

    def test_get_device_profiles_by_ids(self):
        self.assertIsInstance(self.client.get_device_profiles_by_ids([self.test_device_profile.id.id]), list)

    def test_get_default_device_profile_info(self):
        self.assertIsInstance(self.client.get_default_device_profile_info(), DeviceProfileInfo)

    def test_get_device_profile_info_by_id(self):
        self.assertIsInstance(self.client.get_device_profile_info_by_id(self.test_device_profile.id), DeviceProfileInfo)

    def test_get_device_profile_by_id(self):
        self.assertIsInstance(self.client.get_device_profile_by_id(self.test_device_profile.id), DeviceProfile)


class EntityRelationControllerTests(TBClientPETests):
    test_relation = None
    test_asset = None
    test_device = None
    device_profile_id = None
    entity_group = None
    asset_profile_id = None

    @classmethod
    def setUpClass(cls) -> None:
        super(EntityRelationControllerTests, cls).setUpClass()

        cls.device_profile_id = cls.client.get_default_device_profile_info().id

        cls.test_device = Device(name='Test from test 1', device_profile_id=cls.device_profile_id)
        cls.test_device = cls.client.save_device(cls.test_device)

        cls.entity_group = cls.client.get_entity_groups_by_type('ASSET')[0]
        cls.asset_profile_id = cls.client.get_default_asset_profile_info().id
        cls.test_asset = Asset(name="Test Asset", asset_profile_id=cls.asset_profile_id)
        cls.test_asset = cls.client.save_asset(body=cls.test_asset,
                                               entity_group_id=cls.entity_group.id)

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


class EntityViewControllerTests(TBClientPETests):
    test_entity_view = None
    device = None
    device_profile_id = None

    @classmethod
    def setUpClass(cls) -> None:
        super(EntityViewControllerTests, cls).setUpClass()

        cls.device_profile_id = cls.client.get_default_device_profile_info().id
        cls.device = Device(name='Test PE 1', device_profile_id=cls.device_profile_id)
        cls.device = cls.client.save_device(cls.device)

        cls.test_entity_view = EntityView(name='Test PE', type='default',
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

    def test_get_user_entity_views(self):
        self.assertIsInstance(self.client.get_user_entity_views(10, 0), PageDataEntityView)

    def test_get_tenant_entity_views(self):
        self.assertIsInstance(self.client.get_tenant_entity_views(10, 0), PageDataEntityView)

    def test_get_tenant_entity_view(self):
        self.assertIsInstance(self.client.get_tenant_entity_view(self.test_entity_view.name), EntityView)

    def test_get_entity_views_by_ids(self):
        self.assertIsInstance(self.client.get_entity_views_by_ids([self.test_entity_view.id.id]), list)

    def test_get_entity_view_types(self):
        self.assertIsInstance(self.client.get_entity_view_types(), list)

    def test_get_entity_view_by_id(self):
        self.assertIsInstance(self.client.get_entity_view_by_id(self.test_entity_view.id), EntityView)

    def test_get_entity_views_by_entity_group_id(self):
        entity_group = self.client.get_entity_groups_by_type('ENTITY_VIEW')[0]
        self.assertIsInstance(self.client.get_entity_views_by_entity_group_id(entity_group.id, 10, 0),
                              PageDataEntityView)

    def test_get_customer_entity_views(self):
        customer = self.client.get_customers(10, 0).data[0]
        self.assertIsInstance(
            self.client.get_customer_entity_views(customer.id, 10,
                                                  0), PageDataEntityView)


class RoleControllerTests(TBClientPETests):
    test_role = None

    @classmethod
    def setUpClass(cls) -> None:
        super(RoleControllerTests, cls).setUpClass()
        cls.test_role = Role(name='Test PE 111', type='GENERIC', permissions={
            "ALL": [
                "READ",
                "RPC_CALL",
                "READ_CREDENTIALS",
                "READ_ATTRIBUTES",
                "READ_TELEMETRY"
            ],
            "DEVICE": [
                "ALL"
            ],
            "PROFILE": [
                "ALL"
            ]
        })
        cls.test_role = cls.client.save_role(cls.test_role)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_role(cls.test_role.id)

    def test_get_roles_by_ids(self):
        self.assertIsInstance(self.client.get_roles_by_ids([self.test_role.id.id]), list)

    def test_get_roles(self):
        self.assertIsInstance(self.client.get_roles(10, 0), PageDataRole)

    def test_get_role_by_id(self):
        self.assertIsInstance(self.client.get_role_by_id(self.test_role.id), Role)


class UserPermissionsControllerTests(TBClientPETests):
    def test_get_allowed_permissions(self):
        self.assertIsInstance(self.client.get_allowed_permissions(), AllowedPermissionsInfo)


class UiSettingsControllerTests(TBClientPETests):
    def test_get_help_base_url(self):
        self.assertIsInstance(self.client.get_help_base_url(), str)


class UsageInfoControllerTests(TBClientPETests):
    def test_get_tenant_usage_info(self):
        self.assertIsInstance(self.client.get_tenant_usage_info(), UsageInfo)


class WidgetBundleControllerTests(TBClientPETests):
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


class WidgetTypeControllerTests(TBClientPETests):
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


class NotificationControllerTests(TBClientPETests):
    notification = None
    template = None
    notification_target = None

    @classmethod
    def setUpClass(cls) -> None:
        super(NotificationControllerTests, cls).setUpClass()

        cls.notification_target = NotificationTarget(name='Test PE',
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

    def test_get_user_notification_settings(self):
        self.assertIsInstance(self.client.get_user_notification_settings(), UserNotificationSettings)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_notification(cls.notification.id)
        cls.client.delete_notification_target_by_id(cls.notification_target.id)


class NotificationTemplateControllerTests(TBClientPETests):
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


class NotificationTargetControllerTests(TBClientPETests):
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


class NotificationRuleControllerTests(TBClientPETests):
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
                                    trigger_config=NotificationRuleTriggerConfig(trigger_type='ALARM',
                                                                                 notify_on=['CREATED']),
                                    template_id=cls.template.id)
        cls.rule = cls.client.save_notification_rule(cls.rule)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_notification_rule(cls.rule.id)
        cls.client.delete_notification_template_by_id(cls.template.id)

    def test_get_notification_rule_by_id(self):
        self.assertIsInstance(self.client.get_notification_rule_by_id(self.rule.id), NotificationRuleInfo)

    def test_get_notification_rules(self):
        self.assertIsInstance(self.client.get_notification_rules(10, 0), PageDataNotificationRuleInfo)


class ImageControllerTests(TBClientPETests):
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


class QueueStatsControllerTests(TBClientPETests):
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


class TranslationControllerTests(TBClientPETests):
    @classmethod
    def setUpClass(cls) -> None:
        super(TranslationControllerTests, cls).setUpClass()

    def test_download_full_translation(self):
        self.assertIsInstance(self.client.download_full_translation(locale_code='en_US'), str)

    def test_get_available_java_locales(self):
        self.assertIsInstance(self.client.get_available_java_locales(), dict)

    def test_get_available_locales(self):
        self.assertIsInstance(self.client.get_available_locales(), dict)

    def test_get_translation_infos(self):
        self.assertIsInstance(self.client.get_translation_infos(), list)

    def test_get_translation_for_basic_edit(self):
        self.assertIsInstance(self.client.get_translation_for_basic_edit(locale_code='en_US'), dict)


if __name__ == '__main__':
    unittest.main()
