# docspace_api_sdk.AccessToDevToolsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**set_tenant_dev_tools_access_settings**](#set_tenant_dev_tools_access_settings) | **POST** /api/2.0/settings/devtoolsaccess | Set the Developer Tools access settings


# **set_tenant_dev_tools_access_settings**
> TenantDevToolsAccessSettingsWrapper set_tenant_dev_tools_access_settings(tenant_dev_tools_access_settings_dto=tenant_dev_tools_access_settings_dto)

Sets the Developer Tools access settings for the portal.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_dev_tools_access_settings_dto** | [**TenantDevToolsAccessSettingsDto**](TenantDevToolsAccessSettingsDto.md)|  | [optional] 

### Return type

[**TenantDevToolsAccessSettingsWrapper**](TenantDevToolsAccessSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.tenant_dev_tools_access_settings_dto import TenantDevToolsAccessSettingsDto
from docspace_api_sdk.models.tenant_dev_tools_access_settings_wrapper import TenantDevToolsAccessSettingsWrapper
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
    api_instance = docspace_api_sdk.AccessToDevToolsApi(api_client)
    tenant_dev_tools_access_settings_dto = docspace_api_sdk.TenantDevToolsAccessSettingsDto() # TenantDevToolsAccessSettingsDto |  (optional)

    try:
        # Set the Developer Tools access settings
        api_response = api_instance.set_tenant_dev_tools_access_settings(tenant_dev_tools_access_settings_dto=tenant_dev_tools_access_settings_dto)
        print("The response of AccessToDevToolsApi->set_tenant_dev_tools_access_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessToDevToolsApi->set_tenant_dev_tools_access_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Developer Tools access settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

