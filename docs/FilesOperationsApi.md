# docspace_api_sdk.OperationsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_favorites**](#add_favorites) | **POST** /api/2.0/files/favorites | 
[**bulk_download**](#bulk_download) | **PUT** /api/2.0/files/fileops/bulkdownload | 
[**check_conversion_status**](#check_conversion_status) | **GET** /api/2.0/files/file/{fileId}/checkconversion | 
[**check_move_or_copy_batch_items**](#check_move_or_copy_batch_items) | **GET** /api/2.0/files/fileops/move | 
[**check_move_or_copy_dest_folder**](#check_move_or_copy_dest_folder) | **GET** /api/2.0/files/fileops/checkdestfolder | 
[**copy_batch_items**](#copy_batch_items) | **PUT** /api/2.0/files/fileops/copy | 
[**create_upload_session**](#create_upload_session) | **POST** /api/2.0/files/{folderId}/upload/create_session | 
[**delete_batch_items**](#delete_batch_items) | **PUT** /api/2.0/files/fileops/delete | 
[**delete_favorites_from_body**](#delete_favorites_from_body) | **DELETE** /api/2.0/files/favorites | 
[**delete_file_versions**](#delete_file_versions) | **PUT** /api/2.0/files/fileops/deleteversion | 
[**duplicate_batch_items**](#duplicate_batch_items) | **PUT** /api/2.0/files/fileops/duplicate | 
[**empty_trash**](#empty_trash) | **PUT** /api/2.0/files/fileops/emptytrash | 
[**get_operation_statuses**](#get_operation_statuses) | **GET** /api/2.0/files/fileops | 
[**get_operation_statuses_by_type**](#get_operation_statuses_by_type) | **GET** /api/2.0/files/fileops/{operationType} | 
[**mark_as_read**](#mark_as_read) | **PUT** /api/2.0/files/fileops/markasread | 
[**move_batch_items**](#move_batch_items) | **PUT** /api/2.0/files/fileops/move | 
[**start_file_conversion**](#start_file_conversion) | **PUT** /api/2.0/files/file/{fileId}/checkconversion | 
[**terminate_tasks**](#terminate_tasks) | **PUT** /api/2.0/files/fileops/terminate/{id} | 
[**update_file_comment**](#update_file_comment) | **PUT** /api/2.0/files/file/{fileId}/comment | 


# **add_favorites**
> BooleanWrapper add_favorites(base_batch_request_dto=base_batch_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_batch_request_dto** | [**BaseBatchRequestDto**](BaseBatchRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    base_batch_request_dto = docspace_api_sdk.BaseBatchRequestDto() # BaseBatchRequestDto |  (optional)

    try:
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
**200** | Boolean value: true if the operation is successful |  -  |
**403** | You don&#39;t have enough permission to perform the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_download**
> FileOperationArrayWrapper bulk_download(download_request_dto=download_request_dto)



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



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID to check conversion status. | 
 **start** | **bool**| Specifies whether a conversion operation is started or not. | [optional] 

### Return type

[**ConversationResultArrayWrapper**](ConversationResultArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.conversation_result_array_wrapper import ConversationResultArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    file_id = 9846 # int | The file ID to check conversion status.
    start = true # bool | Specifies whether a conversion operation is started or not. (optional)

    try:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_move_or_copy_batch_items**
> FileEntryBaseArrayWrapper check_move_or_copy_batch_items(in_dto=in_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **in_dto** | [**BatchRequestDto**](.md)| The request parameters for copying/moving files. | [optional] 

### Return type

[**FileEntryBaseArrayWrapper**](FileEntryBaseArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_entry_base_array_wrapper import FileEntryBaseArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    in_dto = docspace_api_sdk.BatchRequestDto() # BatchRequestDto | The request parameters for copying/moving files. (optional)

    try:
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
**403** | You don&#39;t have enough permission to create |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_move_or_copy_dest_folder**
> CheckDestFolderWrapper check_move_or_copy_dest_folder(in_dto=in_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **in_dto** | [**BatchRequestDto**](.md)| The request parameters for copying/moving files. | [optional] 

### Return type

[**CheckDestFolderWrapper**](CheckDestFolderWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.check_dest_folder_wrapper import CheckDestFolderWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    in_dto = docspace_api_sdk.BatchRequestDto() # BatchRequestDto | The request parameters for copying/moving files. (optional)

    try:
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
**403** | You don&#39;t have enough permission to create |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_batch_items**
> FileOperationArrayWrapper copy_batch_items(batch_request_dto=batch_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_request_dto** | [**BatchRequestDto**](BatchRequestDto.md)|  | [optional] 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    batch_request_dto = docspace_api_sdk.BatchRequestDto() # BatchRequestDto |  (optional)

    try:
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
**403** | You don&#39;t have enough permission to copy |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_upload_session**
> ObjectWrapper create_upload_session(folder_id, session_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The session folder ID. | 
 **session_request** | [**SessionRequest**](SessionRequest.md)| The session parameters. | 

### Return type

[**ObjectWrapper**](ObjectWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    folder_id = 9846 # int | The session folder ID.
    session_request = docspace_api_sdk.SessionRequest() # SessionRequest | The session parameters.

    try:
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
**200** | Information about created session |  -  |
**403** | You don&#39;t have enough permission to create |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_batch_items**
> FileOperationArrayWrapper delete_batch_items(delete_batch_request_dto=delete_batch_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_batch_request_dto** | [**DeleteBatchRequestDto**](DeleteBatchRequestDto.md)|  | [optional] 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    delete_batch_request_dto = docspace_api_sdk.DeleteBatchRequestDto() # DeleteBatchRequestDto |  (optional)

    try:
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
**403** | You don&#39;t have enough permission to delete |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_favorites_from_body**
> BooleanWrapper delete_favorites_from_body(base_batch_request_dto=base_batch_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_batch_request_dto** | [**BaseBatchRequestDto**](BaseBatchRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    base_batch_request_dto = docspace_api_sdk.BaseBatchRequestDto() # BaseBatchRequestDto |  (optional)

    try:
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
**200** | Boolean value: true if the operation is successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file_versions**
> FileOperationWrapper delete_file_versions(delete_version_batch_request_dto=delete_version_batch_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_version_batch_request_dto** | [**DeleteVersionBatchRequestDto**](DeleteVersionBatchRequestDto.md)|  | [optional] 

### Return type

[**FileOperationWrapper**](FileOperationWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    delete_version_batch_request_dto = docspace_api_sdk.DeleteVersionBatchRequestDto() # DeleteVersionBatchRequestDto |  (optional)

    try:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_batch_items**
> FileOperationArrayWrapper duplicate_batch_items(duplicate_request_dto=duplicate_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **duplicate_request_dto** | [**DuplicateRequestDto**](DuplicateRequestDto.md)|  | [optional] 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    duplicate_request_dto = docspace_api_sdk.DuplicateRequestDto() # DuplicateRequestDto |  (optional)

    try:
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
**403** | You don&#39;t have enough permission to duplicate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **empty_trash**
> FileOperationArrayWrapper empty_trash(single=single)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **single** | **bool**| Specifies whether to return only the current operation | [optional] 

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
    single = true # bool | Specifies whether to return only the current operation (optional)

    try:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operation_statuses**
> FileOperationArrayWrapper get_operation_statuses(id=id)



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



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_batch_request_dto** | [**BaseBatchRequestDto**](BaseBatchRequestDto.md)|  | [optional] 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    base_batch_request_dto = docspace_api_sdk.BaseBatchRequestDto() # BaseBatchRequestDto |  (optional)

    try:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_batch_items**
> FileOperationArrayWrapper move_batch_items(batch_request_dto=batch_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_request_dto** | [**BatchRequestDto**](BatchRequestDto.md)|  | [optional] 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    batch_request_dto = docspace_api_sdk.BatchRequestDto() # BatchRequestDto |  (optional)

    try:
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
**403** | You don&#39;t have enough permission to move |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_file_conversion**
> ConversationResultArrayWrapper start_file_conversion(file_id, check_conversion_request_dto_integer=check_conversion_request_dto_integer)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID to start conversion proccess. | 
 **check_conversion_request_dto_integer** | [**CheckConversionRequestDtoInteger**](CheckConversionRequestDtoInteger.md)| The parameters for checking file conversion. | [optional] 

### Return type

[**ConversationResultArrayWrapper**](ConversationResultArrayWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    file_id = 9846 # int | The file ID to start conversion proccess.
    check_conversion_request_dto_integer = docspace_api_sdk.CheckConversionRequestDtoInteger() # CheckConversionRequestDtoInteger | The parameters for checking file conversion. (optional)

    try:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_tasks**
> FileOperationArrayWrapper terminate_tasks(id)



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
    id = '9846' # str | The operation unique identifier.

    try:
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
> StringWrapper update_file_comment(file_id, update_comment)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID where the comment is located. | 
 **update_comment** | [**UpdateComment**](UpdateComment.md)| The parameters for updating a comment. | 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.OperationsApi(api_client)
    file_id = 9846 # int | The file ID where the comment is located.
    update_comment = docspace_api_sdk.UpdateComment() # UpdateComment | The parameters for updating a comment.

    try:
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
**200** | Updated comment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

