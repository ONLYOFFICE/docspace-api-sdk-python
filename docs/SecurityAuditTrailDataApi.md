# docspace.SecurityAuditTrailDataApi

All URIs are relative to *http://http:*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_audit_trail_report**](SecurityAuditTrailDataApi.md#create_audit_trail_report) | **POST** /api/2.0/security/audit/events/report | Generate the audit trail report
[**get_audit_events_by_filter**](SecurityAuditTrailDataApi.md#get_audit_events_by_filter) | **GET** /api/2.0/security/audit/events/filter | Get filtered audit trail data
[**get_audit_settings**](SecurityAuditTrailDataApi.md#get_audit_settings) | **GET** /api/2.0/security/audit/settings/lifetime | Get the audit trail settings
[**get_audit_trail_mappers**](SecurityAuditTrailDataApi.md#get_audit_trail_mappers) | **GET** /api/2.0/security/audit/mappers | Get audit trail mappers
[**get_audit_trail_types**](SecurityAuditTrailDataApi.md#get_audit_trail_types) | **GET** /api/2.0/security/audit/types | Get audit trail types
[**get_last_audit_events**](SecurityAuditTrailDataApi.md#get_last_audit_events) | **GET** /api/2.0/security/audit/events/last | Get audit trail data
[**set_audit_settings**](SecurityAuditTrailDataApi.md#set_audit_settings) | **POST** /api/2.0/security/audit/settings/lifetime | Set the audit trail settings


# **create_audit_trail_report**
> StringWrapper create_audit_trail_report()

Generate the audit trail report

Generates the audit trail report.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.string_wrapper import StringWrapper
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
    api_instance = docspace.SecurityAuditTrailDataApi(api_client)

    try:
        # Generate the audit trail report
        api_response = api_instance.create_audit_trail_report()
        print("The response of SecurityAuditTrailDataApi->create_audit_trail_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityAuditTrailDataApi->create_audit_trail_report: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | URL to the xlsx report file |  -  |
**401** | Unauthorized |  -  |
**402** | Your pricing plan does not support this option |  -  |
**403** | You don&#39;t have enough permission to create |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_events_by_filter**
> AuditEventArrayWrapper get_audit_events_by_filter(user_id=user_id, product_type=product_type, module_type=module_type, action_type=action_type, action=action, entry_type=entry_type, target=target, var_from=var_from, to=to, count=count, start_index=start_index)

Get filtered audit trail data

Returns a list of the audit events by the parameters specified in the request.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.action_type import ActionType
from docspace.models.api_date_time import ApiDateTime
from docspace.models.audit_event_array_wrapper import AuditEventArrayWrapper
from docspace.models.entry_type import EntryType
from docspace.models.message_action import MessageAction
from docspace.models.module_type import ModuleType
from docspace.models.product_type import ProductType
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
    api_instance = docspace.SecurityAuditTrailDataApi(api_client)
    user_id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28' # str | The ID of the user who triggered the audit event. (optional)
    product_type = docspace.ProductType() # ProductType | The type of product related to the audit event. (optional)
    module_type = docspace.ModuleType() # ModuleType | The module within the product where the audit event occurred. (optional)
    action_type = docspace.ActionType() # ActionType | The type of action performed in the audit event (e.g., Create, Update, Delete). (optional)
    action = docspace.MessageAction() # MessageAction | The specific action that occurred within the audit event. (optional)
    entry_type = docspace.EntryType() # EntryType | The type of audit entry (e.g., Folder, User, File). (optional)
    target = 'some text' # str | The target object affected by the audit event (e.g., document ID, user account). (optional)
    var_from = docspace.ApiDateTime() # ApiDateTime | The starting date and time for filtering audit events. (optional)
    to = docspace.ApiDateTime() # ApiDateTime | The ending date and time for filtering audit events. (optional)
    count = 1234 # int | The maximum number of audit event records to retrieve. (optional)
    start_index = 1234 # int | The index of the first audit event record to retrieve in a paged query. (optional)

    try:
        # Get filtered audit trail data
        api_response = api_instance.get_audit_events_by_filter(user_id=user_id, product_type=product_type, module_type=module_type, action_type=action_type, action=action, entry_type=entry_type, target=target, var_from=var_from, to=to, count=count, start_index=start_index)
        print("The response of SecurityAuditTrailDataApi->get_audit_events_by_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityAuditTrailDataApi->get_audit_events_by_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user who triggered the audit event. | [optional] 
 **product_type** | [**ProductType**](.md)| The type of product related to the audit event. | [optional] 
 **module_type** | [**ModuleType**](.md)| The module within the product where the audit event occurred. | [optional] 
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

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of filtered audit trail data |  -  |
**401** | Unauthorized |  -  |
**402** | Your pricing plan does not support this option |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_settings**
> TenantAuditSettingsWrapper get_audit_settings()

Get the audit trail settings

Returns the audit trail settings.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.tenant_audit_settings_wrapper import TenantAuditSettingsWrapper
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
    api_instance = docspace.SecurityAuditTrailDataApi(api_client)

    try:
        # Get the audit trail settings
        api_response = api_instance.get_audit_settings()
        print("The response of SecurityAuditTrailDataApi->get_audit_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityAuditTrailDataApi->get_audit_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TenantAuditSettingsWrapper**](TenantAuditSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audit settings |  -  |
**401** | Unauthorized |  -  |
**402** | Your pricing plan does not support this option |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_trail_mappers**
> ObjectWrapper get_audit_trail_mappers(product_type=product_type, module_type=module_type)

Get audit trail mappers

Returns the mappers for the audit trail types.

### Example


```python
import docspace
from docspace.models.module_type import ModuleType
from docspace.models.object_wrapper import ObjectWrapper
from docspace.models.product_type import ProductType
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://http:
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://http:"
)


# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.SecurityAuditTrailDataApi(api_client)
    product_type = docspace.ProductType() # ProductType | The type of product related to the audit trail. (optional)
    module_type = docspace.ModuleType() # ModuleType | The module within the product associated with the audit trail. (optional)

    try:
        # Get audit trail mappers
        api_response = api_instance.get_audit_trail_mappers(product_type=product_type, module_type=module_type)
        print("The response of SecurityAuditTrailDataApi->get_audit_trail_mappers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityAuditTrailDataApi->get_audit_trail_mappers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_type** | [**ProductType**](.md)| The type of product related to the audit trail. | [optional] 
 **module_type** | [**ModuleType**](.md)| The module within the product associated with the audit trail. | [optional] 

### Return type

[**ObjectWrapper**](ObjectWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audit trail mappers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_trail_types**
> ObjectWrapper get_audit_trail_types()

Get audit trail types

Returns all the available audit trail types.

### Example


```python
import docspace
from docspace.models.object_wrapper import ObjectWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://http:
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://http:"
)


# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.SecurityAuditTrailDataApi(api_client)

    try:
        # Get audit trail types
        api_response = api_instance.get_audit_trail_types()
        print("The response of SecurityAuditTrailDataApi->get_audit_trail_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityAuditTrailDataApi->get_audit_trail_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ObjectWrapper**](ObjectWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audit trail types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_audit_events**
> AuditEventArrayWrapper get_last_audit_events()

Get audit trail data

Returns a list of the latest changes (creation, modification, deletion, etc.) made by users to the entities on the portal.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.audit_event_array_wrapper import AuditEventArrayWrapper
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
    api_instance = docspace.SecurityAuditTrailDataApi(api_client)

    try:
        # Get audit trail data
        api_response = api_instance.get_last_audit_events()
        print("The response of SecurityAuditTrailDataApi->get_last_audit_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityAuditTrailDataApi->get_last_audit_events: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuditEventArrayWrapper**](AuditEventArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of audit trail data |  -  |
**401** | Unauthorized |  -  |
**402** | Your pricing plan does not support this option |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_audit_settings**
> TenantAuditSettingsWrapper set_audit_settings(tenant_audit_settings_wrapper=tenant_audit_settings_wrapper)

Set the audit trail settings

Sets the audit trail settings for the current portal.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.tenant_audit_settings_wrapper import TenantAuditSettingsWrapper
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
    api_instance = docspace.SecurityAuditTrailDataApi(api_client)
    tenant_audit_settings_wrapper = docspace.TenantAuditSettingsWrapper() # TenantAuditSettingsWrapper |  (optional)

    try:
        # Set the audit trail settings
        api_response = api_instance.set_audit_settings(tenant_audit_settings_wrapper=tenant_audit_settings_wrapper)
        print("The response of SecurityAuditTrailDataApi->set_audit_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityAuditTrailDataApi->set_audit_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_audit_settings_wrapper** | [**TenantAuditSettingsWrapper**](TenantAuditSettingsWrapper.md)|  | [optional] 

### Return type

[**TenantAuditSettingsWrapper**](TenantAuditSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audit trail settings |  -  |
**400** | Exception in LoginHistoryLifeTime or AuditTrailLifeTime |  -  |
**401** | Unauthorized |  -  |
**402** | Your pricing plan does not support this option |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

