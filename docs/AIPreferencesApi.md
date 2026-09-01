# docspace_api_sdk.PreferencesApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_preferences_clear_deep_mode**](#ai_preferences_clear_deep_mode) | **DELETE** /api/2.0/ai/preferences/clear-deep-mode | Clear deep mode
[**ai_preferences_get_deep_mode**](#ai_preferences_get_deep_mode) | **GET** /api/2.0/ai/preferences/get-deep-mode | Get deep mode
[**ai_preferences_is_deep_mode_set**](#ai_preferences_is_deep_mode_set) | **GET** /api/2.0/ai/preferences/is-deep-mode-set | Is deep mode set
[**ai_preferences_set_deep_mode**](#ai_preferences_set_deep_mode) | **PUT** /api/2.0/ai/preferences/set-deep-mode | Set deep mode


# **ai_preferences_clear_deep_mode**
> AiSuccessResponse ai_preferences_clear_deep_mode(body)

Drops the persisted deep-mode toggle of the scope, so later reads fall back to the configured default.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.PreferencesApi(api_client)
    body = 'body_example' # str | 

    try:
        # Clear deep mode
        api_response = api_instance.ai_preferences_clear_deep_mode(body)
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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_preferences_get_deep_mode**
> bool ai_preferences_get_deep_mode(entity_id=entity_id)

Returns the deep-mode toggle of the scope, falling back to the configured default when nothing has been persisted.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. | [optional] 

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
    api_instance = docspace_api_sdk.PreferencesApi(api_client)
    entity_id = 'entity_id_example' # str | The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. (optional)

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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_preferences_is_deep_mode_set**
> bool ai_preferences_is_deep_mode_set(entity_id=entity_id)

Tells whether the scope has an explicitly persisted deep-mode value, whichever way that value is set.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. | [optional] 

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
    api_instance = docspace_api_sdk.PreferencesApi(api_client)
    entity_id = 'entity_id_example' # str | The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. (optional)

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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_preferences_set_deep_mode**
> AiSuccessResponse ai_preferences_set_deep_mode(ai_preferences_set_deep_mode_request)

Persists the deep-mode toggle of the scope. Idempotent - there is no need to check whether a value already exists.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_preferences_set_deep_mode_request** | [**AiPreferencesSetDeepModeRequest**](AiPreferencesSetDeepModeRequest.md)|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

No authorization required

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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

