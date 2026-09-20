# docspace_api_sdk.AuditTrailDataApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_audit_trail_report**](#create_audit_trail_report) | **POST** /api/2.0/security/audit/events/report | Start audit trail report
[**get_audit_events_by_filter**](#get_audit_events_by_filter) | **GET** /api/2.0/security/audit/events/filter | Get filtered audit events
[**get_audit_settings**](#get_audit_settings) | **GET** /api/2.0/security/audit/settings/lifetime | Get audit lifetime settings
[**get_audit_trail_mappers**](#get_audit_trail_mappers) | **GET** /api/2.0/security/audit/mappers | Get audit trail mappers
[**get_audit_trail_report**](#get_audit_trail_report) | **GET** /api/2.0/security/audit/events/report | Get audit trail report status
[**get_audit_trail_types**](#get_audit_trail_types) | **GET** /api/2.0/security/audit/types | Get audit trail types
[**get_last_audit_events**](#get_last_audit_events) | **GET** /api/2.0/security/audit/events/last | Get recent audit events
[**set_audit_settings**](#set_audit_settings) | **POST** /api/2.0/security/audit/settings/lifetime | Set audit lifetime settings
[**terminate_audit_trail_report**](#terminate_audit_trail_report) | **DELETE** /api/2.0/security/audit/events/report | Terminate audit trail report


# **create_audit_trail_report**
> DocumentBuilderTaskWrapper create_audit_trail_report(format=format)

Queues a report of the portal's audit trail and returns the state of the background job that builds it. The
report covers the period reaching from now back by the audit trail lifetime that
`GET api/2.0/security/audit/settings/lifetime` reports and is never filtered: the query parameters of
`GET api/2.0/security/audit/events/filter` do not apply here. The caller needs the portal-settings right of a
DocSpace administrator plus the audit option of the portal's pricing plan, otherwise the call is answered with
402. The file is not ready when the response arrives - poll `GET api/2.0/security/audit/events/report` until
`isCompleted` is true, then take `resultFileUrl`, and treat a non-empty `error` as a failed build. The
finished file is saved to the caller's My documents section, as an XLSX workbook by default or as CSV when
`format=Csv`, in which case `resultFileId` stays empty and only the name and the URL identify it. One job runs
per caller and kind: calling again while the previous one is still building returns that job instead of
starting a second, and `DELETE api/2.0/security/audit/events/report` cancels it.

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
    api_instance = docspace_api_sdk.AuditTrailDataApi(api_client)
    format = docspace_api_sdk.AuditReportFormat() # AuditReportFormat | The format the report file is written in. The workbook format is the default and is the only one that leaves  the finished file addressable by ID: a report asked for as CSV comes back with an empty `resultFileId`, so it  can only be reached through `resultFileName` and `resultFileUrl`. (optional)

    try:
        # Start audit trail report
        api_response = api_instance.create_audit_trail_report(format=format)
        print("The response of AuditTrailDataApi->create_audit_trail_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditTrailDataApi->create_audit_trail_report: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The state of the queued job that builds the audit trail report |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**402** | The portal's pricing plan has no audit option, or the login history and audit trail section is not enabled |  -  |
**403** | The caller does not have the portal-settings right of a DocSpace administrator |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_events_by_filter**
> AuditEventArrayWrapper get_audit_events_by_filter(user_id=user_id, module_type=module_type, action_type=action_type, action=action, entry_type=entry_type, target=target, var_from=var_from, to=to, count=count, start_index=start_index)

Returns the portal's audit events that match the filters in the query - by the user who acted, the module the
action belongs to, the action and its type, the entity type and target, and the period - and is the operation
behind the audit trail page. The caller needs the portal-settings right of a DocSpace administrator plus the
audit option of the portal's pricing plan; when that option is missing the filters are silently ignored and
the answer is the same twenty most recent events that `GET api/2.0/security/audit/events/last` returns, and
when the login history and audit trail section is disabled altogether the call is answered with 402. Take the
values accepted by `action`, `actionType`, `moduleType` and `entryType` from
`GET api/2.0/security/audit/types`, and the tree they belong to from `GET api/2.0/security/audit/mappers`. A
non-default `action` matches only that action and, combined with `target`, only its exact value; it also
stops `moduleType` and `actionType` from narrowing the result, so combine `target` with `entryType` instead of
`action` when filtering by target without pinning a single action. `from` and `to` are read as UTC instants
while `date` comes back in the portal time zone, `count` defaults to 100 and cannot exceed it, and the filters
are applied before the page window, so a full page means there may be more matching events beyond it. The
operation is read-only.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **UUID**| The user who performed the action, given by portal user ID. Leave it at the empty GUID to keep the events of  every user. | [optional] 
 **module_type** | [**LocationType**](.md)| The module the recorded action belongs to, spelled as `GET api/2.0/security/audit/types` lists it under  `moduleTypes`. `GET api/2.0/security/audit/mappers` shows which module records which action. The default  value keeps every module. | [optional] 
 **action_type** | [**ActionType**](.md)| The kind of change the action made, spelled as `GET api/2.0/security/audit/types` lists it under  `actionTypes`. The default value keeps every kind. | [optional] 
 **action** | [**MessageAction**](.md)| The exact action recorded, spelled as the `messageAction` of `GET api/2.0/security/audit/mappers`. Naming  one narrows the answer to that single action and overrides `moduleType` and `actionType`, which stop  narrowing anything once it is set. | [optional] 
 **entry_type** | [**EntryType**](.md)| The kind of object the action was performed on, spelled as `GET api/2.0/security/audit/types` lists it under  `entryTypes`. Pair it with `target` to filter by object without pinning a single action. | [optional] 
 **target** | **str**| The object the action was performed on, as the audit trail recorded it - a file name, a user account, a room  title. It is matched in full and exactly as stored, so it narrows the answer only when `action` or  `entryType` is set as well. | [optional] 
 **var_from** | **datetime**| The earliest moment an event may have been recorded at, read as a UTC instant. The `date` of the events that  come back is in the portal time zone instead, so the two do not line up on a portal that is not on UTC. | [optional] 
 **to** | **datetime**| The latest moment an event may have been recorded at, read as a UTC instant in the same way as `from`. | [optional] 
 **count** | **int**| How many events one page may hold. The maximum is also the default, so a client that wants shorter pages has  to ask for them; a full page means there may be further matches beyond it. | [optional] 
 **start_index** | **int**| How many matching events to skip before the page begins, counting from the newest. Advance it by `count` to  walk backwards through the trail. | [optional] 

### Return type

[**AuditEventArrayWrapper**](AuditEventArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.action_type import ActionType
from docspace_api_sdk.models.audit_event_array_wrapper import AuditEventArrayWrapper
from docspace_api_sdk.models.entry_type import EntryType
from docspace_api_sdk.models.location_type import LocationType
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
    api_instance = docspace_api_sdk.AuditTrailDataApi(api_client)
    user_id = UUID('00000000-0000-0000-0000-000000000001') # UUID | The user who performed the action, given by portal user ID. Leave it at the empty GUID to keep the events of  every user. (optional)
    module_type = docspace_api_sdk.LocationType() # LocationType | The module the recorded action belongs to, spelled as `GET api/2.0/security/audit/types` lists it under  `moduleTypes`. `GET api/2.0/security/audit/mappers` shows which module records which action. The default  value keeps every module. (optional)
    action_type = docspace_api_sdk.ActionType() # ActionType | The kind of change the action made, spelled as `GET api/2.0/security/audit/types` lists it under  `actionTypes`. The default value keeps every kind. (optional)
    action = docspace_api_sdk.MessageAction() # MessageAction | The exact action recorded, spelled as the `messageAction` of `GET api/2.0/security/audit/mappers`. Naming  one narrows the answer to that single action and overrides `moduleType` and `actionType`, which stop  narrowing anything once it is set. (optional)
    entry_type = docspace_api_sdk.EntryType() # EntryType | The kind of object the action was performed on, spelled as `GET api/2.0/security/audit/types` lists it under  `entryTypes`. Pair it with `target` to filter by object without pinning a single action. (optional)
    target = 'document.docx' # str | The object the action was performed on, as the audit trail recorded it - a file name, a user account, a room  title. It is matched in full and exactly as stored, so it narrows the answer only when `action` or  `entryType` is set as well. (optional)
    var_from = '2024-01-01T00:00:00Z' # datetime | The earliest moment an event may have been recorded at, read as a UTC instant. The `date` of the events that  come back is in the portal time zone instead, so the two do not line up on a portal that is not on UTC. (optional)
    to = '2024-01-31T23:59:59Z' # datetime | The latest moment an event may have been recorded at, read as a UTC instant in the same way as `from`. (optional)
    count = 100 # int | How many events one page may hold. The maximum is also the default, so a client that wants shorter pages has  to ask for them; a full page means there may be further matches beyond it. (optional)
    start_index = 0 # int | How many matching events to skip before the page begins, counting from the newest. Advance it by `count` to  walk backwards through the trail. (optional)

    try:
        # Get filtered audit events
        api_response = api_instance.get_audit_events_by_filter(user_id=user_id, module_type=module_type, action_type=action_type, action=action, entry_type=entry_type, target=target, var_from=var_from, to=to, count=count, start_index=start_index)
        print("The response of AuditTrailDataApi->get_audit_events_by_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditTrailDataApi->get_audit_events_by_filter: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audit events matching the filters, newest first, or the twenty most recent events when the portal has no audit option |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**402** | The login history and audit trail section is not enabled for this portal |  -  |
**403** | The caller does not have the portal-settings right of a DocSpace administrator |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_settings**
> TenantAuditSettingsResponseWrapper get_audit_settings()

Returns how long this portal keeps its two security logs: `loginHistoryLifeTime` for login events and
`auditTrailLifeTime` for audit events, both counted in days, together with `lastModified`, the moment the pair
was last saved. The caller needs the portal-settings right of a DocSpace administrator, and in a cloud
installation the login history and audit trail section must be enabled for the portal, otherwise the call is
answered with 402; the audit option of the pricing plan is not required to read the values. Both numbers lie
between 1 and 180 days, and a portal that never changed them reports the default of 180. They define the
window the rest of the audit operations work in: `GET api/2.0/security/audit/events/last` looks exactly this
far back, and the reports started by `POST api/2.0/security/audit/login/report` and
`POST api/2.0/security/audit/events/report` cover exactly this period. The operation is read-only; change the
values with `POST api/2.0/security/audit/settings/lifetime`.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**TenantAuditSettingsResponseWrapper**](TenantAuditSettingsResponseWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.tenant_audit_settings_response_wrapper import TenantAuditSettingsResponseWrapper
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
    api_instance = docspace_api_sdk.AuditTrailDataApi(api_client)

    try:
        # Get audit lifetime settings
        api_response = api_instance.get_audit_settings()
        print("The response of AuditTrailDataApi->get_audit_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditTrailDataApi->get_audit_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The login history and audit trail lifetimes of the portal, in days |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**402** | The login history and audit trail section is not enabled for this portal |  -  |
**403** | The caller does not have the portal-settings right of a DocSpace administrator |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_trail_mappers**
> AuditTrailProductMapperArrayWrapper get_audit_trail_mappers(product_type=product_type, module_type=module_type)

Returns the audit vocabulary as the tree it really is: every product, the modules inside it, and for each
module the actions it can record together with the type of change and the entity each of them applies to. Pass
`productType` to keep a single product and `moduleType` to keep a single module inside the products that
remain; omit both to get the whole tree. The caller needs the portal-settings right of a DocSpace
administrator; the audit option of the pricing plan is not required, and the call is read-only and safe to
repeat. Each action carries `messageAction`, the name to send as the `action` filter of
`GET api/2.0/security/audit/events/filter`, next to `actionType` and `entity`, the values its `actionType` and
`entryType` filters accept - this is where a caller learns which action belongs to which module instead of
guessing. A filter that matches nothing yields an empty list rather than an error. Use
`GET api/2.0/security/audit/types` for the flat lists of the same names.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_type** | [**ProductType**](.md)| The product to keep, spelled as `GET api/2.0/security/audit/types` lists it under `productTypes`. Omitting  it keeps every product; a value no product matches yields an empty list rather than an error. | [optional] 
 **module_type** | [**LocationType**](.md)| The module to keep inside the products that survive `productType`, spelled as  `GET api/2.0/security/audit/types` lists it under `moduleTypes`. Omitting it keeps every module of those  products. | [optional] 

### Return type

[**AuditTrailProductMapperArrayWrapper**](AuditTrailProductMapperArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.audit_trail_product_mapper_array_wrapper import AuditTrailProductMapperArrayWrapper
from docspace_api_sdk.models.location_type import LocationType
from docspace_api_sdk.models.product_type import ProductType
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
    api_instance = docspace_api_sdk.AuditTrailDataApi(api_client)
    product_type = docspace_api_sdk.ProductType() # ProductType | The product to keep, spelled as `GET api/2.0/security/audit/types` lists it under `productTypes`. Omitting  it keeps every product; a value no product matches yields an empty list rather than an error. (optional)
    module_type = docspace_api_sdk.LocationType() # LocationType | The module to keep inside the products that survive `productType`, spelled as  `GET api/2.0/security/audit/types` lists it under `moduleTypes`. Omitting it keeps every module of those  products. (optional)

    try:
        # Get audit trail mappers
        api_response = api_instance.get_audit_trail_mappers(product_type=product_type, module_type=module_type)
        print("The response of AuditTrailDataApi->get_audit_trail_mappers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditTrailDataApi->get_audit_trail_mappers: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The products with their modules and the actions each module can record |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller does not have the portal-settings right of a DocSpace administrator |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_trail_report**
> DocumentBuilderTaskWrapper get_audit_trail_report()

Returns the state of the audit trail report the calling user has started, and is the operation to poll after
`POST api/2.0/security/audit/events/report`. The caller needs the portal-settings right of a DocSpace
administrator plus the audit option of the portal's pricing plan, otherwise the call is answered with 402.
Jobs are kept per user and per report kind: this operation never shows another administrator's report, nor the
login history report, which has its own status at `GET api/2.0/security/audit/login/report`. The answer is
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
    api_instance = docspace_api_sdk.AuditTrailDataApi(api_client)

    try:
        # Get audit trail report status
        api_response = api_instance.get_audit_trail_report()
        print("The response of AuditTrailDataApi->get_audit_trail_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditTrailDataApi->get_audit_trail_report: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The state of the caller's audit trail report, or an empty answer when none is known |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**402** | The portal's pricing plan has no audit option, or the login history and audit trail section is not enabled |  -  |
**403** | The caller does not have the portal-settings right of a DocSpace administrator |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_trail_types**
> AuditTrailTypesWrapper get_audit_trail_types()

Returns the vocabularies the audit filters are built from: `actions` lists every action the portal can record,
`actionTypes` the kinds of change they stand for, `productTypes` the products they belong to, `moduleTypes`
the locations inside those products, and `entryTypes` the kinds of entity an action can be applied to. The
caller needs the portal-settings right of a DocSpace administrator; the audit option of the pricing plan is
not required, so the lists can be read on any portal. The operation is read-only, takes no parameters and
depends on nothing else. Every value is the name to send in the matching query parameter of
`GET api/2.0/security/audit/events/filter` or `GET api/2.0/security/audit/login/filter`, so read this
operation once and reuse the answer instead of guessing spellings. The response is an untyped object holding
those five arrays of names, and it changes only with the portal version. Use
`GET api/2.0/security/audit/mappers` when the relations between products, modules and actions are needed
rather than the flat lists.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**AuditTrailTypesWrapper**](AuditTrailTypesWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.audit_trail_types_wrapper import AuditTrailTypesWrapper
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
    api_instance = docspace_api_sdk.AuditTrailDataApi(api_client)

    try:
        # Get audit trail types
        api_response = api_instance.get_audit_trail_types()
        print("The response of AuditTrailDataApi->get_audit_trail_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditTrailDataApi->get_audit_trail_types: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The action, action type, product, module and entry type names accepted by the audit filters |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller does not have the portal-settings right of a DocSpace administrator |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_audit_events**
> AuditEventArrayWrapper get_last_audit_events()

Returns the twenty most recent audit events of the portal - the creations, changes, deletions, sharing and
settings updates its members made - as the short summary a settings page shows before anyone asks for the full
trail. The caller needs the portal-settings right of a DocSpace administrator, and in a cloud installation the
login history and audit trail section must be enabled for the portal, otherwise the call is answered with 402.
The operation is read-only and takes no parameters: it looks back exactly as far as the audit trail lifetime
that `GET api/2.0/security/audit/settings/lifetime` reports, returns at most twenty events ordered newest
first, and cannot be filtered. `date` is given in the portal time zone, `actionText` is the readable sentence
describing the event with every substituted value shortened to fifty characters here, and `target` names the
entity the action was applied to. An empty list means nothing was recorded inside that period. Use
`GET api/2.0/security/audit/events/filter` to filter by user, module, action or period.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**AuditEventArrayWrapper**](AuditEventArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.audit_event_array_wrapper import AuditEventArrayWrapper
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
    api_instance = docspace_api_sdk.AuditTrailDataApi(api_client)

    try:
        # Get recent audit events
        api_response = api_instance.get_last_audit_events()
        print("The response of AuditTrailDataApi->get_last_audit_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditTrailDataApi->get_last_audit_events: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The twenty most recent audit events of the portal, newest first |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**402** | The login history and audit trail section is not enabled for this portal |  -  |
**403** | The caller does not have the portal-settings right of a DocSpace administrator |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_audit_settings**
> TenantAuditSettingsResponseWrapper set_audit_settings(tenant_audit_settings_wrapper=tenant_audit_settings_wrapper)

Sets how long this portal keeps its login history and its audit trail, in days, and returns the pair as it was
stored. The caller needs the portal-settings right of a DocSpace administrator plus the audit option of the
portal's pricing plan, otherwise the call is answered with 402. Send both numbers inside `settings`: each has
to be between 1 and 180 days, and a value outside that range is refused with 400 without either number being
saved, so read the current pair from `GET api/2.0/security/audit/settings/lifetime` and resend the one that
should stay as it is. The call replaces the stored settings rather than merging them, is idempotent, and takes
effect at once: the period covered by `GET api/2.0/security/audit/events/last` and by both audit reports
shrinks or grows with it, and events older than the new lifetime stop being reported. The change is itself
recorded in the audit trail.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_audit_settings_wrapper** | [**TenantAuditSettingsWrapper**](TenantAuditSettingsWrapper.md)|  | [optional] 

### Return type

[**TenantAuditSettingsResponseWrapper**](TenantAuditSettingsResponseWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.tenant_audit_settings_response_wrapper import TenantAuditSettingsResponseWrapper
from docspace_api_sdk.models.tenant_audit_settings_wrapper import TenantAuditSettingsWrapper
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
    api_instance = docspace_api_sdk.AuditTrailDataApi(api_client)
    tenant_audit_settings_wrapper = docspace_api_sdk.TenantAuditSettingsWrapper() # TenantAuditSettingsWrapper |  (optional)

    try:
        # Set audit lifetime settings
        api_response = api_instance.set_audit_settings(tenant_audit_settings_wrapper=tenant_audit_settings_wrapper)
        print("The response of AuditTrailDataApi->set_audit_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditTrailDataApi->set_audit_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The login history and audit trail lifetimes as they were stored |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | A lifetime is outside the allowed range of 1 to 180 days |  -  |
**402** | The portal's pricing plan has no audit option, or the login history and audit trail section is not enabled |  -  |
**403** | The caller does not have the portal-settings right of a DocSpace administrator |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_audit_trail_report**
> terminate_audit_trail_report()

Cancels the audit trail report the calling user has running and drops it from the build queue. The caller
needs the portal-settings right of a DocSpace administrator plus the audit option of the portal's pricing
plan, otherwise the call is answered with 402. Cancellation is handed to the same background service that
builds the report, so a successful answer means the request was accepted rather than that the job has already
stopped: poll `GET api/2.0/security/audit/events/report` to watch it disappear. The operation returns no
content and touches only the caller's own audit trail report - the login history report is cancelled by
`DELETE api/2.0/security/audit/login/report`, and no report of another user can be reached from here. It is
idempotent: cancelling when nothing is running is not an error. A job stopped before it finished writing
leaves nothing in My documents, and a report cancelled by mistake has to be built again with
`POST api/2.0/security/audit/events/report`.

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
    api_instance = docspace_api_sdk.AuditTrailDataApi(api_client)

    try:
        # Terminate audit trail report
        api_instance.terminate_audit_trail_report()
    except Exception as e:
        print("Exception when calling AuditTrailDataApi->terminate_audit_trail_report: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The cancellation of the caller's audit trail report has been accepted |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**402** | The portal's pricing plan has no audit option, or the login history and audit trail section is not enabled |  -  |
**403** | The caller does not have the portal-settings right of a DocSpace administrator |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

