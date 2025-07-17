# docspace-api-python.SecurityBannersVisibilityApi

All URIs are relative to *http://localhost:8092*

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
import docspace-api-python
from docspace-api-python.models.tenant_banner_settings_dto import TenantBannerSettingsDto
from docspace-api-python.models.tenant_banner_settings_wrapper import TenantBannerSettingsWrapper
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
    api_instance = docspace-api-python.SecurityBannersVisibilityApi(api_client)
    tenant_banner_settings_dto = docspace-api-python.TenantBannerSettingsDto() # TenantBannerSettingsDto |  (optional)

    try:
        # Set the promotional banners visibility settings
        api_response = api_instance.set_tenant_banner_settings(tenant_banner_settings_dto=tenant_banner_settings_dto)
        print("The response of SecurityBannersVisibilityApi->set_tenant_banner_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityBannersVisibilityApi->set_tenant_banner_settings: %s\n" % e)
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

