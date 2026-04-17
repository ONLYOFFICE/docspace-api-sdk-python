# docspace_api_sdk.OperationsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_upload_session**](#abort_upload_session) | **DELETE** /api/2.0/files/{folderId}/session/{sessionId} | Aborts an in-progress file upload session.
[**add_favorites**](#add_favorites) | **POST** /api/2.0/files/favorites | Add favorite files and folders
[**bulk_download**](#bulk_download) | **PUT** /api/2.0/files/fileops/bulkdownload | Bulk download
[**check_conversion_status**](#check_conversion_status) | **GET** /api/2.0/files/file/{fileId}/checkconversion | Get conversion status
[**check_move_or_copy_batch_items**](#check_move_or_copy_batch_items) | **GET** /api/2.0/files/fileops/move | Move or copy files to a folder
[**check_move_or_copy_dest_folder**](#check_move_or_copy_dest_folder) | **GET** /api/2.0/files/fileops/checkdestfolder | Check for moving or copying files to a folder
[**copy_batch_items**](#copy_batch_items) | **PUT** /api/2.0/files/fileops/copy | Copy to the folder
[**create_upload_session**](#create_upload_session) | **POST** /api/2.0/files/{folderId}/upload/create_session | Chunked upload
[**create_upload_session_in_folder**](#create_upload_session_in_folder) | **POST** /api/2.0/files/{folderId}/session | Creates a session for uploading a file to a specific folder in chunks.
[**delete_batch_items**](#delete_batch_items) | **PUT** /api/2.0/files/fileops/delete | Delete files and folders
[**delete_favorites_from_body**](#delete_favorites_from_body) | **DELETE** /api/2.0/files/favorites | Delete favorite files and folders (using body parameters)
[**delete_file_versions**](#delete_file_versions) | **PUT** /api/2.0/files/fileops/deleteversion | Delete file versions
[**duplicate_batch_items**](#duplicate_batch_items) | **PUT** /api/2.0/files/fileops/duplicate | Duplicate files and folders
[**empty_trash**](#empty_trash) | **PUT** /api/2.0/files/fileops/emptytrash | Empty the Trash folder
[**finalize_session**](#finalize_session) | **PUT** /api/2.0/files/{folderId}/session/{sessionId}/finalize | Finalize an upload session
[**get_operation_statuses**](#get_operation_statuses) | **GET** /api/2.0/files/fileops | Get active file operations
[**get_operation_statuses_by_type**](#get_operation_statuses_by_type) | **GET** /api/2.0/files/fileops/{operationType} | Get file operation statuses
[**mark_as_read**](#mark_as_read) | **PUT** /api/2.0/files/fileops/markasread | Mark as read
[**move_batch_items**](#move_batch_items) | **PUT** /api/2.0/files/fileops/move | Move or copy to a folder
[**start_file_conversion**](#start_file_conversion) | **PUT** /api/2.0/files/file/{fileId}/checkconversion | Start file conversion
[**terminate_tasks**](#terminate_tasks) | **PUT** /api/2.0/files/fileops/terminate/{id} | Finish active operations
[**update_file_comment**](#update_file_comment) | **PUT** /api/2.0/files/file/{fileId}/comment | Update a comment
[**upload_async_session**](#upload_async_session) | **POST** /api/2.0/files/{folderId}/session/{sessionId}/upload | Handles the upload of a chunk for an existing upload session.
[**upload_session**](#upload_session) | **POST** /api/2.0/files/{folderId}/session/{sessionId} | Resumes an ongoing file upload session for uploading additional chunks of data.


# **abort_upload_session**
> abort_upload_session(session_id, folder_id)

This method allows users to cancel an ongoing upload session identified by the session ID.
Once the session is aborted, the associated resources will be cleaned up, and the session will no longer accept further uploads.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The session ID. | 
 **folder_id** | **int**| The folder ID. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
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
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    session_id = 'session-123-abc' # str | The session ID.
    folder_id = 1 # int | The folder ID.

    try:
        # Aborts an in-progress file upload session.
        api_instance.abort_upload_session(session_id, folder_id)
    except Exception as e:
        print("Exception when calling OperationsApi->abort_upload_session: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_favorites**
> BooleanWrapper add_favorites(base_batch_request_dto=base_batch_request_dto)

Adds files and folders with the IDs specified in the request to the favorite list.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_batch_request_dto** | [**BaseBatchRequestDto**](BaseBatchRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.base_batch_request_dto import BaseBatchRequestDto
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
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
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    base_batch_request_dto = docspace_api_sdk.BaseBatchRequestDto() # BaseBatchRequestDto |  (optional)

    try:
        # Add favorite files and folders
        api_response = api_instance.add_favorites(base_batch_request_dto=base_batch_request_dto)
        print("The response of OperationsApi->add_favorites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->add_favorites: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to perform the operation |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_download**
> FileOperationArrayWrapper bulk_download(download_request_dto=download_request_dto)

Starts the download process of files and folders with the IDs specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_request_dto** | [**DownloadRequestDto**](DownloadRequestDto.md)|  | [optional] 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.download_request_dto import DownloadRequestDto
from docspace_api_sdk.models.file_operation_array_wrapper import FileOperationArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    download_request_dto = docspace_api_sdk.DownloadRequestDto() # DownloadRequestDto |  (optional)

    try:
        # Bulk download
        api_response = api_instance.bulk_download(download_request_dto=download_request_dto)
        print("The response of OperationsApi->bulk_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->bulk_download: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file operations |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to download |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_conversion_status**
> ConversationResultArrayWrapper check_conversion_status(file_id, start=start)

Checks the conversion status of a file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID to check conversion status. | 
 **start** | **bool**| Specifies whether a conversion operation is started or not. | [optional] 

### Return type

[**ConversationResultArrayWrapper**](ConversationResultArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.conversation_result_array_wrapper import ConversationResultArrayWrapper
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
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    file_id = 1 # int | The file ID to check conversion status.
    start = false # bool | Specifies whether a conversion operation is started or not. (optional)

    try:
        # Get conversion status
        api_response = api_instance.check_conversion_status(file_id, start=start)
        print("The response of OperationsApi->check_conversion_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->check_conversion_status: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Conversion result |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_move_or_copy_batch_items**
> FileEntryBaseArrayWrapper check_move_or_copy_batch_items(in_dto=in_dto)

Checks if files or folders can be moved or copied to the specified folder, moves or copies them, and returns their information.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **in_dto** | [**BatchRequestDto**](.md)| The request parameters for copying/moving files. | [optional] 

### Return type

[**FileEntryBaseArrayWrapper**](FileEntryBaseArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_entry_base_array_wrapper import FileEntryBaseArrayWrapper
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
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    in_dto = docspace_api_sdk.BatchRequestDto() # BatchRequestDto | The request parameters for copying/moving files. (optional)

    try:
        # Move or copy files to a folder
        api_response = api_instance.check_move_or_copy_batch_items(in_dto=in_dto)
        print("The response of OperationsApi->check_move_or_copy_batch_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->check_move_or_copy_batch_items: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file entry information |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to create |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_move_or_copy_dest_folder**
> CheckDestFolderWrapper check_move_or_copy_dest_folder(in_dto=in_dto)

Checks if files can be moved or copied to the specified folder.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **in_dto** | [**BatchRequestDto**](.md)| The request parameters for copying/moving files. | [optional] 

### Return type

[**CheckDestFolderWrapper**](CheckDestFolderWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.check_dest_folder_wrapper import CheckDestFolderWrapper
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
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    in_dto = docspace_api_sdk.BatchRequestDto() # BatchRequestDto | The request parameters for copying/moving files. (optional)

    try:
        # Check for moving or copying files to a folder
        api_response = api_instance.check_move_or_copy_dest_folder(in_dto=in_dto)
        print("The response of OperationsApi->check_move_or_copy_dest_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->check_move_or_copy_dest_folder: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to create |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_batch_items**
> FileOperationArrayWrapper copy_batch_items(batch_request_dto=batch_request_dto)

Copies all the selected files and folders to the folder with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_request_dto** | [**BatchRequestDto**](BatchRequestDto.md)|  | [optional] 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.batch_request_dto import BatchRequestDto
from docspace_api_sdk.models.file_operation_array_wrapper import FileOperationArrayWrapper
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
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    batch_request_dto = docspace_api_sdk.BatchRequestDto() # BatchRequestDto |  (optional)

    try:
        # Copy to the folder
        api_response = api_instance.copy_batch_items(batch_request_dto=batch_request_dto)
        print("The response of OperationsApi->copy_batch_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->copy_batch_items: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file operations |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to copy |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_upload_session**
> ChunkedUploadSessionResponseWrapperIntegerWrapper create_upload_session(folder_id, session_request)

Creates the session to upload large files in multiple chunks to the folder with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The session folder ID. | 
 **session_request** | [**SessionRequest**](SessionRequest.md)| The session parameters. | 

### Return type

[**ChunkedUploadSessionResponseWrapperIntegerWrapper**](ChunkedUploadSessionResponseWrapperIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.chunked_upload_session_response_wrapper_integer_wrapper import ChunkedUploadSessionResponseWrapperIntegerWrapper
from docspace_api_sdk.models.session_request import SessionRequest
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
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    folder_id = 1 # int | The session folder ID.
    session_request = docspace_api_sdk.SessionRequest() # SessionRequest | The session parameters.

    try:
        # Chunked upload
        api_response = api_instance.create_upload_session(folder_id, session_request)
        print("The response of OperationsApi->create_upload_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->create_upload_session: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about created session |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to create |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_upload_session_in_folder**
> ChunkedUploadSessionResponseIntegerWrapper create_upload_session_in_folder(folder_id, session_request)

The session allows the user to upload a file in smaller chunks to the folder identified by its ID.
The file information, such as name, size, and additional metadata, must be provided in the request.
This method facilitates large file upload scenarios by enabling chunked file uploads.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The session folder ID. | 
 **session_request** | [**SessionRequest**](SessionRequest.md)| The session parameters. | 

### Return type

[**ChunkedUploadSessionResponseIntegerWrapper**](ChunkedUploadSessionResponseIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.chunked_upload_session_response_integer_wrapper import ChunkedUploadSessionResponseIntegerWrapper
from docspace_api_sdk.models.session_request import SessionRequest
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
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    folder_id = 1 # int | The session folder ID.
    session_request = docspace_api_sdk.SessionRequest() # SessionRequest | The session parameters.

    try:
        # Creates a session for uploading a file to a specific folder in chunks.
        api_response = api_instance.create_upload_session_in_folder(folder_id, session_request)
        print("The response of OperationsApi->create_upload_session_in_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->create_upload_session_in_folder: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_batch_items**
> FileOperationArrayWrapper delete_batch_items(delete_batch_request_dto=delete_batch_request_dto)

Deletes the files and folders with the IDs specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_batch_request_dto** | [**DeleteBatchRequestDto**](DeleteBatchRequestDto.md)|  | [optional] 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.delete_batch_request_dto import DeleteBatchRequestDto
from docspace_api_sdk.models.file_operation_array_wrapper import FileOperationArrayWrapper
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
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    delete_batch_request_dto = docspace_api_sdk.DeleteBatchRequestDto() # DeleteBatchRequestDto |  (optional)

    try:
        # Delete files and folders
        api_response = api_instance.delete_batch_items(delete_batch_request_dto=delete_batch_request_dto)
        print("The response of OperationsApi->delete_batch_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->delete_batch_items: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file operations |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to delete |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_favorites_from_body**
> BooleanWrapper delete_favorites_from_body(base_batch_request_dto=base_batch_request_dto)

Removes files and folders with the IDs specified in the request from the favorite list. This method uses the body parameters.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_batch_request_dto** | [**BaseBatchRequestDto**](BaseBatchRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.base_batch_request_dto import BaseBatchRequestDto
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
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
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    base_batch_request_dto = docspace_api_sdk.BaseBatchRequestDto() # BaseBatchRequestDto |  (optional)

    try:
        # Delete favorite files and folders (using body parameters)
        api_response = api_instance.delete_favorites_from_body(base_batch_request_dto=base_batch_request_dto)
        print("The response of OperationsApi->delete_favorites_from_body:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->delete_favorites_from_body: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file_versions**
> FileOperationWrapper delete_file_versions(delete_version_batch_request_dto=delete_version_batch_request_dto)

Deletes the file versions with the IDs specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_version_batch_request_dto** | [**DeleteVersionBatchRequestDto**](DeleteVersionBatchRequestDto.md)|  | [optional] 

### Return type

[**FileOperationWrapper**](FileOperationWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.delete_version_batch_request_dto import DeleteVersionBatchRequestDto
from docspace_api_sdk.models.file_operation_wrapper import FileOperationWrapper
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
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    delete_version_batch_request_dto = docspace_api_sdk.DeleteVersionBatchRequestDto() # DeleteVersionBatchRequestDto |  (optional)

    try:
        # Delete file versions
        api_response = api_instance.delete_file_versions(delete_version_batch_request_dto=delete_version_batch_request_dto)
        print("The response of OperationsApi->delete_file_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->delete_file_versions: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file operations |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_batch_items**
> FileOperationArrayWrapper duplicate_batch_items(duplicate_request_dto=duplicate_request_dto)

Duplicates all the selected files and folders.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **duplicate_request_dto** | [**DuplicateRequestDto**](DuplicateRequestDto.md)|  | [optional] 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.duplicate_request_dto import DuplicateRequestDto
from docspace_api_sdk.models.file_operation_array_wrapper import FileOperationArrayWrapper
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
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    duplicate_request_dto = docspace_api_sdk.DuplicateRequestDto() # DuplicateRequestDto |  (optional)

    try:
        # Duplicate files and folders
        api_response = api_instance.duplicate_batch_items(duplicate_request_dto=duplicate_request_dto)
        print("The response of OperationsApi->duplicate_batch_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->duplicate_batch_items: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file operations |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to duplicate |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **empty_trash**
> FileOperationArrayWrapper empty_trash(single=single)

Deletes all the files and folders from the Trash folder.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **single** | **bool**| Specifies whether to return only the current operation | [optional] 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_operation_array_wrapper import FileOperationArrayWrapper
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
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    single = false # bool | Specifies whether to return only the current operation (optional)

    try:
        # Empty the Trash folder
        api_response = api_instance.empty_trash(single=single)
        print("The response of OperationsApi->empty_trash:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->empty_trash: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file operations |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finalize_session**
> UploadSessionResponseIntegerWrapper finalize_session(folder_id, session_id)

Finalizes the upload session by processing the uploaded file chunks and marking the upload as complete.
This method consolidates chunked uploads into a complete file if required, sends notifications about the upload event,
and performs any additional cleanup or related actions, such as socket updates and webhook publishing.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID. | 
 **session_id** | **str**| The session ID. | 

### Return type

[**UploadSessionResponseIntegerWrapper**](UploadSessionResponseIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.upload_session_response_integer_wrapper import UploadSessionResponseIntegerWrapper
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
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    folder_id = 1 # int | The folder ID.
    session_id = 'doc_key_123' # str | The session ID.

    try:
        # Finalize an upload session
        api_response = api_instance.finalize_session(folder_id, session_id)
        print("The response of OperationsApi->finalize_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->finalize_session: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operation_statuses**
> FileOperationArrayWrapper get_operation_statuses(id=id)

Returns a list of all the active file operations.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the file operation. | [optional] 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_operation_array_wrapper import FileOperationArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    id = 'operation-123-abc' # str | The ID of the file operation. (optional)

    try:
        # Get active file operations
        api_response = api_instance.get_operation_statuses(id=id)
        print("The response of OperationsApi->get_operation_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->get_operation_statuses: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file operations |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operation_statuses_by_type**
> FileOperationArrayWrapper get_operation_statuses_by_type(operation_type, id=id)

Retrieves the statuses of operations filtered by the specified operation type.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_type** | [**FileOperationType**](.md)| Specifies the type of file operation to be retrieved. | 
 **id** | **str**| The ID of the file operation. | [optional] 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_operation_array_wrapper import FileOperationArrayWrapper
from docspace_api_sdk.models.file_operation_type import FileOperationType
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    operation_type = docspace_api_sdk.FileOperationType() # FileOperationType | Specifies the type of file operation to be retrieved.
    id = 'operation-123-abc' # str | The ID of the file operation. (optional)

    try:
        # Get file operation statuses
        api_response = api_instance.get_operation_statuses_by_type(operation_type, id=id)
        print("The response of OperationsApi->get_operation_statuses_by_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->get_operation_statuses_by_type: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file operations |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_as_read**
> FileOperationArrayWrapper mark_as_read(base_batch_request_dto=base_batch_request_dto)

Marks the files and folders with the IDs specified in the request as read.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_batch_request_dto** | [**BaseBatchRequestDto**](BaseBatchRequestDto.md)|  | [optional] 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.base_batch_request_dto import BaseBatchRequestDto
from docspace_api_sdk.models.file_operation_array_wrapper import FileOperationArrayWrapper
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
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    base_batch_request_dto = docspace_api_sdk.BaseBatchRequestDto() # BaseBatchRequestDto |  (optional)

    try:
        # Mark as read
        api_response = api_instance.mark_as_read(base_batch_request_dto=base_batch_request_dto)
        print("The response of OperationsApi->mark_as_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->mark_as_read: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file operations |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_batch_items**
> FileOperationArrayWrapper move_batch_items(batch_request_dto=batch_request_dto)

Moves or copies all the selected files and folders to the folder with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_request_dto** | [**BatchRequestDto**](BatchRequestDto.md)|  | [optional] 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.batch_request_dto import BatchRequestDto
from docspace_api_sdk.models.file_operation_array_wrapper import FileOperationArrayWrapper
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
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    batch_request_dto = docspace_api_sdk.BatchRequestDto() # BatchRequestDto |  (optional)

    try:
        # Move or copy to a folder
        api_response = api_instance.move_batch_items(batch_request_dto=batch_request_dto)
        print("The response of OperationsApi->move_batch_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->move_batch_items: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file operations |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to move |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_file_conversion**
> ConversationResultArrayWrapper start_file_conversion(file_id, check_conversion_request_dto_integer=check_conversion_request_dto_integer)

Starts a conversion operation of a file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID to start conversion proccess. | 
 **check_conversion_request_dto_integer** | [**CheckConversionRequestDtoInteger**](CheckConversionRequestDtoInteger.md)| The parameters for checking file conversion. | [optional] 

### Return type

[**ConversationResultArrayWrapper**](ConversationResultArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.check_conversion_request_dto_integer import CheckConversionRequestDtoInteger
from docspace_api_sdk.models.conversation_result_array_wrapper import ConversationResultArrayWrapper
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
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    file_id = 1 # int | The file ID to start conversion proccess.
    check_conversion_request_dto_integer = docspace_api_sdk.CheckConversionRequestDtoInteger() # CheckConversionRequestDtoInteger | The parameters for checking file conversion. (optional)

    try:
        # Start file conversion
        api_response = api_instance.start_file_conversion(file_id, check_conversion_request_dto_integer=check_conversion_request_dto_integer)
        print("The response of OperationsApi->start_file_conversion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->start_file_conversion: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Conversion result |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_tasks**
> FileOperationArrayWrapper terminate_tasks(id)

Finishes an operation with the ID specified in the request or all the active operations.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The operation unique identifier. | 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_operation_array_wrapper import FileOperationArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    id = 'some-operation-id' # str | The operation unique identifier.

    try:
        # Finish active operations
        api_response = api_instance.terminate_tasks(id)
        print("The response of OperationsApi->terminate_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->terminate_tasks: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file operations |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file_comment**
> StringWrapper update_file_comment(file_id, update_comment)

Updates a comment in a file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID where the comment is located. | 
 **update_comment** | [**UpdateComment**](UpdateComment.md)| The parameters for updating a comment. | 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.string_wrapper import StringWrapper
from docspace_api_sdk.models.update_comment import UpdateComment
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
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    file_id = 1 # int | The file ID where the comment is located.
    update_comment = docspace_api_sdk.UpdateComment() # UpdateComment | The parameters for updating a comment.

    try:
        # Update a comment
        api_response = api_instance.update_file_comment(file_id, update_comment)
        print("The response of OperationsApi->update_file_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->update_file_comment: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated comment |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_async_session**
> ChunkedUploadSessionResponseIntegerWrapper upload_async_session(folder_id, session_id, chunk_number=chunk_number, file=file)

This method allows the caller to upload a specific chunk of a file to an ongoing upload session.
The session is identified by the session ID provided in the request. The chunk can be of any size
within the limits allowed during the session initialization. Each chunk must be uploaded in the
correct order for the server to process it appropriately.
The server updates the upload session status and stores the progress information after processing
each chunk. The updated session details are returned in the response.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID. | 
 **session_id** | **str**| The upload session ID. | 
 **chunk_number** | **int**| The chunk number. | [optional] 
 **file** | **bytes**| The file chunk to be uploaded as part of the multipart/form-data request.  This property represents the uploaded file chunk content from the HTTP request form for chunked upload operations.  The file chunk is accessed via the IFormFile interface which provides access to the chunk content and length. | [optional] 

### Return type

[**ChunkedUploadSessionResponseIntegerWrapper**](ChunkedUploadSessionResponseIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.chunked_upload_session_response_integer_wrapper import ChunkedUploadSessionResponseIntegerWrapper
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
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    folder_id = 1 # int | The folder ID.
    session_id = 'session_abc123' # str | The upload session ID.
    chunk_number = 1 # int | The chunk number. (optional)
    file = None # bytes | The file chunk to be uploaded as part of the multipart/form-data request.  This property represents the uploaded file chunk content from the HTTP request form for chunked upload operations.  The file chunk is accessed via the IFormFile interface which provides access to the chunk content and length. (optional)

    try:
        # Handles the upload of a chunk for an existing upload session.
        api_response = api_instance.upload_async_session(folder_id, session_id, chunk_number=chunk_number, file=file)
        print("The response of OperationsApi->upload_async_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->upload_async_session: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_session**
> UploadSessionResponseIntegerWrapper upload_session(folder_id, session_id, file=file)

This method allows continuing an interrupted or partially completed file upload session by uploading subsequent data chunks.
The server will validate each uploaded chunk, update the session state, and respond with the status of the current upload. Once
the total bytes uploaded match the total file size, the file upload process is finalized and related events are triggered.
If the file is newly uploaded, the server responds with a 201 Created status upon completion. If it overwrites an existing file,
versioning information is updated accordingly. The method also triggers associated webhooks and socket notifications to reflect
the updated file state.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID. | 
 **session_id** | **str**| The upload session ID. | 
 **file** | **bytes**| The file to be uploaded as part of the multipart/form-data request.  This property represents the uploaded file content from the HTTP request form.  The file is accessed via the IFormFile interface which provides access to the file name, content type, length, and stream. | [optional] 

### Return type

[**UploadSessionResponseIntegerWrapper**](UploadSessionResponseIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.upload_session_response_integer_wrapper import UploadSessionResponseIntegerWrapper
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
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    folder_id = 1 # int | The folder ID.
    session_id = 'session_abc123' # str | The upload session ID.
    file = None # bytes | The file to be uploaded as part of the multipart/form-data request.  This property represents the uploaded file content from the HTTP request form.  The file is accessed via the IFormFile interface which provides access to the file name, content type, length, and stream. (optional)

    try:
        # Resumes an ongoing file upload session for uploading additional chunks of data.
        api_response = api_instance.upload_session(folder_id, session_id, file=file)
        print("The response of OperationsApi->upload_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->upload_session: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

