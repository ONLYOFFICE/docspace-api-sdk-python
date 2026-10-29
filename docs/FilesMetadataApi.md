# docspace_api_sdk.MetadataApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_file_templates**](#assign_file_templates) | **PUT** /api/2.0/files/metadata/file/{fileId}/templates | Assign templates to a file
[**assign_folder_templates**](#assign_folder_templates) | **PUT** /api/2.0/files/metadata/folder/{folderId}/templates | Assign templates to a folder
[**create_field**](#create_field) | **POST** /api/2.0/files/metadata/templates/{templateId}/fields | Add a metadata field
[**create_template**](#create_template) | **POST** /api/2.0/files/metadata/templates | Create a metadata template
[**delete_field**](#delete_field) | **DELETE** /api/2.0/files/metadata/templates/{templateId}/fields/{fieldId} | Delete a metadata field
[**delete_template**](#delete_template) | **DELETE** /api/2.0/files/metadata/templates/{templateId} | Delete a metadata template
[**get_cascade_progress**](#get_cascade_progress) | **GET** /api/2.0/files/metadata/folder/{folderId}/templates/progress | Get cascade progress
[**get_file_metadata**](#get_file_metadata) | **GET** /api/2.0/files/metadata/file/{fileId} | Get file metadata
[**get_folder_metadata**](#get_folder_metadata) | **GET** /api/2.0/files/metadata/folder/{folderId} | Get folder metadata
[**get_template**](#get_template) | **GET** /api/2.0/files/metadata/templates/{templateId} | Get a metadata template
[**get_templates**](#get_templates) | **GET** /api/2.0/files/metadata/templates | Get metadata templates
[**set_file_custom_fields**](#set_file_custom_fields) | **PUT** /api/2.0/files/metadata/file/{fileId}/customfields | Set file custom fields
[**set_file_values**](#set_file_values) | **PUT** /api/2.0/files/metadata/file/{fileId}/values | Set file metadata values
[**set_folder_custom_fields**](#set_folder_custom_fields) | **PUT** /api/2.0/files/metadata/folder/{folderId}/customfields | Set folder custom fields
[**set_folder_values**](#set_folder_values) | **PUT** /api/2.0/files/metadata/folder/{folderId}/values | Set folder metadata values
[**unassign_file_template**](#unassign_file_template) | **DELETE** /api/2.0/files/metadata/file/{fileId}/templates/{templateId} | Unassign a template from a file
[**unassign_folder_template**](#unassign_folder_template) | **DELETE** /api/2.0/files/metadata/folder/{folderId}/templates/{templateId} | Unassign a template from a folder
[**update_field**](#update_field) | **PUT** /api/2.0/files/metadata/templates/{templateId}/fields/{fieldId} | Update a metadata field
[**update_folder_template**](#update_folder_template) | **PUT** /api/2.0/files/metadata/folder/{folderId}/templates/{templateId} | Update a template assignment on a folder
[**update_template**](#update_template) | **PUT** /api/2.0/files/metadata/templates/{templateId} | Update a metadata template


# **assign_file_templates**
> assign_file_templates(file_id, assign_metadata_templates)

Assigns one or more metadata templates to a file, so its fields can be filled with
`PUT api/2.0/files/metadata/file/{fileId}/values`. The caller needs the right to edit the file. The assignment writes
no values and is idempotent: a template the file already carries is skipped, the others are added, an empty list
changes nothing. The call finishes in the request, nothing runs in the background. A template a cascading folder above
the file already provides stays inherited. A file the caller cannot edit is answered with 403; a file, or a template,
that does not exist with 404. To take a template off the file use
`DELETE api/2.0/files/metadata/file/{fileId}/templates/{templateId}`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID. | 
 **assign_metadata_templates** | [**AssignMetadataTemplates**](AssignMetadataTemplates.md)| The parameters for assigning templates. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.assign_metadata_templates import AssignMetadataTemplates
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
    api_instance = docspace_api_sdk.MetadataApi(api_client)
    file_id = 1 # int | The file ID.
    assign_metadata_templates = docspace_api_sdk.AssignMetadataTemplates() # AssignMetadataTemplates | The parameters for assigning templates.

    try:
        # Assign templates to a file
        api_instance.assign_file_templates(file_id, assign_metadata_templates)
    except Exception as e:
        print("Exception when calling MetadataApi->assign_file_templates: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The templates are assigned to the file, the ones it already carried are skipped; the response carries no content |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The request body cannot be read or has no `templateIds` |  -  |
**403** | The caller cannot edit the file |  -  |
**404** | The file or one of the templates does not exist |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_folder_templates**
> MetadataOperationWrapper assign_folder_templates(folder_id, assign_metadata_templates)

Assigns one or more metadata templates to a folder or a room and, with `cascade` set, propagates them to every
folder and file below it. The caller needs the right to create in the folder (a room manager or a content
creator); for a room that is its manager. The assignment itself finishes in the request and writes no values. The
cascade is asynchronous: a pass is queued that assigns the templates to the whole subtree and copies the values the
folder holds, and the answer is that pass with the `templateIds` it propagates. Poll
`GET api/2.0/files/metadata/folder/{folderId}/templates/progress` until `isCompleted` is true; a failed pass
reports its `error` there. The `conflictResolveType` decides what happens to a value an entry already holds: `Skip`
keeps it, `Overwrite` replaces it with the folder's value. A folder inside the subtree that cascades the same
template keeps its own values for its content. Without a cascade the answer is a completed operation without an identifier;
a template that already cascades keeps cascading, it is turned off with
`PUT api/2.0/files/metadata/folder/{folderId}/templates/{templateId}`. A caller without the right to create in the
folder is answered with 403; a folder, or a template, that does not exist with 404.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID. | 
 **assign_metadata_templates** | [**AssignMetadataTemplates**](AssignMetadataTemplates.md)| The parameters for assigning templates. | 

### Return type

[**MetadataOperationWrapper**](MetadataOperationWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.assign_metadata_templates import AssignMetadataTemplates
from docspace_api_sdk.models.metadata_operation_wrapper import MetadataOperationWrapper
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
    api_instance = docspace_api_sdk.MetadataApi(api_client)
    folder_id = 1 # int | The folder ID.
    assign_metadata_templates = docspace_api_sdk.AssignMetadataTemplates() # AssignMetadataTemplates | The parameters for assigning templates.

    try:
        # Assign templates to a folder
        api_response = api_instance.assign_folder_templates(folder_id, assign_metadata_templates)
        print("The response of MetadataApi->assign_folder_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->assign_folder_templates: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cascade operation status; a completed operation without an ID when no cascade is requested |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The request body cannot be read or has no `templateIds` |  -  |
**403** | The caller cannot create in the folder, or is not the manager of the room |  -  |
**404** | The folder or one of the templates does not exist |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_field**
> MetadataFieldWrapper create_field(template_id, metadata_field_request)

Adds a field to an existing metadata template. Only a DocSpace admin can change templates. The field name must be
unique within the template regardless of case and at most 255 characters, the type must be one of the published ones,
a choice field needs at least one option and unique option values, a field of another type takes no options. A
field without `order` is placed after the last field of the template. The entries the template is already
assigned to get the field without a value: nothing is written on them and no cascade runs. The answer is the
created field with its generated option identifiers. A template that does not exist is answered with 404, an
invalid field with 400.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| The template ID. | 
 **metadata_field_request** | [**MetadataFieldRequest**](MetadataFieldRequest.md)| The parameters of the field. | 

### Return type

[**MetadataFieldWrapper**](MetadataFieldWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.metadata_field_request import MetadataFieldRequest
from docspace_api_sdk.models.metadata_field_wrapper import MetadataFieldWrapper
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
    api_instance = docspace_api_sdk.MetadataApi(api_client)
    template_id = 1 # int | The template ID.
    metadata_field_request = docspace_api_sdk.MetadataFieldRequest() # MetadataFieldRequest | The parameters of the field.

    try:
        # Add a metadata field
        api_response = api_instance.create_field(template_id, metadata_field_request)
        print("The response of MetadataApi->create_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->create_field: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created field with the generated identifiers of its options |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Invalid field: an empty, repeated or too long name, an unknown type, options on a non-choice field or a choice field without options |  -  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | No metadata template with this identifier exists on the portal |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template**
> MetadataTemplateWrapper create_template(create_metadata_template_request_dto=create_metadata_template_request_dto)

Creates a metadata template for the whole portal, optionally with its fields in one call. Only a DocSpace admin can
create templates. The template name must be unique on the portal regardless of case, at most 255 characters, and the
name `System` is reserved. Every field needs a name unique within the template and a type from the published set; a
choice field requires at least one option and the options must be unique, a field of another type takes no options.
A field without `order` is placed after the fields that have one, in the order of the request. The template and
its fields are stored together: an invalid field rejects the whole request and nothing is created.
The answer is the created template with its fields and the generated option identifiers, which the values written
with `PUT api/2.0/files/metadata/file/{fileId}/values` refer to. A name already in use or an invalid field is
answered with 400; the request of a member who is not a DocSpace admin with 403.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_metadata_template_request_dto** | [**CreateMetadataTemplateRequestDto**](CreateMetadataTemplateRequestDto.md)|  | [optional] 

### Return type

[**MetadataTemplateWrapper**](MetadataTemplateWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.create_metadata_template_request_dto import CreateMetadataTemplateRequestDto
from docspace_api_sdk.models.metadata_template_wrapper import MetadataTemplateWrapper
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
    api_instance = docspace_api_sdk.MetadataApi(api_client)
    create_metadata_template_request_dto = docspace_api_sdk.CreateMetadataTemplateRequestDto() # CreateMetadataTemplateRequestDto |  (optional)

    try:
        # Create a metadata template
        api_response = api_instance.create_template(create_metadata_template_request_dto=create_metadata_template_request_dto)
        print("The response of MetadataApi->create_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->create_template: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created template with its fields and the generated identifiers of their options |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | An invalid template or field: a name in use, reserved or too long, an unknown field type, duplicate field names or wrong options |  -  |
**403** | The caller is not a DocSpace admin |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_field**
> delete_field(template_id, field_id)

Deletes a metadata field from its template together with every value written for it on any file, folder or room of
the portal. Only a DocSpace admin can change templates. The deletion is irreversible: the affected entries lose the
value at once, their search documents are rebuilt and the clients viewing them are told to refresh. The template and
its other fields stay as they are. A field that does not exist, or that belongs to another template than the one in
the route, is answered with 404.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| The template ID. | 
 **field_id** | **int**| The field ID. | 

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
    api_instance = docspace_api_sdk.MetadataApi(api_client)
    template_id = 1 # int | The template ID.
    field_id = 1 # int | The field ID.

    try:
        # Delete a metadata field
        api_instance.delete_field(template_id, field_id)
    except Exception as e:
        print("Exception when calling MetadataApi->delete_field: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The field and every value written for it are deleted; the response carries no content |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | The template does not exist, or it has no field with this identifier |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template**
> delete_template(template_id)

Deletes a metadata template together with its fields, its assignments and every value written for its fields on any
file, folder or room of the portal. Only a DocSpace admin can delete templates. The deletion is irreversible and there
is no confirmation: the affected entries lose the template at once, their search documents are rebuilt and the clients
viewing them are told to refresh. A template that does not exist, or was already deleted, is answered with 404.
To take the template off a single entry and keep it for the others use
`DELETE api/2.0/files/metadata/file/{fileId}/templates/{templateId}` instead.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| The template ID. | 

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
    api_instance = docspace_api_sdk.MetadataApi(api_client)
    template_id = 1 # int | The template ID.

    try:
        # Delete a metadata template
        api_instance.delete_template(template_id)
    except Exception as e:
        print("Exception when calling MetadataApi->delete_template: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The template, its fields, its assignments and their values are deleted; the response carries no content |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | No metadata template with this identifier exists on the portal, or it was already deleted |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cascade_progress**
> MetadataOperationWrapper get_cascade_progress(folder_id)

Reports the cascade pass of a folder started by `PUT api/2.0/files/metadata/folder/{folderId}/templates` or by
`PUT api/2.0/files/metadata/folder/{folderId}/templates/{templateId}`: the running one, otherwise the most recent
one. The caller needs read access to the folder, the call is read-only. `templateIds` names the templates the pass
propagates, so a client can show the progress next to the right template; `progress` is the share of the subtree
processed, `isCompleted` tells the pass is over and `error` carries the reason of a failed one; a completed pass
without an error has written every template and value it was asked for. A folder that never cascaded, or whose
passes were already dropped, is answered with a completed operation without an identifier and with empty
`templateIds` rather than with an error. A folder that does not exist is answered with 404.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder the operation acts on. Take the identifier from a listing such as `GET api/2.0/files/@root` or  `GET api/2.0/files/{folderId}`: a folder stored in the portal is numbered, while a folder in a connected  third-party account is named by an opaque string. | 

### Return type

[**MetadataOperationWrapper**](MetadataOperationWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.metadata_operation_wrapper import MetadataOperationWrapper
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
    api_instance = docspace_api_sdk.MetadataApi(api_client)
    folder_id = 1 # int | The folder the operation acts on. Take the identifier from a listing such as `GET api/2.0/files/@root` or  `GET api/2.0/files/{folderId}`: a folder stored in the portal is numbered, while a folder in a connected  third-party account is named by an opaque string.

    try:
        # Get cascade progress
        api_response = api_instance.get_cascade_progress(folder_id)
        print("The response of MetadataApi->get_cascade_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_cascade_progress: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cascade operation status; a completed operation without an ID when the folder has no cascade to report |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | No folder or room with this identifier exists |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_metadata**
> EntryMetadataWrapper get_file_metadata(file_id)

Returns the metadata of a file: the templates assigned to it, directly or inherited from a cascading folder above
it, each with its fields, and the custom text fields set on the file. The caller needs read access to the file: a
member of the portal, or an anonymous caller through an external link that grants access to the file or to a
folder above it, with the link key in the `Request-Token` header or in the `share` query parameter. The call is
read-only. A field carries its value inside it; a field the file holds no value for comes without a `value`.
A file never cascades, so every template reports `cascade` false and no `conflictResolveType`; whether it was
inherited from a folder above is not told apart from a direct assignment. The custom fields are name and value
pairs and are not part of any template. A file without metadata is answered with empty lists, not with an error.
The same shape is returned by `PUT api/2.0/files/metadata/file/{fileId}/values` after a write. A request with
neither a session nor a link key is answered with 401; a file the caller cannot read with 403, a file that does
not exist with 404.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file the operation addresses. Take the identifier from a listing such as `GET api/2.0/files/{folderId}`: a  file stored on the portal is numbered, while a file in a connected third-party account is named by an opaque  string. | 

### Return type

[**EntryMetadataWrapper**](EntryMetadataWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.entry_metadata_wrapper import EntryMetadataWrapper
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
    api_instance = docspace_api_sdk.MetadataApi(api_client)
    file_id = 10 # int | The file the operation addresses. Take the identifier from a listing such as `GET api/2.0/files/{folderId}`: a  file stored on the portal is numbered, while a file in a connected third-party account is named by an opaque  string.

    try:
        # Get file metadata
        api_response = api_instance.get_file_metadata(file_id)
        print("The response of MetadataApi->get_file_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_file_metadata: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The templates assigned to the file with their fields and values, and the custom fields of the file |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The caller has neither a session nor an external link key |  -  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | No file with this identifier exists |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_metadata**
> EntryMetadataWrapper get_folder_metadata(folder_id)

Returns the metadata of a folder or a room: the templates assigned to it, directly or inherited from a cascading
folder above it, each with its fields, and the custom text fields set on it. The caller needs read access to the
folder: a member of the portal, or an anonymous caller through an external link to the folder or to a folder
above it, with the link key in the `Request-Token` header or in the `share` query parameter. The call is
read-only. A field carries its value inside it; a field without a value on the folder comes without `value`. Each
template reports whether this folder cascades it to its content in `cascade`, with the rule of that cascade in
`conflictResolveType`, absent while it does not; an inherited template reports false unless this folder cascades it
on its own. The custom fields are name and value pairs outside any template. A folder without metadata is answered
with empty lists. The cascade is changed with `PUT api/2.0/files/metadata/folder/{folderId}/templates/{templateId}`.
A request with neither a session nor a link key is answered with 401; a folder the caller cannot read with 403, a
folder that does not exist with 404.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder the operation acts on. Take the identifier from a listing such as `GET api/2.0/files/@root` or  `GET api/2.0/files/{folderId}`: a folder stored in the portal is numbered, while a folder in a connected  third-party account is named by an opaque string. | 

### Return type

[**EntryMetadataWrapper**](EntryMetadataWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.entry_metadata_wrapper import EntryMetadataWrapper
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
    api_instance = docspace_api_sdk.MetadataApi(api_client)
    folder_id = 1 # int | The folder the operation acts on. Take the identifier from a listing such as `GET api/2.0/files/@root` or  `GET api/2.0/files/{folderId}`: a folder stored in the portal is numbered, while a folder in a connected  third-party account is named by an opaque string.

    try:
        # Get folder metadata
        api_response = api_instance.get_folder_metadata(folder_id)
        print("The response of MetadataApi->get_folder_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_folder_metadata: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The templates assigned to the folder with their fields, values and cascade state, and the custom fields of the folder |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The caller has neither a session nor an external link key |  -  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | No folder or room with this identifier exists |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template**
> MetadataTemplateWrapper get_template(template_id)

Returns one metadata template with its fields, in their display order, and the options of its choice fields. Any
member of the portal can read a template, the call is read-only. Use it to resolve the template identifiers a file or
a folder reports in `assignedMetadataTemplates` into names and fields. A template that does not exist is answered
with 404.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| The template ID. | 

### Return type

[**MetadataTemplateWrapper**](MetadataTemplateWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.metadata_template_wrapper import MetadataTemplateWrapper
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
    api_instance = docspace_api_sdk.MetadataApi(api_client)
    template_id = 1 # int | The template ID.

    try:
        # Get a metadata template
        api_response = api_instance.get_template(template_id)
        print("The response of MetadataApi->get_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_template: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The template with its fields in display order and the options of its choice fields |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | No metadata template with this identifier exists on the portal |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_templates**
> MetadataTemplateArrayWrapper get_templates(visible=visible)

Lists the metadata templates of the portal with their fields, the dictionary a file, a folder or a room is described
with. Any member of the portal can read it, the list is the same for everyone. The call is read-only. The templates
come back ordered by their creation, each with its fields in their display order and the choice options of the choice
fields; the `visible` parameter narrows the list to the templates shown in the pickers or to the hidden ones, without
it both are returned. The author and the last editor of a template come as user objects with the display name and
the avatar, so a list needs no lookup of its own per author. An empty list means the portal has no templates yet.
The custom text fields set on the entries are not templates and are not listed here: read them on the entry with
`GET api/2.0/files/metadata/file/{fileId}`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visible** | **bool**| Filters the templates by their visibility. | [optional] 

### Return type

[**MetadataTemplateArrayWrapper**](MetadataTemplateArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.metadata_template_array_wrapper import MetadataTemplateArrayWrapper
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
    api_instance = docspace_api_sdk.MetadataApi(api_client)
    visible = true # bool | Filters the templates by their visibility. (optional)

    try:
        # Get metadata templates
        api_response = api_instance.get_templates(visible=visible)
        print("The response of MetadataApi->get_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_templates: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of metadata templates |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_file_custom_fields**
> CustomFieldValueArrayWrapper set_file_custom_fields(file_id, set_custom_fields)

Sets the custom text fields of a file: free-form name and value pairs that need no template. The caller needs the
right to edit the file. A field is addressed by its name regardless of case: a listed name gets the value, a null or
empty value removes the field from the file, the names not listed are left alone, so a partial request is safe. A name
the portal has not seen yet creates the field for the whole portal, and a name no entry holds a value for any more is
dropped, so the set of names follows the values. A name is at most 255 characters, a value at most 8000, a name may
be listed once and a file holds at most 50 custom fields. The write finishes in the request; the values take part in
the free text search and in the `metadataFilters` of the listings. The answer is the custom fields of the file
after the write. An empty list, a blank, repeated or over-long name, an over-long value or more than 50 fields is
answered with 400; a file the caller cannot edit with 403; a file that does not exist with 404.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID. | 
 **set_custom_fields** | [**SetCustomFields**](SetCustomFields.md)| The custom fields to set. | 

### Return type

[**CustomFieldValueArrayWrapper**](CustomFieldValueArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.custom_field_value_array_wrapper import CustomFieldValueArrayWrapper
from docspace_api_sdk.models.set_custom_fields import SetCustomFields
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
    api_instance = docspace_api_sdk.MetadataApi(api_client)
    file_id = 1 # int | The file ID.
    set_custom_fields = docspace_api_sdk.SetCustomFields() # SetCustomFields | The custom fields to set.

    try:
        # Set file custom fields
        api_response = api_instance.set_file_custom_fields(file_id, set_custom_fields)
        print("The response of MetadataApi->set_file_custom_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->set_file_custom_fields: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The custom fields of the file with their values |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Invalid custom fields or too many of them |  -  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | No file with this identifier exists |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_file_values**
> EntryMetadataWrapper set_file_values(file_id, set_metadata_values)

Writes the values of metadata fields on a file. The caller needs the right to edit the file: a member with editing
access, or an anonymous caller through an external link that grants editing, with the link key in the
`Request-Token` header or in the `share` query parameter; a link that grants viewing, commenting, reviewing or
form filling only is refused. Every field must belong to a template the file carries, assigned with
`PUT api/2.0/files/metadata/file/{fileId}/templates` or inherited from a cascading folder, and a field may be
listed once. A value carries exactly the member of its type: `stringValue` for a text field of at most 8000
characters, `numberValue` for a whole number of at most 2^53-1 in magnitude (the largest integer a JSON client
reads exactly), `dateValue` for a date, `optionIds` for a choice field, a single option for a single choice; an
empty value clears the field. A date without a time zone offset is read as UTC. The write
finishes in the request, the file is re-indexed for the metadata filters at once. The custom text fields are not
written here: use `PUT api/2.0/files/metadata/file/{fileId}/customFields`. The answer is the whole metadata of the
file after the write, the same shape `GET api/2.0/files/metadata/file/{fileId}` returns. A value of the wrong type or beyond the number limit,
a field of a template the file does not carry, a field listed twice or a custom field is answered with 400; a
request with neither a session nor a link key with 401; a file the caller cannot edit with 403; a file or a field
that does not exist with 404.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID. | 
 **set_metadata_values** | [**SetMetadataValues**](SetMetadataValues.md)| The parameters for setting values. | 

### Return type

[**EntryMetadataWrapper**](EntryMetadataWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.entry_metadata_wrapper import EntryMetadataWrapper
from docspace_api_sdk.models.set_metadata_values import SetMetadataValues
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
    api_instance = docspace_api_sdk.MetadataApi(api_client)
    file_id = 1 # int | The file ID.
    set_metadata_values = docspace_api_sdk.SetMetadataValues() # SetMetadataValues | The parameters for setting values.

    try:
        # Set file metadata values
        api_response = api_instance.set_file_values(file_id, set_metadata_values)
        print("The response of MetadataApi->set_file_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->set_file_values: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The metadata of the file after the write: the assigned templates with the values of their fields, and the custom fields |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | A value does not match the field type or exceeds the number limit, a field is listed twice or is a custom field, or the field belongs to a template the file does not have |  -  |
**401** | The caller has neither a session nor an external link key |  -  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | The file or a field does not exist |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_folder_custom_fields**
> CustomFieldValueArrayWrapper set_folder_custom_fields(folder_id, set_custom_fields)

Sets the custom text fields of a folder or a room: free-form name and value pairs that need no template. The
caller needs the right to create in the folder (a room manager or a content creator); for a room that is its
manager. A field is addressed by its name regardless of case: a listed name gets the value, a null or empty value
removes the field, the names not listed are left alone. A new name creates the field for the whole portal, and a
name no entry holds a value for any more is dropped. A name is at most 255 characters, a value at most 8000, a name
may be listed once and a folder holds at most 50 custom fields. The custom fields never cascade to the content of
the folder. The write finishes in the request. The answer is the custom fields of the folder after the write. An empty list, a
blank, repeated or over-long name, an over-long value or more than 50 fields is answered with 400; a caller
without the right to create in the folder with 403; a folder that does not exist with 404.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID. | 
 **set_custom_fields** | [**SetCustomFields**](SetCustomFields.md)| The custom fields to set. | 

### Return type

[**CustomFieldValueArrayWrapper**](CustomFieldValueArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.custom_field_value_array_wrapper import CustomFieldValueArrayWrapper
from docspace_api_sdk.models.set_custom_fields import SetCustomFields
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
    api_instance = docspace_api_sdk.MetadataApi(api_client)
    folder_id = 1 # int | The folder ID.
    set_custom_fields = docspace_api_sdk.SetCustomFields() # SetCustomFields | The custom fields to set.

    try:
        # Set folder custom fields
        api_response = api_instance.set_folder_custom_fields(folder_id, set_custom_fields)
        print("The response of MetadataApi->set_folder_custom_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->set_folder_custom_fields: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The custom fields of the folder with their values |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Invalid custom fields or too many of them |  -  |
**403** | The caller cannot create in the folder, or is not the manager of the room |  -  |
**404** | No folder or room with this identifier exists |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_folder_values**
> EntryMetadataWrapper set_folder_values(folder_id, set_metadata_values)

Writes the values of metadata fields on a folder or a room. The caller needs the right to create in the folder (a
room manager or a content creator); for a room that is its manager. Every field must belong to a template the
folder carries, assigned with `PUT api/2.0/files/metadata/folder/{folderId}/templates` or inherited from a
cascading folder, and a field may be listed once. A value carries exactly the member of its type: `stringValue` for
a text field of at most 8000 characters, `numberValue` for a whole number of at most 2^53-1 in magnitude (the
largest integer a JSON client reads exactly), `dateValue` for a date, `optionIds` for a choice field; an empty
value clears the field. The write finishes in the request and touches the folder only: to
push the new values down a cascading folder run the cascade again with `Overwrite`. The custom text fields are written with
`PUT api/2.0/files/metadata/folder/{folderId}/customFields`. The answer is the whole metadata of the folder after
the write. A value of the wrong type or beyond the number limit, a field listed twice, a custom field or a field of a template the folder
does not carry is answered with 400; a caller without the right to create in the folder with 403; a folder or a
field that does not exist with 404.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID. | 
 **set_metadata_values** | [**SetMetadataValues**](SetMetadataValues.md)| The parameters for setting values. | 

### Return type

[**EntryMetadataWrapper**](EntryMetadataWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.entry_metadata_wrapper import EntryMetadataWrapper
from docspace_api_sdk.models.set_metadata_values import SetMetadataValues
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
    api_instance = docspace_api_sdk.MetadataApi(api_client)
    folder_id = 1 # int | The folder ID.
    set_metadata_values = docspace_api_sdk.SetMetadataValues() # SetMetadataValues | The parameters for setting values.

    try:
        # Set folder metadata values
        api_response = api_instance.set_folder_values(folder_id, set_metadata_values)
        print("The response of MetadataApi->set_folder_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->set_folder_values: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The metadata of the folder after the write: the assigned templates with the values of their fields, and the custom fields |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | A value does not match the field type or exceeds the number limit, a field is listed twice or is a custom field, or the field belongs to a template the folder does not have |  -  |
**403** | The caller cannot create in the folder, or is not the manager of the room |  -  |
**404** | The folder or a field does not exist |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_file_template**
> unassign_file_template(file_id, template_id)

Removes a metadata template from a file together with the values of its fields. The caller needs the right to edit
the file. The removal is irreversible for the values, the template itself stays on the portal and on the other
entries. It applies to a directly assigned template and to one inherited from a cascading folder alike; a later
cascade from that folder assigns it again. A file the caller cannot edit is answered with 403; a file, or a template,
that does not exist with 404.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID. | 
 **template_id** | **int**| The template ID. | 

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
    api_instance = docspace_api_sdk.MetadataApi(api_client)
    file_id = 1 # int | The file ID.
    template_id = 1 # int | The template ID.

    try:
        # Unassign a template from a file
        api_instance.unassign_file_template(file_id, template_id)
    except Exception as e:
        print("Exception when calling MetadataApi->unassign_file_template: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The template and the values of its fields are removed from the file; the response carries no content |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | The file or the template does not exist |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_folder_template**
> unassign_folder_template(folder_id, template_id)

Removes a metadata template from a folder or a room together with the values of its fields. The caller needs the
right to create content in the folder, that is a room manager or a content creator; for a room that is its
manager. When the template was cascaded from this folder, the
cascade stops here: the folders and files below keep the template and their values as a direct assignment of their
own, and there is no bulk rollback. To take the template off them as well, remove it entry by entry with
`DELETE api/2.0/files/metadata/file/{fileId}/templates/{templateId}`. A pass of the cascade still running is stopped
for this template. To stop the cascade and keep the template and its values on the folder use
`PUT api/2.0/files/metadata/folder/{folderId}/templates/{templateId}` with `cascade` false instead. A caller
without the right to create in the folder is answered with 403; a folder, or a template, that does not exist with 404.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID. | 
 **template_id** | **int**| The template ID. | 

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
    api_instance = docspace_api_sdk.MetadataApi(api_client)
    folder_id = 1 # int | The folder ID.
    template_id = 1 # int | The template ID.

    try:
        # Unassign a template from a folder
        api_instance.unassign_folder_template(folder_id, template_id)
    except Exception as e:
        print("Exception when calling MetadataApi->unassign_folder_template: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The template and its values are removed from the folder, and a cascade of it from this folder stops; the response carries no content |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller cannot create in the folder, or is not the manager of the room |  -  |
**404** | The folder or the template does not exist |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_field**
> MetadataFieldWrapper update_field(template_id, field_id, update_metadata_field_request)

Changes the name, the type, the options or the display order of a metadata field. Only a DocSpace admin can change
templates. The request is partial: a property left out keeps its value. The type can be changed only while no entry
holds a value for the field, and an option can be removed only while no entry has selected it; a new option is sent
without an identifier and gets one in the answer. A new name must be unique within the template regardless of case.
The values already written are left as they are. The field is addressed through its own template: a field reached
through another template's route is answered with 404, the same as a field that does not exist. A conflicting name,
a type change on a field with values or the removal of an option in use is answered with 400.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| The template ID. | 
 **field_id** | **int**| The field ID. | 
 **update_metadata_field_request** | [**UpdateMetadataFieldRequest**](UpdateMetadataFieldRequest.md)| The parameters of the field update. | 

### Return type

[**MetadataFieldWrapper**](MetadataFieldWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.metadata_field_wrapper import MetadataFieldWrapper
from docspace_api_sdk.models.update_metadata_field_request import UpdateMetadataFieldRequest
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
    api_instance = docspace_api_sdk.MetadataApi(api_client)
    template_id = 1 # int | The template ID.
    field_id = 1 # int | The field ID.
    update_metadata_field_request = docspace_api_sdk.UpdateMetadataFieldRequest() # UpdateMetadataFieldRequest | The parameters of the field update.

    try:
        # Update a metadata field
        api_response = api_instance.update_field(template_id, field_id, update_metadata_field_request)
        print("The response of MetadataApi->update_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->update_field: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The field after the change, with a generated identifier for every new option |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Invalid field, a name another field of the template has, a type change on a field with values or the removal of an option in use |  -  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | The template does not exist, or it has no field with this identifier |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_folder_template**
> MetadataOperationWrapper update_folder_template(folder_id, template_id, update_folder_metadata_template_request)

Turns the cascade of a metadata template the folder or the room already carries on or off, without taking the
template off the folder. The template must be assigned first, with `PUT api/2.0/files/metadata/folder/{folderId}/templates`
or inherited from a folder above. The caller needs the right to create in the folder (a room manager
or a content creator); for a room that is its manager. With `cascade` true the template is marked as cascading with
the given `conflictResolveType`, an inherited assignment becomes the folder's own, and the pass the assignment runs
is queued, also when the cascade was already on: the answer is that pass, poll
`GET api/2.0/files/metadata/folder/{folderId}/templates/progress` until `isCompleted` is true. With `cascade` false
the folder keeps the template and its values, the entries below keep them as their own, entries created later no
longer inherit the template from this folder, a running pass stops at its next batch, and the answer is a completed
operation without an identifier; `conflictResolveType` is ignored and a cascade already off stays so. A caller
without the right to create in the folder is answered with 403; a folder or a template that does not exist, or a
template the folder does not carry, with 404.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID. | 
 **template_id** | **int**| The ID of a template the folder already carries. | 
 **update_folder_metadata_template_request** | [**UpdateFolderMetadataTemplateRequest**](UpdateFolderMetadataTemplateRequest.md)| The new state of the assignment. | 

### Return type

[**MetadataOperationWrapper**](MetadataOperationWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.metadata_operation_wrapper import MetadataOperationWrapper
from docspace_api_sdk.models.update_folder_metadata_template_request import UpdateFolderMetadataTemplateRequest
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
    api_instance = docspace_api_sdk.MetadataApi(api_client)
    folder_id = 1 # int | The folder ID.
    template_id = 1 # int | The ID of a template the folder already carries.
    update_folder_metadata_template_request = docspace_api_sdk.UpdateFolderMetadataTemplateRequest() # UpdateFolderMetadataTemplateRequest | The new state of the assignment.

    try:
        # Update a template assignment on a folder
        api_response = api_instance.update_folder_template(folder_id, template_id, update_folder_metadata_template_request)
        print("The response of MetadataApi->update_folder_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->update_folder_template: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cascade operation status; a completed operation without an ID when the cascade was turned off |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The request body cannot be read |  -  |
**403** | The caller cannot create in the folder, or is not the manager of the room |  -  |
**404** | The folder or the template does not exist, or the template is not assigned to the folder |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template**
> MetadataTemplateWrapper update_template(template_id, update_metadata_template)

Renames a metadata template or changes whether it is shown in the pickers. Only a DocSpace admin can change
templates. The request is partial: a property left out keeps its value, the fields are not touched here and are
changed with `PUT api/2.0/files/metadata/templates/{templateId}/fields/{fieldId}`. The new name follows the rules
of the creation: unique on the portal regardless of case and at most 255 characters. The answer is the whole template
with its fields. A template that does not exist is answered with 404, a name already in use or too long with 400.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| The template ID. | 
 **update_metadata_template** | [**UpdateMetadataTemplate**](UpdateMetadataTemplate.md)| The parameters for updating the template. | 

### Return type

[**MetadataTemplateWrapper**](MetadataTemplateWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.metadata_template_wrapper import MetadataTemplateWrapper
from docspace_api_sdk.models.update_metadata_template import UpdateMetadataTemplate
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
    api_instance = docspace_api_sdk.MetadataApi(api_client)
    template_id = 1 # int | The template ID.
    update_metadata_template = docspace_api_sdk.UpdateMetadataTemplate() # UpdateMetadataTemplate | The parameters for updating the template.

    try:
        # Update a metadata template
        api_response = api_instance.update_template(template_id, update_metadata_template)
        print("The response of MetadataApi->update_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->update_template: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The whole template after the change, with its fields as they were |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | A template with this name already exists, or the name is too long |  -  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | No metadata template with this identifier exists on the portal |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

