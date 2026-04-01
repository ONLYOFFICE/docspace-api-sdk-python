# docspace_api_sdk.DiscoveryApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**handle_options**](#handle_options) | **OPTIONS** /.well-known/oauth-authorization-server | 


# **handle_options**
> object handle_options()



For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.DiscoveryApi(api_client)

    try:
        api_response = api_instance.handle_options()
        print("The response of DiscoveryApi->handle_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryApi->handle_options: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

