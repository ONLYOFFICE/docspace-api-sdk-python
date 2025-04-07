# docspace.SettingsIPRestrictionsApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ip_restrictions**](SettingsIPRestrictionsApi.md#get_ip_restrictions) | **GET** /api/2.0/settings/iprestrictions | Get the IP portal restrictions
[**read_ip_restrictions_settings**](SettingsIPRestrictionsApi.md#read_ip_restrictions_settings) | **GET** /api/2.0/settings/iprestrictions/settings | Get the IP restriction settings
[**save_ip_restrictions**](SettingsIPRestrictionsApi.md#save_ip_restrictions) | **PUT** /api/2.0/settings/iprestrictions | Save the IP restriction settings
[**update_ip_restrictions_settings**](SettingsIPRestrictionsApi.md#update_ip_restrictions_settings) | **PUT** /api/2.0/settings/iprestrictions/settings | Save the IP restriction settings


# **get_ip_restrictions**
> IPRestrictionArrayWrapper get_ip_restrictions()

Get the IP portal restrictions

Returns the IP portal restrictions.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.ip_restriction_array_wrapper import IPRestrictionArrayWrapper
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
    api_instance = docspace.SettingsIPRestrictionsApi(api_client)

    try:
        # Get the IP portal restrictions
        api_response = api_instance.get_ip_restrictions()
        print("The response of SettingsIPRestrictionsApi->get_ip_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsIPRestrictionsApi->get_ip_restrictions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**IPRestrictionArrayWrapper**](IPRestrictionArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

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

Get the IP restriction settings

Returns the IP restriction settings.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.ip_restrictions_settings_wrapper import IPRestrictionsSettingsWrapper
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
    api_instance = docspace.SettingsIPRestrictionsApi(api_client)

    try:
        # Get the IP restriction settings
        api_response = api_instance.read_ip_restrictions_settings()
        print("The response of SettingsIPRestrictionsApi->read_ip_restrictions_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsIPRestrictionsApi->read_ip_restrictions_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**IPRestrictionsSettingsWrapper**](IPRestrictionsSettingsWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

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

Save the IP restriction settings

Updates the IP restriction settings with a parameter specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.ip_restrictions_dto import IpRestrictionsDto
from docspace.models.ip_restrictions_wrapper import IpRestrictionsWrapper
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
    api_instance = docspace.SettingsIPRestrictionsApi(api_client)
    ip_restrictions_dto = docspace.IpRestrictionsDto() # IpRestrictionsDto |  (optional)

    try:
        # Save the IP restriction settings
        api_response = api_instance.save_ip_restrictions(ip_restrictions_dto=ip_restrictions_dto)
        print("The response of SettingsIPRestrictionsApi->save_ip_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsIPRestrictionsApi->save_ip_restrictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_restrictions_dto** | [**IpRestrictionsDto**](IpRestrictionsDto.md)|  | [optional] 

### Return type

[**IpRestrictionsWrapper**](IpRestrictionsWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

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

Save the IP restriction settings

Updates the IP restriction settings with a parameter specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.ip_restrictions_dto import IpRestrictionsDto
from docspace.models.ip_restrictions_wrapper import IpRestrictionsWrapper
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
    api_instance = docspace.SettingsIPRestrictionsApi(api_client)
    ip_restrictions_dto = docspace.IpRestrictionsDto() # IpRestrictionsDto |  (optional)

    try:
        # Save the IP restriction settings
        api_response = api_instance.update_ip_restrictions_settings(ip_restrictions_dto=ip_restrictions_dto)
        print("The response of SettingsIPRestrictionsApi->update_ip_restrictions_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsIPRestrictionsApi->update_ip_restrictions_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_restrictions_dto** | [**IpRestrictionsDto**](IpRestrictionsDto.md)|  | [optional] 

### Return type

[**IpRestrictionsWrapper**](IpRestrictionsWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated IP restriction settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

