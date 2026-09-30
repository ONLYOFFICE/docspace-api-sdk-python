# docspace_api_sdk.EmailApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_user_email**](#change_user_email) | **PUT** /api/2.0/people/{userid}/email | Change a user email
[**send_email_change_instructions**](#send_email_change_instructions) | **POST** /api/2.0/people/email | Send instructions to change email


# **change_user_email**
> EmployeeFullWrapper change_user_email(userid, change_email_request)

Sets a new email address on an account, which is the step that completes an email change.
The request has to carry the confirmation token from the emailed link rather than an ordinary session, and an
expired or already used token is answered with 401.
The account has to exist and be `Active`, and only the portal owner may change the owner's own address.
Pass the address either in plain text as `email` or, as it arrives inside the confirmation link, encrypted as
`encEmail`; an empty or malformed address answers 400.
An address equal to the current one is accepted and changes nothing, while a new one is stored in lowercase
and marks the account `Activated`, because following the link proves the address works.
The answer is the profile with its new address.
The change is requested through `POST api/2.0/people/email`, which is what sends the link.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **UUID**| The ID of the account whose address is set, taken from the route. It has to match the account the  confirmation token was issued for, and the account has to be active. | 
 **change_email_request** | [**ChangeEmailRequest**](ChangeEmailRequest.md)| The new address, in plain text or in the encrypted form the confirmation link carries. | 

### Return type

[**EmployeeFullWrapper**](EmployeeFullWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.change_email_request import ChangeEmailRequest
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
    api_instance = docspace_api_sdk.EmailApi(api_client)
    userid = UUID('00000000-0000-0000-0000-000000000000') # UUID | The ID of the account whose address is set, taken from the route. It has to match the account the  confirmation token was issued for, and the account has to be active.
    change_email_request = docspace_api_sdk.ChangeEmailRequest() # ChangeEmailRequest | The new address, in plain text or in the encrypted form the confirmation link carries.

    try:
        # Change a user email
        api_response = api_instance.change_user_email(userid, change_email_request)
        print("The response of EmailApi->change_user_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->change_user_email: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The profile with its new address |  * X-RateLimit-Limit - Rate limit: 5 requests per 15 minutes per user/IP. <br>  * X-RateLimit-Remaining - Requests remaining in the current 15-minute window. <br>  * X-RateLimit-Reset -  <br>  |
**400** | The user ID is empty, or the address is missing or malformed |  -  |
**403** | The account is not active, or only its owner may change this address |  -  |
**404** | No account has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying (5 req / 15 min limit per user/IP). <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_email_change_instructions**
> StringWrapper send_email_change_instructions(update_member_request_dto=update_member_request_dto)

Starts changing the email address of an account, and what it actually does depends on who calls it.
A caller acting on their own account only gets a confirmation letter sent to the new address, and the address
stays unchanged until that link is followed, which lands on `PUT api/2.0/people/{userid}/email`.
A DocSpace administrator acting on somebody else changes the address immediately instead: the account is
marked as not activated, every session of it is ended, and activation instructions are sent to the new
address - and passing the address the account already has is then rejected with 400.
A caller who is not an administrator may only address their own account, nobody but the owner may change the
owner's address, and only the owner may change the address of another DocSpace administrator.
The target has to be an account that is neither disabled nor a pending invitation, otherwise the operation
answers 404, and an address that already belongs to somebody answers 400.
The answer is a ready-to-display message naming the address the letter was sent to.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_member_request_dto** | [**UpdateMemberRequestDto**](UpdateMemberRequestDto.md)|  | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.string_wrapper import StringWrapper
from docspace_api_sdk.models.update_member_request_dto import UpdateMemberRequestDto
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
    api_instance = docspace_api_sdk.EmailApi(api_client)
    update_member_request_dto = docspace_api_sdk.UpdateMemberRequestDto() # UpdateMemberRequestDto |  (optional)

    try:
        # Send instructions to change email
        api_response = api_instance.send_email_change_instructions(update_member_request_dto=update_member_request_dto)
        print("The response of EmailApi->send_email_change_instructions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->send_email_change_instructions: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The message stating which address the letter was sent to |  * X-RateLimit-Limit - Rate limit: 5 requests per 15 minutes per user/IP. <br>  * X-RateLimit-Remaining - Requests remaining in the current 15-minute window. <br>  * X-RateLimit-Reset -  <br>  |
**400** | The user ID is empty, the address is missing, malformed, already taken, or equal to the current one |  -  |
**403** | The caller may not change the address of that account |  -  |
**404** | The account does not exist, is disabled, or is a pending invitation |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying (5 req / 15 min limit per user/IP). <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

