# docspace.SettingsSSOApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_default_sso_settings_v2**](SettingsSSOApi.md#get_default_sso_settings_v2) | **GET** /api/2.0/settings/ssov2/default | Get the default SSO settings
[**get_sso_settings_v2**](SettingsSSOApi.md#get_sso_settings_v2) | **GET** /api/2.0/settings/ssov2 | Get the SSO settings
[**get_sso_settings_v2_constants**](SettingsSSOApi.md#get_sso_settings_v2_constants) | **GET** /api/2.0/settings/ssov2/constants | Get the SSO settings constants
[**reset_sso_settings_v2**](SettingsSSOApi.md#reset_sso_settings_v2) | **DELETE** /api/2.0/settings/ssov2 | Reset the SSO settings
[**save_sso_settings_v2**](SettingsSSOApi.md#save_sso_settings_v2) | **POST** /api/2.0/settings/ssov2 | Save the SSO settings


# **get_default_sso_settings_v2**
> SsoSettingsV2Wrapper get_default_sso_settings_v2()

Get the default SSO settings

Returns the default portal SSO settings.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.sso_settings_v2_wrapper import SsoSettingsV2Wrapper
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
    api_instance = docspace.SettingsSSOApi(api_client)

    try:
        # Get the default SSO settings
        api_response = api_instance.get_default_sso_settings_v2()
        print("The response of SettingsSSOApi->get_default_sso_settings_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsSSOApi->get_default_sso_settings_v2: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SsoSettingsV2Wrapper**](SsoSettingsV2Wrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default SSO settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sso_settings_v2**
> SsoSettingsV2Wrapper get_sso_settings_v2()

Get the SSO settings

Returns the current portal SSO settings.

### Example


```python
import docspace
from docspace.models.sso_settings_v2_wrapper import SsoSettingsV2Wrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)


# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.SettingsSSOApi(api_client)

    try:
        # Get the SSO settings
        api_response = api_instance.get_sso_settings_v2()
        print("The response of SettingsSSOApi->get_sso_settings_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsSSOApi->get_sso_settings_v2: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SsoSettingsV2Wrapper**](SsoSettingsV2Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSO settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sso_settings_v2_constants**
> ObjectWrapper get_sso_settings_v2_constants()

Get the SSO settings constants

Returns the SSO settings constants.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.object_wrapper import ObjectWrapper
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
    api_instance = docspace.SettingsSSOApi(api_client)

    try:
        # Get the SSO settings constants
        api_response = api_instance.get_sso_settings_v2_constants()
        print("The response of SettingsSSOApi->get_sso_settings_v2_constants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsSSOApi->get_sso_settings_v2_constants: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ObjectWrapper**](ObjectWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SSO settings constants: SSO name ID format type, SSO binding type, SSO signing algorithm type, SSO SP certificate action type, SSO IDP certificate action type |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_sso_settings_v2**
> SsoSettingsV2Wrapper reset_sso_settings_v2()

Reset the SSO settings

Resets the SSO settings of the current portal.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.sso_settings_v2_wrapper import SsoSettingsV2Wrapper
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
    api_instance = docspace.SettingsSSOApi(api_client)

    try:
        # Reset the SSO settings
        api_response = api_instance.reset_sso_settings_v2()
        print("The response of SettingsSSOApi->reset_sso_settings_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsSSOApi->reset_sso_settings_v2: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SsoSettingsV2Wrapper**](SsoSettingsV2Wrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default SSO settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_sso_settings_v2**
> SsoSettingsV2Wrapper save_sso_settings_v2(sso_settings_requests_dto=sso_settings_requests_dto)

Save the SSO settings

Saves the SSO settings for the current portal.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.sso_settings_requests_dto import SsoSettingsRequestsDto
from docspace.models.sso_settings_v2_wrapper import SsoSettingsV2Wrapper
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
    api_instance = docspace.SettingsSSOApi(api_client)
    sso_settings_requests_dto = docspace.SsoSettingsRequestsDto() # SsoSettingsRequestsDto |  (optional)

    try:
        # Save the SSO settings
        api_response = api_instance.save_sso_settings_v2(sso_settings_requests_dto=sso_settings_requests_dto)
        print("The response of SettingsSSOApi->save_sso_settings_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsSSOApi->save_sso_settings_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sso_settings_requests_dto** | [**SsoSettingsRequestsDto**](SsoSettingsRequestsDto.md)|  | [optional] 

### Return type

[**SsoSettingsV2Wrapper**](SsoSettingsV2Wrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSO settings |  -  |
**400** | Settings could not be null |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

