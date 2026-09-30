# docspace_api_sdk.SearchApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_groups_with_files_shared**](#get_groups_with_files_shared) | **GET** /api/2.0/group/file/{id} | Search groups for a file
[**get_groups_with_folders_shared**](#get_groups_with_folders_shared) | **GET** /api/2.0/group/folder/{id} | Search groups for a folder
[**get_groups_with_rooms_shared**](#get_groups_with_rooms_shared) | **GET** /api/2.0/group/room/{id} | Search groups for a room


# **get_groups_with_files_shared**
> GroupArrayWrapper get_groups_with_files_shared(id, exclude_shared=exclude_shared, count=count, start_index=start_index, filter_value=filter_value)

Returns the groups that can be given access to the file with the ID given in the route, and reports for each
of them whether it already has access to that file.
The caller has to be allowed to manage the access of that file, and the ID has to belong to an existing file,
so the operation answers 403 for a file the caller cannot share and 404 for an ID that matches nothing.
The call is read-only and, unlike the account search, works without a filter: leaving `filterValue` empty
returns every group instead of nothing, and a value narrows the result by group name.
The result is paged by `count` and `startIndex`, with the number of matching groups in the total count of the
response.
Pass `excludeShared` to keep only the groups that have no access to the file yet, which is the set to offer
when adding new ones; without it every matching group comes back and `shared` tells them apart.
To search users and groups together, use `GET api/2.0/accounts/file/{id}/search`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Union[int, str]**| The ID of the room, folder or file whose access the search is run against, taken from the route. It is an  integer for an entry stored in DocSpace and a provider-specific string for an entry in a connected  third-party storage. | 
 **exclude_shared** | **bool**| Keeps only the groups that do not have access to the entry yet, which is the set to offer when granting  access. Every returned entry then has `shared` set to false; without the flag every matching group comes back  and `shared` tells them apart. | [optional] 
 **count** | **int**| The size of the page. It defaults to 100, which is also the largest value the operation accepts. | [optional] 
 **start_index** | **int**| The number of matching groups to skip before the page starts. It defaults to 0, and the total number of  matches is reported in the total count of the response. | [optional] 
 **filter_value** | **str**| The text to match against the group name. Omit it to get every group the caller may grant access to. | [optional] 

### Return type

[**GroupArrayWrapper**](GroupArrayWrapper.md)

### Third-party storage

The same method serves an entry in a connected third-party storage, whose identifier is a string such as `sbox-42`: pass `id: str`.

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.group_array_wrapper import GroupArrayWrapper
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
    exclude_shared = false # bool | Keeps only the groups that do not have access to the entry yet, which is the set to offer when granting  access. Every returned entry then has `shared` set to false; without the flag every matching group comes back  and `shared` tells them apart. (optional)
    count = 25 # int | The size of the page. It defaults to 100, which is also the largest value the operation accepts. (optional)
    start_index = 0 # int | The number of matching groups to skip before the page starts. It defaults to 0, and the total number of  matches is reported in the total count of the response. (optional)
    filter_value = 'Marketing' # str | The text to match against the group name. Omit it to get every group the caller may grant access to. (optional)

    try:
        # Search groups for a file
        api_response = api_instance.get_groups_with_files_shared(id, exclude_shared=exclude_shared, count=count, start_index=start_index, filter_value=filter_value)
        print("The response of SearchApi->get_groups_with_files_shared:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_groups_with_files_shared: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matching groups, each with its access state for the file |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**404** | No file has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups_with_folders_shared**
> GroupArrayWrapper get_groups_with_folders_shared(id, exclude_shared=exclude_shared, count=count, start_index=start_index, filter_value=filter_value)

Returns the groups that can be given access to the folder with the ID given in the route, and reports for
each of them whether it already has access to that folder.
The caller has to be allowed to manage the access of that folder, and the ID has to belong to an existing
folder, so the operation answers 403 for a folder the caller cannot share and 404 for an ID that matches
nothing.
The call is read-only and, unlike the account search, works without a filter: leaving `filterValue` empty
returns every group instead of nothing, and a value narrows the result by group name.
The result is paged by `count` and `startIndex`, with the number of matching groups in the total count of the
response.
Pass `excludeShared` to keep only the groups that have no access to the folder yet, which is the set to offer
when adding new ones; without it every matching group comes back and `shared` tells them apart.
To search users and groups together, use `GET api/2.0/accounts/folder/{id}/search`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Union[int, str]**| The ID of the room, folder or file whose access the search is run against, taken from the route. It is an  integer for an entry stored in DocSpace and a provider-specific string for an entry in a connected  third-party storage. | 
 **exclude_shared** | **bool**| Keeps only the groups that do not have access to the entry yet, which is the set to offer when granting  access. Every returned entry then has `shared` set to false; without the flag every matching group comes back  and `shared` tells them apart. | [optional] 
 **count** | **int**| The size of the page. It defaults to 100, which is also the largest value the operation accepts. | [optional] 
 **start_index** | **int**| The number of matching groups to skip before the page starts. It defaults to 0, and the total number of  matches is reported in the total count of the response. | [optional] 
 **filter_value** | **str**| The text to match against the group name. Omit it to get every group the caller may grant access to. | [optional] 

### Return type

[**GroupArrayWrapper**](GroupArrayWrapper.md)

### Third-party storage

The same method serves an entry in a connected third-party storage, whose identifier is a string such as `sbox-42`: pass `id: str`.

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.group_array_wrapper import GroupArrayWrapper
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
    exclude_shared = false # bool | Keeps only the groups that do not have access to the entry yet, which is the set to offer when granting  access. Every returned entry then has `shared` set to false; without the flag every matching group comes back  and `shared` tells them apart. (optional)
    count = 25 # int | The size of the page. It defaults to 100, which is also the largest value the operation accepts. (optional)
    start_index = 0 # int | The number of matching groups to skip before the page starts. It defaults to 0, and the total number of  matches is reported in the total count of the response. (optional)
    filter_value = 'Marketing' # str | The text to match against the group name. Omit it to get every group the caller may grant access to. (optional)

    try:
        # Search groups for a folder
        api_response = api_instance.get_groups_with_folders_shared(id, exclude_shared=exclude_shared, count=count, start_index=start_index, filter_value=filter_value)
        print("The response of SearchApi->get_groups_with_folders_shared:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_groups_with_folders_shared: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matching groups, each with its access state for the folder |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**404** | No folder has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups_with_rooms_shared**
> GroupArrayWrapper get_groups_with_rooms_shared(id, exclude_shared=exclude_shared, count=count, start_index=start_index, filter_value=filter_value)

Returns the groups that can be given access to the room with the ID given in the route, and reports for each
of them whether it already has access to that room.
The caller has to be allowed to manage the access of that room, and the ID has to belong to an existing room,
so the operation answers 403 for a room the caller cannot share and 404 for an ID that matches nothing.
The call is read-only and, unlike the account search, works without a filter: leaving `filterValue` empty
returns every group instead of nothing, and a value narrows the result by group name.
The result is paged by `count` and `startIndex`, with the number of matching groups in the total count of the
response.
Pass `excludeShared` to keep only the groups that have no access to the room yet, which is the set to offer
when adding new ones; without it every matching group comes back and `shared` tells them apart.
To search users and groups together, use `GET api/2.0/accounts/room/{id}/search`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Union[int, str]**| The ID of the room, folder or file whose access the search is run against, taken from the route. It is an  integer for an entry stored in DocSpace and a provider-specific string for an entry in a connected  third-party storage. | 
 **exclude_shared** | **bool**| Keeps only the groups that do not have access to the entry yet, which is the set to offer when granting  access. Every returned entry then has `shared` set to false; without the flag every matching group comes back  and `shared` tells them apart. | [optional] 
 **count** | **int**| The size of the page. It defaults to 100, which is also the largest value the operation accepts. | [optional] 
 **start_index** | **int**| The number of matching groups to skip before the page starts. It defaults to 0, and the total number of  matches is reported in the total count of the response. | [optional] 
 **filter_value** | **str**| The text to match against the group name. Omit it to get every group the caller may grant access to. | [optional] 

### Return type

[**GroupArrayWrapper**](GroupArrayWrapper.md)

### Third-party storage

The same method serves an entry in a connected third-party storage, whose identifier is a string such as `sbox-42`: pass `id: str`.

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.group_array_wrapper import GroupArrayWrapper
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
    exclude_shared = false # bool | Keeps only the groups that do not have access to the entry yet, which is the set to offer when granting  access. Every returned entry then has `shared` set to false; without the flag every matching group comes back  and `shared` tells them apart. (optional)
    count = 25 # int | The size of the page. It defaults to 100, which is also the largest value the operation accepts. (optional)
    start_index = 0 # int | The number of matching groups to skip before the page starts. It defaults to 0, and the total number of  matches is reported in the total count of the response. (optional)
    filter_value = 'Marketing' # str | The text to match against the group name. Omit it to get every group the caller may grant access to. (optional)

    try:
        # Search groups for a room
        api_response = api_instance.get_groups_with_rooms_shared(id, exclude_shared=exclude_shared, count=count, start_index=start_index, filter_value=filter_value)
        print("The response of SearchApi->get_groups_with_rooms_shared:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_groups_with_rooms_shared: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matching groups, each with its access state for the room |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**404** | No room has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

