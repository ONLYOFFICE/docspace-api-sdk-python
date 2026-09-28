# docspace_api_sdk.GroupsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_room_group**](#add_room_group) | **POST** /api/2.0/files/group | Add a new room group
[**change_room_group_icon**](#change_room_group_icon) | **POST** /api/2.0/files/group/{id}/icon | Change room group icon
[**delete_room_group**](#delete_room_group) | **DELETE** /api/2.0/files/group/{id} | Delete a room group
[**get_room_group_info**](#get_room_group_info) | **GET** /api/2.0/files/group/{id} | Get room group info
[**get_room_groups**](#get_room_groups) | **GET** /api/2.0/files/group | List room groups
[**update_room_group**](#update_room_group) | **PUT** /api/2.0/files/group/{id} | Update room group


# **add_room_group**
> RoomGroupWrapper add_room_group(room_group_request_dto=room_group_request_dto)

Creates a room group, a personal collection that gathers rooms the caller already works with under one name
and icon; it belongs to the account that created it and is never shown to other members of the portal. Pass
the group name, the identifier of one of the built-in covers offered by `GET api/2.0/files/rooms/covers`, and
a list of at least one room - a number for a room stored in the portal, a string for a room on a connected
third-party account. Any role may create its own group, a guest included: what is checked is read access to
each listed room, not the role of the caller. Repeated identifiers are collapsed, and a value that is not a
room identifier at all is rejected as an invalid request. When none of the listed rooms can be read the group
is not created; when only some of them can, the group is created with those rooms and the call is still
reported as failed, so re-read `GET api/2.0/files/group` before retrying. A room may sit in several groups,
and two groups of the same account may carry the same name. The answer is the stored group with its rooms.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_group_request_dto** | [**RoomGroupRequestDto**](RoomGroupRequestDto.md)|  | [optional] 

### Return type

[**RoomGroupWrapper**](RoomGroupWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.room_group_request_dto import RoomGroupRequestDto
from docspace_api_sdk.models.room_group_wrapper import RoomGroupWrapper
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
    api_instance = docspace_api_sdk.GroupsApi(api_client)
    room_group_request_dto = docspace_api_sdk.RoomGroupRequestDto() # RoomGroupRequestDto |  (optional)

    try:
        # Add a new room group
        api_response = api_instance.add_room_group(room_group_request_dto=room_group_request_dto)
        print("The response of GroupsApi->add_room_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->add_room_group: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created room group with the rooms that were linked to it |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_room_group_icon**
> RoomGroupWrapper change_room_group_icon(id, icon_request=icon_request)

Replaces the icon of one of the caller's own room groups and returns the whole group, its name and its rooms
left as they were. Send the identifier of one of the built-in covers offered by
`GET api/2.0/files/rooms/covers`; an empty string strips the icon, after which the group comes back with an
empty `icon`, and any other value - including a word that merely reads like one, such as `none` - is rejected
as an invalid request. An uploaded image cannot be used here, unlike the logo of a room. Leaving `icon` out of
the body or sending it as null is accepted and changes nothing, whereas a request that carries no body at all,
or a body that is not JSON, is refused. Setting the icon the group already has is accepted as well, so
retrying the call is safe. Any role may re-icon its own group, and a group belonging to another account is
answered as missing rather than refused, exactly as reading it would be.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room group to re-icon, identified by the value `GET api/2.0/files/group` reports for it. A group of  another account cannot be addressed and reads as missing. | 
 **icon_request** | [**IconRequest**](IconRequest.md)| The icon to give the group. A body that leaves the icon out is accepted and changes nothing. | [optional] 

### Return type

[**RoomGroupWrapper**](RoomGroupWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.icon_request import IconRequest
from docspace_api_sdk.models.room_group_wrapper import RoomGroupWrapper
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
    api_instance = docspace_api_sdk.GroupsApi(api_client)
    id = 42 # int | The room group to re-icon, identified by the value `GET api/2.0/files/group` reports for it. A group of  another account cannot be addressed and reads as missing.
    icon_request = docspace_api_sdk.IconRequest() # IconRequest | The icon to give the group. A body that leaves the icon out is accepted and changes nothing. (optional)

    try:
        # Change room group icon
        api_response = api_instance.change_room_group_icon(id, icon_request=icon_request)
        print("The response of GroupsApi->change_room_group_icon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->change_room_group_icon: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The room group with the new icon |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_room_group**
> delete_room_group(id, include_members=include_members)

Deletes one of the caller's own room groups. Only the collection goes away: the rooms it gathered, their
content and the shares on them are left exactly as they were, and a room that was in no other group simply
stops being grouped. Deleting a group of another account is refused, and an identifier that names nothing -
because it never existed, or because the group has already been deleted - is answered as missing, so repeating
the call after a successful delete does not report success a second time. The operation is destructive and
cannot be undone: there is no trash for groups, and rebuilding one means calling `POST api/2.0/files/group`
again with the same name, icon and rooms, which gives it a new identifier. Nothing is returned in the body.
The `includeMembers` parameter is accepted here because the route shares its contract with
`GET api/2.0/files/group/{id}`, and has no effect on what is deleted. Read the group first when the rooms it
gathers still have to be recorded somewhere.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room group to act on, identified by the value `GET api/2.0/files/group` reports for it. A group of another  account cannot be addressed and reads as missing. | 
 **include_members** | **bool**| Whether the rooms of the group are listed in the answer: true fills the `rooms` array, false leaves it out and  reports only how many there are in `totalRooms`. | [optional] 

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
    api_instance = docspace_api_sdk.GroupsApi(api_client)
    id = 42 # int | The room group to act on, identified by the value `GET api/2.0/files/group` reports for it. A group of another  account cannot be addressed and reads as missing.
    include_members = true # bool | Whether the rooms of the group are listed in the answer: true fills the `rooms` array, false leaves it out and  reports only how many there are in `totalRooms`. (optional)

    try:
        # Delete a room group
        api_instance.delete_room_group(id, include_members=include_members)
    except Exception as e:
        print("Exception when calling GroupsApi->delete_room_group: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The room group no longer exists; the body is empty and the rooms it gathered are left as they were |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_room_group_info**
> RoomGroupWrapper get_room_group_info(id, include_members=include_members)

Returns one room group of the calling account together with the rooms it gathers. Groups are personal: an
identifier that belongs to another member is answered the same way as one that was never created or has
already been deleted, and a portal administrator is no exception to that rule. Take the identifier from
`GET api/2.0/files/group`, which lists the groups the caller owns. Set `includeMembers` to false to get the
group without the `rooms` array, which is the cheaper form when only the name, the icon and the number of
rooms are needed; `totalRooms` is filled either way. A room moved to the archive is left out of both `rooms`
and `totalRooms` while its membership survives, so taking the room out of the archive brings it back into the
group. Rooms stored in the portal are listed before rooms on connected third-party accounts. The call is
read-only and changes nothing about the group or the rooms it refers to.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room group to act on, identified by the value `GET api/2.0/files/group` reports for it. A group of another  account cannot be addressed and reads as missing. | 
 **include_members** | **bool**| Whether the rooms of the group are listed in the answer: true fills the `rooms` array, false leaves it out and  reports only how many there are in `totalRooms`. | [optional] 

### Return type

[**RoomGroupWrapper**](RoomGroupWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.room_group_wrapper import RoomGroupWrapper
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
    api_instance = docspace_api_sdk.GroupsApi(api_client)
    id = 42 # int | The room group to act on, identified by the value `GET api/2.0/files/group` reports for it. A group of another  account cannot be addressed and reads as missing.
    include_members = true # bool | Whether the rooms of the group are listed in the answer: true fills the `rooms` array, false leaves it out and  reports only how many there are in `totalRooms`. (optional)

    try:
        # Get room group info
        api_response = api_instance.get_room_group_info(id, include_members=include_members)
        print("The response of GroupsApi->get_room_group_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_room_group_info: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The room group with the rooms it gathers |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_room_groups**
> RoomGroupArrayWrapper get_room_groups(include_members=include_members, search_area=search_area)

Returns every room group of the calling account, each with the rooms it gathers. Only groups the caller
created are listed: groups of other members never appear here, and an account that has never made one gets an
empty array back. Set `includeMembers` to false to leave the `rooms` array out of every entry and keep the
name, the icon and `totalRooms` alone, which is the cheaper form when the list is only being shown as a menu.
Archived rooms are skipped in both the `rooms` array and the `totalRooms` count, and reappear once the room is
taken out of the archive. The listing is neither paged nor filtered - it always carries the whole set - and
the order of the entries is not contractual, so sort them on the client when the order matters. The call is
read-only. Use `GET api/2.0/files/group/{id}` when the identifier of a single group is already known, and
`POST api/2.0/files/group` to add one.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_members** | **bool**| Whether the rooms of each group are listed in the answer: true fills the `rooms` array of every entry, false  leaves it out and reports only how many there are in `totalRooms`. | [optional] 
 **search_area** | [**SearchArea**](.md)| The section to list the groups of: Active for Rooms and Forms for Forms. Active when omitted. | [optional] 

### Return type

[**RoomGroupArrayWrapper**](RoomGroupArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.room_group_array_wrapper import RoomGroupArrayWrapper
from docspace_api_sdk.models.search_area import SearchArea
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
    api_instance = docspace_api_sdk.GroupsApi(api_client)
    include_members = true # bool | Whether the rooms of each group are listed in the answer: true fills the `rooms` array of every entry, false  leaves it out and reports only how many there are in `totalRooms`. (optional)
    search_area = docspace_api_sdk.SearchArea() # SearchArea | The section to list the groups of: Active for Rooms and Forms for Forms. Active when omitted. (optional)

    try:
        # List room groups
        api_response = api_instance.get_room_groups(include_members=include_members, search_area=search_area)
        print("The response of GroupsApi->get_room_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_room_groups: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The room groups of the calling account |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_room_group**
> RoomGroupWrapper update_room_group(id, update_room_group_request)

Applies changes to one of the caller's own room groups: a new name, rooms to attach, rooms to detach, or any
combination of the three in a single call. A body that carries none of the three (`{}`) is accepted and
changes nothing, while a body that names them and leaves every one of them empty asks for an update that
cannot be performed and is rejected as an invalid request. `roomsToAdd` is resolved the way creation resolves
its list: every identifier has to name a room the caller can read, repeats and rooms already in the group are
collapsed, and when only part of the list resolves the rest is still attached and the call is reported as
failed. `roomsToRemove` works the other way round - a room already in the group is always detached, even when
the caller has since lost access to it, whereas an identifier that is not in the group is resolved first and
refused when it names nothing. The steps are applied in order and are not rolled back when a later one fails.
A group of another account is answered as missing. The answer is the group as stored after the call.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room group to change, identified by the value `GET api/2.0/files/group` reports for it. A group of another  account cannot be addressed and reads as missing. | 
 **update_room_group_request** | [**UpdateRoomGroupRequest**](UpdateRoomGroupRequest.md)| The changes to apply. Carrying none of them leaves the group as it is, and each of them may be sent on its own  or together with the others. | 

### Return type

[**RoomGroupWrapper**](RoomGroupWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.room_group_wrapper import RoomGroupWrapper
from docspace_api_sdk.models.update_room_group_request import UpdateRoomGroupRequest
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
    api_instance = docspace_api_sdk.GroupsApi(api_client)
    id = 42 # int | The room group to change, identified by the value `GET api/2.0/files/group` reports for it. A group of another  account cannot be addressed and reads as missing.
    update_room_group_request = docspace_api_sdk.UpdateRoomGroupRequest() # UpdateRoomGroupRequest | The changes to apply. Carrying none of them leaves the group as it is, and each of them may be sent on its own  or together with the others.

    try:
        # Update room group
        api_response = api_instance.update_room_group(id, update_room_group_request)
        print("The response of GroupsApi->update_room_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->update_room_group: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The room group as stored after the change |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

