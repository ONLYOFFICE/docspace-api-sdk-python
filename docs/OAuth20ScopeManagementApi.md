# docspace_api_sdk.ScopeManagementApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

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
import docspace_api_sdk
from docspace_api_sdk.models.scope_response import ScopeResponse
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ScopeManagementApi(api_client)

    try:
        # Get available OAuth2 scopes
        api_response = api_instance.get_scopes()
        print("The response of ScopeManagementApi->get_scopes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScopeManagementApi->get_scopes: %s\n" % e)
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

