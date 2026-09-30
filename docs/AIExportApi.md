# docspace_api_sdk.ExportApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_export_text_to_docx**](#ai_export_text_to_docx) | **POST** /api/2.0/ai/text-to-docx | Start markdown export


# **ai_export_text_to_docx**
> AiExportTextToDocx202Response ai_export_text_to_docx(ai_export_text_to_docx_request)

Queues a markdown export and answers 202 as soon as the job is accepted, without waiting for it. `title`, `content` and `folderId` are all required, and a `content` of only whitespace counts as missing even though it is not empty. `format` is optional and selects the output - `Docx` (the default), `Pdf`, or `Md`, which stores the markdown verbatim instead of converting it. The conversion runs in the AI worker, which saves the .docx into the target folder - an agent room resolves to its own result-storage subfolder - so there is nothing to poll here: completion arrives as the ordinary folder-modified socket event. This route accepts a body of up to 15 MB rather than the 100 KB the rest of the API allows, because a whole thread transcript is sent in one request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_export_text_to_docx_request** | [**AiExportTextToDocxRequest**](AiExportTextToDocxRequest.md)|  | 

### Return type

[**AiExportTextToDocx202Response**](AiExportTextToDocx202Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_export_text_to_docx202_response import AiExportTextToDocx202Response
from docspace_api_sdk.models.ai_export_text_to_docx_request import AiExportTextToDocxRequest
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
    api_instance = docspace_api_sdk.ExportApi(api_client)
    ai_export_text_to_docx_request = docspace_api_sdk.AiExportTextToDocxRequest() # AiExportTextToDocxRequest | 

    try:
        # Start markdown export
        api_response = api_instance.ai_export_text_to_docx(ai_export_text_to_docx_request)
        print("The response of ExportApi->ai_export_text_to_docx:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportApi->ai_export_text_to_docx: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Confirms the export was queued. The file arrives in the target folder later, announced by a folder-modified socket event. |  -  |
**400** | `title`, `content` or `folderId` is missing, or `format` is not one of `Docx`, `Pdf`, `Md`. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**413** | The transcript is larger than 15 MB, this route's own parser limit. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

