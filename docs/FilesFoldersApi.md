# docspace_api_sdk.FoldersApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_upload**](#check_upload) | **POST** /api/2.0/files/{folderId}/upload/check | Check for upload conflicts
[**create_folder**](#create_folder) | **POST** /api/2.0/files/folder/{folderId} | Create a folder
[**create_folder_primary_external_link**](#create_folder_primary_external_link) | **POST** /api/2.0/files/folder/{id}/link | Create the folder primary external link
[**create_report_folder_history**](#create_report_folder_history) | **POST** /api/2.0/files/folder/{folderId}/log/report | Start the folder history report generation
[**delete_folder**](#delete_folder) | **DELETE** /api/2.0/files/folder/{folderId} | Delete a folder
[**generate_xlsx_by_folder**](#generate_xlsx_by_folder) | **POST** /api/2.0/files/folder/{folderId}/xlsx | Generate XLSX report by folder
[**get_favorites_folder**](#get_favorites_folder) | **GET** /api/2.0/files/@favorites | Get the Favorites section
[**get_files_used_space**](#get_files_used_space) | **GET** /api/2.0/files/filesusedspace | Get used space of files
[**get_folder**](#get_folder) | **GET** /api/2.0/files/{folderId}/formfilter | Get folder form filter
[**get_folder_by_folder_id**](#get_folder_by_folder_id) | **GET** /api/2.0/files/{folderId} | Get a folder by ID
[**get_folder_history**](#get_folder_history) | **GET** /api/2.0/files/folder/{folderId}/log | Get folder history
[**get_folder_info**](#get_folder_info) | **GET** /api/2.0/files/folder/{folderId} | Get folder information
[**get_folder_links**](#get_folder_links) | **GET** /api/2.0/files/folder/{id}/links | Get folder external links
[**get_folder_path**](#get_folder_path) | **GET** /api/2.0/files/folder/{folderId}/path | Get the folder path
[**get_folder_primary_external_link**](#get_folder_primary_external_link) | **GET** /api/2.0/files/folder/{id}/link | Get the folder primary external link
[**get_folders**](#get_folders) | **GET** /api/2.0/files/{folderId}/subfolders | Get subfolders
[**get_forms_folder**](#get_forms_folder) | **GET** /api/2.0/files/@forms | Get the Forms section
[**get_my_folder**](#get_my_folder) | **GET** /api/2.0/files/@my | Get the My documents section
[**get_new_folder_items**](#get_new_folder_items) | **GET** /api/2.0/files/{folderId}/news | Get new folder items
[**get_recent_folder**](#get_recent_folder) | **GET** /api/2.0/files/recent | Get the Recent section
[**get_report_folder_history**](#get_report_folder_history) | **GET** /api/2.0/files/folder/{folderId}/log/report | Get the folder history report generation status
[**get_root_folders**](#get_root_folders) | **GET** /api/2.0/files/@root | Get filtered sections
[**get_trash_folder**](#get_trash_folder) | **GET** /api/2.0/files/@trash | Get the Trash section
[**insert_file**](#insert_file) | **POST** /api/2.0/files/{folderId}/insert | Insert a file
[**insert_file_to_my_from_body**](#insert_file_to_my_from_body) | **POST** /api/2.0/files/@my/insert | Insert a file into My documents
[**rename_folder**](#rename_folder) | **PUT** /api/2.0/files/folder/{folderId} | Rename a folder
[**set_folder_order**](#set_folder_order) | **PUT** /api/2.0/files/folder/{folderId}/order | Set folder order
[**set_folder_primary_external_link**](#set_folder_primary_external_link) | **PUT** /api/2.0/files/folder/{id}/links | Set the folder external link
[**terminate_report_folder_history**](#terminate_report_folder_history) | **DELETE** /api/2.0/files/folder/{folderId}/log/report | Terminate the folder history report generation
[**upload_file**](#upload_file) | **POST** /api/2.0/files/{folderId}/upload | Upload a file
[**upload_file_to_my**](#upload_file_to_my) | **POST** /api/2.0/files/@my/upload | Upload a file to My documents


# **check_upload**
> STRINGArrayWrapper check_upload(folder_id, check_upload_request)

Reports which of the submitted titles already belong to a file in the folder, so an upload can decide in
advance whether to overwrite or to ask for another name. Only the clashing titles come back, unordered and
without repetitions, and an empty array means every name is free. Matching is by title and ignores case, so a
name that differs only in capitalisation is still reported; an existing file that is encrypted is left out,
because an upload cannot take it over. The call changes nothing. It needs the same right as the upload itself,
the right to add content to the folder, which room managers and content creators have and readers, editors and
guests do not; an archived room, a section root and a folder the caller cannot write to are all refused, while
an unknown folder is answered as missing. A request without `filesTitle` is rejected as an invalid request, an
empty list is accepted and answers with an empty array.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **Union[int, str]**| The folder whose contents the names are tested against; take the id from a listing such as  `GET api/2.0/files/@root`. | 
 **check_upload_request** | [**CheckUploadRequest**](CheckUploadRequest.md)| The names to test against the files the folder already holds. | 

### Return type

[**STRINGArrayWrapper**](STRINGArrayWrapper.md)

### Third-party storage

The same method serves an entry in a connected third-party storage, whose identifier is a string such as `sbox-42`: pass `folder_id: str`.

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
    folder_id = 1 # int | The folder whose contents the names are tested against; take the id from a listing such as  `GET api/2.0/files/@root`.
    check_upload_request = docspace_api_sdk.CheckUploadRequest() # CheckUploadRequest | The names to test against the files the folder already holds.

    try:
        # Check for upload conflicts
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
**200** | The submitted titles that already belong to a file in the folder |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder**
> FolderWrapper create_folder(folder_id, create_folder)

Creates a folder inside the folder named in the path and answers with the folder as it was stored. The title
is trimmed, may not be blank and is refused when it is longer than the limit the schema prints; titles are not
required to be unique, so creating the same title twice leaves two folders side by side, which makes the call
mutating and not idempotent. The caller needs the right to create content in the parent, which the room
manager, a content creator and the owner of a personal section have; a member without that right, an archived
parent, and a section root that only holds rooms - Rooms, Forms and AI agents - are all refused, as is a
parent that does not exist. Rooms are not created here: use `POST api/2.0/files/rooms` for those, and this
operation for ordinary folders within them. Members of the room are notified of the new folder. Read the
identifier of the new folder from `id` and fill it with `POST api/2.0/files/{folderId}/upload`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **Union[int, str]**| The folder the request is addressed to: when a folder is created it is the parent that receives the new  folder, and when a folder is renamed it is the folder that gets the new title. | 
 **create_folder** | [**CreateFolder**](CreateFolder.md)| The title carried by the request body. | 

### Return type

[**FolderWrapper**](FolderWrapper.md)

### Third-party storage

The same method serves an entry in a connected third-party storage, whose identifier is a string such as `sbox-42`: pass `folder_id: str` and the answer is [**ThirdPartyFolderWrapper**](ThirdPartyFolderWrapper.md).

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.create_folder import CreateFolder
from docspace_api_sdk.models.folder_wrapper import FolderWrapper
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
    folder_id = 1 # int | The folder the request is addressed to: when a folder is created it is the parent that receives the new  folder, and when a folder is renamed it is the folder that gets the new title.
    create_folder = docspace_api_sdk.CreateFolder() # CreateFolder | The title carried by the request body.

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
**200** | The folder that was created |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder_primary_external_link**
> FileShareWrapper create_folder_primary_external_link(id, folder_link_request)

Answers with the primary external link of a folder or a room, creating it on the first call and returning the
one that already exists afterwards, so the operation is idempotent in effect: a second call with other
parameters does not reconfigure the existing link, and changing one is the business of
`PUT api/2.0/files/folder/{id}/links`. The parameters therefore only shape the link at the moment it is born -
`access` its rights, `title` its name, `expirationDate` its lifetime, which is unlimited here unless one is
given, `internal` whether only signed-in members may follow it, `denyDownload` whether the contents may only
be viewed, and `password` a secret to be asked for. Sending `access` with the value that grants nothing
creates no link and answers with nothing. The caller needs the right to manage the links of the room the
folder belongs to, which its manager and a portal administrator acting as room manager have, and a member with
content-creator or read access is refused with 403; an unknown folder is answered with 404. Read the address
from `sharedTo.shareLink`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Union[int, str]**| The folder or room the link belongs to. | 
 **folder_link_request** | [**FolderLinkRequest**](FolderLinkRequest.md)| The link and the way it is to be shaped. | 

### Return type

[**FileShareWrapper**](FileShareWrapper.md)

### Third-party storage

The same method serves an entry in a connected third-party storage, whose identifier is a string such as `sbox-42`: pass `id: str`.

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
    id = 1 # int | The folder or room the link belongs to.
    folder_link_request = docspace_api_sdk.FolderLinkRequest() # FolderLinkRequest | The link and the way it is to be shaped.

    try:
        # Create the folder primary external link
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
**200** | The primary external link of the folder |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller may not manage the links of this folder |  -  |
**404** | The folder does not exist |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_report_folder_history**
> DocumentBuilderTaskWrapper create_report_folder_history(folder_id, format=format, var_from=var_from, to=to)

Queues a background job that renders the history of a folder into a spreadsheet, or into a CSV file when
`format` asks for one, and saves the result in the caller's My documents. The answer is the queued task, not
the report: poll `GET api/2.0/files/folder/{folderId}/log/report` until `isCompleted` is true, then take the
file from `resultFileId`, `resultFileName` and `resultFileUrl`, of which a CSV report fills only the last two.
`from` and `to` limit the exported period; leaving both out exports the whole history. While a report for the
same folder and caller is still running, this call joins it and answers with the running task instead of
starting a second one, so retrying is safe. The caller needs read access to the folder and may not be a guest,
and the portal plan has to include the audit feature - otherwise the call is refused, with 403 for the access
rule and 404 for a folder that does not exist. Only a portal administrator gets the address, browser and
platform columns. Give up a running report with `DELETE api/2.0/files/folder/{folderId}/log/report`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder whose history is exported; the report covers the folder itself and the entries inside it. | 
 **format** | [**AuditReportFormat**](.md)| The shape the report is written in: `Xlsx` produces a spreadsheet that is saved as a file of the portal, while  `Csv` produces a comma-separated text file that is uploaded to My documents without being reported back with  a file identifier. | [optional] 
 **var_from** | **datetime**| The earliest moment an exported entry may have, read in the time zone of the portal; left out, the report  starts at the oldest entry the portal still keeps. | [optional] 
 **to** | **datetime**| The latest moment an exported entry may have, read in the time zone of the portal; left out, the report ends  at the newest entry. | [optional] 

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
    folder_id = 1 # int | The folder whose history is exported; the report covers the folder itself and the entries inside it.
    format = docspace_api_sdk.AuditReportFormat() # AuditReportFormat | The shape the report is written in: `Xlsx` produces a spreadsheet that is saved as a file of the portal, while  `Csv` produces a comma-separated text file that is uploaded to My documents without being reported back with  a file identifier. (optional)
    var_from = '2025-01-01T00:00:00' # datetime | The earliest moment an exported entry may have, read in the time zone of the portal; left out, the report  starts at the oldest entry the portal still keeps. (optional)
    to = '2025-12-31T23:59:59' # datetime | The latest moment an exported entry may have, read in the time zone of the portal; left out, the report ends  at the newest entry. (optional)

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
**200** | The queued report task |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller may not export the history of this folder |  -  |
**404** | The folder does not exist |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> FileOperationArrayWrapper delete_folder(folder_id, delete_folder)

Queues the deletion of one folder together with everything inside it, and answers with the file operations of
the caller, the one just created among them. The folder is not gone when the response arrives: poll
`GET api/2.0/files/fileops` until the operation reports `finished`, and read its `error` to learn whether the
deletion succeeded. By default the folder is moved to the Trash section, from where it can be restored;
`immediately=true` discards it for good instead, and inside a room, where there is no Trash, deletion is
always final. `deleteAfter=true` postpones the deletion until the editing sessions on the contents have ended,
so files somebody is working on are not pulled away. The caller needs the right to delete the folder, which
the room manager, a portal administrator acting as room manager and a content creator acting on a folder of
their own have; editing access alone, read access and a guest are refused. The call is destructive. To delete
several items at once use `PUT api/2.0/files/fileops/delete`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **Union[int, str]**| The folder to delete, together with everything it holds. | 
 **delete_folder** | [**DeleteFolder**](DeleteFolder.md)| How the deletion is to be carried out. | 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Third-party storage

The same method serves an entry in a connected third-party storage, whose identifier is a string such as `sbox-42`: pass `folder_id: str`.

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
    folder_id = 10 # int | The folder to delete, together with everything it holds.
    delete_folder = docspace_api_sdk.DeleteFolder() # DeleteFolder | How the deletion is to be carried out.

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
**200** | The file operations of the caller, including the deletion just queued |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_xlsx_by_folder**
> XlsxReportResponseWrapper generate_xlsx_by_folder(folder_id)

Rebuilds the spreadsheet that gathers the answers submitted to a form, starting from the Complete folder
that holds the filled copies. The answer names the original form the results belong to, says in `isNewFile`
whether the spreadsheet is being created or an existing one rewritten in place, and carries the queued job in
`task`; the file itself is not ready yet, so poll `GET api/2.0/files/file/{fileId}/xlsx` with the identifier
of the form until the task reports completion. The folder has to be the Complete folder of a form-filling
room and has to hold at least one submitted copy whose original form still exists, and the caller needs the
right to maintain that form, which the room manager has. A folder that does not exist, or one that holds
nothing to report on, is answered with 404, and a folder of the wrong kind or a caller without those rights
with 403. The call is mutating: it writes the results file of the form.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder the operation acts on. Take the identifier from a listing such as `GET api/2.0/files/@root` or  `GET api/2.0/files/{folderId}`: a folder stored in the portal is numbered, while a folder in a connected  third-party account is named by an opaque string. | 

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
    folder_id = 1 # int | The folder the operation acts on. Take the identifier from a listing such as `GET api/2.0/files/@root` or  `GET api/2.0/files/{folderId}`: a folder stored in the portal is numbered, while a folder in a connected  third-party account is named by an opaque string.

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
**200** | The queued report task together with the form the answers belong to |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The folder is not a completed-forms folder, or the caller may not maintain the form |  -  |
**404** | The folder, the submitted copy or the original form was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorites_folder**
> FolderContentWrapper get_favorites_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)

Returns the caller's own Favorites section: the files and folders this account has marked as favorite,
together with the section folder itself. Favorites are per-account, so the entries another member marked are
not listed here, and a guest sees only their own, usually empty, list. Mark a single file with
`GET api/2.0/files/favorites/{fileId}`, or add and remove batches of files and folders with
`POST api/2.0/files/favorites` and `DELETE api/2.0/files/favorites`. Nothing in the section is modified,
though passing `sortBy` saves the requested order as the default order for this account. Entries the caller
can no longer read, and entries that have been moved to the Trash section, drop out of the listing even
though their favorite mark stays, so the section can shrink without an explicit unmark. `folders` and `files`
hold one page of the section, `total` counts the entries matching the request before `count` and `startIndex`
are applied, and `current` describes the section folder itself.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_group_id** | **UUID**| Restricts the listing to the entries authored by this portal member, or by the members of this group; the same  parameter accepts either kind of identifier. Omit it to list everything the caller can read. | [optional] 
 **filter_type** | [**FilterType**](.md)| Narrows the listing to a single kind of entry, such as documents, images or one type of room. Omit it to list  every kind the section holds. | [optional] 
 **count** | **int**| The size of one page of section content. Pair it with `startIndex` to walk the listing, and compare the two  with `total` in the response to see when the last page has been read. | [optional] 
 **start_index** | **int**| The number of matching entries to skip before the returned page begins; add `count` to it to ask for the next  page. | [optional] 
 **sort_by** | **str**| The name of the field the entries are ordered by, matched case-insensitively against the file sort fields:  `DateAndTime`, `AZ`, `Size`, `Author`, `Type`, `New`, `DateAndTimeCreation`, `RoomType`, `Tags`, `Room`,  `CustomOrder`, `LastOpened` and `UsedSpace`. A recognized value is also saved as the default order of the  account and reused by later listings that omit the parameter, while a value matching none of the fields leaves  that saved order in place. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The direction in which the `sortBy` field is ordered. It is saved together with `sortBy` as the default order  of the account. | [optional] 
 **filter_value** | **str**| The search string the section is filtered by: it is matched as a substring of entry titles and, for files,  against the indexed document content as well. Omit it to list the section unfiltered. | [optional] 

### Return type

[**FolderContentWrapper**](FolderContentWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.filter_type import FilterType
from docspace_api_sdk.models.folder_content_wrapper import FolderContentWrapper
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
    user_id_or_group_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Restricts the listing to the entries authored by this portal member, or by the members of this group; the same  parameter accepts either kind of identifier. Omit it to list everything the caller can read. (optional)
    filter_type = docspace_api_sdk.FilterType() # FilterType | Narrows the listing to a single kind of entry, such as documents, images or one type of room. Omit it to list  every kind the section holds. (optional)
    count = 25 # int | The size of one page of section content. Pair it with `startIndex` to walk the listing, and compare the two  with `total` in the response to see when the last page has been read. (optional)
    start_index = 0 # int | The number of matching entries to skip before the returned page begins; add `count` to it to ask for the next  page. (optional)
    sort_by = 'DateAndTime' # str | The name of the field the entries are ordered by, matched case-insensitively against the file sort fields:  `DateAndTime`, `AZ`, `Size`, `Author`, `Type`, `New`, `DateAndTimeCreation`, `RoomType`, `Tags`, `Room`,  `CustomOrder`, `LastOpened` and `UsedSpace`. A recognized value is also saved as the default order of the  account and reused by later listings that omit the parameter, while a value matching none of the fields leaves  that saved order in place. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The direction in which the `sortBy` field is ordered. It is saved together with `sortBy` as the default order  of the account. (optional)
    filter_value = 'My Document' # str | The search string the section is filtered by: it is matched as a substring of entry titles and, for files,  against the indexed document content as well. Omit it to list the section unfiltered. (optional)

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
**200** | The Favorites section with one page of the entries the caller marked as favorite |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not allowed to read the Favorites section |  -  |
**404** | The Favorites section could not be resolved for this account |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files_used_space**
> FilesStatisticsResultWrapper get_files_used_space()

Reports how much storage the portal spends on documents, split by section - My documents, Trash, Rooms,
Archive and, where the feature is on, AI agents - each entry naming the section and the space it takes in
bytes. The figures cover the whole portal rather than the calling account, and moving an entry between
sections moves its space with it, which is why deleting a file to the Trash does not free anything until the
Trash is emptied. Only a caller who may change portal settings, that is the owner and the portal
administrators, is allowed here; a room administrator, an ordinary member and a guest are all refused. The
call is read-only, takes no parameters and answers with the sections in a fixed order. The quota of the portal
as a whole, storage outside documents included, is not part of this answer.

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
**200** | The space taken by documents in each section, in bytes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder**
> FormsItemArrayWrapper get_folder(folder_id)

Lists the fields the completed forms of a form-filling room carry, each of them a key and the kind of value
behind it, so that a client can offer them as filters. Feed a pair from this list back as `formsItemKey` and
`formsItemType` of `GET api/2.0/files/{folderId}` to keep only the completed forms whose field of that name
holds a value. The fields are read from the search index of one of the forms already gathered, so they appear
once indexing has caught up with the first submission. Only the Complete folder of a form-filling room
carries such fields: for any other folder, for a folder that does not exist and for one that has been deleted
the answer is an empty list rather than a refusal, and the same holds while nothing has been submitted yet.
The operation reads the index alone, changes nothing and needs no authorization.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder the operation acts on. Take the identifier from a listing such as `GET api/2.0/files/@root` or  `GET api/2.0/files/{folderId}`: a folder stored in the portal is numbered, while a folder in a connected  third-party account is named by an opaque string. | 

### Return type

[**FormsItemArrayWrapper**](FormsItemArrayWrapper.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.forms_item_array_wrapper import FormsItemArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 1 # int | The folder the operation acts on. Take the identifier from a listing such as `GET api/2.0/files/@root` or  `GET api/2.0/files/{folderId}`: a folder stored in the portal is numbered, while a folder in a connected  third-party account is named by an opaque string.

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
**200** | The form fields that can be used as filters, empty when the folder carries none |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_by_folder_id**
> FolderContentWrapper get_folder_by_folder_id(folder_id, user_id_or_group_id=user_id_or_group_id, shared_by=shared_by, filter_type=filter_type, room_id=room_id, folder_type=folder_type, exclude_subject=exclude_subject, apply_filter_option=apply_filter_option, with_sub_folders=with_sub_folders, extension=extension, search_area=search_area, forms_item_key=forms_item_key, forms_item_type=forms_item_type, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value, location=location)

Returns one page of the contents of a folder - its subfolders in `folders`, its files in `files`, the folder
itself in `current` and the chain of parents in `pathParts` - and is the operation a client browses the file
tree with. `filterType`, `filterValue`, `extension`, `userIdOrGroupId`, `sharedBy` and `folderType` narrow
what is listed, `applyFilterOption` decides whether those filters bite on the files, on the folders or on
both, and `withSubFolders`, which is on unless it is switched off, lets a narrowed request descend through the
whole subtree instead of the top level alone. `filterValue` is matched against titles and against indexed
document content, and indexing is asynchronous, so a file uploaded a moment ago can be missing from a search
for a short while. `count` and `startIndex` page through the result while `total` counts everything that
matches, and `sortBy` with `sortOrder` both order the page and are saved as the default order of the account.
Reading a room or an ordinary folder clears its new-item marks for the caller. A caller who may not read the
folder is answered with 403, and a folder that does not exist with 404.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **Union[int, str]**| The folder whose contents are listed. Each section root has an operation of its own, such as  `GET api/2.0/files/@my`, and every other folder is opened by the identifier a listing gave for it. | 
 **user_id_or_group_id** | **UUID**| Restricts the listing to the entries authored by this portal member, or by the members of this group; the same  parameter accepts either kind of identifier. Omit it to list everything the caller can read. | [optional] 
 **shared_by** | **UUID**| Restricts the listing to the entries this member shared, which narrows a shared listing down to what one  person handed out. | [optional] 
 **filter_type** | [**FilterType**](.md)| Narrows the listing to a single kind of entry, such as documents, spreadsheets, images or one type of room.  Omit it to list every kind the folder holds. | [optional] 
 **room_id** | **Union[int, str]**| Keeps only the entries that lie in this room, which matters when the listing being read gathers entries from  more than one of them. | [optional] 
 **folder_type** | [**List[int]**](int.md)| Keeps only the folders of these kinds, each given as the number of a folder type; it is how a listing is  narrowed down to, say, the form-filling folders of a room. | [optional] 
 **exclude_subject** | **bool**| Turns `userIdOrGroupId` around: with true the entries of that member or group are the ones left out, with  false they are the only ones kept. | [optional] 
 **apply_filter_option** | [**ApplyFilterOption**](.md)| Chooses which half of the listing `filterType` and `filterValue` are applied to: with `Files` the folders come  back unfiltered, with `Folders` the files do, and with `All` both halves are filtered. | [optional] 
 **with_sub_folders** | **bool**| Whether a narrowed request reaches into the subfolders: with true, which is what an omitted parameter means,  matching entries are gathered from the whole subtree, with false only the top level is read. It makes a  difference only once `filterType`, `userIdOrGroupId` or `filterValue` narrows the request, because an  unfiltered listing always shows the top level alone. | [optional] 
 **extension** | **str**| Keeps only the files carrying one of these extensions, several of them separated by commas; the leading dot is  optional. | [optional] 
 **search_area** | [**SearchArea**](.md)| Which area a listing that spans several of them is taken from - the active rooms, the archive, the room  templates or the form-filling rooms. A folder that belongs to one area only settles the area itself and  ignores the parameter. | [optional] 
 **forms_item_key** | **str**| Keeps only the completed forms whose form field of this name holds a value. Take the name from  `GET api/2.0/files/{folderId}/formfilter`, and use it in the folder that gathers the completed copies of a  form-filling room. | [optional] 
 **forms_item_type** | **str**| The kind of the form field named by `formsItemKey`, taken from the same list; the two are sent together. | [optional] 
 **count** | **int**| The size of one page of the listing. Pair it with `startIndex` to walk through the result, and compare the two  with `total` in the response to see when the last page has been read. | [optional] 
 **start_index** | **int**| The number of matching entries to skip before the returned page begins; add `count` to it to ask for the next  page. | [optional] 
 **sort_by** | **str**| The name of the field the entries are ordered by, matched case-insensitively against the file sort fields:  `DateAndTime`, `AZ`, `Size`, `Author`, `Type`, `New`, `DateAndTimeCreation`, `RoomType`, `Tags`, `Room`,  `CustomOrder`, `LastOpened` and `UsedSpace`. A recognized value is also saved as the default order of the  account and reused by later listings that omit the parameter, while a value matching none of the fields leaves  that saved order in place. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The direction in which the `sortBy` field is ordered. It is saved together with `sortBy` as the default order  of the account. | [optional] 
 **filter_value** | **str**| The search string the listing is filtered by: it is matched as a substring of entry titles and, for files,  against the indexed document content as well. Omit it to list the folder unfiltered. | [optional] 
 **location** | [**Location**](.md)| Where the entries of a tag-based listing have to live to be kept: `Room` keeps what lies in a room,  `Documents` what lies in a personal section, and `Link` what was reached through an external link that is  still valid. It shapes the Favorites and Recent listings and does nothing in an ordinary folder. | [optional] 

### Return type

[**FolderContentWrapper**](FolderContentWrapper.md)

### Third-party storage

The same method serves an entry in a connected third-party storage, whose identifier is a string such as `sbox-42`: pass `folder_id: str` `room_id: str` and the answer is [**ThirdPartyFolderContentWrapper**](ThirdPartyFolderContentWrapper.md).

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.apply_filter_option import ApplyFilterOption
from docspace_api_sdk.models.filter_type import FilterType
from docspace_api_sdk.models.folder_content_wrapper import FolderContentWrapper
from docspace_api_sdk.models.location import Location
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

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 1 # int | The folder whose contents are listed. Each section root has an operation of its own, such as  `GET api/2.0/files/@my`, and every other folder is opened by the identifier a listing gave for it.
    user_id_or_group_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Restricts the listing to the entries authored by this portal member, or by the members of this group; the same  parameter accepts either kind of identifier. Omit it to list everything the caller can read. (optional)
    shared_by = UUID('00000000-0000-0000-0000-000000000000') # UUID | Restricts the listing to the entries this member shared, which narrows a shared listing down to what one  person handed out. (optional)
    filter_type = docspace_api_sdk.FilterType() # FilterType | Narrows the listing to a single kind of entry, such as documents, spreadsheets, images or one type of room.  Omit it to list every kind the folder holds. (optional)
    room_id = 1 # int | Keeps only the entries that lie in this room, which matters when the listing being read gathers entries from  more than one of them. (optional)
    folder_type = [[2]] # List[int] | Keeps only the folders of these kinds, each given as the number of a folder type; it is how a listing is  narrowed down to, say, the form-filling folders of a room. (optional)
    exclude_subject = false # bool | Turns `userIdOrGroupId` around: with true the entries of that member or group are the ones left out, with  false they are the only ones kept. (optional)
    apply_filter_option = docspace_api_sdk.ApplyFilterOption() # ApplyFilterOption | Chooses which half of the listing `filterType` and `filterValue` are applied to: with `Files` the folders come  back unfiltered, with `Folders` the files do, and with `All` both halves are filtered. (optional)
    with_sub_folders = true # bool | Whether a narrowed request reaches into the subfolders: with true, which is what an omitted parameter means,  matching entries are gathered from the whole subtree, with false only the top level is read. It makes a  difference only once `filterType`, `userIdOrGroupId` or `filterValue` narrows the request, because an  unfiltered listing always shows the top level alone. (optional)
    extension = 'docx,pdf' # str | Keeps only the files carrying one of these extensions, several of them separated by commas; the leading dot is  optional. (optional)
    search_area = docspace_api_sdk.SearchArea() # SearchArea | Which area a listing that spans several of them is taken from - the active rooms, the archive, the room  templates or the form-filling rooms. A folder that belongs to one area only settles the area itself and  ignores the parameter. (optional)
    forms_item_key = 'first_name' # str | Keeps only the completed forms whose form field of this name holds a value. Take the name from  `GET api/2.0/files/{folderId}/formfilter`, and use it in the folder that gathers the completed copies of a  form-filling room. (optional)
    forms_item_type = 'text' # str | The kind of the form field named by `formsItemKey`, taken from the same list; the two are sent together. (optional)
    count = 25 # int | The size of one page of the listing. Pair it with `startIndex` to walk through the result, and compare the two  with `total` in the response to see when the last page has been read. (optional)
    start_index = 0 # int | The number of matching entries to skip before the returned page begins; add `count` to it to ask for the next  page. (optional)
    sort_by = 'DateAndTime' # str | The name of the field the entries are ordered by, matched case-insensitively against the file sort fields:  `DateAndTime`, `AZ`, `Size`, `Author`, `Type`, `New`, `DateAndTimeCreation`, `RoomType`, `Tags`, `Room`,  `CustomOrder`, `LastOpened` and `UsedSpace`. A recognized value is also saved as the default order of the  account and reused by later listings that omit the parameter, while a value matching none of the fields leaves  that saved order in place. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The direction in which the `sortBy` field is ordered. It is saved together with `sortBy` as the default order  of the account. (optional)
    filter_value = 'My Document' # str | The search string the listing is filtered by: it is matched as a substring of entry titles and, for files,  against the indexed document content as well. Omit it to list the folder unfiltered. (optional)
    location = docspace_api_sdk.Location() # Location | Where the entries of a tag-based listing have to live to be kept: `Room` keeps what lies in a room,  `Documents` what lies in a personal section, and `Link` what was reached through an external link that is  still valid. It shapes the Favorites and Recent listings and does nothing in an ordinary folder. (optional)

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
**200** | One page of the folder contents, with the folder itself and the chain of its parents |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller may not read this folder |  -  |
**404** | The folder does not exist |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_history**
> HistoryArrayWrapper get_folder_history(folder_id, from_date=from_date, to_date=to_date, count=count, start_index=start_index)

Lists what has happened to a folder and to the entries inside it - creations, renames, uploads, moves,
deletions and changes of access - each record naming the action, the moment it happened and the member behind
it. Records that belong to one action are grouped, so a batch arrives as a single entry carrying the rest of
itself in `related`, and the list runs from the most recent record backwards. `fromDate` and `toDate` narrow
the period, `startIndex` and `count` page through the result, and the number of records matching the request
is reported in the response headers rather than in the body. Any member who can read the folder may read its
history; a caller without access is answered with 403 and a folder that does not exist with 404. When the
folder is a form-filling folder the caller reached through a filling invitation, the history is narrowed to
what that caller may see. The call is read-only. To take the same history away as a spreadsheet, start a
report with `POST api/2.0/files/folder/{folderId}/log/report`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder whose activity log is read; the log covers the folder itself and the entries inside it. | 
 **from_date** | **datetime**| The earliest moment an entry may have, read in the time zone of the portal; left out, the log starts at the  oldest entry the portal still keeps. | [optional] 
 **to_date** | **datetime**| The latest moment an entry may have, read in the time zone of the portal; left out, the log ends at the newest  entry. | [optional] 
 **count** | **int**| How many entries one page holds. The number of entries that match the query is reported in the response  headers, not in the body. | [optional] 
 **start_index** | **int**| How many entries to skip before the page begins, counted from the newest one, so pages are taken by adding the  page size to it. | [optional] 

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
    folder_id = 1 # int | The folder whose activity log is read; the log covers the folder itself and the entries inside it.
    from_date = '2025-01-01T00:00:00.0000000Z' # datetime | The earliest moment an entry may have, read in the time zone of the portal; left out, the log starts at the  oldest entry the portal still keeps. (optional)
    to_date = '2025-12-31T23:59:59.0000000Z' # datetime | The latest moment an entry may have, read in the time zone of the portal; left out, the log ends at the newest  entry. (optional)
    count = 25 # int | How many entries one page holds. The number of entries that match the query is reported in the response  headers, not in the body. (optional)
    start_index = 0 # int | How many entries to skip before the page begins, counted from the newest one, so pages are taken by adding the  page size to it. (optional)

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
**200** | One page of the folder history, the most recent record first |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller may not read this folder |  -  |
**404** | The folder does not exist |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_info**
> FolderWrapper get_folder_info(folder_id)

Returns one folder as an object - its title, its parent, the moments it was created and last changed, the
access the caller has to it, the number of items that are new for them, and the room settings when the folder
is a room - without listing anything inside it. Use it to resolve a folder identifier into something
displayable, and `GET api/2.0/files/{folderId}` when the contents are what is wanted; unlike that operation,
this one leaves the new-item marks of the folder alone. Any member who can read the folder may call it, and an
anonymous caller only through an external link that grants access, everybody else being refused; a folder that
does not exist is answered as not found. The call is read-only. The chain of parents above the folder is not
part of the answer and is read with `GET api/2.0/files/folder/{folderId}/path`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **Union[int, str]**| The folder the operation acts on. Take the identifier from a listing such as `GET api/2.0/files/@root` or  `GET api/2.0/files/{folderId}`: a folder stored in the portal is numbered, while a folder in a connected  third-party account is named by an opaque string. | 

### Return type

[**FolderWrapper**](FolderWrapper.md)

### Third-party storage

The same method serves an entry in a connected third-party storage, whose identifier is a string such as `sbox-42`: pass `folder_id: str` and the answer is [**ThirdPartyFolderWrapper**](ThirdPartyFolderWrapper.md).

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.folder_wrapper import FolderWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    folder_id = 1 # int | The folder the operation acts on. Take the identifier from a listing such as `GET api/2.0/files/@root` or  `GET api/2.0/files/{folderId}`: a folder stored in the portal is numbered, while a folder in a connected  third-party account is named by an opaque string.

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
**200** | The folder itself - its title, its parent, the moments it was created and changed, the access the caller has to it, how many items in it are new for them, and the room settings when the folder is a room; nothing about the items it holds |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_links**
> FileShareArrayWrapper get_folder_links(id)

Lists the external links of a folder or a room, each with its identifier, title, address, rights, expiration
date, password flag and download restriction, the primary link among them once it exists. At most the first
hundred links are answered and the number returned is reported in the response headers; there are no paging
parameters here. A folder that has never been shared by link answers with an empty list, and so does a member
who may read the folder but not manage its links - the empty answer therefore means nothing to show you
rather than no links exist. A member without access to the room is refused, an anonymous caller is rejected,
and a folder that does not exist is answered as not found. The call is read-only. Take an identifier from here
to `PUT api/2.0/files/folder/{id}/links` to change or remove that link, and read the primary one alone with
`GET api/2.0/files/folder/{id}/link`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Union[int, str]**| The folder or room whose external links are listed. | 

### Return type

[**FileShareArrayWrapper**](FileShareArrayWrapper.md)

### Third-party storage

The same method serves an entry in a connected third-party storage, whose identifier is a string such as `sbox-42`: pass `id: str`.

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
    id = 1 # int | The folder or room whose external links are listed.

    try:
        # Get folder external links
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
**200** | The external links of the folder the caller may manage |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_path**
> FileEntryBaseArrayWrapper get_folder_path(folder_id)

Returns the chain of folders that leads to the folder named in the path, ordered from the section root down to
the folder itself, which is the last entry. It is what a breadcrumb trail is built from, and it also tells a
client which section - a room, the personal section, the archive - a bare folder identifier belongs to. Only
the folders the caller may see are part of the chain, so a member who was given access to a folder deep inside
a room gets a shorter path than the room manager does. The caller needs read access to the folder and is
otherwise answered with 403, while a folder that does not exist is answered as not found. The call is
read-only and takes no paging parameters. To go the other way, from a folder down into its contents, call
`GET api/2.0/files/{folderId}`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **Union[int, str]**| The folder the operation acts on. Take the identifier from a listing such as `GET api/2.0/files/@root` or  `GET api/2.0/files/{folderId}`: a folder stored in the portal is numbered, while a folder in a connected  third-party account is named by an opaque string. | 

### Return type

[**FileEntryBaseArrayWrapper**](FileEntryBaseArrayWrapper.md)

### Third-party storage

The same method serves an entry in a connected third-party storage, whose identifier is a string such as `sbox-42`: pass `folder_id: str`.

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
    folder_id = 1 # int | The folder the operation acts on. Take the identifier from a listing such as `GET api/2.0/files/@root` or  `GET api/2.0/files/{folderId}`: a folder stored in the portal is numbered, while a folder in a connected  third-party account is named by an opaque string.

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
**200** | The chain of folders leading to the folder, the section root first |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller may not read this folder |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_primary_external_link**
> FileShareWrapper get_folder_primary_external_link(id, count=count, start_index=start_index)

Answers with the primary external link of a folder or a room - the one the Copy link action of a client
hands out - with its address in `sharedTo.shareLink`, its rights in `access`, and its title, expiration date,
password flag and download restriction beside them. The link is created on the first read if the folder has
none, with read rights, no password and no expiry, so this operation mutates on that first call and is a plain
read afterwards; repeated calls answer with the same link identifier. The caller needs the right to manage the
links of the room the folder belongs to, which its manager and a portal administrator acting as room manager
have; a member with read access alone is refused with 403 and an anonymous caller is rejected, while a link
that was deliberately revoked is answered with 404 rather than being recreated. The paging parameters are
accepted for compatibility and leave the single link answered here unchanged. Every external link of the same
folder is listed by `GET api/2.0/files/folder/{id}/links`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Union[int, str]**| The folder or room the operation addresses. A folder stored on the portal is numbered, while a folder in a  connected third-party account is named by an opaque string. | 
 **count** | **int**| How many entries at most to answer with, in the operations of this folder that return a list; an operation  that answers with a single object is not affected by it. | [optional] 
 **start_index** | **int**| How many entries of such a list to skip before answering, used together with `count` to walk through it page  by page. | [optional] 

### Return type

[**FileShareWrapper**](FileShareWrapper.md)

### Third-party storage

The same method serves an entry in a connected third-party storage, whose identifier is a string such as `sbox-42`: pass `id: str`.

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_share_wrapper import FileShareWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FoldersApi(api_client)
    id = 10 # int | The folder or room the operation addresses. A folder stored on the portal is numbered, while a folder in a  connected third-party account is named by an opaque string.
    count = 25 # int | How many entries at most to answer with, in the operations of this folder that return a list; an operation  that answers with a single object is not affected by it. (optional)
    start_index = 0 # int | How many entries of such a list to skip before answering, used together with `count` to walk through it page  by page. (optional)

    try:
        # Get the folder primary external link
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
**200** | The primary external link of the folder |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller may not manage the links of this folder |  -  |
**404** | The folder does not exist, or its primary link was revoked |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folders**
> FileEntryBaseArrayWrapper get_folders(folder_id)

Lists the folders that sit directly inside the folder named in the path, ordered by title, without their own
contents and without the files that lie beside them. The whole list arrives at once - there are no paging or
filtering parameters here - so for a large folder, or when the files are wanted as well, use
`GET api/2.0/files/{folderId}`, which pages and filters. A folder that holds no subfolders answers with an
empty list. The caller needs read access to the folder, and only the subfolders they may see are listed, so a
member of a room can get fewer entries than its manager; a caller without access is answered with 403, and a
folder that does not exist, or one that has been deleted for good, is answered as not found. The call is
read-only and leaves the new-item marks of the folder alone.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **Union[int, str]**| The folder the operation acts on. Take the identifier from a listing such as `GET api/2.0/files/@root` or  `GET api/2.0/files/{folderId}`: a folder stored in the portal is numbered, while a folder in a connected  third-party account is named by an opaque string. | 

### Return type

[**FileEntryBaseArrayWrapper**](FileEntryBaseArrayWrapper.md)

### Third-party storage

The same method serves an entry in a connected third-party storage, whose identifier is a string such as `sbox-42`: pass `folder_id: str`.

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
    folder_id = 1 # int | The folder the operation acts on. Take the identifier from a listing such as `GET api/2.0/files/@root` or  `GET api/2.0/files/{folderId}`: a folder stored in the portal is numbered, while a folder in a connected  third-party account is named by an opaque string.

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
**200** | The direct subfolders of the folder, ordered by title |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller may not read this folder |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forms_folder**
> FolderContentWrapper get_forms_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)

Returns the Forms section: the flat list of form-filling rooms the caller may read. Such rooms are stored
under the Rooms tree but are surfaced only here, so `GET api/2.0/files/rooms` leaves them out of the active
area and lists them when `searchArea` names the forms area instead. The section is not expanded into room
content, so `folders` carries the rooms while `files` comes back empty; to read what is inside one of them,
call `GET api/2.0/files/{folderId}` with the room identifier. Nothing is modified, though passing `sortBy`
saves the requested order as the default order for this account. `filterType`, `filterValue`,
`userIdOrGroupId` and the sorting parameters narrow and order the room list, `count` and `startIndex` page
through it, `total` reports how many rooms match the request in full, and `current` describes the section
folder itself.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_group_id** | **UUID**| Restricts the listing to the entries authored by this portal member, or by the members of this group; the same  parameter accepts either kind of identifier. Omit it to list everything the caller can read. | [optional] 
 **filter_type** | [**FilterType**](.md)| Narrows the listing to a single kind of entry, such as documents, images or one type of room. Omit it to list  every kind the section holds. | [optional] 
 **count** | **int**| The size of one page of section content. Pair it with `startIndex` to walk the listing, and compare the two  with `total` in the response to see when the last page has been read. | [optional] 
 **start_index** | **int**| The number of matching entries to skip before the returned page begins; add `count` to it to ask for the next  page. | [optional] 
 **sort_by** | **str**| The name of the field the entries are ordered by, matched case-insensitively against the file sort fields:  `DateAndTime`, `AZ`, `Size`, `Author`, `Type`, `New`, `DateAndTimeCreation`, `RoomType`, `Tags`, `Room`,  `CustomOrder`, `LastOpened` and `UsedSpace`. A recognized value is also saved as the default order of the  account and reused by later listings that omit the parameter, while a value matching none of the fields leaves  that saved order in place. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The direction in which the `sortBy` field is ordered. It is saved together with `sortBy` as the default order  of the account. | [optional] 
 **filter_value** | **str**| The search string the section is filtered by: it is matched as a substring of entry titles and, for files,  against the indexed document content as well. Omit it to list the section unfiltered. | [optional] 

### Return type

[**FolderContentWrapper**](FolderContentWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.filter_type import FilterType
from docspace_api_sdk.models.folder_content_wrapper import FolderContentWrapper
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
    user_id_or_group_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Restricts the listing to the entries authored by this portal member, or by the members of this group; the same  parameter accepts either kind of identifier. Omit it to list everything the caller can read. (optional)
    filter_type = docspace_api_sdk.FilterType() # FilterType | Narrows the listing to a single kind of entry, such as documents, images or one type of room. Omit it to list  every kind the section holds. (optional)
    count = 25 # int | The size of one page of section content. Pair it with `startIndex` to walk the listing, and compare the two  with `total` in the response to see when the last page has been read. (optional)
    start_index = 0 # int | The number of matching entries to skip before the returned page begins; add `count` to it to ask for the next  page. (optional)
    sort_by = 'DateAndTime' # str | The name of the field the entries are ordered by, matched case-insensitively against the file sort fields:  `DateAndTime`, `AZ`, `Size`, `Author`, `Type`, `New`, `DateAndTimeCreation`, `RoomType`, `Tags`, `Room`,  `CustomOrder`, `LastOpened` and `UsedSpace`. A recognized value is also saved as the default order of the  account and reused by later listings that omit the parameter, while a value matching none of the fields leaves  that saved order in place. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The direction in which the `sortBy` field is ordered. It is saved together with `sortBy` as the default order  of the account. (optional)
    filter_value = 'My Document' # str | The search string the section is filtered by: it is matched as a substring of entry titles and, for files,  against the indexed document content as well. Omit it to list the section unfiltered. (optional)

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
**200** | The Forms section with one page of the form-filling rooms available to the caller |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not allowed to read the Forms section |  -  |
**404** | The Forms section could not be resolved for this account |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_folder**
> FolderContentWrapper get_my_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, apply_filter_option=apply_filter_option, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)

Returns the contents of the caller's My documents section, the personal storage that belongs to this account
alone and stays invisible to other members until something in it is shared explicitly. Any authenticated
member that has a personal section can read it; guest accounts are not given one, and the call then answers
404. Nothing in the section is modified, though passing `sortBy` saves the requested order as the default
order for this account. Without a filter only the top level of the section is listed; as soon as `filterType`,
`userIdOrGroupId` or `filterValue` narrows the request, the search descends through the whole subtree.
`filterValue` is matched against titles and against indexed document content, and the index is written
asynchronously, so a file uploaded a moment ago can be missing from a search for a short while. `folders` and
`files` hold one page of the result, `total` counts everything that matches before `count` and `startIndex`
are applied, and `current` describes the section folder. To open a folder inside the section, call
`GET api/2.0/files/{folderId}` with its identifier.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_group_id** | **UUID**| Restricts the listing to the entries authored by this portal member, or by the members of this group; the same  parameter accepts either kind of identifier. Omit it to list everything the caller can read. | [optional] 
 **filter_type** | [**FilterType**](.md)| Narrows the listing to a single kind of entry, such as documents, images or one type of room. Omit it to list  every kind the section holds. | [optional] 
 **apply_filter_option** | [**ApplyFilterOption**](.md)| Chooses which half of the listing `filterType` and `filterValue` are applied to: with `Files` the folders come  back unfiltered, with `Folders` the files do, and with `All` both halves are filtered. | [optional] 
 **count** | **int**| The size of one page of section content. Pair it with `startIndex` to walk the listing, and compare the two  with `total` in the response to see when the last page has been read. | [optional] 
 **start_index** | **int**| The number of matching entries to skip before the returned page begins; add `count` to it to ask for the next  page. | [optional] 
 **sort_by** | **str**| The name of the field the entries are ordered by, matched case-insensitively against the file sort fields:  `DateAndTime`, `AZ`, `Size`, `Author`, `Type`, `New`, `DateAndTimeCreation`, `RoomType`, `Tags`, `Room`,  `CustomOrder`, `LastOpened` and `UsedSpace`. A recognized value is also saved as the default order of the  account and reused by later listings that omit the parameter, while a value matching none of the fields leaves  that saved order in place. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The direction in which the `sortBy` field is ordered. It is saved together with `sortBy` as the default order  of the account. | [optional] 
 **filter_value** | **str**| The search string the section is filtered by, matched as a substring of entry titles. Omit it to list the  section unfiltered. | [optional] 

### Return type

[**FolderContentWrapper**](FolderContentWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.apply_filter_option import ApplyFilterOption
from docspace_api_sdk.models.filter_type import FilterType
from docspace_api_sdk.models.folder_content_wrapper import FolderContentWrapper
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
    user_id_or_group_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Restricts the listing to the entries authored by this portal member, or by the members of this group; the same  parameter accepts either kind of identifier. Omit it to list everything the caller can read. (optional)
    filter_type = docspace_api_sdk.FilterType() # FilterType | Narrows the listing to a single kind of entry, such as documents, images or one type of room. Omit it to list  every kind the section holds. (optional)
    apply_filter_option = docspace_api_sdk.ApplyFilterOption() # ApplyFilterOption | Chooses which half of the listing `filterType` and `filterValue` are applied to: with `Files` the folders come  back unfiltered, with `Folders` the files do, and with `All` both halves are filtered. (optional)
    count = 25 # int | The size of one page of section content. Pair it with `startIndex` to walk the listing, and compare the two  with `total` in the response to see when the last page has been read. (optional)
    start_index = 0 # int | The number of matching entries to skip before the returned page begins; add `count` to it to ask for the next  page. (optional)
    sort_by = 'DateAndTime' # str | The name of the field the entries are ordered by, matched case-insensitively against the file sort fields:  `DateAndTime`, `AZ`, `Size`, `Author`, `Type`, `New`, `DateAndTimeCreation`, `RoomType`, `Tags`, `Room`,  `CustomOrder`, `LastOpened` and `UsedSpace`. A recognized value is also saved as the default order of the  account and reused by later listings that omit the parameter, while a value matching none of the fields leaves  that saved order in place. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The direction in which the `sortBy` field is ordered. It is saved together with `sortBy` as the default order  of the account. (optional)
    filter_value = 'My Document' # str | The search string the section is filtered by, matched as a substring of entry titles. Omit it to list the  section unfiltered. (optional)

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
**200** | The My documents section with one page of its contents |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not allowed to read the My documents section |  -  |
**404** | This account has no personal section |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_new_folder_items**
> FileEntryBaseArrayWrapper get_new_folder_items(folder_id)

Lists the entries of a folder that are new for the calling member - the files and folders created or changed
there since they last opened it - ordered from the most recently changed backwards. It is what the badge of a
room is filled from, and it is personal: two members of the same room get different answers. Reading this list
does not clear the marks, so the same entries come back until the folder itself is opened with
`GET api/2.0/files/{folderId}`, which does clear them. A folder with nothing new answers with an empty list,
and marks disappear on their own when the entry behind them is deleted or moved out of reach. The caller needs
read access to the folder and is otherwise answered with 403. The whole list arrives at once, without paging
or filtering, and the call is read-only.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **Union[int, str]**| The folder the operation acts on. Take the identifier from a listing such as `GET api/2.0/files/@root` or  `GET api/2.0/files/{folderId}`: a folder stored in the portal is numbered, while a folder in a connected  third-party account is named by an opaque string. | 

### Return type

[**FileEntryBaseArrayWrapper**](FileEntryBaseArrayWrapper.md)

### Third-party storage

The same method serves an entry in a connected third-party storage, whose identifier is a string such as `sbox-42`: pass `folder_id: str`.

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
    folder_id = 1 # int | The folder the operation acts on. Take the identifier from a listing such as `GET api/2.0/files/@root` or  `GET api/2.0/files/{folderId}`: a folder stored in the portal is numbered, while a folder in a connected  third-party account is named by an opaque string.

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
**200** | The entries of the folder that are new for the caller |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller may not read this folder |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recent_folder**
> FolderContentWrapper get_recent_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, exclude_subject=exclude_subject, apply_filter_option=apply_filter_option, search_area=search_area, extension=extension, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)

Returns the Recent section: the files the calling account has opened lately. The section holds files only,
so `folders` comes back empty, and it is personal, so another member's history is not visible here. A file is
added when it is opened and can also be added explicitly with `POST api/2.0/files/file/{fileId}/recent`;
`DELETE api/2.0/files/recent` clears the whole history, and `PUT api/2.0/files/displayrecent` switches the
section on and off for the account, which also decides whether `GET api/2.0/files/@root` includes it. Nothing
in the section is modified, though passing `sortBy` saves the requested order as the default order for this
account. The listing is ordered by the moment the caller last opened each file, newest first, and `sortBy` and
`sortOrder` do not change that order. `files` holds one page, `total` counts the files matching the request
before `count` and `startIndex` are applied, and `current` describes the section folder itself.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_group_id** | **UUID**| Restricts the listing to the files authored by this portal member, or by the members of this group; the same  parameter accepts either kind of identifier. Omit it to list the whole history. | [optional] 
 **filter_type** | [**FilterType**](.md)| Narrows the listing to a single kind of file, such as documents, spreadsheets or images. Omit it to list every  kind the history holds. | [optional] 
 **exclude_subject** | **bool**| Inverts `userIdOrGroupId`: with `true` the files of that member or group are the ones left out of the listing  instead of the only ones kept. | [optional] 
 **apply_filter_option** | [**ApplyFilterOption**](.md)| Chooses which half of a listing `filterType` and `filterValue` are applied to. The Recent section holds  files only, so the value does not change what comes back. | [optional] 
 **search_area** | [**SearchArea**](.md)| The area a listing is taken from. The Recent section is assembled from the caller's own open history rather  than from an area, so the value does not change which files are returned. | [optional] 
 **extension** | [**List[str]**](str.md)| The file extensions the listing is limited to, matched against the end of the file name. The leading dot is  optional, and the parameter is repeated once per extension. | [optional] 
 **count** | **int**| The size of one page of section content. Pair it with `startIndex` to walk the listing, and compare the two  with `total` in the response to see when the last page has been read. | [optional] 
 **start_index** | **int**| The number of matching entries to skip before the returned page begins; add `count` to it to ask for the next  page. | [optional] 
 **sort_by** | **str**| The name of the field the entries are ordered by, matched case-insensitively against the file sort fields:  `DateAndTime`, `AZ`, `Size`, `Author`, `Type`, `New`, `DateAndTimeCreation`, `RoomType`, `Tags`, `Room`,  `CustomOrder`, `LastOpened` and `UsedSpace`. A recognized value is also saved as the default order of the  account and reused by later listings that omit the parameter, while a value matching none of the fields leaves  that saved order in place. The Recent section keeps its own newest-first order, so the value does not  reorder this listing. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The direction in which the `sortBy` field is ordered. It is saved together with `sortBy` as the default order  of the account. The Recent section keeps its own newest-first order, so the value does not reorder this  listing. | [optional] 
 **filter_value** | **str**| The search string the history is filtered by: it is matched as a substring of file titles and against the  indexed document content as well. Omit it to list the whole history. | [optional] 

### Return type

[**FolderContentWrapper**](FolderContentWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.apply_filter_option import ApplyFilterOption
from docspace_api_sdk.models.filter_type import FilterType
from docspace_api_sdk.models.folder_content_wrapper import FolderContentWrapper
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
    user_id_or_group_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Restricts the listing to the files authored by this portal member, or by the members of this group; the same  parameter accepts either kind of identifier. Omit it to list the whole history. (optional)
    filter_type = docspace_api_sdk.FilterType() # FilterType | Narrows the listing to a single kind of file, such as documents, spreadsheets or images. Omit it to list every  kind the history holds. (optional)
    exclude_subject = false # bool | Inverts `userIdOrGroupId`: with `true` the files of that member or group are the ones left out of the listing  instead of the only ones kept. (optional)
    apply_filter_option = docspace_api_sdk.ApplyFilterOption() # ApplyFilterOption | Chooses which half of a listing `filterType` and `filterValue` are applied to. The Recent section holds  files only, so the value does not change what comes back. (optional)
    search_area = docspace_api_sdk.SearchArea() # SearchArea | The area a listing is taken from. The Recent section is assembled from the caller's own open history rather  than from an area, so the value does not change which files are returned. (optional)
    extension = ['.docx'] # List[str] | The file extensions the listing is limited to, matched against the end of the file name. The leading dot is  optional, and the parameter is repeated once per extension. (optional)
    count = 25 # int | The size of one page of section content. Pair it with `startIndex` to walk the listing, and compare the two  with `total` in the response to see when the last page has been read. (optional)
    start_index = 0 # int | The number of matching entries to skip before the returned page begins; add `count` to it to ask for the next  page. (optional)
    sort_by = 'DateAndTime' # str | The name of the field the entries are ordered by, matched case-insensitively against the file sort fields:  `DateAndTime`, `AZ`, `Size`, `Author`, `Type`, `New`, `DateAndTimeCreation`, `RoomType`, `Tags`, `Room`,  `CustomOrder`, `LastOpened` and `UsedSpace`. A recognized value is also saved as the default order of the  account and reused by later listings that omit the parameter, while a value matching none of the fields leaves  that saved order in place. The Recent section keeps its own newest-first order, so the value does not  reorder this listing. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The direction in which the `sortBy` field is ordered. It is saved together with `sortBy` as the default order  of the account. The Recent section keeps its own newest-first order, so the value does not reorder this  listing. (optional)
    filter_value = 'My Document' # str | The search string the history is filtered by: it is matched as a substring of file titles and against the  indexed document content as well. Omit it to list the whole history. (optional)

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
**200** | The Recent section with one page of the files the caller opened lately |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not allowed to read the Recent section |  -  |
**404** | The Recent section could not be resolved for this account |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_folder_history**
> DocumentBuilderTaskWrapper get_report_folder_history(folder_id)

Reports how far the history report of a folder has got, and is the operation to poll after
`POST api/2.0/files/folder/{folderId}/log/report` has queued one. `percentage` climbs to 100, `isCompleted`
turns true when the job is over however it ended, `error` carries the reason when it failed, and
`resultFileId`, `resultFileName` and `resultFileUrl` name the file that was saved in the caller's My
documents - a CSV report leaving the identifier empty. An empty answer means there is no report for this
folder and caller, either because none was started or because a finished one has already been picked up by an
earlier poll. The caller needs read access to the folder and may not be a guest, and the portal plan has to
include the audit feature; a caller who fails the access rule is answered with 403 and a folder that does not
exist with 404. The call is read-only, and each caller sees only their own report.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder whose history report is being polled. It is the folder that was              passed to the operation that started the report. | 

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
    folder_id = 56 # int | The folder whose history report is being polled. It is the folder that was              passed to the operation that started the report.

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
**200** | The state of the report task, or nothing when there is none |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller may not export the history of this folder |  -  |
**404** | The folder does not exist |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_root_folders**
> FolderContentArrayWrapper get_root_folders(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, without_trash=without_trash, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)

Returns every top-level section the calling account can see in one response, each of them a full section
object carrying its own first page of content: Favorites, Recent, Shared with me, My documents,
Trash, Rooms, Forms, Archive and, while AI access is enabled for the portal, AI agents. A section is
left out when the account has none of it, which is why a guest gets no personal section, and Recent is
listed only while it is switched on with `PUT api/2.0/files/displayrecent`. Pass `withoutTrash=true` to drop
the Trash section. The filters, `count` and `startIndex` are applied to each section separately, so
`count=1` returns one entry per section and every section reports its own `total`. Because it builds the
content of all of them, this is the most expensive listing in the module: when a single section is enough,
read it directly, for example with `GET api/2.0/files/@my`. The call modifies nothing in the sections and
leaves their new-item badges untouched, though passing `sortBy` saves the requested order as the default order
for this account.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_group_id** | **UUID**| Restricts the listing to the entries authored by this portal member, or by the members of this group; the same  parameter accepts either kind of identifier. Omit it to list everything the caller can read. | [optional] 
 **filter_type** | [**FilterType**](.md)| Narrows the content listed inside every returned section to a single kind of entry, such as documents, images  or one type of room. Omit it to list every kind the sections hold. | [optional] 
 **without_trash** | **bool**| Set it to `true` to leave the Trash section out of the returned set of sections; with `false`, or when the  parameter is omitted, the section is returned whenever the account has one of its own. | [optional] 
 **count** | **int**| The size of the content page returned for each section separately, so a value of 1 yields one entry per  section rather than one entry in total. | [optional] 
 **start_index** | **int**| The number of matching entries skipped in each section before its page begins; add `count` to it to ask for  the next page of every section. | [optional] 
 **sort_by** | **str**| The name of the field the entries are ordered by, matched case-insensitively against the file sort fields:  `DateAndTime`, `AZ`, `Size`, `Author`, `Type`, `New`, `DateAndTimeCreation`, `RoomType`, `Tags`, `Room`,  `CustomOrder`, `LastOpened` and `UsedSpace`. A recognized value is also saved as the default order of the  account and reused by later listings that omit the parameter, while a value matching none of the fields leaves  that saved order in place. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The direction in which the `sortBy` field is ordered. It is saved together with `sortBy` as the default order  of the account. | [optional] 
 **filter_value** | **str**| The search string the content of every section is filtered by: it is matched as a substring of entry titles  and, for files, against the indexed document content as well. Omit it to list the sections unfiltered. | [optional] 

### Return type

[**FolderContentArrayWrapper**](FolderContentArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.filter_type import FilterType
from docspace_api_sdk.models.folder_content_array_wrapper import FolderContentArrayWrapper
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
    user_id_or_group_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Restricts the listing to the entries authored by this portal member, or by the members of this group; the same  parameter accepts either kind of identifier. Omit it to list everything the caller can read. (optional)
    filter_type = docspace_api_sdk.FilterType() # FilterType | Narrows the content listed inside every returned section to a single kind of entry, such as documents, images  or one type of room. Omit it to list every kind the sections hold. (optional)
    without_trash = false # bool | Set it to `true` to leave the Trash section out of the returned set of sections; with `false`, or when the  parameter is omitted, the section is returned whenever the account has one of its own. (optional)
    count = 25 # int | The size of the content page returned for each section separately, so a value of 1 yields one entry per  section rather than one entry in total. (optional)
    start_index = 0 # int | The number of matching entries skipped in each section before its page begins; add `count` to it to ask for  the next page of every section. (optional)
    sort_by = 'DateAndTime' # str | The name of the field the entries are ordered by, matched case-insensitively against the file sort fields:  `DateAndTime`, `AZ`, `Size`, `Author`, `Type`, `New`, `DateAndTimeCreation`, `RoomType`, `Tags`, `Room`,  `CustomOrder`, `LastOpened` and `UsedSpace`. A recognized value is also saved as the default order of the  account and reused by later listings that omit the parameter, while a value matching none of the fields leaves  that saved order in place. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The direction in which the `sortBy` field is ordered. It is saved together with `sortBy` as the default order  of the account. (optional)
    filter_value = 'My Document' # str | The search string the content of every section is filtered by: it is matched as a substring of entry titles  and, for files, against the indexed document content as well. Omit it to list the sections unfiltered. (optional)

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
**200** | The sections available to the caller, each with one page of its content |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not allowed to read one of the sections |  -  |
**404** | One of the sections could not be resolved for this account |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trash_folder**
> FolderContentWrapper get_trash_folder(user_id_or_group_id=user_id_or_group_id, filter_type=filter_type, apply_filter_option=apply_filter_option, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)

Returns the caller's Trash section: the files and folders this account has deleted, kept there until they
are restored or discarded. Each member has a Trash of their own and sees only what they deleted themselves.
Restore an entry by moving it back with `PUT api/2.0/files/fileops/move`, or discard the whole section with
`PUT api/2.0/files/fileops/emptytrash`; both start a background operation that is polled through
`GET api/2.0/files/fileops`. This call itself modifies nothing, though passing `sortBy` saves the requested
order as the default order for this account. Only the top level of the section is listed, so the contents of a
deleted folder are not expanded into it, and `filterValue` is matched against titles alone here rather than
against document content. `folders` and `files` hold one page of the result, `total` counts everything that
matches before `count` and `startIndex` are applied, and `current` describes the section folder. An account
that is given no Trash of its own, an outsider for instance, receives 404.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_group_id** | **UUID**| Restricts the listing to the entries authored by this portal member, or by the members of this group; the same  parameter accepts either kind of identifier. Omit it to list everything the caller can read. | [optional] 
 **filter_type** | [**FilterType**](.md)| Narrows the listing to a single kind of entry, such as documents, images or one type of room. Omit it to list  every kind the section holds. | [optional] 
 **apply_filter_option** | [**ApplyFilterOption**](.md)| Chooses which half of the listing `filterType` and `filterValue` are applied to: with `Files` the folders come  back unfiltered, with `Folders` the files do, and with `All` both halves are filtered. | [optional] 
 **count** | **int**| The size of one page of section content. Pair it with `startIndex` to walk the listing, and compare the two  with `total` in the response to see when the last page has been read. | [optional] 
 **start_index** | **int**| The number of matching entries to skip before the returned page begins; add `count` to it to ask for the next  page. | [optional] 
 **sort_by** | **str**| The name of the field the entries are ordered by, matched case-insensitively against the file sort fields:  `DateAndTime`, `AZ`, `Size`, `Author`, `Type`, `New`, `DateAndTimeCreation`, `RoomType`, `Tags`, `Room`,  `CustomOrder`, `LastOpened` and `UsedSpace`. A recognized value is also saved as the default order of the  account and reused by later listings that omit the parameter, while a value matching none of the fields leaves  that saved order in place. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The direction in which the `sortBy` field is ordered. It is saved together with `sortBy` as the default order  of the account. | [optional] 
 **filter_value** | **str**| The search string the section is filtered by, matched as a substring of entry titles. Omit it to list the  section unfiltered. | [optional] 

### Return type

[**FolderContentWrapper**](FolderContentWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.apply_filter_option import ApplyFilterOption
from docspace_api_sdk.models.filter_type import FilterType
from docspace_api_sdk.models.folder_content_wrapper import FolderContentWrapper
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
    user_id_or_group_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Restricts the listing to the entries authored by this portal member, or by the members of this group; the same  parameter accepts either kind of identifier. Omit it to list everything the caller can read. (optional)
    filter_type = docspace_api_sdk.FilterType() # FilterType | Narrows the listing to a single kind of entry, such as documents, images or one type of room. Omit it to list  every kind the section holds. (optional)
    apply_filter_option = docspace_api_sdk.ApplyFilterOption() # ApplyFilterOption | Chooses which half of the listing `filterType` and `filterValue` are applied to: with `Files` the folders come  back unfiltered, with `Folders` the files do, and with `All` both halves are filtered. (optional)
    count = 25 # int | The size of one page of section content. Pair it with `startIndex` to walk the listing, and compare the two  with `total` in the response to see when the last page has been read. (optional)
    start_index = 0 # int | The number of matching entries to skip before the returned page begins; add `count` to it to ask for the next  page. (optional)
    sort_by = 'DateAndTime' # str | The name of the field the entries are ordered by, matched case-insensitively against the file sort fields:  `DateAndTime`, `AZ`, `Size`, `Author`, `Type`, `New`, `DateAndTimeCreation`, `RoomType`, `Tags`, `Room`,  `CustomOrder`, `LastOpened` and `UsedSpace`. A recognized value is also saved as the default order of the  account and reused by later listings that omit the parameter, while a value matching none of the fields leaves  that saved order in place. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The direction in which the `sortBy` field is ordered. It is saved together with `sortBy` as the default order  of the account. (optional)
    filter_value = 'My Document' # str | The search string the section is filtered by, matched as a substring of entry titles. Omit it to list the  section unfiltered. (optional)

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
**200** | The Trash section with one page of the entries the caller deleted |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not allowed to read the Trash section |  -  |
**404** | This account has no Trash section |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_file**
> FileWrapper insert_file(folder_id, insert_file_file=insert_file_file, insert_file_title=insert_file_title, insert_file_create_new_if_exist=insert_file_create_new_if_exist, insert_file_keep_convert_status=insert_file_keep_convert_status, insert_file_stream_can_read=insert_file_stream_can_read, insert_file_stream_can_write=insert_file_stream_can_write, insert_file_stream_can_seek=insert_file_stream_can_seek, insert_file_stream_can_timeout=insert_file_stream_can_timeout, insert_file_stream_length=insert_file_stream_length, insert_file_stream_position=insert_file_stream_position, insert_file_stream_read_timeout=insert_file_stream_read_timeout, insert_file_stream_write_timeout=insert_file_stream_write_timeout)

Stores a file in the folder named by the path in a single request, taking its name from `title` rather than
from the uploaded part, which is what separates it from `POST api/2.0/files/{folderId}/upload`. The content
may arrive either as a multipart part or as the raw request body. The name is stripped of characters a title
cannot hold and truncated, and `createNewIfExist` settles the clash: false adds a new version to the file that
already carries the name, true keeps both by giving the new one a numeric suffix. The caller needs the right
to add content to the folder, so a reader, an editor and a guest get 403, a section root and an archived room
are refused as well, and an unknown folder gives 404. Formats the portal converts are converted afterwards in
the background; pass `keepConvertStatus` to keep the outcome readable through
`GET api/2.0/files/file/{fileId}/checkconversion`. The answer is the stored file. A large payload belongs in a
chunked session instead.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **Union[int, str]**| The folder that receives the file; take the id from a listing such as `GET api/2.0/files/@root`. A room or an  ordinary folder inside one is accepted, a section root is not. | 
 **insert_file_file** | **bytes**| The content to store, sent as a `multipart/form-data` part. The same content may instead be sent as the raw  request body, which is what a client that cannot build a form does; when both are present the form part wins. | [optional] 
 **insert_file_title** | **str**| The name to store the file under, extension included. It wins over the name of the uploaded part, which is the  reason to choose this operation over the plain upload, and it is the only name available when the content  arrives as a raw body. Characters a title cannot hold are replaced with underscores and the name is cut to 170  characters before the file is stored. | [optional] 
 **insert_file_create_new_if_exist** | **bool**| Settles the clash with a file already carrying that title: left out, the content is written as the next  version of that file; set to true, both survive and the new one gets a numeric suffix in its title. | [optional] 
 **insert_file_keep_convert_status** | **bool**| Decides whether the outcome of the background conversion outlives the conversion itself. True keeps the queue  record, so `GET api/2.0/files/file/{fileId}/checkconversion` can still report the result or the error; left  out, the record is cleared the moment the conversion ends and that call finds nothing. | [optional] 
 **insert_file_stream_can_read** | **bool**|  | [optional] 
 **insert_file_stream_can_write** | **bool**|  | [optional] 
 **insert_file_stream_can_seek** | **bool**|  | [optional] 
 **insert_file_stream_can_timeout** | **bool**|  | [optional] 
 **insert_file_stream_length** | **int**|  | [optional] 
 **insert_file_stream_position** | **int**|  | [optional] 
 **insert_file_stream_read_timeout** | **int**|  | [optional] 
 **insert_file_stream_write_timeout** | **int**|  | [optional] 

### Return type

[**FileWrapper**](FileWrapper.md)

### Third-party storage

The same method serves an entry in a connected third-party storage, whose identifier is a string such as `sbox-42`: pass `folder_id: str` and the answer is [**ThirdPartyFileWrapper**](ThirdPartyFileWrapper.md).

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_wrapper import FileWrapper
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
    folder_id = 1 # int | The folder that receives the file; take the id from a listing such as `GET api/2.0/files/@root`. A room or an  ordinary folder inside one is accepted, a section root is not.
    insert_file_file = None # bytes | The content to store, sent as a `multipart/form-data` part. The same content may instead be sent as the raw  request body, which is what a client that cannot build a form does; when both are present the form part wins. (optional)
    insert_file_title = 'insert_file_title_example' # str | The name to store the file under, extension included. It wins over the name of the uploaded part, which is the  reason to choose this operation over the plain upload, and it is the only name available when the content  arrives as a raw body. Characters a title cannot hold are replaced with underscores and the name is cut to 170  characters before the file is stored. (optional)
    insert_file_create_new_if_exist = True # bool | Settles the clash with a file already carrying that title: left out, the content is written as the next  version of that file; set to true, both survive and the new one gets a numeric suffix in its title. (optional)
    insert_file_keep_convert_status = True # bool | Decides whether the outcome of the background conversion outlives the conversion itself. True keeps the queue  record, so `GET api/2.0/files/file/{fileId}/checkconversion` can still report the result or the error; left  out, the record is cleared the moment the conversion ends and that call finds nothing. (optional)
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
**200** | The stored file with its id and the title it was actually saved under; a `version` above 1 means the content was added to a file that already carried this name instead of creating a new one |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller cannot add content to this folder |  -  |
**404** | No folder with the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_file_to_my_from_body**
> FileWrapper insert_file_to_my_from_body(file=file, title=title, create_new_if_exist=create_new_if_exist, keep_convert_status=keep_convert_status, stream_can_read=stream_can_read, stream_can_write=stream_can_write, stream_can_seek=stream_can_seek, stream_can_timeout=stream_can_timeout, stream_length=stream_length, stream_position=stream_position, stream_read_timeout=stream_read_timeout, stream_write_timeout=stream_write_timeout)

Stores one file in the caller's own My documents section, the personal storage every portal member has, and
returns the stored file. The destination takes no identifier: it is resolved from the calling account and
created on first use, while a guest account has none and is answered as missing (404). Send the content as a
`multipart/form-data` part or as the raw request body, and name it with `title`, which wins over the name of
the uploaded part and has invalid characters replaced before storing. The call is not idempotent: by default a
file of the same title is overwritten as a new version, while `createNewIfExist=true` stores a separate copy
under a title made unique with a numeric suffix; a title held by a file that is locked or open in the editor
cannot be overwritten either, and a second file appears under the same title. Formats listed in
`extsMustConvert` of `GET api/2.0/files/settings` are converted after the response is sent;
`keepConvertStatus=true` keeps that result readable through `GET api/2.0/files/file/{fileId}/checkconversion`,
which otherwise drops it. Files over the single-request size limit or the account's storage quota are refused:
send those through `POST api/2.0/files/{folderId}/upload/create_session`, and use
`POST api/2.0/files/{folderId}/insert` for any other destination.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytes**| The content to store, sent as a `multipart/form-data` part. The same content may instead be sent as the raw  request body, which is what a client that cannot build a form does; when both are present the form part wins. | [optional] 
 **title** | **str**| The name to store the file under, extension included. It wins over the name of the uploaded part, which is the  reason to choose this operation over the plain upload, and it is the only name available when the content  arrives as a raw body. Characters a title cannot hold are replaced with underscores and the name is cut to 170  characters before the file is stored. | [optional] 
 **create_new_if_exist** | **bool**| Settles the clash with a file already carrying that title: left out, the content is written as the next  version of that file; set to true, both survive and the new one gets a numeric suffix in its title. | [optional] 
 **keep_convert_status** | **bool**| Decides whether the outcome of the background conversion outlives the conversion itself. True keeps the queue  record, so `GET api/2.0/files/file/{fileId}/checkconversion` can still report the result or the error; left  out, the record is cleared the moment the conversion ends and that call finds nothing. | [optional] 
 **stream_can_read** | **bool**|  | [optional] 
 **stream_can_write** | **bool**|  | [optional] 
 **stream_can_seek** | **bool**|  | [optional] 
 **stream_can_timeout** | **bool**|  | [optional] 
 **stream_length** | **int**|  | [optional] 
 **stream_position** | **int**|  | [optional] 
 **stream_read_timeout** | **int**|  | [optional] 
 **stream_write_timeout** | **int**|  | [optional] 

### Return type

[**FileWrapper**](FileWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_wrapper import FileWrapper
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
    file = None # bytes | The content to store, sent as a `multipart/form-data` part. The same content may instead be sent as the raw  request body, which is what a client that cannot build a form does; when both are present the form part wins. (optional)
    title = 'title_example' # str | The name to store the file under, extension included. It wins over the name of the uploaded part, which is the  reason to choose this operation over the plain upload, and it is the only name available when the content  arrives as a raw body. Characters a title cannot hold are replaced with underscores and the name is cut to 170  characters before the file is stored. (optional)
    create_new_if_exist = True # bool | Settles the clash with a file already carrying that title: left out, the content is written as the next  version of that file; set to true, both survive and the new one gets a numeric suffix in its title. (optional)
    keep_convert_status = True # bool | Decides whether the outcome of the background conversion outlives the conversion itself. True keeps the queue  record, so `GET api/2.0/files/file/{fileId}/checkconversion` can still report the result or the error; left  out, the record is cleared the moment the conversion ends and that call finds nothing. (optional)
    stream_can_read = True # bool |  (optional)
    stream_can_write = True # bool |  (optional)
    stream_can_seek = True # bool |  (optional)
    stream_can_timeout = True # bool |  (optional)
    stream_length = 56 # int |  (optional)
    stream_position = 56 # int |  (optional)
    stream_read_timeout = 56 # int |  (optional)
    stream_write_timeout = 56 # int |  (optional)

    try:
        # Insert a file into My documents
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
**200** | The stored file, with the identifier, version and title it was saved under |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | Creating a file in the personal section is not allowed for this account |  -  |
**404** | The caller has no personal section, so there is nothing to store the file in |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_folder**
> FolderWrapper rename_folder(folder_id, create_folder)

Gives a folder a new title and answers with the folder as it now stands. The title is trimmed, may not be
blank and is refused when it is longer than the limit the schema prints; a title that matches the current one
leaves the folder untouched, and titles need not be unique among the neighbours. The caller needs the right to
rename the folder, which the room manager, a content creator acting on a folder of their own and the owner of
a personal section have, while a guest is refused with 403 whatever their access; a folder in the Trash
section or in an archived room cannot be renamed either, and a folder that does not exist is answered as
not found. A room may be renamed here as well, in which case the caller needs the right to edit the
room, and `PUT api/2.0/files/rooms/{id}` is the operation that changes its other settings. The call is
mutating and idempotent; on a folder stored in a connected third-party account the identifier of the folder
may change with the title.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **Union[int, str]**| The folder the request is addressed to: when a folder is created it is the parent that receives the new  folder, and when a folder is renamed it is the folder that gets the new title. | 
 **create_folder** | [**CreateFolder**](CreateFolder.md)| The title carried by the request body. | 

### Return type

[**FolderWrapper**](FolderWrapper.md)

### Third-party storage

The same method serves an entry in a connected third-party storage, whose identifier is a string such as `sbox-42`: pass `folder_id: str` and the answer is [**ThirdPartyFolderWrapper**](ThirdPartyFolderWrapper.md).

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.create_folder import CreateFolder
from docspace_api_sdk.models.folder_wrapper import FolderWrapper
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
    folder_id = 1 # int | The folder the request is addressed to: when a folder is created it is the parent that receives the new  folder, and when a folder is renamed it is the folder that gets the new title.
    create_folder = docspace_api_sdk.CreateFolder() # CreateFolder | The title carried by the request body.

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
**200** | The folder with its new title |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller may not rename this folder |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_folder_order**
> FolderWrapper set_folder_order(folder_id, order_request_dto=order_request_dto)

Puts a folder at a given position among the entries of its parent and answers with the folder, its `order`
reporting where it now stands. Positions count from 1, and the entry that held the wanted position, together
with everything after it, is shifted to make room, so the numbering of the parent stays without gaps; a
position beyond the end places the folder last. The value may also be sent as a dotted path, as in 1.2.3, in
which case only its last segment is read. Ordering is what the manual arrangement of a room is built on, and
it only means something in rooms whose contents are indexed - elsewhere the value is stored and ignored. The
caller needs edit access to the folder, which room managers and content creators have, and a member without it
is refused, while a folder that does not exist is answered as not found. The call is mutating and idempotent.
To move several entries in one go use `PUT api/2.0/files/order`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **Union[int, str]**| The folder to move. | 
 **order_request_dto** | [**OrderRequestDto**](OrderRequestDto.md)| The position the folder is to take. | [optional] 

### Return type

[**FolderWrapper**](FolderWrapper.md)

### Third-party storage

The same method serves an entry in a connected third-party storage, whose identifier is a string such as `sbox-42`: pass `folder_id: str` and the answer is [**ThirdPartyFolderWrapper**](ThirdPartyFolderWrapper.md).

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.folder_wrapper import FolderWrapper
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
    folder_id = 1 # int | The folder to move.
    order_request_dto = docspace_api_sdk.OrderRequestDto() # OrderRequestDto | The position the folder is to take. (optional)

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
**200** | The folder with the position it now holds |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_folder_primary_external_link**
> FileShareWrapper set_folder_primary_external_link(id, folder_link_request)

Creates an external link to a folder or a room, or changes or revokes an existing one, and answers with the
link as it now stands. `linkId` decides which: an identifier that is not yet in use, the empty one included,
creates a link, while the identifier of an existing link rewrites it, so the whole set of parameters is
applied every time and a field left out is reset rather than kept. `access` carries the rights the link
grants, and `access` set to the value that denies everything revokes the link instead - the answer is then
empty, and a revoked primary link is not recreated by a later read. `title` names the link for the people who
manage it, `expirationDate` limits its lifetime and is ignored when it lies in the past, `password` asks
visitors for a secret, `denyDownload` leaves them with viewing only, `internal` admits signed-in members
alone, and `primary=true` makes it the primary link of the folder. The caller needs the right to manage the
links of the room, which its manager and a portal administrator acting as room manager have; anyone else is
refused and an unknown folder is answered as not found. The call is mutating.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Union[int, str]**| The folder or room the link belongs to. | 
 **folder_link_request** | [**FolderLinkRequest**](FolderLinkRequest.md)| The link and the way it is to be shaped. | 

### Return type

[**FileShareWrapper**](FileShareWrapper.md)

### Third-party storage

The same method serves an entry in a connected third-party storage, whose identifier is a string such as `sbox-42`: pass `id: str`.

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
    id = 1 # int | The folder or room the link belongs to.
    folder_link_request = docspace_api_sdk.FolderLinkRequest() # FolderLinkRequest | The link and the way it is to be shaped.

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
**200** | The link as it now stands, or nothing when it was revoked |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_report_folder_history**
> terminate_report_folder_history(folder_id)

Gives up the history report the caller has started for a folder with
`POST api/2.0/files/folder/{folderId}/log/report`. The request only asks the background worker to stop, and
the answer carries no body, so a following `GET api/2.0/files/folder/{folderId}/log/report` is what shows the
task ending as cancelled. Asking to terminate when nothing is running is accepted and changes nothing, which
makes the call safe to repeat. A report that has already finished is not undone by this call and its file
stays in My documents. The caller needs read access to the folder and may not be a guest, and the portal
plan has to include the audit feature; a caller who fails the access rule is answered with 403 and a folder
that does not exist with 404. Each caller can only terminate their own report.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder whose running history report is to be given up. It is the folder that              was passed to the operation that started the report. | 

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
    folder_id = 56 # int | The folder whose running history report is to be given up. It is the folder that              was passed to the operation that started the report.

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
**200** | The request to stop the report was accepted |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller may not export the history of this folder |  -  |
**404** | The folder does not exist |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> FileArrayWrapper upload_file(folder_id, create_new_if_exist=create_new_if_exist, store_original_file=store_original_file, keep_convert_status=keep_convert_status, file=file)

Stores a file in the folder named by the path in a single multipart request, taking its name from the uploaded
part; use `POST api/2.0/files/{folderId}/insert` when the name has to be given separately or the content is
sent as a raw body. The answer is a list that always holds exactly one file. `createNewIfExist` settles the
clash: false adds a new version to the file that already carries the name, true keeps both by giving the new
one a numeric suffix. `storeOriginalFile` reaches further than this call, because it saves the setting on the
calling account, the same one `PUT api/2.0/files/storeoriginal` writes, and it stays in force for later
uploads. The caller needs the right to add content to the folder, so a reader, an editor and a guest get 403,
a section root and an archived room are refused as well, and an unknown folder gives 404. A request without a
file is rejected as invalid, and a payload above the portal upload limit is refused.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **Union[int, str]**| The folder that receives the file; take the id from a listing such as `GET api/2.0/files/@root`. A room or an  ordinary folder inside one is accepted, a section root is not. | 
 **create_new_if_exist** | **bool**| Settles the clash with a file already carrying that title: left out, the content is written as the next  version of that file; set to true, both survive and the new one gets a numeric suffix in its title. | [optional] 
 **store_original_file** | **bool**| Reaches further than this request: it writes a setting on the calling account, the same one  `PUT api/2.0/files/storeoriginal` writes, and it stays in force for later uploads. True keeps both the  uploaded file and the copy the portal converts it into, false replaces the uploaded file with the converted  one, and leaving it out keeps whatever the account already has. | [optional] 
 **keep_convert_status** | **bool**| Decides whether the outcome of the background conversion outlives the conversion itself. True keeps the queue  record, so `GET api/2.0/files/file/{fileId}/checkconversion` can still report the result or the error; left  out, the record is cleared the moment the conversion ends and that call finds nothing. | [optional] 
 **file** | **bytes**| The content to store, sent as a `multipart/form-data` part; the name of that part becomes the title of the  stored file, with characters a title cannot hold replaced and the name cut to 170 characters. A request  without it is rejected as invalid. | [optional] 

### Return type

[**FileArrayWrapper**](FileArrayWrapper.md)

### Third-party storage

The same method serves an entry in a connected third-party storage, whose identifier is a string such as `sbox-42`: pass `folder_id: str` and the answer is [**ThirdPartyFileArrayWrapper**](ThirdPartyFileArrayWrapper.md).

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_array_wrapper import FileArrayWrapper
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
    folder_id = 1 # int | The folder that receives the file; take the id from a listing such as `GET api/2.0/files/@root`. A room or an  ordinary folder inside one is accepted, a section root is not.
    create_new_if_exist = true # bool | Settles the clash with a file already carrying that title: left out, the content is written as the next  version of that file; set to true, both survive and the new one gets a numeric suffix in its title. (optional)
    store_original_file = true # bool | Reaches further than this request: it writes a setting on the calling account, the same one  `PUT api/2.0/files/storeoriginal` writes, and it stays in force for later uploads. True keeps both the  uploaded file and the copy the portal converts it into, false replaces the uploaded file with the converted  one, and leaving it out keeps whatever the account already has. (optional)
    keep_convert_status = true # bool | Decides whether the outcome of the background conversion outlives the conversion itself. True keeps the queue  record, so `GET api/2.0/files/file/{fileId}/checkconversion` can still report the result or the error; left  out, the record is cleared the moment the conversion ends and that call finds nothing. (optional)
    file = None # bytes | The content to store, sent as a `multipart/form-data` part; the name of that part becomes the title of the  stored file, with characters a title cannot hold replaced and the name cut to 170 characters. A request  without it is rejected as invalid. (optional)

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
**200** | The stored file, as a list with one element |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller cannot add content to this folder |  -  |
**404** | No folder with the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file_to_my**
> FileArrayWrapper upload_file_to_my(create_new_if_exist=create_new_if_exist, store_original_file=store_original_file, keep_convert_status=keep_convert_status, file=file)

Uploads one file into the caller's own My documents section and returns it inside a single-element array; one
request stores exactly one file. The destination takes no identifier: it is resolved from the calling account
and created on first use, while a guest account has none and is answered as missing (404). The body has to be
`multipart/form-data` carrying the file part; a request without it is rejected as invalid, and the stored name
comes from that part, since unlike `POST api/2.0/files/@my/insert` there is no separate title. The call is not
idempotent: by default a file of the same title is overwritten as a new version, while `createNewIfExist=true`
stores a separate copy under a title made unique with a numeric suffix. `storeOriginalFile` is not a
per-request switch: it writes the same account setting as `PUT api/2.0/files/storeoriginal`, which decides
what happens to the formats listed in `extsMustConvert` of `GET api/2.0/files/settings` when they are
converted after the response - false replaces the uploaded file with the converted one, true keeps both;
`keepConvertStatus=true` keeps that conversion result readable through
`GET api/2.0/files/file/{fileId}/checkconversion`. Files over the single-request size limit or the account's
storage quota are refused; send those through `POST api/2.0/files/{folderId}/upload/create_session`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_new_if_exist** | **bool**| Settles the clash with a file already carrying that title: left out, the content is written as the next  version of that file; set to true, both survive and the new one gets a numeric suffix in its title. | [optional] 
 **store_original_file** | **bool**| Reaches further than this request: it writes a setting on the calling account, the same one  `PUT api/2.0/files/storeoriginal` writes, and it stays in force for later uploads. True keeps both the  uploaded file and the copy the portal converts it into, false replaces the uploaded file with the converted  one, and leaving it out keeps whatever the account already has. | [optional] 
 **keep_convert_status** | **bool**| Decides whether the outcome of the background conversion outlives the conversion itself. True keeps the queue  record, so `GET api/2.0/files/file/{fileId}/checkconversion` can still report the result or the error; left  out, the record is cleared the moment the conversion ends and that call finds nothing. | [optional] 
 **file** | **bytes**| The content to store, sent as a `multipart/form-data` part; the name of that part becomes the title of the  stored file, with characters a title cannot hold replaced and the name cut to 170 characters. A request  without it is rejected as invalid. | [optional] 

### Return type

[**FileArrayWrapper**](FileArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_array_wrapper import FileArrayWrapper
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
    create_new_if_exist = true # bool | Settles the clash with a file already carrying that title: left out, the content is written as the next  version of that file; set to true, both survive and the new one gets a numeric suffix in its title. (optional)
    store_original_file = true # bool | Reaches further than this request: it writes a setting on the calling account, the same one  `PUT api/2.0/files/storeoriginal` writes, and it stays in force for later uploads. True keeps both the  uploaded file and the copy the portal converts it into, false replaces the uploaded file with the converted  one, and leaving it out keeps whatever the account already has. (optional)
    keep_convert_status = true # bool | Decides whether the outcome of the background conversion outlives the conversion itself. True keeps the queue  record, so `GET api/2.0/files/file/{fileId}/checkconversion` can still report the result or the error; left  out, the record is cleared the moment the conversion ends and that call finds nothing. (optional)
    file = None # bytes | The content to store, sent as a `multipart/form-data` part; the name of that part becomes the title of the  stored file, with characters a title cannot hold replaced and the name cut to 170 characters. A request  without it is rejected as invalid. (optional)

    try:
        # Upload a file to My documents
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
**200** | An array holding the single uploaded file |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | Uploading a file to the personal section is not allowed for this account |  -  |
**404** | The caller has no personal section, so there is nothing to store the file in |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

