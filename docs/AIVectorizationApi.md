# docspace_api_sdk.VectorizationApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_vectorization_start_task**](#ai_vectorization_start_task) | **POST** /api/2.0/ai/vectorization/tasks | Start a vectorization task


# **ai_vectorization_start_task**
> AiSuccessResponse ai_vectorization_start_task(request_body)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.VectorizationApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Start a vectorization task
        api_response = api_instance.ai_vectorization_start_task(request_body)
        print("The response of VectorizationApi->ai_vectorization_start_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VectorizationApi->ai_vectorization_start_task: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

