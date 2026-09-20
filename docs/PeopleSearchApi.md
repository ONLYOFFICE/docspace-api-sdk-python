# docspace_api_sdk.SearchApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accounts_entries_with_files_shared**](#get_accounts_entries_with_files_shared) | **GET** /api/2.0/accounts/file/{id}/search | Search accounts for a file
[**get_accounts_entries_with_files_shared_third_party**](#get_accounts_entries_with_files_shared_third_party) | **GET** /api/2.0/accounts/file/{id}/search | Search accounts for a file (third-party storage)
[**get_accounts_entries_with_folders_shared**](#get_accounts_entries_with_folders_shared) | **GET** /api/2.0/accounts/folder/{id}/search | Search accounts for a folder
[**get_accounts_entries_with_folders_shared_third_party**](#get_accounts_entries_with_folders_shared_third_party) | **GET** /api/2.0/accounts/folder/{id}/search | Search accounts for a folder (third-party storage)
[**get_accounts_entries_with_rooms_shared**](#get_accounts_entries_with_rooms_shared) | **GET** /api/2.0/accounts/room/{id}/search | Search accounts for a room
[**get_accounts_entries_with_rooms_shared_third_party**](#get_accounts_entries_with_rooms_shared_third_party) | **GET** /api/2.0/accounts/room/{id}/search | Search accounts for a room (third-party storage)
[**get_search**](#get_search) | **GET** /api/2.0/people/@search/{query} | Search users
[**get_simple_by_filter**](#get_simple_by_filter) | **GET** /api/2.0/people/simple/filter | Filter users in brief
[**get_users_with_files_shared**](#get_users_with_files_shared) | **GET** /api/2.0/people/file/{id} | Search users for a file
[**get_users_with_files_shared_third_party**](#get_users_with_files_shared_third_party) | **GET** /api/2.0/people/file/{id} | Search users for a file (third-party storage)
[**get_users_with_folders_shared**](#get_users_with_folders_shared) | **GET** /api/2.0/people/folder/{id} | Search users for a folder
[**get_users_with_folders_shared_third_party**](#get_users_with_folders_shared_third_party) | **GET** /api/2.0/people/folder/{id} | Search users for a folder (third-party storage)
[**get_users_with_room_shared**](#get_users_with_room_shared) | **GET** /api/2.0/people/room/{id} | Search users for a room
[**get_users_with_room_shared_third_party**](#get_users_with_room_shared_third_party) | **GET** /api/2.0/people/room/{id} | Search users for a room (third-party storage)
[**search_users_by_extended_filter**](#search_users_by_extended_filter) | **GET** /api/2.0/people/filter | Filter users in detail
[**search_users_by_query**](#search_users_by_query) | **GET** /api/2.0/people/search | Search users by query
[**search_users_by_status**](#search_users_by_status) | **GET** /api/2.0/people/status/{status}/search | Search users by status filter


# **get_accounts_entries_with_files_shared**
> IAccountEntryArrayWrapper get_accounts_entries_with_files_shared(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)

Searches the portal users and groups that can be given access to the file with the ID given in the route, and
reports for each of them whether it already has access to that file.
The caller has to be allowed to manage the access of that file, and the ID has to belong to an existing file,
so the operation answers 403 for a file the caller cannot share and 404 for an ID that matches nothing.
The search is read-only and needs `filterValue`: while it is empty the operation returns an empty list and a
total of 0 instead of every account, so it cannot be used to enumerate the portal.
`filterValue` is matched case-insensitively against the first name, the last name and the email; without
`filterSeparator` it is split on spaces and every term has to match, and with a separator it is split on that
separator and any term may match.
Matching groups are streamed first and users after them, both paged together by `count` and `startIndex`,
while the number of matches is reported in the total count of the response.
Pass `excludeShared` to keep only the accounts that have no access yet, `includeShared` to keep only those
that already have it, and neither to get both kinds with the `shared` field telling them apart.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the room, folder or file whose access the search is run against, taken from the route. It is an  integer for an entry stored in DocSpace and a provider-specific string for an entry in a connected  third-party storage. | 
 **employee_status** | [**EmployeeStatus**](.md)| Keeps only the users in the given account state: `Active` for a working account, `Terminated` for a disabled  one and `Pending` for one that has not accepted its invitation yet. Omit it to search every state. | [optional] 
 **activation_status** | [**EmployeeActivationStatus**](.md)| Keeps only the users whose activation is in the given state: `NotActivated` for an account that has never  been activated, `Activated` for one that completed the activation, `Pending` for one whose invitation is  still open, and `AutoGenerated` for an account created by the portal itself. Omit it to search every state. | [optional] 
 **exclude_shared** | **bool**| Keeps only the accounts that do not have access to the entry yet, which is the set to offer when adding new  members. It takes precedence over `includeShared`, and every returned entry has `shared` set to false. | [optional] 
 **include_shared** | **bool**| Keeps only the accounts that already have access to the entry, which is the set to offer when changing or  revoking access. Every returned entry has `shared` set to true, and the flag is ignored when  `excludeShared` is also set. | [optional] 
 **invited_by_me** | **bool**| Keeps only the users invited by the caller when true, and only the users invited by somebody else when false.  Omit it to search regardless of who sent the invitation. | [optional] 
 **inviter_id** | **UUID**| Keeps only the users invited by the account with this ID. Omit it to search regardless of who sent the  invitation. | [optional] 
 **area** | [**Area**](.md)| The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only - and for a caller who is not a DocSpace  administrator, only the guests that caller is related to. | [optional] 
 **employee_types** | [**List[EmployeeType]**](EmployeeType.md)| Keeps only the users of the listed types, combined as alternatives. An empty list, which is the default,  searches every type. | [optional] 
 **count** | **int**| The size of the page, counting groups and users together. It defaults to 100, which is also the largest value  the operation accepts. | [optional] 
 **start_index** | **int**| The number of matches to skip before the page starts, counted over the groups and users together. It defaults  to 0, and the total number of matches is reported in the total count of the response. | [optional] 
 **filter_separator** | **str**| The character that splits `filterValue` into several terms, of which any one may match. Omit it to split the  value on spaces instead, in which case every term has to match. | [optional] 
 **filter_value** | **str**| The text to search for, matched case-insensitively against the first name, the last name and the email. It is  required in practice: while it is empty the search returns nothing at all rather than every account. | [optional] 

### Return type

[**IAccountEntryArrayWrapper**](IAccountEntryArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.area import Area
from docspace_api_sdk.models.employee_activation_status import EmployeeActivationStatus
from docspace_api_sdk.models.employee_status import EmployeeStatus
from docspace_api_sdk.models.employee_type import EmployeeType
from docspace_api_sdk.models.i_account_entry_array_wrapper import IAccountEntryArrayWrapper
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
    api_instance = docspace_api_sdk.SearchApi(api_client)
    id = 1234 # int | The ID of the room, folder or file whose access the search is run against, taken from the route. It is an  integer for an entry stored in DocSpace and a provider-specific string for an entry in a connected  third-party storage.
    employee_status = docspace_api_sdk.EmployeeStatus() # EmployeeStatus | Keeps only the users in the given account state: `Active` for a working account, `Terminated` for a disabled  one and `Pending` for one that has not accepted its invitation yet. Omit it to search every state. (optional)
    activation_status = docspace_api_sdk.EmployeeActivationStatus() # EmployeeActivationStatus | Keeps only the users whose activation is in the given state: `NotActivated` for an account that has never  been activated, `Activated` for one that completed the activation, `Pending` for one whose invitation is  still open, and `AutoGenerated` for an account created by the portal itself. Omit it to search every state. (optional)
    exclude_shared = false # bool | Keeps only the accounts that do not have access to the entry yet, which is the set to offer when adding new  members. It takes precedence over `includeShared`, and every returned entry has `shared` set to false. (optional)
    include_shared = false # bool | Keeps only the accounts that already have access to the entry, which is the set to offer when changing or  revoking access. Every returned entry has `shared` set to true, and the flag is ignored when  `excludeShared` is also set. (optional)
    invited_by_me = false # bool | Keeps only the users invited by the caller when true, and only the users invited by somebody else when false.  Omit it to search regardless of who sent the invitation. (optional)
    inviter_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Keeps only the users invited by the account with this ID. Omit it to search regardless of who sent the  invitation. (optional)
    area = docspace_api_sdk.Area() # Area | The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only - and for a caller who is not a DocSpace  administrator, only the guests that caller is related to. (optional)
    employee_types = [docspace_api_sdk.EmployeeType()] # List[EmployeeType] | Keeps only the users of the listed types, combined as alternatives. An empty list, which is the default,  searches every type. (optional)
    count = 25 # int | The size of the page, counting groups and users together. It defaults to 100, which is also the largest value  the operation accepts. (optional)
    start_index = 0 # int | The number of matches to skip before the page starts, counted over the groups and users together. It defaults  to 0, and the total number of matches is reported in the total count of the response. (optional)
    filter_separator = ',' # str | The character that splits `filterValue` into several terms, of which any one may match. Omit it to split the  value on spaces instead, in which case every term has to match. (optional)
    filter_value = 'John' # str | The text to search for, matched case-insensitively against the first name, the last name and the email. It is  required in practice: while it is empty the search returns nothing at all rather than every account. (optional)

    try:
        # Search accounts for a file
        api_response = api_instance.get_accounts_entries_with_files_shared(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)
        print("The response of SearchApi->get_accounts_entries_with_files_shared:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_accounts_entries_with_files_shared: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matching users and groups, each with its access state for the file |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**404** | No file has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts_entries_with_files_shared_third_party**
> IAccountEntryArrayWrapper get_accounts_entries_with_files_shared_third_party(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)

Searches the portal users and groups that can be given access to the file with the ID given in the route, and
reports for each of them whether it already has access to that file.
The caller has to be allowed to manage the access of that file, and the ID has to belong to an existing file,
so the operation answers 403 for a file the caller cannot share and 404 for an ID that matches nothing.
The search is read-only and needs `filterValue`: while it is empty the operation returns an empty list and a
total of 0 instead of every account, so it cannot be used to enumerate the portal.
`filterValue` is matched case-insensitively against the first name, the last name and the email; without
`filterSeparator` it is split on spaces and every term has to match, and with a separator it is split on that
separator and any term may match.
Matching groups are streamed first and users after them, both paged together by `count` and `startIndex`,
while the number of matches is reported in the total count of the response.
Pass `excludeShared` to keep only the accounts that have no access yet, `includeShared` to keep only those
that already have it, and neither to get both kinds with the `shared` field telling them apart.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the room, folder or file whose access the search is run against, taken from the route. It is an  integer for an entry stored in DocSpace and a provider-specific string for an entry in a connected  third-party storage. | 
 **employee_status** | [**EmployeeStatus**](.md)| Keeps only the users in the given account state: `Active` for a working account, `Terminated` for a disabled  one and `Pending` for one that has not accepted its invitation yet. Omit it to search every state. | [optional] 
 **activation_status** | [**EmployeeActivationStatus**](.md)| Keeps only the users whose activation is in the given state: `NotActivated` for an account that has never  been activated, `Activated` for one that completed the activation, `Pending` for one whose invitation is  still open, and `AutoGenerated` for an account created by the portal itself. Omit it to search every state. | [optional] 
 **exclude_shared** | **bool**| Keeps only the accounts that do not have access to the entry yet, which is the set to offer when adding new  members. It takes precedence over `includeShared`, and every returned entry has `shared` set to false. | [optional] 
 **include_shared** | **bool**| Keeps only the accounts that already have access to the entry, which is the set to offer when changing or  revoking access. Every returned entry has `shared` set to true, and the flag is ignored when  `excludeShared` is also set. | [optional] 
 **invited_by_me** | **bool**| Keeps only the users invited by the caller when true, and only the users invited by somebody else when false.  Omit it to search regardless of who sent the invitation. | [optional] 
 **inviter_id** | **UUID**| Keeps only the users invited by the account with this ID. Omit it to search regardless of who sent the  invitation. | [optional] 
 **area** | [**Area**](.md)| The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only - and for a caller who is not a DocSpace  administrator, only the guests that caller is related to. | [optional] 
 **employee_types** | [**List[EmployeeType]**](EmployeeType.md)| Keeps only the users of the listed types, combined as alternatives. An empty list, which is the default,  searches every type. | [optional] 
 **count** | **int**| The size of the page, counting groups and users together. It defaults to 100, which is also the largest value  the operation accepts. | [optional] 
 **start_index** | **int**| The number of matches to skip before the page starts, counted over the groups and users together. It defaults  to 0, and the total number of matches is reported in the total count of the response. | [optional] 
 **filter_separator** | **str**| The character that splits `filterValue` into several terms, of which any one may match. Omit it to split the  value on spaces instead, in which case every term has to match. | [optional] 
 **filter_value** | **str**| The text to search for, matched case-insensitively against the first name, the last name and the email. It is  required in practice: while it is empty the search returns nothing at all rather than every account. | [optional] 

### Return type

[**IAccountEntryArrayWrapper**](IAccountEntryArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.area import Area
from docspace_api_sdk.models.employee_activation_status import EmployeeActivationStatus
from docspace_api_sdk.models.employee_status import EmployeeStatus
from docspace_api_sdk.models.employee_type import EmployeeType
from docspace_api_sdk.models.i_account_entry_array_wrapper import IAccountEntryArrayWrapper
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
    api_instance = docspace_api_sdk.SearchApi(api_client)
    id = '1234' # str | The ID of the room, folder or file whose access the search is run against, taken from the route. It is an  integer for an entry stored in DocSpace and a provider-specific string for an entry in a connected  third-party storage.
    employee_status = docspace_api_sdk.EmployeeStatus() # EmployeeStatus | Keeps only the users in the given account state: `Active` for a working account, `Terminated` for a disabled  one and `Pending` for one that has not accepted its invitation yet. Omit it to search every state. (optional)
    activation_status = docspace_api_sdk.EmployeeActivationStatus() # EmployeeActivationStatus | Keeps only the users whose activation is in the given state: `NotActivated` for an account that has never  been activated, `Activated` for one that completed the activation, `Pending` for one whose invitation is  still open, and `AutoGenerated` for an account created by the portal itself. Omit it to search every state. (optional)
    exclude_shared = false # bool | Keeps only the accounts that do not have access to the entry yet, which is the set to offer when adding new  members. It takes precedence over `includeShared`, and every returned entry has `shared` set to false. (optional)
    include_shared = false # bool | Keeps only the accounts that already have access to the entry, which is the set to offer when changing or  revoking access. Every returned entry has `shared` set to true, and the flag is ignored when  `excludeShared` is also set. (optional)
    invited_by_me = false # bool | Keeps only the users invited by the caller when true, and only the users invited by somebody else when false.  Omit it to search regardless of who sent the invitation. (optional)
    inviter_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Keeps only the users invited by the account with this ID. Omit it to search regardless of who sent the  invitation. (optional)
    area = docspace_api_sdk.Area() # Area | The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only - and for a caller who is not a DocSpace  administrator, only the guests that caller is related to. (optional)
    employee_types = [docspace_api_sdk.EmployeeType()] # List[EmployeeType] | Keeps only the users of the listed types, combined as alternatives. An empty list, which is the default,  searches every type. (optional)
    count = 25 # int | The size of the page, counting groups and users together. It defaults to 100, which is also the largest value  the operation accepts. (optional)
    start_index = 0 # int | The number of matches to skip before the page starts, counted over the groups and users together. It defaults  to 0, and the total number of matches is reported in the total count of the response. (optional)
    filter_separator = ',' # str | The character that splits `filterValue` into several terms, of which any one may match. Omit it to split the  value on spaces instead, in which case every term has to match. (optional)
    filter_value = 'John' # str | The text to search for, matched case-insensitively against the first name, the last name and the email. It is  required in practice: while it is empty the search returns nothing at all rather than every account. (optional)

    try:
        # Search accounts for a file (third-party storage)
        api_response = api_instance.get_accounts_entries_with_files_shared_third_party(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)
        print("The response of SearchApi->get_accounts_entries_with_files_shared_third_party:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_accounts_entries_with_files_shared_third_party: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matching users and groups, each with its access state for the file |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**404** | No file has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts_entries_with_folders_shared**
> IAccountEntryArrayWrapper get_accounts_entries_with_folders_shared(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)

Searches the portal users and groups that can be given access to the folder with the ID given in the route,
and reports for each of them whether it already has access to that folder.
The caller has to be allowed to manage the access of that folder, and the ID has to belong to an existing
folder, so the operation answers 403 for a folder the caller cannot share and 404 for an ID that matches
nothing.
The search is read-only and needs `filterValue`: while it is empty the operation returns an empty list and a
total of 0 instead of every account, so it cannot be used to enumerate the portal.
`filterValue` is matched case-insensitively against the first name, the last name and the email; without
`filterSeparator` it is split on spaces and every term has to match, and with a separator it is split on that
separator and any term may match.
Matching groups are streamed first and users after them, both paged together by `count` and `startIndex`,
while the number of matches is reported in the total count of the response.
Pass `excludeShared` to keep only the accounts that have no access yet, `includeShared` to keep only those
that already have it, and neither to get both kinds with the `shared` field telling them apart.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the room, folder or file whose access the search is run against, taken from the route. It is an  integer for an entry stored in DocSpace and a provider-specific string for an entry in a connected  third-party storage. | 
 **employee_status** | [**EmployeeStatus**](.md)| Keeps only the users in the given account state: `Active` for a working account, `Terminated` for a disabled  one and `Pending` for one that has not accepted its invitation yet. Omit it to search every state. | [optional] 
 **activation_status** | [**EmployeeActivationStatus**](.md)| Keeps only the users whose activation is in the given state: `NotActivated` for an account that has never  been activated, `Activated` for one that completed the activation, `Pending` for one whose invitation is  still open, and `AutoGenerated` for an account created by the portal itself. Omit it to search every state. | [optional] 
 **exclude_shared** | **bool**| Keeps only the accounts that do not have access to the entry yet, which is the set to offer when adding new  members. It takes precedence over `includeShared`, and every returned entry has `shared` set to false. | [optional] 
 **include_shared** | **bool**| Keeps only the accounts that already have access to the entry, which is the set to offer when changing or  revoking access. Every returned entry has `shared` set to true, and the flag is ignored when  `excludeShared` is also set. | [optional] 
 **invited_by_me** | **bool**| Keeps only the users invited by the caller when true, and only the users invited by somebody else when false.  Omit it to search regardless of who sent the invitation. | [optional] 
 **inviter_id** | **UUID**| Keeps only the users invited by the account with this ID. Omit it to search regardless of who sent the  invitation. | [optional] 
 **area** | [**Area**](.md)| The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only - and for a caller who is not a DocSpace  administrator, only the guests that caller is related to. | [optional] 
 **employee_types** | [**List[EmployeeType]**](EmployeeType.md)| Keeps only the users of the listed types, combined as alternatives. An empty list, which is the default,  searches every type. | [optional] 
 **count** | **int**| The size of the page, counting groups and users together. It defaults to 100, which is also the largest value  the operation accepts. | [optional] 
 **start_index** | **int**| The number of matches to skip before the page starts, counted over the groups and users together. It defaults  to 0, and the total number of matches is reported in the total count of the response. | [optional] 
 **filter_separator** | **str**| The character that splits `filterValue` into several terms, of which any one may match. Omit it to split the  value on spaces instead, in which case every term has to match. | [optional] 
 **filter_value** | **str**| The text to search for, matched case-insensitively against the first name, the last name and the email. It is  required in practice: while it is empty the search returns nothing at all rather than every account. | [optional] 

### Return type

[**IAccountEntryArrayWrapper**](IAccountEntryArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.area import Area
from docspace_api_sdk.models.employee_activation_status import EmployeeActivationStatus
from docspace_api_sdk.models.employee_status import EmployeeStatus
from docspace_api_sdk.models.employee_type import EmployeeType
from docspace_api_sdk.models.i_account_entry_array_wrapper import IAccountEntryArrayWrapper
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
    api_instance = docspace_api_sdk.SearchApi(api_client)
    id = 1234 # int | The ID of the room, folder or file whose access the search is run against, taken from the route. It is an  integer for an entry stored in DocSpace and a provider-specific string for an entry in a connected  third-party storage.
    employee_status = docspace_api_sdk.EmployeeStatus() # EmployeeStatus | Keeps only the users in the given account state: `Active` for a working account, `Terminated` for a disabled  one and `Pending` for one that has not accepted its invitation yet. Omit it to search every state. (optional)
    activation_status = docspace_api_sdk.EmployeeActivationStatus() # EmployeeActivationStatus | Keeps only the users whose activation is in the given state: `NotActivated` for an account that has never  been activated, `Activated` for one that completed the activation, `Pending` for one whose invitation is  still open, and `AutoGenerated` for an account created by the portal itself. Omit it to search every state. (optional)
    exclude_shared = false # bool | Keeps only the accounts that do not have access to the entry yet, which is the set to offer when adding new  members. It takes precedence over `includeShared`, and every returned entry has `shared` set to false. (optional)
    include_shared = false # bool | Keeps only the accounts that already have access to the entry, which is the set to offer when changing or  revoking access. Every returned entry has `shared` set to true, and the flag is ignored when  `excludeShared` is also set. (optional)
    invited_by_me = false # bool | Keeps only the users invited by the caller when true, and only the users invited by somebody else when false.  Omit it to search regardless of who sent the invitation. (optional)
    inviter_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Keeps only the users invited by the account with this ID. Omit it to search regardless of who sent the  invitation. (optional)
    area = docspace_api_sdk.Area() # Area | The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only - and for a caller who is not a DocSpace  administrator, only the guests that caller is related to. (optional)
    employee_types = [docspace_api_sdk.EmployeeType()] # List[EmployeeType] | Keeps only the users of the listed types, combined as alternatives. An empty list, which is the default,  searches every type. (optional)
    count = 25 # int | The size of the page, counting groups and users together. It defaults to 100, which is also the largest value  the operation accepts. (optional)
    start_index = 0 # int | The number of matches to skip before the page starts, counted over the groups and users together. It defaults  to 0, and the total number of matches is reported in the total count of the response. (optional)
    filter_separator = ',' # str | The character that splits `filterValue` into several terms, of which any one may match. Omit it to split the  value on spaces instead, in which case every term has to match. (optional)
    filter_value = 'John' # str | The text to search for, matched case-insensitively against the first name, the last name and the email. It is  required in practice: while it is empty the search returns nothing at all rather than every account. (optional)

    try:
        # Search accounts for a folder
        api_response = api_instance.get_accounts_entries_with_folders_shared(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)
        print("The response of SearchApi->get_accounts_entries_with_folders_shared:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_accounts_entries_with_folders_shared: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matching users and groups, each with its access state for the folder |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**404** | No folder has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts_entries_with_folders_shared_third_party**
> IAccountEntryArrayWrapper get_accounts_entries_with_folders_shared_third_party(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)

Searches the portal users and groups that can be given access to the folder with the ID given in the route,
and reports for each of them whether it already has access to that folder.
The caller has to be allowed to manage the access of that folder, and the ID has to belong to an existing
folder, so the operation answers 403 for a folder the caller cannot share and 404 for an ID that matches
nothing.
The search is read-only and needs `filterValue`: while it is empty the operation returns an empty list and a
total of 0 instead of every account, so it cannot be used to enumerate the portal.
`filterValue` is matched case-insensitively against the first name, the last name and the email; without
`filterSeparator` it is split on spaces and every term has to match, and with a separator it is split on that
separator and any term may match.
Matching groups are streamed first and users after them, both paged together by `count` and `startIndex`,
while the number of matches is reported in the total count of the response.
Pass `excludeShared` to keep only the accounts that have no access yet, `includeShared` to keep only those
that already have it, and neither to get both kinds with the `shared` field telling them apart.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the room, folder or file whose access the search is run against, taken from the route. It is an  integer for an entry stored in DocSpace and a provider-specific string for an entry in a connected  third-party storage. | 
 **employee_status** | [**EmployeeStatus**](.md)| Keeps only the users in the given account state: `Active` for a working account, `Terminated` for a disabled  one and `Pending` for one that has not accepted its invitation yet. Omit it to search every state. | [optional] 
 **activation_status** | [**EmployeeActivationStatus**](.md)| Keeps only the users whose activation is in the given state: `NotActivated` for an account that has never  been activated, `Activated` for one that completed the activation, `Pending` for one whose invitation is  still open, and `AutoGenerated` for an account created by the portal itself. Omit it to search every state. | [optional] 
 **exclude_shared** | **bool**| Keeps only the accounts that do not have access to the entry yet, which is the set to offer when adding new  members. It takes precedence over `includeShared`, and every returned entry has `shared` set to false. | [optional] 
 **include_shared** | **bool**| Keeps only the accounts that already have access to the entry, which is the set to offer when changing or  revoking access. Every returned entry has `shared` set to true, and the flag is ignored when  `excludeShared` is also set. | [optional] 
 **invited_by_me** | **bool**| Keeps only the users invited by the caller when true, and only the users invited by somebody else when false.  Omit it to search regardless of who sent the invitation. | [optional] 
 **inviter_id** | **UUID**| Keeps only the users invited by the account with this ID. Omit it to search regardless of who sent the  invitation. | [optional] 
 **area** | [**Area**](.md)| The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only - and for a caller who is not a DocSpace  administrator, only the guests that caller is related to. | [optional] 
 **employee_types** | [**List[EmployeeType]**](EmployeeType.md)| Keeps only the users of the listed types, combined as alternatives. An empty list, which is the default,  searches every type. | [optional] 
 **count** | **int**| The size of the page, counting groups and users together. It defaults to 100, which is also the largest value  the operation accepts. | [optional] 
 **start_index** | **int**| The number of matches to skip before the page starts, counted over the groups and users together. It defaults  to 0, and the total number of matches is reported in the total count of the response. | [optional] 
 **filter_separator** | **str**| The character that splits `filterValue` into several terms, of which any one may match. Omit it to split the  value on spaces instead, in which case every term has to match. | [optional] 
 **filter_value** | **str**| The text to search for, matched case-insensitively against the first name, the last name and the email. It is  required in practice: while it is empty the search returns nothing at all rather than every account. | [optional] 

### Return type

[**IAccountEntryArrayWrapper**](IAccountEntryArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.area import Area
from docspace_api_sdk.models.employee_activation_status import EmployeeActivationStatus
from docspace_api_sdk.models.employee_status import EmployeeStatus
from docspace_api_sdk.models.employee_type import EmployeeType
from docspace_api_sdk.models.i_account_entry_array_wrapper import IAccountEntryArrayWrapper
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
    api_instance = docspace_api_sdk.SearchApi(api_client)
    id = '1234' # str | The ID of the room, folder or file whose access the search is run against, taken from the route. It is an  integer for an entry stored in DocSpace and a provider-specific string for an entry in a connected  third-party storage.
    employee_status = docspace_api_sdk.EmployeeStatus() # EmployeeStatus | Keeps only the users in the given account state: `Active` for a working account, `Terminated` for a disabled  one and `Pending` for one that has not accepted its invitation yet. Omit it to search every state. (optional)
    activation_status = docspace_api_sdk.EmployeeActivationStatus() # EmployeeActivationStatus | Keeps only the users whose activation is in the given state: `NotActivated` for an account that has never  been activated, `Activated` for one that completed the activation, `Pending` for one whose invitation is  still open, and `AutoGenerated` for an account created by the portal itself. Omit it to search every state. (optional)
    exclude_shared = false # bool | Keeps only the accounts that do not have access to the entry yet, which is the set to offer when adding new  members. It takes precedence over `includeShared`, and every returned entry has `shared` set to false. (optional)
    include_shared = false # bool | Keeps only the accounts that already have access to the entry, which is the set to offer when changing or  revoking access. Every returned entry has `shared` set to true, and the flag is ignored when  `excludeShared` is also set. (optional)
    invited_by_me = false # bool | Keeps only the users invited by the caller when true, and only the users invited by somebody else when false.  Omit it to search regardless of who sent the invitation. (optional)
    inviter_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Keeps only the users invited by the account with this ID. Omit it to search regardless of who sent the  invitation. (optional)
    area = docspace_api_sdk.Area() # Area | The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only - and for a caller who is not a DocSpace  administrator, only the guests that caller is related to. (optional)
    employee_types = [docspace_api_sdk.EmployeeType()] # List[EmployeeType] | Keeps only the users of the listed types, combined as alternatives. An empty list, which is the default,  searches every type. (optional)
    count = 25 # int | The size of the page, counting groups and users together. It defaults to 100, which is also the largest value  the operation accepts. (optional)
    start_index = 0 # int | The number of matches to skip before the page starts, counted over the groups and users together. It defaults  to 0, and the total number of matches is reported in the total count of the response. (optional)
    filter_separator = ',' # str | The character that splits `filterValue` into several terms, of which any one may match. Omit it to split the  value on spaces instead, in which case every term has to match. (optional)
    filter_value = 'John' # str | The text to search for, matched case-insensitively against the first name, the last name and the email. It is  required in practice: while it is empty the search returns nothing at all rather than every account. (optional)

    try:
        # Search accounts for a folder (third-party storage)
        api_response = api_instance.get_accounts_entries_with_folders_shared_third_party(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)
        print("The response of SearchApi->get_accounts_entries_with_folders_shared_third_party:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_accounts_entries_with_folders_shared_third_party: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matching users and groups, each with its access state for the folder |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**404** | No folder has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts_entries_with_rooms_shared**
> IAccountEntryArrayWrapper get_accounts_entries_with_rooms_shared(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)

Searches the portal users and groups that can be given access to the room with the ID given in the route, and
reports for each of them whether it already has access to that room.
The caller has to be allowed to manage the access of that room, and the ID has to belong to an existing room,
so the operation answers 403 for a room the caller cannot share and 404 for an ID that matches nothing.
The search is read-only and needs `filterValue`: while it is empty the operation returns an empty list and a
total of 0 instead of every account, so it cannot be used to enumerate the portal.
`filterValue` is matched case-insensitively against the first name, the last name and the email; without
`filterSeparator` it is split on spaces and every term has to match, and with a separator it is split on that
separator and any term may match.
Matching groups are streamed first and users after them, both paged together by `count` and `startIndex`,
while the number of matches is reported in the total count of the response.
Pass `excludeShared` to keep only the accounts that have no access yet, `includeShared` to keep only those
that already have it, and neither to get both kinds with the `shared` field telling them apart.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the room, folder or file whose access the search is run against, taken from the route. It is an  integer for an entry stored in DocSpace and a provider-specific string for an entry in a connected  third-party storage. | 
 **employee_status** | [**EmployeeStatus**](.md)| Keeps only the users in the given account state: `Active` for a working account, `Terminated` for a disabled  one and `Pending` for one that has not accepted its invitation yet. Omit it to search every state. | [optional] 
 **activation_status** | [**EmployeeActivationStatus**](.md)| Keeps only the users whose activation is in the given state: `NotActivated` for an account that has never  been activated, `Activated` for one that completed the activation, `Pending` for one whose invitation is  still open, and `AutoGenerated` for an account created by the portal itself. Omit it to search every state. | [optional] 
 **exclude_shared** | **bool**| Keeps only the accounts that do not have access to the entry yet, which is the set to offer when adding new  members. It takes precedence over `includeShared`, and every returned entry has `shared` set to false. | [optional] 
 **include_shared** | **bool**| Keeps only the accounts that already have access to the entry, which is the set to offer when changing or  revoking access. Every returned entry has `shared` set to true, and the flag is ignored when  `excludeShared` is also set. | [optional] 
 **invited_by_me** | **bool**| Keeps only the users invited by the caller when true, and only the users invited by somebody else when false.  Omit it to search regardless of who sent the invitation. | [optional] 
 **inviter_id** | **UUID**| Keeps only the users invited by the account with this ID. Omit it to search regardless of who sent the  invitation. | [optional] 
 **area** | [**Area**](.md)| The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only - and for a caller who is not a DocSpace  administrator, only the guests that caller is related to. | [optional] 
 **employee_types** | [**List[EmployeeType]**](EmployeeType.md)| Keeps only the users of the listed types, combined as alternatives. An empty list, which is the default,  searches every type. | [optional] 
 **count** | **int**| The size of the page, counting groups and users together. It defaults to 100, which is also the largest value  the operation accepts. | [optional] 
 **start_index** | **int**| The number of matches to skip before the page starts, counted over the groups and users together. It defaults  to 0, and the total number of matches is reported in the total count of the response. | [optional] 
 **filter_separator** | **str**| The character that splits `filterValue` into several terms, of which any one may match. Omit it to split the  value on spaces instead, in which case every term has to match. | [optional] 
 **filter_value** | **str**| The text to search for, matched case-insensitively against the first name, the last name and the email. It is  required in practice: while it is empty the search returns nothing at all rather than every account. | [optional] 

### Return type

[**IAccountEntryArrayWrapper**](IAccountEntryArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.area import Area
from docspace_api_sdk.models.employee_activation_status import EmployeeActivationStatus
from docspace_api_sdk.models.employee_status import EmployeeStatus
from docspace_api_sdk.models.employee_type import EmployeeType
from docspace_api_sdk.models.i_account_entry_array_wrapper import IAccountEntryArrayWrapper
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
    api_instance = docspace_api_sdk.SearchApi(api_client)
    id = 1234 # int | The ID of the room, folder or file whose access the search is run against, taken from the route. It is an  integer for an entry stored in DocSpace and a provider-specific string for an entry in a connected  third-party storage.
    employee_status = docspace_api_sdk.EmployeeStatus() # EmployeeStatus | Keeps only the users in the given account state: `Active` for a working account, `Terminated` for a disabled  one and `Pending` for one that has not accepted its invitation yet. Omit it to search every state. (optional)
    activation_status = docspace_api_sdk.EmployeeActivationStatus() # EmployeeActivationStatus | Keeps only the users whose activation is in the given state: `NotActivated` for an account that has never  been activated, `Activated` for one that completed the activation, `Pending` for one whose invitation is  still open, and `AutoGenerated` for an account created by the portal itself. Omit it to search every state. (optional)
    exclude_shared = false # bool | Keeps only the accounts that do not have access to the entry yet, which is the set to offer when adding new  members. It takes precedence over `includeShared`, and every returned entry has `shared` set to false. (optional)
    include_shared = false # bool | Keeps only the accounts that already have access to the entry, which is the set to offer when changing or  revoking access. Every returned entry has `shared` set to true, and the flag is ignored when  `excludeShared` is also set. (optional)
    invited_by_me = false # bool | Keeps only the users invited by the caller when true, and only the users invited by somebody else when false.  Omit it to search regardless of who sent the invitation. (optional)
    inviter_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Keeps only the users invited by the account with this ID. Omit it to search regardless of who sent the  invitation. (optional)
    area = docspace_api_sdk.Area() # Area | The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only - and for a caller who is not a DocSpace  administrator, only the guests that caller is related to. (optional)
    employee_types = [docspace_api_sdk.EmployeeType()] # List[EmployeeType] | Keeps only the users of the listed types, combined as alternatives. An empty list, which is the default,  searches every type. (optional)
    count = 25 # int | The size of the page, counting groups and users together. It defaults to 100, which is also the largest value  the operation accepts. (optional)
    start_index = 0 # int | The number of matches to skip before the page starts, counted over the groups and users together. It defaults  to 0, and the total number of matches is reported in the total count of the response. (optional)
    filter_separator = ',' # str | The character that splits `filterValue` into several terms, of which any one may match. Omit it to split the  value on spaces instead, in which case every term has to match. (optional)
    filter_value = 'John' # str | The text to search for, matched case-insensitively against the first name, the last name and the email. It is  required in practice: while it is empty the search returns nothing at all rather than every account. (optional)

    try:
        # Search accounts for a room
        api_response = api_instance.get_accounts_entries_with_rooms_shared(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)
        print("The response of SearchApi->get_accounts_entries_with_rooms_shared:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_accounts_entries_with_rooms_shared: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matching users and groups, each with its access state for the room |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**404** | No room has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts_entries_with_rooms_shared_third_party**
> IAccountEntryArrayWrapper get_accounts_entries_with_rooms_shared_third_party(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)

Searches the portal users and groups that can be given access to the room with the ID given in the route, and
reports for each of them whether it already has access to that room.
The caller has to be allowed to manage the access of that room, and the ID has to belong to an existing room,
so the operation answers 403 for a room the caller cannot share and 404 for an ID that matches nothing.
The search is read-only and needs `filterValue`: while it is empty the operation returns an empty list and a
total of 0 instead of every account, so it cannot be used to enumerate the portal.
`filterValue` is matched case-insensitively against the first name, the last name and the email; without
`filterSeparator` it is split on spaces and every term has to match, and with a separator it is split on that
separator and any term may match.
Matching groups are streamed first and users after them, both paged together by `count` and `startIndex`,
while the number of matches is reported in the total count of the response.
Pass `excludeShared` to keep only the accounts that have no access yet, `includeShared` to keep only those
that already have it, and neither to get both kinds with the `shared` field telling them apart.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the room, folder or file whose access the search is run against, taken from the route. It is an  integer for an entry stored in DocSpace and a provider-specific string for an entry in a connected  third-party storage. | 
 **employee_status** | [**EmployeeStatus**](.md)| Keeps only the users in the given account state: `Active` for a working account, `Terminated` for a disabled  one and `Pending` for one that has not accepted its invitation yet. Omit it to search every state. | [optional] 
 **activation_status** | [**EmployeeActivationStatus**](.md)| Keeps only the users whose activation is in the given state: `NotActivated` for an account that has never  been activated, `Activated` for one that completed the activation, `Pending` for one whose invitation is  still open, and `AutoGenerated` for an account created by the portal itself. Omit it to search every state. | [optional] 
 **exclude_shared** | **bool**| Keeps only the accounts that do not have access to the entry yet, which is the set to offer when adding new  members. It takes precedence over `includeShared`, and every returned entry has `shared` set to false. | [optional] 
 **include_shared** | **bool**| Keeps only the accounts that already have access to the entry, which is the set to offer when changing or  revoking access. Every returned entry has `shared` set to true, and the flag is ignored when  `excludeShared` is also set. | [optional] 
 **invited_by_me** | **bool**| Keeps only the users invited by the caller when true, and only the users invited by somebody else when false.  Omit it to search regardless of who sent the invitation. | [optional] 
 **inviter_id** | **UUID**| Keeps only the users invited by the account with this ID. Omit it to search regardless of who sent the  invitation. | [optional] 
 **area** | [**Area**](.md)| The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only - and for a caller who is not a DocSpace  administrator, only the guests that caller is related to. | [optional] 
 **employee_types** | [**List[EmployeeType]**](EmployeeType.md)| Keeps only the users of the listed types, combined as alternatives. An empty list, which is the default,  searches every type. | [optional] 
 **count** | **int**| The size of the page, counting groups and users together. It defaults to 100, which is also the largest value  the operation accepts. | [optional] 
 **start_index** | **int**| The number of matches to skip before the page starts, counted over the groups and users together. It defaults  to 0, and the total number of matches is reported in the total count of the response. | [optional] 
 **filter_separator** | **str**| The character that splits `filterValue` into several terms, of which any one may match. Omit it to split the  value on spaces instead, in which case every term has to match. | [optional] 
 **filter_value** | **str**| The text to search for, matched case-insensitively against the first name, the last name and the email. It is  required in practice: while it is empty the search returns nothing at all rather than every account. | [optional] 

### Return type

[**IAccountEntryArrayWrapper**](IAccountEntryArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.area import Area
from docspace_api_sdk.models.employee_activation_status import EmployeeActivationStatus
from docspace_api_sdk.models.employee_status import EmployeeStatus
from docspace_api_sdk.models.employee_type import EmployeeType
from docspace_api_sdk.models.i_account_entry_array_wrapper import IAccountEntryArrayWrapper
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
    api_instance = docspace_api_sdk.SearchApi(api_client)
    id = '1234' # str | The ID of the room, folder or file whose access the search is run against, taken from the route. It is an  integer for an entry stored in DocSpace and a provider-specific string for an entry in a connected  third-party storage.
    employee_status = docspace_api_sdk.EmployeeStatus() # EmployeeStatus | Keeps only the users in the given account state: `Active` for a working account, `Terminated` for a disabled  one and `Pending` for one that has not accepted its invitation yet. Omit it to search every state. (optional)
    activation_status = docspace_api_sdk.EmployeeActivationStatus() # EmployeeActivationStatus | Keeps only the users whose activation is in the given state: `NotActivated` for an account that has never  been activated, `Activated` for one that completed the activation, `Pending` for one whose invitation is  still open, and `AutoGenerated` for an account created by the portal itself. Omit it to search every state. (optional)
    exclude_shared = false # bool | Keeps only the accounts that do not have access to the entry yet, which is the set to offer when adding new  members. It takes precedence over `includeShared`, and every returned entry has `shared` set to false. (optional)
    include_shared = false # bool | Keeps only the accounts that already have access to the entry, which is the set to offer when changing or  revoking access. Every returned entry has `shared` set to true, and the flag is ignored when  `excludeShared` is also set. (optional)
    invited_by_me = false # bool | Keeps only the users invited by the caller when true, and only the users invited by somebody else when false.  Omit it to search regardless of who sent the invitation. (optional)
    inviter_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Keeps only the users invited by the account with this ID. Omit it to search regardless of who sent the  invitation. (optional)
    area = docspace_api_sdk.Area() # Area | The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only - and for a caller who is not a DocSpace  administrator, only the guests that caller is related to. (optional)
    employee_types = [docspace_api_sdk.EmployeeType()] # List[EmployeeType] | Keeps only the users of the listed types, combined as alternatives. An empty list, which is the default,  searches every type. (optional)
    count = 25 # int | The size of the page, counting groups and users together. It defaults to 100, which is also the largest value  the operation accepts. (optional)
    start_index = 0 # int | The number of matches to skip before the page starts, counted over the groups and users together. It defaults  to 0, and the total number of matches is reported in the total count of the response. (optional)
    filter_separator = ',' # str | The character that splits `filterValue` into several terms, of which any one may match. Omit it to split the  value on spaces instead, in which case every term has to match. (optional)
    filter_value = 'John' # str | The text to search for, matched case-insensitively against the first name, the last name and the email. It is  required in practice: while it is empty the search returns nothing at all rather than every account. (optional)

    try:
        # Search accounts for a room (third-party storage)
        api_response = api_instance.get_accounts_entries_with_rooms_shared_third_party(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)
        print("The response of SearchApi->get_accounts_entries_with_rooms_shared_third_party:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_accounts_entries_with_rooms_shared_third_party: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matching users and groups, each with its access state for the room |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**404** | No room has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search**
> EmployeeFullArrayWrapper get_search(query, filter_by=filter_by, filter_value=filter_value)

Searches the active accounts of the portal by a term taken from the path, and is the same search as
`GET api/2.0/people/search`, which takes the term in the query string instead.
Only a DocSpace administrator may call it; every other account, including a room admin, gets 403.
Only accounts with the `Active` status are searched, so a pending invitation and a disabled account are never
found - use `GET api/2.0/people/filter` to search across states.
The call is read-only and is not paged: every match is streamed, without a total.
`filterBy` set to `group` turns `text` into a group ID and keeps only the members of that group, so `text`
then has to be a valid identifier.
The answer holds full profiles.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The term to look for, taken from the route. Only accounts with the `Active` status are searched. | 
 **filter_by** | **str**| The only recognised value is `group`, which turns `filterValue` into a group ID and keeps only the members of  that group. Any other value, and omitting the field, applies no group filter. | [optional] 
 **filter_value** | **str**| The group ID to keep the members of, used only when `filterBy` is `group`. It has to be a valid identifier -  a group name is not accepted. | [optional] 

### Return type

[**EmployeeFullArrayWrapper**](EmployeeFullArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.employee_full_array_wrapper import EmployeeFullArrayWrapper
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
    api_instance = docspace_api_sdk.SearchApi(api_client)
    query = 'John' # str | The term to look for, taken from the route. Only accounts with the `Active` status are searched.
    filter_by = 'group' # str | The only recognised value is `group`, which turns `filterValue` into a group ID and keeps only the members of  that group. Any other value, and omitting the field, applies no group filter. (optional)
    filter_value = '00000000-0000-0000-0000-000000000000' # str | The group ID to keep the members of, used only when `filterBy` is `group`. It has to be a valid identifier -  a group name is not accepted. (optional)

    try:
        # Search users
        api_response = api_instance.get_search(query, filter_by=filter_by, filter_value=filter_value)
        print("The response of SearchApi->get_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_search: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The full profiles of the matching active accounts |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_simple_by_filter**
> EmployeeArrayWrapper get_simple_by_filter(employee_status=employee_status, group_id=group_id, activation_status=activation_status, employee_type=employee_type, employee_types=employee_types, is_administrator=is_administrator, payments=payments, account_login_type=account_login_type, quota_filter=quota_filter, without_group=without_group, exclude_group=exclude_group, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_separator=filter_separator, filter_value=filter_value)

Returns a page of portal accounts selected by the full set of account filters, with the short profile of each
of them - the identifying fields, the avatar and the display name, without the contacts, the groups or the
quota.
The caller has to be a room admin, a DocSpace admin or a People module admin; a member or a guest gets 403.
The call is read-only, paged by `count` and `startIndex`, ordered by `sortBy` and `sortOrder`, and reports
the number of matches in the total count of the response.
It accepts exactly the same filters as `GET api/2.0/people/filter` and differs only in how much of each
profile comes back, so prefer this one for pickers, mentions and any list that shows names, and switch to the
other only when the full profile is needed.
Filters combine as conditions that all have to hold, and the same interactions apply: `withoutGroup` makes
`groupId` irrelevant, `employeeType` wins over `employeeTypes`, and `area` cancels the type filters that
contradict it.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_status** | [**EmployeeStatus**](.md)| Keeps only the accounts in the given state: `Active` for working accounts, `Terminated` for disabled ones  and `Pending` for open invitations. Omit it to search every state. | [optional] 
 **group_id** | **UUID**| Keeps only the members of this group, or excludes them when `excludeGroup` is true. It is ignored when  `withoutGroup` is set. | [optional] 
 **activation_status** | [**EmployeeActivationStatus**](.md)| Keeps only the accounts whose activation is in the given state: `NotActivated`, `Activated`, `Pending` or  `AutoGenerated`. Omit it to search every state. | [optional] 
 **employee_type** | [**EmployeeType**](.md)| Keeps only the accounts of this single type: `DocSpaceAdmin`, `RoomAdmin`, `User` or `Guest`. When it is  sent it wins over `employeeTypes`, and a type that contradicts `area` is dropped. | [optional] 
 **employee_types** | [**List[int]**](int.md)| Keeps the accounts of any of the listed types, combined as alternatives. It is ignored when `employeeType`  is also sent. | [optional] 
 **is_administrator** | **bool**| Set it to true to keep only the DocSpace administrators and the module administrators. Setting it to false  is the same as omitting it and does not exclude administrators. | [optional] 
 **payments** | [**Payments**](.md)| Keeps only the accounts that take a paid seat when `Paid`, or only the guests and members that do not when  `Free`. Omit it to search both. | [optional] 
 **account_login_type** | [**AccountLoginType**](.md)| Keeps only the accounts that sign in this way: `SSO`, `LDAP`, or `Standart` for an ordinary portal  password. Omit it to search all of them. | [optional] 
 **quota_filter** | [**QuotaFilter**](.md)| Keeps only the accounts whose storage quota is the portal default when `Default`, or set individually when  `Custom`. `All`, which is the same as omitting the field, searches both. | [optional] 
 **without_group** | **bool**| Set it to true to keep only the accounts that belong to no group at all, which makes `groupId` and  `excludeGroup` irrelevant. | [optional] 
 **exclude_group** | **bool**| Inverts `groupId`: with true the members of that group are left out instead of being the only ones kept. It  has no effect without `groupId`. | [optional] 
 **invited_by_me** | **bool**| Keeps only the accounts invited by the caller when true, and only those invited by somebody else when  false. Omit it to search regardless of who sent the invitation. | [optional] 
 **inviter_id** | **UUID**| Keeps only the accounts invited by the account with this ID. Omit it to search regardless of who sent the  invitation. | [optional] 
 **area** | [**Area**](.md)| The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only. It also cancels the type filters that contradict  it. | [optional] 
 **count** | **int**| The size of the page. It defaults to 100, which is also the largest value the operation accepts. | [optional] 
 **start_index** | **int**| The number of matches to skip before the page starts. It defaults to 0, and the total number of matches is  reported in the total count of the response. | [optional] 
 **sort_by** | **str**| What to order the accounts by, compared without regard to case: `FirstName`, `LastName`, `DisplayName`,  `Type`, `Email`, `Department`, `UsedSpace`, `CreatedBy` or `RegistrationDate`. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The direction of the ordering: `Ascending`, which is the default, or `Descending`. | [optional] 
 **filter_separator** | **str**| The character that splits `filterValue` into several terms, of which any one may match. Omit it to split  the value on spaces instead, in which case every term has to match. | [optional] 
 **filter_value** | **str**| The text to match against the first name, the last name and the email, case-insensitively. Omit it to apply  no text filter at all. | [optional] 

### Return type

[**EmployeeArrayWrapper**](EmployeeArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.account_login_type import AccountLoginType
from docspace_api_sdk.models.area import Area
from docspace_api_sdk.models.employee_activation_status import EmployeeActivationStatus
from docspace_api_sdk.models.employee_array_wrapper import EmployeeArrayWrapper
from docspace_api_sdk.models.employee_status import EmployeeStatus
from docspace_api_sdk.models.employee_type import EmployeeType
from docspace_api_sdk.models.payments import Payments
from docspace_api_sdk.models.quota_filter import QuotaFilter
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
    api_instance = docspace_api_sdk.SearchApi(api_client)
    employee_status = docspace_api_sdk.EmployeeStatus() # EmployeeStatus | Keeps only the accounts in the given state: `Active` for working accounts, `Terminated` for disabled ones  and `Pending` for open invitations. Omit it to search every state. (optional)
    group_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Keeps only the members of this group, or excludes them when `excludeGroup` is true. It is ignored when  `withoutGroup` is set. (optional)
    activation_status = docspace_api_sdk.EmployeeActivationStatus() # EmployeeActivationStatus | Keeps only the accounts whose activation is in the given state: `NotActivated`, `Activated`, `Pending` or  `AutoGenerated`. Omit it to search every state. (optional)
    employee_type = docspace_api_sdk.EmployeeType() # EmployeeType | Keeps only the accounts of this single type: `DocSpaceAdmin`, `RoomAdmin`, `User` or `Guest`. When it is  sent it wins over `employeeTypes`, and a type that contradicts `area` is dropped. (optional)
    employee_types = [[RoomAdmin, Guest]] # List[int] | Keeps the accounts of any of the listed types, combined as alternatives. It is ignored when `employeeType`  is also sent. (optional)
    is_administrator = false # bool | Set it to true to keep only the DocSpace administrators and the module administrators. Setting it to false  is the same as omitting it and does not exclude administrators. (optional)
    payments = docspace_api_sdk.Payments() # Payments | Keeps only the accounts that take a paid seat when `Paid`, or only the guests and members that do not when  `Free`. Omit it to search both. (optional)
    account_login_type = docspace_api_sdk.AccountLoginType() # AccountLoginType | Keeps only the accounts that sign in this way: `SSO`, `LDAP`, or `Standart` for an ordinary portal  password. Omit it to search all of them. (optional)
    quota_filter = docspace_api_sdk.QuotaFilter() # QuotaFilter | Keeps only the accounts whose storage quota is the portal default when `Default`, or set individually when  `Custom`. `All`, which is the same as omitting the field, searches both. (optional)
    without_group = false # bool | Set it to true to keep only the accounts that belong to no group at all, which makes `groupId` and  `excludeGroup` irrelevant. (optional)
    exclude_group = false # bool | Inverts `groupId`: with true the members of that group are left out instead of being the only ones kept. It  has no effect without `groupId`. (optional)
    invited_by_me = false # bool | Keeps only the accounts invited by the caller when true, and only those invited by somebody else when  false. Omit it to search regardless of who sent the invitation. (optional)
    inviter_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Keeps only the accounts invited by the account with this ID. Omit it to search regardless of who sent the  invitation. (optional)
    area = docspace_api_sdk.Area() # Area | The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only. It also cancels the type filters that contradict  it. (optional)
    count = 25 # int | The size of the page. It defaults to 100, which is also the largest value the operation accepts. (optional)
    start_index = 0 # int | The number of matches to skip before the page starts. It defaults to 0, and the total number of matches is  reported in the total count of the response. (optional)
    sort_by = 'DisplayName' # str | What to order the accounts by, compared without regard to case: `FirstName`, `LastName`, `DisplayName`,  `Type`, `Email`, `Department`, `UsedSpace`, `CreatedBy` or `RegistrationDate`. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The direction of the ordering: `Ascending`, which is the default, or `Descending`. (optional)
    filter_separator = ',' # str | The character that splits `filterValue` into several terms, of which any one may match. Omit it to split  the value on spaces instead, in which case every term has to match. (optional)
    filter_value = 'John' # str | The text to match against the first name, the last name and the email, case-insensitively. Omit it to apply  no text filter at all. (optional)

    try:
        # Filter users in brief
        api_response = api_instance.get_simple_by_filter(employee_status=employee_status, group_id=group_id, activation_status=activation_status, employee_type=employee_type, employee_types=employee_types, is_administrator=is_administrator, payments=payments, account_login_type=account_login_type, quota_filter=quota_filter, without_group=without_group, exclude_group=exclude_group, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_separator=filter_separator, filter_value=filter_value)
        print("The response of SearchApi->get_simple_by_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_simple_by_filter: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of matching accounts, with their short profiles |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is a member or a guest |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_with_files_shared**
> EmployeeFullArrayWrapper get_users_with_files_shared(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)

Returns the accounts that are relevant to the file with the ID given in the route, and reports for each of
them whether it already has access to that file.
The caller only needs read access to the file, not the right to manage its access, but a guest may not call
it at all; an ID that matches no file answers 404.
The call is read-only, works without a filter - leaving `filterValue` empty returns every matching account
rather than nothing - and is paged by `count` and `startIndex`, with the number of matches in the total count
of the response.
Pass `excludeShared` to keep only the accounts that have no access yet, `includeShared` to keep only those
that already have it, and neither to get both kinds with the `shared` field telling them apart.
A DocSpace administrator additionally sees the guests that are not related to the caller.
To search users and groups together, or to build an access dialog that needs the right to manage sharing, use
`GET api/2.0/accounts/file/{id}/search` instead.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the room, folder or file the search is run against, taken from the route. It is an integer for an  entry stored in DocSpace and a provider-specific string for an entry in a connected third-party storage. | 
 **employee_status** | [**EmployeeStatus**](.md)| Keeps only the accounts in the given state: `Active` for working accounts, `Terminated` for disabled ones  and `Pending` for open invitations. Omit it to search every state. | [optional] 
 **activation_status** | [**EmployeeActivationStatus**](.md)| Keeps only the accounts whose activation is in the given state: `NotActivated`, `Activated`, `Pending` or  `AutoGenerated`. Omit it to search every state. | [optional] 
 **exclude_shared** | **bool**| Keeps only the accounts that do not have access to the entry yet, which is the set to offer when granting  access. It takes precedence over `includeShared`, and every returned entry has `shared` set to false. | [optional] 
 **include_shared** | **bool**| Keeps only the accounts that already have access to the entry, which is the set to offer when changing or  revoking access. Every returned entry has `shared` set to true, and the flag is ignored when `excludeShared`  is also set. | [optional] 
 **invited_by_me** | **bool**| Keeps only the accounts invited by the caller when true, and only those invited by somebody else when  false. Omit it to search regardless of who sent the invitation. | [optional] 
 **inviter_id** | **UUID**| Keeps only the accounts invited by the account with this ID. Omit it to search regardless of who sent the  invitation. | [optional] 
 **area** | [**Area**](.md)| The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only - and for a caller who is not a DocSpace  administrator, only the guests that caller is related to. | [optional] 
 **employee_types** | [**List[EmployeeType]**](EmployeeType.md)| Keeps only the accounts of the listed types, combined as alternatives. An empty list, which is the default,  searches every type. | [optional] 
 **count** | **int**| The size of the page. It defaults to 100, which is also the largest value the operation accepts. | [optional] 
 **start_index** | **int**| The number of matches to skip before the page starts. It defaults to 0, and the total number of matches is  reported in the total count of the response. | [optional] 
 **filter_separator** | **str**| The character that splits `filterValue` into several terms, of which any one may match. Omit it to split the  value on spaces instead, in which case every term has to match. | [optional] 
 **filter_value** | **str**| The text to match against the first name, the last name and the email, case-insensitively. Omit it to get  every account the caller may offer access to. | [optional] 

### Return type

[**EmployeeFullArrayWrapper**](EmployeeFullArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.area import Area
from docspace_api_sdk.models.employee_activation_status import EmployeeActivationStatus
from docspace_api_sdk.models.employee_full_array_wrapper import EmployeeFullArrayWrapper
from docspace_api_sdk.models.employee_status import EmployeeStatus
from docspace_api_sdk.models.employee_type import EmployeeType
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
    api_instance = docspace_api_sdk.SearchApi(api_client)
    id = 1234 # int | The ID of the room, folder or file the search is run against, taken from the route. It is an integer for an  entry stored in DocSpace and a provider-specific string for an entry in a connected third-party storage.
    employee_status = docspace_api_sdk.EmployeeStatus() # EmployeeStatus | Keeps only the accounts in the given state: `Active` for working accounts, `Terminated` for disabled ones  and `Pending` for open invitations. Omit it to search every state. (optional)
    activation_status = docspace_api_sdk.EmployeeActivationStatus() # EmployeeActivationStatus | Keeps only the accounts whose activation is in the given state: `NotActivated`, `Activated`, `Pending` or  `AutoGenerated`. Omit it to search every state. (optional)
    exclude_shared = false # bool | Keeps only the accounts that do not have access to the entry yet, which is the set to offer when granting  access. It takes precedence over `includeShared`, and every returned entry has `shared` set to false. (optional)
    include_shared = false # bool | Keeps only the accounts that already have access to the entry, which is the set to offer when changing or  revoking access. Every returned entry has `shared` set to true, and the flag is ignored when `excludeShared`  is also set. (optional)
    invited_by_me = false # bool | Keeps only the accounts invited by the caller when true, and only those invited by somebody else when  false. Omit it to search regardless of who sent the invitation. (optional)
    inviter_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Keeps only the accounts invited by the account with this ID. Omit it to search regardless of who sent the  invitation. (optional)
    area = docspace_api_sdk.Area() # Area | The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only - and for a caller who is not a DocSpace  administrator, only the guests that caller is related to. (optional)
    employee_types = [docspace_api_sdk.EmployeeType()] # List[EmployeeType] | Keeps only the accounts of the listed types, combined as alternatives. An empty list, which is the default,  searches every type. (optional)
    count = 25 # int | The size of the page. It defaults to 100, which is also the largest value the operation accepts. (optional)
    start_index = 0 # int | The number of matches to skip before the page starts. It defaults to 0, and the total number of matches is  reported in the total count of the response. (optional)
    filter_separator = ',' # str | The character that splits `filterValue` into several terms, of which any one may match. Omit it to split the  value on spaces instead, in which case every term has to match. (optional)
    filter_value = 'John' # str | The text to match against the first name, the last name and the email, case-insensitively. Omit it to get  every account the caller may offer access to. (optional)

    try:
        # Search users for a file
        api_response = api_instance.get_users_with_files_shared(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)
        print("The response of SearchApi->get_users_with_files_shared:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_users_with_files_shared: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matching accounts, each with its access state for the file |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is a guest or cannot read the file |  -  |
**404** | No file has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_with_files_shared_third_party**
> EmployeeFullArrayWrapper get_users_with_files_shared_third_party(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)

Returns the accounts that are relevant to the file with the ID given in the route, and reports for each of
them whether it already has access to that file.
The caller only needs read access to the file, not the right to manage its access, but a guest may not call
it at all; an ID that matches no file answers 404.
The call is read-only, works without a filter - leaving `filterValue` empty returns every matching account
rather than nothing - and is paged by `count` and `startIndex`, with the number of matches in the total count
of the response.
Pass `excludeShared` to keep only the accounts that have no access yet, `includeShared` to keep only those
that already have it, and neither to get both kinds with the `shared` field telling them apart.
A DocSpace administrator additionally sees the guests that are not related to the caller.
To search users and groups together, or to build an access dialog that needs the right to manage sharing, use
`GET api/2.0/accounts/file/{id}/search` instead.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the room, folder or file the search is run against, taken from the route. It is an integer for an  entry stored in DocSpace and a provider-specific string for an entry in a connected third-party storage. | 
 **employee_status** | [**EmployeeStatus**](.md)| Keeps only the accounts in the given state: `Active` for working accounts, `Terminated` for disabled ones  and `Pending` for open invitations. Omit it to search every state. | [optional] 
 **activation_status** | [**EmployeeActivationStatus**](.md)| Keeps only the accounts whose activation is in the given state: `NotActivated`, `Activated`, `Pending` or  `AutoGenerated`. Omit it to search every state. | [optional] 
 **exclude_shared** | **bool**| Keeps only the accounts that do not have access to the entry yet, which is the set to offer when granting  access. It takes precedence over `includeShared`, and every returned entry has `shared` set to false. | [optional] 
 **include_shared** | **bool**| Keeps only the accounts that already have access to the entry, which is the set to offer when changing or  revoking access. Every returned entry has `shared` set to true, and the flag is ignored when `excludeShared`  is also set. | [optional] 
 **invited_by_me** | **bool**| Keeps only the accounts invited by the caller when true, and only those invited by somebody else when  false. Omit it to search regardless of who sent the invitation. | [optional] 
 **inviter_id** | **UUID**| Keeps only the accounts invited by the account with this ID. Omit it to search regardless of who sent the  invitation. | [optional] 
 **area** | [**Area**](.md)| The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only - and for a caller who is not a DocSpace  administrator, only the guests that caller is related to. | [optional] 
 **employee_types** | [**List[EmployeeType]**](EmployeeType.md)| Keeps only the accounts of the listed types, combined as alternatives. An empty list, which is the default,  searches every type. | [optional] 
 **count** | **int**| The size of the page. It defaults to 100, which is also the largest value the operation accepts. | [optional] 
 **start_index** | **int**| The number of matches to skip before the page starts. It defaults to 0, and the total number of matches is  reported in the total count of the response. | [optional] 
 **filter_separator** | **str**| The character that splits `filterValue` into several terms, of which any one may match. Omit it to split the  value on spaces instead, in which case every term has to match. | [optional] 
 **filter_value** | **str**| The text to match against the first name, the last name and the email, case-insensitively. Omit it to get  every account the caller may offer access to. | [optional] 

### Return type

[**EmployeeFullArrayWrapper**](EmployeeFullArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.area import Area
from docspace_api_sdk.models.employee_activation_status import EmployeeActivationStatus
from docspace_api_sdk.models.employee_full_array_wrapper import EmployeeFullArrayWrapper
from docspace_api_sdk.models.employee_status import EmployeeStatus
from docspace_api_sdk.models.employee_type import EmployeeType
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
    api_instance = docspace_api_sdk.SearchApi(api_client)
    id = '1234' # str | The ID of the room, folder or file the search is run against, taken from the route. It is an integer for an  entry stored in DocSpace and a provider-specific string for an entry in a connected third-party storage.
    employee_status = docspace_api_sdk.EmployeeStatus() # EmployeeStatus | Keeps only the accounts in the given state: `Active` for working accounts, `Terminated` for disabled ones  and `Pending` for open invitations. Omit it to search every state. (optional)
    activation_status = docspace_api_sdk.EmployeeActivationStatus() # EmployeeActivationStatus | Keeps only the accounts whose activation is in the given state: `NotActivated`, `Activated`, `Pending` or  `AutoGenerated`. Omit it to search every state. (optional)
    exclude_shared = false # bool | Keeps only the accounts that do not have access to the entry yet, which is the set to offer when granting  access. It takes precedence over `includeShared`, and every returned entry has `shared` set to false. (optional)
    include_shared = false # bool | Keeps only the accounts that already have access to the entry, which is the set to offer when changing or  revoking access. Every returned entry has `shared` set to true, and the flag is ignored when `excludeShared`  is also set. (optional)
    invited_by_me = false # bool | Keeps only the accounts invited by the caller when true, and only those invited by somebody else when  false. Omit it to search regardless of who sent the invitation. (optional)
    inviter_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Keeps only the accounts invited by the account with this ID. Omit it to search regardless of who sent the  invitation. (optional)
    area = docspace_api_sdk.Area() # Area | The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only - and for a caller who is not a DocSpace  administrator, only the guests that caller is related to. (optional)
    employee_types = [docspace_api_sdk.EmployeeType()] # List[EmployeeType] | Keeps only the accounts of the listed types, combined as alternatives. An empty list, which is the default,  searches every type. (optional)
    count = 25 # int | The size of the page. It defaults to 100, which is also the largest value the operation accepts. (optional)
    start_index = 0 # int | The number of matches to skip before the page starts. It defaults to 0, and the total number of matches is  reported in the total count of the response. (optional)
    filter_separator = ',' # str | The character that splits `filterValue` into several terms, of which any one may match. Omit it to split the  value on spaces instead, in which case every term has to match. (optional)
    filter_value = 'John' # str | The text to match against the first name, the last name and the email, case-insensitively. Omit it to get  every account the caller may offer access to. (optional)

    try:
        # Search users for a file (third-party storage)
        api_response = api_instance.get_users_with_files_shared_third_party(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)
        print("The response of SearchApi->get_users_with_files_shared_third_party:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_users_with_files_shared_third_party: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matching accounts, each with its access state for the file |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is a guest or cannot read the file |  -  |
**404** | No file has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_with_folders_shared**
> EmployeeFullArrayWrapper get_users_with_folders_shared(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)

Returns the accounts that are relevant to the folder with the ID given in the route, and reports for each of
them whether it already has access to that folder.
The caller only needs read access to the folder, not the right to manage its access, but a guest may not call
it at all; an ID that matches no folder answers 404.
The call is read-only, works without a filter - leaving `filterValue` empty returns every matching account
rather than nothing - and is paged by `count` and `startIndex`, with the number of matches in the total count
of the response.
Pass `excludeShared` to keep only the accounts that have no access yet, `includeShared` to keep only those
that already have it, and neither to get both kinds with the `shared` field telling them apart.
A DocSpace administrator additionally sees the guests that are not related to the caller.
To search users and groups together, or to build an access dialog that needs the right to manage sharing, use
`GET api/2.0/accounts/folder/{id}/search` instead.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the room, folder or file the search is run against, taken from the route. It is an integer for an  entry stored in DocSpace and a provider-specific string for an entry in a connected third-party storage. | 
 **employee_status** | [**EmployeeStatus**](.md)| Keeps only the accounts in the given state: `Active` for working accounts, `Terminated` for disabled ones  and `Pending` for open invitations. Omit it to search every state. | [optional] 
 **activation_status** | [**EmployeeActivationStatus**](.md)| Keeps only the accounts whose activation is in the given state: `NotActivated`, `Activated`, `Pending` or  `AutoGenerated`. Omit it to search every state. | [optional] 
 **exclude_shared** | **bool**| Keeps only the accounts that do not have access to the entry yet, which is the set to offer when granting  access. It takes precedence over `includeShared`, and every returned entry has `shared` set to false. | [optional] 
 **include_shared** | **bool**| Keeps only the accounts that already have access to the entry, which is the set to offer when changing or  revoking access. Every returned entry has `shared` set to true, and the flag is ignored when `excludeShared`  is also set. | [optional] 
 **invited_by_me** | **bool**| Keeps only the accounts invited by the caller when true, and only those invited by somebody else when  false. Omit it to search regardless of who sent the invitation. | [optional] 
 **inviter_id** | **UUID**| Keeps only the accounts invited by the account with this ID. Omit it to search regardless of who sent the  invitation. | [optional] 
 **area** | [**Area**](.md)| The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only - and for a caller who is not a DocSpace  administrator, only the guests that caller is related to. | [optional] 
 **employee_types** | [**List[EmployeeType]**](EmployeeType.md)| Keeps only the accounts of the listed types, combined as alternatives. An empty list, which is the default,  searches every type. | [optional] 
 **count** | **int**| The size of the page. It defaults to 100, which is also the largest value the operation accepts. | [optional] 
 **start_index** | **int**| The number of matches to skip before the page starts. It defaults to 0, and the total number of matches is  reported in the total count of the response. | [optional] 
 **filter_separator** | **str**| The character that splits `filterValue` into several terms, of which any one may match. Omit it to split the  value on spaces instead, in which case every term has to match. | [optional] 
 **filter_value** | **str**| The text to match against the first name, the last name and the email, case-insensitively. Omit it to get  every account the caller may offer access to. | [optional] 

### Return type

[**EmployeeFullArrayWrapper**](EmployeeFullArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.area import Area
from docspace_api_sdk.models.employee_activation_status import EmployeeActivationStatus
from docspace_api_sdk.models.employee_full_array_wrapper import EmployeeFullArrayWrapper
from docspace_api_sdk.models.employee_status import EmployeeStatus
from docspace_api_sdk.models.employee_type import EmployeeType
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
    api_instance = docspace_api_sdk.SearchApi(api_client)
    id = 1234 # int | The ID of the room, folder or file the search is run against, taken from the route. It is an integer for an  entry stored in DocSpace and a provider-specific string for an entry in a connected third-party storage.
    employee_status = docspace_api_sdk.EmployeeStatus() # EmployeeStatus | Keeps only the accounts in the given state: `Active` for working accounts, `Terminated` for disabled ones  and `Pending` for open invitations. Omit it to search every state. (optional)
    activation_status = docspace_api_sdk.EmployeeActivationStatus() # EmployeeActivationStatus | Keeps only the accounts whose activation is in the given state: `NotActivated`, `Activated`, `Pending` or  `AutoGenerated`. Omit it to search every state. (optional)
    exclude_shared = false # bool | Keeps only the accounts that do not have access to the entry yet, which is the set to offer when granting  access. It takes precedence over `includeShared`, and every returned entry has `shared` set to false. (optional)
    include_shared = false # bool | Keeps only the accounts that already have access to the entry, which is the set to offer when changing or  revoking access. Every returned entry has `shared` set to true, and the flag is ignored when `excludeShared`  is also set. (optional)
    invited_by_me = false # bool | Keeps only the accounts invited by the caller when true, and only those invited by somebody else when  false. Omit it to search regardless of who sent the invitation. (optional)
    inviter_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Keeps only the accounts invited by the account with this ID. Omit it to search regardless of who sent the  invitation. (optional)
    area = docspace_api_sdk.Area() # Area | The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only - and for a caller who is not a DocSpace  administrator, only the guests that caller is related to. (optional)
    employee_types = [docspace_api_sdk.EmployeeType()] # List[EmployeeType] | Keeps only the accounts of the listed types, combined as alternatives. An empty list, which is the default,  searches every type. (optional)
    count = 25 # int | The size of the page. It defaults to 100, which is also the largest value the operation accepts. (optional)
    start_index = 0 # int | The number of matches to skip before the page starts. It defaults to 0, and the total number of matches is  reported in the total count of the response. (optional)
    filter_separator = ',' # str | The character that splits `filterValue` into several terms, of which any one may match. Omit it to split the  value on spaces instead, in which case every term has to match. (optional)
    filter_value = 'John' # str | The text to match against the first name, the last name and the email, case-insensitively. Omit it to get  every account the caller may offer access to. (optional)

    try:
        # Search users for a folder
        api_response = api_instance.get_users_with_folders_shared(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)
        print("The response of SearchApi->get_users_with_folders_shared:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_users_with_folders_shared: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matching accounts, each with its access state for the folder |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is a guest or cannot read the folder |  -  |
**404** | No folder has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_with_folders_shared_third_party**
> EmployeeFullArrayWrapper get_users_with_folders_shared_third_party(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)

Returns the accounts that are relevant to the folder with the ID given in the route, and reports for each of
them whether it already has access to that folder.
The caller only needs read access to the folder, not the right to manage its access, but a guest may not call
it at all; an ID that matches no folder answers 404.
The call is read-only, works without a filter - leaving `filterValue` empty returns every matching account
rather than nothing - and is paged by `count` and `startIndex`, with the number of matches in the total count
of the response.
Pass `excludeShared` to keep only the accounts that have no access yet, `includeShared` to keep only those
that already have it, and neither to get both kinds with the `shared` field telling them apart.
A DocSpace administrator additionally sees the guests that are not related to the caller.
To search users and groups together, or to build an access dialog that needs the right to manage sharing, use
`GET api/2.0/accounts/folder/{id}/search` instead.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the room, folder or file the search is run against, taken from the route. It is an integer for an  entry stored in DocSpace and a provider-specific string for an entry in a connected third-party storage. | 
 **employee_status** | [**EmployeeStatus**](.md)| Keeps only the accounts in the given state: `Active` for working accounts, `Terminated` for disabled ones  and `Pending` for open invitations. Omit it to search every state. | [optional] 
 **activation_status** | [**EmployeeActivationStatus**](.md)| Keeps only the accounts whose activation is in the given state: `NotActivated`, `Activated`, `Pending` or  `AutoGenerated`. Omit it to search every state. | [optional] 
 **exclude_shared** | **bool**| Keeps only the accounts that do not have access to the entry yet, which is the set to offer when granting  access. It takes precedence over `includeShared`, and every returned entry has `shared` set to false. | [optional] 
 **include_shared** | **bool**| Keeps only the accounts that already have access to the entry, which is the set to offer when changing or  revoking access. Every returned entry has `shared` set to true, and the flag is ignored when `excludeShared`  is also set. | [optional] 
 **invited_by_me** | **bool**| Keeps only the accounts invited by the caller when true, and only those invited by somebody else when  false. Omit it to search regardless of who sent the invitation. | [optional] 
 **inviter_id** | **UUID**| Keeps only the accounts invited by the account with this ID. Omit it to search regardless of who sent the  invitation. | [optional] 
 **area** | [**Area**](.md)| The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only - and for a caller who is not a DocSpace  administrator, only the guests that caller is related to. | [optional] 
 **employee_types** | [**List[EmployeeType]**](EmployeeType.md)| Keeps only the accounts of the listed types, combined as alternatives. An empty list, which is the default,  searches every type. | [optional] 
 **count** | **int**| The size of the page. It defaults to 100, which is also the largest value the operation accepts. | [optional] 
 **start_index** | **int**| The number of matches to skip before the page starts. It defaults to 0, and the total number of matches is  reported in the total count of the response. | [optional] 
 **filter_separator** | **str**| The character that splits `filterValue` into several terms, of which any one may match. Omit it to split the  value on spaces instead, in which case every term has to match. | [optional] 
 **filter_value** | **str**| The text to match against the first name, the last name and the email, case-insensitively. Omit it to get  every account the caller may offer access to. | [optional] 

### Return type

[**EmployeeFullArrayWrapper**](EmployeeFullArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.area import Area
from docspace_api_sdk.models.employee_activation_status import EmployeeActivationStatus
from docspace_api_sdk.models.employee_full_array_wrapper import EmployeeFullArrayWrapper
from docspace_api_sdk.models.employee_status import EmployeeStatus
from docspace_api_sdk.models.employee_type import EmployeeType
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
    api_instance = docspace_api_sdk.SearchApi(api_client)
    id = '1234' # str | The ID of the room, folder or file the search is run against, taken from the route. It is an integer for an  entry stored in DocSpace and a provider-specific string for an entry in a connected third-party storage.
    employee_status = docspace_api_sdk.EmployeeStatus() # EmployeeStatus | Keeps only the accounts in the given state: `Active` for working accounts, `Terminated` for disabled ones  and `Pending` for open invitations. Omit it to search every state. (optional)
    activation_status = docspace_api_sdk.EmployeeActivationStatus() # EmployeeActivationStatus | Keeps only the accounts whose activation is in the given state: `NotActivated`, `Activated`, `Pending` or  `AutoGenerated`. Omit it to search every state. (optional)
    exclude_shared = false # bool | Keeps only the accounts that do not have access to the entry yet, which is the set to offer when granting  access. It takes precedence over `includeShared`, and every returned entry has `shared` set to false. (optional)
    include_shared = false # bool | Keeps only the accounts that already have access to the entry, which is the set to offer when changing or  revoking access. Every returned entry has `shared` set to true, and the flag is ignored when `excludeShared`  is also set. (optional)
    invited_by_me = false # bool | Keeps only the accounts invited by the caller when true, and only those invited by somebody else when  false. Omit it to search regardless of who sent the invitation. (optional)
    inviter_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Keeps only the accounts invited by the account with this ID. Omit it to search regardless of who sent the  invitation. (optional)
    area = docspace_api_sdk.Area() # Area | The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only - and for a caller who is not a DocSpace  administrator, only the guests that caller is related to. (optional)
    employee_types = [docspace_api_sdk.EmployeeType()] # List[EmployeeType] | Keeps only the accounts of the listed types, combined as alternatives. An empty list, which is the default,  searches every type. (optional)
    count = 25 # int | The size of the page. It defaults to 100, which is also the largest value the operation accepts. (optional)
    start_index = 0 # int | The number of matches to skip before the page starts. It defaults to 0, and the total number of matches is  reported in the total count of the response. (optional)
    filter_separator = ',' # str | The character that splits `filterValue` into several terms, of which any one may match. Omit it to split the  value on spaces instead, in which case every term has to match. (optional)
    filter_value = 'John' # str | The text to match against the first name, the last name and the email, case-insensitively. Omit it to get  every account the caller may offer access to. (optional)

    try:
        # Search users for a folder (third-party storage)
        api_response = api_instance.get_users_with_folders_shared_third_party(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)
        print("The response of SearchApi->get_users_with_folders_shared_third_party:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_users_with_folders_shared_third_party: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matching accounts, each with its access state for the folder |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is a guest or cannot read the folder |  -  |
**404** | No folder has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_with_room_shared**
> EmployeeFullArrayWrapper get_users_with_room_shared(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)

Returns the accounts that are relevant to the room with the ID given in the route, and reports for each of
them whether it already has access to that room.
The caller only needs read access to the room, not the right to manage its access, but a guest may not call
it at all; an ID that matches no room answers 404.
The call is read-only, works without a filter - leaving `filterValue` empty returns every matching account
rather than nothing - and is paged by `count` and `startIndex`, with the number of matches in the total count
of the response.
Pass `excludeShared` to keep only the accounts that have no access yet, `includeShared` to keep only those
that already have it, and neither to get both kinds with the `shared` field telling them apart.
A DocSpace administrator additionally sees the guests that are not related to the caller.
To search users and groups together, or to build an access dialog that needs the right to manage sharing, use
`GET api/2.0/accounts/room/{id}/search` instead.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the room, folder or file the search is run against, taken from the route. It is an integer for an  entry stored in DocSpace and a provider-specific string for an entry in a connected third-party storage. | 
 **employee_status** | [**EmployeeStatus**](.md)| Keeps only the accounts in the given state: `Active` for working accounts, `Terminated` for disabled ones  and `Pending` for open invitations. Omit it to search every state. | [optional] 
 **activation_status** | [**EmployeeActivationStatus**](.md)| Keeps only the accounts whose activation is in the given state: `NotActivated`, `Activated`, `Pending` or  `AutoGenerated`. Omit it to search every state. | [optional] 
 **exclude_shared** | **bool**| Keeps only the accounts that do not have access to the entry yet, which is the set to offer when granting  access. It takes precedence over `includeShared`, and every returned entry has `shared` set to false. | [optional] 
 **include_shared** | **bool**| Keeps only the accounts that already have access to the entry, which is the set to offer when changing or  revoking access. Every returned entry has `shared` set to true, and the flag is ignored when `excludeShared`  is also set. | [optional] 
 **invited_by_me** | **bool**| Keeps only the accounts invited by the caller when true, and only those invited by somebody else when  false. Omit it to search regardless of who sent the invitation. | [optional] 
 **inviter_id** | **UUID**| Keeps only the accounts invited by the account with this ID. Omit it to search regardless of who sent the  invitation. | [optional] 
 **area** | [**Area**](.md)| The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only - and for a caller who is not a DocSpace  administrator, only the guests that caller is related to. | [optional] 
 **employee_types** | [**List[EmployeeType]**](EmployeeType.md)| Keeps only the accounts of the listed types, combined as alternatives. An empty list, which is the default,  searches every type. | [optional] 
 **count** | **int**| The size of the page. It defaults to 100, which is also the largest value the operation accepts. | [optional] 
 **start_index** | **int**| The number of matches to skip before the page starts. It defaults to 0, and the total number of matches is  reported in the total count of the response. | [optional] 
 **filter_separator** | **str**| The character that splits `filterValue` into several terms, of which any one may match. Omit it to split the  value on spaces instead, in which case every term has to match. | [optional] 
 **filter_value** | **str**| The text to match against the first name, the last name and the email, case-insensitively. Omit it to get  every account the caller may offer access to. | [optional] 

### Return type

[**EmployeeFullArrayWrapper**](EmployeeFullArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.area import Area
from docspace_api_sdk.models.employee_activation_status import EmployeeActivationStatus
from docspace_api_sdk.models.employee_full_array_wrapper import EmployeeFullArrayWrapper
from docspace_api_sdk.models.employee_status import EmployeeStatus
from docspace_api_sdk.models.employee_type import EmployeeType
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
    api_instance = docspace_api_sdk.SearchApi(api_client)
    id = 1234 # int | The ID of the room, folder or file the search is run against, taken from the route. It is an integer for an  entry stored in DocSpace and a provider-specific string for an entry in a connected third-party storage.
    employee_status = docspace_api_sdk.EmployeeStatus() # EmployeeStatus | Keeps only the accounts in the given state: `Active` for working accounts, `Terminated` for disabled ones  and `Pending` for open invitations. Omit it to search every state. (optional)
    activation_status = docspace_api_sdk.EmployeeActivationStatus() # EmployeeActivationStatus | Keeps only the accounts whose activation is in the given state: `NotActivated`, `Activated`, `Pending` or  `AutoGenerated`. Omit it to search every state. (optional)
    exclude_shared = false # bool | Keeps only the accounts that do not have access to the entry yet, which is the set to offer when granting  access. It takes precedence over `includeShared`, and every returned entry has `shared` set to false. (optional)
    include_shared = false # bool | Keeps only the accounts that already have access to the entry, which is the set to offer when changing or  revoking access. Every returned entry has `shared` set to true, and the flag is ignored when `excludeShared`  is also set. (optional)
    invited_by_me = false # bool | Keeps only the accounts invited by the caller when true, and only those invited by somebody else when  false. Omit it to search regardless of who sent the invitation. (optional)
    inviter_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Keeps only the accounts invited by the account with this ID. Omit it to search regardless of who sent the  invitation. (optional)
    area = docspace_api_sdk.Area() # Area | The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only - and for a caller who is not a DocSpace  administrator, only the guests that caller is related to. (optional)
    employee_types = [docspace_api_sdk.EmployeeType()] # List[EmployeeType] | Keeps only the accounts of the listed types, combined as alternatives. An empty list, which is the default,  searches every type. (optional)
    count = 25 # int | The size of the page. It defaults to 100, which is also the largest value the operation accepts. (optional)
    start_index = 0 # int | The number of matches to skip before the page starts. It defaults to 0, and the total number of matches is  reported in the total count of the response. (optional)
    filter_separator = ',' # str | The character that splits `filterValue` into several terms, of which any one may match. Omit it to split the  value on spaces instead, in which case every term has to match. (optional)
    filter_value = 'John' # str | The text to match against the first name, the last name and the email, case-insensitively. Omit it to get  every account the caller may offer access to. (optional)

    try:
        # Search users for a room
        api_response = api_instance.get_users_with_room_shared(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)
        print("The response of SearchApi->get_users_with_room_shared:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_users_with_room_shared: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matching accounts, each with its access state for the room |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is a guest or cannot read the room |  -  |
**404** | No room has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_with_room_shared_third_party**
> EmployeeFullArrayWrapper get_users_with_room_shared_third_party(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)

Returns the accounts that are relevant to the room with the ID given in the route, and reports for each of
them whether it already has access to that room.
The caller only needs read access to the room, not the right to manage its access, but a guest may not call
it at all; an ID that matches no room answers 404.
The call is read-only, works without a filter - leaving `filterValue` empty returns every matching account
rather than nothing - and is paged by `count` and `startIndex`, with the number of matches in the total count
of the response.
Pass `excludeShared` to keep only the accounts that have no access yet, `includeShared` to keep only those
that already have it, and neither to get both kinds with the `shared` field telling them apart.
A DocSpace administrator additionally sees the guests that are not related to the caller.
To search users and groups together, or to build an access dialog that needs the right to manage sharing, use
`GET api/2.0/accounts/room/{id}/search` instead.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the room, folder or file the search is run against, taken from the route. It is an integer for an  entry stored in DocSpace and a provider-specific string for an entry in a connected third-party storage. | 
 **employee_status** | [**EmployeeStatus**](.md)| Keeps only the accounts in the given state: `Active` for working accounts, `Terminated` for disabled ones  and `Pending` for open invitations. Omit it to search every state. | [optional] 
 **activation_status** | [**EmployeeActivationStatus**](.md)| Keeps only the accounts whose activation is in the given state: `NotActivated`, `Activated`, `Pending` or  `AutoGenerated`. Omit it to search every state. | [optional] 
 **exclude_shared** | **bool**| Keeps only the accounts that do not have access to the entry yet, which is the set to offer when granting  access. It takes precedence over `includeShared`, and every returned entry has `shared` set to false. | [optional] 
 **include_shared** | **bool**| Keeps only the accounts that already have access to the entry, which is the set to offer when changing or  revoking access. Every returned entry has `shared` set to true, and the flag is ignored when `excludeShared`  is also set. | [optional] 
 **invited_by_me** | **bool**| Keeps only the accounts invited by the caller when true, and only those invited by somebody else when  false. Omit it to search regardless of who sent the invitation. | [optional] 
 **inviter_id** | **UUID**| Keeps only the accounts invited by the account with this ID. Omit it to search regardless of who sent the  invitation. | [optional] 
 **area** | [**Area**](.md)| The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only - and for a caller who is not a DocSpace  administrator, only the guests that caller is related to. | [optional] 
 **employee_types** | [**List[EmployeeType]**](EmployeeType.md)| Keeps only the accounts of the listed types, combined as alternatives. An empty list, which is the default,  searches every type. | [optional] 
 **count** | **int**| The size of the page. It defaults to 100, which is also the largest value the operation accepts. | [optional] 
 **start_index** | **int**| The number of matches to skip before the page starts. It defaults to 0, and the total number of matches is  reported in the total count of the response. | [optional] 
 **filter_separator** | **str**| The character that splits `filterValue` into several terms, of which any one may match. Omit it to split the  value on spaces instead, in which case every term has to match. | [optional] 
 **filter_value** | **str**| The text to match against the first name, the last name and the email, case-insensitively. Omit it to get  every account the caller may offer access to. | [optional] 

### Return type

[**EmployeeFullArrayWrapper**](EmployeeFullArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.area import Area
from docspace_api_sdk.models.employee_activation_status import EmployeeActivationStatus
from docspace_api_sdk.models.employee_full_array_wrapper import EmployeeFullArrayWrapper
from docspace_api_sdk.models.employee_status import EmployeeStatus
from docspace_api_sdk.models.employee_type import EmployeeType
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
    api_instance = docspace_api_sdk.SearchApi(api_client)
    id = '1234' # str | The ID of the room, folder or file the search is run against, taken from the route. It is an integer for an  entry stored in DocSpace and a provider-specific string for an entry in a connected third-party storage.
    employee_status = docspace_api_sdk.EmployeeStatus() # EmployeeStatus | Keeps only the accounts in the given state: `Active` for working accounts, `Terminated` for disabled ones  and `Pending` for open invitations. Omit it to search every state. (optional)
    activation_status = docspace_api_sdk.EmployeeActivationStatus() # EmployeeActivationStatus | Keeps only the accounts whose activation is in the given state: `NotActivated`, `Activated`, `Pending` or  `AutoGenerated`. Omit it to search every state. (optional)
    exclude_shared = false # bool | Keeps only the accounts that do not have access to the entry yet, which is the set to offer when granting  access. It takes precedence over `includeShared`, and every returned entry has `shared` set to false. (optional)
    include_shared = false # bool | Keeps only the accounts that already have access to the entry, which is the set to offer when changing or  revoking access. Every returned entry has `shared` set to true, and the flag is ignored when `excludeShared`  is also set. (optional)
    invited_by_me = false # bool | Keeps only the accounts invited by the caller when true, and only those invited by somebody else when  false. Omit it to search regardless of who sent the invitation. (optional)
    inviter_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Keeps only the accounts invited by the account with this ID. Omit it to search regardless of who sent the  invitation. (optional)
    area = docspace_api_sdk.Area() # Area | The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only - and for a caller who is not a DocSpace  administrator, only the guests that caller is related to. (optional)
    employee_types = [docspace_api_sdk.EmployeeType()] # List[EmployeeType] | Keeps only the accounts of the listed types, combined as alternatives. An empty list, which is the default,  searches every type. (optional)
    count = 25 # int | The size of the page. It defaults to 100, which is also the largest value the operation accepts. (optional)
    start_index = 0 # int | The number of matches to skip before the page starts. It defaults to 0, and the total number of matches is  reported in the total count of the response. (optional)
    filter_separator = ',' # str | The character that splits `filterValue` into several terms, of which any one may match. Omit it to split the  value on spaces instead, in which case every term has to match. (optional)
    filter_value = 'John' # str | The text to match against the first name, the last name and the email, case-insensitively. Omit it to get  every account the caller may offer access to. (optional)

    try:
        # Search users for a room (third-party storage)
        api_response = api_instance.get_users_with_room_shared_third_party(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)
        print("The response of SearchApi->get_users_with_room_shared_third_party:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_users_with_room_shared_third_party: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matching accounts, each with its access state for the room |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is a guest or cannot read the room |  -  |
**404** | No room has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users_by_extended_filter**
> EmployeeFullArrayWrapper search_users_by_extended_filter(employee_status=employee_status, group_id=group_id, activation_status=activation_status, employee_type=employee_type, employee_types=employee_types, is_administrator=is_administrator, payments=payments, account_login_type=account_login_type, quota_filter=quota_filter, without_group=without_group, exclude_group=exclude_group, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_separator=filter_separator, filter_value=filter_value)

Returns a page of portal accounts selected by the full set of account filters, with the complete profile of
each of them.
The caller has to be a room admin, a DocSpace admin or a People module admin; a member or a guest gets 403,
and a DocSpace admin additionally sees the accounts an ordinary admin does not.
The call is read-only, paged by `count` and `startIndex`, ordered by `sortBy` and `sortOrder`, and reports
the number of matches in the total count of the response.
Filters combine as conditions that all have to hold, with three interactions worth knowing: `withoutGroup`
makes `groupId` irrelevant, `employeeType` wins over `employeeTypes` when both are sent, and `area` set to
`Guests` or `People` cancels the type filters that contradict it.
`GET api/2.0/people/simple/filter` accepts exactly the same filters and returns the short profile instead, so
use that one for pickers and lists and this one when the full profile is really needed.
It is available on an unpaid portal.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_status** | [**EmployeeStatus**](.md)| Keeps only the accounts in the given state: `Active` for working accounts, `Terminated` for disabled ones  and `Pending` for open invitations. Omit it to search every state. | [optional] 
 **group_id** | **UUID**| Keeps only the members of this group, or excludes them when `excludeGroup` is true. It is ignored when  `withoutGroup` is set. | [optional] 
 **activation_status** | [**EmployeeActivationStatus**](.md)| Keeps only the accounts whose activation is in the given state: `NotActivated`, `Activated`, `Pending` or  `AutoGenerated`. Omit it to search every state. | [optional] 
 **employee_type** | [**EmployeeType**](.md)| Keeps only the accounts of this single type: `DocSpaceAdmin`, `RoomAdmin`, `User` or `Guest`. When it is  sent it wins over `employeeTypes`, and a type that contradicts `area` is dropped. | [optional] 
 **employee_types** | [**List[int]**](int.md)| Keeps the accounts of any of the listed types, combined as alternatives. It is ignored when `employeeType`  is also sent. | [optional] 
 **is_administrator** | **bool**| Set it to true to keep only the DocSpace administrators and the module administrators. Setting it to false  is the same as omitting it and does not exclude administrators. | [optional] 
 **payments** | [**Payments**](.md)| Keeps only the accounts that take a paid seat when `Paid`, or only the guests and members that do not when  `Free`. Omit it to search both. | [optional] 
 **account_login_type** | [**AccountLoginType**](.md)| Keeps only the accounts that sign in this way: `SSO`, `LDAP`, or `Standart` for an ordinary portal  password. Omit it to search all of them. | [optional] 
 **quota_filter** | [**QuotaFilter**](.md)| Keeps only the accounts whose storage quota is the portal default when `Default`, or set individually when  `Custom`. `All`, which is the same as omitting the field, searches both. | [optional] 
 **without_group** | **bool**| Set it to true to keep only the accounts that belong to no group at all, which makes `groupId` and  `excludeGroup` irrelevant. | [optional] 
 **exclude_group** | **bool**| Inverts `groupId`: with true the members of that group are left out instead of being the only ones kept. It  has no effect without `groupId`. | [optional] 
 **invited_by_me** | **bool**| Keeps only the accounts invited by the caller when true, and only those invited by somebody else when  false. Omit it to search regardless of who sent the invitation. | [optional] 
 **inviter_id** | **UUID**| Keeps only the accounts invited by the account with this ID. Omit it to search regardless of who sent the  invitation. | [optional] 
 **area** | [**Area**](.md)| The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only. It also cancels the type filters that contradict  it. | [optional] 
 **count** | **int**| The size of the page. It defaults to 100, which is also the largest value the operation accepts. | [optional] 
 **start_index** | **int**| The number of matches to skip before the page starts. It defaults to 0, and the total number of matches is  reported in the total count of the response. | [optional] 
 **sort_by** | **str**| What to order the accounts by, compared without regard to case: `FirstName`, `LastName`, `DisplayName`,  `Type`, `Email`, `Department`, `UsedSpace`, `CreatedBy` or `RegistrationDate`. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The direction of the ordering: `Ascending`, which is the default, or `Descending`. | [optional] 
 **filter_separator** | **str**| The character that splits `filterValue` into several terms, of which any one may match. Omit it to split  the value on spaces instead, in which case every term has to match. | [optional] 
 **filter_value** | **str**| The text to match against the first name, the last name and the email, case-insensitively. Omit it to apply  no text filter at all. | [optional] 

### Return type

[**EmployeeFullArrayWrapper**](EmployeeFullArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.account_login_type import AccountLoginType
from docspace_api_sdk.models.area import Area
from docspace_api_sdk.models.employee_activation_status import EmployeeActivationStatus
from docspace_api_sdk.models.employee_full_array_wrapper import EmployeeFullArrayWrapper
from docspace_api_sdk.models.employee_status import EmployeeStatus
from docspace_api_sdk.models.employee_type import EmployeeType
from docspace_api_sdk.models.payments import Payments
from docspace_api_sdk.models.quota_filter import QuotaFilter
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
    api_instance = docspace_api_sdk.SearchApi(api_client)
    employee_status = docspace_api_sdk.EmployeeStatus() # EmployeeStatus | Keeps only the accounts in the given state: `Active` for working accounts, `Terminated` for disabled ones  and `Pending` for open invitations. Omit it to search every state. (optional)
    group_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Keeps only the members of this group, or excludes them when `excludeGroup` is true. It is ignored when  `withoutGroup` is set. (optional)
    activation_status = docspace_api_sdk.EmployeeActivationStatus() # EmployeeActivationStatus | Keeps only the accounts whose activation is in the given state: `NotActivated`, `Activated`, `Pending` or  `AutoGenerated`. Omit it to search every state. (optional)
    employee_type = docspace_api_sdk.EmployeeType() # EmployeeType | Keeps only the accounts of this single type: `DocSpaceAdmin`, `RoomAdmin`, `User` or `Guest`. When it is  sent it wins over `employeeTypes`, and a type that contradicts `area` is dropped. (optional)
    employee_types = [["RoomAdmin","Guest"]] # List[int] | Keeps the accounts of any of the listed types, combined as alternatives. It is ignored when `employeeType`  is also sent. (optional)
    is_administrator = false # bool | Set it to true to keep only the DocSpace administrators and the module administrators. Setting it to false  is the same as omitting it and does not exclude administrators. (optional)
    payments = docspace_api_sdk.Payments() # Payments | Keeps only the accounts that take a paid seat when `Paid`, or only the guests and members that do not when  `Free`. Omit it to search both. (optional)
    account_login_type = docspace_api_sdk.AccountLoginType() # AccountLoginType | Keeps only the accounts that sign in this way: `SSO`, `LDAP`, or `Standart` for an ordinary portal  password. Omit it to search all of them. (optional)
    quota_filter = docspace_api_sdk.QuotaFilter() # QuotaFilter | Keeps only the accounts whose storage quota is the portal default when `Default`, or set individually when  `Custom`. `All`, which is the same as omitting the field, searches both. (optional)
    without_group = false # bool | Set it to true to keep only the accounts that belong to no group at all, which makes `groupId` and  `excludeGroup` irrelevant. (optional)
    exclude_group = false # bool | Inverts `groupId`: with true the members of that group are left out instead of being the only ones kept. It  has no effect without `groupId`. (optional)
    invited_by_me = false # bool | Keeps only the accounts invited by the caller when true, and only those invited by somebody else when  false. Omit it to search regardless of who sent the invitation. (optional)
    inviter_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | Keeps only the accounts invited by the account with this ID. Omit it to search regardless of who sent the  invitation. (optional)
    area = docspace_api_sdk.Area() # Area | The part of the portal to search in: `All`, the default, searches members and guests together, `People`  leaves the guests out, and `Guests` returns guests only. It also cancels the type filters that contradict  it. (optional)
    count = 25 # int | The size of the page. It defaults to 100, which is also the largest value the operation accepts. (optional)
    start_index = 0 # int | The number of matches to skip before the page starts. It defaults to 0, and the total number of matches is  reported in the total count of the response. (optional)
    sort_by = 'DisplayName' # str | What to order the accounts by, compared without regard to case: `FirstName`, `LastName`, `DisplayName`,  `Type`, `Email`, `Department`, `UsedSpace`, `CreatedBy` or `RegistrationDate`. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The direction of the ordering: `Ascending`, which is the default, or `Descending`. (optional)
    filter_separator = ',' # str | The character that splits `filterValue` into several terms, of which any one may match. Omit it to split  the value on spaces instead, in which case every term has to match. (optional)
    filter_value = 'John' # str | The text to match against the first name, the last name and the email, case-insensitively. Omit it to apply  no text filter at all. (optional)

    try:
        # Filter users in detail
        api_response = api_instance.search_users_by_extended_filter(employee_status=employee_status, group_id=group_id, activation_status=activation_status, employee_type=employee_type, employee_types=employee_types, is_administrator=is_administrator, payments=payments, account_login_type=account_login_type, quota_filter=quota_filter, without_group=without_group, exclude_group=exclude_group, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_separator=filter_separator, filter_value=filter_value)
        print("The response of SearchApi->search_users_by_extended_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_users_by_extended_filter: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of matching accounts, with their full profiles |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is a member or a guest |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users_by_query**
> EmployeeFullArrayWrapper search_users_by_query(query=query)

Searches the active accounts of the portal by a term passed in the query string, and is the same search as
`GET api/2.0/people/@search/{query}`, which takes the term in the path instead.
Only a DocSpace administrator may call it; every other account, including a room admin, gets 403.
Only accounts with the `Active` status are searched, so a pending invitation and a disabled account are never
found - use `GET api/2.0/people/filter` to search across states.
The call is read-only and is not paged: every match is streamed, without a total.
It takes the search term and nothing else - the group filter of
`GET api/2.0/people/@search/{query}` is not reachable here, because the handler forwards only `query` - so
use that operation when the result has to be narrowed to one group.
The answer holds full profiles, because the handler passes the request on to the operation that builds the
complete profile.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The term to look for. Only accounts with the `Active` status are searched, and this is the only parameter the  operation reads. | [optional] 

### Return type

[**EmployeeFullArrayWrapper**](EmployeeFullArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.employee_full_array_wrapper import EmployeeFullArrayWrapper
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
    api_instance = docspace_api_sdk.SearchApi(api_client)
    query = 'John' # str | The term to look for. Only accounts with the `Active` status are searched, and this is the only parameter the  operation reads. (optional)

    try:
        # Search users by query
        api_response = api_instance.search_users_by_query(query=query)
        print("The response of SearchApi->search_users_by_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_users_by_query: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The full profiles of the matching active accounts |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users_by_status**
> EmployeeFullArrayWrapper search_users_by_status(status, query=query, filter_by=filter_by, filter_value=filter_value)

Searches the accounts that are in one particular state - the status is taken from the route - and whose name,
user name, email or contacts contain the search term.
Only a DocSpace administrator may call it; every other account, including a room admin, gets 403.
The call is read-only and is not paged: it matches in memory over every account of that status and streams
all of them, so it is meant for administrative lookups rather than for a user-facing list - use
`GET api/2.0/people/filter` when a page and a total are needed.
The term is matched as a case-insensitive substring and is required; `filterBy` set to `group` turns `text`
into a group ID and keeps only the members of that group, so `text` then has to be a valid identifier.
The answer holds full profiles, in no particular order.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**EmployeeStatus**](.md)| The account state to search in, taken from the route: `Active` for working accounts, `Terminated` for  disabled ones, `Pending` for open invitations, or `All` for every state. | 
 **query** | **str**| The term to look for, matched as a case-insensitive substring of the first name, the last name, the user  name, the email and the contacts. It is required in practice, because the search cannot run without it. | [optional] 
 **filter_by** | **str**| The only recognised value is `group`, which turns `filterValue` into a group ID and keeps only the members of  that group. Any other value, and omitting the field, applies no group filter. | [optional] 
 **filter_value** | **str**| The group ID to keep the members of, used only when `filterBy` is `group`. It has to be a valid identifier -  a group name is not accepted. | [optional] 

### Return type

[**EmployeeFullArrayWrapper**](EmployeeFullArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.employee_full_array_wrapper import EmployeeFullArrayWrapper
from docspace_api_sdk.models.employee_status import EmployeeStatus
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
    api_instance = docspace_api_sdk.SearchApi(api_client)
    status = docspace_api_sdk.EmployeeStatus() # EmployeeStatus | The account state to search in, taken from the route: `Active` for working accounts, `Terminated` for  disabled ones, `Pending` for open invitations, or `All` for every state.
    query = 'John' # str | The term to look for, matched as a case-insensitive substring of the first name, the last name, the user  name, the email and the contacts. It is required in practice, because the search cannot run without it. (optional)
    filter_by = 'group' # str | The only recognised value is `group`, which turns `filterValue` into a group ID and keeps only the members of  that group. Any other value, and omitting the field, applies no group filter. (optional)
    filter_value = '00000000-0000-0000-0000-000000000000' # str | The group ID to keep the members of, used only when `filterBy` is `group`. It has to be a valid identifier -  a group name is not accepted. (optional)

    try:
        # Search users by status filter
        api_response = api_instance.search_users_by_status(status, query=query, filter_by=filter_by, filter_value=filter_value)
        print("The response of SearchApi->search_users_by_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_users_by_status: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The full profiles of the matching accounts |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

