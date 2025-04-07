# docspace.FilesOperationsApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_download**](FilesOperationsApi.md#bulk_download) | **PUT** /api/2.0/files/fileops/bulkdownload | Bulk download
[**check_conversion**](FilesOperationsApi.md#check_conversion) | **GET** /api/2.0/files/file/{fileId}/checkconversion | Get conversion status
[**copy_batch_items**](FilesOperationsApi.md#copy_batch_items) | **PUT** /api/2.0/files/fileops/copy | Copy to a folder
[**create_upload_session**](FilesOperationsApi.md#create_upload_session) | **POST** /api/2.0/files/{folderId}/upload/create_session | Chunked upload
[**delete_batch_items**](FilesOperationsApi.md#delete_batch_items) | **PUT** /api/2.0/files/fileops/delete | Delete files and folders
[**delete_file_versions**](FilesOperationsApi.md#delete_file_versions) | **PUT** /api/2.0/files/fileops/deleteversion | 
[**duplicate_batch_items**](FilesOperationsApi.md#duplicate_batch_items) | **PUT** /api/2.0/files/fileops/duplicate | Duplicates all the selected files and folders
[**empty_trash**](FilesOperationsApi.md#empty_trash) | **PUT** /api/2.0/files/fileops/emptytrash | Empty the \&quot;Trash\&quot; folder
[**get_operation_statuses**](FilesOperationsApi.md#get_operation_statuses) | **GET** /api/2.0/files/fileops | Get active operations
[**get_operation_statuses_by_type**](FilesOperationsApi.md#get_operation_statuses_by_type) | **GET** /api/2.0/files/fileops/{operationType} | Retrieves the statuses of operations filtered by the specified operation type.
[**mark_as_read**](FilesOperationsApi.md#mark_as_read) | **PUT** /api/2.0/files/fileops/markasread | Mark as read
[**move_batch_items**](FilesOperationsApi.md#move_batch_items) | **PUT** /api/2.0/files/fileops/move | Move to a folder
[**move_or_copy_batch_check**](FilesOperationsApi.md#move_or_copy_batch_check) | **GET** /api/2.0/files/fileops/move | Check files and folders for conflicts
[**move_or_copy_dest_folder_check**](FilesOperationsApi.md#move_or_copy_dest_folder_check) | **GET** /api/2.0/files/fileops/checkdestfolder | Moves or copies
[**start_conversion**](FilesOperationsApi.md#start_conversion) | **PUT** /api/2.0/files/file/{fileId}/checkconversion | Start file conversion
[**terminate_tasks**](FilesOperationsApi.md#terminate_tasks) | **PUT** /api/2.0/files/fileops/terminate/{id} | Finish active operations
[**update_comment**](FilesOperationsApi.md#update_comment) | **PUT** /api/2.0/files/file/{fileId}/comment | Update a comment


# **bulk_download**
> FileOperationArrayWrapper bulk_download(download_request_dto=download_request_dto)

Bulk download

Starts the download process of files and folders with the IDs specified in the request.

### Example


```python
import docspace
from docspace.models.download_request_dto import DownloadRequestDto
from docspace.models.file_operation_array_wrapper import FileOperationArrayWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)


# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.FilesOperationsApi(api_client)
    download_request_dto = docspace.DownloadRequestDto() # DownloadRequestDto |  (optional)

    try:
        # Bulk download
        api_response = api_instance.bulk_download(download_request_dto=download_request_dto)
        print("The response of FilesOperationsApi->bulk_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesOperationsApi->bulk_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_request_dto** | [**DownloadRequestDto**](DownloadRequestDto.md)|  | [optional] 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file operations |  -  |
**403** | You don&#39;t have enough permission to download |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_conversion**
> ConversationResultArrayWrapper check_conversion(file_id, start=start)

Get conversion status

Checks the conversion status of a file with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.conversation_result_array_wrapper import ConversationResultArrayWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.FilesOperationsApi(api_client)
    file_id = 9846 # int | File ID
    start = true # bool | Specifies if a conversion operation is started or not (optional)

    try:
        # Get conversion status
        api_response = api_instance.check_conversion(file_id, start=start)
        print("The response of FilesOperationsApi->check_conversion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesOperationsApi->check_conversion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File ID | 
 **start** | **bool**| Specifies if a conversion operation is started or not | [optional] 

### Return type

[**ConversationResultArrayWrapper**](ConversationResultArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Conversion result |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_batch_items**
> FileOperationArrayWrapper copy_batch_items(batch_request_dto=batch_request_dto)

Copy to a folder

Copies all the selected files and folders to the folder with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.batch_request_dto import BatchRequestDto
from docspace.models.file_operation_array_wrapper import FileOperationArrayWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.FilesOperationsApi(api_client)
    batch_request_dto = docspace.BatchRequestDto() # BatchRequestDto |  (optional)

    try:
        # Copy to a folder
        api_response = api_instance.copy_batch_items(batch_request_dto=batch_request_dto)
        print("The response of FilesOperationsApi->copy_batch_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesOperationsApi->copy_batch_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_request_dto** | [**BatchRequestDto**](BatchRequestDto.md)|  | [optional] 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

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

Chunked upload

Creates a session to upload large files in multiple chunks to the folder with the ID specified in the request.   **Note**: Each chunk can have different length but the length should be multiple of <b>512</b> and greater or equal to <b>10 mb</b>. Last chunk can have any size.  After the initial response to the request with the <b>200 OK</b> status, you must get the <em>location</em> field value from the response. Send all your chunks to this location.  Each chunk must be sent in the exact order the chunks appear in the file.  After receiving each chunk, the server will respond with the current information about the upload session if no errors occurred.  When the number of bytes uploaded is equal to the number of bytes you sent in the initial request, the server responds with the <b>201 Created</b> status and sends you information about the uploaded file.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.object_wrapper import ObjectWrapper
from docspace.models.session_request import SessionRequest
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.FilesOperationsApi(api_client)
    folder_id = 9846 # int | Folder ID
    session_request = docspace.SessionRequest() # SessionRequest | Session (optional)

    try:
        # Chunked upload
        api_response = api_instance.create_upload_session(folder_id, session_request=session_request)
        print("The response of FilesOperationsApi->create_upload_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesOperationsApi->create_upload_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| Folder ID | 
 **session_request** | [**SessionRequest**](SessionRequest.md)| Session | [optional] 

### Return type

[**ObjectWrapper**](ObjectWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

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

Delete files and folders

Deletes the files and folders with the IDs specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.delete_batch_request_dto import DeleteBatchRequestDto
from docspace.models.file_operation_array_wrapper import FileOperationArrayWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.FilesOperationsApi(api_client)
    delete_batch_request_dto = docspace.DeleteBatchRequestDto() # DeleteBatchRequestDto |  (optional)

    try:
        # Delete files and folders
        api_response = api_instance.delete_batch_items(delete_batch_request_dto=delete_batch_request_dto)
        print("The response of FilesOperationsApi->delete_batch_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesOperationsApi->delete_batch_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_batch_request_dto** | [**DeleteBatchRequestDto**](DeleteBatchRequestDto.md)|  | [optional] 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

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



### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.delete_version_batch_request_dto import DeleteVersionBatchRequestDto
from docspace.models.file_operation_wrapper import FileOperationWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.FilesOperationsApi(api_client)
    delete_version_batch_request_dto = docspace.DeleteVersionBatchRequestDto() # DeleteVersionBatchRequestDto |  (optional)

    try:
        api_response = api_instance.delete_file_versions(delete_version_batch_request_dto=delete_version_batch_request_dto)
        print("The response of FilesOperationsApi->delete_file_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesOperationsApi->delete_file_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_version_batch_request_dto** | [**DeleteVersionBatchRequestDto**](DeleteVersionBatchRequestDto.md)|  | [optional] 

### Return type

[**FileOperationWrapper**](FileOperationWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

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

Duplicates all the selected files and folders

Duplicates all the selected files and folders

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.duplicate_request_dto import DuplicateRequestDto
from docspace.models.file_operation_array_wrapper import FileOperationArrayWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.FilesOperationsApi(api_client)
    duplicate_request_dto = docspace.DuplicateRequestDto() # DuplicateRequestDto |  (optional)

    try:
        # Duplicates all the selected files and folders
        api_response = api_instance.duplicate_batch_items(duplicate_request_dto=duplicate_request_dto)
        print("The response of FilesOperationsApi->duplicate_batch_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesOperationsApi->duplicate_batch_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **duplicate_request_dto** | [**DuplicateRequestDto**](DuplicateRequestDto.md)|  | [optional] 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

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
> FileOperationArrayWrapper empty_trash()

Empty the \"Trash\" folder

Deletes all the files and folders from the \"Trash\" folder.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.file_operation_array_wrapper import FileOperationArrayWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.FilesOperationsApi(api_client)

    try:
        # Empty the \"Trash\" folder
        api_response = api_instance.empty_trash()
        print("The response of FilesOperationsApi->empty_trash:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesOperationsApi->empty_trash: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

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
> FileOperationArrayWrapper get_operation_statuses()

Get active operations

Returns a list of all the active operations.

### Example


```python
import docspace
from docspace.models.file_operation_array_wrapper import FileOperationArrayWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)


# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.FilesOperationsApi(api_client)

    try:
        # Get active operations
        api_response = api_instance.get_operation_statuses()
        print("The response of FilesOperationsApi->get_operation_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesOperationsApi->get_operation_statuses: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file operations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operation_statuses_by_type**
> FileOperationArrayWrapper get_operation_statuses_by_type(operation_type)

Retrieves the statuses of operations filtered by the specified operation type.

Retrieves the statuses of operations filtered by the specified operation type.

### Example


```python
import docspace
from docspace.models.file_operation_array_wrapper import FileOperationArrayWrapper
from docspace.models.file_operation_type import FileOperationType
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)


# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.FilesOperationsApi(api_client)
    operation_type = docspace.FileOperationType() # FileOperationType | Specifies the type of file operation to be retrieved.

    try:
        # Retrieves the statuses of operations filtered by the specified operation type.
        api_response = api_instance.get_operation_statuses_by_type(operation_type)
        print("The response of FilesOperationsApi->get_operation_statuses_by_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesOperationsApi->get_operation_statuses_by_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_type** | [**FileOperationType**](.md)| Specifies the type of file operation to be retrieved. | 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

No authorization required

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

Mark as read

Marks the files and folders with the IDs specified in the request as read.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.base_batch_request_dto import BaseBatchRequestDto
from docspace.models.file_operation_array_wrapper import FileOperationArrayWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.FilesOperationsApi(api_client)
    base_batch_request_dto = docspace.BaseBatchRequestDto() # BaseBatchRequestDto |  (optional)

    try:
        # Mark as read
        api_response = api_instance.mark_as_read(base_batch_request_dto=base_batch_request_dto)
        print("The response of FilesOperationsApi->mark_as_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesOperationsApi->mark_as_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_batch_request_dto** | [**BaseBatchRequestDto**](BaseBatchRequestDto.md)|  | [optional] 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

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

Move to a folder

Moves all the selected files and folders to the folder with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.batch_request_dto import BatchRequestDto
from docspace.models.file_operation_array_wrapper import FileOperationArrayWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.FilesOperationsApi(api_client)
    batch_request_dto = docspace.BatchRequestDto() # BatchRequestDto |  (optional)

    try:
        # Move to a folder
        api_response = api_instance.move_batch_items(batch_request_dto=batch_request_dto)
        print("The response of FilesOperationsApi->move_batch_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesOperationsApi->move_batch_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_request_dto** | [**BatchRequestDto**](BatchRequestDto.md)|  | [optional] 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

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

# **move_or_copy_batch_check**
> FileEntryArrayWrapper move_or_copy_batch_check(in_dto=in_dto)

Check files and folders for conflicts

Checks a batch of files and folders for conflicts when moving or copying them to the folder with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.batch_request_dto import BatchRequestDto
from docspace.models.file_entry_array_wrapper import FileEntryArrayWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.FilesOperationsApi(api_client)
    in_dto = docspace.BatchRequestDto() # BatchRequestDto | Request parameters for copying/moving files (optional)

    try:
        # Check files and folders for conflicts
        api_response = api_instance.move_or_copy_batch_check(in_dto=in_dto)
        print("The response of FilesOperationsApi->move_or_copy_batch_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesOperationsApi->move_or_copy_batch_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **in_dto** | [**BatchRequestDto**](.md)| Request parameters for copying/moving files | [optional] 

### Return type

[**FileEntryArrayWrapper**](FileEntryArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

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

# **move_or_copy_dest_folder_check**
> CheckDestFolderWrapper move_or_copy_dest_folder_check(in_dto=in_dto)

Moves or copies

Moves or copies

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.batch_request_dto import BatchRequestDto
from docspace.models.check_dest_folder_wrapper import CheckDestFolderWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.FilesOperationsApi(api_client)
    in_dto = docspace.BatchRequestDto() # BatchRequestDto | Request parameters for copying/moving files (optional)

    try:
        # Moves or copies
        api_response = api_instance.move_or_copy_dest_folder_check(in_dto=in_dto)
        print("The response of FilesOperationsApi->move_or_copy_dest_folder_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesOperationsApi->move_or_copy_dest_folder_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **in_dto** | [**BatchRequestDto**](.md)| Request parameters for copying/moving files | [optional] 

### Return type

[**CheckDestFolderWrapper**](CheckDestFolderWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

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

# **start_conversion**
> ConversationResultArrayWrapper start_conversion(file_id, check_conversion_request_dto_integer=check_conversion_request_dto_integer)

Start file conversion

Starts a conversion operation of a file with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.check_conversion_request_dto_integer import CheckConversionRequestDtoInteger
from docspace.models.conversation_result_array_wrapper import ConversationResultArrayWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.FilesOperationsApi(api_client)
    file_id = 9846 # int | File ID
    check_conversion_request_dto_integer = docspace.CheckConversionRequestDtoInteger() # CheckConversionRequestDtoInteger | Check conversion (optional)

    try:
        # Start file conversion
        api_response = api_instance.start_conversion(file_id, check_conversion_request_dto_integer=check_conversion_request_dto_integer)
        print("The response of FilesOperationsApi->start_conversion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesOperationsApi->start_conversion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File ID | 
 **check_conversion_request_dto_integer** | [**CheckConversionRequestDtoInteger**](CheckConversionRequestDtoInteger.md)| Check conversion | [optional] 

### Return type

[**ConversationResultArrayWrapper**](ConversationResultArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

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

Finish active operations

Finishes an operation with the ID specified in the request or all the active operations.

### Example


```python
import docspace
from docspace.models.file_operation_array_wrapper import FileOperationArrayWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)


# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.FilesOperationsApi(api_client)
    id = '9846' # str | Operation ID

    try:
        # Finish active operations
        api_response = api_instance.terminate_tasks(id)
        print("The response of FilesOperationsApi->terminate_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesOperationsApi->terminate_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Operation ID | 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file operations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comment**
> StringWrapper update_comment(file_id, update_comment=update_comment)

Update a comment

Updates a comment in a file with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.string_wrapper import StringWrapper
from docspace.models.update_comment import UpdateComment
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.FilesOperationsApi(api_client)
    file_id = 9846 # int | File ID
    update_comment = docspace.UpdateComment() # UpdateComment | Parameters for updating a comment (optional)

    try:
        # Update a comment
        api_response = api_instance.update_comment(file_id, update_comment=update_comment)
        print("The response of FilesOperationsApi->update_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesOperationsApi->update_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File ID | 
 **update_comment** | [**UpdateComment**](UpdateComment.md)| Parameters for updating a comment | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated comment |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

