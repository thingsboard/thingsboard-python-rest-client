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

from tb_rest_client32.rest_client_base import *

logger = getLogger(__name__)


class RestClientCE(RestClientBase):
    def __init__(self, base_url):
        super().__init__(base_url)

    def add_dashboard_customers(self, dashboard_id: DashboardId, str_customer_ids, **kwargs):
        return self.dashboard_controller.add_dashboard_customers_using_post(dashboard_id.id, str_customer_ids, **kwargs)

    def assign_dashboard_to_customer(self, customer_id: CustomerId, dashboard_id: DashboardId, **kwargs):
        return self.dashboard_controller.assign_dashboard_to_customer_using_post(customer_id.id, dashboard_id.id, **kwargs)

    def assign_dashboard_to_public_customer(self, dashboard_id: DashboardId, **kwargs):
        return self.dashboard_controller.assign_dashboard_to_public_customer_using_post(dashboard_id.id, **kwargs)

    def get_customer_dashboards(self, customer_id: CustomerId, page_size=100, page=0, **kwargs):
        return self.dashboard_controller.get_customer_dashboards_using_get(customer_id.id, str(page_size), str(page), **kwargs)

    def remove_dashboard_customers(self, dashboard_id: DashboardId, str_customer_ids, **kwargs):
        return self.dashboard_controller.remove_dashboard_customers_using_post(dashboard_id.id, str_customer_ids, **kwargs)

    def unassign_dashboard_from_customer(self, customer_id: CustomerId, dashboard_id: DashboardId, **kwargs):
        return self.dashboard_controller.unassign_dashboard_from_customer_using_delete(customer_id.id, dashboard_id.id, **kwargs)

    def unassign_dashboard_from_public_customer(self, dashboard_id: DashboardId, **kwargs):
        return self.dashboard_controller.unassign_dashboard_from_public_customer_using_delete(dashboard_id.id, **kwargs)

    def update_dashboard_customers(self, dashboard_id: DashboardId, str_customer_ids, **kwargs):
        return self.dashboard_controller.update_dashboard_customers_using_post(dashboard_id.id, str_customer_ids, **kwargs)

    def get_users(self, page_size=100, page=0, **kwargs):
        return self.user_controller.get_users_using_get(str(page_size), str(page), **kwargs)

    def assign_entity_view_to_customer(self, customer_id: CustomerId, entity_view_id: EntityViewId, **kwargs):
        return self.entity_view_controller.assign_entity_view_to_customer_using_post(customer_id.id, entity_view_id.id, **kwargs)

    def assign_entity_view_to_public_customer(self, entity_view_id: EntityViewId, **kwargs):
        return self.entity_view_controller.assign_entity_view_to_public_customer_using_post(entity_view_id.id, **kwargs)

    def get_customer_entity_view_infos(self, customer_id: CustomerId, page_size=100, page=0, **kwargs):
        return self.entity_view_controller.get_customer_entity_view_infos_using_get(customer_id.id, str(page_size), str(page), **kwargs)

    def get_entity_view_info_by_id(self, entity_view_id: EntityViewId, **kwargs):
        return self.entity_view_controller.get_entity_view_info_by_id_using_get(entity_view_id.id, **kwargs)

    def get_tenant_entity_view_infos(self, page_size=100, page=0, **kwargs):
        return self.entity_view_controller.get_tenant_entity_view_infos_using_get(str(page_size), str(page), **kwargs)

    def unassign_entity_view_from_customer(self, entity_view_id: EntityViewId, **kwargs):
        return self.entity_view_controller.unassign_entity_view_from_customer_using_delete(entity_view_id.id, **kwargs)

    def assign_asset_to_customer(self, customer_id: CustomerId, asset_id: AssetId, **kwargs):
        return self.asset_controller.assign_asset_to_customer_using_post(customer_id.id, asset_id.id, **kwargs)

    def assign_asset_to_public_customer(self, asset_id: AssetId, **kwargs):
        return self.asset_controller.assign_asset_to_public_customer_using_post(asset_id.id, **kwargs)

    def get_asset_info_by_id(self, asset_id: AssetId, **kwargs):
        return self.asset_controller.get_asset_info_by_id_using_get(asset_id.id, **kwargs)

    def get_customer_asset_infos(self, customer_id: CustomerId, page_size=100, page=0, **kwargs):
        return self.asset_controller.get_customer_asset_infos_using_get(customer_id.id, str(page_size), str(page), **kwargs)

    def get_tenant_asset_infos(self, page_size=100, page=0, **kwargs):
        return self.asset_controller.get_tenant_asset_infos_using_get(str(page_size), str(page), **kwargs)

    def unassign_asset_from_customer(self, asset_id: AssetId, **kwargs):
        return self.asset_controller.unassign_asset_from_customer_using_delete(asset_id.id, **kwargs)

    def find_by_from(self, from_id, from_type, relation_type=None, **kwargs):
        if relation_type is not None:
            return self.entity_relation_controller.find_by_from_using_get(from_id, from_type, relation_type, **kwargs)
        else:
            return self.entity_relation_controller.find_by_from_using_get1(from_id, from_type, **kwargs)

    def find_by_to(self, to_id, to_type, relation_type=None, **kwargs):
        if relation_type is not None:
            return self.entity_relation_controller.find_by_to_using_get(to_id, to_type, relation_type, **kwargs)
        else:
            return self.entity_relation_controller.find_by_to_using_get1(to_id, to_type, **kwargs)

    def assign_device_to_customer(self, customer_id: CustomerId, device_id: DeviceId, **kwargs):
        return self.device_controller.assign_device_to_customer_using_post(customer_id.id, device_id.id, **kwargs)

    def assign_device_to_public_customer(self, device_id: DeviceId, **kwargs):
        return self.device_controller.assign_device_to_public_customer_using_post(device_id.id, **kwargs)

    def get_customer_device_infos(self, customer_id: CustomerId, page_size=100, page=0, **kwargs):
        return self.device_controller.get_customer_device_infos_using_get(customer_id.id, str(page_size), str(page), **kwargs)

    def get_device_info_by_id(self, device_id: DeviceId, **kwargs):
        return self.device_controller.get_device_info_by_id_using_get(device_id.id, **kwargs)

    def get_tenant_device_infos(self, page_size=100, page=0, **kwargs):
        return self.device_controller.get_tenant_device_infos_using_get(str(page_size), str(page), **kwargs)

    def unassign_device_from_customer(self, device_id: DeviceId, **kwargs):
        return self.device_controller.unassign_device_from_customer_using_delete(device_id.id, **kwargs)
