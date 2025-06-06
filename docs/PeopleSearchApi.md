# docspace.PeopleSearchApi

All URIs are relative to *http://http:*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accounts_entries_with_shared**](PeopleSearchApi.md#get_accounts_entries_with_shared) | **GET** /api/2.0/accounts/room/{id}/search | Get account entries
[**get_search**](PeopleSearchApi.md#get_search) | **GET** /api/2.0/people/@search/{query} | Search users
[**get_simple_by_filter**](PeopleSearchApi.md#get_simple_by_filter) | **GET** /api/2.0/people/simple/filter | Search users by extended filter
[**get_users_with_room_shared**](PeopleSearchApi.md#get_users_with_room_shared) | **GET** /api/2.0/people/room/{id} | Get users with room sharing settings
[**search_users_by_extended_filter**](PeopleSearchApi.md#search_users_by_extended_filter) | **GET** /api/2.0/people/filter | Search users with detaailed information by extended filter
[**search_users_by_query**](PeopleSearchApi.md#search_users_by_query) | **GET** /api/2.0/people/search | Search users (using query parameters)
[**search_users_by_status**](PeopleSearchApi.md#search_users_by_status) | **GET** /api/2.0/people/status/{status}/search | Search users by status filter


# **get_accounts_entries_with_shared**
> ObjectArrayWrapper get_accounts_entries_with_shared(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)

Get account entries

Returns the account entries with their sharing settings.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.area import Area
from docspace.models.employee_activation_status import EmployeeActivationStatus
from docspace.models.employee_status import EmployeeStatus
from docspace.models.employee_type import EmployeeType
from docspace.models.object_array_wrapper import ObjectArrayWrapper
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
    api_instance = docspace.PeopleSearchApi(api_client)
    id = 9846 # int | The user ID.
    employee_status = docspace.EmployeeStatus() # EmployeeStatus | The user status. (optional)
    activation_status = docspace.EmployeeActivationStatus() # EmployeeActivationStatus | The user activation status. (optional)
    exclude_shared = true # bool | Specifies whether to exclude the account sharing settings from the response. (optional)
    include_shared = true # bool | Specifies whether to include the account sharing settings in the response. (optional)
    invited_by_me = true # bool | Specifies whether the user is invited by the current user or not. (optional)
    inviter_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | The inviter ID. (optional)
    area = docspace.Area() # Area | The area of the account entries. (optional)
    employee_types = [docspace.EmployeeType()] # List[EmployeeType] | The list of the user types. (optional)
    count = 1234 # int | The number of items to retrieve in a request. (optional)
    start_index = 1234 # int | The starting index for the query results. (optional)
    filter_separator = 'some text' # str | Specifies the separator used in filter expressions. (optional)
    filter_value = 'some text' # str | The text filter applied to the accounts search query. (optional)

    try:
        # Get account entries
        api_response = api_instance.get_accounts_entries_with_shared(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)
        print("The response of PeopleSearchApi->get_accounts_entries_with_shared:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleSearchApi->get_accounts_entries_with_shared: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The user ID. | 
 **employee_status** | [**EmployeeStatus**](.md)| The user status. | [optional] 
 **activation_status** | [**EmployeeActivationStatus**](.md)| The user activation status. | [optional] 
 **exclude_shared** | **bool**| Specifies whether to exclude the account sharing settings from the response. | [optional] 
 **include_shared** | **bool**| Specifies whether to include the account sharing settings in the response. | [optional] 
 **invited_by_me** | **bool**| Specifies whether the user is invited by the current user or not. | [optional] 
 **inviter_id** | **str**| The inviter ID. | [optional] 
 **area** | [**Area**](.md)| The area of the account entries. | [optional] 
 **employee_types** | [**List[EmployeeType]**](EmployeeType.md)| The list of the user types. | [optional] 
 **count** | **int**| The number of items to retrieve in a request. | [optional] 
 **start_index** | **int**| The starting index for the query results. | [optional] 
 **filter_separator** | **str**| Specifies the separator used in filter expressions. | [optional] 
 **filter_value** | **str**| The text filter applied to the accounts search query. | [optional] 

### Return type

[**ObjectArrayWrapper**](ObjectArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search**
> EmployeeFullArrayWrapper get_search(query, filter_by=filter_by, filter_value=filter_value)

Search users

Returns a list of users matching the search query.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.employee_full_array_wrapper import EmployeeFullArrayWrapper
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
    api_instance = docspace.PeopleSearchApi(api_client)
    query = 'some text' # str | The search query.
    filter_by = 'some text' # str | Specifies a filter criteria for the user search query. (optional)
    filter_value = 'some text' # str | The value used for filtering users, allowing additional constraints for the query. (optional)

    try:
        # Search users
        api_response = api_instance.get_search(query, filter_by=filter_by, filter_value=filter_value)
        print("The response of PeopleSearchApi->get_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleSearchApi->get_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The search query. | 
 **filter_by** | **str**| Specifies a filter criteria for the user search query. | [optional] 
 **filter_value** | **str**| The value used for filtering users, allowing additional constraints for the query. | [optional] 

### Return type

[**EmployeeFullArrayWrapper**](EmployeeFullArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users with the detailed information |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_simple_by_filter**
> EmployeeArrayWrapper get_simple_by_filter(employee_status=employee_status, group_id=group_id, activation_status=activation_status, employee_type=employee_type, employee_types=employee_types, is_administrator=is_administrator, payments=payments, account_login_type=account_login_type, quota_filter=quota_filter, without_group=without_group, exclude_group=exclude_group, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_separator=filter_separator, filter_value=filter_value)

Search users by extended filter

Returns a list of users matching the parameters specified in the request.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.account_login_type import AccountLoginType
from docspace.models.area import Area
from docspace.models.employee_activation_status import EmployeeActivationStatus
from docspace.models.employee_array_wrapper import EmployeeArrayWrapper
from docspace.models.employee_status import EmployeeStatus
from docspace.models.employee_type import EmployeeType
from docspace.models.payments import Payments
from docspace.models.quota_filter import QuotaFilter
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
    api_instance = docspace.PeopleSearchApi(api_client)
    employee_status = docspace.EmployeeStatus() # EmployeeStatus | The user status. (optional)
    group_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | The group ID. (optional)
    activation_status = docspace.EmployeeActivationStatus() # EmployeeActivationStatus | The user activation status. (optional)
    employee_type = docspace.EmployeeType() # EmployeeType | The user type. (optional)
    employee_types = [56] # List[int] | The list of user types. (optional)
    is_administrator = true # bool | Specifies if the user is an administrator or not. (optional)
    payments = docspace.Payments() # Payments | The user payment status. (optional)
    account_login_type = docspace.AccountLoginType() # AccountLoginType | The account login type. (optional)
    quota_filter = docspace.QuotaFilter() # QuotaFilter | The quota filter (All - 0, Default - 1, Custom - 2). (optional)
    without_group = true # bool | Specifies whether the user should be a member of a group or not. (optional)
    exclude_group = true # bool | Specifies whether the user should be a member of the group with the specified ID. (optional)
    invited_by_me = true # bool | Specifies whether the user is invited by the current user or not. (optional)
    inviter_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | The inviter ID. (optional)
    area = docspace.Area() # Area | The filter area. (optional)
    count = 1234 # int | The maximum number of items to be retrieved in the response. (optional)
    start_index = 1234 # int | The zero-based index of the first item to be retrieved in a filtered result set. (optional)
    sort_by = 'some text' # str | Specifies the property or field name by which the results should be sorted. (optional)
    sort_order = docspace.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_separator = 'some text' # str | Represents the separator used to split filter criteria in query parameters. (optional)
    filter_value = 'some text' # str | The search text used to filter results based on user input. (optional)

    try:
        # Search users by extended filter
        api_response = api_instance.get_simple_by_filter(employee_status=employee_status, group_id=group_id, activation_status=activation_status, employee_type=employee_type, employee_types=employee_types, is_administrator=is_administrator, payments=payments, account_login_type=account_login_type, quota_filter=quota_filter, without_group=without_group, exclude_group=exclude_group, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_separator=filter_separator, filter_value=filter_value)
        print("The response of PeopleSearchApi->get_simple_by_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleSearchApi->get_simple_by_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_status** | [**EmployeeStatus**](.md)| The user status. | [optional] 
 **group_id** | **str**| The group ID. | [optional] 
 **activation_status** | [**EmployeeActivationStatus**](.md)| The user activation status. | [optional] 
 **employee_type** | [**EmployeeType**](.md)| The user type. | [optional] 
 **employee_types** | [**List[int]**](int.md)| The list of user types. | [optional] 
 **is_administrator** | **bool**| Specifies if the user is an administrator or not. | [optional] 
 **payments** | [**Payments**](.md)| The user payment status. | [optional] 
 **account_login_type** | [**AccountLoginType**](.md)| The account login type. | [optional] 
 **quota_filter** | [**QuotaFilter**](.md)| The quota filter (All - 0, Default - 1, Custom - 2). | [optional] 
 **without_group** | **bool**| Specifies whether the user should be a member of a group or not. | [optional] 
 **exclude_group** | **bool**| Specifies whether the user should be a member of the group with the specified ID. | [optional] 
 **invited_by_me** | **bool**| Specifies whether the user is invited by the current user or not. | [optional] 
 **inviter_id** | **str**| The inviter ID. | [optional] 
 **area** | [**Area**](.md)| The filter area. | [optional] 
 **count** | **int**| The maximum number of items to be retrieved in the response. | [optional] 
 **start_index** | **int**| The zero-based index of the first item to be retrieved in a filtered result set. | [optional] 
 **sort_by** | **str**| Specifies the property or field name by which the results should be sorted. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The order in which the results are sorted. | [optional] 
 **filter_separator** | **str**| Represents the separator used to split filter criteria in query parameters. | [optional] 
 **filter_value** | **str**| The search text used to filter results based on user input. | [optional] 

### Return type

[**EmployeeArrayWrapper**](EmployeeArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_with_room_shared**
> EmployeeFullArrayWrapper get_users_with_room_shared(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)

Get users with room sharing settings

Returns the users with the sharing settings in a room with the ID specified in request.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.area import Area
from docspace.models.employee_activation_status import EmployeeActivationStatus
from docspace.models.employee_full_array_wrapper import EmployeeFullArrayWrapper
from docspace.models.employee_status import EmployeeStatus
from docspace.models.employee_type import EmployeeType
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
    api_instance = docspace.PeopleSearchApi(api_client)
    id = 9846 # int | The user ID.
    employee_status = docspace.EmployeeStatus() # EmployeeStatus | The user status. (optional)
    activation_status = docspace.EmployeeActivationStatus() # EmployeeActivationStatus | The user activation status. (optional)
    exclude_shared = true # bool | Specifies whether to exclude the user sharing settings or not. (optional)
    include_shared = true # bool | Specifies whether to include the user sharing settings or not. (optional)
    invited_by_me = true # bool | Specifies whether the user was invited by the current user or not. (optional)
    inviter_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | The inviter ID. (optional)
    area = docspace.Area() # Area | The user area. (optional)
    employee_types = [docspace.EmployeeType()] # List[EmployeeType] | The list of user types. (optional)
    count = 1234 # int | The maximum number of users to be retrieved in the request. (optional)
    start_index = 1234 # int | The zero-based index of the first record to retrieve in a paged query. (optional)
    filter_separator = 'some text' # str | The character or string used to separate multiple filter values in a filtering query. (optional)
    filter_value = 'some text' # str | The filter text value used for searching or filtering user results. (optional)

    try:
        # Get users with room sharing settings
        api_response = api_instance.get_users_with_room_shared(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types, count=count, start_index=start_index, filter_separator=filter_separator, filter_value=filter_value)
        print("The response of PeopleSearchApi->get_users_with_room_shared:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleSearchApi->get_users_with_room_shared: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The user ID. | 
 **employee_status** | [**EmployeeStatus**](.md)| The user status. | [optional] 
 **activation_status** | [**EmployeeActivationStatus**](.md)| The user activation status. | [optional] 
 **exclude_shared** | **bool**| Specifies whether to exclude the user sharing settings or not. | [optional] 
 **include_shared** | **bool**| Specifies whether to include the user sharing settings or not. | [optional] 
 **invited_by_me** | **bool**| Specifies whether the user was invited by the current user or not. | [optional] 
 **inviter_id** | **str**| The inviter ID. | [optional] 
 **area** | [**Area**](.md)| The user area. | [optional] 
 **employee_types** | [**List[EmployeeType]**](EmployeeType.md)| The list of user types. | [optional] 
 **count** | **int**| The maximum number of users to be retrieved in the request. | [optional] 
 **start_index** | **int**| The zero-based index of the first record to retrieve in a paged query. | [optional] 
 **filter_separator** | **str**| The character or string used to separate multiple filter values in a filtering query. | [optional] 
 **filter_value** | **str**| The filter text value used for searching or filtering user results. | [optional] 

### Return type

[**EmployeeFullArrayWrapper**](EmployeeFullArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users_by_extended_filter**
> EmployeeFullArrayWrapper search_users_by_extended_filter(employee_status=employee_status, group_id=group_id, activation_status=activation_status, employee_type=employee_type, employee_types=employee_types, is_administrator=is_administrator, payments=payments, account_login_type=account_login_type, quota_filter=quota_filter, without_group=without_group, exclude_group=exclude_group, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_separator=filter_separator, filter_value=filter_value)

Search users with detaailed information by extended filter

Returns a list of users with full information about them matching the parameters specified in the request.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.account_login_type import AccountLoginType
from docspace.models.area import Area
from docspace.models.employee_activation_status import EmployeeActivationStatus
from docspace.models.employee_full_array_wrapper import EmployeeFullArrayWrapper
from docspace.models.employee_status import EmployeeStatus
from docspace.models.employee_type import EmployeeType
from docspace.models.payments import Payments
from docspace.models.quota_filter import QuotaFilter
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
    api_instance = docspace.PeopleSearchApi(api_client)
    employee_status = docspace.EmployeeStatus() # EmployeeStatus | The user status. (optional)
    group_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | The group ID. (optional)
    activation_status = docspace.EmployeeActivationStatus() # EmployeeActivationStatus | The user activation status. (optional)
    employee_type = docspace.EmployeeType() # EmployeeType | The user type. (optional)
    employee_types = [56] # List[int] | The list of user types. (optional)
    is_administrator = true # bool | Specifies if the user is an administrator or not. (optional)
    payments = docspace.Payments() # Payments | The user payment status. (optional)
    account_login_type = docspace.AccountLoginType() # AccountLoginType | The account login type. (optional)
    quota_filter = docspace.QuotaFilter() # QuotaFilter | The quota filter (All - 0, Default - 1, Custom - 2). (optional)
    without_group = true # bool | Specifies whether the user should be a member of a group or not. (optional)
    exclude_group = true # bool | Specifies whether the user should be a member of the group with the specified ID. (optional)
    invited_by_me = true # bool | Specifies whether the user is invited by the current user or not. (optional)
    inviter_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | The inviter ID. (optional)
    area = docspace.Area() # Area | The filter area. (optional)
    count = 1234 # int | The maximum number of items to be retrieved in the response. (optional)
    start_index = 1234 # int | The zero-based index of the first item to be retrieved in a filtered result set. (optional)
    sort_by = 'some text' # str | Specifies the property or field name by which the results should be sorted. (optional)
    sort_order = docspace.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_separator = 'some text' # str | Represents the separator used to split filter criteria in query parameters. (optional)
    filter_value = 'some text' # str | The search text used to filter results based on user input. (optional)

    try:
        # Search users with detaailed information by extended filter
        api_response = api_instance.search_users_by_extended_filter(employee_status=employee_status, group_id=group_id, activation_status=activation_status, employee_type=employee_type, employee_types=employee_types, is_administrator=is_administrator, payments=payments, account_login_type=account_login_type, quota_filter=quota_filter, without_group=without_group, exclude_group=exclude_group, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_separator=filter_separator, filter_value=filter_value)
        print("The response of PeopleSearchApi->search_users_by_extended_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleSearchApi->search_users_by_extended_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_status** | [**EmployeeStatus**](.md)| The user status. | [optional] 
 **group_id** | **str**| The group ID. | [optional] 
 **activation_status** | [**EmployeeActivationStatus**](.md)| The user activation status. | [optional] 
 **employee_type** | [**EmployeeType**](.md)| The user type. | [optional] 
 **employee_types** | [**List[int]**](int.md)| The list of user types. | [optional] 
 **is_administrator** | **bool**| Specifies if the user is an administrator or not. | [optional] 
 **payments** | [**Payments**](.md)| The user payment status. | [optional] 
 **account_login_type** | [**AccountLoginType**](.md)| The account login type. | [optional] 
 **quota_filter** | [**QuotaFilter**](.md)| The quota filter (All - 0, Default - 1, Custom - 2). | [optional] 
 **without_group** | **bool**| Specifies whether the user should be a member of a group or not. | [optional] 
 **exclude_group** | **bool**| Specifies whether the user should be a member of the group with the specified ID. | [optional] 
 **invited_by_me** | **bool**| Specifies whether the user is invited by the current user or not. | [optional] 
 **inviter_id** | **str**| The inviter ID. | [optional] 
 **area** | [**Area**](.md)| The filter area. | [optional] 
 **count** | **int**| The maximum number of items to be retrieved in the response. | [optional] 
 **start_index** | **int**| The zero-based index of the first item to be retrieved in a filtered result set. | [optional] 
 **sort_by** | **str**| Specifies the property or field name by which the results should be sorted. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The order in which the results are sorted. | [optional] 
 **filter_separator** | **str**| Represents the separator used to split filter criteria in query parameters. | [optional] 
 **filter_value** | **str**| The search text used to filter results based on user input. | [optional] 

### Return type

[**EmployeeFullArrayWrapper**](EmployeeFullArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users with the detailed information |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users_by_query**
> EmployeeArrayWrapper search_users_by_query(query=query)

Search users (using query parameters)

Returns a list of users matching the search query. This method uses the query parameters.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.employee_array_wrapper import EmployeeArrayWrapper
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
    api_instance = docspace.PeopleSearchApi(api_client)
    query = 'some text' # str | The search query. (optional)

    try:
        # Search users (using query parameters)
        api_response = api_instance.search_users_by_query(query=query)
        print("The response of PeopleSearchApi->search_users_by_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleSearchApi->search_users_by_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The search query. | [optional] 

### Return type

[**EmployeeArrayWrapper**](EmployeeArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users_by_status**
> EmployeeFullArrayWrapper search_users_by_status(status, query=query, filter_by=filter_by, filter_value=filter_value)

Search users by status filter

Returns a list of users matching the status filter and search query.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.employee_full_array_wrapper import EmployeeFullArrayWrapper
from docspace.models.employee_status import EmployeeStatus
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
    api_instance = docspace.PeopleSearchApi(api_client)
    status = docspace.EmployeeStatus() # EmployeeStatus | The user status.
    query = 'some text' # str | The advanced search query. (optional)
    filter_by = 'some text' # str | Specifies the criteria used to filter search results in advanced queries. (optional)
    filter_value = 'some text' # str | The value used to filter the search query. (optional)

    try:
        # Search users by status filter
        api_response = api_instance.search_users_by_status(status, query=query, filter_by=filter_by, filter_value=filter_value)
        print("The response of PeopleSearchApi->search_users_by_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleSearchApi->search_users_by_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**EmployeeStatus**](.md)| The user status. | 
 **query** | **str**| The advanced search query. | [optional] 
 **filter_by** | **str**| Specifies the criteria used to filter search results in advanced queries. | [optional] 
 **filter_value** | **str**| The value used to filter the search query. | [optional] 

### Return type

[**EmployeeFullArrayWrapper**](EmployeeFullArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users with the detailed information |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

