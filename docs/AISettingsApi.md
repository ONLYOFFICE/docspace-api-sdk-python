# docspace_api_sdk.SettingsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_settings_get**](#ai_settings_get) | **GET** /api/2.0/ai/config | Get AI settings
[**ai_settings_get_tool_mode**](#ai_settings_get_tool_mode) | **GET** /api/2.0/ai/config/tool-mode | Get the tool permission mode
[**ai_settings_get_user**](#ai_settings_get_user) | **GET** /api/2.0/ai/config/user | Get user AI settings
[**ai_settings_get_vectorization**](#ai_settings_get_vectorization) | **GET** /api/2.0/ai/config/vectorization | Get vectorization settings
[**ai_settings_set_tool_mode**](#ai_settings_set_tool_mode) | **PUT** /api/2.0/ai/config/tool-mode | Set the tool permission mode
[**ai_settings_set_user**](#ai_settings_set_user) | **PUT** /api/2.0/ai/config/user | Update user AI settings
[**ai_settings_set_vectorization**](#ai_settings_set_vectorization) | **PUT** /api/2.0/ai/config/vectorization | Update vectorization settings


# **ai_settings_get**
> AiSettingsWrapper ai_settings_get()

Reports the portal's AI configuration and whether AI is usable at all, which is the first call a client makes before offering any AI feature. It takes no parameters and is proxied unchanged to the DocSpace AI service, so the answer is that service's settings payload. Among other things it says whether the portal runs on the central AI gateway, which decides whether provider profiles can be edited here at all. This is a read-only operation.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**AiSettingsWrapper**](AiSettingsWrapper.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_settings_wrapper import AiSettingsWrapper
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
    api_instance = docspace_api_sdk.SettingsApi(api_client)

    try:
        # Get AI settings
        api_response = api_instance.ai_settings_get()
        print("The response of SettingsApi->ai_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->ai_settings_get: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The portal's AI configuration and whether AI is usable at all. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_settings_get_tool_mode**
> AiSuccessResponse ai_settings_get_tool_mode()

Returns the calling user's tool permission mode as the DocSpace AI service spells it - `{ mode }` with the service's `ToolPermissionMode` enum (`Ask`, `Auto`, `Allow`), proxied unchanged. The chat reads the same value in its own spelling through `GET api/2.0/ai/preferences/get-tool-permission-mode`. This is a read-only operation.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
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
    api_instance = docspace_api_sdk.SettingsApi(api_client)

    try:
        # Get the tool permission mode
        api_response = api_instance.ai_settings_get_tool_mode()
        print("The response of SettingsApi->ai_settings_get_tool_mode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->ai_settings_get_tool_mode: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The calling user's tool permission mode, as `{ mode }`. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_settings_get_user**
> AiUserSettingsWrapper ai_settings_get_user()

Returns the AI settings of the calling user, as opposed to the portal-wide ones. It takes no parameters - the user is the authenticated caller, and there is no way to read somebody else's settings - and is proxied unchanged to the DocSpace AI service. Use `GET api/2.0/ai/config` for the portal-wide configuration. This is a read-only operation.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**AiUserSettingsWrapper**](AiUserSettingsWrapper.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_user_settings_wrapper import AiUserSettingsWrapper
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
    api_instance = docspace_api_sdk.SettingsApi(api_client)

    try:
        # Get user AI settings
        api_response = api_instance.ai_settings_get_user()
        print("The response of SettingsApi->ai_settings_get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->ai_settings_get_user: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The calling user's AI settings. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_settings_get_vectorization**
> AiVectorizationSettingsWrapper ai_settings_get_vectorization()

Returns the portal's vectorization settings - the embedding provider and the options used when portal content is indexed for retrieval. It takes no parameters and is proxied unchanged to the DocSpace AI service. Vectorization is a portal-wide setting, so there is no room-scoped form of it. Change it with `PUT api/2.0/ai/config/vectorization`.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**AiVectorizationSettingsWrapper**](AiVectorizationSettingsWrapper.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_vectorization_settings_wrapper import AiVectorizationSettingsWrapper
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
    api_instance = docspace_api_sdk.SettingsApi(api_client)

    try:
        # Get vectorization settings
        api_response = api_instance.ai_settings_get_vectorization()
        print("The response of SettingsApi->ai_settings_get_vectorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->ai_settings_get_vectorization: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The portal's vectorization settings. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_settings_set_tool_mode**
> AiSuccessResponse ai_settings_set_tool_mode(ai_settings_set_tool_mode_request)

Stores the calling user's tool permission mode and returns the stored result. The body (`{ mode }`) is proxied unchanged to the DocSpace AI service, which rejects a value outside its `ToolPermissionMode` enum. The mode applies to every chat of the user in the portal.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_settings_set_tool_mode_request** | [**Dict[str, Optional[object]]**](object.md)| `{ mode }` with the AI service's `ToolPermissionMode` enum, proxied unchanged; the service rejects anything outside the enum. | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
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
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    ai_settings_set_tool_mode_request = None # Dict[str, Optional[object]] | `{ mode }` with the AI service's `ToolPermissionMode` enum, proxied unchanged; the service rejects anything outside the enum.

    try:
        # Set the tool permission mode
        api_response = api_instance.ai_settings_set_tool_mode(ai_settings_set_tool_mode_request)
        print("The response of SettingsApi->ai_settings_set_tool_mode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->ai_settings_set_tool_mode: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The calling user's stored tool permission mode, as `{ mode }`. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_settings_set_user**
> AiUserSettingsWrapper ai_settings_set_user(ai_settings_set_user_request)

Replaces the AI settings of the calling user and returns the stored result. `chatRecommendedModelVisible` is required and has to be a real boolean - a body the JSON parser cannot read, such as one sent as text/plain, used to arrive empty and answer 200 having stored nothing. The body is then proxied to the DocSpace AI service, which validates the rest, so a rejected value comes back with that service's verdict. Only the caller's own settings can be written. Portal-wide configuration is not touched by this operation.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_settings_set_user_request** | [**Dict[str, Optional[object]]**](object.md)| The user's AI settings: `chatRecommendedModelVisible` as a boolean, required. Read the current one with `GET api/2.0/ai/config/user` and send it back changed. | 

### Return type

[**AiUserSettingsWrapper**](AiUserSettingsWrapper.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_user_settings_wrapper import AiUserSettingsWrapper
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
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    ai_settings_set_user_request = None # Dict[str, Optional[object]] | The user's AI settings: `chatRecommendedModelVisible` as a boolean, required. Read the current one with `GET api/2.0/ai/config/user` and send it back changed.

    try:
        # Update user AI settings
        api_response = api_instance.ai_settings_set_user(ai_settings_set_user_request)
        print("The response of SettingsApi->ai_settings_set_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->ai_settings_set_user: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The calling user's stored AI settings. |  -  |
**400** | `chatRecommendedModelVisible` is missing or not a boolean. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_settings_set_vectorization**
> AiVectorizationSettingsWrapper ai_settings_set_vectorization(ai_settings_set_vectorization_request)

Replaces the portal's vectorization settings and returns the stored result. The body is proxied unchanged to the DocSpace AI service, which validates it, so a rejected value is reported with that service's own verdict rather than being checked here. Changing the embedding provider does not re-index anything already indexed - start that separately with `POST api/2.0/ai/vectorization/tasks`. This is a portal-wide setting and requires the permissions the AI service demands for it.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_settings_set_vectorization_request** | [**Dict[str, Optional[object]]**](object.md)| The portal's vectorization settings, proxied unchanged to the DocSpace AI service, which owns and validates the shape. Read the current one with `GET api/2.0/ai/config/vectorization` and send it back changed. | 

### Return type

[**AiVectorizationSettingsWrapper**](AiVectorizationSettingsWrapper.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_vectorization_settings_wrapper import AiVectorizationSettingsWrapper
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
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    ai_settings_set_vectorization_request = None # Dict[str, Optional[object]] | The portal's vectorization settings, proxied unchanged to the DocSpace AI service, which owns and validates the shape. Read the current one with `GET api/2.0/ai/config/vectorization` and send it back changed.

    try:
        # Update vectorization settings
        api_response = api_instance.ai_settings_set_vectorization(ai_settings_set_vectorization_request)
        print("The response of SettingsApi->ai_settings_set_vectorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->ai_settings_set_vectorization: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The stored vectorization settings. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

