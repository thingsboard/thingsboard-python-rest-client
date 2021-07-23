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

    """ Alarm endpoints """

    def get_all_alarms(self, page_size: int, page: int, text_search=None, sort_property=None, sort_order=None,
                       start_time=None, end_time=None, fetch_originator=None):
        return self.alarm_controller.get_all_alarms_using_get(page_size=str(page_size), page=str(page),
                                                              text_search=text_search, sort_property=sort_property,
                                                              sort_order=sort_order, start_time=start_time,
                                                              end_time=end_time, fetch_originator=fetch_originator)

    """ User endpoints """

    def save_user(self, user: User, send_activation_mail):
        return self.user_controller.save_user_using_post(user=user, send_activation_mail=send_activation_mail)

    """ Asset endpoints """

    def save_asset(self, asset: Asset):
        return self.asset_controller.save_asset_using_post(asset)

    def assign_asset_to_customer(self, customer_id: CustomerId, asset_id: AssetId):
        return self.asset_controller.assign_asset_to_customer_using_post(customer_id=customer_id, asset_id=asset_id)

    def unassign_asset_from_customer(self, asset_id: AssetId):
        return self.asset_controller.unassign_asset_from_customer_using_delete(asset_id=asset_id)

    def assign_asset_to_public_customer(self, asset_id: AssetId):
        return self.asset_controller.assign_asset_to_public_customer_using_post(asset_id=asset_id)

    def get_asset_info_by_id(self, asset_id: AssetId):
        asset_id = self.get_id(asset_id)
        return self.asset_controller.get_asset_info_by_id_using_get(asset_id)

    def get_customer_asset_infos(self, customer_id: CustomerId, page_size: int, page: int):
        customer_id = self.get_id(customer_id)
        return self.asset_controller.get_customer_asset_infos_using_get(customer_id, page_size=str(page_size),
                                                                        page=str(page))

    def unassign_asset_from_edge(self, edge_id: str, asset_id: AssetId):
        asset_id = self.get_id(asset_id)
        return self.asset_controller.unassign_asset_from_edge_using_delete(edge_id, asset_id)

    def assign_asset_to_edge(self, edge_id: str, asset_id: AssetId):
        asset_id = self.get_id(asset_id)
        return self.asset_controller.assign_asset_to_edge_using_post(edge_id, asset_id)

    def get_edge_assets(self, edge_id: str, page_size: int, page: int, type=None, text_search=None, sort_property=None,
                        sort_order=None, start_time=None, end_time=None):
        return self.asset_controller.get_edge_assets_using_get(edge_id=edge_id, page_size=str(page_size),
                                                               page=str(page), type=type, text_search=text_search,
                                                               sort_property=sort_property, sort_order=sort_order,
                                                               start_time=start_time, end_time=end_time)

    def get_tenant_asset_infos(self, page_size: int, page: int, type=None, text_search=None, sort_property=None,
                               sort_order=None):
        return self.asset_controller.get_tenant_asset_infos_using_get(page_size=str(page_size), page=str(page),
                                                                      type=type, text_search=text_search,
                                                                      sort_property=sort_property,
                                                                      sort_order=sort_order)

    """ Customer endpoints """

    def save_customer(self, customer: Customer):
        return self.customer_controller.save_customer_using_post(customer)

    """ Dashboard endpoints """

    def assign_dashboard_to_customer(self, customer_id: CustomerId, dashboard_id: DashboardId):
        return self.dashboard_controller.assign_dashboard_to_customer_using_post(customer_id=customer_id,
                                                                                 dashboard_id=dashboard_id)

    def unassign_dashboard_from_customer(self, customer_id: CustomerId, dashboard_id: DashboardId):
        return self.dashboard_controller.unassign_dashboard_from_customer_using_delete(customer_id=customer_id,
                                                                                       dashboard_id=dashboard_id)

    def update_dashboard_customers(self, dashboard_id: DashboardId, customerIds):
        return self.dashboard_controller.update_dashboard_customers_using_post(dashboard_id=dashboard_id,
                                                                               str_customer_ids=customerIds)

    def add_dashboard_customers(self, dashboard_id: DashboardId, customerIds):
        return self.dashboard_controller.add_dashboard_customers_using_post(dashboard_id=dashboard_id,
                                                                            str_customer_ids=customerIds)

    def remove_dashboard_customers(self, dashboard_id: DashboardId, customerIds):
        return self.dashboard_controller.remove_dashboard_customers_using_post(dashboard_id=dashboard_id,
                                                                               str_customer_ids=customerIds)

    def assign_dashboard_to_public_customer(self, dashboard_id: DashboardId):
        return self.dashboard_controller.assign_dashboard_to_public_customer_using_post(dashboard_id=dashboard_id)

    def unassign_dashboard_from_public_customer(self, dashboard_id: DashboardId):
        return self.dashboard_controller.unassign_dashboard_from_public_customer_using_delete(dashboard_id=dashboard_id)

    def save_dashboard(self, dashboard: Dashboard):
        return self.dashboard_controller.save_dashboard_using_post(dashboard)

    def get_customer_dashboards(self, customer_id: CustomerId, page_size: int, page: int, text_search=None,
                                sort_property=None, sort_order=None):
        return self.dashboard_controller.get_customer_dashboards_using_get(customer_id=customer_id,
                                                                           page_size=str(page_size), page=str(page),
                                                                           text_search=text_search,
                                                                           sort_property=sort_property,
                                                                           sort_order=sort_order)

    def get_home_dashboard_info(self):
        return self.dashboard_controller.get_home_dashboard_info_using_get()

    def unassign_dashboard_from_edge(self, edge_id: str, dashboard_id: DashboardId):
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.unassign_dashboard_from_edge_using_delete(edge_id=edge_id,
                                                                                   dashboard_id=dashboard_id)

    def assign_dashboard_to_edge(self, edge_id: str, dashboard_id: DashboardId):
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.assign_dashboard_to_edge_using_post(edge_id=edge_id, dashboard_id=dashboard_id)

    def get_edge_dashboards(self, edge_id: str, page_size: int, page: int, text_search=None, sort_property=None,
                            sort_order=None, start_time=None, end_time=None):
        return self.dashboard_controller.get_edge_dashboards_using_get(edge_id=edge_id, page_size=str(page_size),
                                                                       page=str(page), text_search=text_search,
                                                                       sort_property=sort_property,
                                                                       sort_order=sort_order, start_time=start_time,
                                                                       end_time=end_time)

    """ Device endpoints """

    def assign_device_to_customer(self, customer_id: CustomerId, device_id: DeviceId):
        return self.device_controller.assign_device_to_customer_using_post(customer_id=customer_id, device_id=device_id)

    def unassign_device_from_customer(self, customer_id: CustomerId, device_id: DeviceId):
        return self.device_controller.unassign_device_from_customer_using_delete(customer_id=customer_id,
                                                                                 device_id=device_id)

    def assign_device_to_public_customer(self, device_id: DeviceId):
        return self.device_controller.assign_device_to_public_customer_using_post(device_id=device_id)

    def get_customer_device_infos(self, customer_id: CustomerId, page_size: int, page: int, type=None, text_search=None,
                                  sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)

        return self.device_controller.get_customer_device_infos_using_get(customer_id=customer_id,
                                                                          page_size=str(page_size),
                                                                          page=str(page),
                                                                          type=type,
                                                                          text_search=text_search,
                                                                          sort_property=sort_property,
                                                                          sort_order=sort_order)

    def get_device_info_by_id(self, device_id: DeviceId):
        return self.device_controller.get_device_info_by_id_using_get(device_id=device_id.id)

    def count_by_device_profile_and_empty_ota_package(self, ota_package_type, device_profile_id):
        return self.device_controller.count_by_device_profile_and_empty_ota_package_using_get(
            ota_package_type=ota_package_type, device_profile_id=device_profile_id)

    def unassign_device_from_edge(self, edge_id, device_id):
        return self.device_controller.unassign_device_from_edge_using_delete(edge_id=edge_id, device_id=device_id)

    def assign_device_to_edge(self, edge_id, device_id):
        return self.device_controller.assign_device_to_edge_using_post(edge_id=edge_id, device_id=device_id)

    def get_edge_devices(self, edge_id, page_size: int, page: int, type=None, text_search=None, sort_property=None,
                         sort_order=None, start_time=None, end_time=None):
        return self.device_controller.get_edge_devices_using_get(edge_id=edge_id, page_size=str(page_size),
                                                                 page=str(page), type=type, text_search=text_search,
                                                                 sort_property=sort_property, sort_order=sort_order,
                                                                 start_time=start_time, end_time=end_time)

    def get_tenant_device_infos(self, page_size: int, page: int, type=None, device_profile_id=None, text_search=None,
                                sort_property=None, sort_order=None):
        return self.device_controller.get_tenant_device_infos_using_get(page_size=str(page_size),
                                                                        page=str(page), type=type,
                                                                        device_profile_id=device_profile_id,
                                                                        text_search=text_search,
                                                                        sort_property=sort_property,
                                                                        sort_order=sort_order)

    """ Edge endpoints """

    def unassign_edge_from_customer(self, edge_id: EdgeId):
        edge_id = self.get_id(edge_id)
        return self.edge_controller.unassign_edge_from_customer_using_delete(edge_id=edge_id)

    def assign_edge_to_public_customer(self, edge_id: EdgeId):
        edge_id = self.get_id(edge_id)
        return self.edge_controller.assign_edge_to_public_customer_using_post(edge_id=edge_id)

    def assign_edge_to_customer(self, customer_id: CustomerId, edge_id: EdgeId):
        customer_id = self.get_id(customer_id)
        edge_id = self.get_id(edge_id)
        return self.edge_controller.edge_controllerassign_edge_to_customer_using_post(customer_id=customer_id,
                                                                                      edge_id=edge_id)

    def get_customer_edge_infos(self, customer_id: CustomerId, page_size: int, page: int, type=None, text_search=None,
                                sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
        return self.edge_controller.get_customer_edge_infos_using_get(customer_id=customer_id, page_size=str(page_size),
                                                                      page=str(page), type=type,
                                                                      text_search=text_search,
                                                                      sort_property=sort_property,
                                                                      sort_order=sort_order)

    def get_customer_edges(self, customer_id: CustomerId, page_size: int, page: int, type=None, text_search=None,
                           sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
        return self.edge_controller.get_customer_edges_using_get(customer_id=customer_id, page_size=str(page_size),
                                                                 page=str(page), type=type, text_search=text_search,
                                                                 sort_property=sort_property, sort_order=sort_order)

    def save_edge(self, edge: Edge):
        return self.edge_controller.save_edge_using_post(edge=edge)

    def get_edge_info_by_id(self, edge_id: EdgeId):
        edge_id = self.get_id(edge_id)
        return self.edge_controller.get_edge_info_by_id_using_get(edge_id=edge_id)

    def find_missing_to_related_rule_chains(self, edge_id: EdgeId):
        edge_id = self.get_id(edge_id)
        return self.edge_controller.find_missing_to_related_rule_chains_using_get(edge_id=edge_id)

    def sync_edge(self, edge_id: EdgeId):
        edge_id = self.get_id(edge_id)
        return self.edge_controller.sync_edge_using_post(edge_id=edge_id)

    def get_edge_types(self):
        return self.edge_controller.get_edge_types_using_get()

    def delete_edge(self, edge_id: EdgeId):
        return self.edge_controller.delete_edge_using_delete(edge_id=edge_id)

    def get_edge_by_id(self, edge_id: EdgeId):
        edge_id = self.get_id(edge_id)
        return self.edge_controller.get_edge_by_id_using_get(edge_id=edge_id)

    def set_root_rule_chain(self, edge_id: EdgeId, rule_chain_id: RuleChainId):
        edge_id = self.get_id(edge_id)
        rule_chain_id = self.get_id(rule_chain_id)
        return self.edge_controller.set_root_rule_chain_using_post(edge_id=edge_id, rule_chain_id=rule_chain_id)

    def find_by_query_edge(self, query):
        return self.edge_controller.find_by_query_using_post2(query=query)

    def is_edges_support_enabled(self):
        return self.edge_controller.is_edges_support_enabled_using_get()

    def get_edges_by_ids(self, edge_ids):
        return self.edge_controller.get_edges_by_ids_using_get(edge_ids=edge_ids)

    def get_edges(self, page_size: int, page: int, text_search=None, sort_property=None, sort_order=None):
        return self.edge_controller.get_edges_using_get(page_size=str(page_size), page=str(page),
                                                        text_search=text_search, sort_property=sort_property,
                                                        sort_order=sort_order)

    def activate_instance(self, license_secret, release_date):
        return self.edge_controller.activate_instance_using_post(license_secret=license_secret,
                                                                 release_date=release_date)

    def check_instance(self, request):
        return self.edge_controller.check_instance_using_post(request=request)

    def get_tenant_edge_infos(self, page_size: int, page: int, type=None, text_search=None, sort_property=None,
                              sort_order=None):
        return self.edge_controller.get_tenant_edge_infos_using_get(page_size=str(page_size), page=str(page), type=type,
                                                                    text_search=text_search,
                                                                    sort_property=sort_property, sort_order=sort_order)

    def get_tenant_edge(self, edge_name: str):
        return self.edge_controller.get_tenant_edge_using_get(edge_name=edge_name)

    def get_tenant_edges(self, page_size: int, page: int, type=None, text_search=None, sort_property=None,
                         sort_order=None):
        return self.edge_controller.get_tenant_edges_using_get(page_size=str(page_size), page=str(page), type=type,
                                                               text_search=text_search,
                                                               sort_property=sort_property, sort_order=sort_order)

    """ Edge event endpoints"""

    def get_edge_events(self, edge_id: EdgeId, page_size: int, page: int, text_search=None, sort_property=None,
                        sort_order=None, start_time=None, end_time=None):
        edge_id = self.get_id(edge_id)
        return self.edge_event_controller.get_edge_events_using_get(edge_id=edge_id, page_size=str(page_size),
                                                                    page=str(page), text_search=text_search,
                                                                    sort_property=sort_property, sort_order=sort_order,
                                                                    start_time=start_time, end_time=end_time)

    """ Entity View endpoints """

    def assign_entity_view_to_customer(self, customer_id: CustomerId, entity_view_id: EntityViewId):
        return self.entity_view_controller.assign_entity_view_to_customer_using_post(customer_id=customer_id,
                                                                                     entity_view_id=entity_view_id)

    def unassign_entity_view_from_customer(self, customer_id: CustomerId, entity_view_id: EntityViewId):
        return self.entity_view_controller.unassign_entity_view_from_customer_using_delete(customer_id=customer_id,
                                                                                           entity_view_id=entity_view_id)

    def assign_entity_view_to_public_customer(self, entity_view_id: EntityViewId):
        return self.entity_view_controller.assign_entity_view_to_public_customer_using_post(
            entity_view_id=entity_view_id)

    def get_customer_entity_view_infos(self, customer_id: CusomerId, page_size: int, page: int, type=None,
                                       text_search=None, sort_property=None, sort_order=None):
        return self.entity_view_controller.get_customer_entity_view_infos_using_get(customer_id=customer_id,
                                                                                    page_size=str(page_size),
                                                                                    page=str(page), type=type,
                                                                                    text_search=text_search,
                                                                                    sort_property=sort_property,
                                                                                    sort_order=sort_order)

    def unassign_entity_view_from_edge(self, edge_id: str, entity_view_id: EntityViewId):
        return self.entity_view_controller.unassign_entity_view_from_edge_using_delete(edge_id=edge_id,
                                                                                       entity_view_id=entity_view_id)

    def assign_entity_view_to_edge(self, edge_id: str, entity_view_id: EntityViewId):
        return self.entity_view_controller.assign_entity_view_to_edge_using_post(edge_id=edge_id,
                                                                                 entity_view_id=entity_view_id)

    def get_edge_entity_views(self, edge_id: str, page_size: int, page: int, type=None, text_search=None,
                              sort_property=None, sort_order=None, start_time=None, end_time=None):
        return self.entity_view_controller.get_edge_entity_views_using_get(edge_id=edge_id, page_size=str(page_size),
                                                                           page=str(page), type=type,
                                                                           text_search=text_search,
                                                                           sort_property=sort_property,
                                                                           sort_order=sort_order, start_time=start_time,
                                                                           end_time=end_time)

    def save_entity_view(self, entity_view: EntityView):
        return self.entity_view_controller.save_entity_view_using_post(entity_view=entity_view)

    def get_entity_view_info_by_id(self, entity_view_id: EntityViewId):
        return self.entity_view_controller.get_entity_view_info_by_id_using_get(entity_view_id=entity_view_id)

    def get_tenant_entity_view_infos(self, page_size: int, page: int, type=None, text_search=None, sort_property=None,
                                     sort_order=None):
        return self.entity_view_controller.get_tenant_entity_view_infos_using_get(page_size=str(page_size),
                                                                                  page=str(page), type=type,
                                                                                  text_search=text_search,
                                                                                  sort_property=sort_property,
                                                                                  sort_order=sort_order)

    """ Lwm 2m endpoints """

    def save_device_with_credentials(self, device_with_device_credentials):
        return self.lwm_2m_controller.save_device_with_credentials_using_post(
            device_with_device_credentials=device_with_device_credentials)

    def get_lwm2m_bootstrap_security_info(self, is_bootstrap_server: bool):
        return self.lwm_2m_controller.get_lwm2m_bootstrap_security_info_using_get(
            is_bootstrap_server=str(is_bootstrap_server))

    """ OTA package endpoints """

    def save_ota_package_info(self, ota_package_info: OtaPackageInfo):
        return self.ota_package_controller.save_ota_package_info_using_post(ota_package_info=ota_package_info)

    def get_ota_package_info_by_id(self, ota_package_id: OtaPackageId):
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.get_ota_package_info_by_id_using_get(ota_package_id=ota_package_id)

    def delete_ota_package(self, ota_package_id: OtaPackageId):
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.delete_ota_package_using_delete(ota_package_id=ota_package_id)

    def get_ota_package_by_id(self, ota_package_id: OtaPackageId):
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.get_ota_package_by_id_using_get(ota_package_id=ota_package_id)

    def download_ota_package(self, ota_package_id: OtaPackageId):
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.download_ota_package_using_get(ota_package_id=ota_package_id)

    def save_ota_package_data(self, ota_package_id: OtaPackageId, checksum_algorithm: str, file: File, checksum=None):
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.save_ota_package_data_using_post(ota_package_id=ota_package_id,
                                                                            checksum_algorithm=checksum_algorithm,
                                                                            file=file, checksum=checksum)

    def get_ota_packages(self, page_size: int, page: int, type=None, device_profile_id=None, text_search=None,
                         sort_property=None, sort_order=None):
        if device_profile_id is not None and type is not None:
            device_profile_id = self.get_id(device_profile_id)
            return self.ota_package_controller.get_ota_packages_using_get(device_profile_id=device_profile_id,
                                                                          type=type,
                                                                          page_size=str(page_size), page=str(page),
                                                                          text_search=text_search,
                                                                          sort_property=sort_property,
                                                                          sort_order=sort_order)

        return self.ota_package_controller.get_ota_packages_using_get1(page_size=str(page_size), page=str(page),
                                                                       text_search=text_search,
                                                                       sort_property=sort_property,
                                                                       sort_order=sort_order)

    """ TB resource endpoints """

    def save_resource(self, resource: Resource):
        return self.tb_resource_controller.save_resource_using_post(resource=resource)

    def get_resource_info_by_id(self, resource_id: ResourceId):
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.get_resource_info_by_id_using_get(resource_id=resource_id)

    def get_lwm2m_list_objects_page(self, page_size: int, page: int, text_search=None, sort_property=None,
                                    sort_order=None):
        return self.tb_resource_controller.get_lwm2m_list_objects_page_using_get(page_size=str(page_size),
                                                                                 page=str(page),
                                                                                 text_search=text_search,
                                                                                 sort_property=sort_property,
                                                                                 sort_order=sort_order)

    def get_lwm2m_list_objects(self, sort_order: str, sort_property: str, object_ids=None):
        return self.tb_resource_controller.get_lwm2m_list_objects_page_using_get(sort_order=sort_order,
                                                                                 sort_property=sort_property,
                                                                                 object_ids=object_ids)

    def delete_resource(self, resource_id: ResourceId):
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.delete_resource_using_delete1(resource_id=resource_id)

    def get_resource_by_id(self, resource_id: ResourceId):
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.get_resource_by_id_using_get(resource_id=resource_id)

    def download_resource(self, resource_id: ResourceId):
        resource_id = self.get_id(resource_id)
        return self.tb_resource_controller.download_resource_using_get(resource_id=resource_id)

    def get_resources(self, page_size: int, page: int, text_search=None, sort_property=None, sort_order=None):
        return self.tb_resource_controller.get_resources_using_get(page_size=str(page_size), page=str(page),
                                                                   text_search=text_search, sort_property=sort_property,
                                                                   sort_order=sort_order)

    """ RPC endpoints """

    def get_persisted_rpc(self, rpc_id: str):
        return self.rpc_controller.get_persisted_rpc_using_get(rpc_id=rpc_id)

    def delete_resource(self, rpc_id: str):
        return self.rpc_controller.delete_resource_using_delete(rpc_id=rpc_id)

    def get_persisted_rpc_by_device(self, device_id: DeviceId, page_size: int, page: int, rpc_status: str,
                                    text_search=None, sort_property=None, sort_order=None):
        device_id = self.get_id(device_id)
        return self.rpc_controller.get_persisted_rpc_by_device_using_get(device_id=device_id, page_size=str(page_size),
                                                                         page=str(page), rpc_status=rpc_status,
                                                                         text_search=text_search,
                                                                         sort_property=sort_property,
                                                                         sort_order=sort_order)

    """ Rule chain endpoints """

    def unassign_rule_chain_from_edge(self, edge_id: str, rule_chain_id: RuleChainId):
        return self.rule_chain_controller.unassign_rule_chain_from_edge_using_delete(edge_id=edge_id,
                                                                                     rule_chain_id=rule_chain_id)

    def assign_rule_chain_to_edge(self, edge_id: str, rule_chain_id: RuleChainId):
        return self.rule_chain_controller.assign_rule_chain_to_edge_using_post(edge_id=edge_id,
                                                                               rule_chain_id=rule_chain_id)

    def get_edge_rule_chains(self, edge_id: str, page_size: int, page: int, text_search=None, sort_property=None,
                             sort_order=None):
        return self.rule_chain_controller.get_edge_rule_chains_using_get(edge_id=edge_id, page_size=str(page_size),
                                                                         page=str(page), text_search=text_search,
                                                                         sort_property=sort_property,
                                                                         sort_order=sort_order)

    def get_auto_assign_to_edge_rule_chains_using_get(self):
        return self.rule_chain_controller.get_auto_assign_to_edge_rule_chains_using_get()

    def unset_auto_assign_to_edge_rule_chain(self, rule_chain_id: RuleChainId):
        return self.rule_chain_controller.unset_auto_assign_to_edge_rule_chain_using_delete(rule_chain_id=rule_chain_id)

    def set_auto_assign_to_edge_rule_chain(self, rule_chain_id: RuleChainId):
        return self.rule_chain_controller.set_auto_assign_to_edge_rule_chain_using_post(rule_chain_id=rule_chain_id)

    def set_edge_template_root_rule_chain(self, rule_chain_id: RuleChainId):
        return self.rule_chain_controller.set_edge_template_root_rule_chain_using_post(rule_chain_id=rule_chain_id)
