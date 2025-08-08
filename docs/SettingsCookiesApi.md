# docspace_api_sdk.CookiesApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cookie_settings**](#get_cookie_settings) | **GET** /api/2.0/settings/cookiesettings | Get cookies lifetime
[**update_cookie_settings**](#update_cookie_settings) | **PUT** /api/2.0/settings/cookiesettings | Update cookies lifetime


# **get_cookie_settings**
> CookieSettingsWrapper get_cookie_settings()

Returns the cookies lifetime value in minutes.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**CookieSettingsWrapper**](CookieSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.cookie_settings_wrapper import CookieSettingsWrapper
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
    api_instance = docspace_api_sdk.CookiesApi(api_client)

    try:
        # Get cookies lifetime
        api_response = api_instance.get_cookie_settings()
        print("The response of CookiesApi->get_cookie_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CookiesApi->get_cookie_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lifetime value in minutes |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cookie_settings**
> StringWrapper update_cookie_settings(cookie_settings_requests_dto=cookie_settings_requests_dto)

Updates the cookies lifetime value in minutes.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cookie_settings_requests_dto** | [**CookieSettingsRequestsDto**](CookieSettingsRequestsDto.md)|  | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.cookie_settings_requests_dto import CookieSettingsRequestsDto
from docspace_api_sdk.models.string_wrapper import StringWrapper
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
    api_instance = docspace_api_sdk.CookiesApi(api_client)
    cookie_settings_requests_dto = docspace_api_sdk.CookieSettingsRequestsDto() # CookieSettingsRequestsDto |  (optional)

    try:
        # Update cookies lifetime
        api_response = api_instance.update_cookie_settings(cookie_settings_requests_dto=cookie_settings_requests_dto)
        print("The response of CookiesApi->update_cookie_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CookiesApi->update_cookie_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message about the result of saving new settings |  -  |
**401** | Unauthorized |  -  |
**402** | Your pricing plan does not support this option |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

