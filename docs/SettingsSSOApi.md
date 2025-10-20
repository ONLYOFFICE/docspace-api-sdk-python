# docspace_api_sdk.SSOApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_default_sso_settings_v2**](#get_default_sso_settings_v2) | **GET** /api/2.0/settings/ssov2/default | Get the default SSO settings
[**get_sso_settings_v2**](#get_sso_settings_v2) | **GET** /api/2.0/settings/ssov2 | Get the SSO settings
[**get_sso_settings_v2_constants**](#get_sso_settings_v2_constants) | **GET** /api/2.0/settings/ssov2/constants | Get the SSO settings constants
[**reset_sso_settings_v2**](#reset_sso_settings_v2) | **DELETE** /api/2.0/settings/ssov2 | Reset the SSO settings
[**save_sso_settings_v2**](#save_sso_settings_v2) | **POST** /api/2.0/settings/ssov2 | Save the SSO settings


# **get_default_sso_settings_v2**
> SsoSettingsV2Wrapper get_default_sso_settings_v2()

Returns the default portal SSO settings.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**SsoSettingsV2Wrapper**](SsoSettingsV2Wrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.sso_settings_v2_wrapper import SsoSettingsV2Wrapper
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
    api_instance = docspace_api_sdk.SSOApi(api_client)

    try:
        # Get the default SSO settings
        api_response = api_instance.get_default_sso_settings_v2()
        print("The response of SSOApi->get_default_sso_settings_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSOApi->get_default_sso_settings_v2: %s\n" % e)
```



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

Returns the current portal SSO settings.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**SsoSettingsV2Wrapper**](SsoSettingsV2Wrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.sso_settings_v2_wrapper import SsoSettingsV2Wrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SSOApi(api_client)

    try:
        # Get the SSO settings
        api_response = api_instance.get_sso_settings_v2()
        print("The response of SSOApi->get_sso_settings_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSOApi->get_sso_settings_v2: %s\n" % e)
```



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

Returns the SSO settings constants.

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
    api_instance = docspace_api_sdk.SSOApi(api_client)

    try:
        # Get the SSO settings constants
        api_response = api_instance.get_sso_settings_v2_constants()
        print("The response of SSOApi->get_sso_settings_v2_constants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSOApi->get_sso_settings_v2_constants: %s\n" % e)
```



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

Resets the SSO settings of the current portal.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**SsoSettingsV2Wrapper**](SsoSettingsV2Wrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.sso_settings_v2_wrapper import SsoSettingsV2Wrapper
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
    api_instance = docspace_api_sdk.SSOApi(api_client)

    try:
        # Reset the SSO settings
        api_response = api_instance.reset_sso_settings_v2()
        print("The response of SSOApi->reset_sso_settings_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSOApi->reset_sso_settings_v2: %s\n" % e)
```



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

Saves the SSO settings for the current portal.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sso_settings_requests_dto** | [**SsoSettingsRequestsDto**](SsoSettingsRequestsDto.md)|  | [optional] 

### Return type

[**SsoSettingsV2Wrapper**](SsoSettingsV2Wrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.sso_settings_requests_dto import SsoSettingsRequestsDto
from docspace_api_sdk.models.sso_settings_v2_wrapper import SsoSettingsV2Wrapper
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
    api_instance = docspace_api_sdk.SSOApi(api_client)
    sso_settings_requests_dto = docspace_api_sdk.SsoSettingsRequestsDto() # SsoSettingsRequestsDto |  (optional)

    try:
        # Save the SSO settings
        api_response = api_instance.save_sso_settings_v2(sso_settings_requests_dto=sso_settings_requests_dto)
        print("The response of SSOApi->save_sso_settings_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSOApi->save_sso_settings_v2: %s\n" % e)
```



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

