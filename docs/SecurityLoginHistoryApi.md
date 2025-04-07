# docspace.SecurityLoginHistoryApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_login_history_report**](SecurityLoginHistoryApi.md#create_login_history_report) | **POST** /api/2.0/security/audit/login/report | Generate the login history report
[**get_last_login_events**](SecurityLoginHistoryApi.md#get_last_login_events) | **GET** /api/2.0/security/audit/login/last | Get login history
[**get_login_events_by_filter**](SecurityLoginHistoryApi.md#get_login_events_by_filter) | **GET** /api/2.0/security/audit/login/filter | Get filtered login events


# **create_login_history_report**
> StringWrapper create_login_history_report()

Generate the login history report

Generates the login history report.

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
    api_instance = docspace.SecurityLoginHistoryApi(api_client)

    try:
        # Generate the login history report
        api_response = api_instance.create_login_history_report()
        print("The response of SecurityLoginHistoryApi->create_login_history_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityLoginHistoryApi->create_login_history_report: %s\n" % e)
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
**200** | URL to the xlsx report file |  -  |
**401** | Unauthorized |  -  |
**402** | Your pricing plan does not support this option |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_login_events**
> LoginEventArrayWrapper get_last_login_events()

Get login history

Returns all the latest user login activity, including successful logins and error logs.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.login_event_array_wrapper import LoginEventArrayWrapper
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
    api_instance = docspace.SecurityLoginHistoryApi(api_client)

    try:
        # Get login history
        api_response = api_instance.get_last_login_events()
        print("The response of SecurityLoginHistoryApi->get_last_login_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityLoginHistoryApi->get_last_login_events: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LoginEventArrayWrapper**](LoginEventArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of login events |  -  |
**401** | Unauthorized |  -  |
**402** | Your pricing plan does not support this option |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_login_events_by_filter**
> LoginEventArrayWrapper get_login_events_by_filter(user_id=user_id, action=action, var_from=var_from, to=to)

Get filtered login events

Returns a list of the login events by the parameters specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.api_date_time import ApiDateTime
from docspace.models.login_event_array_wrapper import LoginEventArrayWrapper
from docspace.models.message_action import MessageAction
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
    api_instance = docspace.SecurityLoginHistoryApi(api_client)
    user_id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28' # str | User ID (optional)
    action = docspace.MessageAction() # MessageAction | Action (optional)
    var_from = docspace.ApiDateTime() # ApiDateTime | Start date (optional)
    to = docspace.ApiDateTime() # ApiDateTime | End date (optional)

    try:
        # Get filtered login events
        api_response = api_instance.get_login_events_by_filter(user_id=user_id, action=action, var_from=var_from, to=to)
        print("The response of SecurityLoginHistoryApi->get_login_events_by_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityLoginHistoryApi->get_login_events_by_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID | [optional] 
 **action** | [**MessageAction**](.md)| Action | [optional] 
 **var_from** | [**ApiDateTime**](.md)| Start date | [optional] 
 **to** | [**ApiDateTime**](.md)| End date | [optional] 

### Return type

[**LoginEventArrayWrapper**](LoginEventArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of filtered login events |  -  |
**401** | Unauthorized |  -  |
**402** | Your pricing plan does not support this option |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

