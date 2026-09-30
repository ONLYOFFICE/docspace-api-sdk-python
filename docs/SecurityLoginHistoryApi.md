# docspace_api_sdk.LoginHistoryApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_login_history_report**](#create_login_history_report) | **POST** /api/2.0/security/audit/login/report | Start login history report
[**get_last_login_events**](#get_last_login_events) | **GET** /api/2.0/security/audit/login/last | Get recent login events
[**get_login_events_by_filter**](#get_login_events_by_filter) | **GET** /api/2.0/security/audit/login/filter | Get filtered login events
[**get_login_history_report**](#get_login_history_report) | **GET** /api/2.0/security/audit/login/report | Get login history report status
[**terminate_login_history_report**](#terminate_login_history_report) | **DELETE** /api/2.0/security/audit/login/report | Terminate login history report


# **create_login_history_report**
> DocumentBuilderTaskWrapper create_login_history_report(format=format)

Queues a report of the portal's login history and returns the state of the background job that builds it. The
report covers the period reaching from now back by the login history lifetime that
`GET api/2.0/security/audit/settings/lifetime` reports and is never filtered: the query parameters of
`GET api/2.0/security/audit/login/filter` do not apply here. The caller needs the portal-settings right of a
DocSpace administrator plus the audit option of the portal's pricing plan, otherwise the call is answered with
402. The file is not ready when the response arrives - poll `GET api/2.0/security/audit/login/report` until
`isCompleted` is true, then take `resultFileUrl`, and treat a non-empty `error` as a failed build. The
finished file is saved to the caller's My documents section, as an XLSX workbook by default or as CSV when
`format=Csv`, in which case `resultFileId` stays empty and only the name and the URL identify it. One job runs
per caller and kind: calling again while the previous one is still building returns that job instead of
starting a second, and `DELETE api/2.0/security/audit/login/report` cancels it.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**AuditReportFormat**](.md)| The format the report file is written in. The workbook format is the default and is the only one that leaves  the finished file addressable by ID: a report asked for as CSV comes back with an empty `resultFileId`, so it  can only be reached through `resultFileName` and `resultFileUrl`. | [optional] 

### Return type

[**DocumentBuilderTaskWrapper**](DocumentBuilderTaskWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.audit_report_format import AuditReportFormat
from docspace_api_sdk.models.document_builder_task_wrapper import DocumentBuilderTaskWrapper
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
    format = docspace_api_sdk.AuditReportFormat() # AuditReportFormat | The format the report file is written in. The workbook format is the default and is the only one that leaves  the finished file addressable by ID: a report asked for as CSV comes back with an empty `resultFileId`, so it  can only be reached through `resultFileName` and `resultFileUrl`. (optional)

    try:
        # Start login history report
        api_response = api_instance.create_login_history_report(format=format)
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
**200** | The state of the queued job that builds the login history report |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**402** | The portal's pricing plan has no audit option, or the login history and audit trail section is not enabled |  -  |
**403** | The caller does not have the portal-settings right of a DocSpace administrator |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_login_events**
> LoginEventArrayWrapper get_last_login_events()

Returns the twenty most recent login events of the whole portal - successful sign-ins, sign-outs and failed
attempts alike - as the short summary a settings page shows before anyone asks for the full history. The
caller needs the portal-settings right of a DocSpace administrator, and in a cloud installation the login
history and audit trail section must be enabled for the portal, otherwise the call is answered with 402. The
operation is read-only and takes no parameters: the number of events is fixed at twenty, nothing can be
filtered, and events are ordered newest first. `date` is given in the portal time zone, `actionText` is the
readable sentence describing the event with every substituted value shortened to fifty characters here, and
`country` and `city` are resolved from the IP address and stay empty when it cannot be located. An empty list
means the portal has recorded no login events yet. Use `GET api/2.0/security/audit/login/filter` to filter by
user, action or period and to page through the whole history.

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
        # Get recent login events
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
**200** | The twenty most recent login events of the portal, newest first |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**402** | The login history and audit trail section is not enabled for this portal |  -  |
**403** | The caller does not have the portal-settings right of a DocSpace administrator |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_login_events_by_filter**
> LoginEventArrayWrapper get_login_events_by_filter(user_id=user_id, action=action, var_from=var_from, to=to, count=count, start_index=start_index)

Returns the portal's login events that match the filters in the query - by user, by login action and by period
- and is the operation behind the login history page. The caller needs the portal-settings right of a DocSpace
administrator plus the audit option of the portal's pricing plan; when that option is missing the filters are
silently ignored and the answer is the same twenty most recent events that
`GET api/2.0/security/audit/login/last` returns, and when the login history and audit trail section is
disabled altogether the call is answered with 402. Omit a filter to match everything. `from` and `to` are read
as UTC instants while `date` comes back in the portal time zone, `count` defaults to 100 and cannot exceed it,
`startIndex` skips events from the newest end, and the page window is applied to the log before the filters,
so a page can hold fewer items than `count` while older matches still exist. The operation is read-only; take
the values accepted by `action` from `GET api/2.0/security/audit/types`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **UUID**| The user whose sign-in attempts are kept, given by portal user ID. Leave it at the empty GUID to keep the  events of every user. | [optional] 
 **action** | [**MessageAction**](.md)| The sign-in action recorded, spelled as `GET api/2.0/security/audit/types` lists it under `actions` - a  successful login, a failed one, a logout. The default value keeps every action. | [optional] 
 **var_from** | **datetime**| The earliest moment an event may have been recorded at, read as a UTC instant. The `date` of the events that  come back is in the portal time zone instead, so the two do not line up on a portal that is not on UTC. | [optional] 
 **to** | **datetime**| The latest moment an event may have been recorded at, read as a UTC instant in the same way as `from`. | [optional] 
 **count** | **int**| How many events one page may hold. The maximum is also the default, so a client that wants shorter pages has  to ask for them. | [optional] 
 **start_index** | **int**| How many events to skip before the page begins, counting from the newest. It is applied to the log before  the filters, so a page can hold fewer events than `count` while older matches still exist. | [optional] 

### Return type

[**LoginEventArrayWrapper**](LoginEventArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
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
    user_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The user whose sign-in attempts are kept, given by portal user ID. Leave it at the empty GUID to keep the  events of every user. (optional)
    action = docspace_api_sdk.MessageAction() # MessageAction | The sign-in action recorded, spelled as `GET api/2.0/security/audit/types` lists it under `actions` - a  successful login, a failed one, a logout. The default value keeps every action. (optional)
    var_from = '2024-01-15T10:30:00Z' # datetime | The earliest moment an event may have been recorded at, read as a UTC instant. The `date` of the events that  come back is in the portal time zone instead, so the two do not line up on a portal that is not on UTC. (optional)
    to = '2024-01-15T10:30:00Z' # datetime | The latest moment an event may have been recorded at, read as a UTC instant in the same way as `from`. (optional)
    count = 1 # int | How many events one page may hold. The maximum is also the default, so a client that wants shorter pages has  to ask for them. (optional)
    start_index = 1 # int | How many events to skip before the page begins, counting from the newest. It is applied to the log before  the filters, so a page can hold fewer events than `count` while older matches still exist. (optional)

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
**200** | Login events matching the filters, newest first, or the twenty most recent events when the portal has no audit option |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**402** | The login history and audit trail section is not enabled for this portal |  -  |
**403** | The caller does not have the portal-settings right of a DocSpace administrator |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_login_history_report**
> DocumentBuilderTaskWrapper get_login_history_report()

Returns the state of the login history report the calling user has started, and is the operation to poll after
`POST api/2.0/security/audit/login/report`. The caller needs the portal-settings right of a DocSpace
administrator plus the audit option of the portal's pricing plan, otherwise the call is answered with 402.
Jobs are kept per user and per report kind: this operation never shows another administrator's report, nor the
audit trail report, which has its own status at `GET api/2.0/security/audit/events/report`. The answer is
empty when no report of this kind is known for the caller; otherwise `percentage` grows towards 100,
`isCompleted` turns true when the build has ended, `error` carries the failure message when it ended badly,
and `resultFileName` and `resultFileUrl` point at the file saved to the caller's My documents section, while
`resultFileId` is filled for an XLSX report only. The operation is read-only and safe to poll every few
seconds; a finished job is dropped as soon as the next report of this kind is started.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**DocumentBuilderTaskWrapper**](DocumentBuilderTaskWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.document_builder_task_wrapper import DocumentBuilderTaskWrapper
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
        # Get login history report status
        api_response = api_instance.get_login_history_report()
        print("The response of LoginHistoryApi->get_login_history_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginHistoryApi->get_login_history_report: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The state of the caller's login history report, or an empty answer when none is known |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**402** | The portal's pricing plan has no audit option, or the login history and audit trail section is not enabled |  -  |
**403** | The caller does not have the portal-settings right of a DocSpace administrator |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_login_history_report**
> terminate_login_history_report()

Cancels the login history report the calling user has running and drops it from the build queue. The caller
needs the portal-settings right of a DocSpace administrator plus the audit option of the portal's pricing
plan, otherwise the call is answered with 402. Cancellation is handed to the same background service that
builds the report, so a successful answer means the request was accepted rather than that the job has already
stopped: poll `GET api/2.0/security/audit/login/report` to watch it disappear. The operation returns no
content and touches only the caller's own login history report - the audit trail report is cancelled by
`DELETE api/2.0/security/audit/events/report`, and no report of another user can be reached from here. It is
idempotent: cancelling when nothing is running is not an error. A job stopped before it finished writing
leaves nothing in My documents, and a report cancelled by mistake has to be built again with
`POST api/2.0/security/audit/login/report`.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

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
    api_instance = docspace_api_sdk.LoginHistoryApi(api_client)

    try:
        # Terminate login history report
        api_instance.terminate_login_history_report()
    except Exception as e:
        print("Exception when calling LoginHistoryApi->terminate_login_history_report: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The cancellation of the caller's login history report has been accepted |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**402** | The portal's pricing plan has no audit option, or the login history and audit trail section is not enabled |  -  |
**403** | The caller does not have the portal-settings right of a DocSpace administrator |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

