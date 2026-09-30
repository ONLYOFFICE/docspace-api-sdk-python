# docspace_api_sdk.LoginSettingsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_login_settings**](#get_login_settings) | **GET** /api/2.0/settings/security/loginsettings | Get login settings
[**set_default_login_settings**](#set_default_login_settings) | **DELETE** /api/2.0/settings/security/loginsettings | Reset login settings
[**update_login_settings**](#update_login_settings) | **PUT** /api/2.0/settings/security/loginsettings | Update login settings


# **get_login_settings**
> LoginSettingsWrapper get_login_settings()

Returns the brute-force protection of the sign-in form for the current portal: how many failed attempts are
tolerated, how long the window they are counted in lasts, and how long an offender stays blocked. The caller
needs the portal-settings right of a DocSpace administrator; members without it are refused, and anonymous
callers are not admitted. The operation is read-only and honours `If-Modified-Since`: send back the
`Last-Modified` value of an earlier answer and unchanged settings come back as an empty not-modified response
rather than a body. `checkPeriod` and `blockTime` are counted in seconds. A portal nobody has configured
tolerates 5 failed attempts inside a window of 60 seconds and blocks for 60 seconds, and reports `isDefault`
true; the flag turns false as soon as any of the three values differs from that. The answer describes the
portal-wide policy only: it does not say which accounts or addresses are blocked at the moment, while a
lockout that has already happened is recorded in the login history and can be read with
`GET api/2.0/security/audit/login/filter`. Change the numbers with
`PUT api/2.0/settings/security/loginsettings`, or put them back with
`DELETE api/2.0/settings/security/loginsettings`.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**LoginSettingsWrapper**](LoginSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.login_settings_wrapper import LoginSettingsWrapper
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
    api_instance = docspace_api_sdk.LoginSettingsApi(api_client)

    try:
        # Get login settings
        api_response = api_instance.get_login_settings()
        print("The response of LoginSettingsApi->get_login_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginSettingsApi->get_login_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The brute-force protection settings of the portal: the tolerated attempts, the counting window and the block in seconds, and whether they match the shipped defaults |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_default_login_settings**
> LoginSettingsWrapper set_default_login_settings()

Puts the brute-force protection of the sign-in form back to what the portal shipped with: 5 tolerated failed
attempts, a counting window of 60 seconds and a block of 60 seconds. The caller needs the portal-settings
right of a DocSpace administrator, otherwise the call is refused. The operation takes no parameters and
overwrites whatever was configured before without asking, so read the current numbers with
`GET api/2.0/settings/security/loginsettings` first if they are worth keeping. Only the setting is reset:
sign-ins already blocked stay blocked until the block they were given runs out, and the attempt counters
running for other users are left alone. The reset is portal-wide, applies to attempts made from now on, is
recorded in the audit trail, and calling it twice changes nothing further. The restored numbers also decide
when the sign-in form starts asking for a captcha, which it does one attempt before the block. The answer is
the restored settings, with `isDefault` true. Store numbers of your own with
`PUT api/2.0/settings/security/loginsettings`.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**LoginSettingsWrapper**](LoginSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.login_settings_wrapper import LoginSettingsWrapper
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
    api_instance = docspace_api_sdk.LoginSettingsApi(api_client)

    try:
        # Reset login settings
        api_response = api_instance.set_default_login_settings()
        print("The response of LoginSettingsApi->set_default_login_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginSettingsApi->set_default_login_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The brute-force protection settings restored to the shipped defaults |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_login_settings**
> LoginSettingsWrapper update_login_settings(login_settings_request_dto=login_settings_request_dto)

Replaces the brute-force protection of the sign-in form for the whole portal: `attemptCount` failed attempts
inside a rolling window of `checkPeriod` seconds, after which the offender is blocked for `blockTime` seconds.
All three values are replaced together and each has to be between 1 and 9999, so read the current ones with
`GET api/2.0/settings/security/loginsettings` before changing only one of them; a value outside the range is
rejected as an invalid request. The caller needs the portal-settings right of a DocSpace administrator,
otherwise the call is refused. Failed attempts are counted per user name and client address, so one member's
lockout leaves the rest of the portal signing in normally, and a blocked pair is refused even once the
password is finally correct. The new numbers apply to attempts made from now on and leave counters and blocks
already running as they are. The change is recorded in the audit trail, and the answer is the stored settings
with the flag that says whether they still match the shipped defaults.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_settings_request_dto** | [**LoginSettingsRequestDto**](LoginSettingsRequestDto.md)|  | [optional] 

### Return type

[**LoginSettingsWrapper**](LoginSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.login_settings_request_dto import LoginSettingsRequestDto
from docspace_api_sdk.models.login_settings_wrapper import LoginSettingsWrapper
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
    api_instance = docspace_api_sdk.LoginSettingsApi(api_client)
    login_settings_request_dto = docspace_api_sdk.LoginSettingsRequestDto() # LoginSettingsRequestDto |  (optional)

    try:
        # Update login settings
        api_response = api_instance.update_login_settings(login_settings_request_dto=login_settings_request_dto)
        print("The response of LoginSettingsApi->update_login_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginSettingsApi->update_login_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The brute-force protection settings as they were stored, with the flag that says whether they match the shipped defaults |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

