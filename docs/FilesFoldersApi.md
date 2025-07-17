# docspace-api-python.FilesFoldersApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_upload**](#check_upload) | **POST** /api/2.0/files/{folderId}/upload/check | Check file uploads
[**create_folder**](#create_folder) | **POST** /api/2.0/files/folder/{folderId} | Create a folder
[**delete_folder**](#delete_folder) | **DELETE** /api/2.0/files/folder/{folderId} | Delete a folder
[**get_files_used_space**](#get_files_used_space) | **GET** /api/2.0/files/filesusedspace | Get used space of files
[**get_folder**](#get_folder) | **GET** /api/2.0/files/{folderId}/formfilter | Get folder form filter
[**get_folder_by_folder_id**](#get_folder_by_folder_id) | **GET** /api/2.0/files/{folderId} | Get a folder by ID
[**get_folder_history**](#get_folder_history) | **GET** /api/2.0/files/folder/{folderId}/log | Get folder history
[**get_folder_info**](#get_folder_info) | **GET** /api/2.0/files/folder/{folderId} | Get folder information
[**get_folder_path**](#get_folder_path) | **GET** /api/2.0/files/folder/{folderId}/path | Get the folder path
[**get_folder_primary_external_link**](#get_folder_primary_external_link) | **GET** /api/2.0/files/folder/{id}/link | Get primary external link
[**get_folders**](#get_folders) | **GET** /api/2.0/files/{folderId}/subfolders | Get subfolders
[**get_my_folder**](#get_my_folder) | **GET** /api/2.0/files/@my | Get the \&quot;My documents\&quot; section
[**get_new_folder_items**](#get_new_folder_items) | **GET** /api/2.0/files/{folderId}/news | Get new folder items
[**get_privacy_folder**](#get_privacy_folder) | **GET** /api/2.0/files/@privacy | Get the \&quot;Private Room\&quot; section
[**get_root_folders**](#get_root_folders) | **GET** /api/2.0/files/@root | Get filtered sections
[**get_trash_folder**](#get_trash_folder) | **GET** /api/2.0/files/@trash | Get the \&quot;Trash\&quot; section
[**insert_file**](#insert_file) | **POST** /api/2.0/files/{folderId}/insert | Insert a file
[**insert_file_to_my_from_body**](#insert_file_to_my_from_body) | **POST** /api/2.0/files/@my/insert | Insert a file to the \&quot;My documents\&quot; section
[**rename_folder**](#rename_folder) | **PUT** /api/2.0/files/folder/{folderId} | Rename a folder
[**set_folder_order**](#set_folder_order) | **PUT** /api/2.0/files/folder/{folderId}/order | Set folder order
[**upload_file**](#upload_file) | **POST** /api/2.0/files/{folderId}/upload | Upload a file
[**upload_file_to_my**](#upload_file_to_my) | **POST** /api/2.0/files/@my/upload | Upload a file to the \&quot;My documents\&quot; section


# **check_upload**
> STRINGArrayWrapper check_upload(folder_id, check_upload_request=check_upload_request)

Checks the file uploads to the folder with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID. | 
 **check_upload_request** | [**CheckUploadRequest**](CheckUploadRequest.md)| The request parameters for checking file uploads. | [optional] 

### Return type

[**STRINGArrayWrapper**](STRINGArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.check_upload_request import CheckUploadRequest
from docspace-api-python.models.string_array_wrapper import STRINGArrayWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.FilesFoldersApi(api_client)
    folder_id = 9846 # int | The folder ID.
    check_upload_request = docspace-api-python.CheckUploadRequest() # CheckUploadRequest | The request parameters for checking file uploads. (optional)

    try:
        # Check file uploads
        api_response = api_instance.check_upload(folder_id, check_upload_request=check_upload_request)
        print("The response of FilesFoldersApi->check_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->check_upload: %s\n" % e)
```



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

Creates a new folder with the title specified in the request. The parent folder ID can be also specified.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID for the folder creation. | 
 **create_folder** | [**CreateFolder**](CreateFolder.md)| The parameters for creating a folder. | [optional] 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.create_folder import CreateFolder
from docspace-api-python.models.folder_integer_wrapper import FolderIntegerWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.FilesFoldersApi(api_client)
    folder_id = 9846 # int | The folder ID for the folder creation.
    create_folder = docspace-api-python.CreateFolder() # CreateFolder | The parameters for creating a folder. (optional)

    try:
        # Create a folder
        api_response = api_instance.create_folder(folder_id, create_folder=create_folder)
        print("The response of FilesFoldersApi->create_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->create_folder: %s\n" % e)
```



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

Deletes a folder with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID to delete. | 
 **delete_folder** | [**DeleteFolder**](DeleteFolder.md)| The parameters for deleting a folder. | [optional] 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.delete_folder import DeleteFolder
from docspace-api-python.models.file_operation_array_wrapper import FileOperationArrayWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.FilesFoldersApi(api_client)
    folder_id = 9846 # int | The folder ID to delete.
    delete_folder = docspace-api-python.DeleteFolder() # DeleteFolder | The parameters for deleting a folder. (optional)

    try:
        # Delete a folder
        api_response = api_instance.delete_folder(folder_id, delete_folder=delete_folder)
        print("The response of FilesFoldersApi->delete_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->delete_folder: %s\n" % e)
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

# **get_files_used_space**
> FilesStatisticsResultWrapper get_files_used_space()

Returns the used space of files in the root folders.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**FilesStatisticsResultWrapper**](FilesStatisticsResultWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.files_statistics_result_wrapper import FilesStatisticsResultWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.FilesFoldersApi(api_client)

    try:
        # Get used space of files
        api_response = api_instance.get_files_used_space()
        print("The response of FilesFoldersApi->get_files_used_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_files_used_space: %s\n" % e)
```



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

Returns the form filter of a folder with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The request folder ID. | 

### Return type

[**FormsItemArrayWrapper**](FormsItemArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace-api-python
from docspace-api-python.models.forms_item_array_wrapper import FormsItemArrayWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)


# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.FilesFoldersApi(api_client)
    folder_id = 9846 # int | The request folder ID.

    try:
        # Get folder form filter
        api_response = api_instance.get_folder(folder_id)
        print("The response of FilesFoldersApi->get_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_folder: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_by_folder_id**
> FolderContentIntegerWrapper get_folder_by_folder_id(folder_id, user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, room_id=room_id, exclude_subject=exclude_subject, apply_filter_option=apply_filter_option, extension=extension, search_area=search_area, forms_item_key=forms_item_key, forms_item_type=forms_item_type, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)

Returns the detailed list of files and folders located in the folder with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID of the request. | 
 **user_id_or_group_id** | **str**| The user or group ID. | [optional] 
 **filter_type** | [**FilterType**](.md)| The filter type. | [optional] 
 **room_id** | **int**| The room ID. | [optional] 
 **exclude_subject** | **bool**| Specifies whether to exclude search by user or group ID. | [optional] 
 **apply_filter_option** | [**ApplyFilterOption**](.md)| Specifies whether to return only files, only folders or all elements from the specified folder. | [optional] 
 **extension** | **str**| Specifies whether to search for the specific file extension. | [optional] 
 **search_area** | [**SearchArea**](.md)| The search area. | [optional] 
 **forms_item_key** | **str**| The forms item key. | [optional] 
 **forms_item_type** | **str**| The forms item type. | [optional] 
 **count** | **int**| The maximum number of items to retrieve in the request. | [optional] 
 **start_index** | **int**| The zero-based index of the first item to retrieve in a paginated request. | [optional] 
 **sort_by** | **str**| Specifies the property used for sorting the folder request results. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The order in which the results are sorted. | [optional] 
 **filter_value** | **str**| The text value used as a filter parameter for folder content queries. | [optional] 

### Return type

[**FolderContentIntegerWrapper**](FolderContentIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace-api-python
from docspace-api-python.models.apply_filter_option import ApplyFilterOption
from docspace-api-python.models.filter_type import FilterType
from docspace-api-python.models.folder_content_integer_wrapper import FolderContentIntegerWrapper
from docspace-api-python.models.search_area import SearchArea
from docspace-api-python.models.sort_order import SortOrder
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)


# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.FilesFoldersApi(api_client)
    folder_id = 9846 # int | The folder ID of the request.
    user_id_or_group_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | The user or group ID. (optional)
    filter_type = docspace-api-python.FilterType() # FilterType | The filter type. (optional)
    room_id = 9846 # int | The room ID. (optional)
    exclude_subject = true # bool | Specifies whether to exclude search by user or group ID. (optional)
    apply_filter_option = docspace-api-python.ApplyFilterOption() # ApplyFilterOption | Specifies whether to return only files, only folders or all elements from the specified folder. (optional)
    extension = '.txt' # str | Specifies whether to search for the specific file extension. (optional)
    search_area = docspace-api-python.SearchArea() # SearchArea | The search area. (optional)
    forms_item_key = 'some text' # str | The forms item key. (optional)
    forms_item_type = 'some text' # str | The forms item type. (optional)
    count = 1234 # int | The maximum number of items to retrieve in the request. (optional)
    start_index = 1234 # int | The zero-based index of the first item to retrieve in a paginated request. (optional)
    sort_by = 'some text' # str | Specifies the property used for sorting the folder request results. (optional)
    sort_order = docspace-api-python.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_value = 'some text' # str | The text value used as a filter parameter for folder content queries. (optional)

    try:
        # Get a folder by ID
        api_response = api_instance.get_folder_by_folder_id(folder_id, user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, room_id=room_id, exclude_subject=exclude_subject, apply_filter_option=apply_filter_option, extension=extension, search_area=search_area, forms_item_key=forms_item_key, forms_item_type=forms_item_type, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)
        print("The response of FilesFoldersApi->get_folder_by_folder_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_folder_by_folder_id: %s\n" % e)
```



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
> HistoryArrayWrapper get_folder_history(folder_id, from_date=from_date, to_date=to_date, count=count, start_index=start_index)

Returns the activity history of a folder with a specified identifier.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID of the history request. | 
 **from_date** | [**ApiDateTime**](.md)| The start date of the history request. | [optional] 
 **to_date** | [**ApiDateTime**](.md)| The end date of the history request. | [optional] 
 **count** | **int**| The number of records to retrieve for the folder history. | [optional] 
 **start_index** | **int**| The starting index from which the history records are retrieved in the request. | [optional] 

### Return type

[**HistoryArrayWrapper**](HistoryArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.api_date_time import ApiDateTime
from docspace-api-python.models.history_array_wrapper import HistoryArrayWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.FilesFoldersApi(api_client)
    folder_id = 9846 # int | The folder ID of the history request.
    from_date = docspace-api-python.ApiDateTime() # ApiDateTime | The start date of the history request. (optional)
    to_date = docspace-api-python.ApiDateTime() # ApiDateTime | The end date of the history request. (optional)
    count = 1234 # int | The number of records to retrieve for the folder history. (optional)
    start_index = 1234 # int | The starting index from which the history records are retrieved in the request. (optional)

    try:
        # Get folder history
        api_response = api_instance.get_folder_history(folder_id, from_date=from_date, to_date=to_date, count=count, start_index=start_index)
        print("The response of FilesFoldersApi->get_folder_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_folder_history: %s\n" % e)
```



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

Returns the detailed information about a folder with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The request folder ID. | 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace-api-python
from docspace-api-python.models.folder_integer_wrapper import FolderIntegerWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)


# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.FilesFoldersApi(api_client)
    folder_id = 9846 # int | The request folder ID.

    try:
        # Get folder information
        api_response = api_instance.get_folder_info(folder_id)
        print("The response of FilesFoldersApi->get_folder_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_folder_info: %s\n" % e)
```



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

Returns a path to the folder with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The request folder ID. | 

### Return type

[**FileEntryArrayWrapper**](FileEntryArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.file_entry_array_wrapper import FileEntryArrayWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.FilesFoldersApi(api_client)
    folder_id = 9846 # int | The request folder ID.

    try:
        # Get the folder path
        api_response = api_instance.get_folder_path(folder_id)
        print("The response of FilesFoldersApi->get_folder_path:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_folder_path: %s\n" % e)
```



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

Returns the primary external link by the identifier specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The request folder ID. | 

### Return type

[**FileShareWrapper**](FileShareWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace-api-python
from docspace-api-python.models.file_share_wrapper import FileShareWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)


# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.FilesFoldersApi(api_client)
    id = 9846 # int | The request folder ID.

    try:
        # Get primary external link
        api_response = api_instance.get_folder_primary_external_link(id)
        print("The response of FilesFoldersApi->get_folder_primary_external_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_folder_primary_external_link: %s\n" % e)
```



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

Returns a list of all the subfolders from a folder with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The request folder ID. | 

### Return type

[**FileEntryArrayWrapper**](FileEntryArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.file_entry_array_wrapper import FileEntryArrayWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.FilesFoldersApi(api_client)
    folder_id = 9846 # int | The request folder ID.

    try:
        # Get subfolders
        api_response = api_instance.get_folders(folder_id)
        print("The response of FilesFoldersApi->get_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_folders: %s\n" % e)
```



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
> FolderContentIntegerWrapper get_my_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, apply_filter_option=apply_filter_option, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value, fields=fields)

Returns the detailed list of files and folders located in the "My documents" section.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_group_id** | **str**| The user or group ID. | [optional] 
 **filter_type** | [**FilterType**](.md)| The filter type. | [optional] 
 **apply_filter_option** | [**ApplyFilterOption**](.md)| Specifies whether to return only files, only folders or all elements. | [optional] 
 **count** | **int**| The maximum number of items to retrieve in the response. | [optional] 
 **start_index** | **int**| The starting position of the items to be retrieved. | [optional] 
 **sort_by** | **str**| The property used to specify the sorting criteria for folder contents. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The order in which the results are sorted. | [optional] 
 **filter_value** | **str**| The text used for filtering or searching folder contents. | [optional] 
 **fields** | **string**| Comma-separated list of fields to include in the response | [optional] 

### Return type

[**FolderContentIntegerWrapper**](FolderContentIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.apply_filter_option import ApplyFilterOption
from docspace-api-python.models.filter_type import FilterType
from docspace-api-python.models.folder_content_integer_wrapper import FolderContentIntegerWrapper
from docspace-api-python.models.sort_order import SortOrder
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.FilesFoldersApi(api_client)
    user_id_or_group_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | The user or group ID. (optional)
    filter_type = docspace-api-python.FilterType() # FilterType | The filter type. (optional)
    apply_filter_option = docspace-api-python.ApplyFilterOption() # ApplyFilterOption | Specifies whether to return only files, only folders or all elements. (optional)
    count = 1234 # int | The maximum number of items to retrieve in the response. (optional)
    start_index = 1234 # int | The starting position of the items to be retrieved. (optional)
    sort_by = 'some text' # str | The property used to specify the sorting criteria for folder contents. (optional)
    sort_order = docspace-api-python.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_value = 'some text' # str | The text used for filtering or searching folder contents. (optional)
    fields =  # string | Comma-separated list of fields to include in the response (optional)

    try:
        # Get the \"My documents\" section
        api_response = api_instance.get_my_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, apply_filter_option=apply_filter_option, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value, fields=fields)
        print("The response of FilesFoldersApi->get_my_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_my_folder: %s\n" % e)
```



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

# **get_new_folder_items**
> FileEntryArrayWrapper get_new_folder_items(folder_id)

Returns a list of all the new items from a folder with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The request folder ID. | 

### Return type

[**FileEntryArrayWrapper**](FileEntryArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.file_entry_array_wrapper import FileEntryArrayWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.FilesFoldersApi(api_client)
    folder_id = 9846 # int | The request folder ID.

    try:
        # Get new folder items
        api_response = api_instance.get_new_folder_items(folder_id)
        print("The response of FilesFoldersApi->get_new_folder_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_new_folder_items: %s\n" % e)
```



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
> FolderContentIntegerWrapper get_privacy_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value, fields=fields)

Returns the detailed list of files and folders located in the "Private Room" section.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_group_id** | **str**| The user or group ID. | [optional] 
 **filter_type** | [**FilterType**](.md)| The filter type. | [optional] 
 **count** | **int**| The maximum number of items to retrieve in the request. | [optional] 
 **start_index** | **int**| The zero-based index of the first item to retrieve in a paginated list. | [optional] 
 **sort_by** | **str**| Specifies the field by which the folder content should be sorted. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The order in which the results are sorted. | [optional] 
 **filter_value** | **str**| The text used as a filter or search criterion for folder content queries. | [optional] 
 **fields** | **string**| Comma-separated list of fields to include in the response | [optional] 

### Return type

[**FolderContentIntegerWrapper**](FolderContentIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.filter_type import FilterType
from docspace-api-python.models.folder_content_integer_wrapper import FolderContentIntegerWrapper
from docspace-api-python.models.sort_order import SortOrder
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.FilesFoldersApi(api_client)
    user_id_or_group_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | The user or group ID. (optional)
    filter_type = docspace-api-python.FilterType() # FilterType | The filter type. (optional)
    count = 1234 # int | The maximum number of items to retrieve in the request. (optional)
    start_index = 1234 # int | The zero-based index of the first item to retrieve in a paginated list. (optional)
    sort_by = 'some text' # str | Specifies the field by which the folder content should be sorted. (optional)
    sort_order = docspace-api-python.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_value = 'some text' # str | The text used as a filter or search criterion for folder content queries. (optional)
    fields =  # string | Comma-separated list of fields to include in the response (optional)

    try:
        # Get the \"Private Room\" section
        api_response = api_instance.get_privacy_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value, fields=fields)
        print("The response of FilesFoldersApi->get_privacy_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_privacy_folder: %s\n" % e)
```



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
> FolderContentIntegerArrayWrapper get_root_folders(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, without_trash=without_trash, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value, fields=fields)

Returns all the sections matching the parameters specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_group_id** | **str**| The user or group ID. | [optional] 
 **filter_type** | [**FilterType**](.md)| The filter type. | [optional] 
 **without_trash** | **bool**| Specifies whether to return the \&quot;Trash\&quot; section or not. | [optional] 
 **count** | **int**| The maximum number of items to retrieve in the response. | [optional] 
 **start_index** | **int**| The starting position of the items to be retrieved. | [optional] 
 **sort_by** | **str**| Specifies the field by which the folder content should be sorted. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The order in which the results are sorted. | [optional] 
 **filter_value** | **str**| The text used as a filter for searching or retrieving folder contents. | [optional] 
 **fields** | **string**| Comma-separated list of fields to include in the response | [optional] 

### Return type

[**FolderContentIntegerArrayWrapper**](FolderContentIntegerArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.filter_type import FilterType
from docspace-api-python.models.folder_content_integer_array_wrapper import FolderContentIntegerArrayWrapper
from docspace-api-python.models.sort_order import SortOrder
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.FilesFoldersApi(api_client)
    user_id_or_group_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | The user or group ID. (optional)
    filter_type = docspace-api-python.FilterType() # FilterType | The filter type. (optional)
    without_trash = true # bool | Specifies whether to return the \"Trash\" section or not. (optional)
    count = 1234 # int | The maximum number of items to retrieve in the response. (optional)
    start_index = 1234 # int | The starting position of the items to be retrieved. (optional)
    sort_by = 'some text' # str | Specifies the field by which the folder content should be sorted. (optional)
    sort_order = docspace-api-python.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_value = 'some text' # str | The text used as a filter for searching or retrieving folder contents. (optional)
    fields =  # string | Comma-separated list of fields to include in the response (optional)

    try:
        # Get filtered sections
        api_response = api_instance.get_root_folders(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, without_trash=without_trash, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value, fields=fields)
        print("The response of FilesFoldersApi->get_root_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_root_folders: %s\n" % e)
```



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
> FolderContentIntegerWrapper get_trash_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, apply_filter_option=apply_filter_option, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value, fields=fields)

Returns the detailed list of files and folders located in the "Trash" section.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_group_id** | **str**| The user or group ID. | [optional] 
 **filter_type** | [**FilterType**](.md)| The filter type. | [optional] 
 **apply_filter_option** | [**ApplyFilterOption**](.md)| Specifies whether to return only files, only folders or all elements. | [optional] 
 **count** | **int**| The maximum number of items to retrieve in the response. | [optional] 
 **start_index** | **int**| The starting position of the items to be retrieved. | [optional] 
 **sort_by** | **str**| The property used to specify the sorting criteria for folder contents. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The order in which the results are sorted. | [optional] 
 **filter_value** | **str**| The text used for filtering or searching folder contents. | [optional] 
 **fields** | **string**| Comma-separated list of fields to include in the response | [optional] 

### Return type

[**FolderContentIntegerWrapper**](FolderContentIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.apply_filter_option import ApplyFilterOption
from docspace-api-python.models.filter_type import FilterType
from docspace-api-python.models.folder_content_integer_wrapper import FolderContentIntegerWrapper
from docspace-api-python.models.sort_order import SortOrder
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.FilesFoldersApi(api_client)
    user_id_or_group_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | The user or group ID. (optional)
    filter_type = docspace-api-python.FilterType() # FilterType | The filter type. (optional)
    apply_filter_option = docspace-api-python.ApplyFilterOption() # ApplyFilterOption | Specifies whether to return only files, only folders or all elements. (optional)
    count = 1234 # int | The maximum number of items to retrieve in the response. (optional)
    start_index = 1234 # int | The starting position of the items to be retrieved. (optional)
    sort_by = 'some text' # str | The property used to specify the sorting criteria for folder contents. (optional)
    sort_order = docspace-api-python.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_value = 'some text' # str | The text used for filtering or searching folder contents. (optional)
    fields =  # string | Comma-separated list of fields to include in the response (optional)

    try:
        # Get the \"Trash\" section
        api_response = api_instance.get_trash_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, apply_filter_option=apply_filter_option, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value, fields=fields)
        print("The response of FilesFoldersApi->get_trash_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->get_trash_folder: %s\n" % e)
```



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

Inserts a file specified in the request to the selected folder by single file uploading.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID for inserting a file. | 
 **insert_file_file** | **bytearray**| The file to be inserted. | [optional] 
 **insert_file_title** | **str**| The file title to be inserted. | [optional] 
 **insert_file_create_new_if_exist** | **bool**| Specifies whether to create a new file if it already exists or not. | [optional] 
 **insert_file_keep_convert_status** | **bool**| Specifies whether to keep the file converting status or not. | [optional] 
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

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.file_integer_wrapper import FileIntegerWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.FilesFoldersApi(api_client)
    folder_id = 9846 # int | The folder ID for inserting a file.
    insert_file_file = None # bytearray | The file to be inserted. (optional)
    insert_file_title = 'insert_file_title_example' # str | The file title to be inserted. (optional)
    insert_file_create_new_if_exist = True # bool | Specifies whether to create a new file if it already exists or not. (optional)
    insert_file_keep_convert_status = True # bool | Specifies whether to keep the file converting status or not. (optional)
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

Inserts a file specified in the request to the "My documents" section by single file uploading.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| The file to be inserted. | [optional] 
 **title** | **str**| The file title to be inserted. | [optional] 
 **create_new_if_exist** | **bool**| Specifies whether to create a new file if it already exists or not. | [optional] 
 **keep_convert_status** | **bool**| Specifies whether to keep the file converting status or not. | [optional] 
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

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.file_integer_wrapper import FileIntegerWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.FilesFoldersApi(api_client)
    file = None # bytearray | The file to be inserted. (optional)
    title = 'title_example' # str | The file title to be inserted. (optional)
    create_new_if_exist = True # bool | Specifies whether to create a new file if it already exists or not. (optional)
    keep_convert_status = True # bool | Specifies whether to keep the file converting status or not. (optional)
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

Renames the selected folder with a new title specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID for the folder creation. | 
 **create_folder** | [**CreateFolder**](CreateFolder.md)| The parameters for creating a folder. | [optional] 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.create_folder import CreateFolder
from docspace-api-python.models.folder_integer_wrapper import FolderIntegerWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.FilesFoldersApi(api_client)
    folder_id = 9846 # int | The folder ID for the folder creation.
    create_folder = docspace-api-python.CreateFolder() # CreateFolder | The parameters for creating a folder. (optional)

    try:
        # Rename a folder
        api_response = api_instance.rename_folder(folder_id, create_folder=create_folder)
        print("The response of FilesFoldersApi->rename_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->rename_folder: %s\n" % e)
```



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

# **set_folder_order**
> FolderIntegerWrapper set_folder_order(folder_id, order_request_dto=order_request_dto)

Sets the file order in the folder with ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder unique identifier. | 
 **order_request_dto** | [**OrderRequestDto**](OrderRequestDto.md)| The folder order information. | [optional] 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.folder_integer_wrapper import FolderIntegerWrapper
from docspace-api-python.models.order_request_dto import OrderRequestDto
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.FilesFoldersApi(api_client)
    folder_id = 9846 # int | The folder unique identifier.
    order_request_dto = docspace-api-python.OrderRequestDto() # OrderRequestDto | The folder order information. (optional)

    try:
        # Set folder order
        api_response = api_instance.set_folder_order(folder_id, order_request_dto=order_request_dto)
        print("The response of FilesFoldersApi->set_folder_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->set_folder_order: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> ObjectWrapper upload_file(folder_id, upload_request_dto=upload_request_dto)

Uploads a file specified in the request to the selected folder by single file uploading or standart multipart/form-data method.

 **Note**:  You can upload files in two different ways:
 <ol>
<li>Using single file upload. You should set the Content-Type and Content-Disposition headers to specify a file name and content type, and send the file to the request body.</li>
<li>Using standart multipart/form-data method.</li>
</ol>

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID to upload a file. | 
 **upload_request_dto** | [**UploadRequestDto**](UploadRequestDto.md)| The request parameters for uploading a file. | [optional] 

### Return type

[**ObjectWrapper**](ObjectWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.object_wrapper import ObjectWrapper
from docspace-api-python.models.upload_request_dto import UploadRequestDto
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.FilesFoldersApi(api_client)
    folder_id = 9846 # int | The folder ID to upload a file.
    upload_request_dto = docspace-api-python.UploadRequestDto() # UploadRequestDto | The request parameters for uploading a file. (optional)

    try:
        # Upload a file
        api_response = api_instance.upload_file(folder_id, upload_request_dto=upload_request_dto)
        print("The response of FilesFoldersApi->upload_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->upload_file: %s\n" % e)
```



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

Uploads a file specified in the request to the "My documents" section by single file uploading or standart multipart/form-data method.

 **Note**:  You can upload files in two different ways:
 <ol>
<li>Using single file upload. You should set the Content-Type and Content-Disposition headers to specify a file name and content type, and send the file to the request body.</li>
<li>Using standart multipart/form-data method.</li>
</ol>

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **in_dto** | [**UploadRequestDto**](.md)| The request parameters for uploading a file. | [optional] 

### Return type

[**ObjectWrapper**](ObjectWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.object_wrapper import ObjectWrapper
from docspace-api-python.models.upload_request_dto import UploadRequestDto
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.FilesFoldersApi(api_client)
    in_dto = docspace-api-python.UploadRequestDto() # UploadRequestDto | The request parameters for uploading a file. (optional)

    try:
        # Upload a file to the \"My documents\" section
        api_response = api_instance.upload_file_to_my(in_dto=in_dto)
        print("The response of FilesFoldersApi->upload_file_to_my:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFoldersApi->upload_file_to_my: %s\n" % e)
```



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

