# docspace_api_sdk.FoldersApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_upload**](#check_upload) | **POST** /api/2.0/files/{folderId}/upload/check | 
[**create_folder**](#create_folder) | **POST** /api/2.0/files/folder/{folderId} | 
[**create_folder_primary_external_link**](#create_folder_primary_external_link) | **POST** /api/2.0/files/folder/{id}/link | 
[**create_report_folder_history**](#create_report_folder_history) | **POST** /api/2.0/files/folder/{folderId}/log/report | 
[**delete_folder**](#delete_folder) | **DELETE** /api/2.0/files/folder/{folderId} | 
[**get_favorites_folder**](#get_favorites_folder) | **GET** /api/2.0/files/@favorites | 
[**get_files_used_space**](#get_files_used_space) | **GET** /api/2.0/files/filesusedspace | 
[**get_folder**](#get_folder) | **GET** /api/2.0/files/{folderId}/formfilter | 
[**get_folder_by_folder_id**](#get_folder_by_folder_id) | **GET** /api/2.0/files/{folderId} | 
[**get_folder_history**](#get_folder_history) | **GET** /api/2.0/files/folder/{folderId}/log | 
[**get_folder_info**](#get_folder_info) | **GET** /api/2.0/files/folder/{folderId} | 
[**get_folder_links**](#get_folder_links) | **GET** /api/2.0/files/folder/{id}/links | 
[**get_folder_path**](#get_folder_path) | **GET** /api/2.0/files/folder/{folderId}/path | 
[**get_folder_primary_external_link**](#get_folder_primary_external_link) | **GET** /api/2.0/files/folder/{id}/link | 
[**get_folder_recent**](#get_folder_recent) | **GET** /api/2.0/files/recent | 
[**get_folders**](#get_folders) | **GET** /api/2.0/files/{folderId}/subfolders | 
[**get_my_folder**](#get_my_folder) | **GET** /api/2.0/files/@my | 
[**get_new_folder_items**](#get_new_folder_items) | **GET** /api/2.0/files/{folderId}/news | 
[**get_privacy_folder**](#get_privacy_folder) | **GET** /api/2.0/files/@privacy | 
[**get_recent_folder**](#get_recent_folder) | **GET** /api/2.0/files/@recent | 
[**get_root_folders**](#get_root_folders) | **GET** /api/2.0/files/@root | 
[**get_trash_folder**](#get_trash_folder) | **GET** /api/2.0/files/@trash | 
[**insert_file**](#insert_file) | **POST** /api/2.0/files/{folderId}/insert | 
[**insert_file_to_my_from_body**](#insert_file_to_my_from_body) | **POST** /api/2.0/files/@my/insert | 
[**rename_folder**](#rename_folder) | **PUT** /api/2.0/files/folder/{folderId} | 
[**set_folder_order**](#set_folder_order) | **PUT** /api/2.0/files/folder/{folderId}/order | 
[**set_folder_primary_external_link**](#set_folder_primary_external_link) | **PUT** /api/2.0/files/folder/{id}/links | 
[**upload_file**](#upload_file) | **POST** /api/2.0/files/{folderId}/upload | 
[**upload_file_to_my**](#upload_file_to_my) | **POST** /api/2.0/files/@my/upload | 


# **check_upload**
> STRINGArrayWrapper check_upload(folder_id, check_upload_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID. | 
 **check_upload_request** | [**CheckUploadRequest**](CheckUploadRequest.md)| The request parameters for checking file uploads. | 

### Return type

[**STRINGArrayWrapper**](STRINGArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.check_upload_request import CheckUploadRequest
from docspace_api_sdk.models.string_array_wrapper import STRINGArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 9846 # int | The folder ID.
    check_upload_request = docspace_api_sdk.CheckUploadRequest() # CheckUploadRequest | The request parameters for checking file uploads.

    try:
        api_response = api_instance.check_upload(folder_id, check_upload_request)
        print("The response of FoldersApi->check_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->check_upload: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inserted file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder**
> FolderIntegerWrapper create_folder(folder_id, create_folder)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID for the folder creation. | 
 **create_folder** | [**CreateFolder**](CreateFolder.md)| The parameters for creating a folder. | 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.create_folder import CreateFolder
from docspace_api_sdk.models.folder_integer_wrapper import FolderIntegerWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 9846 # int | The folder ID for the folder creation.
    create_folder = docspace_api_sdk.CreateFolder() # CreateFolder | The parameters for creating a folder.

    try:
        api_response = api_instance.create_folder(folder_id, create_folder)
        print("The response of FoldersApi->create_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->create_folder: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New folder parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder_primary_external_link**
> FileShareWrapper create_folder_primary_external_link(id, folder_link_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The folder ID. | 
 **folder_link_request** | [**FolderLinkRequest**](FolderLinkRequest.md)| The folder link parameters. | 

### Return type

[**FileShareWrapper**](FileShareWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_share_wrapper import FileShareWrapper
from docspace_api_sdk.models.folder_link_request import FolderLinkRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    id = 9846 # int | The folder ID.
    folder_link_request = docspace_api_sdk.FolderLinkRequest() # FolderLinkRequest | The folder link parameters.

    try:
        api_response = api_instance.create_folder_primary_external_link(id, folder_link_request)
        print("The response of FoldersApi->create_folder_primary_external_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->create_folder_primary_external_link: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folders security information |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_report_folder_history**
> StringWrapper create_report_folder_history(folder_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**|  | 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.string_wrapper import StringWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 56 # int | 

    try:
        api_response = api_instance.create_report_folder_history(folder_id)
        print("The response of FoldersApi->create_report_folder_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->create_report_folder_history: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | URL to the report file |  -  |
**403** | You don&#39;t have enough permission to perform the operation |  -  |
**404** | The required folder was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> FileOperationArrayWrapper delete_folder(folder_id, delete_folder)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID to delete. | 
 **delete_folder** | [**DeleteFolder**](DeleteFolder.md)| The parameters for deleting a folder. | 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.delete_folder import DeleteFolder
from docspace_api_sdk.models.file_operation_array_wrapper import FileOperationArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 9846 # int | The folder ID to delete.
    delete_folder = docspace_api_sdk.DeleteFolder() # DeleteFolder | The parameters for deleting a folder.

    try:
        api_response = api_instance.delete_folder(folder_id, delete_folder)
        print("The response of FoldersApi->delete_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->delete_folder: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file operations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorites_folder**
> FolderContentIntegerWrapper get_favorites_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)



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

### Return type

[**FolderContentIntegerWrapper**](FolderContentIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.filter_type import FilterType
from docspace_api_sdk.models.folder_content_integer_wrapper import FolderContentIntegerWrapper
from docspace_api_sdk.models.sort_order import SortOrder
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    user_id_or_group_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | The user or group ID. (optional)
    filter_type = docspace_api_sdk.FilterType() # FilterType | The filter type. (optional)
    count = 1234 # int | The maximum number of items to retrieve in the request. (optional)
    start_index = 1234 # int | The zero-based index of the first item to retrieve in a paginated list. (optional)
    sort_by = 'some text' # str | Specifies the field by which the folder content should be sorted. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_value = 'some text' # str | The text used as a filter or search criterion for folder content queries. (optional)

    try:
        api_response = api_instance.get_favorites_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)
        print("The response of FoldersApi->get_favorites_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_favorites_folder: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Favorites section contents |  -  |
**403** | You don&#39;t have enough permission to view the folder content |  -  |
**404** | The required folder was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files_used_space**
> FilesStatisticsResultWrapper get_files_used_space()



For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**FilesStatisticsResultWrapper**](FilesStatisticsResultWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.files_statistics_result_wrapper import FilesStatisticsResultWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)

    try:
        api_response = api_instance.get_files_used_space()
        print("The response of FoldersApi->get_files_used_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_files_used_space: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Used space of files in the root folders |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder**
> FormsItemArrayWrapper get_folder(folder_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder unique identifier. | 

### Return type

[**FormsItemArrayWrapper**](FormsItemArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.forms_item_array_wrapper import FormsItemArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 9846 # int | The folder unique identifier.

    try:
        api_response = api_instance.get_folder(folder_id)
        print("The response of FoldersApi->get_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_folder: %s\n" % e)
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
> FolderContentIntegerWrapper get_folder_by_folder_id(folder_id, user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, room_id=room_id, exclude_subject=exclude_subject, apply_filter_option=apply_filter_option, extension=extension, search_area=search_area, forms_item_key=forms_item_key, forms_item_type=forms_item_type, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value, location=location)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID. | 
 **user_id_or_group_id** | **str**| The user or group ID. | [optional] 
 **filter_type** | [**FilterType**](.md)| The filter type. | [optional] 
 **room_id** | **int**| The room ID. | [optional] 
 **exclude_subject** | **bool**| Specifies whether to exclude search by user or group ID. | [optional] 
 **apply_filter_option** | [**ApplyFilterOption**](.md)| Specifies whether to return only files, only folders, or all elements from the specified folder. | [optional] 
 **extension** | **str**| Specifies whether to search for the specific file extension. | [optional] 
 **search_area** | [**SearchArea**](.md)| The search area. | [optional] 
 **forms_item_key** | **str**| The forms item key. | [optional] 
 **forms_item_type** | **str**| The forms item type. | [optional] 
 **count** | **int**| The maximum number of items to retrieve in the request. | [optional] 
 **start_index** | **int**| The zero-based index of the first item to retrieve in a paginated request. | [optional] 
 **sort_by** | **str**| The property used for sorting the folder request results. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The order in which the results are sorted. | [optional] 
 **filter_value** | **str**| The text value used as a filter parameter for folder content queries. | [optional] 
 **location** | [**Location**](.md)| The location context of the request, specifying the area  where the operation is performed, such as a room, documents, or a link. | [optional] 

### Return type

[**FolderContentIntegerWrapper**](FolderContentIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.apply_filter_option import ApplyFilterOption
from docspace_api_sdk.models.filter_type import FilterType
from docspace_api_sdk.models.folder_content_integer_wrapper import FolderContentIntegerWrapper
from docspace_api_sdk.models.location import Location
from docspace_api_sdk.models.search_area import SearchArea
from docspace_api_sdk.models.sort_order import SortOrder
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 9846 # int | The folder ID.
    user_id_or_group_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | The user or group ID. (optional)
    filter_type = docspace_api_sdk.FilterType() # FilterType | The filter type. (optional)
    room_id = 9846 # int | The room ID. (optional)
    exclude_subject = true # bool | Specifies whether to exclude search by user or group ID. (optional)
    apply_filter_option = docspace_api_sdk.ApplyFilterOption() # ApplyFilterOption | Specifies whether to return only files, only folders, or all elements from the specified folder. (optional)
    extension = '.txt' # str | Specifies whether to search for the specific file extension. (optional)
    search_area = docspace_api_sdk.SearchArea() # SearchArea | The search area. (optional)
    forms_item_key = 'some text' # str | The forms item key. (optional)
    forms_item_type = 'some text' # str | The forms item type. (optional)
    count = 1234 # int | The maximum number of items to retrieve in the request. (optional)
    start_index = 1234 # int | The zero-based index of the first item to retrieve in a paginated request. (optional)
    sort_by = 'some text' # str | The property used for sorting the folder request results. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_value = 'some text' # str | The text value used as a filter parameter for folder content queries. (optional)
    location = docspace_api_sdk.Location() # Location | The location context of the request, specifying the area  where the operation is performed, such as a room, documents, or a link. (optional)

    try:
        api_response = api_instance.get_folder_by_folder_id(folder_id, user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, room_id=room_id, exclude_subject=exclude_subject, apply_filter_option=apply_filter_option, extension=extension, search_area=search_area, forms_item_key=forms_item_key, forms_item_type=forms_item_type, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value, location=location)
        print("The response of FoldersApi->get_folder_by_folder_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_folder_by_folder_id: %s\n" % e)
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

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.api_date_time import ApiDateTime
from docspace_api_sdk.models.history_array_wrapper import HistoryArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 9846 # int | The folder ID of the history request.
    from_date = docspace_api_sdk.ApiDateTime() # ApiDateTime | The start date of the history request. (optional)
    to_date = docspace_api_sdk.ApiDateTime() # ApiDateTime | The end date of the history request. (optional)
    count = 1234 # int | The number of records to retrieve for the folder history. (optional)
    start_index = 1234 # int | The starting index from which the history records are retrieved in the request. (optional)

    try:
        api_response = api_instance.get_folder_history(folder_id, from_date=from_date, to_date=to_date, count=count, start_index=start_index)
        print("The response of FoldersApi->get_folder_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_folder_history: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of actions in the folder |  -  |
**403** | You don&#39;t have enough permission to perform the operation |  -  |
**404** | The required folder was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_info**
> FolderIntegerWrapper get_folder_info(folder_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder unique identifier. | 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.folder_integer_wrapper import FolderIntegerWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 9846 # int | The folder unique identifier.

    try:
        api_response = api_instance.get_folder_info(folder_id)
        print("The response of FoldersApi->get_folder_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_folder_info: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_links**
> FileShareArrayWrapper get_folder_links(id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The folder ID. | 

### Return type

[**FileShareArrayWrapper**](FileShareArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_share_array_wrapper import FileShareArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    id = 9846 # int | The folder ID.

    try:
        api_response = api_instance.get_folder_links(id)
        print("The response of FoldersApi->get_folder_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_folder_links: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder security information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_path**
> FileEntryBaseArrayWrapper get_folder_path(folder_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder unique identifier. | 

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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 9846 # int | The folder unique identifier.

    try:
        api_response = api_instance.get_folder_path(folder_id)
        print("The response of FoldersApi->get_folder_path:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_folder_path: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file entry information |  -  |
**403** | You don&#39;t have enough permission to view the folder content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_primary_external_link**
> FileShareWrapper get_folder_primary_external_link(id, count=count, start_index=start_index)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The folder unique identifier. | 
 **count** | **int**| The number of items to retrieve in the request. | [optional] 
 **start_index** | **int**| The starting index for the query results. | [optional] 

### Return type

[**FileShareWrapper**](FileShareWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_share_wrapper import FileShareWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    id = 9846 # int | The folder unique identifier.
    count = 1234 # int | The number of items to retrieve in the request. (optional)
    start_index = 1234 # int | The starting index for the query results. (optional)

    try:
        api_response = api_instance.get_folder_primary_external_link(id, count=count, start_index=start_index)
        print("The response of FoldersApi->get_folder_primary_external_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_folder_primary_external_link: %s\n" % e)
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

# **get_folder_recent**
> FolderContentIntegerWrapper get_folder_recent(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, exclude_subject=exclude_subject, apply_filter_option=apply_filter_option, search_area=search_area, extension=extension, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_group_id** | **str**| The user or group ID. | [optional] 
 **filter_type** | [**FilterType**](.md)| The filter type. | [optional] 
 **exclude_subject** | **bool**| Specifies whether to exclude search by user or group ID. | [optional] 
 **apply_filter_option** | [**ApplyFilterOption**](.md)| Specifies whether to return only files, only folders or all elements. | [optional] 
 **search_area** | [**SearchArea**](.md)| The search area. | [optional] 
 **extension** | [**List[str]**](str.md)| Specifies whether to search for a specific file extension in the Recent folder. | [optional] 
 **count** | **int**| The maximum number of items to return. | [optional] 
 **start_index** | **int**| The starting position of the results to be returned in the query response. | [optional] 
 **sort_by** | **str**| Specifies the sorting criteria for the folder request. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The order in which the results are sorted. | [optional] 
 **filter_value** | **str**| The text used for filtering or searching folder contents. | [optional] 

### Return type

[**FolderContentIntegerWrapper**](FolderContentIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.apply_filter_option import ApplyFilterOption
from docspace_api_sdk.models.filter_type import FilterType
from docspace_api_sdk.models.folder_content_integer_wrapper import FolderContentIntegerWrapper
from docspace_api_sdk.models.search_area import SearchArea
from docspace_api_sdk.models.sort_order import SortOrder
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    user_id_or_group_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | The user or group ID. (optional)
    filter_type = docspace_api_sdk.FilterType() # FilterType | The filter type. (optional)
    exclude_subject = true # bool | Specifies whether to exclude search by user or group ID. (optional)
    apply_filter_option = docspace_api_sdk.ApplyFilterOption() # ApplyFilterOption | Specifies whether to return only files, only folders or all elements. (optional)
    search_area = docspace_api_sdk.SearchArea() # SearchArea | The search area. (optional)
    extension = ['.txt'] # List[str] | Specifies whether to search for a specific file extension in the Recent folder. (optional)
    count = 1234 # int | The maximum number of items to return. (optional)
    start_index = 1234 # int | The starting position of the results to be returned in the query response. (optional)
    sort_by = 'some text' # str | Specifies the sorting criteria for the folder request. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_value = 'some text' # str | The text used for filtering or searching folder contents. (optional)

    try:
        api_response = api_instance.get_folder_recent(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, exclude_subject=exclude_subject, apply_filter_option=apply_filter_option, search_area=search_area, extension=extension, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)
        print("The response of FoldersApi->get_folder_recent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_folder_recent: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Recent section contents |  -  |
**403** | You don&#39;t have enough permission to view the folder content |  -  |
**404** | The required folder was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folders**
> FileEntryBaseArrayWrapper get_folders(folder_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder unique identifier. | 

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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 9846 # int | The folder unique identifier.

    try:
        api_response = api_instance.get_folders(folder_id)
        print("The response of FoldersApi->get_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_folders: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file entry information |  -  |
**403** | You don&#39;t have enough permission to view the folder content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_folder**
> FolderContentIntegerWrapper get_my_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, apply_filter_option=apply_filter_option, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)



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

### Return type

[**FolderContentIntegerWrapper**](FolderContentIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.apply_filter_option import ApplyFilterOption
from docspace_api_sdk.models.filter_type import FilterType
from docspace_api_sdk.models.folder_content_integer_wrapper import FolderContentIntegerWrapper
from docspace_api_sdk.models.sort_order import SortOrder
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    user_id_or_group_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | The user or group ID. (optional)
    filter_type = docspace_api_sdk.FilterType() # FilterType | The filter type. (optional)
    apply_filter_option = docspace_api_sdk.ApplyFilterOption() # ApplyFilterOption | Specifies whether to return only files, only folders or all elements. (optional)
    count = 1234 # int | The maximum number of items to retrieve in the response. (optional)
    start_index = 1234 # int | The starting position of the items to be retrieved. (optional)
    sort_by = 'some text' # str | The property used to specify the sorting criteria for folder contents. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_value = 'some text' # str | The text used for filtering or searching folder contents. (optional)

    try:
        api_response = api_instance.get_my_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, apply_filter_option=apply_filter_option, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)
        print("The response of FoldersApi->get_my_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_my_folder: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The My documents section contents |  -  |
**403** | You don&#39;t have enough permission to view the folder content |  -  |
**404** | The required folder was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_new_folder_items**
> FileEntryBaseArrayWrapper get_new_folder_items(folder_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder unique identifier. | 

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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 9846 # int | The folder unique identifier.

    try:
        api_response = api_instance.get_new_folder_items(folder_id)
        print("The response of FoldersApi->get_new_folder_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_new_folder_items: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file entry information |  -  |
**403** | You don&#39;t have enough permission to view the folder content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_privacy_folder**
> FolderContentIntegerWrapper get_privacy_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)



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

### Return type

[**FolderContentIntegerWrapper**](FolderContentIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.filter_type import FilterType
from docspace_api_sdk.models.folder_content_integer_wrapper import FolderContentIntegerWrapper
from docspace_api_sdk.models.sort_order import SortOrder
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    user_id_or_group_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | The user or group ID. (optional)
    filter_type = docspace_api_sdk.FilterType() # FilterType | The filter type. (optional)
    count = 1234 # int | The maximum number of items to retrieve in the request. (optional)
    start_index = 1234 # int | The zero-based index of the first item to retrieve in a paginated list. (optional)
    sort_by = 'some text' # str | Specifies the field by which the folder content should be sorted. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_value = 'some text' # str | The text used as a filter or search criterion for folder content queries. (optional)

    try:
        api_response = api_instance.get_privacy_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)
        print("The response of FoldersApi->get_privacy_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_privacy_folder: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Private Room section contents |  -  |
**403** | You don&#39;t have enough permission to view the folder content |  -  |
**404** | The required folder was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recent_folder**
> FolderContentIntegerWrapper get_recent_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, exclude_subject=exclude_subject, apply_filter_option=apply_filter_option, search_area=search_area, extension=extension, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_group_id** | **str**| The user or group ID. | [optional] 
 **filter_type** | [**FilterType**](.md)| The filter type. | [optional] 
 **exclude_subject** | **bool**| Specifies whether to exclude search by user or group ID. | [optional] 
 **apply_filter_option** | [**ApplyFilterOption**](.md)| Specifies whether to return only files, only folders or all elements. | [optional] 
 **search_area** | [**SearchArea**](.md)| The search area. | [optional] 
 **extension** | [**List[str]**](str.md)| Specifies whether to search for a specific file extension in the Recent folder. | [optional] 
 **count** | **int**| The maximum number of items to return. | [optional] 
 **start_index** | **int**| The starting position of the results to be returned in the query response. | [optional] 
 **sort_by** | **str**| Specifies the sorting criteria for the folder request. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The order in which the results are sorted. | [optional] 
 **filter_value** | **str**| The text used for filtering or searching folder contents. | [optional] 

### Return type

[**FolderContentIntegerWrapper**](FolderContentIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.apply_filter_option import ApplyFilterOption
from docspace_api_sdk.models.filter_type import FilterType
from docspace_api_sdk.models.folder_content_integer_wrapper import FolderContentIntegerWrapper
from docspace_api_sdk.models.search_area import SearchArea
from docspace_api_sdk.models.sort_order import SortOrder
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    user_id_or_group_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | The user or group ID. (optional)
    filter_type = docspace_api_sdk.FilterType() # FilterType | The filter type. (optional)
    exclude_subject = true # bool | Specifies whether to exclude search by user or group ID. (optional)
    apply_filter_option = docspace_api_sdk.ApplyFilterOption() # ApplyFilterOption | Specifies whether to return only files, only folders or all elements. (optional)
    search_area = docspace_api_sdk.SearchArea() # SearchArea | The search area. (optional)
    extension = ['.txt'] # List[str] | Specifies whether to search for a specific file extension in the Recent folder. (optional)
    count = 1234 # int | The maximum number of items to return. (optional)
    start_index = 1234 # int | The starting position of the results to be returned in the query response. (optional)
    sort_by = 'some text' # str | Specifies the sorting criteria for the folder request. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_value = 'some text' # str | The text used for filtering or searching folder contents. (optional)

    try:
        api_response = api_instance.get_recent_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, exclude_subject=exclude_subject, apply_filter_option=apply_filter_option, search_area=search_area, extension=extension, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)
        print("The response of FoldersApi->get_recent_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_recent_folder: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Recent section contents |  -  |
**403** | You don&#39;t have enough permission to view the folder content |  -  |
**404** | The required folder was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_root_folders**
> FolderContentIntegerArrayWrapper get_root_folders(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, without_trash=without_trash, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_group_id** | **str**| The user or group ID. | [optional] 
 **filter_type** | [**FilterType**](.md)| The filter type. | [optional] 
 **without_trash** | **bool**| Specifies whether to return the Trash section or not. | [optional] 
 **count** | **int**| The maximum number of items to retrieve in the response. | [optional] 
 **start_index** | **int**| The starting position of the items to be retrieved. | [optional] 
 **sort_by** | **str**| Specifies the field by which the folder content should be sorted. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The order in which the results are sorted. | [optional] 
 **filter_value** | **str**| The text used as a filter for searching or retrieving folder contents. | [optional] 

### Return type

[**FolderContentIntegerArrayWrapper**](FolderContentIntegerArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.filter_type import FilterType
from docspace_api_sdk.models.folder_content_integer_array_wrapper import FolderContentIntegerArrayWrapper
from docspace_api_sdk.models.sort_order import SortOrder
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    user_id_or_group_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | The user or group ID. (optional)
    filter_type = docspace_api_sdk.FilterType() # FilterType | The filter type. (optional)
    without_trash = true # bool | Specifies whether to return the Trash section or not. (optional)
    count = 1234 # int | The maximum number of items to retrieve in the response. (optional)
    start_index = 1234 # int | The starting position of the items to be retrieved. (optional)
    sort_by = 'some text' # str | Specifies the field by which the folder content should be sorted. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_value = 'some text' # str | The text used as a filter for searching or retrieving folder contents. (optional)

    try:
        api_response = api_instance.get_root_folders(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, without_trash=without_trash, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)
        print("The response of FoldersApi->get_root_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_root_folders: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of section contents with the following parameters |  -  |
**403** | You don&#39;t have enough permission to view the folder content |  -  |
**404** | The required folder was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trash_folder**
> FolderContentIntegerWrapper get_trash_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, apply_filter_option=apply_filter_option, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)



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

### Return type

[**FolderContentIntegerWrapper**](FolderContentIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.apply_filter_option import ApplyFilterOption
from docspace_api_sdk.models.filter_type import FilterType
from docspace_api_sdk.models.folder_content_integer_wrapper import FolderContentIntegerWrapper
from docspace_api_sdk.models.sort_order import SortOrder
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    user_id_or_group_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | The user or group ID. (optional)
    filter_type = docspace_api_sdk.FilterType() # FilterType | The filter type. (optional)
    apply_filter_option = docspace_api_sdk.ApplyFilterOption() # ApplyFilterOption | Specifies whether to return only files, only folders or all elements. (optional)
    count = 1234 # int | The maximum number of items to retrieve in the response. (optional)
    start_index = 1234 # int | The starting position of the items to be retrieved. (optional)
    sort_by = 'some text' # str | The property used to specify the sorting criteria for folder contents. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_value = 'some text' # str | The text used for filtering or searching folder contents. (optional)

    try:
        api_response = api_instance.get_trash_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, apply_filter_option=apply_filter_option, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)
        print("The response of FoldersApi->get_trash_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_trash_folder: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Trash section contents |  -  |
**403** | You don&#39;t have enough permission to view the folder content |  -  |
**404** | The required folder was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_file**
> FileIntegerWrapper insert_file(folder_id, insert_file_file=insert_file_file, insert_file_title=insert_file_title, insert_file_create_new_if_exist=insert_file_create_new_if_exist, insert_file_keep_convert_status=insert_file_keep_convert_status, insert_file_stream_can_read=insert_file_stream_can_read, insert_file_stream_can_write=insert_file_stream_can_write, insert_file_stream_can_seek=insert_file_stream_can_seek, insert_file_stream_can_timeout=insert_file_stream_can_timeout, insert_file_stream_length=insert_file_stream_length, insert_file_stream_position=insert_file_stream_position, insert_file_stream_read_timeout=insert_file_stream_read_timeout, insert_file_stream_write_timeout=insert_file_stream_write_timeout)



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

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_integer_wrapper import FileIntegerWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
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
        api_response = api_instance.insert_file(folder_id, insert_file_file=insert_file_file, insert_file_title=insert_file_title, insert_file_create_new_if_exist=insert_file_create_new_if_exist, insert_file_keep_convert_status=insert_file_keep_convert_status, insert_file_stream_can_read=insert_file_stream_can_read, insert_file_stream_can_write=insert_file_stream_can_write, insert_file_stream_can_seek=insert_file_stream_can_seek, insert_file_stream_can_timeout=insert_file_stream_can_timeout, insert_file_stream_length=insert_file_stream_length, insert_file_stream_position=insert_file_stream_position, insert_file_stream_read_timeout=insert_file_stream_read_timeout, insert_file_stream_write_timeout=insert_file_stream_write_timeout)
        print("The response of FoldersApi->insert_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->insert_file: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inserted file |  -  |
**403** | You don&#39;t have enough permission to create |  -  |
**404** | Folder not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_file_to_my_from_body**
> FileIntegerWrapper insert_file_to_my_from_body(file=file, title=title, create_new_if_exist=create_new_if_exist, keep_convert_status=keep_convert_status, stream_can_read=stream_can_read, stream_can_write=stream_can_write, stream_can_seek=stream_can_seek, stream_can_timeout=stream_can_timeout, stream_length=stream_length, stream_position=stream_position, stream_read_timeout=stream_read_timeout, stream_write_timeout=stream_write_timeout)



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

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_integer_wrapper import FileIntegerWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
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
        api_response = api_instance.insert_file_to_my_from_body(file=file, title=title, create_new_if_exist=create_new_if_exist, keep_convert_status=keep_convert_status, stream_can_read=stream_can_read, stream_can_write=stream_can_write, stream_can_seek=stream_can_seek, stream_can_timeout=stream_can_timeout, stream_length=stream_length, stream_position=stream_position, stream_read_timeout=stream_read_timeout, stream_write_timeout=stream_write_timeout)
        print("The response of FoldersApi->insert_file_to_my_from_body:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->insert_file_to_my_from_body: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inserted file |  -  |
**403** | You don&#39;t have enough permission to create |  -  |
**404** | Folder not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_folder**
> FolderIntegerWrapper rename_folder(folder_id, create_folder)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID for the folder creation. | 
 **create_folder** | [**CreateFolder**](CreateFolder.md)| The parameters for creating a folder. | 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.create_folder import CreateFolder
from docspace_api_sdk.models.folder_integer_wrapper import FolderIntegerWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 9846 # int | The folder ID for the folder creation.
    create_folder = docspace_api_sdk.CreateFolder() # CreateFolder | The parameters for creating a folder.

    try:
        api_response = api_instance.rename_folder(folder_id, create_folder)
        print("The response of FoldersApi->rename_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->rename_folder: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder parameters |  -  |
**403** | You don&#39;t have enough permission to rename the folder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_folder_order**
> FolderIntegerWrapper set_folder_order(folder_id, order_request_dto=order_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder unique identifier. | 
 **order_request_dto** | [**OrderRequestDto**](OrderRequestDto.md)| The folder order information. | [optional] 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.folder_integer_wrapper import FolderIntegerWrapper
from docspace_api_sdk.models.order_request_dto import OrderRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 9846 # int | The folder unique identifier.
    order_request_dto = docspace_api_sdk.OrderRequestDto() # OrderRequestDto | The folder order information. (optional)

    try:
        api_response = api_instance.set_folder_order(folder_id, order_request_dto=order_request_dto)
        print("The response of FoldersApi->set_folder_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->set_folder_order: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file operations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_folder_primary_external_link**
> FileShareWrapper set_folder_primary_external_link(id, folder_link_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The folder ID. | 
 **folder_link_request** | [**FolderLinkRequest**](FolderLinkRequest.md)| The folder link parameters. | 

### Return type

[**FileShareWrapper**](FileShareWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_share_wrapper import FileShareWrapper
from docspace_api_sdk.models.folder_link_request import FolderLinkRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    id = 9846 # int | The folder ID.
    folder_link_request = docspace_api_sdk.FolderLinkRequest() # FolderLinkRequest | The folder link parameters.

    try:
        api_response = api_instance.set_folder_primary_external_link(id, folder_link_request)
        print("The response of FoldersApi->set_folder_primary_external_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->set_folder_primary_external_link: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> ObjectWrapper upload_file(folder_id, upload_request_dto=upload_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID to upload a file. | 
 **upload_request_dto** | [**UploadRequestDto**](UploadRequestDto.md)| The request parameters for uploading a file. | [optional] 

### Return type

[**ObjectWrapper**](ObjectWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.object_wrapper import ObjectWrapper
from docspace_api_sdk.models.upload_request_dto import UploadRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 9846 # int | The folder ID to upload a file.
    upload_request_dto = docspace_api_sdk.UploadRequestDto() # UploadRequestDto | The request parameters for uploading a file. (optional)

    try:
        api_response = api_instance.upload_file(folder_id, upload_request_dto=upload_request_dto)
        print("The response of FoldersApi->upload_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->upload_file: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inserted file |  -  |
**403** | You don&#39;t have enough permission to create |  -  |
**404** | Folder not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file_to_my**
> ObjectWrapper upload_file_to_my(in_dto=in_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **in_dto** | [**UploadRequestDto**](.md)| The request parameters for uploading a file. | [optional] 

### Return type

[**ObjectWrapper**](ObjectWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.object_wrapper import ObjectWrapper
from docspace_api_sdk.models.upload_request_dto import UploadRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    in_dto = docspace_api_sdk.UploadRequestDto() # UploadRequestDto | The request parameters for uploading a file. (optional)

    try:
        api_response = api_instance.upload_file_to_my(in_dto=in_dto)
        print("The response of FoldersApi->upload_file_to_my:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->upload_file_to_my: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Uploaded file(s) |  -  |
**403** | You don&#39;t have enough permission to create |  -  |
**404** | File not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

