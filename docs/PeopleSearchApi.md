# docspace.PeopleSearchApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accounts_entries_with_shared**](PeopleSearchApi.md#get_accounts_entries_with_shared) | **GET** /api/2.0/accounts/room/{id}/search | Get account entries
[**get_advanced**](PeopleSearchApi.md#get_advanced) | **GET** /api/2.0/people/status/{status}/search | Search users by status filter
[**get_full_by_filter**](PeopleSearchApi.md#get_full_by_filter) | **GET** /api/2.0/people/filter | Search users with detaailed information by extended filter
[**get_people_search**](PeopleSearchApi.md#get_people_search) | **GET** /api/2.0/people/search | Search users (using query parameters)
[**get_search**](PeopleSearchApi.md#get_search) | **GET** /api/2.0/people/@search/{query} | Search users
[**get_simple_by_filter**](PeopleSearchApi.md#get_simple_by_filter) | **GET** /api/2.0/people/simple/filter | Search users by extended filter
[**get_users_with_room_shared**](PeopleSearchApi.md#get_users_with_room_shared) | **GET** /api/2.0/people/room/{id} | Get users with room sharing settings


# **get_accounts_entries_with_shared**
> ObjectArrayWrapper get_accounts_entries_with_shared(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types)

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

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
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

    try:
        # Get account entries
        api_response = api_instance.get_accounts_entries_with_shared(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types)
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

# **get_advanced**
> EmployeeFullArrayWrapper get_advanced(status, query=query)

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

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
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

    try:
        # Search users by status filter
        api_response = api_instance.get_advanced(status, query=query)
        print("The response of PeopleSearchApi->get_advanced:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleSearchApi->get_advanced: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**EmployeeStatus**](.md)| The user status. | 
 **query** | **str**| The advanced search query. | [optional] 

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

# **get_full_by_filter**
> EmployeeFullArrayWrapper get_full_by_filter(employee_status=employee_status, group_id=group_id, activation_status=activation_status, employee_type=employee_type, employee_types=employee_types, is_administrator=is_administrator, payments=payments, account_login_type=account_login_type, quota_filter=quota_filter, without_group=without_group, exclude_group=exclude_group, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area)

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

    try:
        # Search users with detaailed information by extended filter
        api_response = api_instance.get_full_by_filter(employee_status=employee_status, group_id=group_id, activation_status=activation_status, employee_type=employee_type, employee_types=employee_types, is_administrator=is_administrator, payments=payments, account_login_type=account_login_type, quota_filter=quota_filter, without_group=without_group, exclude_group=exclude_group, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area)
        print("The response of PeopleSearchApi->get_full_by_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleSearchApi->get_full_by_filter: %s\n" % e)
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

# **get_people_search**
> EmployeeArrayWrapper get_people_search(query=query)

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

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
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
        api_response = api_instance.get_people_search(query=query)
        print("The response of PeopleSearchApi->get_people_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleSearchApi->get_people_search: %s\n" % e)
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

# **get_search**
> EmployeeFullArrayWrapper get_search(query)

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

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
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

    try:
        # Search users
        api_response = api_instance.get_search(query)
        print("The response of PeopleSearchApi->get_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleSearchApi->get_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The search query. | 

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
> EmployeeArrayWrapper get_simple_by_filter(employee_status=employee_status, group_id=group_id, activation_status=activation_status, employee_type=employee_type, employee_types=employee_types, is_administrator=is_administrator, payments=payments, account_login_type=account_login_type, quota_filter=quota_filter, without_group=without_group, exclude_group=exclude_group, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area)

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

    try:
        # Search users by extended filter
        api_response = api_instance.get_simple_by_filter(employee_status=employee_status, group_id=group_id, activation_status=activation_status, employee_type=employee_type, employee_types=employee_types, is_administrator=is_administrator, payments=payments, account_login_type=account_login_type, quota_filter=quota_filter, without_group=without_group, exclude_group=exclude_group, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area)
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
> EmployeeFullArrayWrapper get_users_with_room_shared(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types)

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

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
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

    try:
        # Get users with room sharing settings
        api_response = api_instance.get_users_with_room_shared(id, employee_status=employee_status, activation_status=activation_status, exclude_shared=exclude_shared, include_shared=include_shared, invited_by_me=invited_by_me, inviter_id=inviter_id, area=area, employee_types=employee_types)
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

