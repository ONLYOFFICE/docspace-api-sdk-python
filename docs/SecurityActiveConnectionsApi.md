# docspace.SecurityActiveConnectionsApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_active_connections**](SecurityActiveConnectionsApi.md#get_all_active_connections) | **GET** /api/2.0/security/activeconnections | Get active connections
[**log_out_active_connection**](SecurityActiveConnectionsApi.md#log_out_active_connection) | **PUT** /api/2.0/security/activeconnections/logout/{loginEventId} | Log out from the connection
[**log_out_all_active_connections_change_password**](SecurityActiveConnectionsApi.md#log_out_all_active_connections_change_password) | **PUT** /api/2.0/security/activeconnections/logoutallchangepassword | Log out and change password
[**log_out_all_active_connections_for_user**](SecurityActiveConnectionsApi.md#log_out_all_active_connections_for_user) | **PUT** /api/2.0/security/activeconnections/logoutall/{userId} | Log out for the user by ID
[**log_out_all_except_this_connection**](SecurityActiveConnectionsApi.md#log_out_all_except_this_connection) | **PUT** /api/2.0/security/activeconnections/logoutallexceptthis | Log out from all connections


# **get_all_active_connections**
> ActiveConnectionsWrapper get_all_active_connections()

Get active connections

Returns all the active connections to the portal.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.active_connections_wrapper import ActiveConnectionsWrapper
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
    api_instance = docspace.SecurityActiveConnectionsApi(api_client)

    try:
        # Get active connections
        api_response = api_instance.get_all_active_connections()
        print("The response of SecurityActiveConnectionsApi->get_all_active_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityActiveConnectionsApi->get_all_active_connections: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ActiveConnectionsWrapper**](ActiveConnectionsWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Active portal connections |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_out_active_connection**
> BooleanWrapper log_out_active_connection(login_event_id)

Log out from the connection

Logs out from the connection with the ID specified in the request.

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
    api_instance = docspace.SecurityActiveConnectionsApi(api_client)
    login_event_id = 9846 # int | Login event ID

    try:
        # Log out from the connection
        api_response = api_instance.log_out_active_connection(login_event_id)
        print("The response of SecurityActiveConnectionsApi->log_out_active_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityActiveConnectionsApi->log_out_active_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_event_id** | **int**| Login event ID | 

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
**200** | Boolean value: true if the operation is successful |  -  |
**401** | Unauthorized |  -  |
**403** | Method not available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_out_all_active_connections_change_password**
> StringWrapper log_out_all_active_connections_change_password()

Log out and change password

Logs out from all the active connections of the current user and changes their password.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
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
    api_instance = docspace.SecurityActiveConnectionsApi(api_client)

    try:
        # Log out and change password
        api_response = api_instance.log_out_all_active_connections_change_password()
        print("The response of SecurityActiveConnectionsApi->log_out_all_active_connections_change_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityActiveConnectionsApi->log_out_all_active_connections_change_password: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | URL to the confirmation message for changing a password |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_out_all_active_connections_for_user**
> log_out_all_active_connections_for_user(user_id)

Log out for the user by ID

Logs out from all the active connections of the user with the ID specified in the request.

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
    api_instance = docspace.SecurityActiveConnectionsApi(api_client)
    user_id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28' # str | User ID

    try:
        # Log out for the user by ID
        api_instance.log_out_all_active_connections_for_user(user_id)
    except Exception as e:
        print("Exception when calling SecurityActiveConnectionsApi->log_out_all_active_connections_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID | 

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
**403** | Method not available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_out_all_except_this_connection**
> StringWrapper log_out_all_except_this_connection()

Log out from all connections

Logs out from all the active connections except the current connection.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
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
    api_instance = docspace.SecurityActiveConnectionsApi(api_client)

    try:
        # Log out from all connections
        api_response = api_instance.log_out_all_except_this_connection()
        print("The response of SecurityActiveConnectionsApi->log_out_all_except_this_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityActiveConnectionsApi->log_out_all_except_this_connection: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | Current user name |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

