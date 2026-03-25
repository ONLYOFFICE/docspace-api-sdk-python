# docspace_api_sdk.VectorizationApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**start_task**](#start_task) | **POST** /api/2.0/ai/vectorization/tasks | Start a vectorization task


# **start_task**
> start_task(vectorization_start_request_body)

Submits the specified files for vectorization. Each file is processed asynchronously by the configured embedding provider
and indexed for semantic search in AI chat sessions. Only files accessible to the current user can be vectorized.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vectorization_start_request_body** | [**VectorizationStartRequestBody**](VectorizationStartRequestBody.md)| The vectorization parameters including file identifiers. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.vectorization_start_request_body import VectorizationStartRequestBody
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
    api_instance = docspace_api_sdk.VectorizationApi(api_client)
    vectorization_start_request_body = docspace_api_sdk.VectorizationStartRequestBody() # VectorizationStartRequestBody | The vectorization parameters including file identifiers.

    try:
        # Start a vectorization task
        api_instance.start_task(vectorization_start_request_body)
    except Exception as e:
        print("Exception when calling VectorizationApi->start_task: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The vectorization task was successfully submitted |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

