# docspace_api_sdk.SettingsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_settings_get**](#ai_settings_get) | **GET** /api/2.0/ai/config | Get AI settings
[**ai_settings_get_user**](#ai_settings_get_user) | **GET** /api/2.0/ai/config/user | Get user AI settings
[**ai_settings_get_vectorization**](#ai_settings_get_vectorization) | **GET** /api/2.0/ai/config/vectorization | Get vectorization settings
[**ai_settings_set_user**](#ai_settings_set_user) | **PUT** /api/2.0/ai/config/user | Update user AI settings
[**ai_settings_set_vectorization**](#ai_settings_set_vectorization) | **PUT** /api/2.0/ai/config/vectorization | Update vectorization settings


# **ai_settings_get**
> AiAiSettingsWrapper ai_settings_get()

Reports the portal's combined AI configuration and readiness.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**AiAiSettingsWrapper**](AiAiSettingsWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_ai_settings_wrapper import AiAiSettingsWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_settings_get_user**
> AiAiUserSettingsWrapper ai_settings_get_user()

Returns the current user's AI settings.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**AiAiUserSettingsWrapper**](AiAiUserSettingsWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_ai_user_settings_wrapper import AiAiUserSettingsWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_settings_get_vectorization**
> AiVectorizationSettingsWrapper ai_settings_get_vectorization()

Returns the portal's vectorization settings.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**AiVectorizationSettingsWrapper**](AiVectorizationSettingsWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_vectorization_settings_wrapper import AiVectorizationSettingsWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_settings_set_user**
> AiAiUserSettingsWrapper ai_settings_set_user(request_body)

Updates the current user's AI settings.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

[**AiAiUserSettingsWrapper**](AiAiUserSettingsWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_ai_user_settings_wrapper import AiAiUserSettingsWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Update user AI settings
        api_response = api_instance.ai_settings_set_user(request_body)
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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_settings_set_vectorization**
> AiVectorizationSettingsWrapper ai_settings_set_vectorization(request_body)

Updates the portal's vectorization settings.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, Optional[object]]**](object.md)|  | 

### Return type

[**AiVectorizationSettingsWrapper**](AiVectorizationSettingsWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_vectorization_settings_wrapper import AiVectorizationSettingsWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    request_body = None # Dict[str, Optional[object]] | 

    try:
        # Update vectorization settings
        api_response = api_instance.ai_settings_set_vectorization(request_body)
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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

