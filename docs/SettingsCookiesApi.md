# docspace_api_sdk.CookiesApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cookie_settings**](#get_cookie_settings) | **GET** /api/2.0/settings/cookiesettings | Get the cookie lifetime settings
[**update_cookie_settings**](#update_cookie_settings) | **PUT** /api/2.0/settings/cookiesettings | Update the cookie lifetime settings


# **get_cookie_settings**
> CookieSettingsWrapper get_cookie_settings()

Returns how long an authentication session of this portal stays valid: `lifeTime` in minutes together with the
`enabled` flag that says whether that limit is applied at all. The caller needs the portal-settings right of a
DocSpace administrator - the portal owner and a DocSpace administrator qualify, any other member is refused -
and the call is read-only. The pair describes the whole portal rather than the calling user, and it is never
empty: a portal nobody has configured answers `lifeTime` 1440, one day, with `enabled` false. Read the two
fields together, because the number alone does not say how long a session lasts - while `enabled` is false the
stored number is ignored and an issued session is honoured for a year, and `lifeTime` 0 with `enabled` true
means a session that never expires on its own. On an installation whose configuration hides the cookie section
the built-in default pair comes back instead of the stored one. `GET api/2.0/settings` carries the same flag
as `cookieSettingsEnabled` without the number; change the pair with `PUT api/2.0/settings/cookiesettings`.

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
        # Get the cookie lifetime settings
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
**200** | The authentication session lifetime of the portal in minutes together with the flag that says whether that limit is applied |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cookie_settings**
> StringWrapper update_cookie_settings(cookie_settings_requests_dto=cookie_settings_requests_dto)

Stores how long an authentication session of this portal stays valid: `lifeTime` in minutes together with the
`enabled` flag that switches the limit on. The caller needs the portal-settings right of a DocSpace
administrator - the portal owner and a DocSpace administrator qualify, any other member is refused - and on an
installation whose configuration hides the cookie section nothing is stored and the call is answered with 402.
A `lifeTime` above 9999 minutes is not rejected but clamped to 9999, while 0 or less clears the number
instead, which with `enabled` true leaves sessions that never expire on their own. Any positive `lifeTime`
raises the session version of the portal: every session issued before the call stops being accepted, and with
`enabled` true the connections behind them are dropped as well. The caller is signed in again inside the same
call and gets a fresh session cookie in the response, so a client that keeps sending the token it held before
this call is the one locked out. The change is recorded in the audit trail. What comes back is a localized
confirmation message; read the stored pair with `GET api/2.0/settings/cookiesettings`.

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
        # Update the cookie lifetime settings
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
**200** | A localized message confirming that the session lifetime has been saved |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**402** | The installation hides the cookie lifetime section, or the portal's payment has lapsed |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

