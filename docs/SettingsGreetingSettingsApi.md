# docspace_api_sdk.GreetingSettingsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_greeting_settings**](#get_greeting_settings) | **GET** /api/2.0/settings/greetingsettings | Get greeting settings
[**get_is_default_greeting_settings**](#get_is_default_greeting_settings) | **GET** /api/2.0/settings/greetingsettings/isdefault | Check the default greeting settings
[**restore_greeting_settings**](#restore_greeting_settings) | **POST** /api/2.0/settings/greetingsettings/restore | Restore the greeting settings
[**save_greeting_settings**](#save_greeting_settings) | **POST** /api/2.0/settings/greetingsettings | Save the greeting settings


# **get_greeting_settings**
> ObjectWrapper get_greeting_settings()

Returns the greeting settings for the current portal.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**ObjectWrapper**](ObjectWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.object_wrapper import ObjectWrapper
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
    api_instance = docspace_api_sdk.GreetingSettingsApi(api_client)

    try:
        # Get greeting settings
        api_response = api_instance.get_greeting_settings()
        print("The response of GreetingSettingsApi->get_greeting_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GreetingSettingsApi->get_greeting_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Greeting settings: tenant name |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_is_default_greeting_settings**
> BooleanWrapper get_is_default_greeting_settings()

Checks if the greeting settings of the current portal are set to default or not.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
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
    api_instance = docspace_api_sdk.GreetingSettingsApi(api_client)

    try:
        # Check the default greeting settings
        api_response = api_instance.get_is_default_greeting_settings()
        print("The response of GreetingSettingsApi->get_is_default_greeting_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GreetingSettingsApi->get_is_default_greeting_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the greeting settings of the current portal are set to default |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_greeting_settings**
> StringWrapper restore_greeting_settings()

Restores the current portal greeting settings.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.string_wrapper import StringWrapper
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
    api_instance = docspace_api_sdk.GreetingSettingsApi(api_client)

    try:
        # Restore the greeting settings
        api_response = api_instance.restore_greeting_settings()
        print("The response of GreetingSettingsApi->restore_greeting_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GreetingSettingsApi->restore_greeting_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Greeting settings: tenant name |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_greeting_settings**
> StringWrapper save_greeting_settings(greeting_settings_requests_dto=greeting_settings_requests_dto)

Saves the greeting settings specified in the request to the current portal.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **greeting_settings_requests_dto** | [**GreetingSettingsRequestsDto**](GreetingSettingsRequestsDto.md)|  | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.greeting_settings_requests_dto import GreetingSettingsRequestsDto
from docspace_api_sdk.models.string_wrapper import StringWrapper
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
    api_instance = docspace_api_sdk.GreetingSettingsApi(api_client)
    greeting_settings_requests_dto = docspace_api_sdk.GreetingSettingsRequestsDto() # GreetingSettingsRequestsDto |  (optional)

    try:
        # Save the greeting settings
        api_response = api_instance.save_greeting_settings(greeting_settings_requests_dto=greeting_settings_requests_dto)
        print("The response of GreetingSettingsApi->save_greeting_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GreetingSettingsApi->save_greeting_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message about saving greeting settings successfully |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

