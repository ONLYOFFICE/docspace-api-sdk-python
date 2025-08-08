# docspace_api_sdk.RoomsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_room_tags**](#add_room_tags) | **PUT** /api/2.0/files/rooms/{id}/tags | 
[**archive_room**](#archive_room) | **PUT** /api/2.0/files/rooms/{id}/archive | 
[**change_room_cover**](#change_room_cover) | **POST** /api/2.0/files/rooms/{id}/cover | 
[**create_room**](#create_room) | **POST** /api/2.0/files/rooms | 
[**create_room_from_template**](#create_room_from_template) | **POST** /api/2.0/files/rooms/fromtemplate | 
[**create_room_logo**](#create_room_logo) | **POST** /api/2.0/files/rooms/{id}/logo | 
[**create_room_tag**](#create_room_tag) | **POST** /api/2.0/files/tags | 
[**create_room_template**](#create_room_template) | **POST** /api/2.0/files/roomtemplate | 
[**create_room_third_party**](#create_room_third_party) | **POST** /api/2.0/files/rooms/thirdparty/{id} | 
[**delete_custom_tags**](#delete_custom_tags) | **DELETE** /api/2.0/files/tags | 
[**delete_room**](#delete_room) | **DELETE** /api/2.0/files/rooms/{id} | 
[**delete_room_logo**](#delete_room_logo) | **DELETE** /api/2.0/files/rooms/{id}/logo | 
[**delete_room_tags**](#delete_room_tags) | **DELETE** /api/2.0/files/rooms/{id}/tags | 
[**get_new_room_items**](#get_new_room_items) | **GET** /api/2.0/files/rooms/{id}/news | 
[**get_public_settings**](#get_public_settings) | **GET** /api/2.0/files/roomtemplate/{id}/public | 
[**get_room_covers**](#get_room_covers) | **GET** /api/2.0/files/rooms/covers | 
[**get_room_creating_status**](#get_room_creating_status) | **GET** /api/2.0/files/rooms/fromtemplate/status | 
[**get_room_index_export**](#get_room_index_export) | **GET** /api/2.0/files/rooms/indexexport | 
[**get_room_info**](#get_room_info) | **GET** /api/2.0/files/rooms/{id} | 
[**get_room_links**](#get_room_links) | **GET** /api/2.0/files/rooms/{id}/links | 
[**get_room_security_info**](#get_room_security_info) | **GET** /api/2.0/files/rooms/{id}/share | 
[**get_room_tags_info**](#get_room_tags_info) | **GET** /api/2.0/files/tags | 
[**get_room_template_creating_status**](#get_room_template_creating_status) | **GET** /api/2.0/files/roomtemplate/status | 
[**get_rooms_folder**](#get_rooms_folder) | **GET** /api/2.0/files/rooms | 
[**get_rooms_new_items**](#get_rooms_new_items) | **GET** /api/2.0/files/rooms/news | 
[**get_rooms_primary_external_link**](#get_rooms_primary_external_link) | **GET** /api/2.0/files/rooms/{id}/link | 
[**pin_room**](#pin_room) | **PUT** /api/2.0/files/rooms/{id}/pin | 
[**reorder_room**](#reorder_room) | **PUT** /api/2.0/files/rooms/{id}/reorder | 
[**resend_email_invitations**](#resend_email_invitations) | **POST** /api/2.0/files/rooms/{id}/resend | 
[**set_public_settings**](#set_public_settings) | **PUT** /api/2.0/files/roomtemplate/public | 
[**set_room_link**](#set_room_link) | **PUT** /api/2.0/files/rooms/{id}/links | 
[**set_room_security**](#set_room_security) | **PUT** /api/2.0/files/rooms/{id}/share | 
[**start_room_index_export**](#start_room_index_export) | **POST** /api/2.0/files/rooms/{id}/indexexport | 
[**terminate_room_index_export**](#terminate_room_index_export) | **DELETE** /api/2.0/files/rooms/indexexport | 
[**unarchive_room**](#unarchive_room) | **PUT** /api/2.0/files/rooms/{id}/unarchive | 
[**unpin_room**](#unpin_room) | **PUT** /api/2.0/files/rooms/{id}/unpin | 
[**update_room**](#update_room) | **PUT** /api/2.0/files/rooms/{id} | 
[**upload_room_logo**](#upload_room_logo) | **POST** /api/2.0/files/logos | 


# **add_room_tags**
> FolderIntegerWrapper add_room_tags(id, batch_tags_request_dto=batch_tags_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room Id. | 
 **batch_tags_request_dto** | [**BatchTagsRequestDto**](BatchTagsRequestDto.md)| The parameters for adding tags. | [optional] 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.batch_tags_request_dto import BatchTagsRequestDto
from docspace_api_sdk.models.folder_integer_wrapper import FolderIntegerWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    id = 9846 # int | The room Id.
    batch_tags_request_dto = docspace_api_sdk.BatchTagsRequestDto() # BatchTagsRequestDto | The parameters for adding tags. (optional)

    try:
        api_response = api_instance.add_room_tags(id, batch_tags_request_dto=batch_tags_request_dto)
        print("The response of RoomsApi->add_room_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->add_room_tags: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room information |  -  |
**403** | You don&#39;t have permission to edit the room |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_room**
> FileOperationWrapper archive_room(id, archive_room_request=archive_room_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room ID. | 
 **archive_room_request** | [**ArchiveRoomRequest**](ArchiveRoomRequest.md)| The parameters for archiving a room. | [optional] 

### Return type

[**FileOperationWrapper**](FileOperationWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.archive_room_request import ArchiveRoomRequest
from docspace_api_sdk.models.file_operation_wrapper import FileOperationWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    id = 9846 # int | The room ID.
    archive_room_request = docspace_api_sdk.ArchiveRoomRequest() # ArchiveRoomRequest | The parameters for archiving a room. (optional)

    try:
        api_response = api_instance.archive_room(id, archive_room_request=archive_room_request)
        print("The response of RoomsApi->archive_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->archive_room: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_room_cover**
> FolderIntegerWrapper change_room_cover(id, cover_request_dto=cover_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room ID. | 
 **cover_request_dto** | [**CoverRequestDto**](CoverRequestDto.md)| The request parameters to change the room cover. | [optional] 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.cover_request_dto import CoverRequestDto
from docspace_api_sdk.models.folder_integer_wrapper import FolderIntegerWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    id = 9846 # int | The room ID.
    cover_request_dto = docspace_api_sdk.CoverRequestDto() # CoverRequestDto | The request parameters to change the room cover. (optional)

    try:
        api_response = api_instance.change_room_cover(id, cover_request_dto=cover_request_dto)
        print("The response of RoomsApi->change_room_cover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->change_room_cover: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room cover |  -  |
**403** | You don&#39;t have permission to change cover |  -  |
**404** | The required room was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_room**
> FolderIntegerWrapper create_room(create_room_request_dto=create_room_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_room_request_dto** | [**CreateRoomRequestDto**](CreateRoomRequestDto.md)|  | [optional] 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.create_room_request_dto import CreateRoomRequestDto
from docspace_api_sdk.models.folder_integer_wrapper import FolderIntegerWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    create_room_request_dto = docspace_api_sdk.CreateRoomRequestDto() # CreateRoomRequestDto |  (optional)

    try:
        api_response = api_instance.create_room(create_room_request_dto=create_room_request_dto)
        print("The response of RoomsApi->create_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->create_room: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_room_from_template**
> RoomFromTemplateStatusWrapper create_room_from_template(create_room_from_template_dto=create_room_from_template_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_room_from_template_dto** | [**CreateRoomFromTemplateDto**](CreateRoomFromTemplateDto.md)|  | [optional] 

### Return type

[**RoomFromTemplateStatusWrapper**](RoomFromTemplateStatusWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.create_room_from_template_dto import CreateRoomFromTemplateDto
from docspace_api_sdk.models.room_from_template_status_wrapper import RoomFromTemplateStatusWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    create_room_from_template_dto = docspace_api_sdk.CreateRoomFromTemplateDto() # CreateRoomFromTemplateDto |  (optional)

    try:
        api_response = api_instance.create_room_from_template(create_room_from_template_dto=create_room_from_template_dto)
        print("The response of RoomsApi->create_room_from_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->create_room_from_template: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_room_logo**
> FolderIntegerWrapper create_room_logo(id, logo_request=logo_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room ID. | 
 **logo_request** | [**LogoRequest**](LogoRequest.md)| The logo request parameters. | [optional] 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.folder_integer_wrapper import FolderIntegerWrapper
from docspace_api_sdk.models.logo_request import LogoRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    id = 9846 # int | The room ID.
    logo_request = docspace_api_sdk.LogoRequest() # LogoRequest | The logo request parameters. (optional)

    try:
        api_response = api_instance.create_room_logo(id, logo_request=logo_request)
        print("The response of RoomsApi->create_room_logo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->create_room_logo: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room information |  -  |
**404** | The required room was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_room_tag**
> ObjectWrapper create_room_tag(create_tag_request_dto=create_tag_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tag_request_dto** | [**CreateTagRequestDto**](CreateTagRequestDto.md)|  | [optional] 

### Return type

[**ObjectWrapper**](ObjectWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.create_tag_request_dto import CreateTagRequestDto
from docspace_api_sdk.models.object_wrapper import ObjectWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    create_tag_request_dto = docspace_api_sdk.CreateTagRequestDto() # CreateTagRequestDto |  (optional)

    try:
        api_response = api_instance.create_room_tag(create_tag_request_dto=create_tag_request_dto)
        print("The response of RoomsApi->create_room_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->create_room_tag: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New tag name |  -  |
**403** | You don&#39;t have enough permission to perform the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_room_template**
> RoomTemplateStatusWrapper create_room_template(room_template_dto=room_template_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_template_dto** | [**RoomTemplateDto**](RoomTemplateDto.md)|  | [optional] 

### Return type

[**RoomTemplateStatusWrapper**](RoomTemplateStatusWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.room_template_dto import RoomTemplateDto
from docspace_api_sdk.models.room_template_status_wrapper import RoomTemplateStatusWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    room_template_dto = docspace_api_sdk.RoomTemplateDto() # RoomTemplateDto |  (optional)

    try:
        api_response = api_instance.create_room_template(room_template_dto=room_template_dto)
        print("The response of RoomsApi->create_room_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->create_room_template: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_room_third_party**
> FolderStringWrapper create_room_third_party(id, create_third_party_room=create_third_party_room)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the folder in the third-party storage in which the contents of the room will be stored. | 
 **create_third_party_room** | [**CreateThirdPartyRoom**](CreateThirdPartyRoom.md)| The third-party room information. | [optional] 

### Return type

[**FolderStringWrapper**](FolderStringWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.create_third_party_room import CreateThirdPartyRoom
from docspace_api_sdk.models.folder_string_wrapper import FolderStringWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    id = '9846' # str | The ID of the folder in the third-party storage in which the contents of the room will be stored.
    create_third_party_room = docspace_api_sdk.CreateThirdPartyRoom() # CreateThirdPartyRoom | The third-party room information. (optional)

    try:
        api_response = api_instance.create_room_third_party(id, create_third_party_room=create_third_party_room)
        print("The response of RoomsApi->create_room_third_party:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->create_room_third_party: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_tags**
> delete_custom_tags(batch_tags_request_dto=batch_tags_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_tags_request_dto** | [**BatchTagsRequestDto**](BatchTagsRequestDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.batch_tags_request_dto import BatchTagsRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    batch_tags_request_dto = docspace_api_sdk.BatchTagsRequestDto() # BatchTagsRequestDto |  (optional)

    try:
        api_instance.delete_custom_tags(batch_tags_request_dto=batch_tags_request_dto)
    except Exception as e:
        print("Exception when calling RoomsApi->delete_custom_tags: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**403** | You don&#39;t have enough permission to perform the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_room**
> FileOperationWrapper delete_room(id, delete_room_request=delete_room_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room ID. | 
 **delete_room_request** | [**DeleteRoomRequest**](DeleteRoomRequest.md)| The parameters for deleting a room. | [optional] 

### Return type

[**FileOperationWrapper**](FileOperationWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.delete_room_request import DeleteRoomRequest
from docspace_api_sdk.models.file_operation_wrapper import FileOperationWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    id = 9846 # int | The room ID.
    delete_room_request = docspace_api_sdk.DeleteRoomRequest() # DeleteRoomRequest | The parameters for deleting a room. (optional)

    try:
        api_response = api_instance.delete_room(id, delete_room_request=delete_room_request)
        print("The response of RoomsApi->delete_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->delete_room: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_room_logo**
> FolderIntegerWrapper delete_room_logo(id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room ID of the request. | 

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
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    id = 9846 # int | The room ID of the request.

    try:
        api_response = api_instance.delete_room_logo(id)
        print("The response of RoomsApi->delete_room_logo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->delete_room_logo: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_room_tags**
> FolderIntegerWrapper delete_room_tags(id, batch_tags_request_dto=batch_tags_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room Id. | 
 **batch_tags_request_dto** | [**BatchTagsRequestDto**](BatchTagsRequestDto.md)| The parameters for adding tags. | [optional] 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.batch_tags_request_dto import BatchTagsRequestDto
from docspace_api_sdk.models.folder_integer_wrapper import FolderIntegerWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    id = 9846 # int | The room Id.
    batch_tags_request_dto = docspace_api_sdk.BatchTagsRequestDto() # BatchTagsRequestDto | The parameters for adding tags. (optional)

    try:
        api_response = api_instance.delete_room_tags(id, batch_tags_request_dto=batch_tags_request_dto)
        print("The response of RoomsApi->delete_room_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->delete_room_tags: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room information |  -  |
**403** | You don&#39;t have permission to edit the room |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_new_room_items**
> NewItemsFileEntryBaseArrayWrapper get_new_room_items(id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room ID of the request. | 

### Return type

[**NewItemsFileEntryBaseArrayWrapper**](NewItemsFileEntryBaseArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.new_items_file_entry_base_array_wrapper import NewItemsFileEntryBaseArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    id = 9846 # int | The room ID of the request.

    try:
        api_response = api_instance.get_new_room_items(id)
        print("The response of RoomsApi->get_new_room_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->get_new_room_items: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file entry information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_settings**
> BooleanWrapper get_public_settings(id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room template ID. | 

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
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    id = 9846 # int | The room template ID.

    try:
        api_response = api_instance.get_public_settings(id)
        print("The response of RoomsApi->get_public_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->get_public_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_room_covers**
> CoversResultArrayWrapper get_room_covers()



For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**CoversResultArrayWrapper**](CoversResultArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.covers_result_array_wrapper import CoversResultArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)

    try:
        api_response = api_instance.get_room_covers()
        print("The response of RoomsApi->get_room_covers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->get_room_covers: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets room cover |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_room_creating_status**
> RoomFromTemplateStatusWrapper get_room_creating_status()



For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**RoomFromTemplateStatusWrapper**](RoomFromTemplateStatusWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.room_from_template_status_wrapper import RoomFromTemplateStatusWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)

    try:
        api_response = api_instance.get_room_creating_status()
        print("The response of RoomsApi->get_room_creating_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->get_room_creating_status: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_room_index_export**
> DocumentBuilderTaskWrapper get_room_index_export()



For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**DocumentBuilderTaskWrapper**](DocumentBuilderTaskWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.document_builder_task_wrapper import DocumentBuilderTaskWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)

    try:
        api_response = api_instance.get_room_index_export()
        print("The response of RoomsApi->get_room_index_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->get_room_index_export: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_room_info**
> FolderIntegerWrapper get_room_info(id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room ID of the request. | 

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
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    id = 9846 # int | The room ID of the request.

    try:
        api_response = api_instance.get_room_info(id)
        print("The response of RoomsApi->get_room_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->get_room_info: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_room_links**
> FileShareArrayWrapper get_room_links(id, type=type)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room ID. | 
 **type** | [**LinkType**](.md)| The link type. | [optional] 

### Return type

[**FileShareArrayWrapper**](FileShareArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_share_array_wrapper import FileShareArrayWrapper
from docspace_api_sdk.models.link_type import LinkType
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    id = 9846 # int | The room ID.
    type = docspace_api_sdk.LinkType() # LinkType | The link type. (optional)

    try:
        api_response = api_instance.get_room_links(id, type=type)
        print("The response of RoomsApi->get_room_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->get_room_links: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room security information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_room_security_info**
> FileShareArrayWrapper get_room_security_info(id, filter_type=filter_type, count=count, start_index=start_index, filter_value=filter_value)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room ID. | 
 **filter_type** | [**ShareFilterType**](.md)| The filter type of the access rights. | [optional] 
 **count** | **int**| The number of items to be retrieved or processed. | [optional] 
 **start_index** | **int**| The starting index of the items to retrieve in a paginated request. | [optional] 
 **filter_value** | **str**| The text filter value used for filtering room security information. | [optional] 

### Return type

[**FileShareArrayWrapper**](FileShareArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_share_array_wrapper import FileShareArrayWrapper
from docspace_api_sdk.models.share_filter_type import ShareFilterType
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    id = 9846 # int | The room ID.
    filter_type = docspace_api_sdk.ShareFilterType() # ShareFilterType | The filter type of the access rights. (optional)
    count = 1234 # int | The number of items to be retrieved or processed. (optional)
    start_index = 1234 # int | The starting index of the items to retrieve in a paginated request. (optional)
    filter_value = 'some text' # str | The text filter value used for filtering room security information. (optional)

    try:
        api_response = api_instance.get_room_security_info(id, filter_type=filter_type, count=count, start_index=start_index, filter_value=filter_value)
        print("The response of RoomsApi->get_room_security_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->get_room_security_info: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Security information of room files |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_room_tags_info**
> ObjectArrayWrapper get_room_tags_info(count=count, start_index=start_index, filter_value=filter_value, fields=fields)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| Gets or sets the number of tag results to retrieve.  This property specifies the maximum amount of tag data to be included in the result set. | [optional] 
 **start_index** | **int**| Represents the starting index from which the tags&#39; information will be retrieved.  This property is used to define the offset for pagination when retrieving a list of tags. It determines  the point in the data set from which the retrieval begins. | [optional] 
 **filter_value** | **str**| Gets or sets the text value used for searching tags.  This property is typically used as a filter value when retrieving tag information. | [optional] 
 **fields** | **string**| Comma-separated list of fields to include in the response | [optional] 

### Return type

[**ObjectArrayWrapper**](ObjectArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.object_array_wrapper import ObjectArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    count = 1234 # int | Gets or sets the number of tag results to retrieve.  This property specifies the maximum amount of tag data to be included in the result set. (optional)
    start_index = 1234 # int | Represents the starting index from which the tags' information will be retrieved.  This property is used to define the offset for pagination when retrieving a list of tags. It determines  the point in the data set from which the retrieval begins. (optional)
    filter_value = 'some text' # str | Gets or sets the text value used for searching tags.  This property is typically used as a filter value when retrieving tag information. (optional)
    fields =  # string | Comma-separated list of fields to include in the response (optional)

    try:
        api_response = api_instance.get_room_tags_info(count=count, start_index=start_index, filter_value=filter_value, fields=fields)
        print("The response of RoomsApi->get_room_tags_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->get_room_tags_info: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tag names |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_room_template_creating_status**
> RoomTemplateStatusWrapper get_room_template_creating_status()



For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**RoomTemplateStatusWrapper**](RoomTemplateStatusWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.room_template_status_wrapper import RoomTemplateStatusWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)

    try:
        api_response = api_instance.get_room_template_creating_status()
        print("The response of RoomsApi->get_room_template_creating_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->get_room_template_creating_status: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rooms_folder**
> FolderContentIntegerWrapper get_rooms_folder(type=type, subject_id=subject_id, search_area=search_area, without_tags=without_tags, tags=tags, exclude_subject=exclude_subject, provider=provider, subject_filter=subject_filter, quota_filter=quota_filter, storage_filter=storage_filter, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value, fields=fields)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**List[RoomType]**](RoomType.md)| The filter by room type. | [optional] 
 **subject_id** | **str**| The filter by user ID. | [optional] 
 **search_area** | [**SearchArea**](.md)| The room search area (Active, Archive, Any, Recent by links). | [optional] 
 **without_tags** | **bool**| Specifies whether to search by tags or not. | [optional] 
 **tags** | **str**| The tags in the serialized format. | [optional] 
 **exclude_subject** | **bool**| Specifies whether to exclude search by user or group ID. | [optional] 
 **provider** | [**ProviderFilter**](.md)| The filter by provider name (None, Box, DropBox, GoogleDrive, kDrive, OneDrive, SharePoint, WebDav, Yandex, Storage). | [optional] 
 **subject_filter** | [**SubjectFilter**](.md)| The filter by user (Owner - 0, Member - 1). | [optional] 
 **quota_filter** | [**QuotaFilter**](.md)| The filter by quota (All - 0, Default - 1, Custom - 2). | [optional] 
 **storage_filter** | [**StorageFilter**](.md)| The filter by storage (None - 0, Internal - 1, ThirdParty - 2). | [optional] 
 **count** | **int**| Specifies the maximum number of items to retrieve. | [optional] 
 **start_index** | **int**| The index from which to start retrieving the room content. | [optional] 
 **sort_by** | **str**| Specifies the field by which the room content should be sorted. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The order in which the results are sorted. | [optional] 
 **filter_value** | **str**| The text filter value used to refine search or query operations. | [optional] 
 **fields** | **string**| Comma-separated list of fields to include in the response | [optional] 

### Return type

[**FolderContentIntegerWrapper**](FolderContentIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.folder_content_integer_wrapper import FolderContentIntegerWrapper
from docspace_api_sdk.models.provider_filter import ProviderFilter
from docspace_api_sdk.models.quota_filter import QuotaFilter
from docspace_api_sdk.models.room_type import RoomType
from docspace_api_sdk.models.search_area import SearchArea
from docspace_api_sdk.models.sort_order import SortOrder
from docspace_api_sdk.models.storage_filter import StorageFilter
from docspace_api_sdk.models.subject_filter import SubjectFilter
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    type = [docspace_api_sdk.RoomType()] # List[RoomType] | The filter by room type. (optional)
    subject_id = 'some text' # str | The filter by user ID. (optional)
    search_area = docspace_api_sdk.SearchArea() # SearchArea | The room search area (Active, Archive, Any, Recent by links). (optional)
    without_tags = true # bool | Specifies whether to search by tags or not. (optional)
    tags = 'some text' # str | The tags in the serialized format. (optional)
    exclude_subject = true # bool | Specifies whether to exclude search by user or group ID. (optional)
    provider = docspace_api_sdk.ProviderFilter() # ProviderFilter | The filter by provider name (None, Box, DropBox, GoogleDrive, kDrive, OneDrive, SharePoint, WebDav, Yandex, Storage). (optional)
    subject_filter = docspace_api_sdk.SubjectFilter() # SubjectFilter | The filter by user (Owner - 0, Member - 1). (optional)
    quota_filter = docspace_api_sdk.QuotaFilter() # QuotaFilter | The filter by quota (All - 0, Default - 1, Custom - 2). (optional)
    storage_filter = docspace_api_sdk.StorageFilter() # StorageFilter | The filter by storage (None - 0, Internal - 1, ThirdParty - 2). (optional)
    count = 1234 # int | Specifies the maximum number of items to retrieve. (optional)
    start_index = 1234 # int | The index from which to start retrieving the room content. (optional)
    sort_by = 'some text' # str | Specifies the field by which the room content should be sorted. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_value = 'some text' # str | The text filter value used to refine search or query operations. (optional)
    fields =  # string | Comma-separated list of fields to include in the response (optional)

    try:
        api_response = api_instance.get_rooms_folder(type=type, subject_id=subject_id, search_area=search_area, without_tags=without_tags, tags=tags, exclude_subject=exclude_subject, provider=provider, subject_filter=subject_filter, quota_filter=quota_filter, storage_filter=storage_filter, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value, fields=fields)
        print("The response of RoomsApi->get_rooms_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->get_rooms_folder: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the contents of the \&quot;Rooms\&quot; section |  -  |
**403** | You don&#39;t have enough permission to view the room content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rooms_new_items**
> NewItemsRoomNewItemsArrayWrapper get_rooms_new_items()



For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**NewItemsRoomNewItemsArrayWrapper**](NewItemsRoomNewItemsArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.new_items_room_new_items_array_wrapper import NewItemsRoomNewItemsArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)

    try:
        api_response = api_instance.get_rooms_new_items()
        print("The response of RoomsApi->get_rooms_new_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->get_rooms_new_items: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of new items |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rooms_primary_external_link**
> FileShareWrapper get_rooms_primary_external_link(id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room ID of the request. | 

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
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    id = 9846 # int | The room ID of the request.

    try:
        api_response = api_instance.get_rooms_primary_external_link(id)
        print("The response of RoomsApi->get_rooms_primary_external_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->get_rooms_primary_external_link: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room security information |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pin_room**
> FolderIntegerWrapper pin_room(id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room ID of the request. | 

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
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    id = 9846 # int | The room ID of the request.

    try:
        api_response = api_instance.pin_room(id)
        print("The response of RoomsApi->pin_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->pin_room: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reorder_room**
> FolderIntegerWrapper reorder_room(id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room ID of the request. | 

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
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    id = 9846 # int | The room ID of the request.

    try:
        api_response = api_instance.reorder_room(id)
        print("The response of RoomsApi->reorder_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->reorder_room: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_email_invitations**
> resend_email_invitations(id, user_invitation=user_invitation)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room ID. | 
 **user_invitation** | [**UserInvitation**](UserInvitation.md)| The user invitation parameters. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.user_invitation import UserInvitation
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    id = 9846 # int | The room ID.
    user_invitation = docspace_api_sdk.UserInvitation() # UserInvitation | The user invitation parameters. (optional)

    try:
        api_instance.resend_email_invitations(id, user_invitation=user_invitation)
    except Exception as e:
        print("Exception when calling RoomsApi->resend_email_invitations: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_public_settings**
> set_public_settings(set_public_dto=set_public_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_public_dto** | [**SetPublicDto**](SetPublicDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.set_public_dto import SetPublicDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    set_public_dto = docspace_api_sdk.SetPublicDto() # SetPublicDto |  (optional)

    try:
        api_instance.set_public_settings(set_public_dto=set_public_dto)
    except Exception as e:
        print("Exception when calling RoomsApi->set_public_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_room_link**
> FileShareWrapper set_room_link(id, room_link_request=room_link_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room ID. | 
 **room_link_request** | [**RoomLinkRequest**](RoomLinkRequest.md)| The room link parameters. | [optional] 

### Return type

[**FileShareWrapper**](FileShareWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_share_wrapper import FileShareWrapper
from docspace_api_sdk.models.room_link_request import RoomLinkRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    id = 9846 # int | The room ID.
    room_link_request = docspace_api_sdk.RoomLinkRequest() # RoomLinkRequest | The room link parameters. (optional)

    try:
        api_response = api_instance.set_room_link(id, room_link_request=room_link_request)
        print("The response of RoomsApi->set_room_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->set_room_link: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room security information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_room_security**
> RoomSecurityWrapper set_room_security(id, room_invitation_request=room_invitation_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room ID. | 
 **room_invitation_request** | [**RoomInvitationRequest**](RoomInvitationRequest.md)| The room invitation request. | [optional] 

### Return type

[**RoomSecurityWrapper**](RoomSecurityWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.room_invitation_request import RoomInvitationRequest
from docspace_api_sdk.models.room_security_wrapper import RoomSecurityWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    id = 9846 # int | The room ID.
    room_invitation_request = docspace_api_sdk.RoomInvitationRequest() # RoomInvitationRequest | The room invitation request. (optional)

    try:
        api_response = api_instance.set_room_security(id, room_invitation_request=room_invitation_request)
        print("The response of RoomsApi->set_room_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->set_room_security: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room security information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_room_index_export**
> DocumentBuilderTaskWrapper start_room_index_export(id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room ID of the request. | 

### Return type

[**DocumentBuilderTaskWrapper**](DocumentBuilderTaskWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.document_builder_task_wrapper import DocumentBuilderTaskWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    id = 9846 # int | The room ID of the request.

    try:
        api_response = api_instance.start_room_index_export(id)
        print("The response of RoomsApi->start_room_index_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->start_room_index_export: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**501** | Folder indexing is turned off |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_room_index_export**
> terminate_room_index_export()



For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)

    try:
        api_instance.terminate_room_index_export()
    except Exception as e:
        print("Exception when calling RoomsApi->terminate_room_index_export: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unarchive_room**
> FileOperationWrapper unarchive_room(id, archive_room_request=archive_room_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room ID. | 
 **archive_room_request** | [**ArchiveRoomRequest**](ArchiveRoomRequest.md)| The parameters for archiving a room. | [optional] 

### Return type

[**FileOperationWrapper**](FileOperationWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.archive_room_request import ArchiveRoomRequest
from docspace_api_sdk.models.file_operation_wrapper import FileOperationWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    id = 9846 # int | The room ID.
    archive_room_request = docspace_api_sdk.ArchiveRoomRequest() # ArchiveRoomRequest | The parameters for archiving a room. (optional)

    try:
        api_response = api_instance.unarchive_room(id, archive_room_request=archive_room_request)
        print("The response of RoomsApi->unarchive_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->unarchive_room: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpin_room**
> FolderIntegerWrapper unpin_room(id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room ID of the request. | 

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
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    id = 9846 # int | The room ID of the request.

    try:
        api_response = api_instance.unpin_room(id)
        print("The response of RoomsApi->unpin_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->unpin_room: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_room**
> FolderIntegerWrapper update_room(id, update_room_request=update_room_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room ID. | 
 **update_room_request** | [**UpdateRoomRequest**](UpdateRoomRequest.md)| The request parameters for updating a room. | [optional] 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.folder_integer_wrapper import FolderIntegerWrapper
from docspace_api_sdk.models.update_room_request import UpdateRoomRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    id = 9846 # int | The room ID.
    update_room_request = docspace_api_sdk.UpdateRoomRequest() # UpdateRoomRequest | The request parameters for updating a room. (optional)

    try:
        api_response = api_instance.update_room(id, update_room_request=update_room_request)
        print("The response of RoomsApi->update_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->update_room: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated room information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_room_logo**
> UploadResultWrapper upload_room_logo(form_collection=form_collection)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_collection** | [**List[KeyValuePairStringStringValues]**](KeyValuePairStringStringValues.md)| The image data. | [optional] 

### Return type

[**UploadResultWrapper**](UploadResultWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.key_value_pair_string_string_values import KeyValuePairStringStringValues
from docspace_api_sdk.models.upload_result_wrapper import UploadResultWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.RoomsApi(api_client)
    form_collection = [docspace_api_sdk.KeyValuePairStringStringValues()] # List[KeyValuePairStringStringValues] | The image data. (optional)

    try:
        api_response = api_instance.upload_room_logo(form_collection=form_collection)
        print("The response of RoomsApi->upload_room_logo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->upload_room_logo: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upload result |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

