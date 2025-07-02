# docspace-api-python.SettingsQuotaApi

All URIs are relative to *http://localhost:8092*

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
import docspace-api-python
from docspace-api-python.models.tenant_user_quota_settings_wrapper import TenantUserQuotaSettingsWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
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
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.SettingsQuotaApi(api_client)

    try:
        # Get the user quota settings
        api_response = api_instance.get_user_quota_settings()
        print("The response of SettingsQuotaApi->get_user_quota_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsQuotaApi->get_user_quota_settings: %s\n" % e)
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
import docspace-api-python
from docspace-api-python.models.quota_settings_requests_dto import QuotaSettingsRequestsDto
from docspace-api-python.models.tenant_room_quota_settings_wrapper import TenantRoomQuotaSettingsWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
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
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.SettingsQuotaApi(api_client)
    quota_settings_requests_dto = docspace-api-python.QuotaSettingsRequestsDto() # QuotaSettingsRequestsDto |  (optional)

    try:
        # Save the room quota settings
        api_response = api_instance.save_room_quota_settings(quota_settings_requests_dto=quota_settings_requests_dto)
        print("The response of SettingsQuotaApi->save_room_quota_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsQuotaApi->save_room_quota_settings: %s\n" % e)
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
import docspace-api-python
from docspace-api-python.models.tenant_quota_settings_requests_dto import TenantQuotaSettingsRequestsDto
from docspace-api-python.models.tenant_quota_settings_wrapper import TenantQuotaSettingsWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
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
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.SettingsQuotaApi(api_client)
    tenant_quota_settings_requests_dto = docspace-api-python.TenantQuotaSettingsRequestsDto() # TenantQuotaSettingsRequestsDto |  (optional)

    try:
        # Save the tenant quota settings
        api_response = api_instance.set_tenant_quota_settings(tenant_quota_settings_requests_dto=tenant_quota_settings_requests_dto)
        print("The response of SettingsQuotaApi->set_tenant_quota_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsQuotaApi->set_tenant_quota_settings: %s\n" % e)
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

