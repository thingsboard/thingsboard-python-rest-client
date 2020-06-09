import logging
from requests import post
from json import load, dumps, loads
import tb_rest_client
from tb_rest_client.rest import ApiException


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# ThingsBoard REST API URL
url = "http://127.0.0.1:8080"

# Default Tenant Administrator credentials
username = "tenant@thingsboard.org"
password = "tenant"

# Request for authorization token
token_json = post(url+"/api/auth/login", json={"username": username, "password": password}).json()
token = None
if isinstance(token_json, dict) and token_json.get("token") is not None:
    token = token_json["token"]

configuration = tb_rest_client.Configuration()
configuration.host = url
configuration.api_key_prefix["X-Authorization"] = "Bearer"
configuration.api_key["X-Authorization"] = token

# Creating API client
api_client = tb_rest_client.ApiClient(configuration)

auth_controller = tb_rest_client.AuthControllerApi(api_client)
current_user = auth_controller.get_user_using_get()

try:
    # Creating Dashboard Group on the Tenant Level
    entity_group_controller = tb_rest_client.EntityGroupControllerApi(api_client)
    shared_dashboards_group = tb_rest_client.EntityGroup(name="Shared Dashboards", type="DASHBOARD")
    shared_dashboards_group = entity_group_controller.save_entity_group_using_post(shared_dashboards_group)

    # Loading Dashboard from file
    dashboard_json = None
    dashboard_controller = tb_rest_client.DashboardControllerApi(api_client)
    with open("watermeters.json", "r") as dashboard_file:
        dashboard_json = load(dashboard_file)
    dashboard = tb_rest_client.Dashboard(title=dashboard_json["title"], configuration=dashboard_json["configuration"])
    dashboard = dashboard_controller.save_dashboard_using_post(dashboard)

    # Adding Dashboard to the Shared Dashboards Group
    entity_group_controller.add_entities_to_entity_group_using_post(shared_dashboards_group.id, [dashboard.id.id])

    # Creating Customer 1
    customer_controller = tb_rest_client.CustomerControllerApi(api_client)
    customer1 = tb_rest_client.Customer(title="Customer 1")
    customer1 = customer_controller.save_customer_using_post(customer1)

    # Creating Device
    device_controller = tb_rest_client.DeviceControllerApi(api_client)
    device = tb_rest_client.Device(name="WaterMeter1", type="waterMeter")
    device = device_controller.save_device_using_post(device)

    # Fetching automatically created "Customer Administrators" Group.
    customer1_administrators = entity_group_controller.get_enitity_group_by_owner_and_name_and_type_using_get(customer1.id.entity_type, customer1.id.id, "USER", "Customer Administrators")

    # Creating Read-Only Role
    role_controller = tb_rest_client.RoleControllerApi(api_client)
    read_only_role = tb_rest_client.Role(name="Read-Only", permissions=['READ', 'READ_ATTRIBUTES', 'READ_TELEMETRY', 'READ_CREDENTIALS'], type="GROUP")
    read_only_role = role_controller.save_role_using_post(read_only_role)

    # Assigning Shared Dashboards to the Customer 1 Administrators
    group_permissions_controller = tb_rest_client.GroupPermissionControllerApi(api_client)
    tenant_controller = tb_rest_client.TenantControllerApi(api_client)
    tenant_id = current_user.tenant_id
    group_permission = tb_rest_client.GroupPermission(role_id=read_only_role.id,
                                                      name="Read Only Permission",
                                                      is_public=False,
                                                      user_group_id=customer1_administrators.id,
                                                      tenant_id=tenant_id,
                                                      entity_group_id=shared_dashboards_group.id,
                                                      entity_group_type=shared_dashboards_group.type)
    group_permission = group_permissions_controller.save_group_permission_using_post(group_permission)

    # Creating User for Customer 1 with default dashboard from Tenant "Shared Dashboards" group.
    user_email = "user@thingsboard.org"
    user_password = "secret"

    user_controller = tb_rest_client.UserControllerApi(api_client)
    additional_info = {
        "defaultDashboardId": dashboard.id.id,
        "defaultDashboardFullscreen": False
    }
    user = tb_rest_client.User(authority="CUSTOMER_USER",
                               customer_id=customer1.id,
                               email=user_email,
                               additional_info=additional_info)
    user = user_controller.save_user_using_post(user, send_activation_mail=False)
    activate_token = user_controller.get_activation_token_using_get(user.id.id).replace("'", '"')
    activation_request = {"activateToken": activate_token,
                          "password": user_password}

    auth_controller.activate_user_using_post(activate_request=activation_request, send_activation_mail=False)
    entity_group_controller.add_entities_to_entity_group_using_post(customer1_administrators.id, [user.id.id])

except ApiException as e:
    logging.exception(e)
