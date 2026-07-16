# docspace_api_sdk.FilesApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_file_to_recent**](#add_file_to_recent) | **POST** /api/2.0/files/file/{fileId}/recent | Add a file to the Recent section
[**add_templates**](#add_templates) | **POST** /api/2.0/files/templates | Add template files
[**change_version_history**](#change_version_history) | **PUT** /api/2.0/files/file/{fileId}/history | Change version history
[**check_fill_form_draft**](#check_fill_form_draft) | **POST** /api/2.0/files/masterform/{fileId}/checkfillformdraft | Check the form draft filling
[**copy_file_as**](#copy_file_as) | **POST** /api/2.0/files/file/{fileId}/copyas | Copy a file
[**create_edit_session**](#create_edit_session) | **POST** /api/2.0/files/file/{fileId}/edit_session | Create the editing session
[**create_file**](#create_file) | **POST** /api/2.0/files/{folderId}/file | Create a file
[**create_file_in_my_documents**](#create_file_in_my_documents) | **POST** /api/2.0/files/@my/file | Create a file in the My documents section
[**create_file_primary_external_link**](#create_file_primary_external_link) | **POST** /api/2.0/files/file/{id}/link | Create primary external link
[**create_html_file**](#create_html_file) | **POST** /api/2.0/files/{folderId}/html | Create an HTML file
[**create_html_file_in_my_documents**](#create_html_file_in_my_documents) | **POST** /api/2.0/files/@my/html | Create an HTML file in the My documents section
[**create_text_file**](#create_text_file) | **POST** /api/2.0/files/{folderId}/text | Create a text file
[**create_text_file_in_my_documents**](#create_text_file_in_my_documents) | **POST** /api/2.0/files/@my/text | Create a text file in the My documents section
[**create_thumbnails**](#create_thumbnails) | **POST** /api/2.0/files/thumbnails | Create file thumbnails
[**delete_file**](#delete_file) | **DELETE** /api/2.0/files/file/{fileId} | Delete a file
[**delete_recent**](#delete_recent) | **DELETE** /api/2.0/files/recent | Delete recent files
[**delete_templates**](#delete_templates) | **DELETE** /api/2.0/files/templates | Delete template files
[**generate_xlsx**](#generate_xlsx) | **POST** /api/2.0/files/file/{fileId}/xlsx | Generate XLSX report
[**get_all_form_roles**](#get_all_form_roles) | **GET** /api/2.0/files/file/{fileId}/formroles | Get form roles
[**get_edit_diff_url**](#get_edit_diff_url) | **GET** /api/2.0/files/file/{fileId}/edit/diff | Get changes URL
[**get_edit_history**](#get_edit_history) | **GET** /api/2.0/files/file/{fileId}/edit/history | Get version history
[**get_file_history**](#get_file_history) | **GET** /api/2.0/files/file/{fileId}/log | Get file history
[**get_file_info**](#get_file_info) | **GET** /api/2.0/files/file/{fileId} | Get file information
[**get_file_links**](#get_file_links) | **GET** /api/2.0/files/file/{id}/links | Get file external links
[**get_file_primary_external_link**](#get_file_primary_external_link) | **GET** /api/2.0/files/file/{id}/link | Get primary external link
[**get_file_version_info**](#get_file_version_info) | **GET** /api/2.0/files/file/{fileId}/history | Get file versions
[**get_fill_result**](#get_fill_result) | **GET** /api/2.0/files/file/fillresult | Get form-filling result
[**get_form_submissions**](#get_form_submissions) | **GET** /api/2.0/files/file/{fileId}/submissions | Get form submission results
[**get_presigned_file_uri**](#get_presigned_file_uri) | **GET** /api/2.0/files/file/{fileId}/presigned | Get file download link asynchronously
[**get_presigned_uri**](#get_presigned_uri) | **GET** /api/2.0/files/file/{fileId}/presigneduri | Get file download link
[**get_protected_file_users**](#get_protected_file_users) | **GET** /api/2.0/files/file/{fileId}/protectusers | Get users access rights to the protected file
[**get_reference_data**](#get_reference_data) | **POST** /api/2.0/files/file/referencedata | Get reference data
[**get_xlsx**](#get_xlsx) | **GET** /api/2.0/files/file/{fileId}/xlsx | Get XLSX report generation status
[**is_form_pdf**](#is_form_pdf) | **GET** /api/2.0/files/file/{fileId}/isformpdf | Check the PDF file
[**lock_file**](#lock_file) | **PUT** /api/2.0/files/file/{fileId}/lock | Lock a file
[**manage_form_filling**](#manage_form_filling) | **PUT** /api/2.0/files/file/{fileId}/manageformfilling | Perform form filling action
[**open_edit_file**](#open_edit_file) | **GET** /api/2.0/files/file/{fileId}/openedit | Open a file configuration
[**restore_file_version**](#restore_file_version) | **POST** /api/2.0/files/file/{fileId}/restoreversion | Restore a file version
[**save_editing_file_from_form**](#save_editing_file_from_form) | **PUT** /api/2.0/files/file/{fileId}/saveediting | Save file edits
[**save_file_as_pdf**](#save_file_as_pdf) | **POST** /api/2.0/files/file/{id}/saveaspdf | Save a file as PDF
[**save_form_role_mapping**](#save_form_role_mapping) | **POST** /api/2.0/files/file/{fileId}/formrolemapping | Save form role mapping
[**set_custom_filter_tag**](#set_custom_filter_tag) | **PUT** /api/2.0/files/file/{fileId}/customfilter | Set the Custom Filter editing mode
[**set_file_external_link**](#set_file_external_link) | **PUT** /api/2.0/files/file/{id}/links | Set an external link
[**set_file_order**](#set_file_order) | **PUT** /api/2.0/files/{fileId}/order | Set file order
[**set_files_order**](#set_files_order) | **PUT** /api/2.0/files/order | Set order of files
[**start_edit_file**](#start_edit_file) | **POST** /api/2.0/files/file/{fileId}/startedit | Start file editing
[**start_filling_file**](#start_filling_file) | **PUT** /api/2.0/files/file/{fileId}/startfilling | Start file filling
[**toggle_file_favorite**](#toggle_file_favorite) | **GET** /api/2.0/files/favorites/{fileId} | Change the file favorite status
[**track_edit_file**](#track_edit_file) | **GET** /api/2.0/files/file/{fileId}/trackeditfile | Track file editing
[**update_file**](#update_file) | **PUT** /api/2.0/files/file/{fileId} | Update a file


# **add_file_to_recent**
> FileIntegerWrapper add_file_to_recent(file_id)

Adds a file with the ID specified in the request to the Recent section.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file unique identifier. | 

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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file unique identifier.

    try:
        # Add a file to the Recent section
        api_response = api_instance.add_file_to_recent(file_id)
        print("The response of FilesApi->add_file_to_recent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->add_file_to_recent: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New file information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | File not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_templates**
> BooleanWrapper add_templates(templates_request_dto=templates_request_dto)

Adds files with the IDs specified in the request to the template list.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templates_request_dto** | [**TemplatesRequestDto**](TemplatesRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.models.templates_request_dto import TemplatesRequestDto
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    templates_request_dto = docspace_api_sdk.TemplatesRequestDto() # TemplatesRequestDto |  (optional)

    try:
        # Add template files
        api_response = api_instance.add_templates(templates_request_dto=templates_request_dto)
        print("The response of FilesApi->add_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->add_templates: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_version_history**
> FileIntegerArrayWrapper change_version_history(file_id, change_history)

Changes the version history of a file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file Id to change its version history. | 
 **change_history** | [**ChangeHistory**](ChangeHistory.md)| The parameters for changing version history. | 

### Return type

[**FileIntegerArrayWrapper**](FileIntegerArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.change_history import ChangeHistory
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file Id to change its version history.
    change_history = docspace_api_sdk.ChangeHistory() # ChangeHistory | The parameters for changing version history.

    try:
        # Change version history
        api_response = api_instance.change_version_history(file_id, change_history)
        print("The response of FilesApi->change_version_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->change_version_history: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated information about file versions |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You do not have enough permissions to edit the file |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_fill_form_draft**
> StringWrapper check_fill_form_draft(file_id, check_fill_form_draft)

Checks if the current file is a form draft which can be filled out.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID of the form draft. | 
 **check_fill_form_draft** | [**CheckFillFormDraft**](CheckFillFormDraft.md)| The parameters for checking the form draft filling. | 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.check_fill_form_draft import CheckFillFormDraft
from docspace_api_sdk.models.string_wrapper import StringWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file ID of the form draft.
    check_fill_form_draft = docspace_api_sdk.CheckFillFormDraft() # CheckFillFormDraft | The parameters for checking the form draft filling.

    try:
        # Check the form draft filling
        api_response = api_instance.check_fill_form_draft(file_id, check_fill_form_draft)
        print("The response of FilesApi->check_fill_form_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->check_fill_form_draft: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Link to the form |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You don't have enough permission to view the file |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_file_as**
> FileEntryBaseWrapper copy_file_as(file_id, copy_as_json_element)

Copies (and converts if possible) an existing file to the specified folder.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID to copy. | 
 **copy_as_json_element** | [**CopyAsJsonElement**](CopyAsJsonElement.md)| The parameters for copying a file. | 

### Return type

[**FileEntryBaseWrapper**](FileEntryBaseWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.copy_as_json_element import CopyAsJsonElement
from docspace_api_sdk.models.file_entry_base_wrapper import FileEntryBaseWrapper
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file ID to copy.
    copy_as_json_element = docspace_api_sdk.CopyAsJsonElement() # CopyAsJsonElement | The parameters for copying a file.

    try:
        # Copy a file
        api_response = api_instance.copy_file_as(file_id, copy_as_json_element)
        print("The response of FilesApi->copy_file_as:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->copy_file_as: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Copied file entry information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**400** | No file id or folder id toFolderId determine provider |  -  |
**403** | You don't have enough permission to create |  -  |
**404** | File not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_edit_session**
> ChunkedUploadSessionResponseWrapperIntegerWrapper create_edit_session(file_id, file_size=file_size)

Creates a session to edit the existing file with multiple chunks (needed for WebDAV).

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID. | 
 **file_size** | **int**| The file size in bytes. | [optional] 

### Return type

[**ChunkedUploadSessionResponseWrapperIntegerWrapper**](ChunkedUploadSessionResponseWrapperIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.chunked_upload_session_response_wrapper_integer_wrapper import ChunkedUploadSessionResponseWrapperIntegerWrapper
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file ID.
    file_size = 1024 # int | The file size in bytes. (optional)

    try:
        # Create the editing session
        api_response = api_instance.create_edit_session(file_id, file_size=file_size)
        print("The response of FilesApi->create_edit_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->create_edit_session: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about created session |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You don't have enough permission to edit the file |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file**
> FileIntegerWrapper create_file(folder_id, create_file_json_element)

Creates a new file in the specified folder with the title specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID for the file creation. | 
 **create_file_json_element** | [**CreateFileJsonElement**](CreateFileJsonElement.md)| The parameters for creating a file. | 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.create_file_json_element import CreateFileJsonElement
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    folder_id = 1 # int | The folder ID for the file creation.
    create_file_json_element = docspace_api_sdk.CreateFileJsonElement() # CreateFileJsonElement | The parameters for creating a file.

    try:
        # Create a file
        api_response = api_instance.create_file(folder_id, create_file_json_element)
        print("The response of FilesApi->create_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->create_file: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New file information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file_in_my_documents**
> FileIntegerWrapper create_file_in_my_documents(create_file_json_element=create_file_json_element)

Creates a new file in the My documents section with the title specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_file_json_element** | [**CreateFileJsonElement**](CreateFileJsonElement.md)|  | [optional] 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.create_file_json_element import CreateFileJsonElement
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    create_file_json_element = docspace_api_sdk.CreateFileJsonElement() # CreateFileJsonElement |  (optional)

    try:
        # Create a file in the My documents section
        api_response = api_instance.create_file_in_my_documents(create_file_json_element=create_file_json_element)
        print("The response of FilesApi->create_file_in_my_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->create_file_in_my_documents: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New file information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file_primary_external_link**
> FileShareWrapper create_file_primary_external_link(id, file_link_request)

Creates a primary external link by the identifier specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The file ID. | 
 **file_link_request** | [**FileLinkRequest**](FileLinkRequest.md)| The file external link parameters. | 

### Return type

[**FileShareWrapper**](FileShareWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_link_request import FileLinkRequest
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

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    id = 1 # int | The file ID.
    file_link_request = docspace_api_sdk.FileLinkRequest() # FileLinkRequest | The file external link parameters.

    try:
        # Create primary external link
        api_response = api_instance.create_file_primary_external_link(id, file_link_request)
        print("The response of FilesApi->create_file_primary_external_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->create_file_primary_external_link: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File security information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_html_file**
> FileIntegerWrapper create_html_file(folder_id, create_text_or_html_file)

Creates an HTML (.html) file in the selected folder with the title and contents specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID to create the text or HTML file. | 
 **create_text_or_html_file** | [**CreateTextOrHtmlFile**](CreateTextOrHtmlFile.md)| The parameters for creating an HTML or text file. | 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.create_text_or_html_file import CreateTextOrHtmlFile
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    folder_id = 1 # int | The folder ID to create the text or HTML file.
    create_text_or_html_file = docspace_api_sdk.CreateTextOrHtmlFile() # CreateTextOrHtmlFile | The parameters for creating an HTML or text file.

    try:
        # Create an HTML file
        api_response = api_instance.create_html_file(folder_id, create_text_or_html_file)
        print("The response of FilesApi->create_html_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->create_html_file: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New file information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You don't have enough permission to create |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_html_file_in_my_documents**
> FileIntegerWrapper create_html_file_in_my_documents(create_text_or_html_file=create_text_or_html_file)

Creates an HTML (.html) file in the My documents section with the title and contents specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_text_or_html_file** | [**CreateTextOrHtmlFile**](CreateTextOrHtmlFile.md)|  | [optional] 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.create_text_or_html_file import CreateTextOrHtmlFile
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    create_text_or_html_file = docspace_api_sdk.CreateTextOrHtmlFile() # CreateTextOrHtmlFile |  (optional)

    try:
        # Create an HTML file in the My documents section
        api_response = api_instance.create_html_file_in_my_documents(create_text_or_html_file=create_text_or_html_file)
        print("The response of FilesApi->create_html_file_in_my_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->create_html_file_in_my_documents: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New file information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You don't have enough permission to create |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_text_file**
> FileIntegerWrapper create_text_file(folder_id, create_text_or_html_file)

Creates a text (.txt) file in the selected folder with the title and contents specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID to create the text or HTML file. | 
 **create_text_or_html_file** | [**CreateTextOrHtmlFile**](CreateTextOrHtmlFile.md)| The parameters for creating an HTML or text file. | 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.create_text_or_html_file import CreateTextOrHtmlFile
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    folder_id = 1 # int | The folder ID to create the text or HTML file.
    create_text_or_html_file = docspace_api_sdk.CreateTextOrHtmlFile() # CreateTextOrHtmlFile | The parameters for creating an HTML or text file.

    try:
        # Create a text file
        api_response = api_instance.create_text_file(folder_id, create_text_or_html_file)
        print("The response of FilesApi->create_text_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->create_text_file: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New file information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_text_file_in_my_documents**
> FileIntegerWrapper create_text_file_in_my_documents(create_text_or_html_file=create_text_or_html_file)

Creates a text (.txt) file in the My documents section with the title and contents specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_text_or_html_file** | [**CreateTextOrHtmlFile**](CreateTextOrHtmlFile.md)|  | [optional] 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.create_text_or_html_file import CreateTextOrHtmlFile
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    create_text_or_html_file = docspace_api_sdk.CreateTextOrHtmlFile() # CreateTextOrHtmlFile |  (optional)

    try:
        # Create a text file in the My documents section
        api_response = api_instance.create_text_file_in_my_documents(create_text_or_html_file=create_text_or_html_file)
        print("The response of FilesApi->create_text_file_in_my_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->create_text_file_in_my_documents: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New file information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_thumbnails**
> ObjectArrayWrapper create_thumbnails(base_batch_request_dto=base_batch_request_dto)

Creates thumbnails for the files with the IDs specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_batch_request_dto** | [**BaseBatchRequestDto**](BaseBatchRequestDto.md)|  | [optional] 

### Return type

[**ObjectArrayWrapper**](ObjectArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.base_batch_request_dto import BaseBatchRequestDto
from docspace_api_sdk.models.object_array_wrapper import ObjectArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    base_batch_request_dto = docspace_api_sdk.BaseBatchRequestDto() # BaseBatchRequestDto |  (optional)

    try:
        # Create file thumbnails
        api_response = api_instance.create_thumbnails(base_batch_request_dto=base_batch_request_dto)
        print("The response of FilesApi->create_thumbnails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->create_thumbnails: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file IDs |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> FileOperationArrayWrapper delete_file(file_id, delete, return_single_operation=return_single_operation)

Deletes a file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID to delete. | 
 **delete** | [**Delete**](Delete.md)| The parameters for deleting a file. | 
 **return_single_operation** | **bool**| Specifies whether to return only the current operation | [optional] 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.delete import Delete
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file ID to delete.
    delete = docspace_api_sdk.Delete() # Delete | The parameters for deleting a file.
    return_single_operation = false # bool | Specifies whether to return only the current operation (optional)

    try:
        # Delete a file
        api_response = api_instance.delete_file(file_id, delete, return_single_operation=return_single_operation)
        print("The response of FilesApi->delete_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->delete_file: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file operations |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recent**
> NoContentResultWrapper delete_recent(base_batch_request_dto=base_batch_request_dto)

Removes files with the IDs specified in the request from the Recent section.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_batch_request_dto** | [**BaseBatchRequestDto**](BaseBatchRequestDto.md)|  | [optional] 

### Return type

[**NoContentResultWrapper**](NoContentResultWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.base_batch_request_dto import BaseBatchRequestDto
from docspace_api_sdk.models.no_content_result_wrapper import NoContentResultWrapper
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    base_batch_request_dto = docspace_api_sdk.BaseBatchRequestDto() # BaseBatchRequestDto |  (optional)

    try:
        # Delete recent files
        api_response = api_instance.delete_recent(base_batch_request_dto=base_batch_request_dto)
        print("The response of FilesApi->delete_recent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->delete_recent: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No content |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_templates**
> BooleanWrapper delete_templates(request_body=request_body)

Removes files with the IDs specified in the request from the template list.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[int]**](int.md)| The file IDs. | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    request_body = [56] # List[int] | The file IDs. (optional)

    try:
        # Delete template files
        api_response = api_instance.delete_templates(request_body=request_body)
        print("The response of FilesApi->delete_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->delete_templates: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_xlsx**
> XlsxReportResponseWrapper generate_xlsx(file_id)

Triggers asynchronous XLSX report generation for the specified form file.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file unique identifier. | 

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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file unique identifier.

    try:
        # Generate XLSX report
        api_response = api_instance.generate_xlsx(file_id)
        print("The response of FilesApi->generate_xlsx:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->generate_xlsx: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You do not have enough permissions to perform this action |  -  |
**404** | The required file was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_form_roles**
> FormRoleArrayWrapper get_all_form_roles(file_id)

Returns all roles for the specified form.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file unique identifier. | 

### Return type

[**FormRoleArrayWrapper**](FormRoleArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.form_role_array_wrapper import FormRoleArrayWrapper
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file unique identifier.

    try:
        # Get form roles
        api_response = api_instance.get_all_form_roles(file_id)
        print("The response of FilesApi->get_all_form_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_all_form_roles: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved all roles for the form |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You do not have enough permissions to view the form roles |  -  |
**404** | The required file was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edit_diff_url**
> EditHistoryDataWrapper get_edit_diff_url(file_id, version=version)

Returns a URL to the changes of a file version specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID. | 
 **version** | **int**| The file version. | [optional] 

### Return type

[**EditHistoryDataWrapper**](EditHistoryDataWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.edit_history_data_wrapper import EditHistoryDataWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file ID.
    version = 1 # int | The file version. (optional)

    try:
        # Get changes URL
        api_response = api_instance.get_edit_diff_url(file_id, version=version)
        print("The response of FilesApi->get_edit_diff_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_edit_diff_url: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File version history data |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edit_history**
> EditHistoryArrayWrapper get_edit_history(file_id)

Returns the version history of a file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file unique identifier. | 

### Return type

[**EditHistoryArrayWrapper**](EditHistoryArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.edit_history_array_wrapper import EditHistoryArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file unique identifier.

    try:
        # Get version history
        api_response = api_instance.get_edit_history(file_id)
        print("The response of FilesApi->get_edit_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_edit_history: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Version history data |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_history**
> HistoryArrayWrapper get_file_history(file_id, from_date=from_date, to_date=to_date, count=count, start_index=start_index)

Returns the list of actions performed on the file with the specified identifier.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID of the history request. | 
 **from_date** | [**ApiDateTime**](.md)| The start date of the history. | [optional] 
 **to_date** | [**ApiDateTime**](.md)| The end date of the history. | [optional] 
 **count** | **int**| The number of history entries to retrieve for the file log. | [optional] 
 **start_index** | **int**| The starting index for retrieving a subset of file history entries. | [optional] 

### Return type

[**HistoryArrayWrapper**](HistoryArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file ID of the history request.
    from_date = docspace_api_sdk.ApiDateTime() # ApiDateTime | The start date of the history. (optional)
    to_date = docspace_api_sdk.ApiDateTime() # ApiDateTime | The end date of the history. (optional)
    count = 25 # int | The number of history entries to retrieve for the file log. (optional)
    start_index = 0 # int | The starting index for retrieving a subset of file history entries. (optional)

    try:
        # Get file history
        api_response = api_instance.get_file_history(file_id, from_date=from_date, to_date=to_date, count=count, start_index=start_index)
        print("The response of FilesApi->get_file_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_file_history: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of actions performed on the file |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | The required file was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_info**
> FileIntegerWrapper get_file_info(file_id, version=version)

Returns the detailed information about a file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID. | 
 **version** | **int**| The file version. | [optional] 

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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file ID.
    version = 1 # int | The file version. (optional)

    try:
        # Get file information
        api_response = api_instance.get_file_info(file_id, version=version)
        print("The response of FilesApi->get_file_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_file_info: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_links**
> FileShareArrayWrapper get_file_links(id, count=count, start_index=start_index)

Returns the external links of a file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The file unique identifier. | 
 **count** | **int**| The number of items to retrieve in the request. | [optional] 
 **start_index** | **int**| The starting index for the query results. | [optional] 

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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    id = 10 # int | The file unique identifier.
    count = 25 # int | The number of items to retrieve in the request. (optional)
    start_index = 0 # int | The starting index for the query results. (optional)

    try:
        # Get file external links
        api_response = api_instance.get_file_links(id, count=count, start_index=start_index)
        print("The response of FilesApi->get_file_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_file_links: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File security information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_primary_external_link**
> FileShareWrapper get_file_primary_external_link(id, count=count, start_index=start_index)

Returns the primary external link by the identifier specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The file unique identifier. | 
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    id = 10 # int | The file unique identifier.
    count = 25 # int | The number of items to retrieve in the request. (optional)
    start_index = 0 # int | The starting index for the query results. (optional)

    try:
        # Get primary external link
        api_response = api_instance.get_file_primary_external_link(id, count=count, start_index=start_index)
        print("The response of FilesApi->get_file_primary_external_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_file_primary_external_link: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File security information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_version_info**
> FileIntegerArrayWrapper get_file_version_info(file_id)

Returns the detailed information about all the available file versions with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file unique identifier. | 

### Return type

[**FileIntegerArrayWrapper**](FileIntegerArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_integer_array_wrapper import FileIntegerArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file unique identifier.

    try:
        # Get file versions
        api_response = api_instance.get_file_version_info(file_id)
        print("The response of FilesApi->get_file_version_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_file_version_info: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about file versions: folder ID, version, version group, content length, pure content length, file status, URL to view a file, web URL, file type, file extension, comment, encrypted or not, thumbnail URL, thumbnail status, locked or not, user ID who locked a file, denies file downloading or not, denies file sharing or not, file accessibility |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fill_result**
> FillingFormResultIntegerWrapper get_fill_result(filling_session_id=filling_session_id)

Retrieves the result of a form-filling session.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filling_session_id** | **str**| The form-filling session ID. | [optional] 

### Return type

[**FillingFormResultIntegerWrapper**](FillingFormResultIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.filling_form_result_integer_wrapper import FillingFormResultIntegerWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    filling_session_id = 'doc_key_123' # str | The form-filling session ID. (optional)

    try:
        # Get form-filling result
        api_response = api_instance.get_fill_result(filling_session_id=filling_session_id)
        print("The response of FilesApi->get_fill_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_fill_result: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_form_submissions**
> FormSubmissionsWrapper get_form_submissions(file_id)

Returns the results of form submissions.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file unique identifier. | 

### Return type

[**FormSubmissionsWrapper**](FormSubmissionsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.form_submissions_wrapper import FormSubmissionsWrapper
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file unique identifier.

    try:
        # Get form submission results
        api_response = api_instance.get_form_submissions(file_id)
        print("The response of FilesApi->get_form_submissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_form_submissions: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Form submission results were successfully retrieved |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You do not have enough permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_presigned_file_uri**
> FileLinkWrapper get_presigned_file_uri(file_id)

Returns a link to download a file with the ID specified in the request asynchronously.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file unique identifier. | 

### Return type

[**FileLinkWrapper**](FileLinkWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_link_wrapper import FileLinkWrapper
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file unique identifier.

    try:
        # Get file download link asynchronously
        api_response = api_instance.get_presigned_file_uri(file_id)
        print("The response of FilesApi->get_presigned_file_uri:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_presigned_file_uri: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File download link |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_presigned_uri**
> StringWrapper get_presigned_uri(file_id)

Returns a pre-signed URL to download a file with the specified ID.
This temporary link provides secure access to the file.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file unique identifier. | 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.string_wrapper import StringWrapper
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file unique identifier.

    try:
        # Get file download link
        api_response = api_instance.get_presigned_uri(file_id)
        print("The response of FilesApi->get_presigned_uri:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_presigned_uri: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File download link |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_protected_file_users**
> MentionWrapperArrayWrapper get_protected_file_users(file_id)

Returns a list of users with their access rights to the protected file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file unique identifier. | 

### Return type

[**MentionWrapperArrayWrapper**](MentionWrapperArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.mention_wrapper_array_wrapper import MentionWrapperArrayWrapper
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file unique identifier.

    try:
        # Get users access rights to the protected file
        api_response = api_instance.get_protected_file_users(file_id)
        print("The response of FilesApi->get_protected_file_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_protected_file_users: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users with their access rights to the protected file |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_data**
> FileReferenceWrapper get_reference_data(get_reference_data_dto_integer=get_reference_data_dto_integer)

Returns the reference data to uniquely identify a file in its system and check the availability of insering data into the destination spreadsheet by the external link.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_reference_data_dto_integer** | [**GetReferenceDataDtoInteger**](GetReferenceDataDtoInteger.md)|  | [optional] 

### Return type

[**FileReferenceWrapper**](FileReferenceWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_reference_wrapper import FileReferenceWrapper
from docspace_api_sdk.models.get_reference_data_dto_integer import GetReferenceDataDtoInteger
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    get_reference_data_dto_integer = docspace_api_sdk.GetReferenceDataDtoInteger() # GetReferenceDataDtoInteger |  (optional)

    try:
        # Get reference data
        api_response = api_instance.get_reference_data(get_reference_data_dto_integer=get_reference_data_dto_integer)
        print("The response of FilesApi->get_reference_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_reference_data: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File reference data |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xlsx**
> DocumentBuilderTaskWrapper get_xlsx(file_id)

Returns the status of the XLSX report generation task for the specified form.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file unique identifier. | 

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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file unique identifier.

    try:
        # Get XLSX report generation status
        api_response = api_instance.get_xlsx(file_id)
        print("The response of FilesApi->get_xlsx:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_xlsx: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_form_pdf**
> BooleanWrapper is_form_pdf(file_id)

Checks if the PDF file is a form or not.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file unique identifier. | 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file unique identifier.

    try:
        # Check the PDF file
        api_response = api_instance.is_form_pdf(file_id)
        print("The response of FilesApi->is_form_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->is_form_pdf: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true - the PDF file is form, false - the PDF file is not a form |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lock_file**
> FileIntegerWrapper lock_file(file_id, lock_file_parameters)

Locks a file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID for locking. | 
 **lock_file_parameters** | [**LockFileParameters**](LockFileParameters.md)| The parameters for locking a file. | 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_integer_wrapper import FileIntegerWrapper
from docspace_api_sdk.models.lock_file_parameters import LockFileParameters
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file ID for locking.
    lock_file_parameters = docspace_api_sdk.LockFileParameters() # LockFileParameters | The parameters for locking a file.

    try:
        # Lock a file
        api_response = api_instance.lock_file(file_id, lock_file_parameters)
        print("The response of FilesApi->lock_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->lock_file: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Locked file information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_form_filling**
> manage_form_filling(file_id, manage_form_filling_dto_integer=manage_form_filling_dto_integer)

Performs the specified form filling action.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  | 
 **manage_form_filling_dto_integer** | [**ManageFormFillingDtoInteger**](ManageFormFillingDtoInteger.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.manage_form_filling_dto_integer import ManageFormFillingDtoInteger
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 'file_id_example' # str | 
    manage_form_filling_dto_integer = docspace_api_sdk.ManageFormFillingDtoInteger() # ManageFormFillingDtoInteger |  (optional)

    try:
        # Perform form filling action
        api_instance.manage_form_filling(file_id, manage_form_filling_dto_integer=manage_form_filling_dto_integer)
    except Exception as e:
        print("Exception when calling FilesApi->manage_form_filling: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully processed the form filling action |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You do not have enough permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_edit_file**
> ConfigurationIntegerWrapper open_edit_file(file_id, version=version, view=view, editor_type=editor_type, edit=edit, fill=fill)

Returns the initialization configuration of a file to open it in the editor.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID to open. | 
 **version** | **int**| The file version to open. | [optional] 
 **view** | **bool**| Specifies if the document will be opened for viewing only or not. | [optional] 
 **editor_type** | [**EditorType**](.md)| The editor type to open the file. | [optional] 
 **edit** | **bool**| Specifies if the document is opened in the editing mode or not. | [optional] 
 **fill** | **bool**| Specifies if the document is opened in the form-filling mode or not. | [optional] 

### Return type

[**ConfigurationIntegerWrapper**](ConfigurationIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.configuration_integer_wrapper import ConfigurationIntegerWrapper
from docspace_api_sdk.models.editor_type import EditorType
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file ID to open.
    version = 1 # int | The file version to open. (optional)
    view = false # bool | Specifies if the document will be opened for viewing only or not. (optional)
    editor_type = docspace_api_sdk.EditorType() # EditorType | The editor type to open the file. (optional)
    edit = false # bool | Specifies if the document is opened in the editing mode or not. (optional)
    fill = false # bool | Specifies if the document is opened in the form-filling mode or not. (optional)

    try:
        # Open a file configuration
        api_response = api_instance.open_edit_file(file_id, version=version, view=view, editor_type=editor_type, edit=edit, fill=fill)
        print("The response of FilesApi->open_edit_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->open_edit_file: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configuration parameters |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You don't have enough permission to view the file |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_file_version**
> EditHistoryArrayWrapper restore_file_version(file_id, version=version, url=url)

Restores a file version specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID of the restore version. | 
 **version** | **int**| The file version of the restore. | [optional] 
 **url** | **str**| The file version URL of the restore. | [optional] 

### Return type

[**EditHistoryArrayWrapper**](EditHistoryArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.edit_history_array_wrapper import EditHistoryArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file ID of the restore version.
    version = 1 # int | The file version of the restore. (optional)
    url = 'https://example.com' # str | The file version URL of the restore. (optional)

    try:
        # Restore a file version
        api_response = api_instance.restore_file_version(file_id, version=version, url=url)
        print("The response of FilesApi->restore_file_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->restore_file_version: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Version history data: file ID, key, file version, version group, a user who updated a file, creation time, history changes in the string format, list of history changes, server version |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**400** | No file id or folder id toFolderId determine provider |  -  |
**403** | You do not have enough permissions to edit the file |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_editing_file_from_form**
> FileIntegerWrapper save_editing_file_from_form(file_id, download_uri=download_uri, file_extension=file_extension, file=file, forcesave=forcesave)

Saves edits to a file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The editing file ID from the request. | 
 **download_uri** | **str**| The URI to download the editing file. | [optional] 
 **file_extension** | **str**| The editing file extension from the request. | [optional] 
 **file** | **bytes**| The edited file to be saved, uploaded as part of the multipart/form-data request.  This property represents the modified file content from the HTTP request form after editing operations.  The file is accessed via the IFormFile interface which provides access to the file name, content type, length, and stream. | [optional] 
 **forcesave** | **bool**| Specifies whether to force save the file or not. | [optional] 

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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The editing file ID from the request.
    download_uri = 'https://example.com/file.txt' # str | The URI to download the editing file. (optional)
    file_extension = 'file_extension_example' # str | The editing file extension from the request. (optional)
    file = None # bytes | The edited file to be saved, uploaded as part of the multipart/form-data request.  This property represents the modified file content from the HTTP request form after editing operations.  The file is accessed via the IFormFile interface which provides access to the file name, content type, length, and stream. (optional)
    forcesave = True # bool | Specifies whether to force save the file or not. (optional)

    try:
        # Save file edits
        api_response = api_instance.save_editing_file_from_form(file_id, download_uri=download_uri, file_extension=file_extension, file=file, forcesave=forcesave)
        print("The response of FilesApi->save_editing_file_from_form:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->save_editing_file_from_form: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Saved file parameters |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**400** | No file id or folder id toFolderId determine provider |  -  |
**403** | You do not have enough permissions to edit the file |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_file_as_pdf**
> FileIntegerWrapper save_file_as_pdf(id, save_as_pdf_integer)

Saves a file with the identifier specified in the request as a PDF document.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The file ID to save as PDF. | 
 **save_as_pdf_integer** | [**SaveAsPdfInteger**](SaveAsPdfInteger.md)| The parameters for saving the file as PDF. | 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_integer_wrapper import FileIntegerWrapper
from docspace_api_sdk.models.save_as_pdf_integer import SaveAsPdfInteger
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    id = 1 # int | The file ID to save as PDF.
    save_as_pdf_integer = docspace_api_sdk.SaveAsPdfInteger() # SaveAsPdfInteger | The parameters for saving the file as PDF.

    try:
        # Save a file as PDF
        api_response = api_instance.save_file_as_pdf(id, save_as_pdf_integer)
        print("The response of FilesApi->save_file_as_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->save_file_as_pdf: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New file information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**404** | File not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_form_role_mapping**
> save_form_role_mapping(file_id, save_form_role_mapping_dto_integer=save_form_role_mapping_dto_integer)

Saves the form role mapping.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  | 
 **save_form_role_mapping_dto_integer** | [**SaveFormRoleMappingDtoInteger**](SaveFormRoleMappingDtoInteger.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.save_form_role_mapping_dto_integer import SaveFormRoleMappingDtoInteger
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 'file_id_example' # str | 
    save_form_role_mapping_dto_integer = docspace_api_sdk.SaveFormRoleMappingDtoInteger() # SaveFormRoleMappingDtoInteger |  (optional)

    try:
        # Save form role mapping
        api_instance.save_form_role_mapping(file_id, save_form_role_mapping_dto_integer=save_form_role_mapping_dto_integer)
    except Exception as e:
        print("Exception when calling FilesApi->save_form_role_mapping: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated information about form role mappings |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You do not have enough permissions to edit the file |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_custom_filter_tag**
> FileIntegerWrapper set_custom_filter_tag(file_id, custom_filter_parameters)

Sets the Custom Filter editing mode to a file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID. | 
 **custom_filter_parameters** | [**CustomFilterParameters**](CustomFilterParameters.md)| The parameters for setting the Custom Filter editing mode. | 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.custom_filter_parameters import CustomFilterParameters
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file ID.
    custom_filter_parameters = docspace_api_sdk.CustomFilterParameters() # CustomFilterParameters | The parameters for setting the Custom Filter editing mode.

    try:
        # Set the Custom Filter editing mode
        api_response = api_instance.set_custom_filter_tag(file_id, custom_filter_parameters)
        print("The response of FilesApi->set_custom_filter_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->set_custom_filter_tag: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_file_external_link**
> FileShareWrapper set_file_external_link(id, file_link_request)

Sets an external link to a file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The file ID. | 
 **file_link_request** | [**FileLinkRequest**](FileLinkRequest.md)| The file external link parameters. | 

### Return type

[**FileShareWrapper**](FileShareWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_link_request import FileLinkRequest
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

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    id = 1 # int | The file ID.
    file_link_request = docspace_api_sdk.FileLinkRequest() # FileLinkRequest | The file external link parameters.

    try:
        # Set an external link
        api_response = api_instance.set_file_external_link(id, file_link_request)
        print("The response of FilesApi->set_file_external_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->set_file_external_link: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File security information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_file_order**
> FileIntegerWrapper set_file_order(file_id, order_request_dto=order_request_dto)

Sets the order of the file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file unique identifier. | 
 **order_request_dto** | [**OrderRequestDto**](OrderRequestDto.md)| The file order information. | [optional] 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_integer_wrapper import FileIntegerWrapper
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file unique identifier.
    order_request_dto = docspace_api_sdk.OrderRequestDto() # OrderRequestDto | The file order information. (optional)

    try:
        # Set file order
        api_response = api_instance.set_file_order(file_id, order_request_dto=order_request_dto)
        print("The response of FilesApi->set_file_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->set_file_order: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated file information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_files_order**
> FileEntryIntegerArrayWrapper set_files_order(orders_request_dto_integer=orders_request_dto_integer)

Sets the order of the files specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_request_dto_integer** | [**OrdersRequestDtoInteger**](OrdersRequestDtoInteger.md)|  | [optional] 

### Return type

[**FileEntryIntegerArrayWrapper**](FileEntryIntegerArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_entry_integer_array_wrapper import FileEntryIntegerArrayWrapper
from docspace_api_sdk.models.orders_request_dto_integer import OrdersRequestDtoInteger
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    orders_request_dto_integer = docspace_api_sdk.OrdersRequestDtoInteger() # OrdersRequestDtoInteger |  (optional)

    try:
        # Set order of files
        api_response = api_instance.set_files_order(orders_request_dto_integer=orders_request_dto_integer)
        print("The response of FilesApi->set_files_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->set_files_order: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated file entries information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_edit_file**
> StringWrapper start_edit_file(file_id, start_edit)

Informs about opening a file with the ID specified in the request for editing, locking it from being deleted or moved (this method is called by the mobile editors).

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID to start editing. | 
 **start_edit** | [**StartEdit**](StartEdit.md)| The file parameters to start editing. | 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.start_edit import StartEdit
from docspace_api_sdk.models.string_wrapper import StringWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file ID to start editing.
    start_edit = docspace_api_sdk.StartEdit() # StartEdit | The file parameters to start editing.

    try:
        # Start file editing
        api_response = api_instance.start_edit_file(file_id, start_edit)
        print("The response of FilesApi->start_edit_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->start_edit_file: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File key for Document Service |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You don't have enough permission to view the file |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_filling_file**
> FileIntegerWrapper start_filling_file(file_id)

Starts filling a file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID to start filling. | 

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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file ID to start filling.

    try:
        # Start file filling
        api_response = api_instance.start_filling_file(file_id)
        print("The response of FilesApi->start_filling_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->start_filling_file: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You do not have enough permissions to edit the file |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_file_favorite**
> BooleanWrapper toggle_file_favorite(file_id, favorite=favorite)

Changes the favorite status of the file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID. | 
 **favorite** | **bool**| Specifies if the file is marked as favorite or not. | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file ID.
    favorite = true # bool | Specifies if the file is marked as favorite or not. (optional)

    try:
        # Change the file favorite status
        api_response = api_instance.toggle_file_favorite(file_id, favorite=favorite)
        print("The response of FilesApi->toggle_file_favorite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->toggle_file_favorite: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true - the file is favorite, false - the file is not favorite |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You don't have enough permission to perform the operation |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **track_edit_file**
> KeyValuePairBooleanStringWrapper track_edit_file(file_id, tab_id=tab_id, doc_key_for_track=doc_key_for_track, is_finish=is_finish)

Tracks file changes when editing.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID to track editing changes. | 
 **tab_id** | **UUID**| The tab ID to track editing changes. | [optional] 
 **doc_key_for_track** | **str**| The document key for tracking changes. | [optional] 
 **is_finish** | **bool**| Specifies whether to finish file tracking or not. | [optional] 

### Return type

[**KeyValuePairBooleanStringWrapper**](KeyValuePairBooleanStringWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.key_value_pair_boolean_string_wrapper import KeyValuePairBooleanStringWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file ID to track editing changes.
    tab_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The tab ID to track editing changes. (optional)
    doc_key_for_track = 'abc123' # str | The document key for tracking changes. (optional)
    is_finish = true # bool | Specifies whether to finish file tracking or not. (optional)

    try:
        # Track file editing
        api_response = api_instance.track_edit_file(file_id, tab_id=tab_id, doc_key_for_track=doc_key_for_track, is_finish=is_finish)
        print("The response of FilesApi->track_edit_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->track_edit_file: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File changes |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You don't have enough permission to perform the operation |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file**
> FileIntegerWrapper update_file(file_id, update_file)

Updates the information of the selected file with the parameters specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID to update. | 
 **update_file** | [**UpdateFile**](UpdateFile.md)| The parameters for updating a file. | 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_integer_wrapper import FileIntegerWrapper
from docspace_api_sdk.models.update_file import UpdateFile
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 1 # int | The file ID to update.
    update_file = docspace_api_sdk.UpdateFile() # UpdateFile | The parameters for updating a file.

    try:
        # Update a file
        api_response = api_instance.update_file(file_id, update_file)
        print("The response of FilesApi->update_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->update_file: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated file information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You do not have enough permissions to edit the file |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

