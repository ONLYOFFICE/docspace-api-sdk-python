# docspace.ModulesApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_portal_modules**](ModulesApi.md#get_all_portal_modules) | **GET** /api/2.0/modules | Get modules
[**get_all_with_info**](ModulesApi.md#get_all_with_info) | **GET** /api/2.0/modules/info | Get modules information


# **get_all_portal_modules**
> STRINGArrayWrapper get_all_portal_modules()

Get modules

Returns a list of all the portal modules.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.string_array_wrapper import STRINGArrayWrapper
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
    api_instance = docspace.ModulesApi(api_client)

    try:
        # Get modules
        api_response = api_instance.get_all_portal_modules()
        print("The response of ModulesApi->get_all_portal_modules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModulesApi->get_all_portal_modules: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**STRINGArrayWrapper**](STRINGArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of modules |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_with_info**
> ModuleArrayWrapper get_all_with_info()

Get modules information

Returns a list of all the portal modules with their information.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.module_array_wrapper import ModuleArrayWrapper
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
    api_instance = docspace.ModulesApi(api_client)

    try:
        # Get modules information
        api_response = api_instance.get_all_with_info()
        print("The response of ModulesApi->get_all_with_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModulesApi->get_all_with_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ModuleArrayWrapper**](ModuleArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of modules with their information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

