# docspace_api_sdk.GroupApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group**](#add_group) | **POST** /api/2.0/group | Add a new group
[**add_members_to**](#add_members_to) | **PUT** /api/2.0/group/{id}/members | Add group members
[**delete_group**](#delete_group) | **DELETE** /api/2.0/group/{id} | Delete a group
[**get_group**](#get_group) | **GET** /api/2.0/group/{id} | Get a group
[**get_group_by_user_id**](#get_group_by_user_id) | **GET** /api/2.0/group/user/{userid} | Get user groups
[**get_groups**](#get_groups) | **GET** /api/2.0/group | Get groups
[**move_members_to**](#move_members_to) | **PUT** /api/2.0/group/{fromId}/members/{toId} | Move group members
[**remove_members_from**](#remove_members_from) | **DELETE** /api/2.0/group/{id}/members | Remove group members
[**set_group_manager**](#set_group_manager) | **PUT** /api/2.0/group/{id}/manager | Set a group manager
[**set_members_to**](#set_members_to) | **POST** /api/2.0/group/{id}/members | Replace group members
[**update_group**](#update_group) | **PUT** /api/2.0/group/{id} | Update a group


# **add_group**
> GroupWrapper add_group(group_request_dto=group_request_dto)

Creates a group with the given name and, optionally, a manager and a first set of members.
The caller needs the permissions to edit groups and to add and remove users.
The name is required and cannot be blank, and unlike the operations that add members later, this one checks
every listed account upfront and rejects the whole call with 400 if any of them is unusable - a guest, a
disabled account or an ID that matches nobody.
The call is not idempotent: names are not unique, so repeating it creates a second group with the same name.
Creating a group raises a `GroupCreated` webhook, and the answer holds the new group with its members
included.
Members can be changed afterwards through `PUT api/2.0/group/{id}` or the dedicated member operations.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_request_dto** | [**GroupRequestDto**](GroupRequestDto.md)|  | [optional] 

### Return type

[**GroupWrapper**](GroupWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.group_request_dto import GroupRequestDto
from docspace_api_sdk.models.group_wrapper import GroupWrapper
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
    api_instance = docspace_api_sdk.GroupApi(api_client)
    group_request_dto = docspace_api_sdk.GroupRequestDto() # GroupRequestDto |  (optional)

    try:
        # Add a new group
        api_response = api_instance.add_group(group_request_dto=group_request_dto)
        print("The response of GroupApi->add_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->add_group: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new group, with its members |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The group name is empty, or one of the listed accounts is a guest, is disabled or does not exist |  -  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_members_to**
> GroupWrapper add_members_to(id, members_request)

Adds the listed accounts to a group, keeping the members it already has.
The caller needs the permissions to edit groups and to add and remove users, and the ID has to belong to a
group that has not been deleted, otherwise the operation answers 404.
Accounts that cannot be group members - a guest, a disabled account or an ID that matches nobody - are
silently skipped instead of failing the call, so compare the members in the answer with what was sent to see
what was actually applied.
The call is idempotent for an account that is already a member, and it does not change who manages the group;
use `PUT api/2.0/group/{id}/manager` for that.
The answer is the group with its members after the addition.
To replace the whole list instead of extending it, use `POST api/2.0/group/{id}/members`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The ID of the group whose members are changed, taken from the route. It has to be a group that has not been  deleted, otherwise the operation answers 404. | 
 **members_request** | [**MembersRequest**](MembersRequest.md)| The accounts to add, replace with, or remove. | 

### Return type

[**GroupWrapper**](GroupWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.group_wrapper import GroupWrapper
from docspace_api_sdk.models.members_request import MembersRequest
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
    api_instance = docspace_api_sdk.GroupApi(api_client)
    id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The ID of the group whose members are changed, taken from the route. It has to be a group that has not been  deleted, otherwise the operation answers 404.
    members_request = docspace_api_sdk.MembersRequest() # MembersRequest | The accounts to add, replace with, or remove.

    try:
        # Add group members
        api_response = api_instance.add_members_to(id, members_request)
        print("The response of GroupApi->add_members_to:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->add_members_to: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The group with its members after the addition |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**404** | No group has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(id)

Deletes a group and withdraws the access it had been granted to rooms, folders and files.
The caller needs the permissions to edit groups and to add and remove users, and the ID has to belong to a
group that has not been deleted, otherwise the operation answers 404.
The removal is permanent and cannot be undone, and it affects sharing: everything that was shared with the
group loses that share, so members who had access only through this group lose it too.
The accounts themselves are kept - only their membership disappears.
The call answers 204 with no body and raises a `GroupDeleted` webhook; a second call with the same ID answers
404 rather than succeeding again.
To empty a group without deleting it, move its members away with
`PUT api/2.0/group/{fromId}/members/{toId}` or remove them through `DELETE api/2.0/group/{id}/members`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The ID of the group to delete, taken from the route. It has to be a group that has not been deleted already,  otherwise the operation answers 404. | 

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
    api_instance = docspace_api_sdk.GroupApi(api_client)
    id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The ID of the group to delete, taken from the route. It has to be a group that has not been deleted already,  otherwise the operation answers 404.

    try:
        # Delete a group
        api_instance.delete_group(id)
    except Exception as e:
        print("Exception when calling GroupApi->delete_group: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The group is deleted. No content is returned |  -  |
**403** | No permissions to perform this action |  -  |
**404** | No group has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> GroupWrapper get_group(id, include_members=include_members)

Returns one group by its ID, with its name, its manager and - when asked for - the accounts that belong to
it.
The caller needs the permission to read groups, and the ID has to belong to a group that has not been
deleted, otherwise the operation answers 404.
The call is read-only, and the member list is left out unless `includeMembers` is set to true, so ask for it
only when the members are actually needed.
Use `GET api/2.0/group` to look a group up by name or to page through them all.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The ID of the group to read, taken from the route. It has to be a group that has not been deleted, otherwise  the operation answers 404. | 
 **include_members** | **bool**| Whether to fill in the member list of the group. It defaults to true, so set it to false when only the name  and the manager are needed and the group may be large. | [optional] 

### Return type

[**GroupWrapper**](GroupWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.group_wrapper import GroupWrapper
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
    api_instance = docspace_api_sdk.GroupApi(api_client)
    id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The ID of the group to read, taken from the route. It has to be a group that has not been deleted, otherwise  the operation answers 404.
    include_members = true # bool | Whether to fill in the member list of the group. It defaults to true, so set it to false when only the name  and the manager are needed and the group may be large. (optional)

    try:
        # Get a group
        api_response = api_instance.get_group(id, include_members=include_members)
        print("The response of GroupApi->get_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->get_group: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The group, with its members when includeMembers was set |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**404** | No group has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_by_user_id**
> GroupSummaryArrayWrapper get_group_by_user_id(userid)

Returns every group the account with the ID in the route belongs to, as a flat list of ID and name pairs.
The caller needs the permission to read groups.
The call is read-only, is not paged, and answers an empty list both for an account that belongs to no group
and for an ID that matches no account, so an empty answer does not prove the account exists.
The entries are summaries and carry neither the manager nor the members - read `GET api/2.0/group/{id}` for
the full picture of one of them.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **UUID**| The ID of the account whose groups are listed, taken from the route. An ID that matches no account yields an  empty list rather than 404. | 

### Return type

[**GroupSummaryArrayWrapper**](GroupSummaryArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.group_summary_array_wrapper import GroupSummaryArrayWrapper
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
    api_instance = docspace_api_sdk.GroupApi(api_client)
    userid = UUID('00000000-0000-0000-0000-000000000000') # UUID | The ID of the account whose groups are listed, taken from the route. An ID that matches no account yields an  empty list rather than 404.

    try:
        # Get user groups
        api_response = api_instance.get_group_by_user_id(userid)
        print("The response of GroupApi->get_group_by_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->get_group_by_user_id: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The groups the account belongs to, as ID and name pairs |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups**
> GroupArrayWrapper get_groups(user_id=user_id, manager=manager, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)

Returns the groups of the portal, one page at a time, with the summary information about each of them - the
ID, the name and the manager - but without the member list.
The caller needs the permission to read groups.
The call is read-only, and the number of groups that match the filters is reported in the total count of the
response, so a client can page through them with `count` and `startIndex`.
Narrow the result with `filterValue` on the group name, with `userId` to keep only the groups that account
belongs to, and with `manager` set to true to keep only the groups it manages; order it with `sortBy` and
`sortOrder`, and an unknown `sortBy` falls back to sorting by title.
The entries carry no members - read `GET api/2.0/group/{id}` with `includeMembers` for one group, or
`GET api/2.0/group/user/{userid}` to find the groups of a single account.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **UUID**| Keeps only the groups the account with this ID takes part in. Omit it to search every group of the portal. | [optional] 
 **manager** | **bool**| Narrows `userId` down to the groups that account manages, instead of every group it belongs to. It has no  effect on its own and defaults to false. | [optional] 
 **count** | **int**| The size of the page. It defaults to 100, which is also the largest value the operation accepts. | [optional] 
 **start_index** | **int**| The number of matching groups to skip before the page starts. It defaults to 0, and the total number of  matches is reported in the total count of the response. | [optional] 
 **sort_by** | **str**| What to order the groups by: `Title`, `Manager` or `MembersCount`, compared without regard to case. Any other  value, and omitting the field, orders by title. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The direction of the ordering: `Ascending`, which is the default, or `Descending`. | [optional] 
 **filter_value** | **str**| The text to match against the group name. Omit it to get every group. | [optional] 

### Return type

[**GroupArrayWrapper**](GroupArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.group_array_wrapper import GroupArrayWrapper
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
    api_instance = docspace_api_sdk.GroupApi(api_client)
    user_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Keeps only the groups the account with this ID takes part in. Omit it to search every group of the portal. (optional)
    manager = false # bool | Narrows `userId` down to the groups that account manages, instead of every group it belongs to. It has no  effect on its own and defaults to false. (optional)
    count = 25 # int | The size of the page. It defaults to 100, which is also the largest value the operation accepts. (optional)
    start_index = 0 # int | The number of matching groups to skip before the page starts. It defaults to 0, and the total number of  matches is reported in the total count of the response. (optional)
    sort_by = 'Title' # str | What to order the groups by: `Title`, `Manager` or `MembersCount`, compared without regard to case. Any other  value, and omitting the field, orders by title. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The direction of the ordering: `Ascending`, which is the default, or `Descending`. (optional)
    filter_value = 'Marketing' # str | The text to match against the group name. Omit it to get every group. (optional)

    try:
        # Get groups
        api_response = api_instance.get_groups(user_id=user_id, manager=manager, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)
        print("The response of GroupApi->get_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->get_groups: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matching groups, with their summary information |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_members_to**
> GroupWrapper move_members_to(from_id, to_id)

Moves every member of one group into another group, emptying the first one.
The caller needs the permissions to edit groups and to add and remove users, and both IDs have to belong to
groups that have not been deleted, otherwise the operation answers 404.
The source group is kept, only without members, so delete it separately through
`DELETE api/2.0/group/{id}` if it is no longer needed.
Members that cannot be group members any more are silently skipped rather than failing the call, and an
account that already belongs to the destination is simply left there.
The answer is the destination group with its members, not the source one.
To move a chosen few instead of everybody, use `PUT api/2.0/group/{id}/members` and
`DELETE api/2.0/group/{id}/members`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_id** | **UUID**| The ID of the group the members are taken from. It is emptied but not deleted, and it has to be a group that  has not been deleted already. | 
 **to_id** | **UUID**| The ID of the group the members are moved into. It is the group the answer describes, and it has to be a  group that has not been deleted already. | 

### Return type

[**GroupWrapper**](GroupWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.group_wrapper import GroupWrapper
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
    api_instance = docspace_api_sdk.GroupApi(api_client)
    from_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The ID of the group the members are taken from. It is emptied but not deleted, and it has to be a group that  has not been deleted already.
    to_id = UUID('11111111-1111-1111-1111-111111111111') # UUID | The ID of the group the members are moved into. It is the group the answer describes, and it has to be a  group that has not been deleted already.

    try:
        # Move group members
        api_response = api_instance.move_members_to(from_id, to_id)
        print("The response of GroupApi->move_members_to:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->move_members_to: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The destination group with its members |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**404** | No group has one of the specified IDs |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_members_from**
> GroupWrapper remove_members_from(id, members_request)

Removes the listed accounts from a group, leaving the rest of its members in place.
The caller needs the permissions to edit groups and to add and remove users, and the ID has to belong to a
group that has not been deleted, otherwise the operation answers 404.
The accounts themselves are kept; only their membership in this group ends, together with the access they had
through it.
The call is idempotent and forgiving: an ID that is not a member, and one that matches no account at all, are
both skipped without an error, and an empty list simply changes nothing.
The answer is the group with the members that remain.
Emptying a group cannot be done through `POST api/2.0/group/{id}/members`, which needs at least one valid
account, so list every member here, or move them away with `PUT api/2.0/group/{fromId}/members/{toId}`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The ID of the group whose members are changed, taken from the route. It has to be a group that has not been  deleted, otherwise the operation answers 404. | 
 **members_request** | [**MembersRequest**](MembersRequest.md)| The accounts to add, replace with, or remove. | 

### Return type

[**GroupWrapper**](GroupWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.group_wrapper import GroupWrapper
from docspace_api_sdk.models.members_request import MembersRequest
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
    api_instance = docspace_api_sdk.GroupApi(api_client)
    id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The ID of the group whose members are changed, taken from the route. It has to be a group that has not been  deleted, otherwise the operation answers 404.
    members_request = docspace_api_sdk.MembersRequest() # MembersRequest | The accounts to add, replace with, or remove.

    try:
        # Remove group members
        api_response = api_instance.remove_members_from(id, members_request)
        print("The response of GroupApi->remove_members_from:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->remove_members_from: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The group with the members that remain |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**404** | No group has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_group_manager**
> GroupWrapper set_group_manager(id, set_manager_request)

Makes an account the manager of a group, replacing whoever managed it before.
The caller needs the permissions to edit groups and to add and remove users.
Both the group and the account have to exist: the operation answers 404 when the ID in the route matches no
live group and also when `userId` matches no account, so the message of the error says which of the two was
not found.
The account is added to the group at the same time, so a manager does not have to be a member beforehand, and
the previous manager stays in the group as an ordinary member.
A group has one manager, which makes the call idempotent when it names the account that manages it already.
The answer is the group with its new manager.
To change the members rather than the manager, use `PUT api/2.0/group/{id}/members`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The ID of the group whose manager is set, taken from the route. It has to be a group that has not been  deleted, otherwise the operation answers 404. | 
 **set_manager_request** | [**SetManagerRequest**](SetManagerRequest.md)| The account to make the manager of the group. | 

### Return type

[**GroupWrapper**](GroupWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.group_wrapper import GroupWrapper
from docspace_api_sdk.models.set_manager_request import SetManagerRequest
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
    api_instance = docspace_api_sdk.GroupApi(api_client)
    id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The ID of the group whose manager is set, taken from the route. It has to be a group that has not been  deleted, otherwise the operation answers 404.
    set_manager_request = docspace_api_sdk.SetManagerRequest() # SetManagerRequest | The account to make the manager of the group.

    try:
        # Set a group manager
        api_response = api_instance.set_group_manager(id, set_manager_request)
        print("The response of GroupApi->set_group_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->set_group_manager: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The group with its new manager |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**404** | No group has the specified ID, or no account has the specified userId |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_members_to**
> GroupWrapper set_members_to(id, members_request)

Replaces the whole member list of a group with the accounts given in the request, removing everybody who is
not in that list.
The caller needs the permissions to edit groups and to add and remove users, and the ID has to belong to a
group that has not been deleted, otherwise the operation answers 404.
At least one of the listed accounts has to be usable as a group member, otherwise the call is rejected with
400 and the group is left untouched; the accounts that cannot be members - a guest, a disabled account or an
ID that matches nobody - are then silently skipped while the rest are applied.
The replacement is not atomic: the current members are removed first and the new ones added afterwards, so a
failure in between can leave the group empty.
The answer is the group with the members it ends up with, which is why it should be read instead of assuming
the request was applied verbatim.
To add or remove a few accounts without touching the others, use `PUT api/2.0/group/{id}/members` and
`DELETE api/2.0/group/{id}/members`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The ID of the group whose members are changed, taken from the route. It has to be a group that has not been  deleted, otherwise the operation answers 404. | 
 **members_request** | [**MembersRequest**](MembersRequest.md)| The accounts to add, replace with, or remove. | 

### Return type

[**GroupWrapper**](GroupWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.group_wrapper import GroupWrapper
from docspace_api_sdk.models.members_request import MembersRequest
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
    api_instance = docspace_api_sdk.GroupApi(api_client)
    id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The ID of the group whose members are changed, taken from the route. It has to be a group that has not been  deleted, otherwise the operation answers 404.
    members_request = docspace_api_sdk.MembersRequest() # MembersRequest | The accounts to add, replace with, or remove.

    try:
        # Replace group members
        api_response = api_instance.set_members_to(id, members_request)
        print("The response of GroupApi->set_members_to:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->set_members_to: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The group with the members it ends up with |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | None of the listed accounts can be a group member |  -  |
**403** | No permissions to perform this action |  -  |
**404** | No group has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> GroupWrapper update_group(id, update_group_request)

Changes the name and the manager of a group and adds or removes members, in one call.
The caller needs the permissions to edit groups and to add and remove users, and the ID has to belong to a
group that has not been deleted, otherwise the operation answers 404.
Every field is optional and the ones that are left out are kept: omitting `groupName` keeps the current name,
and omitting `groupManager` keeps the current manager rather than clearing it.
Accounts in `membersToAdd` that cannot be group members - a guest, a disabled account or an ID that matches
nobody - are silently skipped instead of failing the call, so compare the members in the answer with what was
sent to see what was actually applied.
Members are added first and removed afterwards, an account listed in both lists therefore ends up removed,
and removing an account that is not a member changes nothing.
The change raises a `GroupUpdated` webhook, and the answer holds the group as it is after the update.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The ID of the group to update, taken from the route. It has to be a group that has not been deleted,  otherwise the operation answers 404. | 
 **update_group_request** | [**UpdateGroupRequest**](UpdateGroupRequest.md)| The fields to change. Every field is optional and the ones that are left out keep their current values, so an  empty object changes nothing. | 

### Return type

[**GroupWrapper**](GroupWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.group_wrapper import GroupWrapper
from docspace_api_sdk.models.update_group_request import UpdateGroupRequest
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
    api_instance = docspace_api_sdk.GroupApi(api_client)
    id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The ID of the group to update, taken from the route. It has to be a group that has not been deleted,  otherwise the operation answers 404.
    update_group_request = docspace_api_sdk.UpdateGroupRequest() # UpdateGroupRequest | The fields to change. Every field is optional and the ones that are left out keep their current values, so an  empty object changes nothing.

    try:
        # Update a group
        api_response = api_instance.update_group(id, update_group_request)
        print("The response of GroupApi->update_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->update_group: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The group as it is after the update |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**404** | No group has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

