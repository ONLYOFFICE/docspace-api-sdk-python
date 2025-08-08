# docspace_api_sdk.StatisticsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_space_usage_statistics**](#get_space_usage_statistics) | **GET** /api/2.0/settings/statistics/spaceusage/{id} | Get the space usage statistics


# **get_space_usage_statistics**
> UsageSpaceStatItemArrayWrapper get_space_usage_statistics(id)

Returns the space usage statistics for the module with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID extracted from the route parameters. | 

### Return type

[**UsageSpaceStatItemArrayWrapper**](UsageSpaceStatItemArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.usage_space_stat_item_array_wrapper import UsageSpaceStatItemArrayWrapper
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
    api_instance = docspace_api_sdk.StatisticsApi(api_client)
    id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28' # str | The ID extracted from the route parameters.

    try:
        # Get the space usage statistics
        api_response = api_instance.get_space_usage_statistics(id)
        print("The response of StatisticsApi->get_space_usage_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->get_space_usage_statistics: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Module space usage statistics |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

