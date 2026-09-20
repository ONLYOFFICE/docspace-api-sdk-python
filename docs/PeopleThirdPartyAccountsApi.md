# docspace_api_sdk.ThirdPartyAccountsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_third_party_auth_providers**](#get_third_party_auth_providers) | **GET** /api/2.0/people/thirdparty/providers | Get third-party providers
[**link_third_party_account**](#link_third_party_account) | **PUT** /api/2.0/people/thirdparty/linkaccount | Link a third-party account
[**signup_third_party_account**](#signup_third_party_account) | **POST** /api/2.0/people/thirdparty/signup | Sign up with a provider
[**unlink_third_party_account**](#unlink_third_party_account) | **DELETE** /api/2.0/people/thirdparty/unlinkaccount | Unlink a third-party account


# **get_third_party_auth_providers**
> AccountInfoArrayWrapper get_third_party_auth_providers(invite_view=invite_view, settings_view=settings_view, client_callback=client_callback, from_only=from_only)

Returns the third-party identity providers this portal has enabled, each with the URL that starts the login
with it, so a client can render the social sign-in buttons.
It needs no authentication and is the operation to call before showing a login or an invitation page; an
empty list means the portal has no provider configured, not that the call failed.
The call is read-only, and `linked` says whether the provider is already connected to the calling profile -
for an anonymous caller there is nothing to compare against, so every entry comes back with false.
The order is fixed by the portal, except that a caller located in China gets `weixin` first.
Pass `fromOnly` to keep a single provider, `inviteView` to leave out the providers that cannot be used on an
invitation page, and `settingsView` or `clientCallback` to get URLs that open in a popup instead of
redirecting the desktop application.
Use `PUT api/2.0/people/thirdparty/linkaccount` to connect one of these providers to an existing profile and
`POST api/2.0/people/thirdparty/signup` to create a profile through one.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_view** | **bool**| Set it to true when the list is rendered on an invitation page: the providers that cannot be used to accept an  invitation, `twitter` and `appleid`, are then left out. It defaults to false, which returns every enabled  provider. | [optional] 
 **settings_view** | **bool**| Set it to true when the list is rendered on a settings page, to get login URLs that open in a popup window.  With the default false the URL still opens in a popup for a desktop browser, and switches to a redirect only  for a mobile browser or for the DocSpace desktop application. | [optional] 
 **client_callback** | **str**| The name of the client-side function the popup calls back when the provider authorization finishes. It is  placed into the returned URLs as they are, and it is only used by the popup mode. | [optional] 
 **from_only** | **str**| Keeps only the named provider, compared case-insensitively against the lowercase provider names such as  `google` or `microsoft`; the special value `openid` selects `google`. Omit it to get every enabled provider. | [optional] 

### Return type

[**AccountInfoArrayWrapper**](AccountInfoArrayWrapper.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.account_info_array_wrapper import AccountInfoArrayWrapper
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
    api_instance = docspace_api_sdk.ThirdPartyAccountsApi(api_client)
    invite_view = false # bool | Set it to true when the list is rendered on an invitation page: the providers that cannot be used to accept an  invitation, `twitter` and `appleid`, are then left out. It defaults to false, which returns every enabled  provider. (optional)
    settings_view = false # bool | Set it to true when the list is rendered on a settings page, to get login URLs that open in a popup window.  With the default false the URL still opens in a popup for a desktop browser, and switches to a redirect only  for a mobile browser or for the DocSpace desktop application. (optional)
    client_callback = 'onAuthCallback' # str | The name of the client-side function the popup calls back when the provider authorization finishes. It is  placed into the returned URLs as they are, and it is only used by the popup mode. (optional)
    from_only = 'google' # str | Keeps only the named provider, compared case-insensitively against the lowercase provider names such as  `google` or `microsoft`; the special value `openid` selects `google`. Omit it to get every enabled provider. (optional)

    try:
        # Get third-party providers
        api_response = api_instance.get_third_party_auth_providers(invite_view=invite_view, settings_view=settings_view, client_callback=client_callback, from_only=from_only)
        print("The response of ThirdPartyAccountsApi->get_third_party_auth_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdPartyAccountsApi->get_third_party_auth_providers: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The enabled providers, each with its login URL and its link state for the caller |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_third_party_account**
> link_third_party_account(link_account_request_dto=link_account_request_dto)

Connects a third-party identity to the calling profile, so that the account can afterwards sign in through
that provider.
The profile has to come from a completed provider authorization: pass the serialized `LoginProfile` the login
flow started from `GET api/2.0/people/thirdparty/providers` handed back, not a hand-written object.
It acts on the authenticated account only, and the portal has to be a standalone installation or have a
tariff that includes third-party authorization, otherwise the operation answers 403.
The call returns no body and is not idempotent: one third-party identity can be linked to a single portal
profile, so repeating it, or linking an identity somebody else already uses, answers 400.
A profile whose authorization was cancelled by the user is accepted and ignored, so a cancelled login also
answers 200 and links nothing - read `GET api/2.0/people/thirdparty/providers` afterwards and check `linked`
to find out whether the link exists.
Use `DELETE api/2.0/people/thirdparty/unlinkaccount` to remove a link.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_account_request_dto** | [**LinkAccountRequestDto**](LinkAccountRequestDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.link_account_request_dto import LinkAccountRequestDto
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
    api_instance = docspace_api_sdk.ThirdPartyAccountsApi(api_client)
    link_account_request_dto = docspace_api_sdk.LinkAccountRequestDto() # LinkAccountRequestDto |  (optional)

    try:
        # Link a third-party account
        api_instance.link_third_party_account(link_account_request_dto=link_account_request_dto)
    except Exception as e:
        print("Exception when calling ThirdPartyAccountsApi->link_third_party_account: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The third-party identity is linked to the calling profile. No content is returned |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The third-party identity is already linked to a portal profile |  -  |
**403** | The portal tariff does not include third-party authorization |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signup_third_party_account**
> EmployeeWrapper signup_third_party_account(signup_account_request_dto=signup_account_request_dto)

Creates a portal profile from a third-party identity and joins the invitation the `key` belongs to, which is
how a person accepts an invitation by signing in with a provider instead of setting a password.
It needs no authentication, but it does need a valid invitation: `key` has to be the key of a live invitation
link, and `serializedProfile` has to be the profile a completed provider authorization produced.
The resulting type comes from the invitation link itself, and `employeeType` only says which type to look the
link up as, defaulting to `RoomAdmin`.
When the identity or its email already belongs to a portal profile, that existing profile is returned and the
provider is linked to it instead of a second account being created, so the call can be repeated safely.
The answer is the profile the caller ends up with - and it is empty, still with status 200, when the provider
authorization was cancelled or when the profile could not be created, so check for an empty body instead of
relying on the status alone.
A `weixin` or `nextcloud` identity carries no email address, so the portal generates one and the profile stays
in the `AutoGenerated` activation state; every other provider has to supply an email.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signup_account_request_dto** | [**SignupAccountRequestDto**](SignupAccountRequestDto.md)|  | [optional] 

### Return type

[**EmployeeWrapper**](EmployeeWrapper.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.employee_wrapper import EmployeeWrapper
from docspace_api_sdk.models.signup_account_request_dto import SignupAccountRequestDto
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
    api_instance = docspace_api_sdk.ThirdPartyAccountsApi(api_client)
    signup_account_request_dto = docspace_api_sdk.SignupAccountRequestDto() # SignupAccountRequestDto |  (optional)

    try:
        # Sign up with a provider
        api_response = api_instance.signup_third_party_account(signup_account_request_dto=signup_account_request_dto)
        print("The response of ThirdPartyAccountsApi->signup_third_party_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdPartyAccountsApi->signup_third_party_account: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The profile linked to the third-party identity, or an empty body when the authorization was cancelled or the profile could not be created |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The invitation link is invalid or has expired, or the email already belongs to a profile that has not been activated yet |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_third_party_account**
> unlink_third_party_account(provider=provider)

Removes the link between the calling profile and the named third-party provider, so that the account can no
longer sign in through it.
It acts on the authenticated account only and takes the provider name in the query, using the same lowercase
values `GET api/2.0/people/thirdparty/providers` returns, such as `google` or `microsoft`.
The call returns no body and is idempotent: unlinking a provider that is not linked answers 200 and changes
nothing.
The portal profile itself is kept, together with its password, so the account stays usable through the
ordinary sign-in; only the third-party route is removed.
Link the provider again through `PUT api/2.0/people/thirdparty/linkaccount`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| The name of the provider to unlink, in the lowercase form `GET api/2.0/people/thirdparty/providers` returns,  such as `google` or `microsoft`. A name that is not linked to the calling profile is accepted and changes  nothing. | [optional] 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
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
    api_instance = docspace_api_sdk.ThirdPartyAccountsApi(api_client)
    provider = 'google' # str | The name of the provider to unlink, in the lowercase form `GET api/2.0/people/thirdparty/providers` returns,  such as `google` or `microsoft`. A name that is not linked to the calling profile is accepted and changes  nothing. (optional)

    try:
        # Unlink a third-party account
        api_instance.unlink_third_party_account(provider=provider)
    except Exception as e:
        print("Exception when calling ThirdPartyAccountsApi->unlink_third_party_account: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The third-party identity is no longer linked to the calling profile. No content is returned |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

