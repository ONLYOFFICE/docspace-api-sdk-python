# docspace_api_sdk.FilesApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_file_to_recent**](#add_file_to_recent) | **POST** /api/2.0/files/file/{fileId}/recent | 
[**add_templates**](#add_templates) | **POST** /api/2.0/files/templates | 
[**change_version_history**](#change_version_history) | **PUT** /api/2.0/files/file/{fileId}/history | 
[**check_fill_form_draft**](#check_fill_form_draft) | **POST** /api/2.0/files/masterform/{fileId}/checkfillformdraft | 
[**copy_file_as**](#copy_file_as) | **POST** /api/2.0/files/file/{fileId}/copyas | 
[**create_edit_session**](#create_edit_session) | **POST** /api/2.0/files/file/{fileId}/edit_session | 
[**create_file**](#create_file) | **POST** /api/2.0/files/{folderId}/file | 
[**create_file_in_my_documents**](#create_file_in_my_documents) | **POST** /api/2.0/files/@my/file | 
[**create_file_primary_external_link**](#create_file_primary_external_link) | **POST** /api/2.0/files/file/{id}/link | 
[**create_html_file**](#create_html_file) | **POST** /api/2.0/files/{folderId}/html | 
[**create_html_file_in_my_documents**](#create_html_file_in_my_documents) | **POST** /api/2.0/files/@my/html | 
[**create_text_file**](#create_text_file) | **POST** /api/2.0/files/{folderId}/text | 
[**create_text_file_in_my_documents**](#create_text_file_in_my_documents) | **POST** /api/2.0/files/@my/text | 
[**create_thumbnails**](#create_thumbnails) | **POST** /api/2.0/files/thumbnails | 
[**delete_file**](#delete_file) | **DELETE** /api/2.0/files/file/{fileId} | 
[**delete_recent**](#delete_recent) | **DELETE** /api/2.0/files/recent | 
[**delete_templates**](#delete_templates) | **DELETE** /api/2.0/files/templates | 
[**get_all_form_roles**](#get_all_form_roles) | **GET** /api/2.0/files/file/{fileId}/formroles | 
[**get_edit_diff_url**](#get_edit_diff_url) | **GET** /api/2.0/files/file/{fileId}/edit/diff | 
[**get_edit_history**](#get_edit_history) | **GET** /api/2.0/files/file/{fileId}/edit/history | 
[**get_file_history**](#get_file_history) | **GET** /api/2.0/files/file/{fileId}/log | 
[**get_file_info**](#get_file_info) | **GET** /api/2.0/files/file/{fileId} | 
[**get_file_links**](#get_file_links) | **GET** /api/2.0/files/file/{id}/links | 
[**get_file_primary_external_link**](#get_file_primary_external_link) | **GET** /api/2.0/files/file/{id}/link | 
[**get_file_version_info**](#get_file_version_info) | **GET** /api/2.0/files/file/{fileId}/history | 
[**get_fill_result**](#get_fill_result) | **GET** /api/2.0/files/file/fillresult | 
[**get_presigned_file_uri**](#get_presigned_file_uri) | **GET** /api/2.0/files/file/{fileId}/presigned | 
[**get_presigned_uri**](#get_presigned_uri) | **GET** /api/2.0/files/file/{fileId}/presigneduri | 
[**get_protected_file_users**](#get_protected_file_users) | **GET** /api/2.0/files/file/{fileId}/protectusers | 
[**get_reference_data**](#get_reference_data) | **POST** /api/2.0/files/file/referencedata | 
[**is_form_pdf**](#is_form_pdf) | **GET** /api/2.0/files/file/{fileId}/isformpdf | 
[**lock_file**](#lock_file) | **PUT** /api/2.0/files/file/{fileId}/lock | 
[**manage_form_filling**](#manage_form_filling) | **PUT** /api/2.0/files/file/{fileId}/manageformfilling | 
[**open_edit_file**](#open_edit_file) | **GET** /api/2.0/files/file/{fileId}/openedit | 
[**restore_file_version**](#restore_file_version) | **GET** /api/2.0/files/file/{fileId}/restoreversion | 
[**save_editing_file_from_form**](#save_editing_file_from_form) | **PUT** /api/2.0/files/file/{fileId}/saveediting | 
[**save_file_as_pdf**](#save_file_as_pdf) | **POST** /api/2.0/files/file/{id}/saveaspdf | 
[**save_form_role_mapping**](#save_form_role_mapping) | **POST** /api/2.0/files/file/{fileId}/formrolemapping | 
[**set_custom_filter_tag**](#set_custom_filter_tag) | **PUT** /api/2.0/files/file/{fileId}/customfilter | 
[**set_file_external_link**](#set_file_external_link) | **PUT** /api/2.0/files/file/{id}/links | 
[**set_file_order**](#set_file_order) | **PUT** /api/2.0/files/{fileId}/order | 
[**set_files_order**](#set_files_order) | **PUT** /api/2.0/files/order | 
[**start_edit_file**](#start_edit_file) | **POST** /api/2.0/files/file/{fileId}/startedit | 
[**start_filling_file**](#start_filling_file) | **PUT** /api/2.0/files/file/{fileId}/startfilling | 
[**toggle_file_favorite**](#toggle_file_favorite) | **GET** /api/2.0/files/favorites/{fileId} | 
[**track_edit_file**](#track_edit_file) | **GET** /api/2.0/files/file/{fileId}/trackeditfile | 
[**update_file**](#update_file) | **PUT** /api/2.0/files/file/{fileId} | 


# **add_file_to_recent**
> FileIntegerWrapper add_file_to_recent(file_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID of the request. | 

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
    file_id = 9846 # int | The file ID of the request.

    try:
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
**200** | New file information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_templates**
> BooleanWrapper add_templates(templates_request_dto=templates_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templates_request_dto** | [**TemplatesRequestDto**](TemplatesRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    templates_request_dto = docspace_api_sdk.TemplatesRequestDto() # TemplatesRequestDto |  (optional)

    try:
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
**200** | Boolean value: true if the operation is successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_version_history**
> FileIntegerArrayWrapper change_version_history(file_id, change_history)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file Id to change its version history. | 
 **change_history** | [**ChangeHistory**](ChangeHistory.md)| The parameters for changing version history. | 

### Return type

[**FileIntegerArrayWrapper**](FileIntegerArrayWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 9846 # int | The file Id to change its version history.
    change_history = docspace_api_sdk.ChangeHistory() # ChangeHistory | The parameters for changing version history.

    try:
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
**200** | Updated information about file versions |  -  |
**403** | You do not have enough permissions to edit the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_fill_form_draft**
> StringWrapper check_fill_form_draft(file_id, check_fill_form_draft)



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
    file_id = 9846 # int | The file ID of the form draft.
    check_fill_form_draft = docspace_api_sdk.CheckFillFormDraft() # CheckFillFormDraft | The parameters for checking the form draft filling.

    try:
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
**200** | Link to the form |  -  |
**403** | You don&#39;t have enough permission to view the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_file_as**
> FileEntryBaseWrapper copy_file_as(file_id, copy_as_json_element)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID to copy. | 
 **copy_as_json_element** | [**CopyAsJsonElement**](CopyAsJsonElement.md)| The parameters for copying a file. | 

### Return type

[**FileEntryBaseWrapper**](FileEntryBaseWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 9846 # int | The file ID to copy.
    copy_as_json_element = docspace_api_sdk.CopyAsJsonElement() # CopyAsJsonElement | The parameters for copying a file.

    try:
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
**200** | Copied file entry information |  -  |
**400** | No file id or folder id toFolderId determine provider |  -  |
**403** | You don&#39;t have enough permission to create |  -  |
**404** | File not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_edit_session**
> ObjectWrapper create_edit_session(file_id, file_size=file_size)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID. | 
 **file_size** | **int**| The file size in bytes. | [optional] 

### Return type

[**ObjectWrapper**](ObjectWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.object_wrapper import ObjectWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 9846 # int | The file ID.
    file_size = 1234 # int | The file size in bytes. (optional)

    try:
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
**200** | Information about created session |  -  |
**403** | You don&#39;t have enough permission to edit the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file**
> FileIntegerWrapper create_file(folder_id, create_file_json_element)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID for the file creation. | 
 **create_file_json_element** | [**CreateFileJsonElement**](CreateFileJsonElement.md)| The parameters for creating a file. | 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    folder_id = 9846 # int | The folder ID for the file creation.
    create_file_json_element = docspace_api_sdk.CreateFileJsonElement() # CreateFileJsonElement | The parameters for creating a file.

    try:
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
**200** | New file information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file_in_my_documents**
> FileIntegerWrapper create_file_in_my_documents(create_file_json_element=create_file_json_element)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_file_json_element** | [**CreateFileJsonElement**](CreateFileJsonElement.md)|  | [optional] 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    create_file_json_element = docspace_api_sdk.CreateFileJsonElement() # CreateFileJsonElement |  (optional)

    try:
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
**200** | New file information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file_primary_external_link**
> FileShareWrapper create_file_primary_external_link(id, file_link_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The file ID. | 
 **file_link_request** | [**FileLinkRequest**](FileLinkRequest.md)| The file external link parameters. | 

### Return type

[**FileShareWrapper**](FileShareWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    id = 9846 # int | The file ID.
    file_link_request = docspace_api_sdk.FileLinkRequest() # FileLinkRequest | The file external link parameters.

    try:
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
**200** | File security information |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_html_file**
> FileIntegerWrapper create_html_file(folder_id, create_text_or_html_file)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID to create the text or HTML file. | 
 **create_text_or_html_file** | [**CreateTextOrHtmlFile**](CreateTextOrHtmlFile.md)| The parameters for creating an HTML or text file. | 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    folder_id = 9846 # int | The folder ID to create the text or HTML file.
    create_text_or_html_file = docspace_api_sdk.CreateTextOrHtmlFile() # CreateTextOrHtmlFile | The parameters for creating an HTML or text file.

    try:
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
**200** | New file information |  -  |
**403** | You don&#39;t have enough permission to create |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_html_file_in_my_documents**
> FileIntegerWrapper create_html_file_in_my_documents(create_text_or_html_file=create_text_or_html_file)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_text_or_html_file** | [**CreateTextOrHtmlFile**](CreateTextOrHtmlFile.md)|  | [optional] 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    create_text_or_html_file = docspace_api_sdk.CreateTextOrHtmlFile() # CreateTextOrHtmlFile |  (optional)

    try:
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
**200** | New file information |  -  |
**403** | You don&#39;t have enough permission to create |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_text_file**
> FileIntegerWrapper create_text_file(folder_id, create_text_or_html_file)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID to create the text or HTML file. | 
 **create_text_or_html_file** | [**CreateTextOrHtmlFile**](CreateTextOrHtmlFile.md)| The parameters for creating an HTML or text file. | 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    folder_id = 9846 # int | The folder ID to create the text or HTML file.
    create_text_or_html_file = docspace_api_sdk.CreateTextOrHtmlFile() # CreateTextOrHtmlFile | The parameters for creating an HTML or text file.

    try:
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
**200** | New file information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_text_file_in_my_documents**
> FileIntegerWrapper create_text_file_in_my_documents(create_text_or_html_file=create_text_or_html_file)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_text_or_html_file** | [**CreateTextOrHtmlFile**](CreateTextOrHtmlFile.md)|  | [optional] 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    create_text_or_html_file = docspace_api_sdk.CreateTextOrHtmlFile() # CreateTextOrHtmlFile |  (optional)

    try:
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
**200** | New file information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_thumbnails**
> ObjectArrayWrapper create_thumbnails(base_batch_request_dto=base_batch_request_dto)



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
**200** | List of file IDs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> FileOperationArrayWrapper delete_file(file_id, delete)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID to delete. | 
 **delete** | [**Delete**](Delete.md)| The parameters for deleting a file. | 

### Return type

[**FileOperationArrayWrapper**](FileOperationArrayWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 9846 # int | The file ID to delete.
    delete = docspace_api_sdk.Delete() # Delete | The parameters for deleting a file.

    try:
        api_response = api_instance.delete_file(file_id, delete)
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
**200** | List of file operations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recent**
> NoContentResultWrapper delete_recent(base_batch_request_dto=base_batch_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_batch_request_dto** | [**BaseBatchRequestDto**](BaseBatchRequestDto.md)|  | [optional] 

### Return type

[**NoContentResultWrapper**](NoContentResultWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    base_batch_request_dto = docspace_api_sdk.BaseBatchRequestDto() # BaseBatchRequestDto |  (optional)

    try:
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
**200** | No content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_templates**
> BooleanWrapper delete_templates(request_body=request_body)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[int]**](int.md)| The file IDs. | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    request_body = [56] # List[int] | The file IDs. (optional)

    try:
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
**200** | Boolean value: true if the operation is successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_form_roles**
> FormRoleArrayWrapper get_all_form_roles(file_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID of the request. | 

### Return type

[**FormRoleArrayWrapper**](FormRoleArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.form_role_array_wrapper import FormRoleArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 9846 # int | The file ID of the request.

    try:
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
**200** | Successfully retrieved all roles for the form |  -  |
**403** | You do not have enough permissions to view the form roles |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edit_diff_url**
> EditHistoryDataWrapper get_edit_diff_url(file_id, version=version)



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
    file_id = 9846 # int | The file ID.
    version = 1234 # int | The file version. (optional)

    try:
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
**200** | File version history data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edit_history**
> EditHistoryArrayWrapper get_edit_history(file_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID of the request. | 

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
    file_id = 9846 # int | The file ID of the request.

    try:
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
**200** | Version history data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_history**
> HistoryArrayWrapper get_file_history(file_id, from_date=from_date, to_date=to_date, count=count, start_index=start_index)



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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 9846 # int | The file ID of the history request.
    from_date = docspace_api_sdk.ApiDateTime() # ApiDateTime | The start date of the history. (optional)
    to_date = docspace_api_sdk.ApiDateTime() # ApiDateTime | The end date of the history. (optional)
    count = 1234 # int | The number of history entries to retrieve for the file log. (optional)
    start_index = 1234 # int | The starting index for retrieving a subset of file history entries. (optional)

    try:
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
**200** | List of actions performed on the file |  -  |
**403** | You don&#39;t have enough permission to perform the operation |  -  |
**404** | The required file was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_info**
> FileIntegerWrapper get_file_info(file_id, version=version)



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
    file_id = 9846 # int | The file ID.
    version = 1234 # int | The file version. (optional)

    try:
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
**200** | File information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_links**
> FileShareArrayWrapper get_file_links(id, count=count, start_index=start_index)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The file ID of the request. | 
 **count** | **int**| The number of items to retrieve in the request. | [optional] 
 **start_index** | **int**| The starting index for the query results. | [optional] 

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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    id = 9846 # int | The file ID of the request.
    count = 1234 # int | The number of items to retrieve in the request. (optional)
    start_index = 1234 # int | The starting index for the query results. (optional)

    try:
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
**200** | File security information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_primary_external_link**
> FileShareWrapper get_file_primary_external_link(id, count=count, start_index=start_index)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The file ID of the request. | 
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
    id = 9846 # int | The file ID of the request.
    count = 1234 # int | The number of items to retrieve in the request. (optional)
    start_index = 1234 # int | The starting index for the query results. (optional)

    try:
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
**200** | File security information |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_version_info**
> FileIntegerArrayWrapper get_file_version_info(file_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID of the request. | 

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
    file_id = 9846 # int | The file ID of the request.

    try:
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
**200** | Information about file versions: folder ID, version, version group, content length, pure content length, file status, URL to view a file, web URL, file type, file extension, comment, encrypted or not, thumbnail URL, thumbnail status, locked or not, user ID who locked a file, denies file downloading or not, denies file sharing or not, file accessibility |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fill_result**
> FillingFormResultIntegerWrapper get_fill_result(filling_session_id=filling_session_id)



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
    filling_session_id = 'some text' # str | The form-filling session ID. (optional)

    try:
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
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_presigned_file_uri**
> FileLinkWrapper get_presigned_file_uri(file_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID of the request. | 

### Return type

[**FileLinkWrapper**](FileLinkWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_link_wrapper import FileLinkWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 9846 # int | The file ID of the request.

    try:
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
**200** | File download link |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_presigned_uri**
> StringWrapper get_presigned_uri(file_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID of the request. | 

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
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 9846 # int | The file ID of the request.

    try:
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
**200** | File download link |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_protected_file_users**
> MentionWrapperArrayWrapper get_protected_file_users(file_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID of the request. | 

### Return type

[**MentionWrapperArrayWrapper**](MentionWrapperArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.mention_wrapper_array_wrapper import MentionWrapperArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 9846 # int | The file ID of the request.

    try:
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
**200** | List of users with their access rights to the protected file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_data**
> FileReferenceWrapper get_reference_data(get_reference_data_dto_integer=get_reference_data_dto_integer)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_reference_data_dto_integer** | [**GetReferenceDataDtoInteger**](GetReferenceDataDtoInteger.md)|  | [optional] 

### Return type

[**FileReferenceWrapper**](FileReferenceWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    get_reference_data_dto_integer = docspace_api_sdk.GetReferenceDataDtoInteger() # GetReferenceDataDtoInteger |  (optional)

    try:
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
**200** | File reference data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_form_pdf**
> BooleanWrapper is_form_pdf(file_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID of the request. | 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 9846 # int | The file ID of the request.

    try:
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
**200** | Boolean value: true - the PDF file is form, false - the PDF file is not a form |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lock_file**
> FileIntegerWrapper lock_file(file_id, lock_file_parameters)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID for locking. | 
 **lock_file_parameters** | [**LockFileParameters**](LockFileParameters.md)| The parameters for locking a file. | 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 9846 # int | The file ID for locking.
    lock_file_parameters = docspace_api_sdk.LockFileParameters() # LockFileParameters | The parameters for locking a file.

    try:
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
**200** | Locked file information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_form_filling**
> manage_form_filling(file_id, manage_form_filling_dto_integer=manage_form_filling_dto_integer)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  | 
 **manage_form_filling_dto_integer** | [**ManageFormFillingDtoInteger**](ManageFormFillingDtoInteger.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.manage_form_filling_dto_integer import ManageFormFillingDtoInteger
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 'file_id_example' # str | 
    manage_form_filling_dto_integer = docspace_api_sdk.ManageFormFillingDtoInteger() # ManageFormFillingDtoInteger |  (optional)

    try:
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
**200** | Successfully processed the form filling action |  -  |
**403** | You do not have enough permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_edit_file**
> ConfigurationIntegerWrapper open_edit_file(file_id, version=version, view=view, editor_type=editor_type, edit=edit, fill=fill)



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
    file_id = 9846 # int | The file ID to open.
    version = 1234 # int | The file version to open. (optional)
    view = true # bool | Specifies if the document will be opened for viewing only or not. (optional)
    editor_type = docspace_api_sdk.EditorType() # EditorType | The editor type to open the file. (optional)
    edit = true # bool | Specifies if the document is opened in the editing mode or not. (optional)
    fill = true # bool | Specifies if the document is opened in the form-filling mode or not. (optional)

    try:
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
**200** | Configuration parameters |  -  |
**403** | You don&#39;t have enough permission to view the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_file_version**
> EditHistoryArrayWrapper restore_file_version(file_id, version=version, url=url)



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
    file_id = 9846 # int | The file ID of the restore version.
    version = 1234 # int | The file version of the restore. (optional)
    url = 'some text' # str | The file version URL of the restore. (optional)

    try:
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
**200** | Version history data: file ID, key, file version, version group, a user who updated a file, creation time, history changes in the string format, list of history changes, server version |  -  |
**400** | No file id or folder id toFolderId determine provider |  -  |
**403** | You do not have enough permissions to edit the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_editing_file_from_form**
> FileIntegerWrapper save_editing_file_from_form(file_id, file_extension=file_extension, download_uri=download_uri, file=file, forcesave=forcesave)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The editing file ID from the request. | 
 **file_extension** | **str**| The editing file extension from the request. | [optional] 
 **download_uri** | **str**| The URI to download the editing file. | [optional] 
 **file** | **bytearray**| The request file stream. | [optional] 
 **forcesave** | **bool**| Specifies whether to force save the file or not. | [optional] 

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
    file_id = 9846 # int | The editing file ID from the request.
    file_extension = 'file_extension_example' # str | The editing file extension from the request. (optional)
    download_uri = 'download_uri_example' # str | The URI to download the editing file. (optional)
    file = None # bytearray | The request file stream. (optional)
    forcesave = True # bool | Specifies whether to force save the file or not. (optional)

    try:
        api_response = api_instance.save_editing_file_from_form(file_id, file_extension=file_extension, download_uri=download_uri, file=file, forcesave=forcesave)
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
**200** | Saved file parameters |  -  |
**400** | No file id or folder id toFolderId determine provider |  -  |
**403** | You do not have enough permissions to edit the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_file_as_pdf**
> FileIntegerWrapper save_file_as_pdf(id, save_as_pdf_integer)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The file ID to save as PDF. | 
 **save_as_pdf_integer** | [**SaveAsPdfInteger**](SaveAsPdfInteger.md)| The parameters for saving file as PDF. | 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    id = 9846 # int | The file ID to save as PDF.
    save_as_pdf_integer = docspace_api_sdk.SaveAsPdfInteger() # SaveAsPdfInteger | The parameters for saving file as PDF.

    try:
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
**200** | New file information |  -  |
**404** | File not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_form_role_mapping**
> save_form_role_mapping(file_id, save_form_role_mapping_dto_integer=save_form_role_mapping_dto_integer)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  | 
 **save_form_role_mapping_dto_integer** | [**SaveFormRoleMappingDtoInteger**](SaveFormRoleMappingDtoInteger.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.save_form_role_mapping_dto_integer import SaveFormRoleMappingDtoInteger
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 'file_id_example' # str | 
    save_form_role_mapping_dto_integer = docspace_api_sdk.SaveFormRoleMappingDtoInteger() # SaveFormRoleMappingDtoInteger |  (optional)

    try:
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
**200** | Updated information about form role mappings |  -  |
**403** | You do not have enough permissions to edit the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_custom_filter_tag**
> FileIntegerWrapper set_custom_filter_tag(file_id, custom_filter_parameters)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID. | 
 **custom_filter_parameters** | [**CustomFilterParameters**](CustomFilterParameters.md)| The parameters for setting the Custom Filter editing mode. | 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 9846 # int | The file ID.
    custom_filter_parameters = docspace_api_sdk.CustomFilterParameters() # CustomFilterParameters | The parameters for setting the Custom Filter editing mode.

    try:
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
**200** | File information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_file_external_link**
> FileShareWrapper set_file_external_link(id, file_link_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The file ID. | 
 **file_link_request** | [**FileLinkRequest**](FileLinkRequest.md)| The file external link parameters. | 

### Return type

[**FileShareWrapper**](FileShareWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    id = 9846 # int | The file ID.
    file_link_request = docspace_api_sdk.FileLinkRequest() # FileLinkRequest | The file external link parameters.

    try:
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
**200** | File security information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_file_order**
> FileIntegerWrapper set_file_order(file_id, order_request_dto=order_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file unique identifier. | 
 **order_request_dto** | [**OrderRequestDto**](OrderRequestDto.md)| The file order information. | [optional] 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 9846 # int | The file unique identifier.
    order_request_dto = docspace_api_sdk.OrderRequestDto() # OrderRequestDto | The file order information. (optional)

    try:
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
**200** | Updated file information |  -  |
**403** | You don&#39;t have enough permission to perform the operation |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_files_order**
> FileEntryIntegerArrayWrapper set_files_order(orders_request_dto_integer=orders_request_dto_integer)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_request_dto_integer** | [**OrdersRequestDtoInteger**](OrdersRequestDtoInteger.md)|  | [optional] 

### Return type

[**FileEntryIntegerArrayWrapper**](FileEntryIntegerArrayWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    orders_request_dto_integer = docspace_api_sdk.OrdersRequestDtoInteger() # OrdersRequestDtoInteger |  (optional)

    try:
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
**200** | Updated file entries information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_edit_file**
> StringWrapper start_edit_file(file_id, start_edit)



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
    file_id = 9846 # int | The file ID to start editing.
    start_edit = docspace_api_sdk.StartEdit() # StartEdit | The file parameters to start editing.

    try:
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
**200** | File key for Document Service |  -  |
**403** | You don&#39;t have enough permission to view the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_filling_file**
> FileIntegerWrapper start_filling_file(file_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID to start filling. | 

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
    file_id = 9846 # int | The file ID to start filling.

    try:
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
**200** | File information |  -  |
**403** | You do not have enough permissions to edit the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_file_favorite**
> BooleanWrapper toggle_file_favorite(file_id, favorite=favorite)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID. | 
 **favorite** | **bool**| Specifies if the file is marked as favorite or not. | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.FilesApi(api_client)
    file_id = 9846 # int | The file ID.
    favorite = true # bool | Specifies if the file is marked as favorite or not. (optional)

    try:
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
**200** | Boolean value: true - the file is favorite, false - the file is not favorite |  -  |
**403** | You don&#39;t have enough permission to perform the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **track_edit_file**
> KeyValuePairBooleanStringWrapper track_edit_file(file_id, tab_id=tab_id, doc_key_for_track=doc_key_for_track, is_finish=is_finish)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID to track editing changes. | 
 **tab_id** | **str**| The tab ID to track editing changes. | [optional] 
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
    file_id = 9846 # int | The file ID to track editing changes.
    tab_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | The tab ID to track editing changes. (optional)
    doc_key_for_track = 'some text' # str | The document key for tracking changes. (optional)
    is_finish = true # bool | Specifies whether to finish file tracking or not. (optional)

    try:
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
**200** | File changes |  -  |
**403** | You don&#39;t have enough permission to perform the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file**
> FileIntegerWrapper update_file(file_id, update_file)



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
    file_id = 9846 # int | The file ID to update.
    update_file = docspace_api_sdk.UpdateFile() # UpdateFile | The parameters for updating a file.

    try:
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
**200** | Updated file information |  -  |
**403** | You do not have enough permissions to edit the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

