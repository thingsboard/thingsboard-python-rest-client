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

from tb_rest_client.rest_client_base import *

logger = getLogger(__name__)


class RestClientCE(RestClientBase):
    def __init__(self, base_url):
        super().__init__(base_url)

    """ Asset endpoints """

    def assign_asset_to_customer(self, customer_id: CustomerId, asset_id: AssetId):
        return self.asset_controller.assign_asset_to_customer_using_post(customer_id=customer_id, asset_id=asset_id)

    def unassign_asset_from_customer(self, asset_id: AssetId):
        return self.asset_controller.unassign_asset_from_customer_using_delete(asset_id=asset_id)

    def assign_asset_to_public_customer(self, asset_id: AssetId):
        return self.asset_controller.assign_asset_to_public_customer_using_post(asset_id=asset_id)

    """ Dashboard endpoints """

    def assign_dashboard_to_customer(self, customer_id: CustomerId, dashboard_id: DashboardId):
        return self.dashboard_controller.assign_dashboard_to_customer_using_post(customer_id=customer_id, dashboard_id=dashboard_id)

    def unassign_dashboard_from_customer(self, customer_id: CustomerId, dashboard_id: DashboardId):
        return self.dashboard_controller.unassign_dashboard_from_customer_using_delete(customer_id=customer_id, dashboard_id=dashboard_id)

    def update_dashboard_customers(self, dashboard_id: DashboardId, customerIds):
        return self.dashboard_controller.update_dashboard_customers_using_post(dashboard_id=dashboard_id, str_customer_ids=customerIds)

    def add_dashboard_customers(self, dashboard_id: DashboardId, customerIds):
        return self.dashboard_controller.add_dashboard_customers_using_post(dashboard_id=dashboard_id, str_customer_ids=customerIds)

    def remove_dashboard_customers(self, dashboard_id: DashboardId, customerIds):
        return self.dashboard_controller.remove_dashboard_customers_using_post(dashboard_id=dashboard_id, str_customer_ids=customerIds)

    def assign_dashboard_to_public_customer(self, dashboard_id: DashboardId):
        return self.dashboard_controller.assign_dashboard_to_public_customer_using_post(dashboard_id=dashboard_id)

    def unassign_dashboard_from_public_customer(self, dashboard_id: DashboardId):
        return self.dashboard_controller.unassign_dashboard_from_public_customer_using_delete(dashboard_id=dashboard_id)

    """ Device endpoints """

    def assign_device_to_customer(self, customer_id: CustomerId, device_id: DeviceId):
        return self.device_controller.assign_device_to_customer_using_post(customer_id=customer_id, device_id=device_id)

    def unassign_device_from_customer(self, customer_id: CustomerId, device_id: DeviceId):
        return self.device_controller.unassign_device_from_customer_using_delete(customer_id=customer_id, device_id=device_id)

    def assign_device_to_public_customer(self, device_id: DeviceId):
        return self.device_controller.assign_device_to_public_customer_using_post(device_id=device_id)

    """ Entity View endpoints """

    def assign_entity_view_to_customer(self, customer_id: CustomerId, entity_view_id: EntityViewId):
        return self.entity_view_controller.assign_entity_view_to_customer_using_post(customer_id=customer_id, entity_view_id=entity_view_id)

    def unassign_entity_view_from_customer(self, customer_id: CustomerId, entity_view_id: EntityViewId):
        return self.entity_view_controller.unassign_entity_view_from_customer_using_delete(customer_id=customer_id, entity_view_id=entity_view_id)

    def assign_entity_view_to_public_customer(self, entity_view_id: EntityViewId):
        return self.entity_view_controller.assign_entity_view_to_public_customer_using_post(entity_view_id=entity_view_id)
