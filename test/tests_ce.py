import unittest

from tb_rest_client.rest_client_ce import *
from tb_rest_client.models.models_ce import *


class TBClientCETests(unittest.TestCase):
    client = None

    @classmethod
    def setUpClass(cls) -> None:
        # ThingsBoard REST API URL
        url = "https://demo.thingsboard.io"

        # Default Tenant Administrator credentials
        username = "***"
        password = "***"

        with RestClientCE(url) as cls.client:
            cls.client.login(username, password)


class AlarmControllerTests(TBClientCETests):
    test_alarm = None
    device = None
    device_profile_id = None

    @classmethod
    def setUpClass(cls) -> None:
        super(AlarmControllerTests, cls).setUpClass()

        cls.device_profile_id = list(filter(lambda x: x.type == 'DEFAULT', cls.client.get_device_profiles(10, 0).data))[
            0]

        cls.device = Device(name='Test', type='default',
                            device_profile_id=cls.device_profile_id.id)
        cls.device = cls.client.save_device(cls.device)

        cls.test_alarm = Alarm(name='Test', type='default',
                               originator=cls.device.id,
                               severity='CRITICAL', status='CLEARED_UNACK')
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
        self.assertIsInstance(self.client.get_highest_alarm_severity(self.device.id), str)

    def test_get_alarms(self):
        self.assertIsInstance(self.client.get_alarms(self.device.id, 10, 0), PageDataAlarmInfo)

    def test_clear_alarm(self):
        self.assertEqual(self.client.clear_alarm(self.test_alarm.id), None)

    def test_ack_alarm(self):
        self.assertEqual(self.client.ack_alarm(self.test_alarm.id), None)

    def test_get_alarm_by_id(self):
        self.assertIsInstance(self.client.get_alarm_by_id(self.test_alarm.id), Alarm)


class AssetControllerTests(TBClientCETests):
    test_asset = None

    @classmethod
    def setUpClass(cls) -> None:
        super(AssetControllerTests, cls).setUpClass()

        cls.test_asset = Asset(name="Test Asset", type="building")
        cls.test_asset = cls.client.save_asset(body=cls.test_asset)

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
        customer = self.client.get_customers(10, 0).data[0]
        self.assertIsInstance(self.client.get_customer_assets(customer.id, 10, 0), PageDataAsset)

    def test_get_customer_asset_infos(self):
        customer = self.client.get_customers(10, 0).data[0]
        self.assertIsInstance(self.client.get_customer_asset_infos(customer.id, 10, 0), PageDataAssetInfo)

    def test_get_assets_by_ids(self):
        self.assertIsInstance(self.client.get_assets_by_ids([self.test_asset.id.id]), list)

    def test_get_asset_types(self):
        self.assertIsInstance(self.client.get_asset_types(), list)

    def test_get_asset_info_by_id(self):
        self.assertIsInstance(self.client.get_asset_info_by_id(self.test_asset.id), AssetInfo)

    def test_get_asset_by_id(self):
        self.assertIsInstance(self.client.get_asset_by_id(self.test_asset.id), Asset)


class TelemetryControllerTests(TBClientCETests):
    device = None
    device_profile_id = None

    @classmethod
    def setUpClass(cls) -> None:
        super(TelemetryControllerTests, cls).setUpClass()
        cls.device_profile_id = list(filter(lambda x: x.type == 'DEFAULT', cls.client.get_device_profiles(10, 0).data))[
            0]

        cls.device = Device(name='Test', type='default',
                            device_profile_id=cls.device_profile_id.id)
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

    @classmethod
    def setUpClass(cls) -> None:
        super(DeviceControllerTests, cls).setUpClass()
        cls.device_profile_id = list(filter(lambda x: x.type == 'DEFAULT', cls.client.get_device_profiles(10, 0).data))[
            0]

        cls.device = Device(name='Test', type='default',
                            device_profile_id=cls.device_profile_id.id)
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

    def test_save_device_with_credentials(self):
        test_device = Device(name='Test 1', type='default', device_profile_id=self.device_profile_id.id)
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

    @classmethod
    def setUpClass(cls) -> None:
        super(DashboardControllerTests, cls).setUpClass()
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
        customer = self.client.get_customers(10, 0).data[0]
        self.assertIsInstance(self.client.get_customer_dashboards(customer.id, 10, 0), PageDataDashboardInfo)


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


class EntityRelationControllerTests(TBClientCETests):
    test_relation = None
    test_asset = None
    test_device = None
    device_profile_id = None

    @classmethod
    def setUpClass(cls) -> None:
        super(EntityRelationControllerTests, cls).setUpClass()

        cls.device_profile_id = list(filter(lambda x: x.type == 'DEFAULT', cls.client.get_device_profiles(10, 0).data))[
            0]

        cls.test_device = Device(name='Test from test', type='default',
                                 device_profile_id=cls.device_profile_id.id)
        cls.test_device = cls.client.save_device(cls.test_device)

        cls.test_asset = Asset(name="Test Asset", type="building")
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

    @classmethod
    def setUpClass(cls) -> None:
        super(EntityViewControllerTests, cls).setUpClass()
        cls.device_profile_id = list(filter(lambda x: x.type == 'DEFAULT', cls.client.get_device_profiles(10, 0).data))[
            0]

        cls.device = Device(name='Test', type='default',
                            device_profile_id=cls.device_profile_id.id)
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
        customer = self.client.get_customers(10, 0).data[0]
        self.assertIsInstance(
            self.client.get_customer_entity_views(customer.id, 10,
                                                  0), PageDataEntityView)


class UserControllerTests(TBClientCETests):
    test_user = None

    @classmethod
    def setUpClass(cls) -> None:
        super(UserControllerTests, cls).setUpClass()

        cls.test_user = User(name='Test User', email='admin11@gmail.com', authority='TENANT_ADMIN')
        cls.test_user = cls.client.save_user(cls.test_user)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_user(cls.test_user.id)

    def test_get_users(self):
        self.assertIsInstance(self.client.get_users(10, 0), PageDataUser)

    def test_is_user_token_access_enabled(self):
        self.assertIsInstance(self.client.is_user_token_access_enabled(), bool)

    def test_get_user_token(self):
        self.assertIsInstance(self.client.get_user_token(self.test_user.id), JWTTokenPair)

    def test_get_activation_link(self):
        self.assertIsInstance(self.client.get_activation_link(self.test_user.id), str)

    def test_get_user_by_id(self):
        self.assertIsInstance(self.client.get_user_by_id(self.test_user.id), User)

    def test_get_customer_users(self):
        customer = self.client.get_customers(10, 0).data[0]
        self.assertIsInstance(self.client.get_customer_users(customer.id, 10, 0), PageDataUser)


if __name__ == '__main__':
    unittest.main()
