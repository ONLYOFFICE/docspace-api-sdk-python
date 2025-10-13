# docspace_api_sdk.SettingsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_access_to_thirdparty**](#change_access_to_thirdparty) | **PUT** /api/2.0/files/thirdparty | 
[**change_automatically_clean_up**](#change_automatically_clean_up) | **PUT** /api/2.0/files/settings/autocleanup | 
[**change_default_access_rights**](#change_default_access_rights) | **PUT** /api/2.0/files/settings/dafaultaccessrights | 
[**change_delete_confirm**](#change_delete_confirm) | **PUT** /api/2.0/files/changedeleteconfrim | 
[**change_download_zip_from_body**](#change_download_zip_from_body) | **PUT** /api/2.0/files/settings/downloadtargz | 
[**check_doc_service_url**](#check_doc_service_url) | **PUT** /api/2.0/files/docservice | 
[**display_file_extension**](#display_file_extension) | **PUT** /api/2.0/files/displayfileextension | 
[**display_recent**](#display_recent) | **PUT** /api/2.0/files/displayrecent | 
[**external_share**](#external_share) | **PUT** /api/2.0/files/settings/external | 
[**external_share_social_media**](#external_share_social_media) | **PUT** /api/2.0/files/settings/externalsocialmedia | 
[**forcesave**](#forcesave) | **PUT** /api/2.0/files/forcesave | 
[**get_automatically_clean_up**](#get_automatically_clean_up) | **GET** /api/2.0/files/settings/autocleanup | 
[**get_doc_service_url**](#get_doc_service_url) | **GET** /api/2.0/files/docservice | 
[**get_files_module**](#get_files_module) | **GET** /api/2.0/files/info | 
[**get_files_settings**](#get_files_settings) | **GET** /api/2.0/files/settings | 
[**hide_confirm_cancel_operation**](#hide_confirm_cancel_operation) | **PUT** /api/2.0/files/hideconfirmcanceloperation | 
[**hide_confirm_convert**](#hide_confirm_convert) | **PUT** /api/2.0/files/hideconfirmconvert | 
[**hide_confirm_room_lifetime**](#hide_confirm_room_lifetime) | **PUT** /api/2.0/files/hideconfirmroomlifetime | 
[**is_available_privacy_room_settings**](#is_available_privacy_room_settings) | **GET** /api/2.0/files/@privacy/available | 
[**keep_new_file_name**](#keep_new_file_name) | **PUT** /api/2.0/files/keepnewfilename | 
[**set_open_editor_in_same_tab**](#set_open_editor_in_same_tab) | **PUT** /api/2.0/files/settings/openeditorinsametab | 
[**store_forcesave**](#store_forcesave) | **PUT** /api/2.0/files/storeforcesave | 
[**store_original**](#store_original) | **PUT** /api/2.0/files/storeoriginal | 
[**update_file_if_exist**](#update_file_if_exist) | **PUT** /api/2.0/files/updateifexist | 


# **change_access_to_thirdparty**
> BooleanWrapper change_access_to_thirdparty(settings_request_dto=settings_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_request_dto** | [**SettingsRequestDto**](SettingsRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.models.settings_request_dto import SettingsRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    settings_request_dto = docspace_api_sdk.SettingsRequestDto() # SettingsRequestDto |  (optional)

    try:
        api_response = api_instance.change_access_to_thirdparty(settings_request_dto=settings_request_dto)
        print("The response of SettingsApi->change_access_to_thirdparty:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->change_access_to_thirdparty: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_automatically_clean_up**
> AutoCleanUpDataWrapper change_automatically_clean_up(auto_cleanup_request_dto=auto_cleanup_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_cleanup_request_dto** | [**AutoCleanupRequestDto**](AutoCleanupRequestDto.md)|  | [optional] 

### Return type

[**AutoCleanUpDataWrapper**](AutoCleanUpDataWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.auto_clean_up_data_wrapper import AutoCleanUpDataWrapper
from docspace_api_sdk.models.auto_cleanup_request_dto import AutoCleanupRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    auto_cleanup_request_dto = docspace_api_sdk.AutoCleanupRequestDto() # AutoCleanupRequestDto |  (optional)

    try:
        api_response = api_instance.change_automatically_clean_up(auto_cleanup_request_dto=auto_cleanup_request_dto)
        print("The response of SettingsApi->change_automatically_clean_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->change_automatically_clean_up: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The auto-clearing setting properties: auto-clearing or not, a time interval when the auto-clearing will be performed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_default_access_rights**
> FileShareArrayWrapper change_default_access_rights(request_body=request_body)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[int]**](int.md)| Sharing rights (None, ReadWrite, Read, Restrict, Varies, Review, Comment, FillForms, CustomFilter, RoomAdmin, Editing, Collaborator). | [optional] 

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
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    request_body = [56] # List[int] | Sharing rights (None, ReadWrite, Read, Restrict, Varies, Review, Comment, FillForms, CustomFilter, RoomAdmin, Editing, Collaborator). (optional)

    try:
        api_response = api_instance.change_default_access_rights(request_body=request_body)
        print("The response of SettingsApi->change_default_access_rights:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->change_default_access_rights: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated sharing rights (None, ReadWrite, Read, Restrict, Varies, Review, Comment, FillForms, CustomFilter, RoomAdmin, Editing, Collaborator) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_delete_confirm**
> BooleanWrapper change_delete_confirm(settings_request_dto=settings_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_request_dto** | [**SettingsRequestDto**](SettingsRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.models.settings_request_dto import SettingsRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    settings_request_dto = docspace_api_sdk.SettingsRequestDto() # SettingsRequestDto |  (optional)

    try:
        api_response = api_instance.change_delete_confirm(settings_request_dto=settings_request_dto)
        print("The response of SettingsApi->change_delete_confirm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->change_delete_confirm: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_download_zip_from_body**
> ICompressWrapper change_download_zip_from_body(display_request_dto=display_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_request_dto** | [**DisplayRequestDto**](DisplayRequestDto.md)|  | [optional] 

### Return type

[**ICompressWrapper**](ICompressWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.display_request_dto import DisplayRequestDto
from docspace_api_sdk.models.i_compress_wrapper import ICompressWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    display_request_dto = docspace_api_sdk.DisplayRequestDto() # DisplayRequestDto |  (optional)

    try:
        api_response = api_instance.change_download_zip_from_body(display_request_dto=display_request_dto)
        print("The response of SettingsApi->change_download_zip_from_body:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->change_download_zip_from_body: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Archive |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_doc_service_url**
> DocServiceUrlWrapper check_doc_service_url(check_doc_service_url_request_dto=check_doc_service_url_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_doc_service_url_request_dto** | [**CheckDocServiceUrlRequestDto**](CheckDocServiceUrlRequestDto.md)|  | [optional] 

### Return type

[**DocServiceUrlWrapper**](DocServiceUrlWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.check_doc_service_url_request_dto import CheckDocServiceUrlRequestDto
from docspace_api_sdk.models.doc_service_url_wrapper import DocServiceUrlWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    check_doc_service_url_request_dto = docspace_api_sdk.CheckDocServiceUrlRequestDto() # CheckDocServiceUrlRequestDto |  (optional)

    try:
        api_response = api_instance.check_doc_service_url(check_doc_service_url_request_dto=check_doc_service_url_request_dto)
        print("The response of SettingsApi->check_doc_service_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->check_doc_service_url: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document service information: the Document Server address, the Document Server address in the local private network, the Community Server address |  -  |
**400** | Invalid input urls/Mixed Active Content is not allowed. HTTPS address for Document Server is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_file_extension**
> BooleanWrapper display_file_extension(settings_request_dto=settings_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_request_dto** | [**SettingsRequestDto**](SettingsRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.models.settings_request_dto import SettingsRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    settings_request_dto = docspace_api_sdk.SettingsRequestDto() # SettingsRequestDto |  (optional)

    try:
        api_response = api_instance.display_file_extension(settings_request_dto=settings_request_dto)
        print("The response of SettingsApi->display_file_extension:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->display_file_extension: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the parameter is enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_recent**
> BooleanWrapper display_recent(display_request_dto=display_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_request_dto** | [**DisplayRequestDto**](DisplayRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.models.display_request_dto import DisplayRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    display_request_dto = docspace_api_sdk.DisplayRequestDto() # DisplayRequestDto |  (optional)

    try:
        api_response = api_instance.display_recent(display_request_dto=display_request_dto)
        print("The response of SettingsApi->display_recent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->display_recent: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the parameter is enabled |  -  |
**403** | You don&#39;t have enough permission to perform the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_share**
> BooleanWrapper external_share(display_request_dto=display_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_request_dto** | [**DisplayRequestDto**](DisplayRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.models.display_request_dto import DisplayRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    display_request_dto = docspace_api_sdk.DisplayRequestDto() # DisplayRequestDto |  (optional)

    try:
        api_response = api_instance.external_share(display_request_dto=display_request_dto)
        print("The response of SettingsApi->external_share:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->external_share: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the parameter is enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_share_social_media**
> BooleanWrapper external_share_social_media(display_request_dto=display_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_request_dto** | [**DisplayRequestDto**](DisplayRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.models.display_request_dto import DisplayRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    display_request_dto = docspace_api_sdk.DisplayRequestDto() # DisplayRequestDto |  (optional)

    try:
        api_response = api_instance.external_share_social_media(display_request_dto=display_request_dto)
        print("The response of SettingsApi->external_share_social_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->external_share_social_media: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the parameter is enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forcesave**
> BooleanWrapper forcesave()



For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

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
    api_instance = docspace_api_sdk.SettingsApi(api_client)

    try:
        api_response = api_instance.forcesave()
        print("The response of SettingsApi->forcesave:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->forcesave: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the parameter is enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_automatically_clean_up**
> AutoCleanUpDataWrapper get_automatically_clean_up()



For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**AutoCleanUpDataWrapper**](AutoCleanUpDataWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.auto_clean_up_data_wrapper import AutoCleanUpDataWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SettingsApi(api_client)

    try:
        api_response = api_instance.get_automatically_clean_up()
        print("The response of SettingsApi->get_automatically_clean_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_automatically_clean_up: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The auto-clearing setting properties: auto-clearing or not, a time interval when the auto-clearing will be performed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_doc_service_url**
> DocServiceUrlWrapper get_doc_service_url(version=version)



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
import docspace_api_sdk
from docspace_api_sdk.models.doc_service_url_wrapper import DocServiceUrlWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    version = true # bool | Specifies whether to return the editor version or not. (optional)

    try:
        api_response = api_instance.get_doc_service_url(version=version)
        print("The response of SettingsApi->get_doc_service_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_doc_service_url: %s\n" % e)
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



For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**ModuleWrapper**](ModuleWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.module_wrapper import ModuleWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SettingsApi(api_client)

    try:
        api_response = api_instance.get_files_module()
        print("The response of SettingsApi->get_files_module:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_files_module: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Module information: ID, product class name, title, description, icon URL, large icon URL, start URL, primary or nor, help URL |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files_settings**
> FilesSettingsWrapper get_files_settings()



For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**FilesSettingsWrapper**](FilesSettingsWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.files_settings_wrapper import FilesSettingsWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SettingsApi(api_client)

    try:
        api_response = api_instance.get_files_settings()
        print("The response of SettingsApi->get_files_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_files_settings: %s\n" % e)
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



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_request_dto** | [**SettingsRequestDto**](SettingsRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.models.settings_request_dto import SettingsRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    settings_request_dto = docspace_api_sdk.SettingsRequestDto() # SettingsRequestDto |  (optional)

    try:
        api_response = api_instance.hide_confirm_cancel_operation(settings_request_dto=settings_request_dto)
        print("The response of SettingsApi->hide_confirm_cancel_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->hide_confirm_cancel_operation: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the parameter is enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hide_confirm_convert**
> ModuleWrapper hide_confirm_convert(hide_confirm_convert_request_dto=hide_confirm_convert_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hide_confirm_convert_request_dto** | [**HideConfirmConvertRequestDto**](HideConfirmConvertRequestDto.md)|  | [optional] 

### Return type

[**ModuleWrapper**](ModuleWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.hide_confirm_convert_request_dto import HideConfirmConvertRequestDto
from docspace_api_sdk.models.module_wrapper import ModuleWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    hide_confirm_convert_request_dto = docspace_api_sdk.HideConfirmConvertRequestDto() # HideConfirmConvertRequestDto |  (optional)

    try:
        api_response = api_instance.hide_confirm_convert(hide_confirm_convert_request_dto=hide_confirm_convert_request_dto)
        print("The response of SettingsApi->hide_confirm_convert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->hide_confirm_convert: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hide_confirm_room_lifetime**
> BooleanWrapper hide_confirm_room_lifetime(settings_request_dto=settings_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_request_dto** | [**SettingsRequestDto**](SettingsRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.models.settings_request_dto import SettingsRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    settings_request_dto = docspace_api_sdk.SettingsRequestDto() # SettingsRequestDto |  (optional)

    try:
        api_response = api_instance.hide_confirm_room_lifetime(settings_request_dto=settings_request_dto)
        print("The response of SettingsApi->hide_confirm_room_lifetime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->hide_confirm_room_lifetime: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the parameter is enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_available_privacy_room_settings**
> BooleanWrapper is_available_privacy_room_settings()



For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

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
    api_instance = docspace_api_sdk.SettingsApi(api_client)

    try:
        api_response = api_instance.is_available_privacy_room_settings()
        print("The response of SettingsApi->is_available_privacy_room_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->is_available_privacy_room_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the Private Room settings are available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keep_new_file_name**
> BooleanWrapper keep_new_file_name(settings_request_dto=settings_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_request_dto** | [**SettingsRequestDto**](SettingsRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.models.settings_request_dto import SettingsRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    settings_request_dto = docspace_api_sdk.SettingsRequestDto() # SettingsRequestDto |  (optional)

    try:
        api_response = api_instance.keep_new_file_name(settings_request_dto=settings_request_dto)
        print("The response of SettingsApi->keep_new_file_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->keep_new_file_name: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_open_editor_in_same_tab**
> BooleanWrapper set_open_editor_in_same_tab(settings_request_dto=settings_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_request_dto** | [**SettingsRequestDto**](SettingsRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.models.settings_request_dto import SettingsRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    settings_request_dto = docspace_api_sdk.SettingsRequestDto() # SettingsRequestDto |  (optional)

    try:
        api_response = api_instance.set_open_editor_in_same_tab(settings_request_dto=settings_request_dto)
        print("The response of SettingsApi->set_open_editor_in_same_tab:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->set_open_editor_in_same_tab: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the parameter is enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_forcesave**
> BooleanWrapper store_forcesave()



For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

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
    api_instance = docspace_api_sdk.SettingsApi(api_client)

    try:
        api_response = api_instance.store_forcesave()
        print("The response of SettingsApi->store_forcesave:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->store_forcesave: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_original**
> BooleanWrapper store_original(settings_request_dto=settings_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_request_dto** | [**SettingsRequestDto**](SettingsRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.models.settings_request_dto import SettingsRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    settings_request_dto = docspace_api_sdk.SettingsRequestDto() # SettingsRequestDto |  (optional)

    try:
        api_response = api_instance.store_original(settings_request_dto=settings_request_dto)
        print("The response of SettingsApi->store_original:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->store_original: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file_if_exist**
> BooleanWrapper update_file_if_exist(settings_request_dto=settings_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_request_dto** | [**SettingsRequestDto**](SettingsRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.models.settings_request_dto import SettingsRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    settings_request_dto = docspace_api_sdk.SettingsRequestDto() # SettingsRequestDto |  (optional)

    try:
        api_response = api_instance.update_file_if_exist(settings_request_dto=settings_request_dto)
        print("The response of SettingsApi->update_file_if_exist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->update_file_if_exist: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

