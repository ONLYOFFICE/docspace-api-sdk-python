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



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_tools_add_custom_server_request** | [**AiToolsAddCustomServerRequest**](AiToolsAddCustomServerRequest.md)|  | 

### Return type

[**AiToolsMutationResult**](AiToolsMutationResult.md)

### Authorization

No authorization required

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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_tools_get_allow_always**
> List[str] ai_tools_get_allow_always(entity_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 

### Return type

**List[str]**

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ToolsApi(api_client)
    entity_id = 'entity_id_example' # str | 

    try:
        # Get allow always
        api_response = api_instance.ai_tools_get_allow_always(entity_id)
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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_tools_get_custom_server**
> object ai_tools_get_custom_server(name, entity_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **entity_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ToolsApi(api_client)
    name = 'name_example' # str | 
    entity_id = 'entity_id_example' # str | 

    try:
        # Get custom server
        api_response = api_instance.ai_tools_get_custom_server(name, entity_id)
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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_tools_get_disabled**
> Dict[str, List[str]] ai_tools_get_disabled(entity_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 

### Return type

**Dict[str, List[str]]**

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ToolsApi(api_client)
    entity_id = 'entity_id_example' # str | 

    try:
        # Get disabled
        api_response = api_instance.ai_tools_get_disabled(entity_id)
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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_tools_is_allow_always**
> bool ai_tools_is_allow_always(server_type, tool_name, entity_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_type** | **str**|  | 
 **tool_name** | **str**|  | 
 **entity_id** | **str**|  | 

### Return type

**bool**

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ToolsApi(api_client)
    server_type = 'server_type_example' # str | 
    tool_name = 'tool_name_example' # str | 
    entity_id = 'entity_id_example' # str | 

    try:
        # Is allow always
        api_response = api_instance.ai_tools_is_allow_always(server_type, tool_name, entity_id)
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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_tools_is_tool_disabled**
> bool ai_tools_is_tool_disabled(server_type, tool_name, entity_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_type** | **str**|  | 
 **tool_name** | **str**|  | 
 **entity_id** | **str**|  | 

### Return type

**bool**

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ToolsApi(api_client)
    server_type = 'server_type_example' # str | 
    tool_name = 'tool_name_example' # str | 
    entity_id = 'entity_id_example' # str | 

    try:
        # Is tool disabled
        api_response = api_instance.ai_tools_is_tool_disabled(server_type, tool_name, entity_id)
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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_tools_list_custom_servers**
> Dict[str, object] ai_tools_list_custom_servers(entity_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ToolsApi(api_client)
    entity_id = 'entity_id_example' # str | 

    try:
        # List custom servers
        api_response = api_instance.ai_tools_list_custom_servers(entity_id)
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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_tools_list_system_tools**
> Dict[str, List[AiTMCPItem]] ai_tools_list_system_tools(entity_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 

### Return type

**Dict[str, List[AiTMCPItem]]**

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_tmcp_item import AiTMCPItem
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ToolsApi(api_client)
    entity_id = 'entity_id_example' # str | 

    try:
        # List system tools
        api_response = api_instance.ai_tools_list_system_tools(entity_id)
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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_tools_remove_custom_server**
> AiSuccessResponse ai_tools_remove_custom_server(ai_tools_remove_custom_server_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_tools_remove_custom_server_request** | [**AiToolsRemoveCustomServerRequest**](AiToolsRemoveCustomServerRequest.md)|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

No authorization required

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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_tools_replace_all_custom_servers**
> AiToolsBulkResult ai_tools_replace_all_custom_servers(ai_tools_replace_all_custom_servers_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_tools_replace_all_custom_servers_request** | [**AiToolsReplaceAllCustomServersRequest**](AiToolsReplaceAllCustomServersRequest.md)|  | 

### Return type

[**AiToolsBulkResult**](AiToolsBulkResult.md)

### Authorization

No authorization required

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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_tools_set_allow_always**
> AiSuccessResponse ai_tools_set_allow_always(ai_tools_set_allow_always_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_tools_set_allow_always_request** | [**AiToolsSetAllowAlwaysRequest**](AiToolsSetAllowAlwaysRequest.md)|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

No authorization required

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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_tools_set_disabled**
> AiSuccessResponse ai_tools_set_disabled(ai_tools_set_disabled_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_tools_set_disabled_request** | [**AiToolsSetDisabledRequest**](AiToolsSetDisabledRequest.md)|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

No authorization required

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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_tools_update_custom_server**
> AiToolsMutationResult ai_tools_update_custom_server(ai_tools_update_custom_server_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_tools_update_custom_server_request** | [**AiToolsUpdateCustomServerRequest**](AiToolsUpdateCustomServerRequest.md)|  | 

### Return type

[**AiToolsMutationResult**](AiToolsMutationResult.md)

### Authorization

No authorization required

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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

