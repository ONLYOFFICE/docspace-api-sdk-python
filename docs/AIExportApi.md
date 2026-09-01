# docspace_api_sdk.ExportApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_export_text_to_docx**](#ai_export_text_to_docx) | **POST** /api/2.0/ai/text-to-docx | Start markdown → docx export


# **ai_export_text_to_docx**
> AiExportTextToDocx200Response ai_export_text_to_docx(ai_export_text_to_docx_request)

Starts an asynchronous markdown-to-docx export. The response only acknowledges the task: the AI Worker converts the content and saves the .docx into the target folder (an agent room resolves to its result-storage subfolder), and completion reaches the client as the usual folder-modified socket event.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_export_text_to_docx_request** | [**AiExportTextToDocxRequest**](AiExportTextToDocxRequest.md)|  | 

### Return type

[**AiExportTextToDocx200Response**](AiExportTextToDocx200Response.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_export_text_to_docx200_response import AiExportTextToDocx200Response
from docspace_api_sdk.models.ai_export_text_to_docx_request import AiExportTextToDocxRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ExportApi(api_client)
    ai_export_text_to_docx_request = docspace_api_sdk.AiExportTextToDocxRequest() # AiExportTextToDocxRequest | 

    try:
        # Start markdown → docx export
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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

