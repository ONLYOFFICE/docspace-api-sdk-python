# docspace_api_sdk.LoginHistoryApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_login_history_report**](#create_login_history_report) | **POST** /api/2.0/security/audit/login/report | Generate the login history report
[**get_last_login_events**](#get_last_login_events) | **GET** /api/2.0/security/audit/login/last | Get login history
[**get_login_events_by_filter**](#get_login_events_by_filter) | **GET** /api/2.0/security/audit/login/filter | Get filtered login events


# **create_login_history_report**
> StringWrapper create_login_history_report()

Generates the login history report.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.string_wrapper import StringWrapper
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
    api_instance = docspace_api_sdk.LoginHistoryApi(api_client)

    try:
        # Generate the login history report
        api_response = api_instance.create_login_history_report()
        print("The response of LoginHistoryApi->create_login_history_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginHistoryApi->create_login_history_report: %s\n" % e)
```



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

Returns all the latest user login activity, including successful logins and error logs.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**LoginEventArrayWrapper**](LoginEventArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.login_event_array_wrapper import LoginEventArrayWrapper
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
    api_instance = docspace_api_sdk.LoginHistoryApi(api_client)

    try:
        # Get login history
        api_response = api_instance.get_last_login_events()
        print("The response of LoginHistoryApi->get_last_login_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginHistoryApi->get_last_login_events: %s\n" % e)
```



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
> LoginEventArrayWrapper get_login_events_by_filter(user_id=user_id, action=action, var_from=var_from, to=to, count=count, start_index=start_index)

Returns a list of the login events by the parameters specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user whose login events are being queried. | [optional] 
 **action** | [**MessageAction**](.md)| The login-related action to filter events by. | [optional] 
 **var_from** | [**ApiDateTime**](.md)| The starting date and time for filtering login events. | [optional] 
 **to** | [**ApiDateTime**](.md)| The ending date and time for filtering login events. | [optional] 
 **count** | **int**| The number of login events to retrieve in the query. | [optional] 
 **start_index** | **int**| The starting index for fetching a subset of login events from the query results. | [optional] 

### Return type

[**LoginEventArrayWrapper**](LoginEventArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.api_date_time import ApiDateTime
from docspace_api_sdk.models.login_event_array_wrapper import LoginEventArrayWrapper
from docspace_api_sdk.models.message_action import MessageAction
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
    api_instance = docspace_api_sdk.LoginHistoryApi(api_client)
    user_id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28' # str | The ID of the user whose login events are being queried. (optional)
    action = docspace_api_sdk.MessageAction() # MessageAction | The login-related action to filter events by. (optional)
    var_from = docspace_api_sdk.ApiDateTime() # ApiDateTime | The starting date and time for filtering login events. (optional)
    to = docspace_api_sdk.ApiDateTime() # ApiDateTime | The ending date and time for filtering login events. (optional)
    count = 1234 # int | The number of login events to retrieve in the query. (optional)
    start_index = 1234 # int | The starting index for fetching a subset of login events from the query results. (optional)

    try:
        # Get filtered login events
        api_response = api_instance.get_login_events_by_filter(user_id=user_id, action=action, var_from=var_from, to=to, count=count, start_index=start_index)
        print("The response of LoginHistoryApi->get_login_events_by_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginHistoryApi->get_login_events_by_filter: %s\n" % e)
```



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

