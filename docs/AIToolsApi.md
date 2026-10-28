# docspace_api_sdk.ToolsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_tools_add_custom_server**](#ai_tools_add_custom_server) | **POST** /api/2.0/ai/tools/add-custom-server | Add custom server
[**ai_tools_get_allow_always**](#ai_tools_get_allow_always) | **GET** /api/2.0/ai/tools/get-allow-always | Get allow always
[**ai_tools_get_custom_server**](#ai_tools_get_custom_server) | **GET** /api/2.0/ai/tools/get-custom-server | Get custom server
[**ai_tools_get_disabled**](#ai_tools_get_disabled) | **GET** /api/2.0/ai/tools/get-disabled | Get disabled
[**ai_tools_is_allow_always**](#ai_tools_is_allow_always) | **GET** /api/2.0/ai/tools/is-allow-always | Is allow always
[**ai_tools_is_tool_disabled**](#ai_tools_is_tool_disabled) | **GET** /api/2.0/ai/tools/is-tool-disabled | Is tool disabled
[**ai_tools_list_custom_servers**](#ai_tools_list_custom_servers) | **GET** /api/2.0/ai/tools/list-custom-servers | List custom servers
[**ai_tools_list_system_tools**](#ai_tools_list_system_tools) | **GET** /api/2.0/ai/tools/list-system-tools | List system tools
[**ai_tools_remove_custom_server**](#ai_tools_remove_custom_server) | **DELETE** /api/2.0/ai/tools/remove-custom-server | Remove custom server
[**ai_tools_replace_all_custom_servers**](#ai_tools_replace_all_custom_servers) | **PUT** /api/2.0/ai/tools/replace-all-custom-servers | Replace all custom servers
[**ai_tools_set_allow_always**](#ai_tools_set_allow_always) | **PUT** /api/2.0/ai/tools/set-allow-always | Set allow always
[**ai_tools_set_disabled**](#ai_tools_set_disabled) | **PUT** /api/2.0/ai/tools/set-disabled | Set disabled
[**ai_tools_update_custom_server**](#ai_tools_update_custom_server) | **PUT** /api/2.0/ai/tools/update-custom-server | Update custom server


# **ai_tools_add_custom_server**
> AiToolsMutationResult ai_tools_add_custom_server(ai_tools_add_custom_server_request)

Registers a custom MCP server under the given name so the model may call its tools. The name becomes a URL path segment, so it may not be `.`, `..`, or contain a path separator or a control character. `config` may be omitted in two cases: a name matching a host-configured system server pins the entry to that server's canonical settings as a whitelist marker, and a name already registered portal-wide copies the portal-level configuration into this scope; anything else without a config is rejected. `entityId` scopes the registration and has to name a room the caller can open - a room that is not an agent room folds to the portal-wide scope, while an unreachable one is refused so it cannot silently rewrite the portal's own registry.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_tools_add_custom_server_request** | [**AiToolsAddCustomServerRequest**](AiToolsAddCustomServerRequest.md)|  | 

### Return type

[**AiToolsMutationResult**](AiToolsMutationResult.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_tools_add_custom_server_request import AiToolsAddCustomServerRequest
from docspace_api_sdk.models.ai_tools_mutation_result import AiToolsMutationResult
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ToolsApi(api_client)
    ai_tools_add_custom_server_request = docspace_api_sdk.AiToolsAddCustomServerRequest() # AiToolsAddCustomServerRequest | 

    try:
        # Add custom server
        api_response = api_instance.ai_tools_add_custom_server(ai_tools_add_custom_server_request)
        print("The response of ToolsApi->ai_tools_add_custom_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->ai_tools_add_custom_server: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Whether the server was registered, with the stored entry. |  -  |
**400** | The server name is missing or is not routable. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**404** | The referenced object does not exist: an unknown or deleted room named by `entityId`, or an object the caller cannot read - for those the two cases are deliberately indistinguishable. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_tools_get_allow_always**
> List[str] ai_tools_get_allow_always(entity_id=entity_id)

Returns the always-allow list of the scope - the tools whose calls run without pausing the round for approval. `entityId` picks the scope and omitting it reads the portal-wide setting. An empty answer means every tool call has to be approved through `POST api/2.0/ai/ai/approve-tool-call`. Use `GET api/2.0/ai/tools/is-allow-always` to ask about a single tool.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. | [optional] 

### Return type

**List[str]**

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ToolsApi(api_client)
    entity_id = '1234' # str | The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. (optional)

    try:
        # Get allow always
        api_response = api_instance.ai_tools_get_allow_always(entity_id=entity_id)
        print("The response of ToolsApi->ai_tools_get_allow_always:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->ai_tools_get_allow_always: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tools that run without an approval pause. An empty list means every call needs approval. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_tools_get_custom_server**
> object ai_tools_get_custom_server(name, entity_id=entity_id)

Returns the stored configuration of one registered custom MCP server. The name is required and is read from the query; `entityId` picks the scope, and omitting it reads the portal-wide registry. A name that is not registered answers a null body with status 200 rather than 404. The configuration of a system server is returned empty on purpose: those run server-side only, so neither their endpoint nor their credentials are handed to a browser.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The custom MCP server name. | 
 **entity_id** | **str**| The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. | [optional] 

### Return type

**object**

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ToolsApi(api_client)
    name = 'acme-mcp' # str | The custom MCP server name.
    entity_id = '1234' # str | The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. (optional)

    try:
        # Get custom server
        api_response = api_instance.ai_tools_get_custom_server(name, entity_id=entity_id)
        print("The response of ToolsApi->ai_tools_get_custom_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->ai_tools_get_custom_server: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The stored configuration, empty for a system server and null when the name is not registered. |  -  |
**400** | The server name is missing. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_tools_get_disabled**
> Dict[str, List[str]] ai_tools_get_disabled(scope, entity_id=entity_id)

Returns the tools switched off in the scope, as a map of server type to tool names. `entityId` picks the scope and omitting it reads the portal-wide setting. Without `scope` the answer is the caller's effective list, with the tools an administrator switched off for everyone folded in; `scope=tenant` reads that administrator list alone, which is what the settings page shows. An absent server type means nothing is switched off for it, so an empty answer means every tool is on offer. Use `GET api/2.0/ai/tools/is-tool-disabled` to ask about one tool instead of reading the whole map.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | 
 **entity_id** | **str**| The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. | [optional] 

### Return type

**Dict[str, List[str]]**

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ToolsApi(api_client)
    scope = 'scope_example' # str | 
    entity_id = '1234' # str | The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. (optional)

    try:
        # Get disabled
        api_response = api_instance.ai_tools_get_disabled(scope, entity_id=entity_id)
        print("The response of ToolsApi->ai_tools_get_disabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->ai_tools_get_disabled: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The switched-off tools as a map of server type to tool names. An absent type means nothing is switched off for it. |  -  |
**400** | `scope` is not `user` or `tenant`. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_tools_is_allow_always**
> bool ai_tools_is_allow_always(server_type, tool_name, entity_id=entity_id)

Tells whether one named tool runs without an approval pause in the scope. Both `serverType` and `toolName` are required and are read from the query; `entityId` picks the scope. The answer is a bare boolean. A false answer means a call to that tool pauses the round, and the caller resumes it with the approve or deny operation.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_type** | **str**| The MCP server type the tool belongs to. | 
 **tool_name** | **str**| The tool name. | 
 **entity_id** | **str**| The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. | [optional] 

### Return type

**bool**

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ToolsApi(api_client)
    server_type = 'docspace' # str | The MCP server type the tool belongs to.
    tool_name = 'docspace_get_folder' # str | The tool name.
    entity_id = '1234' # str | The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. (optional)

    try:
        # Is allow always
        api_response = api_instance.ai_tools_is_allow_always(server_type, tool_name, entity_id=entity_id)
        print("The response of ToolsApi->ai_tools_is_allow_always:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->ai_tools_is_allow_always: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Whether that one tool runs without an approval pause. |  -  |
**400** | `serverType` or `toolName` is missing. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_tools_is_tool_disabled**
> bool ai_tools_is_tool_disabled(server_type, tool_name, entity_id=entity_id)

Tells whether one named tool of one server type is switched off in the scope. Both `serverType` and `toolName` are required and are read from the query; `entityId` picks the scope. The answer is a bare boolean. It reflects only the disable list - a tool that is on offer may still require approval, which `GET api/2.0/ai/tools/is-allow-always` reports.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_type** | **str**| The MCP server type the tool belongs to. | 
 **tool_name** | **str**| The tool name. | 
 **entity_id** | **str**| The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. | [optional] 

### Return type

**bool**

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ToolsApi(api_client)
    server_type = 'docspace' # str | The MCP server type the tool belongs to.
    tool_name = 'docspace_get_folder' # str | The tool name.
    entity_id = '1234' # str | The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. (optional)

    try:
        # Is tool disabled
        api_response = api_instance.ai_tools_is_tool_disabled(server_type, tool_name, entity_id=entity_id)
        print("The response of ToolsApi->ai_tools_is_tool_disabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->ai_tools_is_tool_disabled: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Whether that one tool is switched off in the scope. |  -  |
**400** | `serverType` or `toolName` is missing. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_tools_list_custom_servers**
> Dict[str, object] ai_tools_list_custom_servers(entity_id=entity_id)

Lists the custom MCP servers registered in the scope as a map of name to configuration. `entityId` picks the scope and omitting it lists the portal-wide registry. The configuration of any entry that names a host-configured system server comes back empty, for the same reason as in the single-server read, and the portal's own built-in MCP server is left out of the list entirely because it is always enabled and cannot be configured. The names in the answer are what the disable and always-allow operations accept as `serverType`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. | [optional] 

### Return type

**Dict[str, object]**

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ToolsApi(api_client)
    entity_id = '1234' # str | The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. (optional)

    try:
        # List custom servers
        api_response = api_instance.ai_tools_list_custom_servers(entity_id=entity_id)
        print("The response of ToolsApi->ai_tools_list_custom_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->ai_tools_list_custom_servers: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The scope's registrations as a map of name to configuration, system entries emptied and the portal's built-in server left out. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_tools_list_system_tools**
> AiToolsListSystemTools200Response ai_tools_list_system_tools(entity_id=entity_id)

Lists every tool the scope can offer the model, as a map of server type to tool group. The answer merges two sources - the host-configured system servers and the live tools of the scope's registered custom MCP servers; for an agent room those are the servers enabled for that agent alone, never the portal-wide registry - and names the system ones separately in `system`, so a client can tell the two apart. `errors` carries the reason a registered server delivered no tools, which is the text to show on a permission card, because the browser cannot reach a server-executed MCP server to find out for itself. The connections are opened server-side, so one request is enough and the client never speaks MCP itself; the portal's own built-in server is left out because it is always enabled.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. | [optional] 

### Return type

[**AiToolsListSystemTools200Response**](AiToolsListSystemTools200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_tools_list_system_tools200_response import AiToolsListSystemTools200Response
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ToolsApi(api_client)
    entity_id = '1234' # str | The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. (optional)

    try:
        # List system tools
        api_response = api_instance.ai_tools_list_system_tools(entity_id=entity_id)
        print("The response of ToolsApi->ai_tools_list_system_tools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->ai_tools_list_system_tools: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The scope's tools grouped by server type, the system group keys named in `system`, and the reason a registered server delivered none in `errors`. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_tools_remove_custom_server**
> AiSuccessResponse ai_tools_remove_custom_server(ai_tools_remove_custom_server_request)

Unregisters a custom MCP server from the scope, so the model is no longer offered its tools. The name is required and may be sent in the body or as a query parameter, and `entityId` has to name a room the caller can open. A name that is not registered is not reported: the call answers success without removing anything. The server itself is untouched - only this portal's registration is dropped.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_tools_remove_custom_server_request** | [**AiToolsRemoveCustomServerRequest**](AiToolsRemoveCustomServerRequest.md)|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
from docspace_api_sdk.models.ai_tools_remove_custom_server_request import AiToolsRemoveCustomServerRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ToolsApi(api_client)
    ai_tools_remove_custom_server_request = docspace_api_sdk.AiToolsRemoveCustomServerRequest() # AiToolsRemoveCustomServerRequest | 

    try:
        # Remove custom server
        api_response = api_instance.ai_tools_remove_custom_server(ai_tools_remove_custom_server_request)
        print("The response of ToolsApi->ai_tools_remove_custom_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->ai_tools_remove_custom_server: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirms the request was accepted, whether or not a registration was removed. |  -  |
**400** | The server name is missing. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**404** | The referenced object does not exist: an unknown or deleted room named by `entityId`, or an object the caller cannot read - for those the two cases are deliberately indistinguishable. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_tools_replace_all_custom_servers**
> AiToolsBulkResult ai_tools_replace_all_custom_servers(ai_tools_replace_all_custom_servers_request)

Replaces the whole custom MCP server registry of the scope with the supplied map in one write, which makes it the operation a settings screen saves with. `map` is required: without it the registry would be emptied, so a missing or non-object value is rejected rather than treated as none. Every name in the map is validated as a routable path segment and every configuration is resolved before anything is written, so a map with one bad entry changes nothing. `entityId` has to name a room the caller can open - this is the operation where an unreachable one would otherwise have wiped the portal-wide registry.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_tools_replace_all_custom_servers_request** | [**AiToolsReplaceAllCustomServersRequest**](AiToolsReplaceAllCustomServersRequest.md)|  | 

### Return type

[**AiToolsBulkResult**](AiToolsBulkResult.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_tools_bulk_result import AiToolsBulkResult
from docspace_api_sdk.models.ai_tools_replace_all_custom_servers_request import AiToolsReplaceAllCustomServersRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ToolsApi(api_client)
    ai_tools_replace_all_custom_servers_request = docspace_api_sdk.AiToolsReplaceAllCustomServersRequest() # AiToolsReplaceAllCustomServersRequest | 

    try:
        # Replace all custom servers
        api_response = api_instance.ai_tools_replace_all_custom_servers(ai_tools_replace_all_custom_servers_request)
        print("The response of ToolsApi->ai_tools_replace_all_custom_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->ai_tools_replace_all_custom_servers: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Whether the registry was replaced, with `errors` listing what was refused. |  -  |
**400** | The body is not a map of server name to configuration, or a name is not routable. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**404** | The referenced object does not exist: an unknown or deleted room named by `entityId`, or an object the caller cannot read - for those the two cases are deliberately indistinguishable. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_tools_set_allow_always**
> AiSuccessResponse ai_tools_set_allow_always(ai_tools_set_allow_always_request)

Adds one tool to the scope's always-allow list, or takes it off, which decides whether a call to it pauses the round for approval. `serverType` and `toolName` have to be non-empty strings and `value` a real boolean - `true` adds, `false` removes - and anything else is rejected before the list is touched, so a malformed body can no longer grant a permanent approval. Unlike the disable operation, `serverType` is not checked against the known server types: an unknown one is stored and then simply never matches. `entityId` has to name a room the caller can open.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_tools_set_allow_always_request** | [**AiToolsSetAllowAlwaysRequest**](AiToolsSetAllowAlwaysRequest.md)|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
from docspace_api_sdk.models.ai_tools_set_allow_always_request import AiToolsSetAllowAlwaysRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ToolsApi(api_client)
    ai_tools_set_allow_always_request = docspace_api_sdk.AiToolsSetAllowAlwaysRequest() # AiToolsSetAllowAlwaysRequest | 

    try:
        # Set allow always
        api_response = api_instance.ai_tools_set_allow_always(ai_tools_set_allow_always_request)
        print("The response of ToolsApi->ai_tools_set_allow_always:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->ai_tools_set_allow_always: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirms the always-allow list was updated. |  -  |
**400** | `serverType` or `toolName` is missing or empty, or `value` is not a boolean. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**404** | The referenced object does not exist: an unknown or deleted room named by `entityId`, or an object the caller cannot read - for those the two cases are deliberately indistinguishable. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_tools_set_disabled**
> AiSuccessResponse ai_tools_set_disabled(ai_tools_set_disabled_request)

Switches off the listed tools of one server type in the scope, so the model is no longer offered them. `serverType` has to be a key the round's tool filter actually matches - a host-configured system server, one of the two DocSpace integration groups, web search, image generation, or one of the scope's registered custom servers - and an unknown value is rejected with the list of valid ones in the message, rather than stored and silently ignored. `toolNames` is required and replaces the previous selection for that server type, so send the full list and pass an empty one to switch everything back on; a missing or non-array value is rejected rather than read as a request to clear, and so is one with anything but non-empty tool names in it. `entityId` has to name a room the caller can open. `scope` picks the list the write lands in: omitted or `user`, the caller's own; `tenant`, the list an administrator keeps for everyone, which every user's reads fold in - the portal settings page writes that one, the composer's own toggles the first.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_tools_set_disabled_request** | [**AiToolsSetDisabledRequest**](AiToolsSetDisabledRequest.md)|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
from docspace_api_sdk.models.ai_tools_set_disabled_request import AiToolsSetDisabledRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ToolsApi(api_client)
    ai_tools_set_disabled_request = docspace_api_sdk.AiToolsSetDisabledRequest() # AiToolsSetDisabledRequest | 

    try:
        # Set disabled
        api_response = api_instance.ai_tools_set_disabled(ai_tools_set_disabled_request)
        print("The response of ToolsApi->ai_tools_set_disabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->ai_tools_set_disabled: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirms the new disable list was stored for that server type. |  -  |
**400** | `toolNames` is missing or not an array of non-empty tool names, `serverType` is unknown, or `scope` is not `user` or `tenant`. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**404** | The referenced object does not exist: an unknown or deleted room named by `entityId`, or an object the caller cannot read - for those the two cases are deliberately indistinguishable. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_tools_update_custom_server**
> AiToolsMutationResult ai_tools_update_custom_server(ai_tools_update_custom_server_request)

Replaces the stored configuration of a registered custom MCP server, under the same name and scope rules as the add operation. The name is re-validated as a routable path segment, and an omitted `config` resolves the same way - to a system server's canonical settings, or to the portal-level entry of that name. `entityId` has to name a room the caller can open. The answer carries the stored registry entry.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_tools_update_custom_server_request** | [**AiToolsUpdateCustomServerRequest**](AiToolsUpdateCustomServerRequest.md)|  | 

### Return type

[**AiToolsMutationResult**](AiToolsMutationResult.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_tools_mutation_result import AiToolsMutationResult
from docspace_api_sdk.models.ai_tools_update_custom_server_request import AiToolsUpdateCustomServerRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ToolsApi(api_client)
    ai_tools_update_custom_server_request = docspace_api_sdk.AiToolsUpdateCustomServerRequest() # AiToolsUpdateCustomServerRequest | 

    try:
        # Update custom server
        api_response = api_instance.ai_tools_update_custom_server(ai_tools_update_custom_server_request)
        print("The response of ToolsApi->ai_tools_update_custom_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->ai_tools_update_custom_server: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Whether the server was updated, with the stored entry. |  -  |
**400** | The server name is missing or is not routable. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**404** | The referenced object does not exist: an unknown or deleted room named by `entityId`, or an object the caller cannot read - for those the two cases are deliberately indistinguishable. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

