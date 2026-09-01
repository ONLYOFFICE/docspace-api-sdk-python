# docspace_api_sdk.AuditTrailDataApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_audit_trail_report**](#create_audit_trail_report) | **POST** /api/2.0/security/audit/events/report | Start the audit trail report generation
[**get_audit_events_by_filter**](#get_audit_events_by_filter) | **GET** /api/2.0/security/audit/events/filter | Get filtered audit trail data
[**get_audit_settings**](#get_audit_settings) | **GET** /api/2.0/security/audit/settings/lifetime | Get the audit trail settings
[**get_audit_trail_mappers**](#get_audit_trail_mappers) | **GET** /api/2.0/security/audit/mappers | Get audit trail mappers
[**get_audit_trail_report**](#get_audit_trail_report) | **GET** /api/2.0/security/audit/events/report | Get the audit trail report generation status
[**get_audit_trail_types**](#get_audit_trail_types) | **GET** /api/2.0/security/audit/types | Get audit trail types
[**get_last_audit_events**](#get_last_audit_events) | **GET** /api/2.0/security/audit/events/last | Get audit trail data
[**set_audit_settings**](#set_audit_settings) | **POST** /api/2.0/security/audit/settings/lifetime | Set the audit trail settings
[**terminate_audit_trail_report**](#terminate_audit_trail_report) | **DELETE** /api/2.0/security/audit/events/report | Terminate the audit trail report generation


# **create_audit_trail_report**
> DocumentBuilderTaskWrapper create_audit_trail_report(format=format)

Starts generating the audit trail report (XLSX by default, or CSV) and saves it to My documents.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**AuditReportFormat**](.md)| The output file format of the report. Defaults to XLSX. | [optional] 

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
    format = docspace_api_sdk.AuditReportFormat() # AuditReportFormat | The output file format of the report. Defaults to XLSX. (optional)

    try:
        # Start the audit trail report generation
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
**200** | Operation execution status |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**402** | Your pricing plan does not support this option |  -  |
**403** | You don't have enough permission to create |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_events_by_filter**
> AuditEventArrayWrapper get_audit_events_by_filter(user_id=user_id, module_type=module_type, action_type=action_type, action=action, entry_type=entry_type, target=target, var_from=var_from, to=to, count=count, start_index=start_index)

Returns a list of the audit events by the parameters specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **UUID**| The ID of the user who triggered the audit event. | [optional] 
 **module_type** | [**LocationType**](.md)| The location where the audit event occurred. | [optional] 
 **action_type** | [**ActionType**](.md)| The type of action performed in the audit event (e.g., Create, Update, Delete). | [optional] 
 **action** | [**MessageAction**](.md)| The specific action that occurred within the audit event. | [optional] 
 **entry_type** | [**EntryType**](.md)| The type of audit entry (e.g., Folder, User, File). | [optional] 
 **target** | **str**| The target object affected by the audit event (e.g., document ID, user account). | [optional] 
 **var_from** | [**ApiDateTime**](.md)| The starting date and time for filtering audit events. | [optional] 
 **to** | [**ApiDateTime**](.md)| The ending date and time for filtering audit events. | [optional] 
 **count** | **int**| The maximum number of audit event records to retrieve. | [optional] 
 **start_index** | **int**| The index of the first audit event record to retrieve in a paged query. | [optional] 

### Return type

[**AuditEventArrayWrapper**](AuditEventArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.action_type import ActionType
from docspace_api_sdk.models.api_date_time import ApiDateTime
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
    user_id = UUID('00000000-0000-0000-0000-000000000001') # UUID | The ID of the user who triggered the audit event. (optional)
    module_type = docspace_api_sdk.LocationType() # LocationType | The location where the audit event occurred. (optional)
    action_type = docspace_api_sdk.ActionType() # ActionType | The type of action performed in the audit event (e.g., Create, Update, Delete). (optional)
    action = docspace_api_sdk.MessageAction() # MessageAction | The specific action that occurred within the audit event. (optional)
    entry_type = docspace_api_sdk.EntryType() # EntryType | The type of audit entry (e.g., Folder, User, File). (optional)
    target = 'document.docx' # str | The target object affected by the audit event (e.g., document ID, user account). (optional)
    var_from = docspace_api_sdk.ApiDateTime() # ApiDateTime | The starting date and time for filtering audit events. (optional)
    to = docspace_api_sdk.ApiDateTime() # ApiDateTime | The ending date and time for filtering audit events. (optional)
    count = 100 # int | The maximum number of audit event records to retrieve. (optional)
    start_index = 0 # int | The index of the first audit event record to retrieve in a paged query. (optional)

    try:
        # Get filtered audit trail data
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
**200** | List of filtered audit trail data |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**402** | Your pricing plan does not support this option |  -  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_settings**
> TenantAuditSettingsWrapper get_audit_settings()

Returns the audit trail settings.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**TenantAuditSettingsWrapper**](TenantAuditSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
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

    try:
        # Get the audit trail settings
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
**200** | Audit settings |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**402** | Your pricing plan does not support this option |  -  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_trail_mappers**
> ObjectWrapper get_audit_trail_mappers(product_type=product_type, module_type=module_type)

Returns the mappers for the audit trail types.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_type** | [**ProductType**](.md)| The type of product related to the audit trail. | [optional] 
 **module_type** | [**LocationType**](.md)| The location associated with the audit trail. | [optional] 

### Return type

[**ObjectWrapper**](ObjectWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.location_type import LocationType
from docspace_api_sdk.models.object_wrapper import ObjectWrapper
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
    product_type = docspace_api_sdk.ProductType() # ProductType | The type of product related to the audit trail. (optional)
    module_type = docspace_api_sdk.LocationType() # LocationType | The location associated with the audit trail. (optional)

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
**200** | Audit trail mappers |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_trail_report**
> DocumentBuilderTaskWrapper get_audit_trail_report()

Returns the status of generating the audit trail report.

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
        # Get the audit trail report generation status
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
**200** | Operation execution status |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**402** | Your pricing plan does not support this option |  -  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_trail_types**
> ObjectWrapper get_audit_trail_types()

Returns all the available audit trail types.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**ObjectWrapper**](ObjectWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.object_wrapper import ObjectWrapper
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
**200** | Audit trail types |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_audit_events**
> AuditEventArrayWrapper get_last_audit_events()

Returns a list of the latest changes (creation, modification, deletion, etc.) made by users to the entities on the portal.

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
        # Get audit trail data
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
**200** | List of audit trail data |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**402** | Your pricing plan does not support this option |  -  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_audit_settings**
> TenantAuditSettingsWrapper set_audit_settings(tenant_audit_settings_wrapper=tenant_audit_settings_wrapper)

Sets the audit trail settings for the current portal.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_audit_settings_wrapper** | [**TenantAuditSettingsWrapper**](TenantAuditSettingsWrapper.md)|  | [optional] 

### Return type

[**TenantAuditSettingsWrapper**](TenantAuditSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
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
        # Set the audit trail settings
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
**200** | Audit trail settings |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**400** | Exception in LoginHistoryLifeTime or AuditTrailLifeTime |  -  |
**402** | Your pricing plan does not support this option |  -  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_audit_trail_report**
> terminate_audit_trail_report()

Terminates generating the audit trail report.

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
        # Terminate the audit trail report generation
        api_instance.terminate_audit_trail_report()
    except Exception as e:
        print("Exception when calling AuditTrailDataApi->terminate_audit_trail_report: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**402** | Your pricing plan does not support this option |  -  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

