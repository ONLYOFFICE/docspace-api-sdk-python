# docspace.FilesRoomsApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_tags**](FilesRoomsApi.md#add_tags) | **PUT** /api/2.0/files/rooms/{id}/tags | Add room tags
[**archive_room**](FilesRoomsApi.md#archive_room) | **PUT** /api/2.0/files/rooms/{id}/archive | Archive a room
[**change_room_cover**](FilesRoomsApi.md#change_room_cover) | **POST** /api/2.0/files/rooms/{id}/cover | Changes room cover
[**create_room**](FilesRoomsApi.md#create_room) | **POST** /api/2.0/files/rooms | Create a room
[**create_room_from_template**](FilesRoomsApi.md#create_room_from_template) | **POST** /api/2.0/files/rooms/fromtemplate | Start create a room based on a template
[**create_room_logo**](FilesRoomsApi.md#create_room_logo) | **POST** /api/2.0/files/rooms/{id}/logo | Create a room logo
[**create_room_third_party**](FilesRoomsApi.md#create_room_third_party) | **POST** /api/2.0/files/rooms/thirdparty/{id} | Create a third-party room
[**create_tag**](FilesRoomsApi.md#create_tag) | **POST** /api/2.0/files/tags | Create a tag
[**create_template**](FilesRoomsApi.md#create_template) | **POST** /api/2.0/files/roomtemplate | Start create room template
[**delete_custom_tags**](FilesRoomsApi.md#delete_custom_tags) | **DELETE** /api/2.0/files/tags | Delete tags
[**delete_room**](FilesRoomsApi.md#delete_room) | **DELETE** /api/2.0/files/rooms/{id} | Remove a room
[**delete_room_logo**](FilesRoomsApi.md#delete_room_logo) | **DELETE** /api/2.0/files/rooms/{id}/logo | Remove a room logo
[**delete_tags**](FilesRoomsApi.md#delete_tags) | **DELETE** /api/2.0/files/rooms/{id}/tags | Remove room tags
[**get_covers**](FilesRoomsApi.md#get_covers) | **GET** /api/2.0/files/rooms/covers | Gets covers
[**get_new_room_items**](FilesRoomsApi.md#get_new_room_items) | **GET** /api/2.0/files/rooms/{id}/news | Get new room items
[**get_room_creating_status**](FilesRoomsApi.md#get_room_creating_status) | **GET** /api/2.0/files/rooms/fromtemplate/status | Get progress creating room
[**get_room_index_export**](FilesRoomsApi.md#get_room_index_export) | **GET** /api/2.0/files/rooms/indexexport | Gets room index export
[**get_room_info**](FilesRoomsApi.md#get_room_info) | **GET** /api/2.0/files/rooms/{id} | Get room information
[**get_room_links**](FilesRoomsApi.md#get_room_links) | **GET** /api/2.0/files/rooms/{id}/links | Get room links
[**get_room_security_info**](FilesRoomsApi.md#get_room_security_info) | **GET** /api/2.0/files/rooms/{id}/share | Get room access rights
[**get_rooms_folder**](FilesRoomsApi.md#get_rooms_folder) | **GET** /api/2.0/files/rooms | Get rooms
[**get_rooms_new_items**](FilesRoomsApi.md#get_rooms_new_items) | **GET** /api/2.0/files/rooms/news | Gets room new items
[**get_rooms_primary_external_link**](FilesRoomsApi.md#get_rooms_primary_external_link) | **GET** /api/2.0/files/rooms/{id}/link | Get primary external link
[**get_tags_info**](FilesRoomsApi.md#get_tags_info) | **GET** /api/2.0/files/tags | Get tags
[**get_template_creating_status**](FilesRoomsApi.md#get_template_creating_status) | **GET** /api/2.0/files/roomtemplate/status | Get progress creating room template
[**is_public**](FilesRoomsApi.md#is_public) | **GET** /api/2.0/files/roomtemplate/{id}/public | Get public
[**pin_room**](FilesRoomsApi.md#pin_room) | **PUT** /api/2.0/files/rooms/{id}/pin | Pin a room
[**reorder**](FilesRoomsApi.md#reorder) | **PUT** /api/2.0/files/rooms/{id}/reorder | Reorders to a room with ID specified in the request
[**resend_email_invitations**](FilesRoomsApi.md#resend_email_invitations) | **POST** /api/2.0/files/rooms/{id}/resend | Resend room invitations
[**set_link**](FilesRoomsApi.md#set_link) | **PUT** /api/2.0/files/rooms/{id}/links | Set an external or invitation link
[**set_public**](FilesRoomsApi.md#set_public) | **PUT** /api/2.0/files/roomtemplate/public | Set public
[**set_room_security**](FilesRoomsApi.md#set_room_security) | **PUT** /api/2.0/files/rooms/{id}/share | Set room access rights
[**start_room_index_export**](FilesRoomsApi.md#start_room_index_export) | **POST** /api/2.0/files/rooms/{id}/indexexport | Starts room index export
[**terminate_room_index_export**](FilesRoomsApi.md#terminate_room_index_export) | **DELETE** /api/2.0/files/rooms/indexexport | Terminates room index export
[**unarchive_room**](FilesRoomsApi.md#unarchive_room) | **PUT** /api/2.0/files/rooms/{id}/unarchive | Unarchive a room
[**unpin_room**](FilesRoomsApi.md#unpin_room) | **PUT** /api/2.0/files/rooms/{id}/unpin | Unpin a room
[**update_room**](FilesRoomsApi.md#update_room) | **PUT** /api/2.0/files/rooms/{id} | Rename a room
[**upload_room_logo**](FilesRoomsApi.md#upload_room_logo) | **POST** /api/2.0/files/logos | Upload an image for room logo


# **add_tags**
> FolderIntegerWrapper add_tags(id, batch_tags_request_dto=batch_tags_request_dto)

Add room tags

Adds the tags to a room with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.batch_tags_request_dto import BatchTagsRequestDto
from docspace.models.folder_integer_wrapper import FolderIntegerWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)
    id = 9846 # int | Room Id
    batch_tags_request_dto = docspace.BatchTagsRequestDto() # BatchTagsRequestDto | Batch tags (optional)

    try:
        # Add room tags
        api_response = api_instance.add_tags(id, batch_tags_request_dto=batch_tags_request_dto)
        print("The response of FilesRoomsApi->add_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->add_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Room Id | 
 **batch_tags_request_dto** | [**BatchTagsRequestDto**](BatchTagsRequestDto.md)| Batch tags | [optional] 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room information |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have permission to edit the room |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_room**
> FileOperationWrapper archive_room(id, archive_room_request=archive_room_request)

Archive a room

Moves a room with the ID specified in the request to the \"Archive\" section.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.archive_room_request import ArchiveRoomRequest
from docspace.models.file_operation_wrapper import FileOperationWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)
    id = 9846 # int | Room ID
    archive_room_request = docspace.ArchiveRoomRequest() # ArchiveRoomRequest | Parameters for archiving a room (optional)

    try:
        # Archive a room
        api_response = api_instance.archive_room(id, archive_room_request=archive_room_request)
        print("The response of FilesRoomsApi->archive_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->archive_room: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Room ID | 
 **archive_room_request** | [**ArchiveRoomRequest**](ArchiveRoomRequest.md)| Parameters for archiving a room | [optional] 

### Return type

[**FileOperationWrapper**](FileOperationWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File operation |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_room_cover**
> FolderIntegerWrapper change_room_cover(id, cover_request_dto=cover_request_dto)

Changes room cover

Changes room cover

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.cover_request_dto import CoverRequestDto
from docspace.models.folder_integer_wrapper import FolderIntegerWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)
    id = 9846 # int | Room ID
    cover_request_dto = docspace.CoverRequestDto() # CoverRequestDto | Parameters to change the room cover (optional)

    try:
        # Changes room cover
        api_response = api_instance.change_room_cover(id, cover_request_dto=cover_request_dto)
        print("The response of FilesRoomsApi->change_room_cover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->change_room_cover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Room ID | 
 **cover_request_dto** | [**CoverRequestDto**](CoverRequestDto.md)| Parameters to change the room cover | [optional] 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room cover |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have permission to change cover |  -  |
**404** | The required room was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_room**
> FolderIntegerWrapper create_room(create_room_request_dto=create_room_request_dto)

Create a room

Creates a room in the \"Rooms\" section.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.create_room_request_dto import CreateRoomRequestDto
from docspace.models.folder_integer_wrapper import FolderIntegerWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)
    create_room_request_dto = docspace.CreateRoomRequestDto() # CreateRoomRequestDto |  (optional)

    try:
        # Create a room
        api_response = api_instance.create_room(create_room_request_dto=create_room_request_dto)
        print("The response of FilesRoomsApi->create_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->create_room: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_room_request_dto** | [**CreateRoomRequestDto**](CreateRoomRequestDto.md)|  | [optional] 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_room_from_template**
> RoomFromTemplateStatusWrapper create_room_from_template(create_room_from_template_dto=create_room_from_template_dto)

Start create a room based on a template

Start create a room in the \"Rooms\" section based on a template.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.create_room_from_template_dto import CreateRoomFromTemplateDto
from docspace.models.room_from_template_status_wrapper import RoomFromTemplateStatusWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)
    create_room_from_template_dto = docspace.CreateRoomFromTemplateDto() # CreateRoomFromTemplateDto |  (optional)

    try:
        # Start create a room based on a template
        api_response = api_instance.create_room_from_template(create_room_from_template_dto=create_room_from_template_dto)
        print("The response of FilesRoomsApi->create_room_from_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->create_room_from_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_room_from_template_dto** | [**CreateRoomFromTemplateDto**](CreateRoomFromTemplateDto.md)|  | [optional] 

### Return type

[**RoomFromTemplateStatusWrapper**](RoomFromTemplateStatusWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_room_logo**
> FolderIntegerWrapper create_room_logo(id, logo_request=logo_request)

Create a room logo

Creates a logo for a room with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.folder_integer_wrapper import FolderIntegerWrapper
from docspace.models.logo_request import LogoRequest
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
    api_instance = docspace.FilesRoomsApi(api_client)
    id = 9846 # int | Room Id
    logo_request = docspace.LogoRequest() # LogoRequest | Logo (optional)

    try:
        # Create a room logo
        api_response = api_instance.create_room_logo(id, logo_request=logo_request)
        print("The response of FilesRoomsApi->create_room_logo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->create_room_logo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Room Id | 
 **logo_request** | [**LogoRequest**](LogoRequest.md)| Logo | [optional] 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room information |  -  |
**401** | Unauthorized |  -  |
**404** | The required room was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_room_third_party**
> FolderStringWrapper create_room_third_party(id, create_third_party_room=create_third_party_room)

Create a third-party room

Creates a room in the \"Rooms\" section stored in a third-party storage.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.create_third_party_room import CreateThirdPartyRoom
from docspace.models.folder_string_wrapper import FolderStringWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)
    id = '9846' # str | ID of the folder in the third-party storage in which the contents of the room will be stored
    create_third_party_room = docspace.CreateThirdPartyRoom() # CreateThirdPartyRoom | ThirdParty room (optional)

    try:
        # Create a third-party room
        api_response = api_instance.create_room_third_party(id, create_third_party_room=create_third_party_room)
        print("The response of FilesRoomsApi->create_room_third_party:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->create_room_third_party: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the folder in the third-party storage in which the contents of the room will be stored | 
 **create_third_party_room** | [**CreateThirdPartyRoom**](CreateThirdPartyRoom.md)| ThirdParty room | [optional] 

### Return type

[**FolderStringWrapper**](FolderStringWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tag**
> ObjectWrapper create_tag(create_tag_request_dto=create_tag_request_dto)

Create a tag

Creates a custom tag with the parameters specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.create_tag_request_dto import CreateTagRequestDto
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
    api_instance = docspace.FilesRoomsApi(api_client)
    create_tag_request_dto = docspace.CreateTagRequestDto() # CreateTagRequestDto |  (optional)

    try:
        # Create a tag
        api_response = api_instance.create_tag(create_tag_request_dto=create_tag_request_dto)
        print("The response of FilesRoomsApi->create_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->create_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tag_request_dto** | [**CreateTagRequestDto**](CreateTagRequestDto.md)|  | [optional] 

### Return type

[**ObjectWrapper**](ObjectWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New tag name |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to perform the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template**
> RoomTemplateStatusWrapper create_template(room_template_dto=room_template_dto)

Start create room template

Start create room template

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.room_template_dto import RoomTemplateDto
from docspace.models.room_template_status_wrapper import RoomTemplateStatusWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)
    room_template_dto = docspace.RoomTemplateDto() # RoomTemplateDto |  (optional)

    try:
        # Start create room template
        api_response = api_instance.create_template(room_template_dto=room_template_dto)
        print("The response of FilesRoomsApi->create_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->create_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_template_dto** | [**RoomTemplateDto**](RoomTemplateDto.md)|  | [optional] 

### Return type

[**RoomTemplateStatusWrapper**](RoomTemplateStatusWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_tags**
> delete_custom_tags(batch_tags_request_dto=batch_tags_request_dto)

Delete tags

Deletes a bunch of custom tags specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.batch_tags_request_dto import BatchTagsRequestDto
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
    api_instance = docspace.FilesRoomsApi(api_client)
    batch_tags_request_dto = docspace.BatchTagsRequestDto() # BatchTagsRequestDto |  (optional)

    try:
        # Delete tags
        api_instance.delete_custom_tags(batch_tags_request_dto=batch_tags_request_dto)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->delete_custom_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_tags_request_dto** | [**BatchTagsRequestDto**](BatchTagsRequestDto.md)|  | [optional] 

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
**200** | Ok |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to perform the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_room**
> FileOperationWrapper delete_room(id, delete_room_request=delete_room_request)

Remove a room

Removes a room with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.delete_room_request import DeleteRoomRequest
from docspace.models.file_operation_wrapper import FileOperationWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)
    id = 9846 # int | Room ID
    delete_room_request = docspace.DeleteRoomRequest() # DeleteRoomRequest | Parameters for deleting a room (optional)

    try:
        # Remove a room
        api_response = api_instance.delete_room(id, delete_room_request=delete_room_request)
        print("The response of FilesRoomsApi->delete_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->delete_room: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Room ID | 
 **delete_room_request** | [**DeleteRoomRequest**](DeleteRoomRequest.md)| Parameters for deleting a room | [optional] 

### Return type

[**FileOperationWrapper**](FileOperationWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File operation |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_room_logo**
> FolderIntegerWrapper delete_room_logo(id)

Remove a room logo

Removes a logo from a room with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.folder_integer_wrapper import FolderIntegerWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)
    id = 9846 # int | Room Id

    try:
        # Remove a room logo
        api_response = api_instance.delete_room_logo(id)
        print("The response of FilesRoomsApi->delete_room_logo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->delete_room_logo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Room Id | 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tags**
> FolderIntegerWrapper delete_tags(id, batch_tags_request_dto=batch_tags_request_dto)

Remove room tags

Removes the tags from a room with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.batch_tags_request_dto import BatchTagsRequestDto
from docspace.models.folder_integer_wrapper import FolderIntegerWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)
    id = 9846 # int | Room Id
    batch_tags_request_dto = docspace.BatchTagsRequestDto() # BatchTagsRequestDto | Batch tags (optional)

    try:
        # Remove room tags
        api_response = api_instance.delete_tags(id, batch_tags_request_dto=batch_tags_request_dto)
        print("The response of FilesRoomsApi->delete_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->delete_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Room Id | 
 **batch_tags_request_dto** | [**BatchTagsRequestDto**](BatchTagsRequestDto.md)| Batch tags | [optional] 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room information |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have permission to edit the room |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_covers**
> CoversResultArrayWrapper get_covers()

Gets covers

Gets covers

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.covers_result_array_wrapper import CoversResultArrayWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)

    try:
        # Gets covers
        api_response = api_instance.get_covers()
        print("The response of FilesRoomsApi->get_covers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->get_covers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CoversResultArrayWrapper**](CoversResultArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets room cover |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_new_room_items**
> NewItemsFileEntryArrayWrapper get_new_room_items(id)

Get new room items

Returns a list of all the new items from a room with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.new_items_file_entry_array_wrapper import NewItemsFileEntryArrayWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)
    id = 9846 # int | Room Id

    try:
        # Get new room items
        api_response = api_instance.get_new_room_items(id)
        print("The response of FilesRoomsApi->get_new_room_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->get_new_room_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Room Id | 

### Return type

[**NewItemsFileEntryArrayWrapper**](NewItemsFileEntryArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file entry information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_room_creating_status**
> RoomFromTemplateStatusWrapper get_room_creating_status()

Get progress creating room

Get progress creating room based a template

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.room_from_template_status_wrapper import RoomFromTemplateStatusWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)

    try:
        # Get progress creating room
        api_response = api_instance.get_room_creating_status()
        print("The response of FilesRoomsApi->get_room_creating_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->get_room_creating_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RoomFromTemplateStatusWrapper**](RoomFromTemplateStatusWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_room_index_export**
> DocumentBuilderTaskWrapper get_room_index_export()

Gets room index export

Gets room index export

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.document_builder_task_wrapper import DocumentBuilderTaskWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)

    try:
        # Gets room index export
        api_response = api_instance.get_room_index_export()
        print("The response of FilesRoomsApi->get_room_index_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->get_room_index_export: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DocumentBuilderTaskWrapper**](DocumentBuilderTaskWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_room_info**
> FolderIntegerWrapper get_room_info(id)

Get room information

Returns the room information.

### Example


```python
import docspace
from docspace.models.folder_integer_wrapper import FolderIntegerWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)
    id = 9846 # int | Room Id

    try:
        # Get room information
        api_response = api_instance.get_room_info(id)
        print("The response of FilesRoomsApi->get_room_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->get_room_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Room Id | 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

No authorization required

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

Get room links

Returns the links of a room with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.file_share_array_wrapper import FileShareArrayWrapper
from docspace.models.link_type import LinkType
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
    api_instance = docspace.FilesRoomsApi(api_client)
    id = 9846 # int | Room ID
    type = docspace.LinkType() # LinkType | Link type (optional)

    try:
        # Get room links
        api_response = api_instance.get_room_links(id, type=type)
        print("The response of FilesRoomsApi->get_room_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->get_room_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Room ID | 
 **type** | [**LinkType**](.md)| Link type | [optional] 

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
**200** | Room security information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_room_security_info**
> FileShareArrayWrapper get_room_security_info(id, filter_type=filter_type)

Get room access rights

Returns the access rights of a room with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.file_share_array_wrapper import FileShareArrayWrapper
from docspace.models.share_filter_type import ShareFilterType
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
    api_instance = docspace.FilesRoomsApi(api_client)
    id = 9846 # int | Room ID
    filter_type = docspace.ShareFilterType() # ShareFilterType | Share filter type (optional)

    try:
        # Get room access rights
        api_response = api_instance.get_room_security_info(id, filter_type=filter_type)
        print("The response of FilesRoomsApi->get_room_security_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->get_room_security_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Room ID | 
 **filter_type** | [**ShareFilterType**](.md)| Share filter type | [optional] 

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
**200** | Security information of room files |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rooms_folder**
> FolderContentIntegerWrapper get_rooms_folder(type=type, subject_id=subject_id, search_area=search_area, without_tags=without_tags, tags=tags, exclude_subject=exclude_subject, provider=provider, subject_filter=subject_filter, quota_filter=quota_filter, storage_filter=storage_filter)

Get rooms

Returns the contents of the \"Rooms\" section by the parameters specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.folder_content_integer_wrapper import FolderContentIntegerWrapper
from docspace.models.provider_filter import ProviderFilter
from docspace.models.quota_filter import QuotaFilter
from docspace.models.room_type import RoomType
from docspace.models.search_area import SearchArea
from docspace.models.storage_filter import StorageFilter
from docspace.models.subject_filter import SubjectFilter
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
    api_instance = docspace.FilesRoomsApi(api_client)
    type = [docspace.RoomType()] # List[RoomType] | Filter by room type (optional)
    subject_id = 'some text' # str | Filter by user ID (optional)
    search_area = docspace.SearchArea() # SearchArea | Room search area (Active, Archive, Any, Recent by links) (optional)
    without_tags = true # bool | Specifies whether to search by tags or not (optional)
    tags = 'some text' # str | Tags in the serialized format (optional)
    exclude_subject = true # bool | Specifies whether to exclude a subject or not (optional)
    provider = docspace.ProviderFilter() # ProviderFilter | Filter by provider name (None, Box, DropBox, GoogleDrive, kDrive, OneDrive, SharePoint, WebDav, Yandex, Storage) (optional)
    subject_filter = docspace.SubjectFilter() # SubjectFilter | Filter by subject (Owner - 0, Member - 1) (optional)
    quota_filter = docspace.QuotaFilter() # QuotaFilter | Filter by quota (All - 0, Default - 1, Custom - 2) (optional)
    storage_filter = docspace.StorageFilter() # StorageFilter | Filter by storage (None - 0, Internal - 1, ThirdParty - 2) (optional)

    try:
        # Get rooms
        api_response = api_instance.get_rooms_folder(type=type, subject_id=subject_id, search_area=search_area, without_tags=without_tags, tags=tags, exclude_subject=exclude_subject, provider=provider, subject_filter=subject_filter, quota_filter=quota_filter, storage_filter=storage_filter)
        print("The response of FilesRoomsApi->get_rooms_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->get_rooms_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**List[RoomType]**](RoomType.md)| Filter by room type | [optional] 
 **subject_id** | **str**| Filter by user ID | [optional] 
 **search_area** | [**SearchArea**](.md)| Room search area (Active, Archive, Any, Recent by links) | [optional] 
 **without_tags** | **bool**| Specifies whether to search by tags or not | [optional] 
 **tags** | **str**| Tags in the serialized format | [optional] 
 **exclude_subject** | **bool**| Specifies whether to exclude a subject or not | [optional] 
 **provider** | [**ProviderFilter**](.md)| Filter by provider name (None, Box, DropBox, GoogleDrive, kDrive, OneDrive, SharePoint, WebDav, Yandex, Storage) | [optional] 
 **subject_filter** | [**SubjectFilter**](.md)| Filter by subject (Owner - 0, Member - 1) | [optional] 
 **quota_filter** | [**QuotaFilter**](.md)| Filter by quota (All - 0, Default - 1, Custom - 2) | [optional] 
 **storage_filter** | [**StorageFilter**](.md)| Filter by storage (None - 0, Internal - 1, ThirdParty - 2) | [optional] 

### Return type

[**FolderContentIntegerWrapper**](FolderContentIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the contents of the \&quot;Rooms\&quot; section |  -  |
**401** | Unauthorized |  -  |
**403** | You don&#39;t have enough permission to view the room content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rooms_new_items**
> NewItemsRoomNewItemsArrayWrapper get_rooms_new_items()

Gets room new items

Gets room new items

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.new_items_room_new_items_array_wrapper import NewItemsRoomNewItemsArrayWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)

    try:
        # Gets room new items
        api_response = api_instance.get_rooms_new_items()
        print("The response of FilesRoomsApi->get_rooms_new_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->get_rooms_new_items: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NewItemsRoomNewItemsArrayWrapper**](NewItemsRoomNewItemsArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of new items |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rooms_primary_external_link**
> FileShareWrapper get_rooms_primary_external_link(id)

Get primary external link

Returns the primary external link of a room with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

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
    api_instance = docspace.FilesRoomsApi(api_client)
    id = 9846 # int | Room Id

    try:
        # Get primary external link
        api_response = api_instance.get_rooms_primary_external_link(id)
        print("The response of FilesRoomsApi->get_rooms_primary_external_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->get_rooms_primary_external_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Room Id | 

### Return type

[**FileShareWrapper**](FileShareWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room security information |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags_info**
> ObjectArrayWrapper get_tags_info()

Get tags

Returns a list of custom tags.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.object_array_wrapper import ObjectArrayWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)

    try:
        # Get tags
        api_response = api_instance.get_tags_info()
        print("The response of FilesRoomsApi->get_tags_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->get_tags_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ObjectArrayWrapper**](ObjectArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tag names |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_creating_status**
> RoomTemplateStatusWrapper get_template_creating_status()

Get progress creating room template

Get progress creating room template

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.room_template_status_wrapper import RoomTemplateStatusWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)

    try:
        # Get progress creating room template
        api_response = api_instance.get_template_creating_status()
        print("The response of FilesRoomsApi->get_template_creating_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->get_template_creating_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RoomTemplateStatusWrapper**](RoomTemplateStatusWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_public**
> BooleanWrapper is_public(id)

Get public

Get public settings

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
    api_instance = docspace.FilesRoomsApi(api_client)
    id = 9846 # int | Template id

    try:
        # Get public
        api_response = api_instance.is_public(id)
        print("The response of FilesRoomsApi->is_public:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->is_public: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Template id | 

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
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pin_room**
> FolderIntegerWrapper pin_room(id)

Pin a room

Pins a room with the ID specified in the request to the top of the list.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.folder_integer_wrapper import FolderIntegerWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)
    id = 9846 # int | Room Id

    try:
        # Pin a room
        api_response = api_instance.pin_room(id)
        print("The response of FilesRoomsApi->pin_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->pin_room: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Room Id | 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reorder**
> FolderIntegerWrapper reorder(id)

Reorders to a room with ID specified in the request

Reorders to a room with ID specified in the request

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.folder_integer_wrapper import FolderIntegerWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)
    id = 9846 # int | Room Id

    try:
        # Reorders to a room with ID specified in the request
        api_response = api_instance.reorder(id)
        print("The response of FilesRoomsApi->reorder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->reorder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Room Id | 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_email_invitations**
> resend_email_invitations(id, user_invitation=user_invitation)

Resend room invitations

Resends the email invitations to a room with the ID specified in the request to the selected users.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.user_invitation import UserInvitation
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
    api_instance = docspace.FilesRoomsApi(api_client)
    id = 9846 # int | Room Id
    user_invitation = docspace.UserInvitation() # UserInvitation | User invitation (optional)

    try:
        # Resend room invitations
        api_instance.resend_email_invitations(id, user_invitation=user_invitation)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->resend_email_invitations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Room Id | 
 **user_invitation** | [**UserInvitation**](UserInvitation.md)| User invitation | [optional] 

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
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_link**
> FileShareWrapper set_link(id, room_link_request=room_link_request)

Set an external or invitation link

Sets an external or invitation link with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.file_share_wrapper import FileShareWrapper
from docspace.models.room_link_request import RoomLinkRequest
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
    api_instance = docspace.FilesRoomsApi(api_client)
    id = 9846 # int | Room ID
    room_link_request = docspace.RoomLinkRequest() # RoomLinkRequest | Room link (optional)

    try:
        # Set an external or invitation link
        api_response = api_instance.set_link(id, room_link_request=room_link_request)
        print("The response of FilesRoomsApi->set_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->set_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Room ID | 
 **room_link_request** | [**RoomLinkRequest**](RoomLinkRequest.md)| Room link | [optional] 

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
**200** | Room security information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_public**
> set_public(set_public_dto=set_public_dto)

Set public

Set public settings

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.set_public_dto import SetPublicDto
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
    api_instance = docspace.FilesRoomsApi(api_client)
    set_public_dto = docspace.SetPublicDto() # SetPublicDto |  (optional)

    try:
        # Set public
        api_instance.set_public(set_public_dto=set_public_dto)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->set_public: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_public_dto** | [**SetPublicDto**](SetPublicDto.md)|  | [optional] 

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
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_room_security**
> RoomSecurityWrapper set_room_security(id, room_invitation_request=room_invitation_request)

Set room access rights

Sets the access rights to a room with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.room_invitation_request import RoomInvitationRequest
from docspace.models.room_security_wrapper import RoomSecurityWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)
    id = 9846 # int | Room ID
    room_invitation_request = docspace.RoomInvitationRequest() # RoomInvitationRequest | Room invitation (optional)

    try:
        # Set room access rights
        api_response = api_instance.set_room_security(id, room_invitation_request=room_invitation_request)
        print("The response of FilesRoomsApi->set_room_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->set_room_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Room ID | 
 **room_invitation_request** | [**RoomInvitationRequest**](RoomInvitationRequest.md)| Room invitation | [optional] 

### Return type

[**RoomSecurityWrapper**](RoomSecurityWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room security information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_room_index_export**
> DocumentBuilderTaskWrapper start_room_index_export(id)

Starts room index export

Starts room index export

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.document_builder_task_wrapper import DocumentBuilderTaskWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)
    id = 9846 # int | Room Id

    try:
        # Starts room index export
        api_response = api_instance.start_room_index_export(id)
        print("The response of FilesRoomsApi->start_room_index_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->start_room_index_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Room Id | 

### Return type

[**DocumentBuilderTaskWrapper**](DocumentBuilderTaskWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Unauthorized |  -  |
**501** | Folder indexing is turned off |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_room_index_export**
> terminate_room_index_export()

Terminates room index export

Terminates room index export

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
    api_instance = docspace.FilesRoomsApi(api_client)

    try:
        # Terminates room index export
        api_instance.terminate_room_index_export()
    except Exception as e:
        print("Exception when calling FilesRoomsApi->terminate_room_index_export: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unarchive_room**
> FileOperationWrapper unarchive_room(id, archive_room_request=archive_room_request)

Unarchive a room

Moves a room with the ID specified in the request from the \"Archive\" section to the \"Rooms\" section.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.archive_room_request import ArchiveRoomRequest
from docspace.models.file_operation_wrapper import FileOperationWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)
    id = 9846 # int | Room ID
    archive_room_request = docspace.ArchiveRoomRequest() # ArchiveRoomRequest | Parameters for archiving a room (optional)

    try:
        # Unarchive a room
        api_response = api_instance.unarchive_room(id, archive_room_request=archive_room_request)
        print("The response of FilesRoomsApi->unarchive_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->unarchive_room: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Room ID | 
 **archive_room_request** | [**ArchiveRoomRequest**](ArchiveRoomRequest.md)| Parameters for archiving a room | [optional] 

### Return type

[**FileOperationWrapper**](FileOperationWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File operation |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpin_room**
> FolderIntegerWrapper unpin_room(id)

Unpin a room

Unpins a room with the ID specified in the request from the top of the list.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.folder_integer_wrapper import FolderIntegerWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)
    id = 9846 # int | Room Id

    try:
        # Unpin a room
        api_response = api_instance.unpin_room(id)
        print("The response of FilesRoomsApi->unpin_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->unpin_room: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Room Id | 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_room**
> FolderIntegerWrapper update_room(id, update_room_request=update_room_request)

Rename a room

Renames a room with the ID specified in  the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.folder_integer_wrapper import FolderIntegerWrapper
from docspace.models.update_room_request import UpdateRoomRequest
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
    api_instance = docspace.FilesRoomsApi(api_client)
    id = 9846 # int | Room ID
    update_room_request = docspace.UpdateRoomRequest() # UpdateRoomRequest | Update room (optional)

    try:
        # Rename a room
        api_response = api_instance.update_room(id, update_room_request=update_room_request)
        print("The response of FilesRoomsApi->update_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->update_room: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Room ID | 
 **update_room_request** | [**UpdateRoomRequest**](UpdateRoomRequest.md)| Update room | [optional] 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated room information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_room_logo**
> UploadResultWrapper upload_room_logo(form_collection=form_collection)

Upload an image for room logo

Uploads a temporary image to create a room logo.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.key_value_pair_string_string_values import KeyValuePairStringStringValues
from docspace.models.upload_result_wrapper import UploadResultWrapper
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
    api_instance = docspace.FilesRoomsApi(api_client)
    form_collection = [docspace.KeyValuePairStringStringValues()] # List[KeyValuePairStringStringValues] | Image data (optional)

    try:
        # Upload an image for room logo
        api_response = api_instance.upload_room_logo(form_collection=form_collection)
        print("The response of FilesRoomsApi->upload_room_logo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesRoomsApi->upload_room_logo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_collection** | [**List[KeyValuePairStringStringValues]**](KeyValuePairStringStringValues.md)| Image data | [optional] 

### Return type

[**UploadResultWrapper**](UploadResultWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upload result |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

