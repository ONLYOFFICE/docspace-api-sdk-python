# docspace_api_sdk.AttachmentsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_attachments_delete**](#ai_attachments_delete) | **DELETE** /api/2.0/ai/attachments/delete | Delete
[**ai_attachments_delete_many**](#ai_attachments_delete_many) | **DELETE** /api/2.0/ai/attachments/delete-many | Delete many
[**ai_attachments_get**](#ai_attachments_get) | **POST** /api/2.0/ai/attachments/get | Get
[**ai_attachments_get_many**](#ai_attachments_get_many) | **POST** /api/2.0/ai/attachments/get-many | Get many
[**ai_attachments_link_to_message**](#ai_attachments_link_to_message) | **POST** /api/2.0/ai/attachments/link-to-message | Link to message
[**ai_attachments_save_file**](#ai_attachments_save_file) | **POST** /api/2.0/ai/attachments/save-file | Save file
[**ai_attachments_save_files_many**](#ai_attachments_save_files_many) | **POST** /api/2.0/ai/attachments/save-files-many | Save files many


# **ai_attachments_delete**
> AiSuccessResponse ai_attachments_delete(body)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

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
    api_instance = docspace_api_sdk.AttachmentsApi(api_client)
    body = 'body_example' # str | 

    try:
        # Delete
        api_response = api_instance.ai_attachments_delete(body)
        print("The response of AttachmentsApi->ai_attachments_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->ai_attachments_delete: %s\n" % e)
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

# **ai_attachments_delete_many**
> AiSuccessResponse ai_attachments_delete_many(request_body)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

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
    api_instance = docspace_api_sdk.AttachmentsApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Delete many
        api_response = api_instance.ai_attachments_delete_many(request_body)
        print("The response of AttachmentsApi->ai_attachments_delete_many:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->ai_attachments_delete_many: %s\n" % e)
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

# **ai_attachments_get**
> AiAttachment ai_attachments_get(body)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

[**AiAttachment**](AiAttachment.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_attachment import AiAttachment
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AttachmentsApi(api_client)
    body = 'body_example' # str | 

    try:
        # Get
        api_response = api_instance.ai_attachments_get(body)
        print("The response of AttachmentsApi->ai_attachments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->ai_attachments_get: %s\n" % e)
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

# **ai_attachments_get_many**
> List[Optional[AiAttachment]] ai_attachments_get_many(request_body)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

[**List[Optional[AiAttachment]]**](AiAttachment.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_attachment import AiAttachment
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AttachmentsApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Get many
        api_response = api_instance.ai_attachments_get_many(request_body)
        print("The response of AttachmentsApi->ai_attachments_get_many:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->ai_attachments_get_many: %s\n" % e)
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

# **ai_attachments_link_to_message**
> AiSuccessResponse ai_attachments_link_to_message(ai_attachments_link_to_message_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_attachments_link_to_message_request** | [**AiAttachmentsLinkToMessageRequest**](AiAttachmentsLinkToMessageRequest.md)|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_attachments_link_to_message_request import AiAttachmentsLinkToMessageRequest
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AttachmentsApi(api_client)
    ai_attachments_link_to_message_request = docspace_api_sdk.AiAttachmentsLinkToMessageRequest() # AiAttachmentsLinkToMessageRequest | 

    try:
        # Link to message
        api_response = api_instance.ai_attachments_link_to_message(ai_attachments_link_to_message_request)
        print("The response of AttachmentsApi->ai_attachments_link_to_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->ai_attachments_link_to_message: %s\n" % e)
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

# **ai_attachments_save_file**
> AiAttachment ai_attachments_save_file(ai_attachments_save_file_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_attachments_save_file_request** | [**AiAttachmentsSaveFileRequest**](AiAttachmentsSaveFileRequest.md)|  | 

### Return type

[**AiAttachment**](AiAttachment.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_attachment import AiAttachment
from docspace_api_sdk.models.ai_attachments_save_file_request import AiAttachmentsSaveFileRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AttachmentsApi(api_client)
    ai_attachments_save_file_request = docspace_api_sdk.AiAttachmentsSaveFileRequest() # AiAttachmentsSaveFileRequest | 

    try:
        # Save file
        api_response = api_instance.ai_attachments_save_file(ai_attachments_save_file_request)
        print("The response of AttachmentsApi->ai_attachments_save_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->ai_attachments_save_file: %s\n" % e)
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

# **ai_attachments_save_files_many**
> List[AiAttachment] ai_attachments_save_files_many(ai_attachments_save_files_many_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_attachments_save_files_many_request** | [**AiAttachmentsSaveFilesManyRequest**](AiAttachmentsSaveFilesManyRequest.md)|  | 

### Return type

[**List[AiAttachment]**](AiAttachment.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_attachment import AiAttachment
from docspace_api_sdk.models.ai_attachments_save_files_many_request import AiAttachmentsSaveFilesManyRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AttachmentsApi(api_client)
    ai_attachments_save_files_many_request = docspace_api_sdk.AiAttachmentsSaveFilesManyRequest() # AiAttachmentsSaveFilesManyRequest | 

    try:
        # Save files many
        api_response = api_instance.ai_attachments_save_files_many(ai_attachments_save_files_many_request)
        print("The response of AttachmentsApi->ai_attachments_save_files_many:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->ai_attachments_save_files_many: %s\n" % e)
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

