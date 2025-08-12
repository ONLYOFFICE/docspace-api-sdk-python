# docspace_api_sdk.OperationsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_download**](#bulk_download) | **PUT** /api/2.0/files/fileops/bulkdownload | Bulk download
[**check_conversion_status**](#check_conversion_status) | **GET** /api/2.0/files/file/{fileId}/checkconversion | Get conversion status
[**check_move_or_copy_batch_items**](#check_move_or_copy_batch_items) | **GET** /api/2.0/files/fileops/move | Check and move or copy to a folder
[**check_move_or_copy_dest_folder**](#check_move_or_copy_dest_folder) | **GET** /api/2.0/files/fileops/checkdestfolder | Check for moving or copying to a folder
[**copy_batch_items**](#copy_batch_items) | **PUT** /api/2.0/files/fileops/copy | Copy to the folder
[**create_upload_session**](#create_upload_session) | **POST** /api/2.0/files/{folderId}/upload/create_session | Chunked upload
[**delete_batch_items**](#delete_batch_items) | **PUT** /api/2.0/files/fileops/delete | Delete files and folders
[**delete_file_versions**](#delete_file_versions) | **PUT** /api/2.0/files/fileops/deleteversion | Delete file versions
[**duplicate_batch_items**](#duplicate_batch_items) | **PUT** /api/2.0/files/fileops/duplicate | Duplicate files and folders
[**empty_trash**](#empty_trash) | **PUT** /api/2.0/files/fileops/emptytrash | Empty the \&quot;Trash\&quot; folder
[**get_operation_statuses**](#get_operation_statuses) | **GET** /api/2.0/files/fileops | Get active file operations
[**get_operation_statuses_by_type**](#get_operation_statuses_by_type) | **GET** /api/2.0/files/fileops/{operationType} | Get file operation statuses
[**mark_as_read**](#mark_as_read) | **PUT** /api/2.0/files/fileops/markasread | Mark as read
[**move_batch_items**](#move_batch_items) | **PUT** /api/2.0/files/fileops/move | Move or copy to a folder
[**start_file_conversion**](#start_file_conversion) | **PUT** /api/2.0/files/file/{fileId}/checkconversion | Start file conversion
[**terminate_tasks**](#terminate_tasks) | **PUT** /api/2.0/files/fileops/terminate/{id} | Finish active operations
[**update_file_comment**](#update_file_comment) | **PUT** /api/2.0/files/file/{fileId}/comment | Update a comment


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
**200** | List of file operations |  -  |
**403** | You don&#39;t have enough permission to download |  -  |

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
    file_id = 9846 # int | The file ID to check conversion status.
    start = true # bool | Specifies whether a conversion operation is started or not. (optional)

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
**200** | Conversion result |  -  |
**401** | Unauthorized |  -  |

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
        # Check and move or copy to a folder
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
**200** | List of file entry information |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to create |  -  |

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
        # Check for moving or copying to a folder
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
**200** | Result |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to create |  -  |

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
**200** | List of file operations |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to copy |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_upload_session**
> ObjectWrapper create_upload_session(folder_id, session_request=session_request)

Creates the session to upload large files in multiple chunks to the folder with the ID specified in the request.

 **Note**: Each chunk can have different length but the length should be multiple of <b>512</b> and greater or equal to <b>10 mb</b>. Last chunk can have any size.
After the initial response to the request with the <b>200 OK</b> status, you must get the <em>location</em> field value from the response. Send all your chunks to this location.
Each chunk must be sent in the exact order the chunks appear in the file.
After receiving each chunk, the server will respond with the current information about the upload session if no errors occurred.
When the number of bytes uploaded is equal to the number of bytes you sent in the initial request, the server responds with the <b>201 Created</b> status and sends you information about the uploaded file.
Information about created session which includes:
<ul>
<li><b>id:</b> unique ID of this upload session,</li>
<li><b>created:</b> UTC time when the session was created,</li>
<li><b>expired:</b> UTC time when the session will expire if no chunks are sent before that time,</li>
<li><b>location:</b> URL where you should send your next chunk,</li>
<li><b>bytes_uploaded:</b> number of bytes uploaded for the specific upload ID,</li>
<li><b>bytes_total:</b> total number of bytes which will be uploaded.</li>
</ul>

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID of the session. | 
 **session_request** | [**SessionRequest**](SessionRequest.md)| The session parameters. | [optional] 

### Return type

[**ObjectWrapper**](ObjectWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.object_wrapper import ObjectWrapper
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
    folder_id = 9846 # int | The folder ID of the session.
    session_request = docspace_api_sdk.SessionRequest() # SessionRequest | The session parameters. (optional)

    try:
        # Chunked upload
        api_response = api_instance.create_upload_session(folder_id, session_request=session_request)
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
**200** | Information about created session |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to create |  -  |

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
**200** | List of file operations |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to delete |  -  |

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
**200** | List of file operations |  -  |
**401** | Unauthorized |  -  |

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
**200** | List of file operations |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to duplicate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **empty_trash**
> FileOperationArrayWrapper empty_trash(single=single)

Deletes all the files and folders from the "Trash" folder.

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
    single = true # bool | Specifies whether to return only the current operation (optional)

    try:
        # Empty the \"Trash\" folder
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
**200** | List of file operations |  -  |
**401** | Unauthorized |  -  |

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
    id = '9846' # str | The ID of the file operation. (optional)

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
**200** | List of file operations |  -  |

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
    id = '9846' # str | The ID of the file operation. (optional)

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
**200** | List of file operations |  -  |

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
**200** | List of file operations |  -  |
**401** | Unauthorized |  -  |

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
**200** | List of file operations |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to move |  -  |

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
    file_id = 9846 # int | The file ID to start conversion proccess.
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
**200** | Conversion result |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_tasks**
> FileOperationArrayWrapper terminate_tasks(id)

Finishes an operation with the ID specified in the request or all the active operations.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The operation ID of the request. | 

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
    id = '9846' # str | The operation ID of the request.

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
**200** | List of file operations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file_comment**
> StringWrapper update_file_comment(file_id, update_comment=update_comment)

Updates a comment in a file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID where the comment is located. | 
 **update_comment** | [**UpdateComment**](UpdateComment.md)| The parameters for updating a comment. | [optional] 

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
    file_id = 9846 # int | The file ID where the comment is located.
    update_comment = docspace_api_sdk.UpdateComment() # UpdateComment | The parameters for updating a comment. (optional)

    try:
        # Update a comment
        api_response = api_instance.update_file_comment(file_id, update_comment=update_comment)
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
**200** | Updated comment |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

