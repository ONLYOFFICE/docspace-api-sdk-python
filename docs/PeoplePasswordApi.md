# docspace_api_sdk.PasswordApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_user_password**](#change_user_password) | **PUT** /api/2.0/people/{userid}/password | Change a user password
[**send_user_password**](#send_user_password) | **POST** /api/2.0/people/password | Remind a user password


# **change_user_password**
> EmployeeFullWrapper change_user_password(userid, change_password_request)

Sets a new password on an account, which is the step that completes a password change or a password
recovery.
The request has to carry the confirmation token from the emailed link rather than an ordinary session, and an
expired or already used token is answered with 401.
The account has to exist and be `Active`, so the password of a disabled account or of an open invitation
cannot be set, and only the portal owner may set the owner's own password.
Send either `passwordHash`, which is taken as it is, or a plain `password`, which is checked against the
portal password policy; sending neither, or a password the policy rejects, answers 400.
The change ends every other session of that account and emails it a notice that the password was changed.
The answer is the profile, which does not carry the password in any form.
To have the recovery link sent in the first place, use `POST api/2.0/people/password`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **UUID**| The ID of the account whose password is set, taken from the route. It has to match the account the  confirmation token was issued for, and the account has to be active. | 
 **change_password_request** | [**ChangePasswordRequest**](ChangePasswordRequest.md)| The new password, sent either in plain text or already hashed. Exactly one of the two fields is needed. | 

### Return type

[**EmployeeFullWrapper**](EmployeeFullWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.change_password_request import ChangePasswordRequest
from docspace_api_sdk.models.employee_full_wrapper import EmployeeFullWrapper
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
    api_instance = docspace_api_sdk.PasswordApi(api_client)
    userid = UUID('00000000-0000-0000-0000-000000000000') # UUID | The ID of the account whose password is set, taken from the route. It has to match the account the  confirmation token was issued for, and the account has to be active.
    change_password_request = docspace_api_sdk.ChangePasswordRequest() # ChangePasswordRequest | The new password, sent either in plain text or already hashed. Exactly one of the two fields is needed.

    try:
        # Change a user password
        api_response = api_instance.change_user_password(userid, change_password_request)
        print("The response of PasswordApi->change_user_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PasswordApi->change_user_password: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The profile whose password was changed |  * X-RateLimit-Limit - Rate limit: 5 requests per 15 minutes per user/IP. <br>  * X-RateLimit-Remaining - Requests remaining in the current 15-minute window. <br>  * X-RateLimit-Reset -  <br>  |
**400** | The user ID is empty, no password was sent, or the password does not meet the portal policy |  -  |
**403** | The account is not active, or only its owner may change this password |  -  |
**404** | No account has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying (5 req / 15 min limit per user/IP). <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_user_password**
> StringWrapper send_user_password(email_member_request_dto=email_member_request_dto)

Emails a password recovery link to an address, and is the entry point of the recovery flow rather than the
operation that changes anything.
It needs no authentication, which is how a person who cannot sign in uses it; when the portal has a CAPTCHA
configured, an unauthenticated request has to pass it and answers 403 if it does not.
An unauthenticated caller always gets the same success message, whether or not the address belongs to an
account, so the answer cannot be used to find out which addresses are registered.
An authenticated caller does get told: a failure is answered with 403, and asking for somebody else requires
DocSpace administrator rights, while the owner's password can be asked for by the owner alone and another
administrator's only by the owner.
The link that is sent leads to `PUT api/2.0/people/{userid}/password`, which is where the new password is
set; no password is ever sent by email despite the wording of the message.
Repeated calls are throttled.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_member_request_dto** | [**EmailMemberRequestDto**](EmailMemberRequestDto.md)|  | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.email_member_request_dto import EmailMemberRequestDto
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

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.PasswordApi(api_client)
    email_member_request_dto = docspace_api_sdk.EmailMemberRequestDto() # EmailMemberRequestDto |  (optional)

    try:
        # Remind a user password
        api_response = api_instance.send_user_password(email_member_request_dto=email_member_request_dto)
        print("The response of PasswordApi->send_user_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PasswordApi->send_user_password: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The message stating that the recovery link was sent to the address |  * X-RateLimit-Limit - Rate limit: 5 requests per 15 minutes per user/IP. <br>  * X-RateLimit-Remaining - Requests remaining in the current 15-minute window. <br>  * X-RateLimit-Reset -  <br>  |
**403** | The CAPTCHA was not passed, or an authenticated caller may not ask for that account |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying (5 req / 15 min limit per user/IP). <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

