# docspace.FilesFoldersApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_upload**](FilesFoldersApi.md#check_upload) | **POST** /api/2.0/files/{folderId}/upload/check | Checks upload
[**create_folder**](FilesFoldersApi.md#create_folder) | **POST** /api/2.0/files/folder/{folderId} | Create a folder
[**delete_folder**](FilesFoldersApi.md#delete_folder) | **DELETE** /api/2.0/files/folder/{folderId} | Delete a folder
[**get_files_used_space**](FilesFoldersApi.md#get_files_used_space) | **GET** /api/2.0/files/filesusedspace | Get used space of files
[**get_folder**](FilesFoldersApi.md#get_folder) | **GET** /api/2.0/files/{folderId}/formfilter | Get folder form filter
[**get_folder_by_folder_id**](FilesFoldersApi.md#get_folder_by_folder_id) | **GET** /api/2.0/files/{folderId} | Get a folder by ID
[**get_folder_history**](FilesFoldersApi.md#get_folder_history) | **GET** /api/2.0/files/folder/{folderId}/log | Get folder history
[**get_folder_info**](FilesFoldersApi.md#get_folder_info) | **GET** /api/2.0/files/folder/{folderId} | Get folder information
[**get_folder_path**](FilesFoldersApi.md#get_folder_path) | **GET** /api/2.0/files/folder/{folderId}/path | Get the folder path
[**get_folder_primary_external_link**](FilesFoldersApi.md#get_folder_primary_external_link) | **GET** /api/2.0/files/folder/{id}/link | Get primary external link
[**get_folders**](FilesFoldersApi.md#get_folders) | **GET** /api/2.0/files/{folderId}/subfolders | Get subfolders
[**get_my_folder**](FilesFoldersApi.md#get_my_folder) | **GET** /api/2.0/files/@my | Get the \&quot;My documents\&quot; section
[**get_new_items**](FilesFoldersApi.md#get_new_items) | **GET** /api/2.0/files/{folderId}/news | Get new folder items
[**get_privacy_folder**](FilesFoldersApi.md#get_privacy_folder) | **GET** /api/2.0/files/@privacy | Get the \&quot;Private Room\&quot; section
[**get_root_folders**](FilesFoldersApi.md#get_root_folders) | **GET** /api/2.0/files/@root | Get filtered sections
[**get_trash_folder**](FilesFoldersApi.md#get_trash_folder) | **GET** /api/2.0/files/@trash | Get the \&quot;Trash\&quot; section
[**insert_file**](FilesFoldersApi.md#insert_file) | **POST** /api/2.0/files/{folderId}/insert | Insert a file
[**insert_file_to_my_from_body**](FilesFoldersApi.md#insert_file_to_my_from_body) | **POST** /api/2.0/files/@my/insert | Insert a file to the \&quot;My documents\&quot; section
[**rename_folder**](FilesFoldersApi.md#rename_folder) | **PUT** /api/2.0/files/folder/{folderId} | Rename a folder
[**set_file_order**](FilesFoldersApi.md#set_file_order) | **PUT** /api/2.0/files/folder/{folderId}/order | Sets file order in the folder with ID specified in the request
[**upload_file**](FilesFoldersApi.md#upload_file) | **POST** /api/2.0/files/{folderId}/upload | Upload a file
[**upload_file_to_my**](FilesFoldersApi.md#upload_file_to_my) | **POST** /api/2.0/files/@my/upload | Upload a file to the \&quot;My documents\&quot; section


# **check_upload**
> STRINGArrayWrapper check_upload(folder_id, check_upload_request=check_upload_request)

Checks upload

Checks upload

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.check_upload_request import CheckUploadRequest
from docspace.models.string_array_wrapper import STRINGArrayWrapper
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
    api_instance = docspace.FilesFoldersApi(api_client)
    folder_id = 9846 # int | Folder ID
    check_upload_request = docspace.CheckUploadRequest() # CheckUploadRequest | Parameters for checking files uploading (optional)

    try:
        # Checks upload
        api_response = api_instance.check_upload(folder_id, check_upload_request=check_upload_request)
        print("The response of FilesFoldersApi->check_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->check_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| Folder ID | 
 **check_upload_request** | [**CheckUploadRequest**](CheckUploadRequest.md)| Parameters for checking files uploading | [optional] 

### Return type

[**STRINGArrayWrapper**](STRINGArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inserted file |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder**
> FolderIntegerWrapper create_folder(folder_id, create_folder=create_folder)

Create a folder

Creates a new folder with the title specified in the request. The parent folder ID can be also specified.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.create_folder import CreateFolder
from docspace.models.folder_integer_wrapper import FolderIntegerWrapper
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
    api_instance = docspace.FilesFoldersApi(api_client)
    folder_id = 9846 # int | Folder ID
    create_folder = docspace.CreateFolder() # CreateFolder | Folder (optional)

    try:
        # Create a folder
        api_response = api_instance.create_folder(folder_id, create_folder=create_folder)
        print("The response of FilesFoldersApi->create_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->create_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| Folder ID | 
 **create_folder** | [**CreateFolder**](CreateFolder.md)| Folder | [optional] 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New folder parameters |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> FileOperationArrayWrapper delete_folder(folder_id, delete_folder=delete_folder)

Delete a folder

Deletes a folder with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.delete_folder import DeleteFolder
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
    api_instance = docspace.FilesFoldersApi(api_client)
    folder_id = 9846 # int | Folder ID
    delete_folder = docspace.DeleteFolder() # DeleteFolder | Parameters for deleting a folder (optional)

    try:
        # Delete a folder
        api_response = api_instance.delete_folder(folder_id, delete_folder=delete_folder)
        print("The response of FilesFoldersApi->delete_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->delete_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| Folder ID | 
 **delete_folder** | [**DeleteFolder**](DeleteFolder.md)| Parameters for deleting a folder | [optional] 

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

# **get_files_used_space**
> FilesStatisticsResultWrapper get_files_used_space()

Get used space of files

Returns the used space of files in the root folders.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.files_statistics_result_wrapper import FilesStatisticsResultWrapper
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
    api_instance = docspace.FilesFoldersApi(api_client)

    try:
        # Get used space of files
        api_response = api_instance.get_files_used_space()
        print("The response of FilesFoldersApi->get_files_used_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_files_used_space: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FilesStatisticsResultWrapper**](FilesStatisticsResultWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Used space of files in the root folders |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder**
> FormsItemArrayWrapper get_folder(folder_id)

Get folder form filter

Get form filter of a folder with id specified in request

### Example


```python
import docspace
from docspace.models.forms_item_array_wrapper import FormsItemArrayWrapper
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
    api_instance = docspace.FilesFoldersApi(api_client)
    folder_id = 9846 # int | Folder ID

    try:
        # Get folder form filter
        api_response = api_instance.get_folder(folder_id)
        print("The response of FilesFoldersApi->get_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| Folder ID | 

### Return type

[**FormsItemArrayWrapper**](FormsItemArrayWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_by_folder_id**
> FolderContentIntegerWrapper get_folder_by_folder_id(folder_id, user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, room_id=room_id, exclude_subject=exclude_subject, apply_filter_option=apply_filter_option, extension=extension, search_area=search_area, forms_item_key=forms_item_key, forms_item_type=forms_item_type)

Get a folder by ID

Returns the detailed list of files and folders located in the folder with the ID specified in the request.

### Example


```python
import docspace
from docspace.models.apply_filter_option import ApplyFilterOption
from docspace.models.filter_type import FilterType
from docspace.models.folder_content_integer_wrapper import FolderContentIntegerWrapper
from docspace.models.search_area import SearchArea
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
    api_instance = docspace.FilesFoldersApi(api_client)
    folder_id = 9846 # int | Folder ID
    user_id_or_group_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | User or group ID (optional)
    filter_type = docspace.FilterType() # FilterType | Filter type (optional)
    room_id = 9846 # int | Room ID (optional)
    exclude_subject = true # bool | Specifies whether to exclude a subject or not (optional)
    apply_filter_option = docspace.ApplyFilterOption() # ApplyFilterOption | Specifies whether to return only files, only folders or all elements from the specified folder (optional)
    extension = '.txt' # str | Specifies whether to search for a specific file extension (optional)
    search_area = docspace.SearchArea() # SearchArea | Search area (optional)
    forms_item_key = 'some text' # str |  (optional)
    forms_item_type = 'some text' # str |  (optional)

    try:
        # Get a folder by ID
        api_response = api_instance.get_folder_by_folder_id(folder_id, user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, room_id=room_id, exclude_subject=exclude_subject, apply_filter_option=apply_filter_option, extension=extension, search_area=search_area, forms_item_key=forms_item_key, forms_item_type=forms_item_type)
        print("The response of FilesFoldersApi->get_folder_by_folder_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_folder_by_folder_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| Folder ID | 
 **user_id_or_group_id** | **str**| User or group ID | [optional] 
 **filter_type** | [**FilterType**](.md)| Filter type | [optional] 
 **room_id** | **int**| Room ID | [optional] 
 **exclude_subject** | **bool**| Specifies whether to exclude a subject or not | [optional] 
 **apply_filter_option** | [**ApplyFilterOption**](.md)| Specifies whether to return only files, only folders or all elements from the specified folder | [optional] 
 **extension** | **str**| Specifies whether to search for a specific file extension | [optional] 
 **search_area** | [**SearchArea**](.md)| Search area | [optional] 
 **forms_item_key** | **str**|  | [optional] 
 **forms_item_type** | **str**|  | [optional] 

### Return type

[**FolderContentIntegerWrapper**](FolderContentIntegerWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder contents |  -  |
**403** | You don&#39;t have enough permission to view the folder content |  -  |
**404** | The required folder was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_history**
> HistoryArrayWrapper get_folder_history(folder_id, from_date=from_date, to_date=to_date)

Get folder history

Get the activity history of a folder with a specified identifier

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.api_date_time import ApiDateTime
from docspace.models.history_array_wrapper import HistoryArrayWrapper
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
    api_instance = docspace.FilesFoldersApi(api_client)
    folder_id = 9846 # int | File ID
    from_date = docspace.ApiDateTime() # ApiDateTime | Start date (optional)
    to_date = docspace.ApiDateTime() # ApiDateTime | End date (optional)

    try:
        # Get folder history
        api_response = api_instance.get_folder_history(folder_id, from_date=from_date, to_date=to_date)
        print("The response of FilesFoldersApi->get_folder_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_folder_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| File ID | 
 **from_date** | [**ApiDateTime**](.md)| Start date | [optional] 
 **to_date** | [**ApiDateTime**](.md)| End date | [optional] 

### Return type

[**HistoryArrayWrapper**](HistoryArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of actions in the folder |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to perform the operation |  -  |
**404** | The required folder was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_info**
> FolderIntegerWrapper get_folder_info(folder_id)

Get folder information

Returns the detailed information about a folder with the ID specified in the request.

### Example


```python
import docspace
from docspace.models.folder_integer_wrapper import FolderIntegerWrapper
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
    api_instance = docspace.FilesFoldersApi(api_client)
    folder_id = 9846 # int | Folder ID

    try:
        # Get folder information
        api_response = api_instance.get_folder_info(folder_id)
        print("The response of FilesFoldersApi->get_folder_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_folder_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| Folder ID | 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_path**
> FileEntryArrayWrapper get_folder_path(folder_id)

Get the folder path

Returns a path to the folder with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
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
    api_instance = docspace.FilesFoldersApi(api_client)
    folder_id = 9846 # int | Folder ID

    try:
        # Get the folder path
        api_response = api_instance.get_folder_path(folder_id)
        print("The response of FilesFoldersApi->get_folder_path:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_folder_path: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| Folder ID | 

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
**403** | You don&#39;t have enough permission to view the folder content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_primary_external_link**
> FileShareWrapper get_folder_primary_external_link(id)

Get primary external link

Returns the primary external link by the identifier specified in the request.

### Example


```python
import docspace
from docspace.models.file_share_wrapper import FileShareWrapper
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
    api_instance = docspace.FilesFoldersApi(api_client)
    id = 9846 # int | Folder Id

    try:
        # Get primary external link
        api_response = api_instance.get_folder_primary_external_link(id)
        print("The response of FilesFoldersApi->get_folder_primary_external_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_folder_primary_external_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Folder Id | 

### Return type

[**FileShareWrapper**](FileShareWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder security information |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folders**
> FileEntryArrayWrapper get_folders(folder_id)

Get subfolders

Returns a list of all the subfolders from a folder with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
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
    api_instance = docspace.FilesFoldersApi(api_client)
    folder_id = 9846 # int | Folder ID

    try:
        # Get subfolders
        api_response = api_instance.get_folders(folder_id)
        print("The response of FilesFoldersApi->get_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_folders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| Folder ID | 

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
**403** | You don&#39;t have enough permission to view the folder content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_folder**
> FolderContentIntegerWrapper get_my_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, apply_filter_option=apply_filter_option)

Get the \"My documents\" section

Returns the detailed list of files and folders located in the \"My documents\" section.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.apply_filter_option import ApplyFilterOption
from docspace.models.filter_type import FilterType
from docspace.models.folder_content_integer_wrapper import FolderContentIntegerWrapper
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
    api_instance = docspace.FilesFoldersApi(api_client)
    user_id_or_group_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | User or group ID (optional)
    filter_type = docspace.FilterType() # FilterType | Filter type (optional)
    apply_filter_option = docspace.ApplyFilterOption() # ApplyFilterOption | Specifies whether to return only files, only folders or all elements from the specified folder (optional)

    try:
        # Get the \"My documents\" section
        api_response = api_instance.get_my_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, apply_filter_option=apply_filter_option)
        print("The response of FilesFoldersApi->get_my_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_my_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_group_id** | **str**| User or group ID | [optional] 
 **filter_type** | [**FilterType**](.md)| Filter type | [optional] 
 **apply_filter_option** | [**ApplyFilterOption**](.md)| Specifies whether to return only files, only folders or all elements from the specified folder | [optional] 

### Return type

[**FolderContentIntegerWrapper**](FolderContentIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The \&quot;My documents\&quot; section contents |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to view the folder content |  -  |
**404** | The required folder was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_new_items**
> FileEntryArrayWrapper get_new_items(folder_id)

Get new folder items

Returns a list of all the new items from a folder with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
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
    api_instance = docspace.FilesFoldersApi(api_client)
    folder_id = 9846 # int | Folder ID

    try:
        # Get new folder items
        api_response = api_instance.get_new_items(folder_id)
        print("The response of FilesFoldersApi->get_new_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_new_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| Folder ID | 

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
**403** | You don&#39;t have enough permission to view the folder content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_privacy_folder**
> FolderContentIntegerWrapper get_privacy_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type)

Get the \"Private Room\" section

Returns the detailed list of files and folders located in the \"Private Room\" section.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.filter_type import FilterType
from docspace.models.folder_content_integer_wrapper import FolderContentIntegerWrapper
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
    api_instance = docspace.FilesFoldersApi(api_client)
    user_id_or_group_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | User or group ID (optional)
    filter_type = docspace.FilterType() # FilterType | Filter type (optional)

    try:
        # Get the \"Private Room\" section
        api_response = api_instance.get_privacy_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type)
        print("The response of FilesFoldersApi->get_privacy_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_privacy_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_group_id** | **str**| User or group ID | [optional] 
 **filter_type** | [**FilterType**](.md)| Filter type | [optional] 

### Return type

[**FolderContentIntegerWrapper**](FolderContentIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The \&quot;Private Room\&quot; section contents |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to view the folder content |  -  |
**404** | The required folder was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_root_folders**
> FolderContentIntegerArrayWrapper get_root_folders(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, without_trash=without_trash)

Get filtered sections

Returns all the sections matching the parameters specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.filter_type import FilterType
from docspace.models.folder_content_integer_array_wrapper import FolderContentIntegerArrayWrapper
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
    api_instance = docspace.FilesFoldersApi(api_client)
    user_id_or_group_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | User or group ID (optional)
    filter_type = docspace.FilterType() # FilterType | Filter type (optional)
    without_trash = true # bool | Specifies whether to return the \"Trash\" section or not (optional)

    try:
        # Get filtered sections
        api_response = api_instance.get_root_folders(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, without_trash=without_trash)
        print("The response of FilesFoldersApi->get_root_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_root_folders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_group_id** | **str**| User or group ID | [optional] 
 **filter_type** | [**FilterType**](.md)| Filter type | [optional] 
 **without_trash** | **bool**| Specifies whether to return the \&quot;Trash\&quot; section or not | [optional] 

### Return type

[**FolderContentIntegerArrayWrapper**](FolderContentIntegerArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of section contents with the following parameters |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to view the folder content |  -  |
**404** | The required folder was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trash_folder**
> FolderContentIntegerWrapper get_trash_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, apply_filter_option=apply_filter_option)

Get the \"Trash\" section

Returns the detailed list of files and folders located in the \"Trash\" section.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.apply_filter_option import ApplyFilterOption
from docspace.models.filter_type import FilterType
from docspace.models.folder_content_integer_wrapper import FolderContentIntegerWrapper
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
    api_instance = docspace.FilesFoldersApi(api_client)
    user_id_or_group_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | User or group ID (optional)
    filter_type = docspace.FilterType() # FilterType | Filter type (optional)
    apply_filter_option = docspace.ApplyFilterOption() # ApplyFilterOption | Specifies whether to return only files, only folders or all elements from the specified folder (optional)

    try:
        # Get the \"Trash\" section
        api_response = api_instance.get_trash_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, apply_filter_option=apply_filter_option)
        print("The response of FilesFoldersApi->get_trash_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_trash_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_group_id** | **str**| User or group ID | [optional] 
 **filter_type** | [**FilterType**](.md)| Filter type | [optional] 
 **apply_filter_option** | [**ApplyFilterOption**](.md)| Specifies whether to return only files, only folders or all elements from the specified folder | [optional] 

### Return type

[**FolderContentIntegerWrapper**](FolderContentIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The \&quot;Trash\&quot; section contents |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to view the folder content |  -  |
**404** | The required folder was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_file**
> FileIntegerWrapper insert_file(folder_id, insert_file_file=insert_file_file, insert_file_title=insert_file_title, insert_file_create_new_if_exist=insert_file_create_new_if_exist, insert_file_keep_convert_status=insert_file_keep_convert_status, insert_file_stream_can_read=insert_file_stream_can_read, insert_file_stream_can_write=insert_file_stream_can_write, insert_file_stream_can_seek=insert_file_stream_can_seek, insert_file_stream_can_timeout=insert_file_stream_can_timeout, insert_file_stream_length=insert_file_stream_length, insert_file_stream_position=insert_file_stream_position, insert_file_stream_read_timeout=insert_file_stream_read_timeout, insert_file_stream_write_timeout=insert_file_stream_write_timeout)

Insert a file

Inserts a file specified in the request to the selected folder by single file uploading.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.file_integer_wrapper import FileIntegerWrapper
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
    api_instance = docspace.FilesFoldersApi(api_client)
    folder_id = 9846 # int | Folder ID
    insert_file_file = None # bytearray | File (optional)
    insert_file_title = 'insert_file_title_example' # str | File name (optional)
    insert_file_create_new_if_exist = True # bool | Specifies whether to create a new file if it already exists or not (optional)
    insert_file_keep_convert_status = True # bool | Specifies whether to keep the file converting status or not (optional)
    insert_file_stream_can_read = True # bool |  (optional)
    insert_file_stream_can_write = True # bool |  (optional)
    insert_file_stream_can_seek = True # bool |  (optional)
    insert_file_stream_can_timeout = True # bool |  (optional)
    insert_file_stream_length = 56 # int |  (optional)
    insert_file_stream_position = 56 # int |  (optional)
    insert_file_stream_read_timeout = 56 # int |  (optional)
    insert_file_stream_write_timeout = 56 # int |  (optional)

    try:
        # Insert a file
        api_response = api_instance.insert_file(folder_id, insert_file_file=insert_file_file, insert_file_title=insert_file_title, insert_file_create_new_if_exist=insert_file_create_new_if_exist, insert_file_keep_convert_status=insert_file_keep_convert_status, insert_file_stream_can_read=insert_file_stream_can_read, insert_file_stream_can_write=insert_file_stream_can_write, insert_file_stream_can_seek=insert_file_stream_can_seek, insert_file_stream_can_timeout=insert_file_stream_can_timeout, insert_file_stream_length=insert_file_stream_length, insert_file_stream_position=insert_file_stream_position, insert_file_stream_read_timeout=insert_file_stream_read_timeout, insert_file_stream_write_timeout=insert_file_stream_write_timeout)
        print("The response of FilesFoldersApi->insert_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->insert_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| Folder ID | 
 **insert_file_file** | **bytearray**| File | [optional] 
 **insert_file_title** | **str**| File name | [optional] 
 **insert_file_create_new_if_exist** | **bool**| Specifies whether to create a new file if it already exists or not | [optional] 
 **insert_file_keep_convert_status** | **bool**| Specifies whether to keep the file converting status or not | [optional] 
 **insert_file_stream_can_read** | **bool**|  | [optional] 
 **insert_file_stream_can_write** | **bool**|  | [optional] 
 **insert_file_stream_can_seek** | **bool**|  | [optional] 
 **insert_file_stream_can_timeout** | **bool**|  | [optional] 
 **insert_file_stream_length** | **int**|  | [optional] 
 **insert_file_stream_position** | **int**|  | [optional] 
 **insert_file_stream_read_timeout** | **int**|  | [optional] 
 **insert_file_stream_write_timeout** | **int**|  | [optional] 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inserted file |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to create |  -  |
**404** | Folder not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_file_to_my_from_body**
> FileIntegerWrapper insert_file_to_my_from_body(file=file, title=title, create_new_if_exist=create_new_if_exist, keep_convert_status=keep_convert_status, stream_can_read=stream_can_read, stream_can_write=stream_can_write, stream_can_seek=stream_can_seek, stream_can_timeout=stream_can_timeout, stream_length=stream_length, stream_position=stream_position, stream_read_timeout=stream_read_timeout, stream_write_timeout=stream_write_timeout)

Insert a file to the \"My documents\" section

Inserts a file specified in the request to the \"My documents\" section by single file uploading.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.file_integer_wrapper import FileIntegerWrapper
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
    api_instance = docspace.FilesFoldersApi(api_client)
    file = None # bytearray | File (optional)
    title = 'title_example' # str | File name (optional)
    create_new_if_exist = True # bool | Specifies whether to create a new file if it already exists or not (optional)
    keep_convert_status = True # bool | Specifies whether to keep the file converting status or not (optional)
    stream_can_read = True # bool |  (optional)
    stream_can_write = True # bool |  (optional)
    stream_can_seek = True # bool |  (optional)
    stream_can_timeout = True # bool |  (optional)
    stream_length = 56 # int |  (optional)
    stream_position = 56 # int |  (optional)
    stream_read_timeout = 56 # int |  (optional)
    stream_write_timeout = 56 # int |  (optional)

    try:
        # Insert a file to the \"My documents\" section
        api_response = api_instance.insert_file_to_my_from_body(file=file, title=title, create_new_if_exist=create_new_if_exist, keep_convert_status=keep_convert_status, stream_can_read=stream_can_read, stream_can_write=stream_can_write, stream_can_seek=stream_can_seek, stream_can_timeout=stream_can_timeout, stream_length=stream_length, stream_position=stream_position, stream_read_timeout=stream_read_timeout, stream_write_timeout=stream_write_timeout)
        print("The response of FilesFoldersApi->insert_file_to_my_from_body:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->insert_file_to_my_from_body: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| File | [optional] 
 **title** | **str**| File name | [optional] 
 **create_new_if_exist** | **bool**| Specifies whether to create a new file if it already exists or not | [optional] 
 **keep_convert_status** | **bool**| Specifies whether to keep the file converting status or not | [optional] 
 **stream_can_read** | **bool**|  | [optional] 
 **stream_can_write** | **bool**|  | [optional] 
 **stream_can_seek** | **bool**|  | [optional] 
 **stream_can_timeout** | **bool**|  | [optional] 
 **stream_length** | **int**|  | [optional] 
 **stream_position** | **int**|  | [optional] 
 **stream_read_timeout** | **int**|  | [optional] 
 **stream_write_timeout** | **int**|  | [optional] 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inserted file |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to create |  -  |
**404** | Folder not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_folder**
> FolderIntegerWrapper rename_folder(folder_id, create_folder=create_folder)

Rename a folder

Renames the selected folder with a new title specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.create_folder import CreateFolder
from docspace.models.folder_integer_wrapper import FolderIntegerWrapper
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
    api_instance = docspace.FilesFoldersApi(api_client)
    folder_id = 9846 # int | Folder ID
    create_folder = docspace.CreateFolder() # CreateFolder | Folder (optional)

    try:
        # Rename a folder
        api_response = api_instance.rename_folder(folder_id, create_folder=create_folder)
        print("The response of FilesFoldersApi->rename_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->rename_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| Folder ID | 
 **create_folder** | [**CreateFolder**](CreateFolder.md)| Folder | [optional] 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder parameters |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to rename the folder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_file_order**
> set_file_order(folder_id, order_request_dto=order_request_dto)

Sets file order in the folder with ID specified in the request

Sets file order in the folder with ID specified in the request

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.order_request_dto import OrderRequestDto
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
    api_instance = docspace.FilesFoldersApi(api_client)
    folder_id = 9846 # int | The unique identifier of the folder
    order_request_dto = docspace.OrderRequestDto() # OrderRequestDto | Order information for the folder (optional)

    try:
        # Sets file order in the folder with ID specified in the request
        api_instance.set_file_order(folder_id, order_request_dto=order_request_dto)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->set_file_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The unique identifier of the folder | 
 **order_request_dto** | [**OrderRequestDto**](OrderRequestDto.md)| Order information for the folder | [optional] 

### Return type

void (empty response body)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> ObjectWrapper upload_file(folder_id, upload_request_dto=upload_request_dto)

Upload a file

Uploads a file specified in the request to the selected folder by single file uploading or standart multipart/form-data method.   **Note**:  You can upload files in two different ways:   <ol>  <li>Using single file upload. You should set the Content-Type and Content-Disposition headers to specify a file name and content type, and send the file to the request body.</li>  <li>Using standart multipart/form-data method.</li>  </ol>

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.object_wrapper import ObjectWrapper
from docspace.models.upload_request_dto import UploadRequestDto
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
    api_instance = docspace.FilesFoldersApi(api_client)
    folder_id = 9846 # int | Folder ID
    upload_request_dto = docspace.UploadRequestDto() # UploadRequestDto | Upload data (optional)

    try:
        # Upload a file
        api_response = api_instance.upload_file(folder_id, upload_request_dto=upload_request_dto)
        print("The response of FilesFoldersApi->upload_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->upload_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| Folder ID | 
 **upload_request_dto** | [**UploadRequestDto**](UploadRequestDto.md)| Upload data | [optional] 

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
**200** | Inserted file |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to create |  -  |
**404** | Folder not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file_to_my**
> ObjectWrapper upload_file_to_my(in_dto=in_dto)

Upload a file to the \"My documents\" section

Uploads a file specified in the request to the \"My documents\" section by single file uploading or standart multipart/form-data method.   **Note**:  You can upload files in two different ways:   <ol>  <li>Using single file upload. You should set the Content-Type and Content-Disposition headers to specify a file name and content type, and send the file to the request body.</li>  <li>Using standart multipart/form-data method.</li>  </ol>

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.object_wrapper import ObjectWrapper
from docspace.models.upload_request_dto import UploadRequestDto
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
    api_instance = docspace.FilesFoldersApi(api_client)
    in_dto = docspace.UploadRequestDto() # UploadRequestDto | Request parameters for uploading a file (optional)

    try:
        # Upload a file to the \"My documents\" section
        api_response = api_instance.upload_file_to_my(in_dto=in_dto)
        print("The response of FilesFoldersApi->upload_file_to_my:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->upload_file_to_my: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **in_dto** | [**UploadRequestDto**](.md)| Request parameters for uploading a file | [optional] 

### Return type

[**ObjectWrapper**](ObjectWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Uploaded file(s) |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to create |  -  |
**404** | File not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

