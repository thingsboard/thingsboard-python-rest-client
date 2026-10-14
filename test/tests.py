#  Copyright 2026. ThingsBoard
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

import os
import socket
import tempfile
import threading
import unittest
from uuid import uuid4

from tb_rest_client.rest import ApiException
from tb_rest_client.rest_client import *

TB_URL = os.environ.get('TB_URL', 'http://0.0.0.0:8080')

TB_TENANT_USERNAME = os.environ.get('TB_TENANT_USERNAME', 'tenant@thingsboard.org')
TB_TENANT_PASSWORD = os.environ.get('TB_TENANT_PASSWORD', 'tenant')
TB_TENANT_TOKEN = os.environ.get('TB_TENANT_TOKEN')  # a JWT instead of the credentials

TB_SYSADMIN_USERNAME = os.environ.get('TB_SYSADMIN_USERNAME', 'sysadmin@thingsboard.org')
TB_SYSADMIN_PASSWORD = os.environ.get('TB_SYSADMIN_PASSWORD', 'sysadmin')
TB_SYSADMIN_TOKEN = os.environ.get('TB_SYSADMIN_TOKEN')  # a JWT instead of the credentials

TASK_DONE_IMAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'images', 'task_done.png')


def login(client, username, password, token=None):
    if token:
        client.token_login(token)
    else:
        client.login(username, password)


created_customers = []


def ensure_customer(client):
    # the tests need a customer; the demo data has some, a clean server has none
    customers = client.get_customers(10, 0).data
    if customers:
        return customers[0]
    customer = client.save_customer(Customer(title='Test Customer'))
    created_customers.append(customer)
    return customer


def tearDownModule():
    if created_customers:
        with RestClient(TB_URL) as client:
            login(client, TB_TENANT_USERNAME, TB_TENANT_PASSWORD, TB_TENANT_TOKEN)
            for customer in created_customers:
                client.delete_customer(customer.id)


def unreachable_url():
    with socket.socket() as free:
        free.bind(('127.0.0.1', 0))
        return 'http://127.0.0.1:%d' % free.getsockname()[1]


def call_ai(test, function, *args, **kwargs):
    """Calls an AI endpoint. They need a base URL in the general settings of the sysadmin that is not "localhost"
    (checked on 4.4: with http://127.0.0.1:8080 they work, with http://localhost:8080 the server answers 400 "Please
    configure the base URL"). Without it only the route is reached. Calls that need an LLM are not made."""
    try:
        return function(*args, **kwargs)
    except ApiException as e:
        test.assertEqual(e.status, 400)
        test.assertIn('base URL', str(e.body))


class TBClientTests(unittest.TestCase):
    client = None

    @classmethod
    def setUpClass(cls) -> None:
        # ThingsBoard REST API URL
        url = TB_URL

        # Default Tenant Administrator credentials
        username = TB_TENANT_USERNAME
        password = TB_TENANT_PASSWORD

        with RestClient(url) as cls.client:
            login(cls.client, username, password, TB_TENANT_TOKEN)


class DeviceConnectivityControllerTests(TBClientTests):
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

    def test_download_gateway_docker_compose(self):
        gateway = self.client.save_device(Device(name='Test binary gateway', additional_info={'gateway': True},
                                                 device_profile_id=self.client.get_default_device_profile_info().id))
        try:
            compose = self.client.download_gateway_docker_compose(gateway.id)
            self.assertIsInstance(compose, bytes)
            self.assertIn(b'services', compose)
        finally:
            self.client.delete_device(gateway.id)


class AdminControllerTests(TBClientTests):
    def test_get_mail_processing_url(self):
        self.assertIsInstance(self.client.get_mail_processing_url(), str)

    @classmethod
    def setUpClass(cls) -> None:
        # ThingsBoard REST API URL
        url = TB_URL

        # Default Tenant Administrator credentials
        username = TB_SYSADMIN_USERNAME
        password = TB_SYSADMIN_PASSWORD

        with RestClient(url) as cls.client:
            login(cls.client, username, password, TB_SYSADMIN_TOKEN)

    @unittest.skip("Client id wasn't configured")
    def test_get_authorization_url(self):
        self.assertIsInstance(self.client.get_authorization_url(), str)

    def test_get_admin_settings(self):
        self.assertIsInstance(self.client.get_admin_settings('general'), AdminSettings)

    def test_get_system_settings(self):
        self.assertIsInstance(self.client.get_jwt_setting(), JwtSettings)
        self.assertIsInstance(self.client.get_security_settings(), SecuritySettings)
        self.assertIsInstance(self.client.get_system_info(), SystemInfo)
        self.assertIsInstance(self.client.get_features_info(), FeaturesInfo)
        self.assertIsInstance(self.client.get_license_usage_info(), LicenseUsageInfo)
        self.assertIsInstance(self.client.check_updates(), UpdateMessage)
        self.assertIsInstance(self.client.get_subscription_info(), SubscriptionInfo)

    def test_send_test_sms(self):
        # an SMPP server that does not exist: the request is built and sent, the server cannot deliver it
        provider = SmppSmsProviderConfiguration(type='SMPP', protocol_version='3.4', host='127.0.0.1', port=1,
                                                system_id='test', password='test', bind_type='TX')
        request = TestSmsRequest(number_to='+15550000000', message='test', provider_configuration=provider)
        with self.assertRaises(ApiException) as error:
            self.client.send_test_sms(request)
        self.assertIn(error.exception.status, (400, 500))

    def test_refresh_license(self):
        # not refreshed here (it reaches the license server): a tenant administrator is refused
        with RestClient(TB_URL) as client:
            login(client, TB_TENANT_USERNAME, TB_TENANT_PASSWORD, TB_TENANT_TOKEN)
            with self.assertRaises(ApiException) as error:
                client.refresh_license()
        self.assertEqual(error.exception.status, 403)


class AlarmCommentControllerTests(TBClientTests):
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


class TelemetryControllerTests(TBClientTests):
    device = None
    device_profile_id = None

    @classmethod
    def setUpClass(cls) -> None:
        super(TelemetryControllerTests, cls).setUpClass()

        cls.device_profile_id = cls.client.get_default_device_profile_info().id
        cls.device = Device(name='Test', device_profile_id=cls.device_profile_id)
        cls.device = cls.client.save_device(cls.device)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_device(cls.device.id)

    def test_get_latest_timeseries(self):
        self.assertIsInstance(
            self.client.get_latest_timeseries(self.device.id), dict)

    def test_get_timeseries(self):
        self.assertIsInstance(
            self.client.get_timeseries(entity_id=self.device.id, keys='string_read3', start_ts=164999693900,
                                       end_ts=168999693900), dict)

    def test_get_attributes_by_scope(self):
        self.assertIsInstance(
            self.client.get_attributes_by_scope(self.device.id,
                                                'SHARED_SCOPE'), list)

    def test_get_attributes(self):
        self.assertIsInstance(self.client.get_attributes(self.device.id),
                              list)

    def test_delete_entity_timeseries(self):
        self.assertIsNone(self.client.delete_entity_timeseries(self.device.id, 'combination',
                                                               delete_all_data_for_keys=True))

    def test_save_entity_telemetry(self):
        self.assertIsNone(self.client.save_entity_telemetry(self.device.id, 'ANY',
                                                            body={"ts": 1634712287000,
                                                                  "values": {"temperature": 26, "humidity": 87}}))

    def test_save_entity_telemetry_with_ttl(self):
        self.assertIsNone(self.client.save_entity_telemetry_with_ttl(self.device.id, scope='ANY', ttl=1000,
                                                                     body={"temperature": 26, "humidity": 87}))

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
        self.assertIsNone(self.client.save_entity_attributes_v2(self.device.id, 'SHARED_SCOPE', {'shared1': 12}))

    def test_delete_entity_attributes(self):
        self.assertIsNone(self.client.delete_entity_attributes(self.device.id, 'SHARED_SCOPE', 'shared1'))

    def test_save_entity_attributes_v1(self):
        self.assertIsNone(self.client.save_entity_attributes_v1(self.device.id, 'SHARED_SCOPE', {'shared1': 12}))

    def test_delete_device_attributes(self):
        self.assertIsNone(self.client.delete_device_attributes(self.device.id, 'SHARED_SCOPE', 'shared1'))

    def test_save_device_attributes(self):
        self.assertIsNone(self.client.save_device_attributes(self.device.id, 'SHARED_SCOPE', {'shared1': 12}))

    def test_get_timeseries_by_read_ts_kv_queries(self):
        now = int(time() * 1000)
        self.client.save_entity_telemetry(self.device.id, 'ANY', {'ts': now - 1000, 'values': {'temperature': 21}})
        result = self.client.get_timeseries_by_read_ts_kv_queries(
            [BaseReadTsKvQuery(id=1, key='temperature', start_ts=now - 60000, end_ts=now, limit=10, order='DESC',
                               # the server needs aggParameters (500 without them)
                               agg_parameters=AggregationParams(aggregation='NONE', interval_type='MILLISECONDS',
                                                                interval=0, tz_id='UTC'))], self.device.id)
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], ReadTsKvQueryResult)


class DeviceControllerTests(TBClientTests):
    device = None
    device_profile_id = None
    ota_package_request = None
    customer = None

    @classmethod
    def setUpClass(cls) -> None:
        super(DeviceControllerTests, cls).setUpClass()
        cls.device_profile_id = cls.client.get_default_device_profile_info().id

        cls.device = Device(name='Test', device_profile_id=cls.device_profile_id)
        cls.device = cls.client.save_device(cls.device)
        cls.cred = cls.client.get_device_credentials_by_device_id(cls.device.id)

        cls.ota_package_request = cls.client.save_ota_package_info(
            SaveOtaPackageInfoRequest(device_profile_id=cls.device_profile_id, title='Test OTA', version=1,
                                      type='FIRMWARE', file_name='tests.py'))

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
        self.assertIsNone(self.client.re_claim_device(self.device.name))

    def test_get_customer_devices(self):
        customer = ensure_customer(self.client)
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

    def test_get_tenant_device_infos(self):
        self.assertIsInstance(self.client.get_tenant_device_infos(10, 0), PageDataDeviceInfo)

    def test_process_devices_bulk_import(self):
        request = BulkImportRequest(file='name,type\nTest Bulk Device,default\n',
                                    mapping=Mapping(columns=[ColumnMapping(type='NAME'), ColumnMapping(type='TYPE')],
                                                    delimiter=',', update=False, header=True))
        result = self.client.process_devices_bulk_import(request)
        self.assertIsInstance(result, BulkImportResultDevice)
        self.assertEqual(result.created, 1)
        for device in self.client.get_tenant_devices(10, 0, text_search='Test Bulk Device').data:
            self.client.delete_device(device.id)

    def test_find_by_query_v1(self):
        parameters = RelationsSearchParameters(root_id=self.device.id.id, root_type='DEVICE', direction='FROM',
                                               relation_type_group='COMMON', max_level=1)
        self.assertIsInstance(self.client.find_by_query_v1(
            DeviceSearchQuery(parameters=parameters, relation_type='Contains', device_types=['default'])), list)

    def test_claim_device_by_name(self):
        # only a customer user can claim a device
        with self.assertRaises(ApiException) as error:
            self.client.claim_device_by_name(self.device.name, ClaimRequest(secret_key='test'))
        self.assertEqual(error.exception.status, 403)


class AssetControllerTests(TBClientTests):
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
        customer = ensure_customer(self.client)
        self.assertIsInstance(self.client.get_customer_assets(customer.id, 10, 0), PageDataAsset)

    def test_get_assets_by_ids(self):
        self.assertIsInstance(self.client.get_assets_by_ids([self.test_asset.id.id]), list)

    def test_get_asset_types(self):
        self.assertIsInstance(self.client.get_asset_types(), list)

    def test_get_asset_by_id(self):
        self.assertIsInstance(self.client.get_asset_by_id(self.test_asset.id), Asset)

    def test_get_tenant_asset_infos(self):
        self.assertIsInstance(self.client.get_tenant_asset_infos(10, 0), PageDataAssetInfo)

    def test_get_customer_asset_infos(self):
        self.assertIsInstance(self.client.get_customer_asset_infos(ensure_customer(self.client).id, 10, 0),
                              PageDataAssetInfo)

    def test_get_asset_info_by_id(self):
        self.assertIsInstance(self.client.get_asset_info_by_id(self.test_asset.id), AssetInfo)

    def test_process_asset_bulk_import(self):
        request = BulkImportRequest(file='name,type\nTest Bulk Asset,default\n',
                                    mapping=Mapping(columns=[ColumnMapping(type='NAME'), ColumnMapping(type='TYPE')],
                                                    delimiter=',', update=False, header=True))
        result = self.client.process_asset_bulk_import(request)
        self.assertIsInstance(result, BulkImportResultAsset)
        self.assertEqual(result.created, 1)
        for asset in self.client.get_tenant_assets(10, 0, text_search='Test Bulk Asset').data:
            self.client.delete_asset(asset.id)

    def test_find_by_query(self):
        parameters = RelationsSearchParameters(root_id=self.test_asset.id.id, root_type='ASSET', direction='FROM',
                                               relation_type_group='COMMON', max_level=1)
        self.assertIsInstance(self.client.find_by_query(
            AssetSearchQuery(parameters=parameters, relation_type='Contains', asset_types=['default'])), list)


class AssetProfileControllerTests(TBClientTests):
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

    def test_get_asset_profiles_by_ids(self):
        self.assertIsInstance(self.client.get_asset_profiles_by_ids([self.asset_profile.id.id]), list)


class AuditLogControllerTests(TBClientTests):
    customer = None
    device = None
    user = None

    @classmethod
    def setUpClass(cls) -> None:
        super(AuditLogControllerTests, cls).setUpClass()

        cls.customer = ensure_customer(cls.client)
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


class EntityGroupControllerTests(TBClientTests):
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
        cls.customer = ensure_customer(cls.client)
        cls.user_group = cls.client.get_entity_groups_by_owner_and_type('TENANT', cls.user.owner_id, 'USER')[-1]

        cls.role = Role(name='Test EGC', type='GROUP', permissions=['ALL'])
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
        customer = ensure_customer(self.client)
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
        self.assertIsInstance(self.client.get_owners(1, 0), PageDataContactBasedObject)

    def test_share_entity_group_to_child_owner_user_group(self):
        self.assertEqual(
            self.client.share_entity_group_to_child_owner_user_group(self.test_entity_group.id, self.user_group.id,
                                                                     self.role.id), None)

    def test_share_entity_group_to_child_owner_user_group_v2(self):
        self.assertIsNone(self.client.share_entity_group_to_child_owner_user_group_v2(
            ShareGroupRequest(owner_id=self.customer.id, all_user_group=True, read_else_write=True),
            self.test_entity_group.id))

    def test_get_entities(self):
        self.assertIsInstance(self.client.get_entities(self.test_entity_group.id, 10, 0),
                              PageDataShortEntityView)

    def test_get_group_entity(self):
        self.assertIsInstance(self.client.get_group_entity(self.test_entity_group.id, self.test_asset.id),
                              ShortEntityView)


class CustomerControllerTests(TBClientTests):
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

    def test_get_customers_by_ids(self):
        self.assertIsInstance(self.client.get_customers_by_ids([self.test_customer.id.id]), list)


class DashboardControllerTests(TBClientTests):
    test_dashboard = None
    customer = None

    @classmethod
    def setUpClass(cls) -> None:
        super(DashboardControllerTests, cls).setUpClass()

        cls.test_dashboard = Dashboard(name='Test', title='Test')
        cls.client.save_dashboard(body=cls.test_dashboard)
        cls.test_dashboard = [x for x in cls.client.get_user_dashboards(100, 0).data
                              if x.name == cls.test_dashboard.name][0]
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

    def test_get_customer_dashboards(self):
        self.assertIsInstance(
            self.client.get_customer_dashboards(ensure_customer(self.client).id, 10, 0), PageDataDashboardInfo)


class ConverterControllerTests(TBClientTests):
    test_converter = None

    @classmethod
    def setUpClass(cls) -> None:
        super(ConverterControllerTests, cls).setUpClass()
        cls.test_converter = Converter(name='Test', type='UPLINK', configuration={
            "decoder": "// Decode an uplink message from a buffer\n// payload - array of bytes\n// metadata - key/value object\n\n/** Decoder **/\n\n// decode payload to string\nvar payloadStr = decodeToString(payload);\n\n// decode payload to JSON\n// var data = decodeToJson(payload);\n\nvar deviceName = 'Device A';\nvar deviceType = 'thermostat';\nvar customerName = 'customer';\nvar groupName = 'thermostat devices';\n// use assetName and assetType instead of deviceName and deviceType\n// to automatically create assets instead of devices.\n// var assetName = 'Asset A';\n// var assetType = 'building';\n\n// Result object with device/asset attributes/telemetry data\nvar result = {\n// Use deviceName and deviceType or assetName and assetType, but not both.\n   deviceName: deviceName,\n   deviceType: deviceType,\n// assetName: assetName,\n// assetType: assetType,\n   customerName: customerName,\n   groupName: groupName,\n   attributes: {\n       model: 'Model A',\n       serialNumber: 'SN111',\n       integrationName: metadata['integrationName']\n   },\n   telemetry: {\n       temperature: 42,\n       humidity: 80,\n       rawData: payloadStr\n   }\n};\n\n/** Helper functions **/\n\nfunction decodeToString(payload) {\n   return String.fromCharCode.apply(String, payload);\n}\n\nfunction decodeToJson(payload) {\n   // covert payload to string.\n   var str = decodeToString(payload);\n\n   // parse string to JSON\n   var data = JSON.parse(str);\n   return data;\n}\n\nreturn result;",
            "encoder": None
        })
        cls.test_converter = cls.client.save_converter(cls.test_converter)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_converter(cls.test_converter.id)

    def test_unwrap_raw_payload(self):
        self.assertIsInstance(self.client.unwrap_raw_payload({'payload': {'a': 1}, 'metadata': {}}, 'CHIRPSTACK'),
                              dict)

    def test_get_converters(self):
        self.assertIsInstance(self.client.get_converters(10, 0), PageDataConverter)

    def test_get_converters_by_ids(self):
        self.assertIsInstance(self.client.get_converters_by_ids([self.test_converter.id.id]), list)

    def test_get_latest_converter_debug_input(self):
        self.assertIsInstance(self.client.get_latest_converter_debug_input(
            self.test_converter.id), (dict, type(None)))

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


class IntegrationControllerTests(TBClientTests):
    test_converter = None
    integration = None

    @classmethod
    def setUpClass(cls) -> None:
        super(IntegrationControllerTests, cls).setUpClass()

        cls.test_converter = Converter(name='Test', type='UPLINK', configuration={
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

    def test_export_integration_package(self):
        self.assertIsInstance(self.client.export_integration_package(self.integration.id), bytes)

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


class AlarmControllerTests(TBClientTests):
    test_alarm = None
    device = None
    device_profile_id = None

    @classmethod
    def setUpClass(cls) -> None:
        super(AlarmControllerTests, cls).setUpClass()

        cls.device_profile_id = cls.client.get_default_device_profile_info().id
        cls.device = Device(name='Test 1', device_profile_id=cls.device_profile_id)
        cls.device = cls.client.save_device(cls.device)

        cls.test_alarm = Alarm(name='Test', type='default',
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

    def test_get_all_alarms_v2(self):
        self.assertIsInstance(self.client.get_all_alarms_v2(10, 0), PageDataAlarmInfo)

    def test_get_alarms_v2(self):
        self.assertIsInstance(self.client.get_alarms_v2(self.device.id, 10, 0), PageDataAlarmInfo)


class DeviceProfileControllerTests(TBClientTests):
    test_device_profile = None

    @classmethod
    def setUpClass(cls) -> None:
        super(DeviceProfileControllerTests, cls).setUpClass()
        cls.test_device_profile = DeviceProfile(name='Test 1', type='DEFAULT', transport_type='MQTT',
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

    def test_get_device_profile_infos_by_ids(self):
        self.assertIsInstance(self.client.get_device_profile_infos_by_ids([self.test_device_profile.id.id]), list)


class EntityRelationControllerTests(TBClientTests):
    test_relation = None
    test_asset = None
    test_device = None
    device_profile_id = None
    entity_group = None
    asset_profile_id = None
    asset_device_profile_id = None

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

        cls.test_relation = EntityRelation(_from=cls.test_asset.id, to=cls.test_device.id, type="Contains", type_group="COMMON")
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

    def test_find_info_by_query(self):
        query = EntityRelationsQuery(parameters=RelationsSearchParameters(
            root_id=self.test_device.id.id, root_type='DEVICE', direction='FROM', relation_type_group='COMMON', max_level=1),
            filters=[])
        self.assertIsInstance(self.client.find_info_by_query(query), list)


class EntityViewControllerTests(TBClientTests):
    test_entity_view = None
    device = None
    device_profile_id = None
    customer = None

    @classmethod
    def setUpClass(cls) -> None:
        super(EntityViewControllerTests, cls).setUpClass()

        cls.device_profile_id = cls.client.get_default_device_profile_info().id
        cls.device = Device(name='Test 1', device_profile_id=cls.device_profile_id)
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
        customer = ensure_customer(self.client)
        self.assertIsInstance(
            self.client.get_customer_entity_views(customer.id, 10,
                                                  0), PageDataEntityView)

    def test_find_by_query_v4(self):
        parameters = RelationsSearchParameters(root_id=self.device.id.id, root_type='DEVICE', direction='FROM',
                                               relation_type_group='COMMON', max_level=1)
        self.assertIsInstance(self.client.find_by_query_v4(
            EntityViewSearchQuery(parameters=parameters, relation_type='Contains', entity_view_types=['default'])),
            list)


class RoleControllerTests(TBClientTests):
    test_role = None

    @classmethod
    def setUpClass(cls) -> None:
        super(RoleControllerTests, cls).setUpClass()
        cls.test_role = Role(name='Test 111', type='GENERIC', permissions={
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


class UserPermissionsControllerTests(TBClientTests):
    def test_get_allowed_permissions(self):
        self.assertIsInstance(self.client.get_allowed_permissions(), AllowedPermissionsInfo)


class UiSettingsControllerTests(TBClientTests):
    def test_get_help_base_url(self):
        self.assertIsInstance(self.client.get_help_base_url(), str)


class UsageInfoControllerTests(TBClientTests):
    def test_get_tenant_usage_info(self):
        self.assertIsInstance(self.client.get_tenant_usage_info(), UsageInfo)


class WidgetBundleControllerTests(TBClientTests):
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
        self.assertIsInstance(self.client.get_all_widgets_bundles(), list)

    def test_get_widget_bundles(self):
        self.assertIsInstance(self.client.get_widgets_bundles_v1(10, 0), PageDataWidgetsBundle)

    def test_get_widgets_bundles_by_ids(self):
        self.assertIsInstance(
            self.client.get_widgets_bundles_by_ids([self.widget_bundle.id.id]), list)


class WidgetTypeControllerTests(TBClientTests):
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
        cls.client.delete_widgets_bundle(cls.widget_bundle.id)

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


class NotificationControllerTests(TBClientTests):
    notification = None
    template = None
    notification_target = None

    @classmethod
    def setUpClass(cls) -> None:
        super(NotificationControllerTests, cls).setUpClass()

        configuration = PlatformUsersNotificationTargetConfig(type='PLATFORM_USERS', description='test',
                                                              users_filter={'type': 'ALL_USERS'})
        cls.notification_target = NotificationTarget(name='Test', configuration=configuration)
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

    def test_get_unread_notifications_count(self):
        self.assertIsInstance(self.client.get_unread_notifications_count(), int)


class NotificationTemplateControllerTests(TBClientTests):
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


class NotificationTargetControllerTests(TBClientTests):
    notification_target = None

    @classmethod
    def setUpClass(cls) -> None:
        super(NotificationTargetControllerTests, cls).setUpClass()

        configuration = PlatformUsersNotificationTargetConfig(type='PLATFORM_USERS', description='test',
                                                              users_filter={'type': 'ALL_USERS'})
        cls.notification_target = NotificationTarget(name='Test', configuration=configuration)
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


class NotificationRuleControllerTests(TBClientTests):
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
                                    trigger_config=AlarmNotificationRuleTriggerConfig(trigger_type='ALARM',
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


class ImageControllerTests(TBClientTests):
    image_info = None

    @classmethod
    def setUpClass(cls) -> None:
        super(ImageControllerTests, cls).setUpClass()

        cls.image_info = cls.client.upload_image(title='test', file=TASK_DONE_IMAGE)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_image('tenant', 'task_done.png')

    def test_upload_image(self):
        self.assertIsInstance(self.client.upload_image(title='tenant', file=TASK_DONE_IMAGE), TbResourceInfo)

    def test_update_image(self):
        self.assertIsInstance(self.client.update_image('tenant', 'task_done.png', TASK_DONE_IMAGE),
                              TbResourceInfo)

    def test_get_image_info(self):
        self.assertIsInstance(self.client.get_image_info('tenant', 'task_done.png'), TbResourceInfo)

    def test_get_images(self):
        self.assertIsInstance(self.client.get_images(10, 0), PageDataTbResourceInfo)

    def test_download_image(self):
        self.assertIsInstance(self.client.download_image('tenant', 'task_done.png'), bytes)

    def test_download_image_preview_and_public_image(self):
        image = self.client.upload_image(file=TASK_DONE_IMAGE, title='Test binary image')
        try:
            preview = self.client.download_image_preview('tenant', image.resource_key)
            self.assertIsInstance(preview, bytes)
            self.assertTrue(preview.startswith(b'\x89PNG'))
            public = self.client.update_image_public_status('tenant', image.resource_key, True)
            data = self.client.download_public_image(public.public_resource_key)
            with open(TASK_DONE_IMAGE, 'rb') as f:
                self.assertEqual(data, f.read())
        finally:
            self.client.delete_image('tenant', image.resource_key, force=True)


class QueueStatsControllerTests(TBClientTests):
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


class MobileAppBundleControllerTests(TBClientTests):
    mobile_app_bundle = None

    @classmethod
    def setUpClass(cls) -> None:
        super(MobileAppBundleControllerTests, cls).setUpClass()

        cls.mobile_app_bundle = MobileAppBundle(name='Test', title='Test')
        cls.mobile_app_bundle = cls.client.save_mobile_app_bundle(cls.mobile_app_bundle)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_mobile_app_bundle(cls.mobile_app_bundle.id)

    def test_get_mobile_app_bundle_info_by_id(self):
        self.assertIsInstance(self.client.get_mobile_app_bundle_info_by_id(self.mobile_app_bundle.id),
                              MobileAppBundleInfo)

    def test_get_tenant_mobile_app_bundle_infos(self):
        self.assertIsInstance(self.client.get_tenant_mobile_app_bundle_infos(10, 0),
                              PageDataMobileAppBundleInfo)

    def test_update_mobile_app_bundle_oauth2_clients(self):
        self.assertIsNone(self.client.update_mobile_app_bundle_oauth2_clients([], self.mobile_app_bundle.id))


class TranslationControllerTests(TBClientTests):
    @classmethod
    def setUpClass(cls) -> None:
        super(TranslationControllerTests, cls).setUpClass()

    def test_download_full_translation(self):
        self.assertIsInstance(self.client.download_full_translation(locale_code='en_US'), bytes)

    def test_get_available_java_locales(self):
        self.assertIsInstance(self.client.get_available_java_locales(), dict)

    def test_get_available_locales(self):
        self.assertIsInstance(self.client.get_available_locales(), dict)

    def test_get_translation_infos(self):
        self.assertIsInstance(self.client.get_translation_infos(), list)

    def test_get_translation_for_basic_edit(self):
        self.assertIsInstance(self.client.get_translation_for_basic_edit(locale_code='en_US'), dict)


class MobileAppControllerTests(TBClientTests):
    mobile_app = None

    @classmethod
    def setUpClass(cls) -> None:
        # ThingsBoard REST API URL
        url = TB_URL

        # Default Tenant Administrator credentials
        username = TB_SYSADMIN_USERNAME
        password = TB_SYSADMIN_PASSWORD

        with RestClient(url) as cls.client:
            login(cls.client, username, password, TB_SYSADMIN_TOKEN)

        cls.mobile_app = cls.client.save_mobile_app(body=MobileApp(title='Test Mobile App', pkg_name='string',
                                                                      app_secret='SDgegheheegheghthgehdsfsdFegfwE',
                                                                      platform_type='ANDROID', status='DRAFT'))
        assert cls.mobile_app is not None

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_mobile_app(cls.mobile_app.id)

    def test_get_mobile_app_info_by_id(self):
        self.assertIsInstance(self.client.get_mobile_app_info_by_id(self.mobile_app.id), MobileApp)

    def test_get_tenant_mobile_app_infos(self):
        self.assertIsInstance(self.client.get_tenant_mobile_app_infos(10, 0), PageDataMobileApp)


class CalculatedFieldControllerTests(TBClientTests):
    calculated_field = None
    device = None
    device_profile_id = None

    @classmethod
    def setUpClass(cls) -> None:
        super(CalculatedFieldControllerTests, cls).setUpClass()

        cls.device_profile_id = cls.client.get_default_device_profile_info().id
        cls.device = Device(name='Test', label='Test', device_profile_id=cls.device_profile_id)
        cls.device = cls.client.save_device(body=cls.device)

        cls.calculated_field = CalculatedField(name='Test', entity_id=cls.device.id, type='SIMPLE',
                                               configuration=SimpleCalculatedFieldConfiguration(
                                                   arguments={
                                                       'temperature': Argument(
                                                           ref_entity_id=cls.device.id,
                                                           ref_entity_key=ReferencedEntityKey(
                                                               key='temperature',
                                                               type='TS_LATEST',
                                                               scope='CLIENT_SCOPE'
                                                           )
                                                       )
                                                   },
                                                   expression='(temperature - 32)/1.8',
                                                   output=TimeSeriesOutput(name='celsius', type='TIME_SERIES'),
                                                   type='SIMPLE'
                                               ))
        cls.calculated_field = cls.client.save_calculated_field(cls.calculated_field)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_calculated_field(cls.calculated_field.id)
        cls.client.delete_device(cls.device.id)

    def test_reprocess_calculated_field_and_wait(self):
        now = int(time() * 1000)
        self.client.save_entity_telemetry(self.device.id, 'ANY', {'ts': now - 1000, 'values': {'temperature': 50}})
        self.assertIsNone(self.client.reprocess_calculated_field_and_wait(self.calculated_field.id, now - 5000, now))

    def test_get_calculated_field_by_id(self):
        self.assertIsInstance(self.client.get_calculated_field_by_id(self.calculated_field.id), CalculatedField)

    def test_get_calculated_fields_by_entity_id(self):
        self.assertIsInstance(self.client.get_calculated_fields_by_entity_id(self.device.id, 10, 0),
                              PageDataCalculatedField)

    def test_get_latest_calculated_field_debug_event(self):
        # the latest debug event as JSON, None while the field has none
        self.assertIsInstance(self.client.get_latest_calculated_field_debug_event(self.calculated_field.id),
                              (dict, type(None)))

    def test_get_calculated_field_names(self):
        self.assertIsInstance(self.client.get_calculated_field_names('SIMPLE', 10, 0), PageDataString)

    def test_get_calculated_fields(self):
        self.assertIsInstance(self.client.get_calculated_fields(10, 0), PageDataCalculatedFieldInfo)

    def test_test_calculated_field_script(self):
        self.assertIsInstance(self.client.test_calculated_field_script({'expression': 'return 1;',
                                                                         'arguments': {}}), dict)

    def test_calculated_field_output_strategies(self):
        def save(output):
            return self.client.save_calculated_field(CalculatedField(
                name='Test Output Strategy', entity_id=self.device.id, type='SIMPLE',
                configuration=SimpleCalculatedFieldConfiguration(
                    arguments={'t': Argument(ref_entity_key=ReferencedEntityKey(key='t', type='TS_LATEST'))},
                    expression='t + 1', output=output, type='SIMPLE')))
        for output in (TimeSeriesOutput(name='t2', type='TIME_SERIES', strategy=TimeSeriesImmediateOutputStrategy(
                           type='IMMEDIATE', save_time_series=True, save_latest=True)),
                       TimeSeriesOutput(name='t2', type='TIME_SERIES',
                                        strategy=TimeSeriesRuleChainOutputStrategy(type='RULE_CHAIN')),
                       AttributesOutput(name='t2', type='ATTRIBUTES', scope='SERVER_SCOPE',
                                        strategy=AttributesImmediateOutputStrategy(type='IMMEDIATE',
                                                                                   save_attribute=True)),
                       AttributesOutput(name='t2', type='ATTRIBUTES', scope='SERVER_SCOPE',
                                        strategy=AttributesRuleChainOutputStrategy(type='RULE_CHAIN'))):
            self.assertIsNotNone(output.strategy)  # the constructor must keep it
            field = save(output)
            try:
                read = self.client.get_calculated_field_by_id(field.id)
                self.assertIsInstance(read.configuration.output.strategy, type(output.strategy))
            finally:
                self.client.delete_calculated_field(field.id)

    def test_entity_aggregation_calculated_field(self):
        configuration = EntityAggregationCalculatedFieldConfiguration(
            type='ENTITY_AGGREGATION',
            arguments={'t': Argument(ref_entity_key=ReferencedEntityKey(key='t', type='TS_LATEST'))},
            metrics={'avg_t': AggMetric(function='AVG', input=AggKeyInput(type='key', key='t'))},
            interval=HourInterval(type='HOUR', tz='UTC'),
            output=TimeSeriesOutput(name='avg_t', type='TIME_SERIES'))
        field = self.client.save_calculated_field(CalculatedField(
            name='Test Aggregation', entity_id=self.device.id, type='ENTITY_AGGREGATION', configuration=configuration))
        try:
            read = self.client.get_calculated_field_by_id(field.id).configuration
            self.assertIsInstance(read, EntityAggregationCalculatedFieldConfiguration)
            self.assertIsInstance(read.interval, HourInterval)
            self.assertIsInstance(read.metrics['avg_t'].input, AggKeyInput)
        finally:
            self.client.delete_calculated_field(field.id)
        with self.assertRaises(ValueError):  # output is required for this configuration type
            EntityAggregationCalculatedFieldConfiguration(**{'type': 'ENTITY_AGGREGATION'})


class SecretControllerTests(TBClientTests):
    secret_info = None

    @classmethod
    def setUpClass(cls) -> None:
        super(SecretControllerTests, cls).setUpClass()

        try:
            cls.secret_info = cls.client.save_secret(Secret(name='Test Secret', value='Test Value', type='TEXT'))
        except ApiException as e:
            if e.status == 500 and 'Encryption failed' in str(e.body):
                raise unittest.SkipTest('the server has no secret encryption configured')
            raise

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_secret(cls.secret_info.id)

    def test_get_secret_by_id(self):
        self.assertIsInstance(self.client.get_secret_info_by_id(self.secret_info.id), SecretInfo)

    def test_get_secret_infos(self):
        self.assertIsInstance(self.client.get_secret_infos(10, 0), PageDataSecretInfo)

    def test_get_secret_names(self):
        self.assertIsInstance(self.client.get_secret_names(), list)

    def test_get_secret_info_by_name(self):
        self.assertIsInstance(self.client.get_secret_info_by_name(self.secret_info.name), SecretInfo)

    def test_update_secret_description(self):
        updated_description = "Updated description"
        self.secret_info.description = updated_description
        updated_secret_info = self.client.update_secret_description(self.secret_info.id, updated_description)
        self.assertEqual(updated_secret_info.description, f'"{updated_description}"')


class EntityQueryControllerTests(TBClientTests):
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
                                     entity_filter=EntityTypeFilter(type='entityType',
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
        entity_count_query = EntityCountQuery(entity_filter=EntityTypeFilter(type='entityType', entity_type='DEVICE'),
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
            entity_filter=EntityTypeFilter(type='entityType', entity_type='DEVICE'),
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
            entity_filter=EntityTypeFilter(type='entityType', entity_type='DEVICE'),
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
                                                                            body=entity_data_query),
            AvailableEntityKeys)

    def test_find_available_entity_keys_by_query_v2(self):
        query = EntityDataQuery(entity_filter=SingleEntityFilter(single_entity=self.user.id, type='singleEntity'),
                                page_link=EntityDataPageLink(page_size=10, page=0))
        self.assertIsInstance(self.client.find_available_entity_keys_by_query_v2(query), AvailableEntityKeysV2)


class UserControllerTests(TBClientTests):
    test_user = None
    customer = None
    test_mobile_session = None
    mobile_token = None

    @classmethod
    def setUpClass(cls) -> None:
        super(UserControllerTests, cls).setUpClass()

        cls.customer = ensure_customer(cls.client)
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

    def test_get_activation_link_info(self):
        self.assertIsInstance(self.client.get_activation_link_info(self.test_user.id), UserActivationLink)

    def test_get_users_by_ids(self):
        self.assertEqual([u.id.id for u in self.client.get_users_by_ids([self.test_user.id.id])],
                         [self.test_user.id.id])

    def test_user_settings_by_type(self):
        self.assertIsNone(self.client.put_user_settings_by_type({'testKey': 1}, 'general'))
        try:
            self.assertEqual(self.client.get_user_settings_by_type('general')['testKey'], 1)
        finally:
            self.assertIsNone(self.client.delete_general_user_settings('testKey'))
        self.assertNotIn('testKey', self.client.get_user_settings_by_type('general'))


class TenantControllerTests(TBClientTests):
    tenant = None
    tenant_profile_id = None

    @classmethod
    def setUpClass(cls) -> None:
        # ThingsBoard REST API URL
        url = TB_URL

        # Default Tenant Administrator credentials
        username = TB_SYSADMIN_USERNAME
        password = TB_SYSADMIN_PASSWORD

        with RestClient(url) as cls.client:
            login(cls.client, username, password, TB_SYSADMIN_TOKEN)

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

    def test_get_tenants_by_ids(self):
        self.assertIsInstance(self.client.get_tenants_by_ids([self.tenant.id.id]), list)


class TenantProfileControllerTests(TBClientTests):
    tenant_profile = None

    @classmethod
    def setUpClass(cls) -> None:
        # ThingsBoard REST API URL
        url = TB_URL

        # Default Tenant Administrator credentials
        username = TB_SYSADMIN_USERNAME
        password = TB_SYSADMIN_PASSWORD

        with RestClient(url) as cls.client:
            login(cls.client, username, password, TB_SYSADMIN_TOKEN)

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


class MobileApplicationControllerTests(TBClientTests):
    @classmethod
    def setUpClass(cls) -> None:
        super(MobileApplicationControllerTests, cls).setUpClass()

    def test_get_qr_code_settings(self):
        self.assertIsInstance(self.client.get_qr_code_settings(), QrCodeSettings)

    @unittest.skip("permissions error")
    def test_save_qr_code_settings(self):
        qr_code_config = QRCodeConfig()
        qr_code_setting = QrCodeSettings(use_default_app=True, android_enabled=True, qr_code_config=qr_code_config,
                                          google_play_link='https://play.google.com/store/apps/details?id=org.thingsboard.mobile',
                                          ios_enabled=True,
                                          app_store_link='https://apps.apple.com/us/app/thingsboard/id1456570833')
        self.assertIsInstance(self.client.save_qr_code_settings(body=qr_code_setting), QrCodeSettings)


class TBAgentClientTests(TBClientTests):
    """An agent profile, an agent, an application profile assigned to it and an installed application."""
    agent_profile = None
    agent = None
    app_profile = None
    application = None
    event = None
    device = None

    @classmethod
    def setUpClass(cls) -> None:
        super(TBAgentClientTests, cls).setUpClass()

        cls.agent_profile = cls.client.save_agent_profile(
            AgentProfile(name='Test Agent Profile', provision_type='AUTO_INSTALL_PER_APP_TYPE'))
        cls.agent = cls.client.save_agent(
            Agent(name='Test Agent', agent_profile_id=cls.agent_profile.id, routing_key='test-agent-routing-key',
                  secret='test-agent-secret'))
        cls.device = cls.client.save_device(
            Device(name='Test Agent Device', device_profile_id=cls.client.get_default_device_profile_info().id))

        cls.app_profile = cls.client.materialize_agent_app_profile('GENERIC', 'default', 'default')
        cls.app_profile.name = 'Test Agent App Profile'
        cls.app_profile = cls.client.save_agent_app_profile(cls.app_profile)
        cls.client.assign_app_profile_to_agent_profile(cls.agent_profile.id, cls.app_profile.id.id)

        template = [t for t in cls.client.get_agent_app_templates()
                    if t.app_type == 'GENERIC' and t.current_version == 'default'][0]
        application = cls.client.merge_agent_application_for_preview('default', app_type='GENERIC',
                                                                     compose_type='default')
        application.agent_id = cls.agent.id
        application.name = 'Test Agent Application'
        step_inputs = {step.id: step.state for step in template.start_steps if getattr(step, 'state', None)}
        installed = cls.client.install_agent_app(
            AgentAppEventRequest(action_type='INSTALL', application=application, step_inputs=step_inputs))
        cls.application = installed.application
        cls.event = installed.event

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_agent(cls.agent.id)
        cls.client.delete_agent_app_profile(cls.app_profile.id)
        cls.client.delete_agent_profile(cls.agent_profile.id)
        cls.client.delete_device(cls.device.id)


class AgentAppProfileControllerTests(TBAgentClientTests):
    def test_get_agent_app_profile_by_id(self):
        self.assertIsInstance(self.client.get_agent_app_profile_by_id(self.app_profile.id), AgentAppProfile)

    def test_get_agent_app_profile_info_by_id(self):
        self.assertIsInstance(self.client.get_agent_app_profile_info_by_id(self.app_profile.id),
                              AgentAppProfileInfo)

    def test_get_agent_app_profiles_by_app_type(self):
        profiles = self.client.get_agent_app_profiles_by_app_type('GENERIC')
        self.assertIsInstance(profiles, list)
        self.assertIsInstance(profiles[0], AgentAppProfileInfo)

    def test_get_agent_app_profiles_by_ids(self):
        profiles = self.client.get_agent_app_profiles_by_ids([self.app_profile.id.id])
        self.assertIsInstance(profiles[0], AgentAppProfile)

    def test_get_tenant_agent_app_profiles(self):
        self.assertIsInstance(self.client.get_tenant_agent_app_profiles(10, 0), PageDataAgentAppProfile)

    def test_materialize_agent_app_profile(self):
        self.assertIsInstance(self.client.materialize_agent_app_profile('GENERIC', 'default', 'default'),
                              AgentAppProfile)

    def test_merge_agent_app_profile_for_preview(self):
        self.assertIsInstance(
            self.client.merge_agent_app_profile_for_preview(self.app_profile, 'default', 'default'),
            AgentAppProfile)


class AgentAppTemplateControllerTests(TBClientTests):
    def test_get_agent_app_templates(self):
        templates = self.client.get_agent_app_templates()
        self.assertIsInstance(templates, list)
        self.assertIsInstance(templates[0], AgentAppTemplate)

    def test_get_agent_app_templates_by_app_type(self):
        templates = self.client.get_agent_app_templates_by_app_type('GENERIC', 'DOCKER_COMPOSE')
        self.assertIsInstance(templates[0], AgentAppTemplate)

    def test_get_latest_agent_app_template_by_app_type_and_config_type(self):
        self.assertIsInstance(
            self.client.get_latest_agent_app_template_by_app_type_and_config_type('GENERIC', 'DOCKER_COMPOSE'),
            AgentAppTemplate)

    def test_get_agent_app_template_by_current_version(self):
        self.assertIsInstance(
            self.client.get_agent_app_template_by_current_version('GENERIC', 'DOCKER_COMPOSE', 'default'),
            AgentAppTemplate)


class AgentApplicationControllerTests(TBAgentClientTests):
    def test_get_agent_application_by_id(self):
        self.assertIsInstance(self.client.get_agent_application_by_id(self.application.id), AgentApplicationInfo)

    def test_get_agent_applications_by_agent_id(self):
        self.assertIsInstance(self.client.get_agent_applications_by_agent_id(self.agent.id, 10, 0),
                              PageDataAgentApplicationInfo)

    def test_get_agent_app_events(self):
        self.assertIsInstance(self.client.get_agent_app_events(self.application.id, 10, 0), PageDataAgentAppEvent)

    def test_get_agent_app_units(self):
        self.assertIsInstance(self.client.get_agent_app_units(self.application.id, 10, 0), PageDataAgentAppUnit)

    def test_get_agent_app_event_by_id(self):
        self.assertIsInstance(self.client.get_agent_app_event_by_id(self.event.id), AgentAppEvent)

    def test_cancel_agent_app_event(self):
        self.assertIsNone(self.client.cancel_agent_app_event(self.application.id, self.event.id))

    def test_create_agent_app_event(self):
        # the agent is not connected, so the INSTALL event stays in processing and the server refuses a new one
        try:
            event = self.client.create_agent_app_event(AgentAppEventRequest(action_type='RESTART'),
                                                       self.application.id)
            self.assertIsInstance(event, AgentAppEvent)
        except ApiException as e:
            self.assertEqual(e.status, 400)

    def test_update_agent_application(self):
        application = self.client.get_agent_application_by_id(self.application.id)
        self.assertIsInstance(self.client.update_agent_application(application), AgentApplication)

    def test_attach_to_and_detach_from_profile(self):
        self.assertIsInstance(self.client.attach_to_profile(self.application.id, self.app_profile.id.id),
                              AgentApplication)
        self.assertIsInstance(self.client.detach_from_profile(self.application.id), AgentApplication)

    def test_merge_agent_application_for_preview(self):
        self.assertIsInstance(
            self.client.merge_agent_application_for_preview('default', app_type='GENERIC', compose_type='default'),
            AgentApplication)

    def test_get_managed_related_entity_ids(self):
        self.assertIsInstance(self.client.get_managed_related_entity_ids('DEVICE'), list)

    def test_get_related_entity_candidates(self):
        self.assertIsInstance(self.client.get_related_entity_candidates('DEVICE', 10, 0), PageDataEntityInfo)

    def test_assign_related_entity_to_agent_app(self):
        # only some application types (not GENERIC) can have a related entity
        with self.assertRaises(ApiException) as error:
            self.client.assign_related_entity_to_agent_app(self.application.id, self.device.id)
        self.assertEqual(error.exception.status, 400)

    def test_unassign_related_entity_from_agent_app(self):
        self.assertIsInstance(self.client.unassign_related_entity_from_agent_app(self.application.id),
                              AgentApplication)

    def test_get_agent_application_by_related_entity(self):
        with self.assertRaises(ApiException) as error:
            self.client.get_agent_application_by_related_entity(self.device.id)
        self.assertEqual(error.exception.status, 404)


class AgentBulkActionControllerTests(TBAgentClientTests):
    bulk_action = None

    @classmethod
    def setUpClass(cls) -> None:
        super(AgentBulkActionControllerTests, cls).setUpClass()

        cls.bulk_action = cls.client.bulk_operation(BulkOperationRequest(action_type='RESTART'), cls.agent_profile.id,
                                                    cls.app_profile.id.id)

    def test_get_agent_bulk_action(self):
        self.assertIsInstance(self.client.get_agent_bulk_action(self.bulk_action.id), AgentBulkAction)

    def test_get_agent_bulk_action_event_stats(self):
        self.assertIsInstance(self.client.get_agent_bulk_action_event_stats(self.bulk_action.id),
                              AgentBulkActionEventStats)

    def test_get_agent_bulk_action_events(self):
        self.assertIsInstance(self.client.get_agent_bulk_action_events(self.bulk_action.id, 10, 0),
                              PageDataAgentAppEventInfo)


class AgentControllerTests(TBAgentClientTests):
    def test_get_agent_by_id(self):
        self.assertIsInstance(self.client.get_agent_by_id(self.agent.id), Agent)

    def test_get_agent_info_by_id(self):
        self.assertIsInstance(self.client.get_agent_info_by_id(self.agent.id), AgentInfo)

    def test_get_agent_infos_by_ids(self):
        agents = self.client.get_agent_infos_by_ids([self.agent.id.id])
        self.assertIsInstance(agents, list)
        self.assertIsInstance(agents[0], AgentInfo)

    def test_get_tenant_agents(self):
        self.assertIsInstance(self.client.get_tenant_agents(10, 0), PageDataAgent)

    def test_get_tenant_agent_infos(self):
        self.assertIsInstance(self.client.get_tenant_agent_infos(10, 0), PageDataAgentInfo)

    def test_get_customer_agents(self):
        customer = ensure_customer(self.client)
        self.assertIsInstance(self.client.get_customer_agents(customer.id, 10, 0), PageDataAgent)

    def test_get_customer_agent_infos(self):
        customer = ensure_customer(self.client)
        self.assertIsInstance(self.client.get_customer_agent_infos(customer.id, 10, 0), PageDataAgentInfo)

    def test_get_agent_install_instructions(self):
        self.assertIsInstance(self.client.get_agent_install_instructions(self.agent.id, 'docker'),
                              AgentInstructions)

    def test_get_latest_agent_image_ref(self):
        self.assertIsInstance(self.client.get_latest_agent_image_ref(), str)

    def test_get_agent_upgrade_target(self):
        self.assertIsInstance(self.client.get_agent_upgrade_target(self.agent.id), str)

    def test_is_agent_upgrade_available(self):
        self.assertIsInstance(self.client.is_agent_upgrade_available(self.agent.id), bool)

    def test_get_agent_app_events_by_agent_id(self):
        self.assertIsInstance(self.client.get_agent_app_events_by_agent_id(self.agent.id, 10, 0),
                              PageDataAgentAppEvent)

    def test_get_agent_app_event_infos_by_agent_id(self):
        self.assertIsInstance(self.client.get_agent_app_event_infos_by_agent_id(self.agent.id, 10, 0),
                              PageDataAgentAppEventInfo)

    @classmethod
    def setUpClass(cls) -> None:
        super(AgentControllerTests, cls).setUpClass()

        # the server refuses a new event of an agent while the INSTALL event of the fixture is processed
        cls.client.cancel_agent_app_event(cls.application.id, cls.event.id)

    def test_upgrade_agent(self):
        self.assertIsInstance(
            self.client.upgrade_agent(AgentUpgradeRequest(image_ref=self.client.get_latest_agent_image_ref()),
                                      self.agent.id), AgentAppEvent)


class AgentProfileControllerTests(TBAgentClientTests):
    def test_get_agent_profile_by_id(self):
        self.assertIsInstance(self.client.get_agent_profile_by_id(self.agent_profile.id), AgentProfile)

    def test_get_agent_profile_info_by_id(self):
        self.assertIsInstance(self.client.get_agent_profile_info_by_id(self.agent_profile.id), AgentProfileInfo)

    def test_get_default_agent_profile_info(self):
        self.assertIsInstance(self.client.get_default_agent_profile_info(), AgentProfileInfo)

    def test_get_tenant_agent_profiles(self):
        self.assertIsInstance(self.client.get_tenant_agent_profiles(10, 0), PageDataAgentProfile)

    def test_get_tenant_agent_profile_infos(self):
        self.assertIsInstance(self.client.get_tenant_agent_profile_infos(10, 0), PageDataAgentProfileInfo)

    def test_get_agent_provision_instructions(self):
        self.assertIsInstance(self.client.get_agent_provision_instructions(self.agent_profile.id, 'docker'),
                              AgentInstructions)

    def test_get_agent_profile_app_profile_infos(self):
        infos = self.client.get_agent_profile_app_profile_infos(self.agent_profile.id)
        self.assertIsInstance(infos, list)
        self.assertIsInstance(infos[0], AgentAppProfileRelationInfo)

    def test_assign_app_profiles_to_agent_profile(self):
        self.assertIsNone(self.client.assign_app_profiles_to_agent_profile(self.agent_profile.id,
                                                                           [self.app_profile.id.id]))

    def test_set_app_profile_relates_on_auto_discovery(self):
        self.assertIsNone(self.client.set_app_profile_relates_on_auto_discovery(
            self.agent_profile.id, self.app_profile.id.id, True))

    def test_unassign_and_assign_app_profile(self):
        self.assertIsNone(self.client.unassign_app_profile_from_agent_profile(self.agent_profile.id,
                                                                              self.app_profile.id.id))
        self.assertIsNone(self.client.assign_app_profile_to_agent_profile(self.agent_profile.id,
                                                                          self.app_profile.id.id))

    def test_preview_bulk_operation(self):
        self.assertIsInstance(self.client.preview_bulk_operation(BulkOperationRequest(action_type='RESTART'),
                                                                 self.agent_profile.id, self.app_profile.id.id),
                              BulkOperationPreview)

    def test_bulk_operation(self):
        self.assertIsInstance(self.client.bulk_operation(BulkOperationRequest(action_type='RESTART'),
                                                         self.agent_profile.id, self.app_profile.id.id),
                              AgentBulkAction)

    def test_get_agent_profile_bulk_actions(self):
        self.assertIsInstance(self.client.get_agent_profile_bulk_actions(self.agent_profile.id, 10, 0),
                              PageDataAgentBulkAction)

    def test_get_agent_profile_app_profile_bulk_actions(self):
        self.assertIsInstance(self.client.get_agent_profile_app_profile_bulk_actions(
            self.agent_profile.id, self.app_profile.id.id, 10, 0), PageDataAgentBulkAction)

    def test_set_default_agent_profile(self):
        default = self.client.get_default_agent_profile_info()
        self.assertIsInstance(self.client.set_default_agent_profile(self.agent_profile.id), AgentProfile)
        self.assertIsInstance(self.client.set_default_agent_profile(default.id), AgentProfile)


class AiChatControllerTests(TBClientTests):
    def test_list_chats(self):
        self.assertIn(type(call_ai(self, self.client.list_chats)), (dict, list, type(None)))

    def test_create_chat(self):
        chat_id = call_ai(self, self.client.create_chat, {'title': 'Test chat'})
        if chat_id:  # the answer is the id of the new chat
            self.assertIsInstance(chat_id, str)
            try:
                self.assertIsNone(self.client.update_chat({'title': 'Test chat 2'}, chat_id))
                self.assertIsNotNone(self.client.get_chat_messages(chat_id))
            finally:
                self.assertIsNone(self.client.delete_chat(chat_id))


class AiDeviceDashboardControllerTests(TBClientTests):
    device = None

    @classmethod
    def setUpClass(cls) -> None:
        super(AiDeviceDashboardControllerTests, cls).setUpClass()

        cls.device = cls.client.save_device(
            Device(name='Test AI Dashboard Device', device_profile_id=cls.client.get_default_device_profile_info().id))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_device(cls.device.id)

    def test_generate_dashboard(self):
        try:
            self.client.generate_dashboard({'prompt': 'test'}, self.device.id)
        except ApiException as e:
            # 400: no base URL; 500 "Request blocked": no LLM behind the AI model of this server
            self.assertIn(e.status, (400, 500))


class AiModelControllerTests(TBClientTests):
    def test_save_ai_model(self):
        model = self.client.save_ai_model(AiModel(name='Test AI model', configuration=OpenAiChatModelConfig(
            provider='OPENAI', model_type='CHAT', model_id='gpt-4o-mini',
            provider_config=OpenAiProviderConfig(api_key='test-key'))))
        self.assertIsInstance(model, AiModel)
        try:
            self.assertIsInstance(self.client.get_ai_model_by_id(model.id).configuration, OpenAiChatModelConfig)
        finally:
            self.assertTrue(self.client.delete_ai_model_by_id(model.id))


class AiSolutionControllerTests(TBClientTests):
    def test_start_new(self):
        solution = call_ai(self, self.client.start_new)
        if solution:
            try:
                self.assertIsInstance(self.client.get_solution(solution['id']), dict)
                self.assertIsInstance(self.client.get_solutions(), list)
                self.assertIsNone(self.client.clear_step(solution['id'], 'INITIAL_CONFIGURATION'))
            finally:
                self.assertIsNone(self.client.delete_solution(solution['id']))
            return
        # not configured: the routes are reached with a random id
        solution_id = str(uuid4())
        call_ai(self, self.client.get_solutions)
        call_ai(self, self.client.get_solution, solution_id)
        call_ai(self, self.client.create_solution, solution_id)
        call_ai(self, self.client.chat, 'hello', solution_id, 'INITIAL_CONFIGURATION')
        call_ai(self, self.client.update_data, {'a': 1}, solution_id, 'test')
        call_ai(self, self.client.clear_step, solution_id, 'INITIAL_CONFIGURATION')
        call_ai(self, self.client.install_solution, solution_id)
        call_ai(self, self.client.uninstall_solution, solution_id)
        call_ai(self, self.client.delete_solution, solution_id)


class AiToolControllerTests(TBClientTests):
    def test_resolve_tool_approval(self):
        try:
            self.client.resolve_tool_approval({'toolCallId': 'none', 'approved': False})
        except ApiException as e:
            self.assertIn(e.status, (400, 404, 500))


class AlarmRuleControllerTests(TBClientTests):
    device = None
    alarm_rule = None

    @classmethod
    def setUpClass(cls) -> None:
        super(AlarmRuleControllerTests, cls).setUpClass()

        cls.device = cls.client.save_device(
            Device(name='Test Alarm Rule Device', device_profile_id=cls.client.get_default_device_profile_info().id))
        configuration = AlarmCalculatedFieldConfiguration(
            arguments={'temperature': Argument(
                ref_entity_key=ReferencedEntityKey(key='temperature', type='TS_LATEST'))},
            create_rules={'CRITICAL': AlarmRule(condition=SimpleAlarmCondition(
                expression=SimpleAlarmConditionExpression(
                    filters=[AlarmConditionFilter(
                        argument='temperature', value_type='NUMERIC', operation='AND',
                        predicates=[AlarmRuleNumericFilterPredicate(
                            operation='GREATER', value=AlarmConditionValueDouble(static_value=50.0),
                            type='NUMERIC')])],
                    operation='AND', type='SIMPLE'), type='SIMPLE'))},
            type='ALARM')
        cls.alarm_rule = cls.client.save_alarm_rule(
            AlarmRuleDefinition(name='Test Alarm Rule', entity_id=cls.device.id, configuration=configuration))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_alarm_rule(cls.alarm_rule.id.id)
        cls.client.delete_device(cls.device.id)

    def test_get_alarm_rule_by_id(self):
        self.assertIsInstance(self.client.get_alarm_rule_by_id(self.alarm_rule.id.id), AlarmRuleDefinition)

    def test_get_alarm_rules(self):
        self.assertIsInstance(self.client.get_alarm_rules(10, 0), PageDataAlarmRuleDefinitionInfo)

    def test_get_alarm_rules_by_entity_id(self):
        self.assertIsInstance(self.client.get_alarm_rules_by_entity_id(self.device.id, 10, 0),
                              PageDataAlarmRuleDefinition)

    def test_get_alarm_rule_names(self):
        names = self.client.get_alarm_rule_names(10, 0)
        self.assertIsInstance(names, PageDataString)
        self.assertIn('Test Alarm Rule', names.data)

    def test_get_latest_alarm_rule_debug_event(self):
        self.assertIsInstance(self.client.get_latest_alarm_rule_debug_event(self.alarm_rule.id.id),
                              (dict, type(None)))

    def test_test_alarm_rule_script(self):
        self.assertIsInstance(self.client.test_alarm_rule_script({'expression': 'return 1;', 'arguments': {}}), dict)


class ApiKeyControllerTests(TBClientTests):
    api_key = None

    @classmethod
    def setUpClass(cls) -> None:
        super(ApiKeyControllerTests, cls).setUpClass()

        cls.user = cls.client.get_user()
        cls.api_key = cls.client.save_api_key(ApiKeyInfo(description='Test API key', user_id=cls.user.id, enabled=True))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_api_key(cls.api_key.id)

    def test_save_api_key(self):
        self.assertIsInstance(self.api_key, ApiKey)
        self.assertTrue(self.api_key.value)

    def test_get_user_api_keys(self):
        self.assertIsInstance(self.client.get_user_api_keys(self.user.id, 10, 0), PageDataApiKeyInfo)

    def test_enable_api_key(self):
        self.assertFalse(self.client.enable_api_key(self.api_key.id, False).enabled)
        self.assertTrue(self.client.enable_api_key(self.api_key.id, True).enabled)

    def test_update_api_key_description(self):
        self.assertIsInstance(self.client.update_api_key_description(self.api_key.id, 'Test API key 2'), ApiKeyInfo)


class AuthControllerTests(TBClientTests):
    customer = None

    @classmethod
    def setUpClass(cls) -> None:
        super(AuthControllerTests, cls).setUpClass()

        cls.customer = cls.client.save_customer(Customer(title='Test Auth Customer'))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_customer(cls.customer.id)

    def test_change_password(self):
        group = self.client.get_entity_group_by_owner_and_name_and_type(self.customer.id, 'USER', 'Customer Users')
        user = self.client.save_user(User(authority='CUSTOMER_USER', customer_id=self.customer.id,
                                          email='test-change-password@example.com'),
                                     send_activation_mail=False, entity_group_id=group.id)
        try:
            link = self.client.get_activation_link(user.id)
            self.client.activate_user(ActivateUserRequest(activate_token=link.split('=')[-1], password='OldPassw0rd!'),
                                      send_activation_mail=False)
            with RestClient(TB_URL) as user_client:
                user_client.login('test-change-password@example.com', 'OldPassw0rd!')
                self.assertIsInstance(user_client.change_password(
                    ChangePasswordRequest(current_password='OldPassw0rd!', new_password='NewPassw0rd!')), JwtPair)
            with RestClient(TB_URL) as user_client:
                user_client.login('test-change-password@example.com', 'NewPassw0rd!')
                self.assertEqual(user_client.get_user().email, 'test-change-password@example.com')
        finally:
            self.client.delete_user(user.id)

    def test_login_timeout(self):
        # a server that accepts the connection and never answers the TLS handshake: login fails instead of hanging
        server = socket.socket()
        server.bind(('127.0.0.1', 0))
        server.listen()
        connections = []
        threading.Thread(target=lambda: connections.append(server.accept()[0]), daemon=True).start()
        try:
            client = RestClient('https://127.0.0.1:%d' % server.getsockname()[1], timeout=1)
            started = time()
            with self.assertRaises(Exception):
                client.login('test@example.com', 'test')
            self.assertLess(time() - started, 5)
        finally:
            server.close()

    def test_token_refresh_survives_network_failure(self):
        if TB_TENANT_TOKEN:
            self.skipTest('a token login has no refresh token')
        with RestClient(TB_URL, refresh_retry_delay=0.2) as client:
            client.login(TB_TENANT_USERNAME, TB_TENANT_PASSWORD)
            server_url = client.base_url
            client.base_url = unreachable_url()
            with self.assertLogs('tb_rest_client.rest_client', 'ERROR') as logs:
                client.token_info['exp'] = 0
                for _ in range(50):
                    if len(logs.records) >= 3:
                        break
                    sleep(0.1)
            self.assertTrue(client.is_alive())
            self.assertGreaterEqual(len(logs.records), 3)
            self.assertEqual([record.exc_info is not None for record in logs.records],
                             [True] + [False] * (len(logs.records) - 1))
            client.base_url = server_url
            for _ in range(20):
                if client.token_info['exp'] > time():
                    break
                sleep(0.25)
            self.assertGreater(client.token_info['exp'], time())
            self.assertIsInstance(client.get_user(), User)
        client.join(5)
        self.assertFalse(client.is_alive())

    def test_stop_interrupts_token_refresh_retry(self):
        if TB_TENANT_TOKEN:
            self.skipTest('a token login has no refresh token')
        with RestClient(TB_URL, refresh_retry_delay=60) as client:
            client.login(TB_TENANT_USERNAME, TB_TENANT_PASSWORD)
            client.base_url = unreachable_url()
            with self.assertLogs('tb_rest_client.rest_client', 'ERROR'):
                client.token_info['exp'] = 0
                sleep(1.5)
            self.assertTrue(client.is_alive())
        client.join(2)
        self.assertFalse(client.is_alive())


class BlobEntityControllerTests(TBClientTests):
    def test_get_blob_entities_by_ids(self):
        self.assertEqual(self.client.get_blob_entities_by_ids([str(uuid4())]), [])


class CustomMenuControllerTests(TBClientTests):
    def test_create_custom_menu(self):
        menu = self.client.create_custom_menu(CustomMenuInfo(name='Test Custom Menu', scope='TENANT',
                                                             assignee_type='NO_ASSIGN'))
        self.assertIsInstance(menu, CustomMenu)
        try:
            self.assertIsInstance(self.client.get_custom_menu_info_by_id(menu.id), CustomMenuInfo)
            self.assertIsNone(self.client.update_custom_menu_name(menu.id, 'Test Custom Menu 2'))
        finally:
            self.assertIsInstance(self.client.delete_custom_menu(menu.id, force=True), CustomMenuDeleteResult)

    def test_update_custom_menu_config(self):
        menu = self.client.create_custom_menu(CustomMenuInfo(name='Test Custom Menu Config', scope='TENANT',
                                                             assignee_type='NO_ASSIGN'))
        try:
            # hidden items: visible is a field of MenuItem too and must survive the constructors
            config = CustomMenuConfig(items=[
                DefaultMenuItem(id='home', type='DEFAULT', visible=False),
                CustomMenuItem(name='Test link', type='CUSTOM', menu_item_type='LINK', link_type='URL',
                               url='https://example.com', visible=False)])
            self.assertIsInstance(self.client.update_custom_menu_config(menu.id, config), CustomMenu)
            items = self.client.get_custom_menu_config(menu.id).items
            self.assertEqual([(type(item), item.visible) for item in items],
                             [(DefaultMenuItem, False), (CustomMenuItem, False)])
        finally:
            self.client.delete_custom_menu(menu.id, force=True)


class DomainControllerTests(TBClientTests):
    def test_save_domain(self):
        domain = self.client.save_domain(Domain(name='test-domain.example.com', oauth2_enabled=False,
                                                propagate_to_edge=False))
        self.assertIsInstance(domain, Domain)
        try:
            self.assertIsInstance(self.client.get_domain_info_by_id(domain.id), DomainInfo)
        finally:
            self.assertIsNone(self.client.delete_domain(domain.id))


class EdgeControllerTests(TBClientTests):
    def test_get_edges_by_ids(self):
        self.assertEqual(self.client.get_edges_by_ids([str(uuid4())]), [])

    def test_get_edges_by_entity_group_id(self):
        entity_group = self.client.get_entity_groups_by_type('EDGE')[0]
        self.assertIsInstance(self.client.get_edges_by_entity_group_id(entity_group.id, '10', '0'), PageDataEdge)

    def test_find_by_query_v2(self):
        tenant_id = self.client.get_user().tenant_id
        parameters = RelationsSearchParameters(root_id=tenant_id.id, root_type='TENANT', direction='FROM',
                                               relation_type_group='COMMON', max_level=1)
        self.assertIsInstance(self.client.find_by_query_v2(
            EdgeSearchQuery(parameters=parameters, relation_type='Contains', edge_types=['default'])), list)


class EventControllerTests(TBClientTests):
    device = None

    @classmethod
    def setUpClass(cls) -> None:
        super(EventControllerTests, cls).setUpClass()

        cls.device = cls.client.save_device(
            Device(name='Test Event Device', device_profile_id=cls.client.get_default_device_profile_info().id))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_device(cls.device.id)

    def test_get_events_post(self):
        user = self.client.get_user()
        for event_filter in (RuleNodeDebugEventFilter(event_type='DEBUG_RULE_NODE'),
                             CalculatedFieldDebugEventFilter(event_type='DEBUG_CALCULATED_FIELD'),
                             RawDataEventFilter(event_type='RAW_DATA')):
            self.assertIsInstance(self.client.get_events_post(user.tenant_id, 10, 0, self.device.id, event_filter),
                                  PageDataEventInfo)


class OtaPackageControllerTests(TBClientTests):
    def test_download_ota_package(self):
        profile_id = self.client.get_default_device_profile_info().id
        package = self.client.save_ota_package_info(SaveOtaPackageInfoRequest(
            device_profile_id=profile_id, title='Test binary OTA', version='1.0', type='FIRMWARE', uses_url=False))
        try:
            path = os.path.join(tempfile.mkdtemp(), 'firmware.bin')
            with open(path, 'wb') as f:
                f.write(b'\x00\x01firmware')
            self.client.save_ota_package_data(ota_package_id=package.id, checksum_algorithm='SHA256', file=path)
            self.assertEqual(self.client.download_ota_package(package.id), b'\x00\x01firmware')
        finally:
            self.client.delete_ota_package(package.id)


class OwnerControllerTests(TBClientTests):
    device = None
    customer = None

    @classmethod
    def setUpClass(cls) -> None:
        super(OwnerControllerTests, cls).setUpClass()

        cls.device = cls.client.save_device(
            Device(name='Test Owner Device', device_profile_id=cls.client.get_default_device_profile_info().id))
        cls.customer = cls.client.save_customer(Customer(title='Test Owner Customer'))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_device(cls.device.id)
        cls.client.delete_customer(cls.customer.id)

    def test_change_owner_to_customer_and_tenant(self):
        self.assertIsNone(self.client.change_owner_to_customer(self.customer.id, self.device.id))
        self.assertEqual(self.client.get_device_by_id(self.device.id).owner_id.id, self.customer.id.id)
        user = self.client.get_user()
        self.assertIsNone(self.client.change_owner_to_tenant(user.tenant_id, self.device.id))
        self.assertEqual(self.client.get_device_by_id(self.device.id).owner_id.id, user.tenant_id.id)


class ReportControllerTests(TBClientTests):
    report_template = None
    report = None

    @classmethod
    def setUpClass(cls) -> None:
        super(ReportControllerTests, cls).setUpClass()

        cls.report_template = cls.client.save_report_template(ReportTemplate(
            name='Test Report Template', format='PDF', type='REPORT',
            configuration=ReportTemplateConfig(name_pattern='Test report', format='PDF', components=[])))
        cls.client.request_report(ReportRequest(report_template_id=cls.report_template.id, timezone='UTC'))
        for _ in range(30):
            reports = cls.client.get_report_infos(10, 0, report_template_id=cls.report_template.id).data
            if reports:
                cls.report = cls.client.get_report_by_id(reports[0].id)
                break
            sleep(1)
        assert cls.report is not None, 'the report was not generated'

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_report(cls.report.id)
        cls.client.delete_report_template(cls.report_template.id)

    def test_get_report_by_id(self):
        self.assertIsInstance(self.client.get_report_by_id(self.report.id), Report)

    def test_get_reports(self):
        self.assertIsInstance(self.client.get_reports(10, 0), PageDataReport)

    def test_get_report_infos(self):
        self.assertIsInstance(self.client.get_report_infos(10, 0), PageDataReportInfo)

    def test_get_report_infos_by_ids(self):
        infos = self.client.get_report_infos_by_ids([self.report.id.id])
        self.assertIsInstance(infos[0], ReportInfo)

    def test_download_report(self):
        self.assertIsInstance(self.client.download_report(self.report.id), bytes)

    def test_update_report_public_status_and_download_by_public_key(self):
        report = self.client.update_report_public_status(self.report.id, True)
        self.assertIsInstance(report, Report)
        self.assertIsInstance(self.client.download_report_by_public_key(report.public_key), bytes)
        self.client.update_report_public_status(self.report.id, False)

    def test_create_report(self):
        pdf = self.client.download_report(self.report.id)
        path = os.path.join(tempfile.mkdtemp(), 'test_report.pdf')
        with open(path, 'wb') as f:
            f.write(pdf)
        user = self.client.get_user()
        report = self.client.create_report(path, Report(name='Test created report', format='PDF',
                                                        template_id=self.report_template.id, tenant_id=user.tenant_id,
                                                        user_id=user.id))
        self.assertIsInstance(report, Report)
        self.client.delete_report(report.id)


class RpcV1ControllerTests(TBClientTests):
    device = None

    @classmethod
    def setUpClass(cls) -> None:
        super(RpcV1ControllerTests, cls).setUpClass()

        cls.device = cls.client.save_device(
            Device(name='Test RPC v1 Device', device_profile_id=cls.client.get_default_device_profile_info().id))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_device(cls.device.id)

    # nobody answers: 409 for a device that is not connected, 504 when a two-way request times out
    def test_handle_one_way_device_rpc_request(self):
        with self.assertRaises(ApiException) as error:
            self.client.handle_one_way_device_rpc_request(self.device.id, {'method': 'test', 'params': {},
                                                                           'timeout': 1000})
        self.assertIn(error.exception.status, (409, 504))

    def test_handle_two_way_device_rpc_request(self):
        with self.assertRaises(ApiException) as error:
            self.client.handle_two_way_device_rpc_request(self.device.id, {'method': 'test', 'params': {},
                                                                           'timeout': 1000})
        self.assertIn(error.exception.status, (409, 504))


class RpcV2ControllerTests(TBClientTests):
    device = None

    @classmethod
    def setUpClass(cls) -> None:
        super(RpcV2ControllerTests, cls).setUpClass()

        cls.device = cls.client.save_device(
            Device(name='Test RPC v2 Device', device_profile_id=cls.client.get_default_device_profile_info().id))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_device(cls.device.id)

    def test_handle_two_way_device_rpc_request_v1(self):
        # nobody answers: 409 for a device that is not connected, 504 when the request times out
        with self.assertRaises(ApiException) as error:
            self.client.handle_two_way_device_rpc_request_v1(self.device.id, {'method': 'test', 'params': {},
                                                                              'timeout': 1000})
        self.assertIn(error.exception.status, (409, 504))


class RuleEngineControllerTests(TBClientTests):
    """Nothing answers a request in the rule chain of a new device: the server times out (408)."""
    device = None

    @classmethod
    def setUpClass(cls) -> None:
        super(RuleEngineControllerTests, cls).setUpClass()

        cls.device = cls.client.save_device(
            Device(name='Test Rule Engine Device', device_profile_id=cls.client.get_default_device_profile_info().id))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_device(cls.device.id)

    def test_handle_rule_engine_request_for_entity(self):
        with self.assertRaises(ApiException) as error:
            self.client.handle_rule_engine_request_for_entity(self.device.id, {'test': 1})
        self.assertEqual(error.exception.status, 408)

    def test_handle_rule_engine_request_for_entity_with_timeout(self):
        with self.assertRaises(ApiException) as error:
            self.client.handle_rule_engine_request_for_entity_with_timeout(self.device.id, 1000, {'test': 1})
        self.assertEqual(error.exception.status, 408)

    def test_handle_rule_engine_request_for_entity_with_queue_and_timeout(self):
        with self.assertRaises(ApiException) as error:
            self.client.handle_rule_engine_request_for_entity_with_queue_and_timeout(self.device.id, 'Main', 1000,
                                                                                    {'test': 1})
        self.assertEqual(error.exception.status, 408)

    def test_handle_rule_engine_request_for_user(self):
        with self.assertRaises(ApiException) as error:
            self.client.handle_rule_engine_request_for_user({'test': 1})
        self.assertEqual(error.exception.status, 408)


class SchedulerEventControllerTests(TBClientTests):
    def test_get_scheduler_events_by_ids(self):
        self.assertEqual(self.client.get_scheduler_events_by_ids([str(uuid4())]), [])

    def test_get_scheduler_events_all(self):
        self.assertIsInstance(self.client.get_scheduler_events_all(), list)

    def test_get_scheduler_events_by_range(self):
        self.assertIsInstance(self.client.get_scheduler_events_by_range(0, 9999999999999), list)


class SolutionExportImportControllerTests(TBClientTests):
    device = None

    @classmethod
    def setUpClass(cls) -> None:
        super(SolutionExportImportControllerTests, cls).setUpClass()

        cls.device = cls.client.save_device(
            Device(name='Test Solution Device', device_profile_id=cls.client.get_default_device_profile_info().id))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_device(cls.device.id)

    def test_export_and_validate_solution(self):
        solution = self.client.export_solution(SolutionExportRequest(internal_ids=[self.device.id]))
        self.assertIsInstance(solution, SolutionExportResponse)
        self.assertIsInstance(self.client.validate_solution(solution.solution), SolutionValidationResult)

    def test_export_solution_with_export_data_subclasses(self):
        rule_chain = self.client.get_rule_chains(10, 0).data[0]
        # a bundle of the tenant: the system bundles cannot be exported
        bundle = self.client.save_widgets_bundle(WidgetsBundle(name='Test Solution Bundle', alias='test_solution',
                                                               title='Test Solution Bundle'))
        group = self.client.get_entity_groups_by_type('DEVICE')[0]
        try:
            solution = self.client.export_solution(SolutionExportRequest(
                internal_ids=[self.device.id, rule_chain.id, bundle.id, group.id])).solution
        finally:
            self.client.delete_widgets_bundle(bundle.id)
        types = {type(e).__name__ for entities in solution.entities.values() for e in entities}
        for expected in ('DeviceExportData', 'RuleChainExportData', 'WidgetsBundleExportData', 'EntityGroupExportData'):
            self.assertIn(expected, types)

    def test_import_solution(self):
        exported = self.client.export_solution(SolutionExportRequest(internal_ids=[self.device.id]))
        self.client.delete_device(self.device.id)
        try:
            result = self.client.import_solution(exported.solution)
            self.assertIsInstance(result, SolutionImportResult)
            self.assertEqual(result.created, {'DEVICE': 1})
        finally:
            # the imported device gets a new id; the fixture deletes the device by the old one in tearDownClass
            for device in self.client.get_tenant_devices(100, 0, text_search=self.device.name).data:
                type(self).device = device


class TbResourceControllerTests(TBClientTests):
    def test_upload_resource(self):
        path = os.path.join(tempfile.mkdtemp(), 'test_resource.js')
        with open(path, 'w') as f:
            f.write('var test = 1;')
        resource = self.client.upload_resource(resource_type='JS_MODULE', file=path, title='Test resource')
        self.assertIsInstance(self.client.delete_resource_v1(resource.id, force=True), TbResourceDeleteResult)

    def test_download_resource(self):
        path = os.path.join(tempfile.mkdtemp(), 'test_download.js')
        with open(path, 'w') as f:
            f.write('var downloaded = 1;')
        resource = self.client.upload_resource(resource_type='JS_MODULE', file=path, title='Test download')
        try:
            self.assertEqual(self.client.download_resource(resource.id), b'var downloaded = 1;')
            self.assertEqual(self.client.download_js_resource_if_changed(resource.id), b'var downloaded = 1;')
            self.assertEqual(self.client.download_resource_if_changed('js_module', 'tenant', resource.resource_key),
                             b'var downloaded = 1;')
        finally:
            self.client.delete_resource_v1(resource.id, force=True)

    def test_get_system_or_tenant_resources_by_ids(self):
        image = self.client.upload_image(file=TASK_DONE_IMAGE, title='Test ids')
        try:
            found = self.client.get_system_or_tenant_resources_by_ids([image.id.id])
            self.assertEqual([r.id.id for r in found], [image.id.id])
        finally:
            self.client.delete_image('tenant', image.resource_key, force=True)

    def test_get_resource_info(self):
        image = self.client.upload_image(file=TASK_DONE_IMAGE, title='Test resource info')
        try:
            self.assertIsInstance(self.client.get_resource_info('IMAGE', 'tenant', image.resource_key),
                                  TbResourceInfo)
        finally:
            self.client.delete_image('tenant', image.resource_key, force=True)


class WhiteLabelingControllerTests(TBClientTests):
    def test_get_and_save_mail_templates(self):
        templates = self.client.get_mail_templates()
        self.assertIsInstance(templates, dict)
        # the same templates are saved back, nothing changes
        self.assertIsInstance(self.client.save_mail_templates(templates), dict)


if __name__ == '__main__':
    unittest.main()
