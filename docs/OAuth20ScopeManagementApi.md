# docspace-api-sdk.OAuth20ScopeManagementApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_scopes**](#get_scopes) | **GET** /api/2.0/scopes | Get available OAuth2 scopes


# **get_scopes**
> ScopeResponse get_scopes()

Retrieves a list of all available OAuth2 scopes for the specified tenant. The scopes define the permissions that can be requested by OAuth2 clients. The list is ordered alphabetically, with the 'openid' scope always appearing first.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**ScopeResponse**](ScopeResponse.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.scope_response import ScopeResponse
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
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
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.OAuth20ScopeManagementApi(api_client)

    try:
        # Get available OAuth2 scopes
        api_response = api_instance.get_scopes()
        print("The response of OAuth20ScopeManagementApi->get_scopes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth20ScopeManagementApi->get_scopes: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scopes successfully retrieved |  -  |
**400** | Invalid request parameters |  -  |
**403** | Insufficient permissions to get a list of scopes |  -  |
**429** | Too many requests - rate limit exceeded |  -  |
**500** | Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

