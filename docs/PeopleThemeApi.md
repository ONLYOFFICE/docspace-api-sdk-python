# docspace_api_sdk.ThemeApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_portal_theme**](#change_portal_theme) | **PUT** /api/2.0/people/theme | Change the portal theme
[**get_portal_theme**](#get_portal_theme) | **GET** /api/2.0/people/theme | Get the portal theme


# **change_portal_theme**
> DarkThemeSettingsWrapper change_portal_theme(dark_theme_settings_request_dto=dark_theme_settings_request_dto)

Changes the current portal theme.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dark_theme_settings_request_dto** | [**DarkThemeSettingsRequestDto**](DarkThemeSettingsRequestDto.md)|  | [optional] 

### Return type

[**DarkThemeSettingsWrapper**](DarkThemeSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.dark_theme_settings_request_dto import DarkThemeSettingsRequestDto
from docspace_api_sdk.models.dark_theme_settings_wrapper import DarkThemeSettingsWrapper
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
    api_instance = docspace_api_sdk.ThemeApi(api_client)
    dark_theme_settings_request_dto = docspace_api_sdk.DarkThemeSettingsRequestDto() # DarkThemeSettingsRequestDto |  (optional)

    try:
        # Change the portal theme
        api_response = api_instance.change_portal_theme(dark_theme_settings_request_dto=dark_theme_settings_request_dto)
        print("The response of ThemeApi->change_portal_theme:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThemeApi->change_portal_theme: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Theme |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portal_theme**
> DarkThemeSettingsWrapper get_portal_theme()

Returns a theme which is set to the current portal.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**DarkThemeSettingsWrapper**](DarkThemeSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.dark_theme_settings_wrapper import DarkThemeSettingsWrapper
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
    api_instance = docspace_api_sdk.ThemeApi(api_client)

    try:
        # Get the portal theme
        api_response = api_instance.get_portal_theme()
        print("The response of ThemeApi->get_portal_theme:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThemeApi->get_portal_theme: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Theme |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

