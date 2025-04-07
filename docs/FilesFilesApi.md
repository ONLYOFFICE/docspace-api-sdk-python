# docspace.FilesFilesApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_templates**](FilesFilesApi.md#add_templates) | **POST** /api/2.0/files/templates | Add template files
[**change_history**](FilesFilesApi.md#change_history) | **PUT** /api/2.0/files/file/{fileId}/history | Change version history
[**check_fill_form_draft**](FilesFilesApi.md#check_fill_form_draft) | **POST** /api/2.0/files/masterform/{fileId}/checkfillformdraft | Check the form draft
[**copy_file_as**](FilesFilesApi.md#copy_file_as) | **POST** /api/2.0/files/file/{fileId}/copyas | Copy a file
[**create_edit_session**](FilesFilesApi.md#create_edit_session) | **POST** /api/2.0/files/file/{fileId}/edit_session | Create the editing session
[**create_file**](FilesFilesApi.md#create_file) | **POST** /api/2.0/files/{folderId}/file | Create a file
[**create_file_my_documents**](FilesFilesApi.md#create_file_my_documents) | **POST** /api/2.0/files/@my/file | Create a file in the \&quot;My documents\&quot; section
[**create_html_file**](FilesFilesApi.md#create_html_file) | **POST** /api/2.0/files/{folderId}/html | Create an HTML file
[**create_html_file_in_my**](FilesFilesApi.md#create_html_file_in_my) | **POST** /api/2.0/files/@my/html | Create an HTML file in the \&quot;My documents\&quot; section
[**create_primary_external_link**](FilesFilesApi.md#create_primary_external_link) | **POST** /api/2.0/files/file/{id}/link | Create primary external link
[**create_text_file**](FilesFilesApi.md#create_text_file) | **POST** /api/2.0/files/{folderId}/text | Create a txt file
[**create_text_file_in_my**](FilesFilesApi.md#create_text_file_in_my) | **POST** /api/2.0/files/@my/text | Create a text file in the \&quot;My documents\&quot; section
[**create_thumbnails**](FilesFilesApi.md#create_thumbnails) | **POST** /api/2.0/files/thumbnails | Create thumbnails
[**delete_file**](FilesFilesApi.md#delete_file) | **DELETE** /api/2.0/files/file/{fileId} | Delete a file
[**delete_recent**](FilesFilesApi.md#delete_recent) | **DELETE** /api/2.0/files/recent | Delete recent files
[**delete_templates**](FilesFilesApi.md#delete_templates) | **DELETE** /api/2.0/files/templates | Delete template files
[**get_edit_diff_url**](FilesFilesApi.md#get_edit_diff_url) | **GET** /api/2.0/files/file/{fileId}/edit/diff | Get changes URL
[**get_edit_history**](FilesFilesApi.md#get_edit_history) | **GET** /api/2.0/files/file/{fileId}/edit/history | Get version history
[**get_file_history**](FilesFilesApi.md#get_file_history) | **GET** /api/2.0/files/file/{fileId}/log | Get file history
[**get_file_info**](FilesFilesApi.md#get_file_info) | **GET** /api/2.0/files/file/{fileId} | Get file information
[**get_file_primary_external_link**](FilesFilesApi.md#get_file_primary_external_link) | **GET** /api/2.0/files/file/{id}/link | Get primary external link
[**get_file_version_info**](FilesFilesApi.md#get_file_version_info) | **GET** /api/2.0/files/file/{fileId}/history | Get file versions
[**get_fill_result**](FilesFilesApi.md#get_fill_result) | **GET** /api/2.0/files/file/fillresult | Gets fill result
[**get_links**](FilesFilesApi.md#get_links) | **GET** /api/2.0/files/file/{id}/links | Get file external links
[**get_presigned_file_uri**](FilesFilesApi.md#get_presigned_file_uri) | **GET** /api/2.0/files/file/{fileId}/presigned | Get file download link asynchronously
[**get_presigned_uri**](FilesFilesApi.md#get_presigned_uri) | **GET** /api/2.0/files/file/{fileId}/presigneduri | Get file download link
[**get_reference_data**](FilesFilesApi.md#get_reference_data) | **POST** /api/2.0/files/file/referencedata | Get reference data
[**is_form_pdf**](FilesFilesApi.md#is_form_pdf) | **GET** /api/2.0/files/file/{fileId}/isformpdf | Check the PDF file
[**lock_file**](FilesFilesApi.md#lock_file) | **PUT** /api/2.0/files/file/{fileId}/lock | Lock a file
[**open_edit**](FilesFilesApi.md#open_edit) | **GET** /api/2.0/files/file/{fileId}/openedit | Open a file
[**protect_users**](FilesFilesApi.md#protect_users) | **GET** /api/2.0/files/file/{fileId}/protectusers | Get users with the access to the protected file
[**restore_version**](FilesFilesApi.md#restore_version) | **GET** /api/2.0/files/file/{fileId}/restoreversion | Restore a file version
[**save_as_pdf**](FilesFilesApi.md#save_as_pdf) | **POST** /api/2.0/files/file/{id}/saveaspdf | Save as pdf
[**save_editing_from_form**](FilesFilesApi.md#save_editing_from_form) | **PUT** /api/2.0/files/file/{fileId}/saveediting | Save file edits
[**set_external_link**](FilesFilesApi.md#set_external_link) | **PUT** /api/2.0/files/file/{id}/links | Set an external link
[**set_files_order**](FilesFilesApi.md#set_files_order) | **PUT** /api/2.0/files/order | Sets order
[**set_order_file**](FilesFilesApi.md#set_order_file) | **PUT** /api/2.0/files/{fileId}/order | Sets order of a file with ID specified in the request
[**start_edit**](FilesFilesApi.md#start_edit) | **POST** /api/2.0/files/file/{fileId}/startedit | Start file editing
[**start_filling**](FilesFilesApi.md#start_filling) | **PUT** /api/2.0/files/file/{fileId}/startfilling | Starts filling
[**track_edit_file**](FilesFilesApi.md#track_edit_file) | **GET** /api/2.0/files/file/{fileId}/trackeditfile | Track file editing
[**update_file**](FilesFilesApi.md#update_file) | **PUT** /api/2.0/files/file/{fileId} | Update a file


# **add_templates**
> BooleanWrapper add_templates(templates_request_dto=templates_request_dto)

Add template files

Adds files with the IDs specified in the request to the template list.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.boolean_wrapper import BooleanWrapper
from docspace.models.templates_request_dto import TemplatesRequestDto
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
    api_instance = docspace.FilesFilesApi(api_client)
    templates_request_dto = docspace.TemplatesRequestDto() # TemplatesRequestDto |  (optional)

    try:
        # Add template files
        api_response = api_instance.add_templates(templates_request_dto=templates_request_dto)
        print("The response of FilesFilesApi->add_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->add_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templates_request_dto** | [**TemplatesRequestDto**](TemplatesRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_history**
> FileIntegerArrayWrapper change_history(file_id, change_history=change_history)

Change version history

Changes the version history of a file with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.change_history import ChangeHistory
from docspace.models.file_integer_array_wrapper import FileIntegerArrayWrapper
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
    api_instance = docspace.FilesFilesApi(api_client)
    file_id = 9846 # int | File Id
    change_history = docspace.ChangeHistory() # ChangeHistory | File (optional)

    try:
        # Change version history
        api_response = api_instance.change_history(file_id, change_history=change_history)
        print("The response of FilesFilesApi->change_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->change_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File Id | 
 **change_history** | [**ChangeHistory**](ChangeHistory.md)| File | [optional] 

### Return type

[**FileIntegerArrayWrapper**](FileIntegerArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated information about file versions |  -  |
**401** | Unauthorized |  -  |
**403** | You do not have enough permissions to edit the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_fill_form_draft**
> StringWrapper check_fill_form_draft(file_id, check_fill_form_draft=check_fill_form_draft)

Check the form draft

Checks if the current file is a form draft which can be filled out.

### Example


```python
import docspace
from docspace.models.check_fill_form_draft import CheckFillFormDraft
from docspace.models.string_wrapper import StringWrapper
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
    api_instance = docspace.FilesFilesApi(api_client)
    file_id = 9846 # int | File ID
    check_fill_form_draft = docspace.CheckFillFormDraft() # CheckFillFormDraft | File (optional)

    try:
        # Check the form draft
        api_response = api_instance.check_fill_form_draft(file_id, check_fill_form_draft=check_fill_form_draft)
        print("The response of FilesFilesApi->check_fill_form_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->check_fill_form_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File ID | 
 **check_fill_form_draft** | [**CheckFillFormDraft**](CheckFillFormDraft.md)| File | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

No authorization required

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
> FileEntryWrapper copy_file_as(file_id, copy_as_json_element=copy_as_json_element)

Copy a file

Copies (and converts if possible) an existing file to the specified folder.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.copy_as_json_element import CopyAsJsonElement
from docspace.models.file_entry_wrapper import FileEntryWrapper
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
    api_instance = docspace.FilesFilesApi(api_client)
    file_id = 9846 # int | File id
    copy_as_json_element = docspace.CopyAsJsonElement() # CopyAsJsonElement | File (optional)

    try:
        # Copy a file
        api_response = api_instance.copy_file_as(file_id, copy_as_json_element=copy_as_json_element)
        print("The response of FilesFilesApi->copy_file_as:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->copy_file_as: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File id | 
 **copy_as_json_element** | [**CopyAsJsonElement**](CopyAsJsonElement.md)| File | [optional] 

### Return type

[**FileEntryWrapper**](FileEntryWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Copied file entry information |  -  |
**400** | No file id or folder id toFolderId determine provider |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to create |  -  |
**404** | File not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_edit_session**
> ObjectWrapper create_edit_session(file_id, file_size=file_size)

Create the editing session

Creates a session to edit the existing file with multiple chunks (needed for WebDAV).

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.object_wrapper import ObjectWrapper
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
    api_instance = docspace.FilesFilesApi(api_client)
    file_id = 9846 # int | File ID
    file_size = 1234 # int | File size in bytes (optional)

    try:
        # Create the editing session
        api_response = api_instance.create_edit_session(file_id, file_size=file_size)
        print("The response of FilesFilesApi->create_edit_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->create_edit_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File ID | 
 **file_size** | **int**| File size in bytes | [optional] 

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
**200** | Information about created session |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to edit the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file**
> FileIntegerWrapper create_file(folder_id, create_file_json_element=create_file_json_element)

Create a file

Creates a new file in the specified folder with the title specified in the request.   **Note**: If a file extension is different from DOCX/XLSX/PPTX and refers to one of the known text, spreadsheet, or presentation formats, it will be changed to DOCX/XLSX/PPTX accordingly. If the file extension is not specified or is unknown, the DOCX extension will be added to the file title.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.create_file_json_element import CreateFileJsonElement
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
    api_instance = docspace.FilesFilesApi(api_client)
    folder_id = 9846 # int | Folder ID
    create_file_json_element = docspace.CreateFileJsonElement() # CreateFileJsonElement | File (optional)

    try:
        # Create a file
        api_response = api_instance.create_file(folder_id, create_file_json_element=create_file_json_element)
        print("The response of FilesFilesApi->create_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->create_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| Folder ID | 
 **create_file_json_element** | [**CreateFileJsonElement**](CreateFileJsonElement.md)| File | [optional] 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New file information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file_my_documents**
> FileIntegerWrapper create_file_my_documents(create_file_json_element=create_file_json_element)

Create a file in the \"My documents\" section

Creates a new file in the \"My documents\" section with the title specified in the request.   **Note**: If a file extension is different from DOCX/XLSX/PPTX and refers to one of the known text, spreadsheet, or presentation formats, it will be changed to DOCX/XLSX/PPTX accordingly. If the file extension is not specified or is unknown, the DOCX extension will be added to the file title.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.create_file_json_element import CreateFileJsonElement
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
    api_instance = docspace.FilesFilesApi(api_client)
    create_file_json_element = docspace.CreateFileJsonElement() # CreateFileJsonElement |  (optional)

    try:
        # Create a file in the \"My documents\" section
        api_response = api_instance.create_file_my_documents(create_file_json_element=create_file_json_element)
        print("The response of FilesFilesApi->create_file_my_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->create_file_my_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_file_json_element** | [**CreateFileJsonElement**](CreateFileJsonElement.md)|  | [optional] 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New file information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_html_file**
> FileIntegerWrapper create_html_file(folder_id, create_text_or_html_file=create_text_or_html_file)

Create an HTML file

Creates an HTML (.html) file in the selected folder with the title and contents specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.create_text_or_html_file import CreateTextOrHtmlFile
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
    api_instance = docspace.FilesFilesApi(api_client)
    folder_id = 9846 # int | Folder ID
    create_text_or_html_file = docspace.CreateTextOrHtmlFile() # CreateTextOrHtmlFile | File (optional)

    try:
        # Create an HTML file
        api_response = api_instance.create_html_file(folder_id, create_text_or_html_file=create_text_or_html_file)
        print("The response of FilesFilesApi->create_html_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->create_html_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| Folder ID | 
 **create_text_or_html_file** | [**CreateTextOrHtmlFile**](CreateTextOrHtmlFile.md)| File | [optional] 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New file information |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to create |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_html_file_in_my**
> FileIntegerWrapper create_html_file_in_my(create_text_or_html_file=create_text_or_html_file)

Create an HTML file in the \"My documents\" section

Creates an HTML (.html) file in the \"My documents\" section with the title and contents specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.create_text_or_html_file import CreateTextOrHtmlFile
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
    api_instance = docspace.FilesFilesApi(api_client)
    create_text_or_html_file = docspace.CreateTextOrHtmlFile() # CreateTextOrHtmlFile |  (optional)

    try:
        # Create an HTML file in the \"My documents\" section
        api_response = api_instance.create_html_file_in_my(create_text_or_html_file=create_text_or_html_file)
        print("The response of FilesFilesApi->create_html_file_in_my:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->create_html_file_in_my: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_text_or_html_file** | [**CreateTextOrHtmlFile**](CreateTextOrHtmlFile.md)|  | [optional] 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New file information |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to create |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_primary_external_link**
> FileShareWrapper create_primary_external_link(id, file_link_request=file_link_request)

Create primary external link

Creates a primary external link by the identifier specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.file_link_request import FileLinkRequest
from docspace.models.file_share_wrapper import FileShareWrapper
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
    api_instance = docspace.FilesFilesApi(api_client)
    id = 9846 # int | File ID
    file_link_request = docspace.FileLinkRequest() # FileLinkRequest | External link parameters (optional)

    try:
        # Create primary external link
        api_response = api_instance.create_primary_external_link(id, file_link_request=file_link_request)
        print("The response of FilesFilesApi->create_primary_external_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->create_primary_external_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| File ID | 
 **file_link_request** | [**FileLinkRequest**](FileLinkRequest.md)| External link parameters | [optional] 

### Return type

[**FileShareWrapper**](FileShareWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File security information |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_text_file**
> FileIntegerWrapper create_text_file(folder_id, create_text_or_html_file=create_text_or_html_file)

Create a txt file

Creates a text (.txt) file in the selected folder with the title and contents specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.create_text_or_html_file import CreateTextOrHtmlFile
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
    api_instance = docspace.FilesFilesApi(api_client)
    folder_id = 9846 # int | Folder ID
    create_text_or_html_file = docspace.CreateTextOrHtmlFile() # CreateTextOrHtmlFile | File (optional)

    try:
        # Create a txt file
        api_response = api_instance.create_text_file(folder_id, create_text_or_html_file=create_text_or_html_file)
        print("The response of FilesFilesApi->create_text_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->create_text_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| Folder ID | 
 **create_text_or_html_file** | [**CreateTextOrHtmlFile**](CreateTextOrHtmlFile.md)| File | [optional] 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New file information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_text_file_in_my**
> FileIntegerWrapper create_text_file_in_my(create_text_or_html_file=create_text_or_html_file)

Create a text file in the \"My documents\" section

Creates a text (.txt) file in the \"My documents\" section with the title and contents specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.create_text_or_html_file import CreateTextOrHtmlFile
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
    api_instance = docspace.FilesFilesApi(api_client)
    create_text_or_html_file = docspace.CreateTextOrHtmlFile() # CreateTextOrHtmlFile |  (optional)

    try:
        # Create a text file in the \"My documents\" section
        api_response = api_instance.create_text_file_in_my(create_text_or_html_file=create_text_or_html_file)
        print("The response of FilesFilesApi->create_text_file_in_my:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->create_text_file_in_my: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_text_or_html_file** | [**CreateTextOrHtmlFile**](CreateTextOrHtmlFile.md)|  | [optional] 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New file information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_thumbnails**
> ObjectArrayWrapper create_thumbnails(base_batch_request_dto=base_batch_request_dto)

Create thumbnails

Creates thumbnails for the files with the IDs specified in the request.

### Example


```python
import docspace
from docspace.models.base_batch_request_dto import BaseBatchRequestDto
from docspace.models.object_array_wrapper import ObjectArrayWrapper
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
    api_instance = docspace.FilesFilesApi(api_client)
    base_batch_request_dto = docspace.BaseBatchRequestDto() # BaseBatchRequestDto |  (optional)

    try:
        # Create thumbnails
        api_response = api_instance.create_thumbnails(base_batch_request_dto=base_batch_request_dto)
        print("The response of FilesFilesApi->create_thumbnails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->create_thumbnails: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_batch_request_dto** | [**BaseBatchRequestDto**](BaseBatchRequestDto.md)|  | [optional] 

### Return type

[**ObjectArrayWrapper**](ObjectArrayWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file IDs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> FileOperationArrayWrapper delete_file(file_id, delete=delete)

Delete a file

Deletes a file with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.delete import Delete
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
    api_instance = docspace.FilesFilesApi(api_client)
    file_id = 9846 # int | File ID
    delete = docspace.Delete() # Delete | File (optional)

    try:
        # Delete a file
        api_response = api_instance.delete_file(file_id, delete=delete)
        print("The response of FilesFilesApi->delete_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->delete_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File ID | 
 **delete** | [**Delete**](Delete.md)| File | [optional] 

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

# **delete_recent**
> NoContentResultWrapper delete_recent(base_batch_request_dto=base_batch_request_dto)

Delete recent files

Removes files with the IDs specified in the request from the \"Recent\" section.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.base_batch_request_dto import BaseBatchRequestDto
from docspace.models.no_content_result_wrapper import NoContentResultWrapper
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
    api_instance = docspace.FilesFilesApi(api_client)
    base_batch_request_dto = docspace.BaseBatchRequestDto() # BaseBatchRequestDto |  (optional)

    try:
        # Delete recent files
        api_response = api_instance.delete_recent(base_batch_request_dto=base_batch_request_dto)
        print("The response of FilesFilesApi->delete_recent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->delete_recent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_batch_request_dto** | [**BaseBatchRequestDto**](BaseBatchRequestDto.md)|  | [optional] 

### Return type

[**NoContentResultWrapper**](NoContentResultWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No content |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_templates**
> BooleanWrapper delete_templates(request_body=request_body)

Delete template files

Removes files with the IDs specified in the request from the template list.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.boolean_wrapper import BooleanWrapper
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
    api_instance = docspace.FilesFilesApi(api_client)
    request_body = [56] # List[int] | File IDs (optional)

    try:
        # Delete template files
        api_response = api_instance.delete_templates(request_body=request_body)
        print("The response of FilesFilesApi->delete_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->delete_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[int]**](int.md)| File IDs | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edit_diff_url**
> EditHistoryDataWrapper get_edit_diff_url(file_id, version=version)

Get changes URL

Returns a URL to the changes of a file version specified in the request.

### Example


```python
import docspace
from docspace.models.edit_history_data_wrapper import EditHistoryDataWrapper
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
    api_instance = docspace.FilesFilesApi(api_client)
    file_id = 9846 # int | File ID
    version = 1234 # int | File version (optional)

    try:
        # Get changes URL
        api_response = api_instance.get_edit_diff_url(file_id, version=version)
        print("The response of FilesFilesApi->get_edit_diff_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->get_edit_diff_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File ID | 
 **version** | **int**| File version | [optional] 

### Return type

[**EditHistoryDataWrapper**](EditHistoryDataWrapper.md)

### Authorization

No authorization required

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

Get version history

Returns the version history of a file with the ID specified in the request.

### Example


```python
import docspace
from docspace.models.edit_history_array_wrapper import EditHistoryArrayWrapper
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
    api_instance = docspace.FilesFilesApi(api_client)
    file_id = 9846 # int | File ID

    try:
        # Get version history
        api_response = api_instance.get_edit_history(file_id)
        print("The response of FilesFilesApi->get_edit_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->get_edit_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File ID | 

### Return type

[**EditHistoryArrayWrapper**](EditHistoryArrayWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Version history data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_history**
> HistoryArrayWrapper get_file_history(file_id, from_date=from_date, to_date=to_date)

Get file history

Get the list of actions performed on the file with the specified identifier

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
    api_instance = docspace.FilesFilesApi(api_client)
    file_id = 9846 # int | File ID
    from_date = docspace.ApiDateTime() # ApiDateTime | Start date (optional)
    to_date = docspace.ApiDateTime() # ApiDateTime | End date (optional)

    try:
        # Get file history
        api_response = api_instance.get_file_history(file_id, from_date=from_date, to_date=to_date)
        print("The response of FilesFilesApi->get_file_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->get_file_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File ID | 
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
**200** | List of actions performed on the file |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to perform the operation |  -  |
**404** | The required file was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_info**
> FileIntegerWrapper get_file_info(file_id, version=version)

Get file information

Returns the detailed information about a file with the ID specified in the request.

### Example


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


# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.FilesFilesApi(api_client)
    file_id = 9846 # int | File ID
    version = 1234 # int | File version (optional)

    try:
        # Get file information
        api_response = api_instance.get_file_info(file_id, version=version)
        print("The response of FilesFilesApi->get_file_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->get_file_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File ID | 
 **version** | **int**| File version | [optional] 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_primary_external_link**
> FileShareWrapper get_file_primary_external_link(id)

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
    api_instance = docspace.FilesFilesApi(api_client)
    id = 9846 # int | File ID

    try:
        # Get primary external link
        api_response = api_instance.get_file_primary_external_link(id)
        print("The response of FilesFilesApi->get_file_primary_external_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->get_file_primary_external_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| File ID | 

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
**200** | File security information |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_version_info**
> FileIntegerArrayWrapper get_file_version_info(file_id)

Get file versions

Returns the detailed information about all the available file versions with the ID specified in the request.

### Example


```python
import docspace
from docspace.models.file_integer_array_wrapper import FileIntegerArrayWrapper
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
    api_instance = docspace.FilesFilesApi(api_client)
    file_id = 9846 # int | File ID

    try:
        # Get file versions
        api_response = api_instance.get_file_version_info(file_id)
        print("The response of FilesFilesApi->get_file_version_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->get_file_version_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File ID | 

### Return type

[**FileIntegerArrayWrapper**](FileIntegerArrayWrapper.md)

### Authorization

No authorization required

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

Gets fill result

Gets fill result

### Example


```python
import docspace
from docspace.models.filling_form_result_integer_wrapper import FillingFormResultIntegerWrapper
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
    api_instance = docspace.FilesFilesApi(api_client)
    filling_session_id = 'some text' # str | Filling session id (optional)

    try:
        # Gets fill result
        api_response = api_instance.get_fill_result(filling_session_id=filling_session_id)
        print("The response of FilesFilesApi->get_fill_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->get_fill_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filling_session_id** | **str**| Filling session id | [optional] 

### Return type

[**FillingFormResultIntegerWrapper**](FillingFormResultIntegerWrapper.md)

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

# **get_links**
> FileShareArrayWrapper get_links(id)

Get file external links

Returns the external links of a file with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.file_share_array_wrapper import FileShareArrayWrapper
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
    api_instance = docspace.FilesFilesApi(api_client)
    id = 9846 # int | File ID

    try:
        # Get file external links
        api_response = api_instance.get_links(id)
        print("The response of FilesFilesApi->get_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->get_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| File ID | 

### Return type

[**FileShareArrayWrapper**](FileShareArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File security information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_presigned_file_uri**
> FileLinkWrapper get_presigned_file_uri(file_id)

Get file download link asynchronously

Returns a link to download a file with the ID specified in the request asynchronously.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.file_link_wrapper import FileLinkWrapper
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
    api_instance = docspace.FilesFilesApi(api_client)
    file_id = 9846 # int | File ID

    try:
        # Get file download link asynchronously
        api_response = api_instance.get_presigned_file_uri(file_id)
        print("The response of FilesFilesApi->get_presigned_file_uri:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->get_presigned_file_uri: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File ID | 

### Return type

[**FileLinkWrapper**](FileLinkWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File download link |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_presigned_uri**
> StringWrapper get_presigned_uri(file_id)

Get file download link

Returns a link to download a file with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.string_wrapper import StringWrapper
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
    api_instance = docspace.FilesFilesApi(api_client)
    file_id = 9846 # int | File ID

    try:
        # Get file download link
        api_response = api_instance.get_presigned_uri(file_id)
        print("The response of FilesFilesApi->get_presigned_uri:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->get_presigned_uri: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File ID | 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File download link |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_data**
> FileReferenceWrapper get_reference_data(get_reference_data_dto_integer=get_reference_data_dto_integer)

Get reference data

Returns the reference data to uniquely identify a file in its system and check the availability of insering data into the destination spreadsheet by the external link.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.file_reference_wrapper import FileReferenceWrapper
from docspace.models.get_reference_data_dto_integer import GetReferenceDataDtoInteger
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
    api_instance = docspace.FilesFilesApi(api_client)
    get_reference_data_dto_integer = docspace.GetReferenceDataDtoInteger() # GetReferenceDataDtoInteger |  (optional)

    try:
        # Get reference data
        api_response = api_instance.get_reference_data(get_reference_data_dto_integer=get_reference_data_dto_integer)
        print("The response of FilesFilesApi->get_reference_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->get_reference_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_reference_data_dto_integer** | [**GetReferenceDataDtoInteger**](GetReferenceDataDtoInteger.md)|  | [optional] 

### Return type

[**FileReferenceWrapper**](FileReferenceWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File reference data |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_form_pdf**
> BooleanWrapper is_form_pdf(file_id)

Check the PDF file

Checks if the PDF file is form or not.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.boolean_wrapper import BooleanWrapper
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
    api_instance = docspace.FilesFilesApi(api_client)
    file_id = 9846 # int | File ID

    try:
        # Check the PDF file
        api_response = api_instance.is_form_pdf(file_id)
        print("The response of FilesFilesApi->is_form_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->is_form_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File ID | 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true - the PDF file is form, false - the PDF file is not a form |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lock_file**
> FileIntegerWrapper lock_file(file_id, lock_file_parameters=lock_file_parameters)

Lock a file

Locks a file with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.file_integer_wrapper import FileIntegerWrapper
from docspace.models.lock_file_parameters import LockFileParameters
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
    api_instance = docspace.FilesFilesApi(api_client)
    file_id = 9846 # int | File ID
    lock_file_parameters = docspace.LockFileParameters() # LockFileParameters | Parameters for locking a file (optional)

    try:
        # Lock a file
        api_response = api_instance.lock_file(file_id, lock_file_parameters=lock_file_parameters)
        print("The response of FilesFilesApi->lock_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->lock_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File ID | 
 **lock_file_parameters** | [**LockFileParameters**](LockFileParameters.md)| Parameters for locking a file | [optional] 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Locked file information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_edit**
> ConfigurationIntegerWrapper open_edit(file_id, version=version, view=view, editor_type=editor_type, edit=edit, fill=fill)

Open a file

Returns the initialization configuration of a file to open it in the editor.

### Example


```python
import docspace
from docspace.models.configuration_integer_wrapper import ConfigurationIntegerWrapper
from docspace.models.editor_type import EditorType
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
    api_instance = docspace.FilesFilesApi(api_client)
    file_id = 9846 # int | File ID
    version = 1234 # int | File version (optional)
    view = true # bool | Specifies if a document will be opened for viewing only or not (optional)
    editor_type = docspace.EditorType() # EditorType | Editor type (optional)
    edit = true # bool | Edit (optional)
    fill = true # bool | Fill (optional)

    try:
        # Open a file
        api_response = api_instance.open_edit(file_id, version=version, view=view, editor_type=editor_type, edit=edit, fill=fill)
        print("The response of FilesFilesApi->open_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->open_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File ID | 
 **version** | **int**| File version | [optional] 
 **view** | **bool**| Specifies if a document will be opened for viewing only or not | [optional] 
 **editor_type** | [**EditorType**](.md)| Editor type | [optional] 
 **edit** | **bool**| Edit | [optional] 
 **fill** | **bool**| Fill | [optional] 

### Return type

[**ConfigurationIntegerWrapper**](ConfigurationIntegerWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configuration parameters |  -  |
**403** | You don&#39;t have enough permission to view the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_users**
> MentionWrapperArrayWrapper protect_users(file_id)

Get users with the access to the protected file

Returns a list of users with their access rights to the protected file with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.mention_wrapper_array_wrapper import MentionWrapperArrayWrapper
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
    api_instance = docspace.FilesFilesApi(api_client)
    file_id = 9846 # int | File ID

    try:
        # Get users with the access to the protected file
        api_response = api_instance.protect_users(file_id)
        print("The response of FilesFilesApi->protect_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->protect_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File ID | 

### Return type

[**MentionWrapperArrayWrapper**](MentionWrapperArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users with their access rights to the protected file |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_version**
> EditHistoryArrayWrapper restore_version(file_id, version=version, url=url)

Restore a file version

Restores a file version specified in the request.

### Example


```python
import docspace
from docspace.models.edit_history_array_wrapper import EditHistoryArrayWrapper
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
    api_instance = docspace.FilesFilesApi(api_client)
    file_id = 9846 # int | File ID
    version = 1234 # int | File version (optional)
    url = 'some text' # str | File version URL (optional)

    try:
        # Restore a file version
        api_response = api_instance.restore_version(file_id, version=version, url=url)
        print("The response of FilesFilesApi->restore_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->restore_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File ID | 
 **version** | **int**| File version | [optional] 
 **url** | **str**| File version URL | [optional] 

### Return type

[**EditHistoryArrayWrapper**](EditHistoryArrayWrapper.md)

### Authorization

No authorization required

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

# **save_as_pdf**
> FileIntegerWrapper save_as_pdf(id, save_as_pdf_integer=save_as_pdf_integer)

Save as pdf

Saves a file with the identifier specified in the request as a PDF document

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.file_integer_wrapper import FileIntegerWrapper
from docspace.models.save_as_pdf_integer import SaveAsPdfInteger
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
    api_instance = docspace.FilesFilesApi(api_client)
    id = 9846 # int | File ID
    save_as_pdf_integer = docspace.SaveAsPdfInteger() # SaveAsPdfInteger | Parameters for saving file as pdf (optional)

    try:
        # Save as pdf
        api_response = api_instance.save_as_pdf(id, save_as_pdf_integer=save_as_pdf_integer)
        print("The response of FilesFilesApi->save_as_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->save_as_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| File ID | 
 **save_as_pdf_integer** | [**SaveAsPdfInteger**](SaveAsPdfInteger.md)| Parameters for saving file as pdf | [optional] 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New file information |  -  |
**401** | Unauthorized |  -  |
**404** | File not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_editing_from_form**
> FileIntegerWrapper save_editing_from_form(file_id, file_extension=file_extension, download_uri=download_uri, file=file, forcesave=forcesave)

Save file edits

Saves edits to a file with the ID specified in the request.

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
    api_instance = docspace.FilesFilesApi(api_client)
    file_id = 9846 # int | File ID
    file_extension = 'file_extension_example' # str | File extension (optional)
    download_uri = 'download_uri_example' # str | URI to download a file (optional)
    file = None # bytearray | Request file stream (optional)
    forcesave = True # bool | Specifies whether to force save a file or not (optional)

    try:
        # Save file edits
        api_response = api_instance.save_editing_from_form(file_id, file_extension=file_extension, download_uri=download_uri, file=file, forcesave=forcesave)
        print("The response of FilesFilesApi->save_editing_from_form:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->save_editing_from_form: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File ID | 
 **file_extension** | **str**| File extension | [optional] 
 **download_uri** | **str**| URI to download a file | [optional] 
 **file** | **bytearray**| Request file stream | [optional] 
 **forcesave** | **bool**| Specifies whether to force save a file or not | [optional] 

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
**200** | Saved file parameters |  -  |
**400** | No file id or folder id toFolderId determine provider |  -  |
**401** | Unauthorized |  -  |
**403** | You do not have enough permissions to edit the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_external_link**
> FileShareWrapper set_external_link(id, file_link_request=file_link_request)

Set an external link

Sets an external link to a file with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.file_link_request import FileLinkRequest
from docspace.models.file_share_wrapper import FileShareWrapper
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
    api_instance = docspace.FilesFilesApi(api_client)
    id = 9846 # int | File ID
    file_link_request = docspace.FileLinkRequest() # FileLinkRequest | External link parameters (optional)

    try:
        # Set an external link
        api_response = api_instance.set_external_link(id, file_link_request=file_link_request)
        print("The response of FilesFilesApi->set_external_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->set_external_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| File ID | 
 **file_link_request** | [**FileLinkRequest**](FileLinkRequest.md)| External link parameters | [optional] 

### Return type

[**FileShareWrapper**](FileShareWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File security information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_files_order**
> set_files_order(orders_request_dto_integer=orders_request_dto_integer)

Sets order

Sets order

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.orders_request_dto_integer import OrdersRequestDtoInteger
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
    api_instance = docspace.FilesFilesApi(api_client)
    orders_request_dto_integer = docspace.OrdersRequestDtoInteger() # OrdersRequestDtoInteger |  (optional)

    try:
        # Sets order
        api_instance.set_files_order(orders_request_dto_integer=orders_request_dto_integer)
    except Exception as e:
        print("Exception when calling FilesFilesApi->set_files_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_request_dto_integer** | [**OrdersRequestDtoInteger**](OrdersRequestDtoInteger.md)|  | [optional] 

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
**200** | Order is set |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_order_file**
> set_order_file(file_id, order_request_dto=order_request_dto)

Sets order of a file with ID specified in the request

Sets order of a file with ID specified in the request

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
    api_instance = docspace.FilesFilesApi(api_client)
    file_id = 9846 # int | The unique identifier of the file
    order_request_dto = docspace.OrderRequestDto() # OrderRequestDto | Order information for the file (optional)

    try:
        # Sets order of a file with ID specified in the request
        api_instance.set_order_file(file_id, order_request_dto=order_request_dto)
    except Exception as e:
        print("Exception when calling FilesFilesApi->set_order_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The unique identifier of the file | 
 **order_request_dto** | [**OrderRequestDto**](OrderRequestDto.md)| Order information for the file | [optional] 

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
**200** | Order is set |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to perform the operation |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_edit**
> StringWrapper start_edit(file_id, start_edit=start_edit)

Start file editing

Informs about opening a file with the ID specified in the request for editing, locking it from being deleted or moved (this method is called by the mobile editors).

### Example


```python
import docspace
from docspace.models.start_edit import StartEdit
from docspace.models.string_wrapper import StringWrapper
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
    api_instance = docspace.FilesFilesApi(api_client)
    file_id = 9846 # int | File ID
    start_edit = docspace.StartEdit() # StartEdit | Parameters for starting file editing (optional)

    try:
        # Start file editing
        api_response = api_instance.start_edit(file_id, start_edit=start_edit)
        print("The response of FilesFilesApi->start_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->start_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File ID | 
 **start_edit** | [**StartEdit**](StartEdit.md)| Parameters for starting file editing | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File key for Document Service |  -  |
**403** | You don&#39;t have enough permission to view the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_filling**
> start_filling(file_id)

Starts filling

Starts filling a file with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
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
    api_instance = docspace.FilesFilesApi(api_client)
    file_id = 9846 # int | File ID

    try:
        # Starts filling
        api_instance.start_filling(file_id)
    except Exception as e:
        print("Exception when calling FilesFilesApi->start_filling: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File ID | 

### Return type

void (empty response body)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Unauthorized |  -  |
**403** | You do not have enough permissions to edit the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **track_edit_file**
> KeyValuePairBooleanStringWrapper track_edit_file(file_id, tab_id=tab_id, doc_key_for_track=doc_key_for_track, is_finish=is_finish)

Track file editing

Tracks file changes when editing.

### Example


```python
import docspace
from docspace.models.key_value_pair_boolean_string_wrapper import KeyValuePairBooleanStringWrapper
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
    api_instance = docspace.FilesFilesApi(api_client)
    file_id = 9846 # int | File ID
    tab_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | Tab ID (optional)
    doc_key_for_track = 'some text' # str | Document key for tracking (optional)
    is_finish = true # bool | Specifies whether to finish file tracking or not (optional)

    try:
        # Track file editing
        api_response = api_instance.track_edit_file(file_id, tab_id=tab_id, doc_key_for_track=doc_key_for_track, is_finish=is_finish)
        print("The response of FilesFilesApi->track_edit_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->track_edit_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File ID | 
 **tab_id** | **str**| Tab ID | [optional] 
 **doc_key_for_track** | **str**| Document key for tracking | [optional] 
 **is_finish** | **bool**| Specifies whether to finish file tracking or not | [optional] 

### Return type

[**KeyValuePairBooleanStringWrapper**](KeyValuePairBooleanStringWrapper.md)

### Authorization

No authorization required

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
> FileIntegerWrapper update_file(file_id, update_file=update_file)

Update a file

Updates the information of the selected file with the parameters specified in the request.

### Example


```python
import docspace
from docspace.models.file_integer_wrapper import FileIntegerWrapper
from docspace.models.update_file import UpdateFile
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
    api_instance = docspace.FilesFilesApi(api_client)
    file_id = 9846 # int | File ID
    update_file = docspace.UpdateFile() # UpdateFile | File (optional)

    try:
        # Update a file
        api_response = api_instance.update_file(file_id, update_file=update_file)
        print("The response of FilesFilesApi->update_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesFilesApi->update_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| File ID | 
 **update_file** | [**UpdateFile**](UpdateFile.md)| File | [optional] 

### Return type

[**FileIntegerWrapper**](FileIntegerWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated file information |  -  |
**403** | You do not have enough permissions to edit the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

