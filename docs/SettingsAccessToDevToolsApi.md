# docspace_api_sdk.AccessToDevToolsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tenant_access_dev_tools_settings**](#get_tenant_access_dev_tools_settings) | **GET** /api/2.0/settings/devtoolsaccess | Get the Developer Tools access settings


# **get_tenant_access_dev_tools_settings**
> TenantDevToolsAccessSettingsWrapper get_tenant_access_dev_tools_settings()

Returns the Developer Tools access settings for the portal.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**TenantDevToolsAccessSettingsWrapper**](TenantDevToolsAccessSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
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

    try:
        # Get the Developer Tools access settings
        api_response = api_instance.get_tenant_access_dev_tools_settings()
        print("The response of AccessToDevToolsApi->get_tenant_access_dev_tools_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessToDevToolsApi->get_tenant_access_dev_tools_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Developer Tools access settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

