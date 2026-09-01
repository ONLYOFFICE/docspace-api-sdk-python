# docspace_api_sdk.FoldersApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_upload**](#check_upload) | **POST** /api/2.0/files/{folderId}/upload/check | Check file uploads
[**create_folder**](#create_folder) | **POST** /api/2.0/files/folder/{folderId} | Create a folder
[**create_folder_primary_external_link**](#create_folder_primary_external_link) | **POST** /api/2.0/files/folder/{id}/link | Create primary external link
[**create_report_folder_history**](#create_report_folder_history) | **POST** /api/2.0/files/folder/{folderId}/log/report | Start the folder history report generation
[**delete_folder**](#delete_folder) | **DELETE** /api/2.0/files/folder/{folderId} | Delete a folder
[**generate_xlsx_by_folder**](#generate_xlsx_by_folder) | **POST** /api/2.0/files/folder/{folderId}/xlsx | Generate XLSX report by folder
[**get_favorites_folder**](#get_favorites_folder) | **GET** /api/2.0/files/@favorites | Get the Favorites section
[**get_files_used_space**](#get_files_used_space) | **GET** /api/2.0/files/filesusedspace | Get used space of files
[**get_folder**](#get_folder) | **GET** /api/2.0/files/{folderId}/formfilter | Get folder form filter
[**get_folder_by_folder_id**](#get_folder_by_folder_id) | **GET** /api/2.0/files/{folderId} | Get a folder by ID
[**get_folder_history**](#get_folder_history) | **GET** /api/2.0/files/folder/{folderId}/log | Get folder history
[**get_folder_info**](#get_folder_info) | **GET** /api/2.0/files/folder/{folderId} | Get folder information
[**get_folder_links**](#get_folder_links) | **GET** /api/2.0/files/folder/{id}/links | Get the folder links
[**get_folder_path**](#get_folder_path) | **GET** /api/2.0/files/folder/{folderId}/path | Get the folder path
[**get_folder_primary_external_link**](#get_folder_primary_external_link) | **GET** /api/2.0/files/folder/{id}/link | Get primary external link
[**get_folders**](#get_folders) | **GET** /api/2.0/files/{folderId}/subfolders | Get subfolders
[**get_forms_folder**](#get_forms_folder) | **GET** /api/2.0/files/@forms | Get the Forms section
[**get_my_folder**](#get_my_folder) | **GET** /api/2.0/files/@my | Get the My documents section
[**get_new_folder_items**](#get_new_folder_items) | **GET** /api/2.0/files/{folderId}/news | Get new folder items
[**get_recent_folder**](#get_recent_folder) | **GET** /api/2.0/files/recent | Get the Recent section
[**get_report_folder_history**](#get_report_folder_history) | **GET** /api/2.0/files/folder/{folderId}/log/report | Get the folder history report generation status
[**get_root_folders**](#get_root_folders) | **GET** /api/2.0/files/@root | Get filtered sections
[**get_trash_folder**](#get_trash_folder) | **GET** /api/2.0/files/@trash | Get the Trash section
[**insert_file**](#insert_file) | **POST** /api/2.0/files/{folderId}/insert | Insert a file
[**insert_file_to_my_from_body**](#insert_file_to_my_from_body) | **POST** /api/2.0/files/@my/insert | Insert a file to the My documents section
[**rename_folder**](#rename_folder) | **PUT** /api/2.0/files/folder/{folderId} | Rename a folder
[**set_folder_order**](#set_folder_order) | **PUT** /api/2.0/files/folder/{folderId}/order | Set folder order
[**set_folder_primary_external_link**](#set_folder_primary_external_link) | **PUT** /api/2.0/files/folder/{id}/links | Set the folder external link
[**terminate_report_folder_history**](#terminate_report_folder_history) | **DELETE** /api/2.0/files/folder/{folderId}/log/report | Terminate the folder history report generation
[**upload_file**](#upload_file) | **POST** /api/2.0/files/{folderId}/upload | Upload a file
[**upload_file_to_my**](#upload_file_to_my) | **POST** /api/2.0/files/@my/upload | Upload a file to the My documents section


# **check_upload**
> STRINGArrayWrapper check_upload(folder_id, check_upload_request)

Checks the file uploads to the folder with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID. | 
 **check_upload_request** | [**CheckUploadRequest**](CheckUploadRequest.md)| The request parameters for checking file uploads. | 

### Return type

[**STRINGArrayWrapper**](STRINGArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 1 # int | The folder ID.
    check_upload_request = docspace_api_sdk.CheckUploadRequest() # CheckUploadRequest | The request parameters for checking file uploads.

    try:
        # Check file uploads
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
**200** | Inserted file |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder**
> FolderIntegerWrapper create_folder(folder_id, create_folder)

Creates a new folder with the title specified in the request. The parent folder ID can be also specified.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID for the folder creation. | 
 **create_folder** | [**CreateFolder**](CreateFolder.md)| The parameters for creating a folder. | 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 1 # int | The folder ID for the folder creation.
    create_folder = docspace_api_sdk.CreateFolder() # CreateFolder | The parameters for creating a folder.

    try:
        # Create a folder
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
**200** | New folder parameters |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder_primary_external_link**
> FileShareWrapper create_folder_primary_external_link(id, folder_link_request)

Creates a primary external link by the identifier specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The folder ID. | 
 **folder_link_request** | [**FolderLinkRequest**](FolderLinkRequest.md)| The folder link parameters. | 

### Return type

[**FileShareWrapper**](FileShareWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    id = 1 # int | The folder ID.
    folder_link_request = docspace_api_sdk.FolderLinkRequest() # FolderLinkRequest | The folder link parameters.

    try:
        # Create primary external link
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
**200** | Folders security information |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_report_folder_history**
> DocumentBuilderTaskWrapper create_report_folder_history(folder_id, format=format, var_from=var_from, to=to)

Starts generating the activity history report of a folder (XLSX by default, or CSV) and saves it to My documents.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID whose history is exported. | 
 **format** | [**AuditReportFormat**](.md)| The output file format of the report. Defaults to XLSX. | [optional] 
 **var_from** | **datetime**| The start date of the history period to export. | [optional] 
 **to** | **datetime**| The end date of the history period to export. | [optional] 

### Return type

[**DocumentBuilderTaskWrapper**](DocumentBuilderTaskWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.audit_report_format import AuditReportFormat
from docspace_api_sdk.models.document_builder_task_wrapper import DocumentBuilderTaskWrapper
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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 1 # int | The folder ID whose history is exported.
    format = docspace_api_sdk.AuditReportFormat() # AuditReportFormat | The output file format of the report. Defaults to XLSX. (optional)
    var_from = '2025-01-01T00:00:00' # datetime | The start date of the history period to export. (optional)
    to = '2025-12-31T23:59:59' # datetime | The end date of the history period to export. (optional)

    try:
        # Start the folder history report generation
        api_response = api_instance.create_report_folder_history(folder_id, format=format, var_from=var_from, to=to)
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
**200** | Operation execution status |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | The required folder was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> FileOperationArrayWrapper delete_folder(folder_id, delete_folder)

Deletes a folder with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID to delete. | 
 **delete_folder** | [**DeleteFolder**](DeleteFolder.md)| The parameters for deleting a folder. | 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 10 # int | The folder ID to delete.
    delete_folder = docspace_api_sdk.DeleteFolder() # DeleteFolder | The parameters for deleting a folder.

    try:
        # Delete a folder
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
**200** | List of file operations |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_xlsx_by_folder**
> XlsxReportResponseWrapper generate_xlsx_by_folder(folder_id)

Triggers asynchronous XLSX report generation for the specified form results folder.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder unique identifier. | 

### Return type

[**XlsxReportResponseWrapper**](XlsxReportResponseWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.xlsx_report_response_wrapper import XlsxReportResponseWrapper
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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 1 # int | The folder unique identifier.

    try:
        # Generate XLSX report by folder
        api_response = api_instance.generate_xlsx_by_folder(folder_id)
        print("The response of FoldersApi->generate_xlsx_by_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->generate_xlsx_by_folder: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You do not have enough permissions to perform this action |  -  |
**404** | The required folder was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorites_folder**
> FolderContentIntegerWrapper get_favorites_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)

Returns the detailed list of files and folders located in the Favorites section.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_group_id** | **UUID**| The user or group ID. | [optional] 
 **filter_type** | [**FilterType**](.md)| The filter type. | [optional] 
 **count** | **int**| The maximum number of items to retrieve in the request. | [optional] 
 **start_index** | **int**| The zero-based index of the first item to retrieve in a paginated list. | [optional] 
 **sort_by** | **str**| Specifies the field by which the folder content should be sorted. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The order in which the results are sorted. | [optional] 
 **filter_value** | **str**| The text used as a filter or search criterion for folder content queries. | [optional] 

### Return type

[**FolderContentIntegerWrapper**](FolderContentIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    user_id_or_group_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The user or group ID. (optional)
    filter_type = docspace_api_sdk.FilterType() # FilterType | The filter type. (optional)
    count = 25 # int | The maximum number of items to retrieve in the request. (optional)
    start_index = 0 # int | The zero-based index of the first item to retrieve in a paginated list. (optional)
    sort_by = 'DateAndTime' # str | Specifies the field by which the folder content should be sorted. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_value = 'My Document' # str | The text used as a filter or search criterion for folder content queries. (optional)

    try:
        # Get the Favorites section
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
**200** | The Favorites section contents |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to view the folder content |  -  |
**404** | The required folder was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

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
import docspace_api_sdk
from docspace_api_sdk.models.files_statistics_result_wrapper import FilesStatisticsResultWrapper
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
    api_instance = docspace_api_sdk.FoldersApi(api_client)

    try:
        # Get used space of files
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
**200** | Used space of files in the root folders |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder**
> FormsItemArrayWrapper get_folder(folder_id)

Returns the form filter of a folder with the ID specified in the request.

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
    folder_id = 1 # int | The folder unique identifier.

    try:
        # Get folder form filter
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
**200** | Ok |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_by_folder_id**
> FolderContentIntegerWrapper get_folder_by_folder_id(folder_id, user_id_or_group_id=user_id_or_group_id, shared_by=shared_by, filter_type=filter_type, room_id=room_id, folder_type=folder_type, exclude_subject=exclude_subject, apply_filter_option=apply_filter_option, with_sub_folders=with_sub_folders, extension=extension, search_area=search_area, forms_item_key=forms_item_key, forms_item_type=forms_item_type, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value, location=location)

Returns the detailed list of files and folders located in the folder with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID. | 
 **user_id_or_group_id** | **UUID**| The user or group ID. | [optional] 
 **shared_by** | **UUID**| The identifier of the user who shared the folder or file. | [optional] 
 **filter_type** | [**FilterType**](.md)| The filter type. | [optional] 
 **room_id** | **int**| The room ID. | [optional] 
 **folder_type** | [**List[int]**](int.md)| The parent folder types used to filter the folder contents by folder type. | [optional] 
 **exclude_subject** | **bool**| Specifies whether to exclude search by user or group ID. | [optional] 
 **apply_filter_option** | [**ApplyFilterOption**](.md)| Specifies whether to return only files, only folders, or all elements from the specified folder. | [optional] 
 **with_sub_folders** | **bool**| Specifies whether to include files from subfolders in the results. | [optional] 
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
    folder_id = 1 # int | The folder ID.
    user_id_or_group_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The user or group ID. (optional)
    shared_by = UUID('00000000-0000-0000-0000-000000000000') # UUID | The identifier of the user who shared the folder or file. (optional)
    filter_type = docspace_api_sdk.FilterType() # FilterType | The filter type. (optional)
    room_id = 1 # int | The room ID. (optional)
    folder_type = [[2]] # List[int] | The parent folder types used to filter the folder contents by folder type. (optional)
    exclude_subject = false # bool | Specifies whether to exclude search by user or group ID. (optional)
    apply_filter_option = docspace_api_sdk.ApplyFilterOption() # ApplyFilterOption | Specifies whether to return only files, only folders, or all elements from the specified folder. (optional)
    with_sub_folders = true # bool | Specifies whether to include files from subfolders in the results. (optional)
    extension = '.docx' # str | Specifies whether to search for the specific file extension. (optional)
    search_area = docspace_api_sdk.SearchArea() # SearchArea | The search area. (optional)
    forms_item_key = 'doc_key_123' # str | The forms item key. (optional)
    forms_item_type = 'text' # str | The forms item type. (optional)
    count = 25 # int | The maximum number of items to retrieve in the request. (optional)
    start_index = 0 # int | The zero-based index of the first item to retrieve in a paginated request. (optional)
    sort_by = 'DateAndTime' # str | The property used for sorting the folder request results. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_value = 'My Document' # str | The text value used as a filter parameter for folder content queries. (optional)
    location = docspace_api_sdk.Location() # Location | The location context of the request, specifying the area  where the operation is performed, such as a room, documents, or a link. (optional)

    try:
        # Get a folder by ID
        api_response = api_instance.get_folder_by_folder_id(folder_id, user_id_or_group_id=user_id_or_group_id, shared_by=shared_by, filter_type=filter_type, room_id=room_id, folder_type=folder_type, exclude_subject=exclude_subject, apply_filter_option=apply_filter_option, with_sub_folders=with_sub_folders, extension=extension, search_area=search_area, forms_item_key=forms_item_key, forms_item_type=forms_item_type, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value, location=location)
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
**200** | Folder contents |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to view the folder content |  -  |
**404** | The required folder was not found |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_history**
> HistoryArrayWrapper get_folder_history(folder_id, from_date=from_date, to_date=to_date, count=count, start_index=start_index)

Returns the activity history of a folder with a specified identifier.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID of the history request. | 
 **from_date** | **datetime**| The start date of the history request. | [optional] 
 **to_date** | **datetime**| The end date of the history request. | [optional] 
 **count** | **int**| The number of records to retrieve for the folder history. | [optional] 
 **start_index** | **int**| The starting index from which the history records are retrieved in the request. | [optional] 

### Return type

[**HistoryArrayWrapper**](HistoryArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.history_array_wrapper import HistoryArrayWrapper
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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 1 # int | The folder ID of the history request.
    from_date = '2025-01-01T00:00:00.0000000Z' # datetime | The start date of the history request. (optional)
    to_date = '2025-12-31T23:59:59.0000000Z' # datetime | The end date of the history request. (optional)
    count = 25 # int | The number of records to retrieve for the folder history. (optional)
    start_index = 0 # int | The starting index from which the history records are retrieved in the request. (optional)

    try:
        # Get folder history
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
**200** | List of actions in the folder |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | The required folder was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_info**
> FolderIntegerWrapper get_folder_info(folder_id)

Returns the detailed information about a folder with the ID specified in the request.

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
    folder_id = 1 # int | The folder unique identifier.

    try:
        # Get folder information
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
**200** | Folder parameters |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_links**
> FileShareArrayWrapper get_folder_links(id)

Returns the links of the folder with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The folder ID. | 

### Return type

[**FileShareArrayWrapper**](FileShareArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_share_array_wrapper import FileShareArrayWrapper
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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    id = 1 # int | The folder ID.

    try:
        # Get the folder links
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
**200** | Folder security information |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_path**
> FileEntryBaseArrayWrapper get_folder_path(folder_id)

Returns a path to the folder with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder unique identifier. | 

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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 1 # int | The folder unique identifier.

    try:
        # Get the folder path
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
**200** | List of file entry information |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to view the folder content |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_primary_external_link**
> FileShareWrapper get_folder_primary_external_link(id, count=count, start_index=start_index)

Returns the primary external link by the identifier specified in the request.

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
    id = 10 # int | The folder unique identifier.
    count = 25 # int | The number of items to retrieve in the request. (optional)
    start_index = 0 # int | The starting index for the query results. (optional)

    try:
        # Get primary external link
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
**200** | Folder security information |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folders**
> FileEntryBaseArrayWrapper get_folders(folder_id)

Returns a list of all the subfolders from a folder with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder unique identifier. | 

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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 1 # int | The folder unique identifier.

    try:
        # Get subfolders
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
**200** | List of file entry information |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to view the folder content |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forms_folder**
> FolderContentIntegerWrapper get_forms_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)

Returns the detailed list of rooms used for filling out forms located in the Forms section.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_group_id** | **UUID**| The user or group ID. | [optional] 
 **filter_type** | [**FilterType**](.md)| The filter type. | [optional] 
 **count** | **int**| The maximum number of items to retrieve in the request. | [optional] 
 **start_index** | **int**| The zero-based index of the first item to retrieve in a paginated list. | [optional] 
 **sort_by** | **str**| Specifies the field by which the folder content should be sorted. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The order in which the results are sorted. | [optional] 
 **filter_value** | **str**| The text used as a filter or search criterion for folder content queries. | [optional] 

### Return type

[**FolderContentIntegerWrapper**](FolderContentIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    user_id_or_group_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The user or group ID. (optional)
    filter_type = docspace_api_sdk.FilterType() # FilterType | The filter type. (optional)
    count = 25 # int | The maximum number of items to retrieve in the request. (optional)
    start_index = 0 # int | The zero-based index of the first item to retrieve in a paginated list. (optional)
    sort_by = 'DateAndTime' # str | Specifies the field by which the folder content should be sorted. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_value = 'My Document' # str | The text used as a filter or search criterion for folder content queries. (optional)

    try:
        # Get the Forms section
        api_response = api_instance.get_forms_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)
        print("The response of FoldersApi->get_forms_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_forms_folder: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Forms section contents |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to view the folder content |  -  |
**404** | The required folder was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_folder**
> FolderContentIntegerWrapper get_my_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, apply_filter_option=apply_filter_option, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)

Returns the detailed list of files and folders located in the My documents section.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_group_id** | **UUID**| The user or group ID. | [optional] 
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

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    user_id_or_group_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The user or group ID. (optional)
    filter_type = docspace_api_sdk.FilterType() # FilterType | The filter type. (optional)
    apply_filter_option = docspace_api_sdk.ApplyFilterOption() # ApplyFilterOption | Specifies whether to return only files, only folders or all elements. (optional)
    count = 25 # int | The maximum number of items to retrieve in the response. (optional)
    start_index = 0 # int | The starting position of the items to be retrieved. (optional)
    sort_by = 'DateAndTime' # str | The property used to specify the sorting criteria for folder contents. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_value = 'My Document' # str | The text used for filtering or searching folder contents. (optional)

    try:
        # Get the My documents section
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
**200** | The My documents section contents |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to view the folder content |  -  |
**404** | The required folder was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_new_folder_items**
> FileEntryBaseArrayWrapper get_new_folder_items(folder_id)

Returns a list of all the new items from a folder with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder unique identifier. | 

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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 1 # int | The folder unique identifier.

    try:
        # Get new folder items
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
**200** | List of file entry information |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to view the folder content |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recent_folder**
> FolderContentIntegerWrapper get_recent_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, exclude_subject=exclude_subject, apply_filter_option=apply_filter_option, search_area=search_area, extension=extension, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)

Returns the detailed list of files located in the Recent section.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_group_id** | **UUID**| The user or group ID. | [optional] 
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

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    user_id_or_group_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The user or group ID. (optional)
    filter_type = docspace_api_sdk.FilterType() # FilterType | The filter type. (optional)
    exclude_subject = false # bool | Specifies whether to exclude search by user or group ID. (optional)
    apply_filter_option = docspace_api_sdk.ApplyFilterOption() # ApplyFilterOption | Specifies whether to return only files, only folders or all elements. (optional)
    search_area = docspace_api_sdk.SearchArea() # SearchArea | The search area. (optional)
    extension = ['.docx'] # List[str] | Specifies whether to search for a specific file extension in the Recent folder. (optional)
    count = 25 # int | The maximum number of items to return. (optional)
    start_index = 0 # int | The starting position of the results to be returned in the query response. (optional)
    sort_by = 'DateAndTime' # str | Specifies the sorting criteria for the folder request. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_value = 'My Document' # str | The text used for filtering or searching folder contents. (optional)

    try:
        # Get the Recent section
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
**200** | The Recent section contents |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to view the folder content |  -  |
**404** | The required folder was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_folder_history**
> DocumentBuilderTaskWrapper get_report_folder_history(folder_id)

Returns the status of generating the folder history report.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder unique identifier. | 

### Return type

[**DocumentBuilderTaskWrapper**](DocumentBuilderTaskWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.document_builder_task_wrapper import DocumentBuilderTaskWrapper
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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 56 # int | The folder unique identifier.

    try:
        # Get the folder history report generation status
        api_response = api_instance.get_report_folder_history(folder_id)
        print("The response of FoldersApi->get_report_folder_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_report_folder_history: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation execution status |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | The required folder was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_root_folders**
> FolderContentIntegerArrayWrapper get_root_folders(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, without_trash=without_trash, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)

Returns all the sections matching the parameters specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_group_id** | **UUID**| The user or group ID. | [optional] 
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

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    user_id_or_group_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The user or group ID. (optional)
    filter_type = docspace_api_sdk.FilterType() # FilterType | The filter type. (optional)
    without_trash = false # bool | Specifies whether to return the Trash section or not. (optional)
    count = 25 # int | The maximum number of items to retrieve in the response. (optional)
    start_index = 0 # int | The starting position of the items to be retrieved. (optional)
    sort_by = 'DateAndTime' # str | Specifies the field by which the folder content should be sorted. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_value = 'My Document' # str | The text used as a filter for searching or retrieving folder contents. (optional)

    try:
        # Get filtered sections
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
**200** | List of section contents with the following parameters |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to view the folder content |  -  |
**404** | The required folder was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trash_folder**
> FolderContentIntegerWrapper get_trash_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, apply_filter_option=apply_filter_option, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)

Returns the detailed list of files and folders located in the Trash section.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_group_id** | **UUID**| The user or group ID. | [optional] 
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

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    user_id_or_group_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The user or group ID. (optional)
    filter_type = docspace_api_sdk.FilterType() # FilterType | The filter type. (optional)
    apply_filter_option = docspace_api_sdk.ApplyFilterOption() # ApplyFilterOption | Specifies whether to return only files, only folders or all elements. (optional)
    count = 25 # int | The maximum number of items to retrieve in the response. (optional)
    start_index = 0 # int | The starting position of the items to be retrieved. (optional)
    sort_by = 'DateAndTime' # str | The property used to specify the sorting criteria for folder contents. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_value = 'My Document' # str | The text used for filtering or searching folder contents. (optional)

    try:
        # Get the Trash section
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
**200** | The Trash section contents |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to view the folder content |  -  |
**404** | The required folder was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_file**
> FileIntegerWrapper insert_file(folder_id, insert_file_file=insert_file_file, insert_file_title=insert_file_title, insert_file_create_new_if_exist=insert_file_create_new_if_exist, insert_file_keep_convert_status=insert_file_keep_convert_status, insert_file_stream_can_read=insert_file_stream_can_read, insert_file_stream_can_write=insert_file_stream_can_write, insert_file_stream_can_seek=insert_file_stream_can_seek, insert_file_stream_can_timeout=insert_file_stream_can_timeout, insert_file_stream_length=insert_file_stream_length, insert_file_stream_position=insert_file_stream_position, insert_file_stream_read_timeout=insert_file_stream_read_timeout, insert_file_stream_write_timeout=insert_file_stream_write_timeout)

Inserts a file specified in the request to the selected folder by single file uploading.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID for inserting a file. | 
 **insert_file_file** | **bytes**| The file to be inserted. | [optional] 
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
import docspace_api_sdk
from docspace_api_sdk.models.file_integer_wrapper import FileIntegerWrapper
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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 1 # int | The folder ID for inserting a file.
    insert_file_file = None # bytes | The file to be inserted. (optional)
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
**200** | Inserted file |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to create |  -  |
**404** | Folder not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_file_to_my_from_body**
> FileIntegerWrapper insert_file_to_my_from_body(file=file, title=title, create_new_if_exist=create_new_if_exist, keep_convert_status=keep_convert_status, stream_can_read=stream_can_read, stream_can_write=stream_can_write, stream_can_seek=stream_can_seek, stream_can_timeout=stream_can_timeout, stream_length=stream_length, stream_position=stream_position, stream_read_timeout=stream_read_timeout, stream_write_timeout=stream_write_timeout)

Inserts a file specified in the request to the My documents section by single file uploading.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytes**| The file to be inserted. | [optional] 
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
import docspace_api_sdk
from docspace_api_sdk.models.file_integer_wrapper import FileIntegerWrapper
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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    file = None # bytes | The file to be inserted. (optional)
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
        # Insert a file to the My documents section
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
**200** | Inserted file |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to create |  -  |
**404** | Folder not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_folder**
> FolderIntegerWrapper rename_folder(folder_id, create_folder)

Renames the selected folder with a new title specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID for the folder creation. | 
 **create_folder** | [**CreateFolder**](CreateFolder.md)| The parameters for creating a folder. | 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 1 # int | The folder ID for the folder creation.
    create_folder = docspace_api_sdk.CreateFolder() # CreateFolder | The parameters for creating a folder.

    try:
        # Rename a folder
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
**200** | Folder parameters |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to rename the folder |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_folder_order**
> FolderIntegerWrapper set_folder_order(folder_id, order_request_dto=order_request_dto)

Sets the order of a folder with ID specified in the request.

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
import docspace_api_sdk
from docspace_api_sdk.models.folder_integer_wrapper import FolderIntegerWrapper
from docspace_api_sdk.models.order_request_dto import OrderRequestDto
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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 1 # int | The folder unique identifier.
    order_request_dto = docspace_api_sdk.OrderRequestDto() # OrderRequestDto | The folder order information. (optional)

    try:
        # Set folder order
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
**200** | List of file operations |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_folder_primary_external_link**
> FileShareWrapper set_folder_primary_external_link(id, folder_link_request)

Sets the folder external link with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The folder ID. | 
 **folder_link_request** | [**FolderLinkRequest**](FolderLinkRequest.md)| The folder link parameters. | 

### Return type

[**FileShareWrapper**](FileShareWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    id = 1 # int | The folder ID.
    folder_link_request = docspace_api_sdk.FolderLinkRequest() # FolderLinkRequest | The folder link parameters.

    try:
        # Set the folder external link
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
**200** | Folder information |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_report_folder_history**
> terminate_report_folder_history(folder_id)

Terminates generating the folder history report.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder unique identifier. | 

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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 56 # int | The folder unique identifier.

    try:
        # Terminate the folder history report generation
        api_instance.terminate_report_folder_history(folder_id)
    except Exception as e:
        print("Exception when calling FoldersApi->terminate_report_folder_history: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | The required folder was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> FileIntegerArrayWrapper upload_file(folder_id, create_new_if_exist=create_new_if_exist, store_original_file=store_original_file, keep_convert_status=keep_convert_status, file=file)

Uploads a file specified in the request to the selected folder by single file uploading or standart multipart/form-data method.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID to upload a file. | 
 **create_new_if_exist** | **bool**| Specifies whether to create the new file if it already exists or not. | [optional] 
 **store_original_file** | **bool**| Specifies whether to upload documents in the original formats as well or not. | [optional] 
 **keep_convert_status** | **bool**| Specifies whether to keep the file converting status or not. | [optional] 
 **file** | **bytes**| The file to be uploaded. | [optional] 

### Return type

[**FileIntegerArrayWrapper**](FileIntegerArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_integer_array_wrapper import FileIntegerArrayWrapper
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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 1 # int | The folder ID to upload a file.
    create_new_if_exist = true # bool | Specifies whether to create the new file if it already exists or not. (optional)
    store_original_file = true # bool | Specifies whether to upload documents in the original formats as well or not. (optional)
    keep_convert_status = false # bool | Specifies whether to keep the file converting status or not. (optional)
    file = None # bytes | The file to be uploaded. (optional)

    try:
        # Upload a file
        api_response = api_instance.upload_file(folder_id, create_new_if_exist=create_new_if_exist, store_original_file=store_original_file, keep_convert_status=keep_convert_status, file=file)
        print("The response of FoldersApi->upload_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->upload_file: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inserted file |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to create |  -  |
**404** | Folder not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file_to_my**
> FileIntegerArrayWrapper upload_file_to_my(create_new_if_exist=create_new_if_exist, store_original_file=store_original_file, keep_convert_status=keep_convert_status, file=file)

Uploads a file specified in the request to the My documents section by single file uploading or standart multipart/form-data method.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_new_if_exist** | **bool**| Specifies whether to create the new file if it already exists or not. | [optional] 
 **store_original_file** | **bool**| Specifies whether to upload documents in the original formats as well or not. | [optional] 
 **keep_convert_status** | **bool**| Specifies whether to keep the file converting status or not. | [optional] 
 **file** | **bytes**| The file to be uploaded. | [optional] 

### Return type

[**FileIntegerArrayWrapper**](FileIntegerArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_integer_array_wrapper import FileIntegerArrayWrapper
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
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    create_new_if_exist = true # bool | Specifies whether to create the new file if it already exists or not. (optional)
    store_original_file = true # bool | Specifies whether to upload documents in the original formats as well or not. (optional)
    keep_convert_status = false # bool | Specifies whether to keep the file converting status or not. (optional)
    file = None # bytes | The file to be uploaded. (optional)

    try:
        # Upload a file to the My documents section
        api_response = api_instance.upload_file_to_my(create_new_if_exist=create_new_if_exist, store_original_file=store_original_file, keep_convert_status=keep_convert_status, file=file)
        print("The response of FoldersApi->upload_file_to_my:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->upload_file_to_my: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Uploaded file(s) |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to create |  -  |
**404** | File not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

