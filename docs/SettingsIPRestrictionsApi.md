# docspace_api_sdk.IPRestrictionsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ip_restrictions**](#get_ip_restrictions) | **GET** /api/2.0/settings/iprestrictions | Get the IP portal restrictions
[**read_ip_restrictions_settings**](#read_ip_restrictions_settings) | **GET** /api/2.0/settings/iprestrictions/settings | Get the IP restriction settings
[**save_ip_restrictions**](#save_ip_restrictions) | **PUT** /api/2.0/settings/iprestrictions | Update the IP restrictions
[**update_ip_restrictions_settings**](#update_ip_restrictions_settings) | **PUT** /api/2.0/settings/iprestrictions/settings | Update the IP restriction settings


# **get_ip_restrictions**
> IPRestrictionArrayWrapper get_ip_restrictions()

Returns the IP portal restrictions.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**IPRestrictionArrayWrapper**](IPRestrictionArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ip_restriction_array_wrapper import IPRestrictionArrayWrapper
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
    api_instance = docspace_api_sdk.IPRestrictionsApi(api_client)

    try:
        # Get the IP portal restrictions
        api_response = api_instance.get_ip_restrictions()
        print("The response of IPRestrictionsApi->get_ip_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPRestrictionsApi->get_ip_restrictions: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of IP restrictions parameters |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_ip_restrictions_settings**
> IPRestrictionsSettingsWrapper read_ip_restrictions_settings()

Returns the IP restriction settings.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**IPRestrictionsSettingsWrapper**](IPRestrictionsSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ip_restrictions_settings_wrapper import IPRestrictionsSettingsWrapper
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
    api_instance = docspace_api_sdk.IPRestrictionsApi(api_client)

    try:
        # Get the IP restriction settings
        api_response = api_instance.read_ip_restrictions_settings()
        print("The response of IPRestrictionsApi->read_ip_restrictions_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPRestrictionsApi->read_ip_restrictions_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IP restriction settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_ip_restrictions**
> IpRestrictionsWrapper save_ip_restrictions(ip_restrictions_dto=ip_restrictions_dto)

Updates the IP restrictions with the parameters specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_restrictions_dto** | [**IpRestrictionsDto**](IpRestrictionsDto.md)|  | [optional] 

### Return type

[**IpRestrictionsWrapper**](IpRestrictionsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ip_restrictions_dto import IpRestrictionsDto
from docspace_api_sdk.models.ip_restrictions_wrapper import IpRestrictionsWrapper
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
    api_instance = docspace_api_sdk.IPRestrictionsApi(api_client)
    ip_restrictions_dto = docspace_api_sdk.IpRestrictionsDto() # IpRestrictionsDto |  (optional)

    try:
        # Update the IP restrictions
        api_response = api_instance.save_ip_restrictions(ip_restrictions_dto=ip_restrictions_dto)
        print("The response of IPRestrictionsApi->save_ip_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPRestrictionsApi->save_ip_restrictions: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated IP restriction settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ip_restrictions_settings**
> IpRestrictionsWrapper update_ip_restrictions_settings(ip_restrictions_dto=ip_restrictions_dto)

Updates the IP restriction settings with the parameters specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_restrictions_dto** | [**IpRestrictionsDto**](IpRestrictionsDto.md)|  | [optional] 

### Return type

[**IpRestrictionsWrapper**](IpRestrictionsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ip_restrictions_dto import IpRestrictionsDto
from docspace_api_sdk.models.ip_restrictions_wrapper import IpRestrictionsWrapper
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
    api_instance = docspace_api_sdk.IPRestrictionsApi(api_client)
    ip_restrictions_dto = docspace_api_sdk.IpRestrictionsDto() # IpRestrictionsDto |  (optional)

    try:
        # Update the IP restriction settings
        api_response = api_instance.update_ip_restrictions_settings(ip_restrictions_dto=ip_restrictions_dto)
        print("The response of IPRestrictionsApi->update_ip_restrictions_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPRestrictionsApi->update_ip_restrictions_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated IP restriction settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

