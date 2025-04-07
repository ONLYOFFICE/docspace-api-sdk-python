# docspace.PortalUsersApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ge_invite_link**](PortalUsersApi.md#ge_invite_link) | **GET** /api/2.0/portal/users/invite/{employeeType} | Get an invitation link
[**get_user**](PortalUsersApi.md#get_user) | **GET** /api/2.0/portal/users/{userID} | Get a user by ID
[**get_users_count**](PortalUsersApi.md#get_users_count) | **GET** /api/2.0/portal/userscount | Get a number of portal users
[**mark_present_as_readed**](PortalUsersApi.md#mark_present_as_readed) | **POST** /api/2.0/portal/present/mark | Mark a gift message as read
[**send_congratulations**](PortalUsersApi.md#send_congratulations) | **POST** /api/2.0/portal/sendcongratulations | Send congratulations


# **ge_invite_link**
> StringWrapper ge_invite_link(employee_type)

Get an invitation link

Returns an invitation link for joining the portal.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.employee_type import EmployeeType
from docspace.models.string_wrapper import StringWrapper
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
    api_instance = docspace.PortalUsersApi(api_client)
    employee_type = docspace.EmployeeType() # EmployeeType | Employee type (All, RoomAdmin, Guest, DocSpaceAdmin, User)

    try:
        # Get an invitation link
        api_response = api_instance.ge_invite_link(employee_type)
        print("The response of PortalUsersApi->ge_invite_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalUsersApi->ge_invite_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_type** | [**EmployeeType**](.md)| Employee type (All, RoomAdmin, Guest, DocSpaceAdmin, User) | 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invitation link |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserInfoWrapper get_user(user_id)

Get a user by ID

Returns a user with the ID specified in the request from the current portal.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.user_info_wrapper import UserInfoWrapper
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
    api_instance = docspace.PortalUsersApi(api_client)
    user_id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28' # str | User ID

    try:
        # Get a user by ID
        api_response = api_instance.get_user(user_id)
        print("The response of PortalUsersApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalUsersApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID | 

### Return type

[**UserInfoWrapper**](UserInfoWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_count**
> Int64Wrapper get_users_count()

Get a number of portal users

Returns a number of portal users.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.int64_wrapper import Int64Wrapper
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
    api_instance = docspace.PortalUsersApi(api_client)

    try:
        # Get a number of portal users
        api_response = api_instance.get_users_count()
        print("The response of PortalUsersApi->get_users_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalUsersApi->get_users_count: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Int64Wrapper**](Int64Wrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Number of portal users |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_present_as_readed**
> mark_present_as_readed()

Mark a gift message as read

Marks a gift message as read.

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
    api_instance = docspace.PortalUsersApi(api_client)

    try:
        # Mark a gift message as read
        api_instance.mark_present_as_readed()
    except Exception as e:
        print("Exception when calling PortalUsersApi->mark_present_as_readed: %s\n" % e)
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
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_congratulations**
> send_congratulations(userid=userid, key=key)

Send congratulations

Sends congratulations to the user after registering the portal.

### Example


```python
import docspace
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
    api_instance = docspace.PortalUsersApi(api_client)
    userid = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | User ID (optional)
    key = 'some text' # str | Email key (optional)

    try:
        # Send congratulations
        api_instance.send_congratulations(userid=userid, key=key)
    except Exception as e:
        print("Exception when calling PortalUsersApi->send_congratulations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| User ID | [optional] 
 **key** | **str**| Email key | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

