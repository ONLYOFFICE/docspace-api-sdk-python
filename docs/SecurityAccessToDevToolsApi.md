# docspace.SecurityAccessToDevToolsApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**set_tenant_dev_tools_access_settings**](SecurityAccessToDevToolsApi.md#set_tenant_dev_tools_access_settings) | **POST** /api/2.0/settings/devtoolsaccess | Set the Developer Tools access settings


# **set_tenant_dev_tools_access_settings**
> TenantDevToolsAccessSettingsWrapper set_tenant_dev_tools_access_settings(tenant_dev_tools_access_settings_dto=tenant_dev_tools_access_settings_dto)

Set the Developer Tools access settings

Sets the Developer Tools access settings for the portal.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.tenant_dev_tools_access_settings_dto import TenantDevToolsAccessSettingsDto
from docspace.models.tenant_dev_tools_access_settings_wrapper import TenantDevToolsAccessSettingsWrapper
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
    api_instance = docspace.SecurityAccessToDevToolsApi(api_client)
    tenant_dev_tools_access_settings_dto = docspace.TenantDevToolsAccessSettingsDto() # TenantDevToolsAccessSettingsDto |  (optional)

    try:
        # Set the Developer Tools access settings
        api_response = api_instance.set_tenant_dev_tools_access_settings(tenant_dev_tools_access_settings_dto=tenant_dev_tools_access_settings_dto)
        print("The response of SecurityAccessToDevToolsApi->set_tenant_dev_tools_access_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityAccessToDevToolsApi->set_tenant_dev_tools_access_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_dev_tools_access_settings_dto** | [**TenantDevToolsAccessSettingsDto**](TenantDevToolsAccessSettingsDto.md)|  | [optional] 

### Return type

[**TenantDevToolsAccessSettingsWrapper**](TenantDevToolsAccessSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Developer Tools access settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

