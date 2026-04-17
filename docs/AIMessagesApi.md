# docspace_api_sdk.MessagesApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_message**](#export_message) | **POST** /api/2.0/ai/messages/{messageId}/export | Export a single AI message to a document


# **export_message**
> export_message(message_id, export_message_request_body)

Exports a specific AI chat message as a document into the specified folder. The system verifies that the message exists
and belongs to a chat accessible by the current user, then publishes an asynchronous export task to the event bus.
The exported document will be created in the target folder with the given title once the background task completes.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **int**| The unique identifier of the AI chat message to export. | 
 **export_message_request_body** | [**ExportMessageRequestBody**](ExportMessageRequestBody.md)| The export parameters including destination folder and file title. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.export_message_request_body import ExportMessageRequestBody
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
    api_instance = docspace_api_sdk.MessagesApi(api_client)
    message_id = 1 # int | The unique identifier of the AI chat message to export.
    export_message_request_body = docspace_api_sdk.ExportMessageRequestBody() # ExportMessageRequestBody | The export parameters including destination folder and file title.

    try:
        # Export a single AI message to a document
        api_instance.export_message(message_id, export_message_request_body)
    except Exception as e:
        print("Exception when calling MessagesApi->export_message: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The message export task has been successfully queued for background processing |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The message identifier is invalid (must be greater than 0) |  -  |
**404** | The specified message was not found or the current user does not have access to it |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

