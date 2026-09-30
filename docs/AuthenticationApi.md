# docspace_api_sdk.AuthenticationApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_me**](#authenticate_me) | **POST** /api/2.0/authentication | Authenticate a user
[**authenticate_me_from_body_with_code**](#authenticate_me_from_body_with_code) | **POST** /api/2.0/authentication/{code} | Authenticate a user by code
[**check_confirm**](#check_confirm) | **POST** /api/2.0/authentication/confirm | Check a confirmation link
[**get_is_authentificated**](#get_is_authentificated) | **GET** /api/2.0/authentication | Check authentication
[**logout**](#logout) | **POST** /api/2.0/authentication/logout | Log out
[**save_mobile_phone**](#save_mobile_phone) | **POST** /api/2.0/authentication/setphone | Set a mobile phone
[**send_sms_code**](#send_sms_code) | **POST** /api/2.0/authentication/sendsms | Send SMS code


# **authenticate_me**
> AuthenticationTokenWrapper authenticate_me(auth_requests_dto=auth_requests_dto)

Signs a user in to the current portal and either issues the authentication token or reports which second
factor is still missing. Credentials go in the body as `userName` with `password` or `passwordHash`, as the
key of a confirmation link in `confirmData`, or as a third-party account (`provider` with `accessToken`, or
`serializedProfile`), which only a standalone installation or a tariff with third-party sign-in allows. Open
to unauthenticated callers, mutating and not
idempotent: it writes a login event, sets the portal cookies and counts every failure against the brute-force
limit. When a second factor is required for this user the answer carries no `token` but `sms` with the masked
phone number - or a `confirmUrl` pointing at `POST api/2.0/authentication/setphone` while no number is
activated yet - or `tfa` with the setup key while the authenticator app is not connected; submit the code to
`POST api/2.0/authentication/{code}` to finish such a sign-in. Otherwise the answer carries `token` for the
`Authorization` header and `expires`, which is omitted when `session=true` ties the token to the browser
session. An unknown user fails with 404, rejected credentials with 401, a disabled or blocked user with 403.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_requests_dto** | [**AuthRequestsDto**](AuthRequestsDto.md)|  | [optional] 

### Return type

[**AuthenticationTokenWrapper**](AuthenticationTokenWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.auth_requests_dto import AuthRequestsDto
from docspace_api_sdk.models.authentication_token_wrapper import AuthenticationTokenWrapper
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
    api_instance = docspace_api_sdk.AuthenticationApi(api_client)
    auth_requests_dto = docspace_api_sdk.AuthRequestsDto() # AuthRequestsDto |  (optional)

    try:
        # Authenticate a user
        api_response = api_instance.authenticate_me(auth_requests_dto=auth_requests_dto)
        print("The response of AuthenticationApi->authenticate_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authenticate_me: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The authentication token, or the second factor that has to be passed before a token is issued |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The request body could not be validated, for example `confirmData.email` is not an email address |  -  |
**401** | The password, the confirmation key or the third-party profile was rejected, or third-party sign-in is not allowed for this portal |  -  |
**403** | The user is disabled, or too many failed attempts and CAPTCHA failures have blocked further sign-ins for these credentials |  -  |
**404** | No user of this portal matches the credentials in the request body |  -  |
**429** | The portal rate limiter rejected the call - retry after the interval in the `Retry-After` header |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authenticate_me_from_body_with_code**
> AuthenticationTokenWrapper authenticate_me_from_body_with_code(code, auth_with_code_requests_dto=auth_with_code_requests_dto)

Finishes a two-factor sign-in: checks the one-time code and, when it matches, issues the authentication token.
Call it only after `POST api/2.0/authentication` answered with `sms` or `tfa` set, and repeat the same
credentials in the body next to `code` - the code alone does not identify the user. The code comes from the
SMS the portal sent, which `POST api/2.0/authentication/sendsms` resends, or from the authenticator app;
whichever second factor the portal has enabled for this user is the one checked here. Open to unauthenticated
callers, mutating and not idempotent: a code is single-use, the sign-in is written to the login history, and
the first code accepted from an authenticator app also connects that app to the user. The answer carries
`token` for the `Authorization` header, `expires` unless `session=true` tied the token to the browser session,
and either `sms` with the masked phone number or `tfa`. A wrong, empty or expired code fails with 401 and
counts against the brute-force limit, which then refuses further attempts with 403.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The two-factor authentication code. Send the same value as the `code` of the request body, which is the one the handler reads. | 
 **auth_with_code_requests_dto** | [**AuthWithCodeRequestsDto**](AuthWithCodeRequestsDto.md)|  | [optional] 

### Return type

[**AuthenticationTokenWrapper**](AuthenticationTokenWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.auth_with_code_requests_dto import AuthWithCodeRequestsDto
from docspace_api_sdk.models.authentication_token_wrapper import AuthenticationTokenWrapper
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
    api_instance = docspace_api_sdk.AuthenticationApi(api_client)
    code = 'code_example' # str | The two-factor authentication code. Send the same value as the `code` of the request body, which is the one the handler reads.
    auth_with_code_requests_dto = docspace_api_sdk.AuthWithCodeRequestsDto() # AuthWithCodeRequestsDto |  (optional)

    try:
        # Authenticate a user by code
        api_response = api_instance.authenticate_me_from_body_with_code(code, auth_with_code_requests_dto=auth_with_code_requests_dto)
        print("The response of AuthenticationApi->authenticate_me_from_body_with_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authenticate_me_from_body_with_code: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The authentication token to send in the `Authorization` header, together with the second factor that was accepted |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The request body could not be validated, for example `confirmData.email` is not an email address |  -  |
**401** | The credentials were rejected, or the two-factor code is wrong, empty or expired |  -  |
**403** | The user is disabled, or too many failed attempts have blocked further sign-ins for these credentials |  -  |
**404** | No user of this portal matches the credentials in the request body |  -  |
**429** | The portal rate limiter rejected the call - retry after the interval in the `Retry-After` header |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_confirm**
> ConfirmWrapper check_confirm(email_validation_key_model=email_validation_key_model)

Checks the key of a confirmation link that the portal sent by email and reports whether the action behind that
link can still be carried out - an employee invitation, phone activation, a password change, portal removal
and so on. Take `key` and `type` from the query string of the link; when `key` is left empty, the key saved in
the confirmation cookie of the same `type` is used instead. Open to unauthenticated callers and read-only: it
neither accepts the invitation nor signs anyone in. `result` is `Ok` when the link may be used, `Invalid` when
the key does not match the type or the email, `Expired` when it is too old, and `TariffLimit`, `UserExisted`,
`UserExcluded` or `QuotaFailed` when the key is sound but the invitation behind it cannot be accepted. Only
`Ok` should be followed by the operation that performs the action - `POST api/2.0/people` with
`fromInviteLink` for an invitation, `POST api/2.0/authentication` with `confirmData` for a sign-in link - and
for an invitation to a room the answer also carries the identifier and the title of that room.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_validation_key_model** | [**EmailValidationKeyModel**](EmailValidationKeyModel.md)|  | [optional] 

### Return type

[**ConfirmWrapper**](ConfirmWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.confirm_wrapper import ConfirmWrapper
from docspace_api_sdk.models.email_validation_key_model import EmailValidationKeyModel
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
    api_instance = docspace_api_sdk.AuthenticationApi(api_client)
    email_validation_key_model = docspace_api_sdk.EmailValidationKeyModel() # EmailValidationKeyModel |  (optional)

    try:
        # Check a confirmation link
        api_response = api_instance.check_confirm(email_validation_key_model=email_validation_key_model)
        print("The response of AuthenticationApi->check_confirm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->check_confirm: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Whether the confirmation link may be used, with the room and the email it was issued for when it is an invitation |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The portal's IP restrictions do not allow this address to check an invitation link |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_is_authentificated**
> BooleanWrapper get_is_authentificated()

Reports whether the credentials that came with this very request identify a signed-in user of the current
portal - the authentication cookie, or the token in the `Authorization` header. Nothing has to be called
first: the operation is open to unauthenticated callers, who simply get `false`, it is read-only and
idempotent, and it answers even while the portal's payment has lapsed. The result is a bare boolean that
carries no reason, so `false` covers a missing, malformed, expired and revoked token alike; the way to recover
from it is to sign in again with `POST api/2.0/authentication`. It says nothing about who the caller is or how
long the session still lasts - read `GET api/2.0/people/@self` for the profile behind the token.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
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
    api_instance = docspace_api_sdk.AuthenticationApi(api_client)

    try:
        # Check authentication
        api_response = api_instance.get_is_authentificated()
        print("The response of AuthenticationApi->get_is_authentificated:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->get_is_authentificated: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | `true` when the request carries a valid token or cookie of an active portal user, `false` in every other case |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> StringWrapper logout()

Ends the session the request itself was made with: the login event behind the authentication cookie is closed,
the sockets opened for it are disconnected, the portal cookies are cleared and a logout event is written to
the login history. Send it with the cookie or token of the session that is to be closed; an anonymous call is
accepted and closes nothing. The operation is mutating and idempotent - the same session cannot be closed
twice - and it touches only that one session: the other sessions of the same user stay alive and are ended by
`PUT api/2.0/security/activeconnections/logoutallexceptthis` or
`PUT api/2.0/security/activeconnections/logout/{loginEventId}`. The answer is a single logout URL when the
user signed in through SSO and the portal has an SLO endpoint configured, and the client has to open that URL
to end the session on the identity provider as well; for everyone else it is empty and nothing more is needed.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
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
    api_instance = docspace_api_sdk.AuthenticationApi(api_client)

    try:
        # Log out
        api_response = api_instance.logout()
        print("The response of AuthenticationApi->logout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->logout: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The single logout URL to open when the user signed in through SSO, or an empty result when no further action is needed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_mobile_phone**
> AuthenticationTokenWrapper save_mobile_phone(mobile_requests_dto=mobile_requests_dto)

Stores the mobile phone number of a user who is going through phone activation and sends the first SMS
authentication code to it. It is reachable only with the phone-activation confirmation link that
`POST api/2.0/authentication` returns in `confirmUrl` when SMS two-factor is required and the user has no
activated number yet: that link authorizes the call in place of an authentication token, and no token is
issued here. The operation is mutating and not idempotent - it saves the number as not activated, writes an
audit event and sends a message - and an already activated number is not replaced this way, the stored number
has to be erased first. The answer carries `sms`, the masked number and `expires`, the moment the code stops
being accepted. Submit that code to `POST api/2.0/authentication/{code}`, which signs the user in and marks
the number activated, or ask for another one with `POST api/2.0/authentication/sendsms`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_requests_dto** | [**MobileRequestsDto**](MobileRequestsDto.md)|  | [optional] 

### Return type

[**AuthenticationTokenWrapper**](AuthenticationTokenWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.authentication_token_wrapper import AuthenticationTokenWrapper
from docspace_api_sdk.models.mobile_requests_dto import MobileRequestsDto
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
    api_instance = docspace_api_sdk.AuthenticationApi(api_client)
    mobile_requests_dto = docspace_api_sdk.MobileRequestsDto() # MobileRequestsDto |  (optional)

    try:
        # Set a mobile phone
        api_response = api_instance.save_mobile_phone(mobile_requests_dto=mobile_requests_dto)
        print("The response of AuthenticationApi->save_mobile_phone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->save_mobile_phone: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The masked phone number the code was sent to and the moment that code expires - no authentication token yet |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_sms_code**
> AuthenticationTokenWrapper send_sms_code(auth_requests_dto=auth_requests_dto)

Sends a new SMS authentication code to the phone number stored for the user and reports when that code
expires. The credentials in the body are checked exactly as by `POST api/2.0/authentication`, so use this
operation to resend the code after that call answered with `sms`; the user needs SMS two-factor enabled and a
phone number already stored, which `POST api/2.0/authentication/setphone` registers. Open to unauthenticated
callers, mutating and not idempotent: every call sends a message, is counted in the portal's SMS usage and
spends one of the few codes a number is allowed within the code lifetime (ten minutes by default), after which
the call fails until those codes expire. Codes sent earlier stay valid, so a resent code does not invalidate
them, and the first one to be accepted invalidates all of them. The answer carries `sms`, the masked number
and `expires`, and no token - submit the code to `POST api/2.0/authentication/{code}`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_requests_dto** | [**AuthRequestsDto**](AuthRequestsDto.md)|  | [optional] 

### Return type

[**AuthenticationTokenWrapper**](AuthenticationTokenWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.auth_requests_dto import AuthRequestsDto
from docspace_api_sdk.models.authentication_token_wrapper import AuthenticationTokenWrapper
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
    api_instance = docspace_api_sdk.AuthenticationApi(api_client)
    auth_requests_dto = docspace_api_sdk.AuthRequestsDto() # AuthRequestsDto |  (optional)

    try:
        # Send SMS code
        api_response = api_instance.send_sms_code(auth_requests_dto=auth_requests_dto)
        print("The response of AuthenticationApi->send_sms_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->send_sms_code: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The masked phone number the code was sent to and the moment that code expires - no authentication token yet |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The request body could not be validated, for example `confirmData.email` is not an email address |  -  |
**401** | The password, the confirmation key or the third-party profile was rejected |  -  |
**403** | The user is disabled, or too many failed attempts have blocked further sign-ins for these credentials |  -  |
**404** | No user of this portal matches the credentials in the request body |  -  |
**429** | The portal rate limiter rejected the call - retry after the interval in the `Retry-After` header |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

