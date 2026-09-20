# docspace_api_sdk.MessagesApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enable_admin_message_settings**](#enable_admin_message_settings) | **POST** /api/2.0/settings/messagesettings | Enable or disable administrator messages
[**send_admin_mail**](#send_admin_mail) | **POST** /api/2.0/settings/sendadmmail | Send a message to the administrator
[**send_join_invite_mail**](#send_join_invite_mail) | **POST** /api/2.0/settings/sendjoininvite | Send an invitation email


# **enable_admin_message_settings**
> StringWrapper enable_admin_message_settings(turn_on_admin_message_settings_request_dto=turn_on_admin_message_settings_request_dto)

Switches on or off the contact form the sign-in page offers a visitor who cannot get into the portal, and
which delivers their message to the portal administrators. The caller needs the portal-settings right of a
DocSpace administrator - the portal owner and a DocSpace administrator qualify, any other member is refused.
Send the new state as `turnOn`: `true` publishes the form, `false` hides it. The change covers the whole
portal, applies to the next sign-in page without a restart, is recorded in the audit trail, and repeating the
call with the same value leaves the portal as it is. What comes back is a localized confirmation message
rather than the stored flag - read the flag as `enableAdmMess` from `GET api/2.0/settings`, which needs no
token. That flag is also forced on while the portal's payment has lapsed, so it can report `true` on a portal
where the form was switched off here. The form itself posts to `POST api/2.0/settings/sendadmmail` and this
setting gates nothing else: the notifications administrators receive as portal members are subscribed
separately with `POST api/2.0/settings/notification`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **turn_on_admin_message_settings_request_dto** | [**TurnOnAdminMessageSettingsRequestDto**](TurnOnAdminMessageSettingsRequestDto.md)|  | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.string_wrapper import StringWrapper
from docspace_api_sdk.models.turn_on_admin_message_settings_request_dto import TurnOnAdminMessageSettingsRequestDto
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
    api_instance = docspace_api_sdk.MessagesApi(api_client)
    turn_on_admin_message_settings_request_dto = docspace_api_sdk.TurnOnAdminMessageSettingsRequestDto() # TurnOnAdminMessageSettingsRequestDto |  (optional)

    try:
        # Enable or disable administrator messages
        api_response = api_instance.enable_admin_message_settings(turn_on_admin_message_settings_request_dto=turn_on_admin_message_settings_request_dto)
        print("The response of MessagesApi->enable_admin_message_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->enable_admin_message_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A localized message confirming that the administrator message setting has been saved |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_admin_mail**
> StringWrapper send_admin_mail(admin_message_settings_requests_dto=admin_message_settings_requests_dto)

Sends a message from someone who cannot get into the portal to its administrators - the contact form the
sign-in page offers unauthenticated visitors. No token is needed. The form has to be published first with
`POST api/2.0/settings/messagesettings` unless the portal's payment has lapsed, otherwise nothing is sent;
`enableAdmMess` in `GET api/2.0/settings` reports whether the call is worth making. `email` is the address the
administrators answer to and has to be a real address, and `message` is reduced to plain text first, so a body
carrying nothing but markup counts as empty - either fault is refused with 400. When the caller is not signed
in and this installation has a CAPTCHA configured, `recaptchaResponse` has to carry a solved challenge of the
`recaptchaType` that `GET api/2.0/settings` publishes together with the site key, and a missing or stale
answer refuses the call. `culture` picks the language of the letter. Delivery is queued and reaches the
administrators subscribed to administrator notifications, so a confirmed call means accepted rather than read,
and the answer is a localized confirmation. Attempts are rate limited per address and per operation, and
further ones are refused with 429.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_message_settings_requests_dto** | [**AdminMessageSettingsRequestsDto**](AdminMessageSettingsRequestsDto.md)|  | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.admin_message_settings_requests_dto import AdminMessageSettingsRequestsDto
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
    api_instance = docspace_api_sdk.MessagesApi(api_client)
    admin_message_settings_requests_dto = docspace_api_sdk.AdminMessageSettingsRequestsDto() # AdminMessageSettingsRequestsDto |  (optional)

    try:
        # Send a message to the administrator
        api_response = api_instance.send_admin_mail(admin_message_settings_requests_dto=admin_message_settings_requests_dto)
        print("The response of MessagesApi->send_admin_mail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->send_admin_mail: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A localized message confirming that the message has been queued for the portal administrators |  * X-RateLimit-Limit - Rate limit: 5 requests per 15 minutes per user/IP. <br>  * X-RateLimit-Remaining - Requests remaining in the current 15-minute window. <br>  * X-RateLimit-Reset -  <br>  |
**400** | The email address is malformed, or the message is empty once its markup is stripped |  -  |
**429** | Too many contact attempts came from the same address within the rate-limit window |  * Retry-After - Seconds to wait before retrying (5 req / 15 min limit per user/IP). <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_join_invite_mail**
> StringWrapper send_join_invite_mail(admin_message_base_settings_requests_dto=admin_message_base_settings_requests_dto)

Sends an invitation email with a join link to the address in the request - the self-registration the sign-in
page's register link performs. No token is needed. The portal has to publish a trusted-domain policy first,
saved with `POST api/2.0/settings/maildomainsettings`: without one there is nothing to join and every caller
alike is answered with 405 - the same condition `GET api/2.0/settings` reports as `enabledJoin`. `email` has
to be a real address written in ASCII rather than an internationalized one, must not already belong to a
portal member, and, when the policy names domains rather than accepting all of them, has to end with one of
them - each of those faults is refused with 400. `culture` picks the language of the letter. The invitation is
not an account: the invitee becomes a member only after following the link, and the role it grants, user or
room administrator, follows the trusted-domain settings and drops to user once the portal's paid places are
taken. Where the installation caps invitations, an accepted call spends one of those counted by
`invitationLimit`, and only about a dozen calls from one address in two minutes are accepted. What comes back
is a localized confirmation.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_message_base_settings_requests_dto** | [**AdminMessageBaseSettingsRequestsDto**](AdminMessageBaseSettingsRequestsDto.md)|  | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.admin_message_base_settings_requests_dto import AdminMessageBaseSettingsRequestsDto
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
    api_instance = docspace_api_sdk.MessagesApi(api_client)
    admin_message_base_settings_requests_dto = docspace_api_sdk.AdminMessageBaseSettingsRequestsDto() # AdminMessageBaseSettingsRequestsDto |  (optional)

    try:
        # Send an invitation email
        api_response = api_instance.send_join_invite_mail(admin_message_base_settings_requests_dto=admin_message_base_settings_requests_dto)
        print("The response of MessagesApi->send_join_invite_mail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->send_join_invite_mail: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A localized message confirming that the invitation with the join link has been sent |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The email address is malformed or internationalized, lies outside the trusted domains, or already belongs to a member of the portal |  -  |
**403** | The portal is not accepting requests while it is being restored, transferred or encrypted |  -  |
**405** | The portal publishes no trusted-domain policy, so it has nothing to join |  -  |
**429** | Too many invitation requests came from the same network address |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

