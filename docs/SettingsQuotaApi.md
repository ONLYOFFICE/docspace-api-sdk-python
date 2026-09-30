# docspace_api_sdk.QuotaApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_quota_settings**](#get_user_quota_settings) | **GET** /api/2.0/settings/userquotasettings | Get the user quota settings
[**save_ai_agent_quota_settings**](#save_ai_agent_quota_settings) | **POST** /api/2.0/settings/aiagentquotasettings | Save the AI Agent quota settings
[**save_room_quota_settings**](#save_room_quota_settings) | **POST** /api/2.0/settings/roomquotasettings | Save the room quota settings
[**set_tenant_quota_settings**](#set_tenant_quota_settings) | **PUT** /api/2.0/settings/tenantquotasettings | Save the tenant quota settings


# **get_user_quota_settings**
> TenantUserQuotaSettingsWrapper get_user_quota_settings()

Returns the portal's per-user default storage quota: whether it is enabled and, if so, its size in bytes.
Requires Owner or DocSpaceAdmin (the EditPortalSettings permission); every other authenticated role, and an
anonymous caller, is refused. This is a read-only, idempotent call. When `enableQuota` is false, the size
value is not enforced and users get unlimited personal storage regardless of what it holds. The response
supports conditional requests: send the standard If-Modified-Since header with the previous `lastModified`
value, and an unchanged response comes back empty instead of resending the settings.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**TenantUserQuotaSettingsWrapper**](TenantUserQuotaSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.tenant_user_quota_settings_wrapper import TenantUserQuotaSettingsWrapper
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
    api_instance = docspace_api_sdk.QuotaApi(api_client)

    try:
        # Get the user quota settings
        api_response = api_instance.get_user_quota_settings()
        print("The response of QuotaApi->get_user_quota_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotaApi->get_user_quota_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current per-user default storage quota settings |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_ai_agent_quota_settings**
> TenantAiAgentQuotaSettingsWrapper save_ai_agent_quota_settings(quota_settings_requests_dto=quota_settings_requests_dto)

Sets the portal's default storage quota for AI agents, applied as the starting limit for newly created agents.
Requires Owner or DocSpaceAdmin (the EditPortalSettings permission), and on a paid SaaS tenant the portal's
plan must include the statistics feature, or the call is rejected as not covered by the plan. The requested
size cannot exceed the portal's own total storage quota, nor, on a Standalone install with a portal-wide quota
enabled, that quota's size. Disable enforcement by passing `enableQuota=false`; the size is then ignored for
new agents. This is a mutating, idempotent call: sending the same body again leaves the quota unchanged. It
returns the saved settings, not any agent's current usage.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quota_settings_requests_dto** | [**QuotaSettingsRequestsDto**](QuotaSettingsRequestsDto.md)|  | [optional] 

### Return type

[**TenantAiAgentQuotaSettingsWrapper**](TenantAiAgentQuotaSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.quota_settings_requests_dto import QuotaSettingsRequestsDto
from docspace_api_sdk.models.tenant_ai_agent_quota_settings_wrapper import TenantAiAgentQuotaSettingsWrapper
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
    api_instance = docspace_api_sdk.QuotaApi(api_client)
    quota_settings_requests_dto = docspace_api_sdk.QuotaSettingsRequestsDto() # QuotaSettingsRequestsDto |  (optional)

    try:
        # Save the AI Agent quota settings
        api_response = api_instance.save_ai_agent_quota_settings(quota_settings_requests_dto=quota_settings_requests_dto)
        print("The response of QuotaApi->save_ai_agent_quota_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotaApi->save_ai_agent_quota_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Saved default AI agent storage quota settings |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**402** | The portal's pricing plan does not include the statistics feature required for AI agent quotas |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_room_quota_settings**
> TenantRoomQuotaSettingsWrapper save_room_quota_settings(quota_settings_requests_dto=quota_settings_requests_dto)

Sets the portal's default per-room storage quota, applied to newly created rooms as their starting limit.
Requires Owner or DocSpaceAdmin (the EditPortalSettings permission), and on a paid SaaS tenant the portal's
plan must include the statistics feature, or the call is rejected as not covered by the plan. The requested
size cannot exceed the portal's own total storage quota, nor, on a Standalone install with a portal-wide quota
enabled, that quota's size. Disable enforcement by passing `enableQuota=false`; the size is then ignored for
new rooms. This is a mutating, idempotent call: sending the same body again leaves the quota unchanged. It
returns the saved settings, not the individual rooms' current usage.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quota_settings_requests_dto** | [**QuotaSettingsRequestsDto**](QuotaSettingsRequestsDto.md)|  | [optional] 

### Return type

[**TenantRoomQuotaSettingsWrapper**](TenantRoomQuotaSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.quota_settings_requests_dto import QuotaSettingsRequestsDto
from docspace_api_sdk.models.tenant_room_quota_settings_wrapper import TenantRoomQuotaSettingsWrapper
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
    api_instance = docspace_api_sdk.QuotaApi(api_client)
    quota_settings_requests_dto = docspace_api_sdk.QuotaSettingsRequestsDto() # QuotaSettingsRequestsDto |  (optional)

    try:
        # Save the room quota settings
        api_response = api_instance.save_room_quota_settings(quota_settings_requests_dto=quota_settings_requests_dto)
        print("The response of QuotaApi->save_room_quota_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotaApi->save_room_quota_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Saved default per-room storage quota settings |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**402** | The portal's pricing plan does not include the statistics feature required for room quotas |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_tenant_quota_settings**
> TenantQuotaSettingsWrapper set_tenant_quota_settings(tenant_quota_settings_requests_dto=tenant_quota_settings_requests_dto)

Sets or removes the storage quota for a given tenant. Available only on a Standalone (self-hosted)
installation; on SaaS the call is always refused. Requires a DocSpace administrator, and the portal's plan
must include the statistics feature or the call is rejected as not covered by the plan. Pass a non-negative
`quota` in bytes to enable the limit for the tenant identified by `tenantId`, or a negative value to remove
any limit. This is a mutating, idempotent call: sending the same body again leaves the quota unchanged. It
returns the saved quota settings for that tenant, not its current usage.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_quota_settings_requests_dto** | [**TenantQuotaSettingsRequestsDto**](TenantQuotaSettingsRequestsDto.md)|  | [optional] 

### Return type

[**TenantQuotaSettingsWrapper**](TenantQuotaSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.tenant_quota_settings_requests_dto import TenantQuotaSettingsRequestsDto
from docspace_api_sdk.models.tenant_quota_settings_wrapper import TenantQuotaSettingsWrapper
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
    api_instance = docspace_api_sdk.QuotaApi(api_client)
    tenant_quota_settings_requests_dto = docspace_api_sdk.TenantQuotaSettingsRequestsDto() # TenantQuotaSettingsRequestsDto |  (optional)

    try:
        # Save the tenant quota settings
        api_response = api_instance.set_tenant_quota_settings(tenant_quota_settings_requests_dto=tenant_quota_settings_requests_dto)
        print("The response of QuotaApi->set_tenant_quota_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotaApi->set_tenant_quota_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Saved tenant storage quota settings |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**402** | The portal's pricing plan does not include the statistics feature required for tenant quotas |  -  |
**405** | The caller is not a DocSpace administrator, or the portal is not a Standalone installation |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

