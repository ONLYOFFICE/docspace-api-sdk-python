# docspace_api_sdk.VectorizationApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_vectorization_start_task**](#ai_vectorization_start_task) | **POST** /api/2.0/ai/vectorization/tasks | Start a vectorization task


# **ai_vectorization_start_task**
> AiVectorizationStartTask200Response ai_vectorization_start_task(ai_vectorization_start_task_request)

Queues the indexing of the portal files named in the body so their contents can be retrieved during a chat round. The body is proxied unchanged to the DocSpace AI service, which validates it and owns the job. Indexing is asynchronous and fire-and-forget: the answer acknowledges the request without carrying a job handle, so there is nothing to poll and progress is not reported here. The embedding provider used is the one in `GET api/2.0/ai/config/vectorization`, and changing that setting does not re-index anything already indexed - queue it again for that.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_vectorization_start_task_request** | [**AiVectorizationStartTaskRequest**](AiVectorizationStartTaskRequest.md)| The files to index, proxied unchanged to the DocSpace AI service, which owns and validates the shape. | 

### Return type

[**AiVectorizationStartTask200Response**](AiVectorizationStartTask200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_vectorization_start_task200_response import AiVectorizationStartTask200Response
from docspace_api_sdk.models.ai_vectorization_start_task_request import AiVectorizationStartTaskRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.VectorizationApi(api_client)
    ai_vectorization_start_task_request = docspace_api_sdk.AiVectorizationStartTaskRequest() # AiVectorizationStartTaskRequest | The files to index, proxied unchanged to the DocSpace AI service, which owns and validates the shape.

    try:
        # Start a vectorization task
        api_response = api_instance.ai_vectorization_start_task(ai_vectorization_start_task_request)
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
**200** | Confirms the indexing was queued. It carries no job handle, so there is nothing to poll. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

