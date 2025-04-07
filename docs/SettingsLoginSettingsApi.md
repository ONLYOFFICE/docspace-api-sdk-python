# docspace.SettingsLoginSettingsApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_login_settings**](SettingsLoginSettingsApi.md#get_login_settings) | **GET** /api/2.0/settings/security/loginsettings | Get login settings
[**set_default_login_settings**](SettingsLoginSettingsApi.md#set_default_login_settings) | **DELETE** /api/2.0/settings/security/loginsettings | Returns the portal login settings.
[**update_login_settings**](SettingsLoginSettingsApi.md#update_login_settings) | **PUT** /api/2.0/settings/security/loginsettings | Update login settings


# **get_login_settings**
> LoginSettingsWrapper get_login_settings()

Get login settings

Returns the portal login settings.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.login_settings_wrapper import LoginSettingsWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.SettingsLoginSettingsApi(api_client)

    try:
        # Get login settings
        api_response = api_instance.get_login_settings()
        print("The response of SettingsLoginSettingsApi->get_login_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsLoginSettingsApi->get_login_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LoginSettingsWrapper**](LoginSettingsWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Login settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_default_login_settings**
> LoginSettingsWrapper set_default_login_settings()

Returns the portal login settings.

Returns the portal login settings.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.login_settings_wrapper import LoginSettingsWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.SettingsLoginSettingsApi(api_client)

    try:
        # Returns the portal login settings.
        api_response = api_instance.set_default_login_settings()
        print("The response of SettingsLoginSettingsApi->set_default_login_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsLoginSettingsApi->set_default_login_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LoginSettingsWrapper**](LoginSettingsWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Login settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_login_settings**
> LoginSettingsWrapper update_login_settings(login_settings_request_dto=login_settings_request_dto)

Update login settings

Updates the login settings with the parameters specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.login_settings_request_dto import LoginSettingsRequestDto
from docspace.models.login_settings_wrapper import LoginSettingsWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.SettingsLoginSettingsApi(api_client)
    login_settings_request_dto = docspace.LoginSettingsRequestDto() # LoginSettingsRequestDto |  (optional)

    try:
        # Update login settings
        api_response = api_instance.update_login_settings(login_settings_request_dto=login_settings_request_dto)
        print("The response of SettingsLoginSettingsApi->update_login_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsLoginSettingsApi->update_login_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_settings_request_dto** | [**LoginSettingsRequestDto**](LoginSettingsRequestDto.md)|  | [optional] 

### Return type

[**LoginSettingsWrapper**](LoginSettingsWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated login settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

