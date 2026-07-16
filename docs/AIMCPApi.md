# docspace_api_sdk.MCPApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_room_servers**](#add_room_servers) | **POST** /api/2.0/ai/rooms/{roomId}/servers | Assign MCP servers to a room
[**add_server**](#add_server) | **POST** /api/2.0/ai/servers | Register a custom MCP server
[**connect_server**](#connect_server) | **POST** /api/2.0/ai/rooms/{roomId}/servers/{serverId}/connect | Connect an OAuth-based MCP server in a room
[**delete_room_servers**](#delete_room_servers) | **DELETE** /api/2.0/ai/rooms/{roomId}/servers | Remove MCP servers from a room
[**delete_server**](#delete_server) | **DELETE** /api/2.0/ai/servers | Delete MCP servers
[**disconnect_server**](#disconnect_server) | **POST** /api/2.0/ai/rooms/{roomId}/servers/{serverId}/disconnect | Disconnect an MCP server in a room
[**get_available_servers**](#get_available_servers) | **GET** /api/2.0/ai/servers/available | Get available MCP servers
[**get_room_servers**](#get_room_servers) | **GET** /api/2.0/ai/rooms/{roomId}/servers | Get MCP servers assigned to a room
[**get_server**](#get_server) | **GET** /api/2.0/ai/servers/{id} | Get an MCP server by ID
[**get_servers**](#get_servers) | **GET** /api/2.0/ai/servers | Get all MCP servers
[**get_tools**](#get_tools) | **GET** /api/2.0/ai/rooms/{roomId}/servers/{serverId}/tools | Get MCP server tools in a room
[**set_server_status**](#set_server_status) | **PUT** /api/2.0/ai/servers/{id}/status | Enable or disable an MCP server
[**set_tools**](#set_tools) | **PUT** /api/2.0/ai/rooms/{roomId}/servers/{serverId}/tools | Configure MCP server tools in a room
[**update_server**](#update_server) | **PUT** /api/2.0/ai/servers/{id} | Update a custom MCP server


# **add_room_servers**
> McpServerStatusArrayWrapper add_room_servers(room_id, add_room_servers_request_body)

Associates one or more MCP servers with a specific room, making them available for AI chat sessions
within that room. A maximum of 5 MCP servers can be assigned to a single room. If OAuth-based servers
are included, each room member will need to individually authorize their connection.
Requires room edit permissions.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **int**| Identifier of the room to which MCP servers will be assigned. | 
 **add_room_servers_request_body** | [**AddRoomServersRequestBody**](AddRoomServersRequestBody.md)| Server identifiers to assign. | 

### Return type

[**McpServerStatusArrayWrapper**](McpServerStatusArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.add_room_servers_request_body import AddRoomServersRequestBody
from docspace_api_sdk.models.mcp_server_status_array_wrapper import McpServerStatusArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.MCPApi(api_client)
    room_id = 42 # int | Identifier of the room to which MCP servers will be assigned.
    add_room_servers_request_body = docspace_api_sdk.AddRoomServersRequestBody() # AddRoomServersRequestBody | Server identifiers to assign.

    try:
        # Assign MCP servers to a room
        api_response = api_instance.add_room_servers(room_id, add_room_servers_request_body)
        print("The response of MCPApi->add_room_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->add_room_servers: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of MCP server statuses after assignment |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The maximum number of servers per room has been exceeded |  -  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | The room with the specified ID was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_server**
> McpServerWrapper add_server(add_mcp_server_request_body)

Registers a new custom MCP (Model Context Protocol) server for the current tenant.
The system validates the server name (only letters, numbers, underscores, and hyphens are allowed),
checks that it is not reserved or already taken, and then attempts to connect to the provided endpoint
to verify reachability and credentials before persisting the configuration.
Requires DocSpace administrator privileges.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_mcp_server_request_body** | [**AddMcpServerRequestBody**](AddMcpServerRequestBody.md)| MCP server registration parameters. | 

### Return type

[**McpServerWrapper**](McpServerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.add_mcp_server_request_body import AddMcpServerRequestBody
from docspace_api_sdk.models.mcp_server_wrapper import McpServerWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.MCPApi(api_client)
    add_mcp_server_request_body = docspace_api_sdk.AddMcpServerRequestBody() # AddMcpServerRequestBody | MCP server registration parameters.

    try:
        # Register a custom MCP server
        api_response = api_instance.add_server(add_mcp_server_request_body)
        print("The response of MCPApi->add_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->add_server: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newly registered MCP server configuration |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Invalid server name, reserved name, duplicate name, incorrect credentials, or invalid endpoint URL |  -  |
**403** | You don't have permission to manage MCP servers |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect_server**
> McpServerStatusWrapper connect_server(room_id, server_id, connect_server_request_body)

Completes the OAuth authorization flow for an MCP server within a specific room on behalf of the
current user. The authorization code obtained from the OAuth provider must be passed in the request body.
Upon successful token exchange, the system verifies connectivity to the server and stores
the credentials for the current user. Requires room edit permissions.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **int**| Identifier of the room containing the MCP server. | 
 **server_id** | **UUID**| Unique identifier of the MCP server to connect. | 
 **connect_server_request_body** | [**ConnectServerRequestBody**](ConnectServerRequestBody.md)| The request body containing additional data necessary for connecting to the server,  such as authentication or operation-specific information. | 

### Return type

[**McpServerStatusWrapper**](McpServerStatusWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.connect_server_request_body import ConnectServerRequestBody
from docspace_api_sdk.models.mcp_server_status_wrapper import McpServerStatusWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.MCPApi(api_client)
    room_id = 42 # int | Identifier of the room containing the MCP server.
    server_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Unique identifier of the MCP server to connect.
    connect_server_request_body = docspace_api_sdk.ConnectServerRequestBody() # ConnectServerRequestBody | The request body containing additional data necessary for connecting to the server,  such as authentication or operation-specific information.

    try:
        # Connect an OAuth-based MCP server in a room
        api_response = api_instance.connect_server(room_id, server_id, connect_server_request_body)
        print("The response of MCPApi->connect_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->connect_server: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MCP server connection status after authorization |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The provided authorization code is invalid |  -  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | The room or MCP server connection was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_room_servers**
> delete_room_servers(room_id, delete_room_servers_request_body)

Detaches one or more MCP servers from the specified room. After removal, the servers will no longer
be available in AI chat sessions within this room. Existing connections and tool configurations for
the removed servers are also cleaned up. Requires room edit permissions.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **int**| Identifier of the room from which MCP servers will be removed. | 
 **delete_room_servers_request_body** | [**DeleteRoomServersRequestBody**](DeleteRoomServersRequestBody.md)| Server identifiers to remove. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.delete_room_servers_request_body import DeleteRoomServersRequestBody
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.MCPApi(api_client)
    room_id = 42 # int | Identifier of the room from which MCP servers will be removed.
    delete_room_servers_request_body = docspace_api_sdk.DeleteRoomServersRequestBody() # DeleteRoomServersRequestBody | Server identifiers to remove.

    try:
        # Remove MCP servers from a room
        api_instance.delete_room_servers(room_id, delete_room_servers_request_body)
    except Exception as e:
        print("Exception when calling MCPApi->delete_room_servers: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | MCP servers were successfully removed from the room |  -  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | The room with the specified ID was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_server**
> delete_server(delete_servers_request_body)

Permanently removes one or more MCP servers from the current tenant by their IDs.
All room associations and connection data for the deleted servers are also cleaned up.
This action is irreversible. Requires DocSpace administrator privileges.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_servers_request_body** | [**DeleteServersRequestBody**](DeleteServersRequestBody.md)| Server identifiers to delete. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.delete_servers_request_body import DeleteServersRequestBody
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.MCPApi(api_client)
    delete_servers_request_body = docspace_api_sdk.DeleteServersRequestBody() # DeleteServersRequestBody | Server identifiers to delete.

    try:
        # Delete MCP servers
        api_instance.delete_server(delete_servers_request_body)
    except Exception as e:
        print("Exception when calling MCPApi->delete_server: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | MCP servers were successfully deleted |  -  |
**403** | You don't have permission to manage MCP servers |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disconnect_server**
> McpServerStatusWrapper disconnect_server(room_id, server_id)

Revokes the current user's OAuth connection to an MCP server within the specified room. After
disconnection, the server's tools will no longer be available to this user in AI chat sessions
until they re-authorize. Other room members' connections are not affected.
Requires room edit permissions.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **int**| Identifier of the room containing the MCP server. | 
 **server_id** | **UUID**| Unique identifier of the MCP server to disconnect from. | 

### Return type

[**McpServerStatusWrapper**](McpServerStatusWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.mcp_server_status_wrapper import McpServerStatusWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.MCPApi(api_client)
    room_id = 42 # int | Identifier of the room containing the MCP server.
    server_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Unique identifier of the MCP server to disconnect from.

    try:
        # Disconnect an MCP server in a room
        api_response = api_instance.disconnect_server(room_id, server_id)
        print("The response of MCPApi->disconnect_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->disconnect_server: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MCP server connection status after disconnection |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | The room or MCP server connection was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_servers**
> McpServerShortArrayWrapper get_available_servers(start_index=start_index, count=count)

Returns a paginated list of MCP servers that are currently active (enabled) and available for
assignment to rooms. Only servers in the enabled state are included. Each entry contains a compact
summary with the server name, type, icon, and status. Supports pagination via startIndex and count.
The total count of available servers is included in the response metadata.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_index** | **int**| The number of items to skip before returning results (zero-based offset). Defaults to 0. | [optional] 
 **count** | **int**| The maximum number of items to return per page. Defaults to 100. | [optional] 

### Return type

[**McpServerShortArrayWrapper**](McpServerShortArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.mcp_server_short_array_wrapper import McpServerShortArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.MCPApi(api_client)
    start_index = 0 # int | The number of items to skip before returning results (zero-based offset). Defaults to 0. (optional)
    count = 100 # int | The maximum number of items to return per page. Defaults to 100. (optional)

    try:
        # Get available MCP servers
        api_response = api_instance.get_available_servers(start_index=start_index, count=count)
        print("The response of MCPApi->get_available_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->get_available_servers: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of active MCP servers available for room assignment |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_room_servers**
> McpServerStatusArrayWrapper get_room_servers(room_id)

Returns the list of MCP servers currently assigned to the specified room along with their connection
statuses for the current user. For OAuth-based servers, the connection status reflects whether the
current user has completed authorization. Requires access to the room's AI chat.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **int**| Identifier of the room whose assigned MCP servers are being retrieved. | 

### Return type

[**McpServerStatusArrayWrapper**](McpServerStatusArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.mcp_server_status_array_wrapper import McpServerStatusArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.MCPApi(api_client)
    room_id = 42 # int | Identifier of the room whose assigned MCP servers are being retrieved.

    try:
        # Get MCP servers assigned to a room
        api_response = api_instance.get_room_servers(room_id)
        print("The response of MCPApi->get_room_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->get_room_servers: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of MCP server statuses in the room |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | The room with the specified ID was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server**
> McpServerShortWrapper get_server(id)

Retrieves a summary view of a single MCP server by its unique identifier, including its name,
type, enabled state, and icon. This endpoint returns a compact representation without
sensitive details such as endpoint URL or authentication headers.
Requires DocSpace administrator privileges.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique identifier of the MCP server to retrieve. | 

### Return type

[**McpServerShortWrapper**](McpServerShortWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.mcp_server_short_wrapper import McpServerShortWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.MCPApi(api_client)
    id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Unique identifier of the MCP server to retrieve.

    try:
        # Get an MCP server by ID
        api_response = api_instance.get_server(id)
        print("The response of MCPApi->get_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->get_server: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MCP server summary information |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have permission to manage MCP servers |  -  |
**404** | The MCP server with the specified ID was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_servers**
> McpServerArrayWrapper get_servers(start_index=start_index, count=count)

Returns a paginated list of all MCP servers registered for the current tenant, including both
enabled and disabled servers. Each entry contains the full configuration (endpoint, headers,
icon, type, and status). Supports pagination via the startIndex and count query parameters.
The total number of servers is included in the response metadata.
Requires DocSpace administrator privileges.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_index** | **int**| The number of items to skip before returning results (zero-based offset). Defaults to 0. | [optional] 
 **count** | **int**| The maximum number of items to return per page. Defaults to 100. | [optional] 

### Return type

[**McpServerArrayWrapper**](McpServerArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.mcp_server_array_wrapper import McpServerArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.MCPApi(api_client)
    start_index = 0 # int | The number of items to skip before returning results (zero-based offset). Defaults to 0. (optional)
    count = 100 # int | The maximum number of items to return per page. Defaults to 100. (optional)

    try:
        # Get all MCP servers
        api_response = api_instance.get_servers(start_index=start_index, count=count)
        print("The response of MCPApi->get_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->get_servers: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of all registered MCP servers |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have permission to manage MCP servers |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tools**
> McpToolArrayWrapper get_tools(room_id, server_id)

Retrieves the full list of tools exposed by an MCP server within the context of a specific room,
along with each tool's enabled or disabled state. Disabled tools will not be invoked during
AI chat sessions in this room. Requires access to the room's AI chat.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **int**| Identifier of the room containing the MCP server. | 
 **server_id** | **UUID**| Unique identifier of the MCP server whose tools are being retrieved. | 

### Return type

[**McpToolArrayWrapper**](McpToolArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.mcp_tool_array_wrapper import McpToolArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.MCPApi(api_client)
    room_id = 42 # int | Identifier of the room containing the MCP server.
    server_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Unique identifier of the MCP server whose tools are being retrieved.

    try:
        # Get MCP server tools in a room
        api_response = api_instance.get_tools(room_id, server_id)
        print("The response of MCPApi->get_tools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->get_tools: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tools with their enabled/disabled states |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | The room or MCP server was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_server_status**
> McpServerWrapper set_server_status(id, set_server_status_request_body)

Toggles the enabled/disabled state of an MCP server. When a server is disabled, it becomes
unavailable for assignment to rooms and will not be used during AI chat sessions.
Enabling a previously disabled server restores its availability across the tenant.
Requires DocSpace administrator privileges.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique identifier of the MCP server whose status is being changed. | 
 **set_server_status_request_body** | [**SetServerStatusRequestBody**](SetServerStatusRequestBody.md)| New status value. | 

### Return type

[**McpServerWrapper**](McpServerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.mcp_server_wrapper import McpServerWrapper
from docspace_api_sdk.models.set_server_status_request_body import SetServerStatusRequestBody
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.MCPApi(api_client)
    id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Unique identifier of the MCP server whose status is being changed.
    set_server_status_request_body = docspace_api_sdk.SetServerStatusRequestBody() # SetServerStatusRequestBody | New status value.

    try:
        # Enable or disable an MCP server
        api_response = api_instance.set_server_status(id, set_server_status_request_body)
        print("The response of MCPApi->set_server_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->set_server_status: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MCP server with the updated status |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have permission to manage MCP servers |  -  |
**404** | The MCP server with the specified ID was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_tools**
> McpToolArrayWrapper set_tools(room_id, server_id, set_mcp_tools_request_body)

Updates the set of disabled tools for an MCP server within a specific room. Pass a list of tool names
that should be disabled — all other tools exposed by the server will remain enabled. This allows
room administrators to restrict which MCP capabilities are available during AI chat sessions.
Requires room edit permissions.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **int**| Identifier of the room containing the MCP server. | 
 **server_id** | **UUID**| Unique identifier of the MCP server whose tools are being configured. | 
 **set_mcp_tools_request_body** | [**SetMcpToolsRequestBody**](SetMcpToolsRequestBody.md)| Tool configuration parameters. | 

### Return type

[**McpToolArrayWrapper**](McpToolArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.mcp_tool_array_wrapper import McpToolArrayWrapper
from docspace_api_sdk.models.set_mcp_tools_request_body import SetMcpToolsRequestBody
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.MCPApi(api_client)
    room_id = 42 # int | Identifier of the room containing the MCP server.
    server_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Unique identifier of the MCP server whose tools are being configured.
    set_mcp_tools_request_body = docspace_api_sdk.SetMcpToolsRequestBody() # SetMcpToolsRequestBody | Tool configuration parameters.

    try:
        # Configure MCP server tools in a room
        api_response = api_instance.set_tools(room_id, server_id, set_mcp_tools_request_body)
        print("The response of MCPApi->set_tools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->set_tools: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Complete list of tools with their enabled/disabled states |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | The room or MCP server was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_server**
> McpServerWrapper update_server(id, update_server_request_body)

Updates the configuration of an existing custom MCP server identified by its unique ID.
Any combination of fields (name, description, endpoint, headers, icon) can be updated in a single request.
If the endpoint or headers are changed, the system re-validates connectivity by attempting to reach
the new endpoint before saving. Name uniqueness and format rules are enforced on every update.
Requires DocSpace administrator privileges.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique identifier of the MCP server to update. | 
 **update_server_request_body** | [**UpdateServerRequestBody**](UpdateServerRequestBody.md)| Updated server configuration fields. | 

### Return type

[**McpServerWrapper**](McpServerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.mcp_server_wrapper import McpServerWrapper
from docspace_api_sdk.models.update_server_request_body import UpdateServerRequestBody
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.MCPApi(api_client)
    id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Unique identifier of the MCP server to update.
    update_server_request_body = docspace_api_sdk.UpdateServerRequestBody() # UpdateServerRequestBody | Updated server configuration fields.

    try:
        # Update a custom MCP server
        api_response = api_instance.update_server(id, update_server_request_body)
        print("The response of MCPApi->update_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->update_server: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated MCP server configuration |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Invalid server name, reserved name, duplicate name, incorrect credentials, or invalid endpoint URL |  -  |
**403** | You don't have permission to manage MCP servers |  -  |
**404** | The MCP server with the specified ID was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

