# docspace_api_sdk.SMTPSettingsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_smtp_operation_status**](#get_smtp_operation_status) | **GET** /api/2.0/smtpsettings/smtp/test/status | Get SMTP test status
[**get_smtp_settings**](#get_smtp_settings) | **GET** /api/2.0/smtpsettings/smtp | Get SMTP settings
[**reset_smtp_settings**](#reset_smtp_settings) | **DELETE** /api/2.0/smtpsettings/smtp | Reset SMTP settings
[**save_smtp_settings**](#save_smtp_settings) | **POST** /api/2.0/smtpsettings/smtp | Save SMTP settings
[**test_smtp_settings**](#test_smtp_settings) | **GET** /api/2.0/smtpsettings/smtp/test | Test SMTP settings


# **get_smtp_operation_status**
> SmtpOperationStatusRequestsWrapper get_smtp_operation_status()

Returns the state of the test message that `GET api/2.0/smtpsettings/smtp/test` queued for this portal, and is
the operation to poll while that test runs. A test has to be queued first; the caller needs the
portal-settings right of a DocSpace administrator, and the SMTP settings section has to be enabled for the
portal, otherwise the call is answered with 402. The call changes no settings, but it is not free of
consequence: the first answer that reports `completed` true also discards the finished job, so a later call no
longer knows about it - take `error` from that answer and keep it. An empty answer means the portal has no
test on record, either because none was queued or because its result has already been read. While the job
runs, `percents` climbs to 100 and `status` names the step reached, such as `Connect to host` or
`Send test message`; `error` is empty until something fails and stays empty when the relay accepted the
message. `id` identifies the queued job, of which a portal only ever has one.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**SmtpOperationStatusRequestsWrapper**](SmtpOperationStatusRequestsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.smtp_operation_status_requests_wrapper import SmtpOperationStatusRequestsWrapper
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
    api_instance = docspace_api_sdk.SMTPSettingsApi(api_client)

    try:
        # Get SMTP test status
        api_response = api_instance.get_smtp_operation_status()
        print("The response of SMTPSettingsApi->get_smtp_operation_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMTPSettingsApi->get_smtp_operation_status: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The state of the test message of the portal, or an empty answer when no test is on record |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**402** | The SMTP settings section is not enabled for this portal |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smtp_settings**
> SmtpSettingsWrapper get_smtp_settings()

Returns the SMTP relay this portal sends its own mail through - host, port, sender identity and authentication
flags - as it is stored for the portal. Nothing has to be called first; the caller needs the portal-settings
right of a DocSpace administrator, and the SMTP settings section has to be enabled for the portal, otherwise
the call is answered with 402. The call is read-only and safe to repeat. `isDefaultSettings` is true when the
portal has no settings of its own and runs on the mail configuration of the installation: a standalone
installation then shows those server-wide values, while a cloud portal is answered with an empty settings
object instead, so an empty `host` together with `isDefaultSettings` true means nothing was ever saved here.
`credentialsUserPassword` always comes back empty - the stored password cannot be read back, and a client that
saves the settings again has to ask the user for it once more. `port` is the port that was saved, and settings
saved without one are stored with `25`. To find out whether the returned relay actually accepts mail, queue a
test with `GET api/2.0/smtpsettings/smtp/test`.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**SmtpSettingsWrapper**](SmtpSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.smtp_settings_wrapper import SmtpSettingsWrapper
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
    api_instance = docspace_api_sdk.SMTPSettingsApi(api_client)

    try:
        # Get SMTP settings
        api_response = api_instance.get_smtp_settings()
        print("The response of SMTPSettingsApi->get_smtp_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMTPSettingsApi->get_smtp_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SMTP settings stored for the portal, with an empty password and `isDefaultSettings` telling whether the configuration of the installation is in use |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**402** | The SMTP settings section is not enabled for this portal |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_smtp_settings**
> SmtpSettingsWrapper reset_smtp_settings()

Deletes the SMTP settings of this portal and puts it back on the mail configuration of the installation, so
the portal stops using the relay saved by `POST api/2.0/smtpsettings/smtp`. Nothing has to be called first;
the caller needs the portal-settings right of a DocSpace administrator, and the SMTP settings section has to
be enabled for the portal, otherwise the call is answered with 402. The call is destructive and cannot be
undone - the host, the sender identity and the credentials are gone and have to be entered again - but it is
idempotent, and on a portal that has no settings of its own it changes nothing. Portal mail itself keeps
working as long as the installation has a relay of its own configured. The answer holds the settings that are
in force after the reset, always with `isDefaultSettings` true: the server-wide values in a standalone
installation, an empty settings object in a cloud portal, and an empty `credentialsUserPassword` in both. Read
them back at any time with `GET api/2.0/smtpsettings/smtp`.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**SmtpSettingsWrapper**](SmtpSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.smtp_settings_wrapper import SmtpSettingsWrapper
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
    api_instance = docspace_api_sdk.SMTPSettingsApi(api_client)

    try:
        # Reset SMTP settings
        api_response = api_instance.reset_smtp_settings()
        print("The response of SMTPSettingsApi->reset_smtp_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMTPSettingsApi->reset_smtp_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The settings in force after the reset - the configuration of the installation, or an empty settings object in a cloud portal |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**402** | The SMTP settings section is not enabled for this portal |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_smtp_settings**
> SmtpSettingsWrapper save_smtp_settings(smtp_settings_dto=smtp_settings_dto)

Stores the SMTP relay that this portal will hand all of its own mail to, replacing whatever was saved before
and taking the portal off the mail configuration of the installation. Nothing has to be called first; the
caller needs the portal-settings right of a DocSpace administrator, and the SMTP settings section has to be
enabled for the portal, otherwise the call is answered with 402. The call is mutating and idempotent - the
same body saved twice leaves the same settings - and it applies to the next message the portal sends. The
settings are stored unverified, no connection to `host` is attempted, so queue
`GET api/2.0/smtpsettings/smtp/test` afterwards to find out whether they work. `host` and `senderAddress` must
not be empty, `senderDisplayName` has to be present, and `enableAuth` true also requires `credentialsUserName`
and `credentialsUserPassword`; a request that misses any of them is rejected and nothing is saved. `port`
falls back to `25` when it is omitted, and `useNtlm` is accepted but not stored, so the saved settings always
authenticate with a plain user name and password. The answer repeats the stored settings with the password
emptied. Use `DELETE api/2.0/smtpsettings/smtp` to return to the configuration of the installation.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smtp_settings_dto** | [**SmtpSettingsDto**](SmtpSettingsDto.md)|  | [optional] 

### Return type

[**SmtpSettingsWrapper**](SmtpSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.smtp_settings_dto import SmtpSettingsDto
from docspace_api_sdk.models.smtp_settings_wrapper import SmtpSettingsWrapper
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
    api_instance = docspace_api_sdk.SMTPSettingsApi(api_client)
    smtp_settings_dto = docspace_api_sdk.SmtpSettingsDto() # SmtpSettingsDto |  (optional)

    try:
        # Save SMTP settings
        api_response = api_instance.save_smtp_settings(smtp_settings_dto=smtp_settings_dto)
        print("The response of SMTPSettingsApi->save_smtp_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMTPSettingsApi->save_smtp_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SMTP settings now stored for the portal, with an empty password |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**402** | The SMTP settings section is not enabled for this portal |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_smtp_settings**
> SmtpOperationStatusRequestsWrapper test_smtp_settings()

Queues a background job that sends a test message through the SMTP settings currently stored for the portal to
the email address of the calling user, and returns the state of that job. Save the settings with
`POST api/2.0/smtpsettings/smtp` first: the job always takes the stored settings and nothing can be passed to
it here. The caller needs the portal-settings right of a DocSpace administrator, and the SMTP settings section
has to be enabled for the portal, otherwise the call is answered with 402. The call is mutating, it sends
mail, and it is rate-limited to five requests per fifteen minutes per user and path by default, answering 429
above that; while a test is still running the same job is returned instead of a second one being started. The
message has not been sent when the answer arrives: poll `GET api/2.0/smtpsettings/smtp/test/status` until
`completed` is true, then read `error` - empty means the relay accepted the message, otherwise it carries the
reason. `percents` climbs to 100 and `status` names the step reached, such as `Connect to host` or
`Send test message`. An unreachable relay is reported in `error` after a 30-second connection timeout, not as
a failed request.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**SmtpOperationStatusRequestsWrapper**](SmtpOperationStatusRequestsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.smtp_operation_status_requests_wrapper import SmtpOperationStatusRequestsWrapper
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
    api_instance = docspace_api_sdk.SMTPSettingsApi(api_client)

    try:
        # Test SMTP settings
        api_response = api_instance.test_smtp_settings()
        print("The response of SMTPSettingsApi->test_smtp_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMTPSettingsApi->test_smtp_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The state of the queued test message, to be polled until `completed` is true |  * X-RateLimit-Limit - Rate limit: 5 requests per 15 minutes per user/IP. <br>  * X-RateLimit-Remaining - Requests remaining in the current 15-minute window. <br>  * X-RateLimit-Reset -  <br>  |
**402** | The SMTP settings section is not enabled for this portal |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying (5 req / 15 min limit per user/IP). <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

