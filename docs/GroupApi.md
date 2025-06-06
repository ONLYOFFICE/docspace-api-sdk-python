# docspace.GroupApi

All URIs are relative to *http://http:*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group**](GroupApi.md#add_group) | **POST** /api/2.0/group | Add a new group
[**add_members_to**](GroupApi.md#add_members_to) | **PUT** /api/2.0/group/{id}/members | Add group members
[**delete_group**](GroupApi.md#delete_group) | **DELETE** /api/2.0/group/{id} | Delete a group
[**get_group**](GroupApi.md#get_group) | **GET** /api/2.0/group/{id} | Get a group
[**get_group_by_user_id**](GroupApi.md#get_group_by_user_id) | **GET** /api/2.0/group/user/{userid} | Get user groups
[**get_groups**](GroupApi.md#get_groups) | **GET** /api/2.0/group | Get groups
[**move_members_to**](GroupApi.md#move_members_to) | **PUT** /api/2.0/group/{fromId}/members/{toId} | Move group members
[**remove_members_from**](GroupApi.md#remove_members_from) | **DELETE** /api/2.0/group/{id}/members | Remove group members
[**set_group_manager**](GroupApi.md#set_group_manager) | **PUT** /api/2.0/group/{id}/manager | Set a group manager
[**set_members_to**](GroupApi.md#set_members_to) | **POST** /api/2.0/group/{id}/members | Replace group members
[**update_group**](GroupApi.md#update_group) | **PUT** /api/2.0/group/{id} | Update a group


# **add_group**
> GroupWrapper add_group(group_request_dto=group_request_dto)

Add a new group

Adds a new group with the group manager, name, and members specified in the request.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.group_request_dto import GroupRequestDto
from docspace.models.group_wrapper import GroupWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://http:
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://http:"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace.Configuration(
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
configuration = docspace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.GroupApi(api_client)
    group_request_dto = docspace.GroupRequestDto() # GroupRequestDto |  (optional)

    try:
        # Add a new group
        api_response = api_instance.add_group(group_request_dto=group_request_dto)
        print("The response of GroupApi->add_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->add_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_request_dto** | [**GroupRequestDto**](GroupRequestDto.md)|  | [optional] 

### Return type

[**GroupWrapper**](GroupWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newly created group with the detailed information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_members_to**
> GroupWrapper add_members_to(id, members_request=members_request)

Add group members

Adds new group members to the group with the ID specified in the request.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.group_wrapper import GroupWrapper
from docspace.models.members_request import MembersRequest
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://http:
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://http:"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace.Configuration(
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
configuration = docspace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.GroupApi(api_client)
    id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28' # str | The group ID.
    members_request = docspace.MembersRequest() # MembersRequest | The member request. (optional)

    try:
        # Add group members
        api_response = api_instance.add_members_to(id, members_request=members_request)
        print("The response of GroupApi->add_members_to:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->add_members_to: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group ID. | 
 **members_request** | [**MembersRequest**](MembersRequest.md)| The member request. | [optional] 

### Return type

[**GroupWrapper**](GroupWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group with the detailed information |  -  |
**401** | Unauthorized |  -  |
**404** | Group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> NoContentResultWrapper delete_group(id)

Delete a group

Deletes a group with the ID specified in the request from the list of groups on the portal.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.no_content_result_wrapper import NoContentResultWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://http:
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://http:"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace.Configuration(
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
configuration = docspace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.GroupApi(api_client)
    id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28' # str | The group ID.

    try:
        # Delete a group
        api_response = api_instance.delete_group(id)
        print("The response of GroupApi->delete_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->delete_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group ID. | 

### Return type

[**NoContentResultWrapper**](NoContentResultWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No content |  -  |
**401** | Unauthorized |  -  |
**404** | Group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> GroupWrapper get_group(id, include_members=include_members)

Get a group

Returns the detailed information about the selected group.   **Note**: This method returns full group information.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.group_wrapper import GroupWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://http:
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://http:"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace.Configuration(
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
configuration = docspace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.GroupApi(api_client)
    id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28' # str | The group ID.
    include_members = true # bool | Specifies whether to include the group members or not. (optional)

    try:
        # Get a group
        api_response = api_instance.get_group(id, include_members=include_members)
        print("The response of GroupApi->get_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->get_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group ID. | 
 **include_members** | **bool**| Specifies whether to include the group members or not. | [optional] 

### Return type

[**GroupWrapper**](GroupWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group with the detailed information |  -  |
**401** | Unauthorized |  -  |
**404** | Group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_by_user_id**
> GroupSummaryArrayWrapper get_group_by_user_id(userid)

Get user groups

Returns a list of groups for the user with the ID specified in the request.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.group_summary_array_wrapper import GroupSummaryArrayWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://http:
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://http:"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace.Configuration(
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
configuration = docspace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.GroupApi(api_client)
    userid = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28' # str | The user ID.

    try:
        # Get user groups
        api_response = api_instance.get_group_by_user_id(userid)
        print("The response of GroupApi->get_group_by_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->get_group_by_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| The user ID. | 

### Return type

[**GroupSummaryArrayWrapper**](GroupSummaryArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of groups |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups**
> GroupArrayWrapper get_groups(user_id=user_id, manager=manager, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)

Get groups

Returns the general information about all the groups, such as group ID and group manager.   **Note**: This method returns partial group information.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.group_array_wrapper import GroupArrayWrapper
from docspace.models.sort_order import SortOrder
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://http:
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://http:"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace.Configuration(
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
configuration = docspace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.GroupApi(api_client)
    user_id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28' # str | The user ID. (optional)
    manager = true # bool | Specifies if the user is a manager or not. (optional)
    count = 1234 # int | The number of records to retrieve. (optional)
    start_index = 1234 # int | The starting index for paginated results. (optional)
    sort_by = 'some text' # str | Specifies the property used to sort the query results. (optional)
    sort_order = docspace.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_value = 'some text' # str | The text used for filtering or searching group data. (optional)

    try:
        # Get groups
        api_response = api_instance.get_groups(user_id=user_id, manager=manager, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)
        print("The response of GroupApi->get_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->get_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID. | [optional] 
 **manager** | **bool**| Specifies if the user is a manager or not. | [optional] 
 **count** | **int**| The number of records to retrieve. | [optional] 
 **start_index** | **int**| The starting index for paginated results. | [optional] 
 **sort_by** | **str**| Specifies the property used to sort the query results. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The order in which the results are sorted. | [optional] 
 **filter_value** | **str**| The text used for filtering or searching group data. | [optional] 

### Return type

[**GroupArrayWrapper**](GroupArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of groups |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_members_to**
> GroupWrapper move_members_to(from_id, to_id)

Move group members

Moves all the members from the selected group to another one specified in the request.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.group_wrapper import GroupWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://http:
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://http:"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace.Configuration(
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
configuration = docspace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.GroupApi(api_client)
    from_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | The group ID to move from.
    to_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | The group ID to move to.

    try:
        # Move group members
        api_response = api_instance.move_members_to(from_id, to_id)
        print("The response of GroupApi->move_members_to:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->move_members_to: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_id** | **str**| The group ID to move from. | 
 **to_id** | **str**| The group ID to move to. | 

### Return type

[**GroupWrapper**](GroupWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group with the detailed information |  -  |
**401** | Unauthorized |  -  |
**404** | Group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_members_from**
> GroupWrapper remove_members_from(id, members_request=members_request)

Remove group members

Removes the group members specified in the request from the selected group.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.group_wrapper import GroupWrapper
from docspace.models.members_request import MembersRequest
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://http:
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://http:"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace.Configuration(
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
configuration = docspace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.GroupApi(api_client)
    id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28' # str | The group ID.
    members_request = docspace.MembersRequest() # MembersRequest | The member request. (optional)

    try:
        # Remove group members
        api_response = api_instance.remove_members_from(id, members_request=members_request)
        print("The response of GroupApi->remove_members_from:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->remove_members_from: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group ID. | 
 **members_request** | [**MembersRequest**](MembersRequest.md)| The member request. | [optional] 

### Return type

[**GroupWrapper**](GroupWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group with the detailed information |  -  |
**401** | Unauthorized |  -  |
**404** | Group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_group_manager**
> GroupWrapper set_group_manager(id, set_manager_request=set_manager_request)

Set a group manager

Sets a user with the ID specified in the request as a group manager.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.group_wrapper import GroupWrapper
from docspace.models.set_manager_request import SetManagerRequest
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://http:
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://http:"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace.Configuration(
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
configuration = docspace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.GroupApi(api_client)
    id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28' # str | The group ID.
    set_manager_request = docspace.SetManagerRequest() # SetManagerRequest | The request for setting a group manager. (optional)

    try:
        # Set a group manager
        api_response = api_instance.set_group_manager(id, set_manager_request=set_manager_request)
        print("The response of GroupApi->set_group_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->set_group_manager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group ID. | 
 **set_manager_request** | [**SetManagerRequest**](SetManagerRequest.md)| The request for setting a group manager. | [optional] 

### Return type

[**GroupWrapper**](GroupWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group with the detailed information |  -  |
**401** | Unauthorized |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_members_to**
> GroupWrapper set_members_to(id, members_request=members_request)

Replace group members

Replaces the group members with those specified in the request.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.group_wrapper import GroupWrapper
from docspace.models.members_request import MembersRequest
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://http:
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://http:"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace.Configuration(
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
configuration = docspace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.GroupApi(api_client)
    id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28' # str | The group ID.
    members_request = docspace.MembersRequest() # MembersRequest | The member request. (optional)

    try:
        # Replace group members
        api_response = api_instance.set_members_to(id, members_request=members_request)
        print("The response of GroupApi->set_members_to:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->set_members_to: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group ID. | 
 **members_request** | [**MembersRequest**](MembersRequest.md)| The member request. | [optional] 

### Return type

[**GroupWrapper**](GroupWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group with the detailed information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> GroupWrapper update_group(id, update_group_request=update_group_request)

Update a group

Updates the existing group changing the group manager, name, and/or members.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.group_wrapper import GroupWrapper
from docspace.models.update_group_request import UpdateGroupRequest
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://http:
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://http:"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace.Configuration(
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
configuration = docspace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.GroupApi(api_client)
    id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28' # str | The group ID.
    update_group_request = docspace.UpdateGroupRequest() # UpdateGroupRequest | The request for updating a group. (optional)

    try:
        # Update a group
        api_response = api_instance.update_group(id, update_group_request=update_group_request)
        print("The response of GroupApi->update_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->update_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group ID. | 
 **update_group_request** | [**UpdateGroupRequest**](UpdateGroupRequest.md)| The request for updating a group. | [optional] 

### Return type

[**GroupWrapper**](GroupWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated group with the detailed information |  -  |
**401** | Unauthorized |  -  |
**404** | Group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

