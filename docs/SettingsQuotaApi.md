# docspace_api_sdk.QuotaApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_quota_settings**](#get_user_quota_settings) | **GET** /api/2.0/settings/userquotasettings | Get the user quota settings
[**save_room_quota_settings**](#save_room_quota_settings) | **POST** /api/2.0/settings/roomquotasettings | Save the room quota settings
[**set_tenant_quota_settings**](#set_tenant_quota_settings) | **PUT** /api/2.0/settings/tenantquotasettings | Save the tenant quota settings


# **get_user_quota_settings**
> TenantUserQuotaSettingsWrapper get_user_quota_settings()

Returns the user quota settings.

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
**200** | Ok |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_room_quota_settings**
> TenantRoomQuotaSettingsWrapper save_room_quota_settings(quota_settings_requests_dto=quota_settings_requests_dto)

Saves the room quota settings specified in the request to the current portal.

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
**200** | Tenant room quota settings |  -  |
**401** | Unauthorized |  -  |
**402** | Your pricing plan does not support this option |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_tenant_quota_settings**
> TenantQuotaSettingsWrapper set_tenant_quota_settings(tenant_quota_settings_requests_dto=tenant_quota_settings_requests_dto)

Saves the tenant quota settings specified in the request to the current portal.

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
**200** | Tenant quota settings |  -  |
**401** | Unauthorized |  -  |
**402** | Your pricing plan does not support this option |  -  |
**405** | Not available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

