# docspace.PortalQuotaApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_quota**](PortalQuotaApi.md#get_quota) | **GET** /api/2.0/portal/quota | Get a portal quota
[**get_right_quota**](PortalQuotaApi.md#get_right_quota) | **GET** /api/2.0/portal/quota/right | Get the recommended quota
[**get_tariff**](PortalQuotaApi.md#get_tariff) | **GET** /api/2.0/portal/tariff | Get a portal tariff
[**get_used_space**](PortalQuotaApi.md#get_used_space) | **GET** /api/2.0/portal/usedspace | Get the used portal space


# **get_quota**
> TenantQuotaWrapper get_quota()

Get a portal quota

Returns the current portal quota.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.tenant_quota_wrapper import TenantQuotaWrapper
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
    api_instance = docspace.PortalQuotaApi(api_client)

    try:
        # Get a portal quota
        api_response = api_instance.get_quota()
        print("The response of PortalQuotaApi->get_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalQuotaApi->get_quota: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TenantQuotaWrapper**](TenantQuotaWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current portal quota |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_right_quota**
> TenantQuotaWrapper get_right_quota()

Get the recommended quota

Returns the recommended quota for the current portal.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.tenant_quota_wrapper import TenantQuotaWrapper
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
    api_instance = docspace.PortalQuotaApi(api_client)

    try:
        # Get the recommended quota
        api_response = api_instance.get_right_quota()
        print("The response of PortalQuotaApi->get_right_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalQuotaApi->get_right_quota: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TenantQuotaWrapper**](TenantQuotaWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recommended portal quota |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tariff**
> TariffWrapper get_tariff(refresh=refresh)

Get a portal tariff

Returns the current portal tariff.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.tariff_wrapper import TariffWrapper
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
    api_instance = docspace.PortalQuotaApi(api_client)
    refresh = true # bool | Specifies whether the tariff will be refreshed (optional)

    try:
        # Get a portal tariff
        api_response = api_instance.get_tariff(refresh=refresh)
        print("The response of PortalQuotaApi->get_tariff:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalQuotaApi->get_tariff: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh** | **bool**| Specifies whether the tariff will be refreshed | [optional] 

### Return type

[**TariffWrapper**](TariffWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current portal tariff |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_used_space**
> DoubleWrapper get_used_space()

Get the used portal space

Returns the used space of the current portal.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.double_wrapper import DoubleWrapper
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
    api_instance = docspace.PortalQuotaApi(api_client)

    try:
        # Get the used portal space
        api_response = api_instance.get_used_space()
        print("The response of PortalQuotaApi->get_used_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalQuotaApi->get_used_space: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DoubleWrapper**](DoubleWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Used portal space |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

