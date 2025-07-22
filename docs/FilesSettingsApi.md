# docspace-api-sdk.FilesSettingsApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_access_to_thirdparty**](#change_access_to_thirdparty) | **PUT** /api/2.0/files/thirdparty | Change the third-party settings access
[**change_automatically_clean_up**](#change_automatically_clean_up) | **PUT** /api/2.0/files/settings/autocleanup | Update the trash bin auto-clearing setting
[**change_default_access_rights**](#change_default_access_rights) | **PUT** /api/2.0/files/settings/dafaultaccessrights | Change the default access rights
[**change_delete_confirm**](#change_delete_confirm) | **PUT** /api/2.0/files/changedeleteconfrim | Confirm the file deletion
[**change_download_zip_from_body**](#change_download_zip_from_body) | **PUT** /api/2.0/files/settings/downloadtargz | Change the archive format (using body parameters)
[**check_doc_service_url**](#check_doc_service_url) | **PUT** /api/2.0/files/docservice | Check the document service URL
[**display_file_extension**](#display_file_extension) | **PUT** /api/2.0/files/displayfileextension | Display a file extension
[**external_share**](#external_share) | **PUT** /api/2.0/files/settings/external | Change the external sharing ability
[**external_share_social_media**](#external_share_social_media) | **PUT** /api/2.0/files/settings/externalsocialmedia | Change the external sharing ability on social networks
[**forcesave**](#forcesave) | **PUT** /api/2.0/files/forcesave | Change the forcesaving ability
[**get_automatically_clean_up**](#get_automatically_clean_up) | **GET** /api/2.0/files/settings/autocleanup | Get the trash bin auto-clearing setting
[**get_doc_service_url**](#get_doc_service_url) | **GET** /api/2.0/files/docservice | Get the document service URL
[**get_files_module**](#get_files_module) | **GET** /api/2.0/files/info | Get the \&quot;Documents\&quot; information
[**get_files_settings**](#get_files_settings) | **GET** /api/2.0/files/settings | Get file settings
[**hide_confirm_cancel_operation**](#hide_confirm_cancel_operation) | **PUT** /api/2.0/files/hideconfirmcanceloperation | Hide confirmation dialog when canceling operations
[**hide_confirm_convert**](#hide_confirm_convert) | **PUT** /api/2.0/files/hideconfirmconvert | Hide the confirmation dialog when converting
[**hide_confirm_room_lifetime**](#hide_confirm_room_lifetime) | **PUT** /api/2.0/files/hideconfirmroomlifetime | Hide confirmation dialog when changing room lifetime settings
[**is_available_privacy_room_settings**](#is_available_privacy_room_settings) | **GET** /api/2.0/files/@privacy/available | Check the \&quot;Private Room\&quot; availability
[**keep_new_file_name**](#keep_new_file_name) | **PUT** /api/2.0/files/keepnewfilename | Ask a new file name
[**set_open_editor_in_same_tab**](#set_open_editor_in_same_tab) | **PUT** /api/2.0/files/settings/openeditorinsametab | Open document in the same browser tab
[**store_forcesave**](#store_forcesave) | **PUT** /api/2.0/files/storeforcesave | Change the ability to store the forcesaved files
[**store_original**](#store_original) | **PUT** /api/2.0/files/storeoriginal | Change the ability to upload original formats
[**update_file_if_exist**](#update_file_if_exist) | **PUT** /api/2.0/files/updateifexist | Update a file version if it exists


# **change_access_to_thirdparty**
> BooleanWrapper change_access_to_thirdparty(settings_request_dto=settings_request_dto)

Changes the access to the third-party settings.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_request_dto** | [**SettingsRequestDto**](SettingsRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.boolean_wrapper import BooleanWrapper
from docspace-api-sdk.models.settings_request_dto import SettingsRequestDto
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.FilesSettingsApi(api_client)
    settings_request_dto = docspace-api-sdk.SettingsRequestDto() # SettingsRequestDto |  (optional)

    try:
        # Change the third-party settings access
        api_response = api_instance.change_access_to_thirdparty(settings_request_dto=settings_request_dto)
        print("The response of FilesSettingsApi->change_access_to_thirdparty:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSettingsApi->change_access_to_thirdparty: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_automatically_clean_up**
> AutoCleanUpDataWrapper change_automatically_clean_up(auto_cleanup_request_dto=auto_cleanup_request_dto)

Updates the trash bin auto-clearing setting.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_cleanup_request_dto** | [**AutoCleanupRequestDto**](AutoCleanupRequestDto.md)|  | [optional] 

### Return type

[**AutoCleanUpDataWrapper**](AutoCleanUpDataWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.auto_clean_up_data_wrapper import AutoCleanUpDataWrapper
from docspace-api-sdk.models.auto_cleanup_request_dto import AutoCleanupRequestDto
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.FilesSettingsApi(api_client)
    auto_cleanup_request_dto = docspace-api-sdk.AutoCleanupRequestDto() # AutoCleanupRequestDto |  (optional)

    try:
        # Update the trash bin auto-clearing setting
        api_response = api_instance.change_automatically_clean_up(auto_cleanup_request_dto=auto_cleanup_request_dto)
        print("The response of FilesSettingsApi->change_automatically_clean_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSettingsApi->change_automatically_clean_up: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The auto-clearing setting properties: auto-clearing or not, a time interval when the auto-clearing will be performed |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_default_access_rights**
> FileShareArrayWrapper change_default_access_rights(request_body=request_body)

Changes the default access rights in the sharing settings.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[int]**](int.md)| Sharing rights (None, ReadWrite, Read, Restrict, Varies, Review, Comment, FillForms, CustomFilter, RoomAdmin, Editing, Collaborator). | [optional] 

### Return type

[**FileShareArrayWrapper**](FileShareArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.file_share_array_wrapper import FileShareArrayWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.FilesSettingsApi(api_client)
    request_body = [56] # List[int] | Sharing rights (None, ReadWrite, Read, Restrict, Varies, Review, Comment, FillForms, CustomFilter, RoomAdmin, Editing, Collaborator). (optional)

    try:
        # Change the default access rights
        api_response = api_instance.change_default_access_rights(request_body=request_body)
        print("The response of FilesSettingsApi->change_default_access_rights:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSettingsApi->change_default_access_rights: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated sharing rights (None, ReadWrite, Read, Restrict, Varies, Review, Comment, FillForms, CustomFilter, RoomAdmin, Editing, Collaborator) |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_delete_confirm**
> BooleanWrapper change_delete_confirm(settings_request_dto=settings_request_dto)

Specifies whether to confirm the file deletion or not.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_request_dto** | [**SettingsRequestDto**](SettingsRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.boolean_wrapper import BooleanWrapper
from docspace-api-sdk.models.settings_request_dto import SettingsRequestDto
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.FilesSettingsApi(api_client)
    settings_request_dto = docspace-api-sdk.SettingsRequestDto() # SettingsRequestDto |  (optional)

    try:
        # Confirm the file deletion
        api_response = api_instance.change_delete_confirm(settings_request_dto=settings_request_dto)
        print("The response of FilesSettingsApi->change_delete_confirm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSettingsApi->change_delete_confirm: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_download_zip_from_body**
> ICompressWrapper change_download_zip_from_body(display_request_dto=display_request_dto)

Changes the format of the downloaded archive from .zip to .tar.gz. This method uses the body parameters.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_request_dto** | [**DisplayRequestDto**](DisplayRequestDto.md)|  | [optional] 

### Return type

[**ICompressWrapper**](ICompressWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.display_request_dto import DisplayRequestDto
from docspace-api-sdk.models.i_compress_wrapper import ICompressWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.FilesSettingsApi(api_client)
    display_request_dto = docspace-api-sdk.DisplayRequestDto() # DisplayRequestDto |  (optional)

    try:
        # Change the archive format (using body parameters)
        api_response = api_instance.change_download_zip_from_body(display_request_dto=display_request_dto)
        print("The response of FilesSettingsApi->change_download_zip_from_body:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSettingsApi->change_download_zip_from_body: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Archive |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_doc_service_url**
> DocServiceUrlWrapper check_doc_service_url(check_doc_service_url_request_dto=check_doc_service_url_request_dto)

Checks the document service location URL.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_doc_service_url_request_dto** | [**CheckDocServiceUrlRequestDto**](CheckDocServiceUrlRequestDto.md)|  | [optional] 

### Return type

[**DocServiceUrlWrapper**](DocServiceUrlWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.check_doc_service_url_request_dto import CheckDocServiceUrlRequestDto
from docspace-api-sdk.models.doc_service_url_wrapper import DocServiceUrlWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.FilesSettingsApi(api_client)
    check_doc_service_url_request_dto = docspace-api-sdk.CheckDocServiceUrlRequestDto() # CheckDocServiceUrlRequestDto |  (optional)

    try:
        # Check the document service URL
        api_response = api_instance.check_doc_service_url(check_doc_service_url_request_dto=check_doc_service_url_request_dto)
        print("The response of FilesSettingsApi->check_doc_service_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSettingsApi->check_doc_service_url: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document service information: the Document Server address, the Document Server address in the local private network, the Community Server address |  -  |
**400** | Invalid input urls/Mixed Active Content is not allowed. HTTPS address for Document Server is required |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_file_extension**
> BooleanWrapper display_file_extension(settings_request_dto=settings_request_dto)

Specifies whether to display a file extension or not.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_request_dto** | [**SettingsRequestDto**](SettingsRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.boolean_wrapper import BooleanWrapper
from docspace-api-sdk.models.settings_request_dto import SettingsRequestDto
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.FilesSettingsApi(api_client)
    settings_request_dto = docspace-api-sdk.SettingsRequestDto() # SettingsRequestDto |  (optional)

    try:
        # Display a file extension
        api_response = api_instance.display_file_extension(settings_request_dto=settings_request_dto)
        print("The response of FilesSettingsApi->display_file_extension:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSettingsApi->display_file_extension: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the parameter is enabled |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_share**
> BooleanWrapper external_share(display_request_dto=display_request_dto)

Changes the ability to share a file externally.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_request_dto** | [**DisplayRequestDto**](DisplayRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.boolean_wrapper import BooleanWrapper
from docspace-api-sdk.models.display_request_dto import DisplayRequestDto
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.FilesSettingsApi(api_client)
    display_request_dto = docspace-api-sdk.DisplayRequestDto() # DisplayRequestDto |  (optional)

    try:
        # Change the external sharing ability
        api_response = api_instance.external_share(display_request_dto=display_request_dto)
        print("The response of FilesSettingsApi->external_share:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSettingsApi->external_share: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the parameter is enabled |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_share_social_media**
> BooleanWrapper external_share_social_media(display_request_dto=display_request_dto)

Changes the ability to share a file externally on social networks.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_request_dto** | [**DisplayRequestDto**](DisplayRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.boolean_wrapper import BooleanWrapper
from docspace-api-sdk.models.display_request_dto import DisplayRequestDto
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.FilesSettingsApi(api_client)
    display_request_dto = docspace-api-sdk.DisplayRequestDto() # DisplayRequestDto |  (optional)

    try:
        # Change the external sharing ability on social networks
        api_response = api_instance.external_share_social_media(display_request_dto=display_request_dto)
        print("The response of FilesSettingsApi->external_share_social_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSettingsApi->external_share_social_media: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the parameter is enabled |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forcesave**
> BooleanWrapper forcesave()

Specifies if the file forcesaving is enabled or not.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.boolean_wrapper import BooleanWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.FilesSettingsApi(api_client)

    try:
        # Change the forcesaving ability
        api_response = api_instance.forcesave()
        print("The response of FilesSettingsApi->forcesave:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSettingsApi->forcesave: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the parameter is enabled |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_automatically_clean_up**
> AutoCleanUpDataWrapper get_automatically_clean_up()

Returns the trash bin auto-clearing setting.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**AutoCleanUpDataWrapper**](AutoCleanUpDataWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.auto_clean_up_data_wrapper import AutoCleanUpDataWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.FilesSettingsApi(api_client)

    try:
        # Get the trash bin auto-clearing setting
        api_response = api_instance.get_automatically_clean_up()
        print("The response of FilesSettingsApi->get_automatically_clean_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSettingsApi->get_automatically_clean_up: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The auto-clearing setting properties: auto-clearing or not, a time interval when the auto-clearing will be performed |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_doc_service_url**
> DocServiceUrlWrapper get_doc_service_url(version=version)

Returns the URL address of the connected editors.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **bool**| Specifies whether to return the editor version or not. | [optional] 

### Return type

[**DocServiceUrlWrapper**](DocServiceUrlWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.doc_service_url_wrapper import DocServiceUrlWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)


# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.FilesSettingsApi(api_client)
    version = true # bool | Specifies whether to return the editor version or not. (optional)

    try:
        # Get the document service URL
        api_response = api_instance.get_doc_service_url(version=version)
        print("The response of FilesSettingsApi->get_doc_service_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSettingsApi->get_doc_service_url: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The document service URL with the editor version specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files_module**
> ModuleWrapper get_files_module()

Returns the information about the "Documents" module.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**ModuleWrapper**](ModuleWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.module_wrapper import ModuleWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.FilesSettingsApi(api_client)

    try:
        # Get the \"Documents\" information
        api_response = api_instance.get_files_module()
        print("The response of FilesSettingsApi->get_files_module:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSettingsApi->get_files_module: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Module information: ID, product class name, title, description, icon URL, large icon URL, start URL, primary or nor, help URL |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files_settings**
> FilesSettingsWrapper get_files_settings()

Returns all the file settings.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**FilesSettingsWrapper**](FilesSettingsWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.files_settings_wrapper import FilesSettingsWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)


# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.FilesSettingsApi(api_client)

    try:
        # Get file settings
        api_response = api_instance.get_files_settings()
        print("The response of FilesSettingsApi->get_files_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSettingsApi->get_files_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hide_confirm_cancel_operation**
> BooleanWrapper hide_confirm_cancel_operation(settings_request_dto=settings_request_dto)

Hides the confirmation dialog when canceling operations.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_request_dto** | [**SettingsRequestDto**](SettingsRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.boolean_wrapper import BooleanWrapper
from docspace-api-sdk.models.settings_request_dto import SettingsRequestDto
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.FilesSettingsApi(api_client)
    settings_request_dto = docspace-api-sdk.SettingsRequestDto() # SettingsRequestDto |  (optional)

    try:
        # Hide confirmation dialog when canceling operations
        api_response = api_instance.hide_confirm_cancel_operation(settings_request_dto=settings_request_dto)
        print("The response of FilesSettingsApi->hide_confirm_cancel_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSettingsApi->hide_confirm_cancel_operation: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the parameter is enabled |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hide_confirm_convert**
> ModuleWrapper hide_confirm_convert(hide_confirm_convert_request_dto=hide_confirm_convert_request_dto)

Hides the confirmation dialog for saving the file copy in the original format when converting a file.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hide_confirm_convert_request_dto** | [**HideConfirmConvertRequestDto**](HideConfirmConvertRequestDto.md)|  | [optional] 

### Return type

[**ModuleWrapper**](ModuleWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.hide_confirm_convert_request_dto import HideConfirmConvertRequestDto
from docspace-api-sdk.models.module_wrapper import ModuleWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.FilesSettingsApi(api_client)
    hide_confirm_convert_request_dto = docspace-api-sdk.HideConfirmConvertRequestDto() # HideConfirmConvertRequestDto |  (optional)

    try:
        # Hide the confirmation dialog when converting
        api_response = api_instance.hide_confirm_convert(hide_confirm_convert_request_dto=hide_confirm_convert_request_dto)
        print("The response of FilesSettingsApi->hide_confirm_convert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSettingsApi->hide_confirm_convert: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hide_confirm_room_lifetime**
> BooleanWrapper hide_confirm_room_lifetime(settings_request_dto=settings_request_dto)

Hides the confirmation dialog when changing the room lifetime settings.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_request_dto** | [**SettingsRequestDto**](SettingsRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.boolean_wrapper import BooleanWrapper
from docspace-api-sdk.models.settings_request_dto import SettingsRequestDto
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.FilesSettingsApi(api_client)
    settings_request_dto = docspace-api-sdk.SettingsRequestDto() # SettingsRequestDto |  (optional)

    try:
        # Hide confirmation dialog when changing room lifetime settings
        api_response = api_instance.hide_confirm_room_lifetime(settings_request_dto=settings_request_dto)
        print("The response of FilesSettingsApi->hide_confirm_room_lifetime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSettingsApi->hide_confirm_room_lifetime: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the parameter is enabled |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_available_privacy_room_settings**
> BooleanWrapper is_available_privacy_room_settings()

Checks if the "Private Room" settings are available or not.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.boolean_wrapper import BooleanWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.FilesSettingsApi(api_client)

    try:
        # Check the \"Private Room\" availability
        api_response = api_instance.is_available_privacy_room_settings()
        print("The response of FilesSettingsApi->is_available_privacy_room_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSettingsApi->is_available_privacy_room_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the Private Room settings are available |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keep_new_file_name**
> BooleanWrapper keep_new_file_name(settings_request_dto=settings_request_dto)

Specifies whether to ask a user for a file name on creation or not.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_request_dto** | [**SettingsRequestDto**](SettingsRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.boolean_wrapper import BooleanWrapper
from docspace-api-sdk.models.settings_request_dto import SettingsRequestDto
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.FilesSettingsApi(api_client)
    settings_request_dto = docspace-api-sdk.SettingsRequestDto() # SettingsRequestDto |  (optional)

    try:
        # Ask a new file name
        api_response = api_instance.keep_new_file_name(settings_request_dto=settings_request_dto)
        print("The response of FilesSettingsApi->keep_new_file_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSettingsApi->keep_new_file_name: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_open_editor_in_same_tab**
> BooleanWrapper set_open_editor_in_same_tab(settings_request_dto=settings_request_dto)

Changes the ability to open the document in the same browser tab.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_request_dto** | [**SettingsRequestDto**](SettingsRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.boolean_wrapper import BooleanWrapper
from docspace-api-sdk.models.settings_request_dto import SettingsRequestDto
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.FilesSettingsApi(api_client)
    settings_request_dto = docspace-api-sdk.SettingsRequestDto() # SettingsRequestDto |  (optional)

    try:
        # Open document in the same browser tab
        api_response = api_instance.set_open_editor_in_same_tab(settings_request_dto=settings_request_dto)
        print("The response of FilesSettingsApi->set_open_editor_in_same_tab:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSettingsApi->set_open_editor_in_same_tab: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the parameter is enabled |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_forcesave**
> BooleanWrapper store_forcesave()

Changes the ability to store the forcesaved file versions.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.boolean_wrapper import BooleanWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.FilesSettingsApi(api_client)

    try:
        # Change the ability to store the forcesaved files
        api_response = api_instance.store_forcesave()
        print("The response of FilesSettingsApi->store_forcesave:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSettingsApi->store_forcesave: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_original**
> BooleanWrapper store_original(settings_request_dto=settings_request_dto)

Changes the ability to upload documents in the original formats as well.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_request_dto** | [**SettingsRequestDto**](SettingsRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.boolean_wrapper import BooleanWrapper
from docspace-api-sdk.models.settings_request_dto import SettingsRequestDto
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.FilesSettingsApi(api_client)
    settings_request_dto = docspace-api-sdk.SettingsRequestDto() # SettingsRequestDto |  (optional)

    try:
        # Change the ability to upload original formats
        api_response = api_instance.store_original(settings_request_dto=settings_request_dto)
        print("The response of FilesSettingsApi->store_original:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSettingsApi->store_original: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file_if_exist**
> BooleanWrapper update_file_if_exist(settings_request_dto=settings_request_dto)

Updates a file version if a file with such a name already exists.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_request_dto** | [**SettingsRequestDto**](SettingsRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.boolean_wrapper import BooleanWrapper
from docspace-api-sdk.models.settings_request_dto import SettingsRequestDto
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.FilesSettingsApi(api_client)
    settings_request_dto = docspace-api-sdk.SettingsRequestDto() # SettingsRequestDto |  (optional)

    try:
        # Update a file version if it exists
        api_response = api_instance.update_file_if_exist(settings_request_dto=settings_request_dto)
        print("The response of FilesSettingsApi->update_file_if_exist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSettingsApi->update_file_if_exist: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

