# docspace_api_sdk.PreferencesApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_preferences_clear_deep_mode**](#ai_preferences_clear_deep_mode) | **DELETE** /api/2.0/ai/preferences/clear-deep-mode | Clear deep mode
[**ai_preferences_get_deep_mode**](#ai_preferences_get_deep_mode) | **GET** /api/2.0/ai/preferences/get-deep-mode | Get deep mode
[**ai_preferences_get_reasoning_level**](#ai_preferences_get_reasoning_level) | **GET** /api/2.0/ai/preferences/get-reasoning-level | Get reasoning level
[**ai_preferences_get_tool_permission_mode**](#ai_preferences_get_tool_permission_mode) | **GET** /api/2.0/ai/preferences/get-tool-permission-mode | Get tool permission mode
[**ai_preferences_is_deep_mode_set**](#ai_preferences_is_deep_mode_set) | **GET** /api/2.0/ai/preferences/is-deep-mode-set | Is deep mode set
[**ai_preferences_set_deep_mode**](#ai_preferences_set_deep_mode) | **PUT** /api/2.0/ai/preferences/set-deep-mode | Set deep mode
[**ai_preferences_set_reasoning_level**](#ai_preferences_set_reasoning_level) | **PUT** /api/2.0/ai/preferences/set-reasoning-level | Set reasoning level
[**ai_preferences_set_tool_permission_mode**](#ai_preferences_set_tool_permission_mode) | **PUT** /api/2.0/ai/preferences/set-tool-permission-mode | Set tool permission mode


# **ai_preferences_clear_deep_mode**
> AiSuccessResponse ai_preferences_clear_deep_mode(ai_preferences_clear_deep_mode_request)

Removes the stored extended-thinking setting of a scope (the depth and, with it, the deep-mode toggle), after which reads fall back to the configured default rather than to false. `entityId` picks a room and omitting it clears the portal-wide preference. Clearing a scope that has no stored value is not an error. This differs from storing false, which is an explicit choice a later read reports as set.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_preferences_clear_deep_mode_request** | **str**| The ID of the room whose preference is cleared, as a bare JSON string. Send an empty body to clear the portal-wide preference. | 

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
    api_instance = docspace_api_sdk.PreferencesApi(api_client)
    ai_preferences_clear_deep_mode_request = 'ai_preferences_clear_deep_mode_request_example' # str | The ID of the room whose preference is cleared, as a bare JSON string. Send an empty body to clear the portal-wide preference.

    try:
        # Clear deep mode
        api_response = api_instance.ai_preferences_clear_deep_mode(ai_preferences_clear_deep_mode_request)
        print("The response of PreferencesApi->ai_preferences_clear_deep_mode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreferencesApi->ai_preferences_clear_deep_mode: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirms the scope has no preference of its own and now inherits the default. |  -  |
**400** | `entityId` is not a room ID. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_preferences_get_deep_mode**
> bool ai_preferences_get_deep_mode(entity_id=entity_id)

Returns the deep-mode toggle of a scope, as a bare boolean: whether the stored extended-thinking depth is above `off`. `entityId` picks a room and omitting it reads the portal-wide preference; a value that is not a room ID is refused with 400, as it is on the write. A scope that has never had a value stored falls back to the configured default, so the answer never distinguishes off from unset - ask `GET api/2.0/ai/preferences/is-deep-mode-set` for that. This is a read-only operation.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
    api_instance = docspace_api_sdk.PreferencesApi(api_client)
    entity_id = '1234' # str | The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. (optional)

    try:
        # Get deep mode
        api_response = api_instance.ai_preferences_get_deep_mode(entity_id=entity_id)
        print("The response of PreferencesApi->ai_preferences_get_deep_mode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreferencesApi->ai_preferences_get_deep_mode: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Whether deep mode is on, falling back to the configured default when the scope has no value of its own. |  -  |
**400** | `entityId` is not a room ID. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_preferences_get_reasoning_level**
> AiReasoningLevel ai_preferences_get_reasoning_level(entity_id=entity_id)

Returns the effective extended-thinking depth of the scope: `off` while deep mode is off, otherwise the persisted depth (`low`, `medium`, `high`, `max`), falling back to the default depth (`medium`) when none has been stored. `entityId` picks a room and omitting it reads the portal-wide preference; a value that is not a room ID is refused with 400. Providers clamp the depth to what the model accepts.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. | [optional] 

### Return type

[**AiReasoningLevel**](AiReasoningLevel.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_reasoning_level import AiReasoningLevel
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
    api_instance = docspace_api_sdk.PreferencesApi(api_client)
    entity_id = '1234' # str | The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. (optional)

    try:
        # Get reasoning level
        api_response = api_instance.ai_preferences_get_reasoning_level(entity_id=entity_id)
        print("The response of PreferencesApi->ai_preferences_get_reasoning_level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreferencesApi->ai_preferences_get_reasoning_level: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | `entityId` is not a room ID. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_preferences_get_tool_permission_mode**
> AiChatToolPermissionMode ai_preferences_get_tool_permission_mode(entity_id=entity_id)

Returns how a tool call the model makes is approved for the calling user, in the chat library's spelling: `ask` prompts for every call bar the tools pinned as always allowed, `auto` also runs a tool that opted out of approval itself or is annotated read-only / non-destructive, `allow` runs everything without asking. The mode is one value per user, stored in the user's AI settings (the same value `GET api/2.0/ai/config/tool-mode` reports as the AI service's enum); `entityId` is accepted for symmetry with the depth routes and ignored, though a value that is not a room ID is still refused with 400. The AI service's default is `auto`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. | [optional] 

### Return type

[**AiChatToolPermissionMode**](AiChatToolPermissionMode.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_chat_tool_permission_mode import AiChatToolPermissionMode
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
    api_instance = docspace_api_sdk.PreferencesApi(api_client)
    entity_id = '1234' # str | The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. (optional)

    try:
        # Get tool permission mode
        api_response = api_instance.ai_preferences_get_tool_permission_mode(entity_id=entity_id)
        print("The response of PreferencesApi->ai_preferences_get_tool_permission_mode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreferencesApi->ai_preferences_get_tool_permission_mode: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The mode in force for the scope, as a bare JSON string, falling back to `ask` when none is stored. |  -  |
**400** | `entityId` is not a room ID. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_preferences_is_deep_mode_set**
> bool ai_preferences_is_deep_mode_set(entity_id=entity_id)

Tells whether a scope has an explicitly persisted extended-thinking setting of its own, as opposed to inheriting the configured default. `entityId` picks a room and omitting it asks about the portal-wide preference; a value that is not a room ID is refused with 400. A true answer means a value was stored, whether that value is on or off - read the value itself with `GET api/2.0/ai/preferences/get-deep-mode`. This is the check a settings screen uses to show an explicit override rather than an inherited state.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
    api_instance = docspace_api_sdk.PreferencesApi(api_client)
    entity_id = '1234' # str | The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. (optional)

    try:
        # Is deep mode set
        api_response = api_instance.ai_preferences_is_deep_mode_set(entity_id=entity_id)
        print("The response of PreferencesApi->ai_preferences_is_deep_mode_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreferencesApi->ai_preferences_is_deep_mode_set: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Whether the scope has a preference of its own, whichever way that preference is set. |  -  |
**400** | `entityId` is not a room ID. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_preferences_set_deep_mode**
> AiSuccessResponse ai_preferences_set_deep_mode(ai_preferences_set_deep_mode_request)

Stores the deep-mode toggle of a scope. `false` stores the `off` depth; `true` keeps the depth already stored and falls back to the default depth (`medium`) when none is. `value` has to be a real boolean: a string, a number or an absent value is rejected rather than coerced, so the string false cannot silently switch the setting on and an empty request cannot silently switch it off. `entityId` picks a room and omitting it writes the portal-wide preference. It is idempotent, so there is no need to read the current value first.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_preferences_set_deep_mode_request** | [**AiPreferencesSetDeepModeRequest**](AiPreferencesSetDeepModeRequest.md)|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_preferences_set_deep_mode_request import AiPreferencesSetDeepModeRequest
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
    api_instance = docspace_api_sdk.PreferencesApi(api_client)
    ai_preferences_set_deep_mode_request = docspace_api_sdk.AiPreferencesSetDeepModeRequest() # AiPreferencesSetDeepModeRequest | 

    try:
        # Set deep mode
        api_response = api_instance.ai_preferences_set_deep_mode(ai_preferences_set_deep_mode_request)
        print("The response of PreferencesApi->ai_preferences_set_deep_mode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreferencesApi->ai_preferences_set_deep_mode: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirms the preference was stored. |  -  |
**400** | `value` is missing or is not a boolean, or `entityId` is not a room ID. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_preferences_set_reasoning_level**
> AiSuccessResponse ai_preferences_set_reasoning_level(ai_preferences_set_reasoning_level_request)

Persists the extended-thinking depth of the scope as its single stored value: a depth turns deep mode on at that depth, `off` turns it off and replaces the stored depth (a later deep-mode `true` without a depth lands on `medium`). `entityId` picks a room and omitting it writes the portal-wide preference. Idempotent.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_preferences_set_reasoning_level_request** | [**AiPreferencesSetReasoningLevelRequest**](AiPreferencesSetReasoningLevelRequest.md)|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_preferences_set_reasoning_level_request import AiPreferencesSetReasoningLevelRequest
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
    api_instance = docspace_api_sdk.PreferencesApi(api_client)
    ai_preferences_set_reasoning_level_request = docspace_api_sdk.AiPreferencesSetReasoningLevelRequest() # AiPreferencesSetReasoningLevelRequest | 

    try:
        # Set reasoning level
        api_response = api_instance.ai_preferences_set_reasoning_level(ai_preferences_set_reasoning_level_request)
        print("The response of PreferencesApi->ai_preferences_set_reasoning_level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreferencesApi->ai_preferences_set_reasoning_level: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | `value` is not one of the depths, or `entityId` is not a room ID. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_preferences_set_tool_permission_mode**
> AiSuccessResponse ai_preferences_set_tool_permission_mode(ai_preferences_set_tool_permission_mode_request)

Persists the tool permission mode of the calling user. `value` has to be one of `ask`, `auto`, `allow`: anything else is rejected rather than coerced, so an absent or mistyped value can never overwrite the stored mode. `entityId` is validated like on the other writes and otherwise ignored - the mode applies to every chat of the user. Idempotent.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_preferences_set_tool_permission_mode_request** | [**AiPreferencesSetToolPermissionModeRequest**](AiPreferencesSetToolPermissionModeRequest.md)|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_preferences_set_tool_permission_mode_request import AiPreferencesSetToolPermissionModeRequest
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
    api_instance = docspace_api_sdk.PreferencesApi(api_client)
    ai_preferences_set_tool_permission_mode_request = docspace_api_sdk.AiPreferencesSetToolPermissionModeRequest() # AiPreferencesSetToolPermissionModeRequest | 

    try:
        # Set tool permission mode
        api_response = api_instance.ai_preferences_set_tool_permission_mode(ai_preferences_set_tool_permission_mode_request)
        print("The response of PreferencesApi->ai_preferences_set_tool_permission_mode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreferencesApi->ai_preferences_set_tool_permission_mode: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirms the preference was stored. |  -  |
**400** | `value` is not one of `ask`, `auto`, `allow`, or `entityId` is not a room ID. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

