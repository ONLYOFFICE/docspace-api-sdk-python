# docspace_api_sdk.BannersVisibilityApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**set_tenant_banner_settings**](#set_tenant_banner_settings) | **POST** /api/2.0/settings/banner | Set the promotional banners visibility settings


# **set_tenant_banner_settings**
> TenantBannerSettingsWrapper set_tenant_banner_settings(tenant_banner_settings_dto=tenant_banner_settings_dto)

Sets the promotional banners visibility settings settings for the portal.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_banner_settings_dto** | [**TenantBannerSettingsDto**](TenantBannerSettingsDto.md)|  | [optional] 

### Return type

[**TenantBannerSettingsWrapper**](TenantBannerSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.tenant_banner_settings_dto import TenantBannerSettingsDto
from docspace_api_sdk.models.tenant_banner_settings_wrapper import TenantBannerSettingsWrapper
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
    api_instance = docspace_api_sdk.BannersVisibilityApi(api_client)
    tenant_banner_settings_dto = docspace_api_sdk.TenantBannerSettingsDto() # TenantBannerSettingsDto |  (optional)

    try:
        # Set the promotional banners visibility settings
        api_response = api_instance.set_tenant_banner_settings(tenant_banner_settings_dto=tenant_banner_settings_dto)
        print("The response of BannersVisibilityApi->set_tenant_banner_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BannersVisibilityApi->set_tenant_banner_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Promotional banners visibility settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

