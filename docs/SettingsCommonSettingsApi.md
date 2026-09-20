# docspace_api_sdk.CommonSettingsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_admin_helper**](#close_admin_helper) | **PUT** /api/2.0/settings/closeadminhelper | Close the admin helper
[**complete_wizard**](#complete_wizard) | **PUT** /api/2.0/settings/wizard/complete | Complete the Wizard settings
[**configure_deep_link**](#configure_deep_link) | **POST** /api/2.0/settings/deeplink | Configure the deep link settings
[**delete_portal_color_theme**](#delete_portal_color_theme) | **DELETE** /api/2.0/settings/colortheme | Delete a color theme
[**get_deep_link_settings**](#get_deep_link_settings) | **GET** /api/2.0/settings/deeplink | Get the deep link settings
[**get_payment_settings**](#get_payment_settings) | **GET** /api/2.0/settings/payment | Get the payment settings
[**get_portal_color_theme**](#get_portal_color_theme) | **GET** /api/2.0/settings/colortheme | Get a color theme
[**get_portal_hostname**](#get_portal_hostname) | **GET** /api/2.0/settings/machine | Get the portal hostname
[**get_portal_logo**](#get_portal_logo) | **GET** /api/2.0/settings/logo | Get a portal logo
[**get_portal_settings**](#get_portal_settings) | **GET** /api/2.0/settings | Get the portal settings
[**get_socket_settings**](#get_socket_settings) | **GET** /api/2.0/settings/socket | Get the socket settings
[**get_supported_cultures**](#get_supported_cultures) | **GET** /api/2.0/settings/cultures | Get supported languages
[**get_tenant_ai_access_settings**](#get_tenant_ai_access_settings) | **GET** /api/2.0/settings/ai-access | Get the AI access settings
[**get_tenant_user_invitation_settings**](#get_tenant_user_invitation_settings) | **GET** /api/2.0/settings/invitationsettings | Get the user invitation settings
[**get_time_zones**](#get_time_zones) | **GET** /api/2.0/settings/timezones | Get time zones
[**save_default_folder**](#save_default_folder) | **PUT** /api/2.0/settings/defaultfolder | Set the default folder
[**save_dns_settings**](#save_dns_settings) | **PUT** /api/2.0/settings/dns | Save the DNS settings
[**save_mail_domain_settings**](#save_mail_domain_settings) | **POST** /api/2.0/settings/maildomainsettings | Save the mail domain settings
[**save_portal_color_theme**](#save_portal_color_theme) | **PUT** /api/2.0/settings/colortheme | Save a color theme
[**set_tenant_ai_access_settings**](#set_tenant_ai_access_settings) | **POST** /api/2.0/settings/ai-access | Set the AI access settings
[**update_email_activation_settings**](#update_email_activation_settings) | **PUT** /api/2.0/settings/emailactivation | Update the email activation settings
[**update_invitation_settings**](#update_invitation_settings) | **PUT** /api/2.0/settings/invitationsettings | Update the user invitation settings


# **close_admin_helper**
> close_admin_helper()

Dismisses the administrator helper tip for the caller, so it is not shown again on this account. Available
only to a DocSpace administrator, which includes the portal Owner, on a Standalone (self-hosted) installation
running outside white-label custom mode; every other caller is refused. This is a mutating, idempotent call
scoped to the calling account only; it never affects other administrators. It returns no data on success.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

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
    api_instance = docspace_api_sdk.CommonSettingsApi(api_client)

    try:
        # Close the admin helper
        api_instance.close_admin_helper()
    except Exception as e:
        print("Exception when calling CommonSettingsApi->close_admin_helper: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The admin helper tip was dismissed for the caller |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**405** | The caller is not a DocSpace administrator, or the portal is on SaaS, custom mode, or not Standalone |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_wizard**
> WizardSettingsWrapper complete_wizard(wizard_requests_dto=wizard_requests_dto)

Finishes the initial portal setup wizard: sets the owner's password and locale, applies the supplied license
if one is required, and marks the wizard as completed so it is not shown again. This call is not for a normal
logged-in session: it requires a confirmation link bearing the Wizard claim, of the kind issued when a new
portal is created, and the link is consumed as part of authenticating the request; the caller must also hold
the EditPortalSettings permission. An empty password or a malformed email address is rejected without
completing the wizard, and so is a missing, invalid, or expired license, or a license whose user quota does
not cover the portal. This call is meant to run once per portal; running it again is accepted but has no
further effect once the wizard is already completed. It returns the resulting wizard settings, including the
completed flag.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wizard_requests_dto** | [**WizardRequestsDto**](WizardRequestsDto.md)|  | [optional] 

### Return type

[**WizardSettingsWrapper**](WizardSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.wizard_requests_dto import WizardRequestsDto
from docspace_api_sdk.models.wizard_settings_wrapper import WizardSettingsWrapper
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
    api_instance = docspace_api_sdk.CommonSettingsApi(api_client)
    wizard_requests_dto = docspace_api_sdk.WizardRequestsDto() # WizardRequestsDto |  (optional)

    try:
        # Complete the Wizard settings
        api_response = api_instance.complete_wizard(wizard_requests_dto=wizard_requests_dto)
        print("The response of CommonSettingsApi->complete_wizard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonSettingsApi->complete_wizard: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resulting wizard settings, including the completed flag |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The email address is malformed, or the password is empty |  -  |
**402** | The supplied license is missing, invalid, expired, or its user quota does not cover the portal |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configure_deep_link**
> TenantDeepLinkSettingsWrapper configure_deep_link(deep_link_configuration_requests_dto=deep_link_configuration_requests_dto)

Sets how the portal responds when a client opens a DocSpace link on a mobile device: always in the browser,
always in the native app, or asking the user to choose each time. Requires Owner or DocSpaceAdmin (the
EditPortalSettings permission). The handling mode must be one of the documented enum values; anything else is
rejected without being saved. This is a mutating, idempotent call: sending the same mode again leaves the
setting unchanged. It returns the saved deep link settings, including the timestamp of the last change; read
the current value at any time, including anonymously, from `GET api/2.0/settings/deeplink`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deep_link_configuration_requests_dto** | [**DeepLinkConfigurationRequestsDto**](DeepLinkConfigurationRequestsDto.md)|  | [optional] 

### Return type

[**TenantDeepLinkSettingsWrapper**](TenantDeepLinkSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.deep_link_configuration_requests_dto import DeepLinkConfigurationRequestsDto
from docspace_api_sdk.models.tenant_deep_link_settings_wrapper import TenantDeepLinkSettingsWrapper
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
    api_instance = docspace_api_sdk.CommonSettingsApi(api_client)
    deep_link_configuration_requests_dto = docspace_api_sdk.DeepLinkConfigurationRequestsDto() # DeepLinkConfigurationRequestsDto |  (optional)

    try:
        # Configure the deep link settings
        api_response = api_instance.configure_deep_link(deep_link_configuration_requests_dto=deep_link_configuration_requests_dto)
        print("The response of CommonSettingsApi->configure_deep_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonSettingsApi->configure_deep_link: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Saved deep link handling settings |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The handling mode is not one of the supported deep link handling values |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_portal_color_theme**
> CustomColorThemesSettingsWrapper delete_portal_color_theme(id)

Removes a custom color theme from the portal by its ID. Requires Owner or DocSpaceAdmin (the
EditPortalSettings permission). An ID belonging to one of the built-in default themes is not removable; the
call succeeds but leaves the theme list unchanged. If the deleted theme was the currently selected one, the
theme with the lowest remaining ID is selected automatically. This is a mutating, idempotent call: deleting an
ID that is already gone succeeds without error and again leaves nothing changed. It returns the full updated
theme configuration, including the (possibly new) selected theme.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The theme to remove, by theme ID. An ID belonging to a built-in theme leaves the list untouched, and so does  one that is already gone - neither is reported as an error. Removing the theme currently in use moves the  portal to the remaining theme with the lowest ID. | 

### Return type

[**CustomColorThemesSettingsWrapper**](CustomColorThemesSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.custom_color_themes_settings_wrapper import CustomColorThemesSettingsWrapper
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
    api_instance = docspace_api_sdk.CommonSettingsApi(api_client)
    id = 1 # int | The theme to remove, by theme ID. An ID belonging to a built-in theme leaves the list untouched, and so does  one that is already gone - neither is reported as an error. Removing the theme currently in use moves the  portal to the remaining theme with the lowest ID.

    try:
        # Delete a color theme
        api_response = api_instance.delete_portal_color_theme(id)
        print("The response of CommonSettingsApi->delete_portal_color_theme:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonSettingsApi->delete_portal_color_theme: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated color theme configuration: saved themes, selected theme, and plan limit |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deep_link_settings**
> TenantDeepLinkSettingsWrapper get_deep_link_settings()

Returns how the portal currently responds when a client opens a DocSpace link on a mobile device: always in
the browser, always in the native app, or asking the user to choose. No permission is required; anonymous
callers can read it too. This is a read-only, idempotent call. The response supports conditional requests:
send the standard If-Modified-Since header with the previous `lastModified` value, and an unchanged response
comes back empty instead of resending the settings. Change the mode with `POST api/2.0/settings/deeplink`,
which requires the EditPortalSettings permission.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**TenantDeepLinkSettingsWrapper**](TenantDeepLinkSettingsWrapper.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.tenant_deep_link_settings_wrapper import TenantDeepLinkSettingsWrapper
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
    api_instance = docspace_api_sdk.CommonSettingsApi(api_client)

    try:
        # Get the deep link settings
        api_response = api_instance.get_deep_link_settings()
        print("The response of CommonSettingsApi->get_deep_link_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonSettingsApi->get_deep_link_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current deep link handling settings |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_settings**
> PaymentSettingsWrapper get_payment_settings()

Returns the portal's payment-related configuration: the sales contact email, the URL to buy or extend a
subscription, whether the portal is Standalone, the current license's trial status and expiration date, and
the maximum quota quantity that can be purchased at once. Requires Owner or DocSpaceAdmin (the
EditPortalSettings permission). This is a read-only, idempotent call. It remains reachable even while the
portal's own subscription payment is overdue, since this is how the caller finds the link to resolve it.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**PaymentSettingsWrapper**](PaymentSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.payment_settings_wrapper import PaymentSettingsWrapper
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
    api_instance = docspace_api_sdk.CommonSettingsApi(api_client)

    try:
        # Get the payment settings
        api_response = api_instance.get_payment_settings()
        print("The response of CommonSettingsApi->get_payment_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonSettingsApi->get_payment_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment-related settings: sales contact, buy URL, Standalone flag, license, and quota cap |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portal_color_theme**
> CustomColorThemesSettingsWrapper get_portal_color_theme()

Returns the portal's color theme configuration: every saved custom theme, which one is currently selected, and
how many custom themes the plan still allows. No permission is required; anonymous callers can read it too.
This is a read-only, idempotent call. The response supports conditional requests: send the standard
If-Modified-Since header with the previous `lastModified` value, and an unchanged response comes back empty
instead of resending the same settings. A `limit` of `0` means the plan does not cap the number of custom
themes.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**CustomColorThemesSettingsWrapper**](CustomColorThemesSettingsWrapper.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.custom_color_themes_settings_wrapper import CustomColorThemesSettingsWrapper
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
    api_instance = docspace_api_sdk.CommonSettingsApi(api_client)

    try:
        # Get a color theme
        api_response = api_instance.get_portal_color_theme()
        print("The response of CommonSettingsApi->get_portal_color_theme:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonSettingsApi->get_portal_color_theme: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current color theme configuration: saved themes, selected theme, and plan limit |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portal_hostname**
> StringWrapper get_portal_hostname()

Returns the hostname the current request arrived on, exactly as sent in the HTTP Host header, so a client
mid-setup can learn the address the portal is actually reachable at. This call is not for a normal logged-in
session: it requires a confirmation link bearing the Wizard claim, of the kind generated during initial portal
setup, and the link is consumed as part of authenticating the request. This is a read-only, idempotent call.
The value reflects whatever the caller connected through, including a reverse proxy's public name, and is not
necessarily the tenant's configured alias or mapped domain.

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
    api_instance = docspace_api_sdk.CommonSettingsApi(api_client)

    try:
        # Get the portal hostname
        api_response = api_instance.get_portal_hostname()
        print("The response of CommonSettingsApi->get_portal_hostname:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonSettingsApi->get_portal_hostname: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hostname the current request arrived on |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portal_logo**
> StringWrapper get_portal_logo()

Returns the absolute URL of the portal's current logo image, already resolved against the active white-label
branding. Requires an authenticated session; every role, including Guest, can read it. This is a read-only,
idempotent call. The response supports conditional requests: send the standard If-Modified-Since header with
the previous `lastModified` value, and an unchanged response comes back empty instead of resending the same
URL. The URL points at whatever image is currently configured, including the default DocSpace logo when no
custom branding has been set.

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
    api_instance = docspace_api_sdk.CommonSettingsApi(api_client)

    try:
        # Get a portal logo
        api_response = api_instance.get_portal_logo()
        print("The response of CommonSettingsApi->get_portal_logo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonSettingsApi->get_portal_logo: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Absolute URL of the portal's current logo image |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portal_settings**
> SettingsWrapper get_portal_settings(withpassword=withpassword)

Returns the current portal's general configuration: branding, culture, feature flags, and DocSpace/Standalone
mode, everything the client needs to render its shell before or after login. No permission is required, but
the response shape depends on the caller's identity. An anonymous caller receives only the public subset
(culture, branding, DocSpace/Standalone flags, deep link data, setup-wizard and join-by-domain hints); once
authenticated, the response also includes tenant-specific fields such as the owner ID, time zone, invitation
limit, AI/banner/dev-tools flags, and, for a DocSpace administrator, the tenant wallet's low-balance flag.
This is a read-only, idempotent call. Pass `withPassword=true` to also receive the parameters (`salt`,
iteration count, hash size) used to hash the password client-side before it is sent to the authentication
endpoints; these are only added for an anonymous caller or when explicitly requested, never as part of the
default authenticated response.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **withpassword** | **bool**| Whether the answer also carries the salt, iteration count and hash size a client needs to hash a password  before sending it to the authentication operations. They are included for an anonymous caller anyway; for a  signed-in one they are left out unless this is set. | [optional] 

### Return type

[**SettingsWrapper**](SettingsWrapper.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.settings_wrapper import SettingsWrapper
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
    api_instance = docspace_api_sdk.CommonSettingsApi(api_client)
    withpassword = true # bool | Whether the answer also carries the salt, iteration count and hash size a client needs to hash a password  before sending it to the authentication operations. They are included for an anonymous caller anyway; for a  signed-in one they are left out unless this is set. (optional)

    try:
        # Get the portal settings
        api_response = api_instance.get_portal_settings(withpassword=withpassword)
        print("The response of CommonSettingsApi->get_portal_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonSettingsApi->get_portal_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current portal settings, tailored to the caller's authentication state |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_socket_settings**
> SocketSettingsWrapper get_socket_settings()

Returns the base URL of the portal's real-time notification hub (Socket.IO), which the client connects to for
live updates such as file changes, presence, or quota alerts. Requires an authenticated session; every role
can read it. This is a read-only, idempotent call. The value comes from server-side configuration and cannot
be changed through this API; an empty `url` means the portal has no notification hub configured and the client
should not attempt to connect.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**SocketSettingsWrapper**](SocketSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.socket_settings_wrapper import SocketSettingsWrapper
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
    api_instance = docspace_api_sdk.CommonSettingsApi(api_client)

    try:
        # Get the socket settings
        api_response = api_instance.get_socket_settings()
        print("The response of CommonSettingsApi->get_socket_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonSettingsApi->get_socket_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Base URL of the portal's real-time notification hub |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_cultures**
> STRINGArrayWrapper get_supported_cultures()

Returns the two- or four-letter language codes of every culture currently enabled on the portal (for example
`en-US`), used to populate a language picker before or after login. No permission is required; anonymous
callers can read it too. This is a read-only, idempotent call, and the list is not paginated. The response
supports conditional requests: an unchanged result is signaled instead of resending the same list. The set of
enabled cultures is a portal-wide configuration value, not a per-user preference.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**STRINGArrayWrapper**](STRINGArrayWrapper.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.string_array_wrapper import STRINGArrayWrapper
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
    api_instance = docspace_api_sdk.CommonSettingsApi(api_client)

    try:
        # Get supported languages
        api_response = api_instance.get_supported_cultures()
        print("The response of CommonSettingsApi->get_supported_cultures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonSettingsApi->get_supported_cultures: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Language codes of every culture currently enabled on the portal |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_ai_access_settings**
> TenantAiAccessSettingsWrapper get_tenant_ai_access_settings()

Returns whether AI functionality (chat, agents, vectorization) is currently available on the portal at all; AI
is enabled by default. Requires an authenticated session; every role can read it. This is a read-only,
idempotent call. When the setting is disabled, every AI-specific endpoint and folder is unavailable regardless
of the caller's own permissions; this call only reports the portal-wide switch, not any per-user entitlement.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**TenantAiAccessSettingsWrapper**](TenantAiAccessSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.tenant_ai_access_settings_wrapper import TenantAiAccessSettingsWrapper
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
    api_instance = docspace_api_sdk.CommonSettingsApi(api_client)

    try:
        # Get the AI access settings
        api_response = api_instance.get_tenant_ai_access_settings()
        print("The response of CommonSettingsApi->get_tenant_ai_access_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonSettingsApi->get_tenant_ai_access_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Whether AI functionality is currently enabled for the portal |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_user_invitation_settings**
> TenantUserInvitationSettingsWrapper get_tenant_user_invitation_settings()

Returns whether the portal currently allows inviting new members and new guests at all. No permission is
required; anonymous callers can read it too, since the invitation flow itself may run before the caller has
signed in. This is a read-only, idempotent call. The response supports conditional requests: send the standard
If-Modified-Since header with the previous `lastModified` value, and an unchanged response comes back empty
instead of resending the same settings.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**TenantUserInvitationSettingsWrapper**](TenantUserInvitationSettingsWrapper.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.tenant_user_invitation_settings_wrapper import TenantUserInvitationSettingsWrapper
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
    api_instance = docspace_api_sdk.CommonSettingsApi(api_client)

    try:
        # Get the user invitation settings
        api_response = api_instance.get_tenant_user_invitation_settings()
        print("The response of CommonSettingsApi->get_tenant_user_invitation_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonSettingsApi->get_tenant_user_invitation_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Whether inviting new members and new guests is currently allowed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_zones**
> TimezonesRequestsArrayWrapper get_time_zones()

Returns every time zone known to the host machine, each with its IANA identifier and a human-readable display
name, ordered from the most negative to the most positive UTC offset. This call is not for a normal logged-in
session: it requires a confirmation link bearing the Wizard or Administrators claim, of the kind generated
during initial portal setup or issued by an administrator, and the link is consumed as part of authenticating
the request. This is a read-only, idempotent call, and the list is not paginated. Use the returned `id` values
wherever the portal expects a time zone identifier; an unrecognized value is rejected there, not here.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**TimezonesRequestsArrayWrapper**](TimezonesRequestsArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.timezones_requests_array_wrapper import TimezonesRequestsArrayWrapper
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
    api_instance = docspace_api_sdk.CommonSettingsApi(api_client)

    try:
        # Get time zones
        api_response = api_instance.get_time_zones()
        print("The response of CommonSettingsApi->get_time_zones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonSettingsApi->get_time_zones: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Every time zone known to the host, with its IANA ID and display name |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_default_folder**
> StudioDefaultPageSettingsWrapper save_default_folder(default_product_request_dto=default_product_request_dto)

Sets which folder the current user's account opens into by default, such as My Documents, the rooms list, or
favorites. Requires an authenticated session; every role may set its own default, and the change never affects
any other user. Only folder types the client actually offers as a landing page are accepted; picking My
Documents (`USER`) as a Guest is rejected too, since guests have no personal storage. This is a mutating,
idempotent call. It returns the saved setting.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **default_product_request_dto** | [**DefaultProductRequestDto**](DefaultProductRequestDto.md)|  | [optional] 

### Return type

[**StudioDefaultPageSettingsWrapper**](StudioDefaultPageSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.default_product_request_dto import DefaultProductRequestDto
from docspace_api_sdk.models.studio_default_page_settings_wrapper import StudioDefaultPageSettingsWrapper
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
    api_instance = docspace_api_sdk.CommonSettingsApi(api_client)
    default_product_request_dto = docspace_api_sdk.DefaultProductRequestDto() # DefaultProductRequestDto |  (optional)

    try:
        # Set the default folder
        api_response = api_instance.save_default_folder(default_product_request_dto=default_product_request_dto)
        print("The response of CommonSettingsApi->save_default_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonSettingsApi->save_default_folder: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Saved default folder setting for the current user |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_dns_settings**
> StringWrapper save_dns_settings(dns_settings_requests_dto=dns_settings_requests_dto)

Maps a custom domain name onto the current tenant, or clears the mapping, so the portal becomes reachable
under the caller's own DNS name instead of only its default alias. Available only on a Standalone
(self-hosted) installation; on SaaS the call is always refused. Requires Owner or DocSpaceAdmin (the
EditPortalSettings permission). Disable the mapping by passing `enable=false`, in which case the domain name
in the request is ignored. A domain that collides with the portal's reserved base domain, or otherwise fails
validation, is rejected without changing the current mapping. This is a mutating, idempotent call. On success
the previous domain also stops answering, and any CSP configuration referencing it is updated to the new one.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dns_settings_requests_dto** | [**DnsSettingsRequestsDto**](DnsSettingsRequestsDto.md)|  | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.dns_settings_requests_dto import DnsSettingsRequestsDto
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
    api_instance = docspace_api_sdk.CommonSettingsApi(api_client)
    dns_settings_requests_dto = docspace_api_sdk.DnsSettingsRequestsDto() # DnsSettingsRequestsDto |  (optional)

    try:
        # Save the DNS settings
        api_response = api_instance.save_dns_settings(dns_settings_requests_dto=dns_settings_requests_dto)
        print("The response of CommonSettingsApi->save_dns_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonSettingsApi->save_dns_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirmation that the DNS mapping was updated |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The domain name is invalid, or collides with the portal's reserved base domain |  -  |
**402** | This option is not available under the portal's current pricing plan |  -  |
**405** | The portal is not a Standalone installation, so a custom domain cannot be mapped |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_mail_domain_settings**
> StringWrapper save_mail_domain_settings(mail_domain_settings_requests_dto=mail_domain_settings_requests_dto)

Overwrites the portal's trusted mail domain configuration, which controls which email domains are treated as
already verified when a user is invited or self-registers. Requires Owner or DocSpaceAdmin (the
EditPortalSettings permission). When the requested mode is a custom domain list, every domain is normalized to
lowercase and checked against the expected hostname format; a domain that fails the check, or an empty custom
list, causes the whole call to be rejected without saving anything. For the other modes the domain list in the
request is ignored. The `inviteUsersAsVisitors` flag controls whether users who join through a trusted domain
are added as full members or as visitors, and takes effect on the next join rather than retroactively. This is
a mutating, idempotent call: repeating it with the same body leaves the portal in the same state. On success
it returns a confirmation message, not the saved settings themselves; read them back from
`GET api/2.0/settings`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_domain_settings_requests_dto** | [**MailDomainSettingsRequestsDto**](MailDomainSettingsRequestsDto.md)|  | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.mail_domain_settings_requests_dto import MailDomainSettingsRequestsDto
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
    api_instance = docspace_api_sdk.CommonSettingsApi(api_client)
    mail_domain_settings_requests_dto = docspace_api_sdk.MailDomainSettingsRequestsDto() # MailDomainSettingsRequestsDto |  (optional)

    try:
        # Save the mail domain settings
        api_response = api_instance.save_mail_domain_settings(mail_domain_settings_requests_dto=mail_domain_settings_requests_dto)
        print("The response of CommonSettingsApi->save_mail_domain_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonSettingsApi->save_mail_domain_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirmation message that the trusted mail domain settings were saved |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_portal_color_theme**
> CustomColorThemesSettingsWrapper save_portal_color_theme(custom_color_themes_settings_requests_dto=custom_color_themes_settings_requests_dto)

Adds or updates a custom color theme, or changes which theme is selected, for the whole portal. Requires Owner
or DocSpaceAdmin (the EditPortalSettings permission). Pass `theme` to create or edit one: an existing theme is
matched and updated by its ID, a new one is appended, and an ID that collides with a built-in default theme is
treated as a request to create a new custom theme instead of overwriting the default. Once the plan's
custom-theme limit is reached, a new theme is silently not added rather than rejected with an error, so check
the returned `themes` count against `limit` before assuming it was saved. Pass `selected` to switch the active
theme; an ID that does not match any existing theme is ignored. This is a mutating call, not strictly
idempotent once the limit has been reached. It returns the full updated theme configuration.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_color_themes_settings_requests_dto** | [**CustomColorThemesSettingsRequestsDto**](CustomColorThemesSettingsRequestsDto.md)|  | [optional] 

### Return type

[**CustomColorThemesSettingsWrapper**](CustomColorThemesSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.custom_color_themes_settings_requests_dto import CustomColorThemesSettingsRequestsDto
from docspace_api_sdk.models.custom_color_themes_settings_wrapper import CustomColorThemesSettingsWrapper
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
    api_instance = docspace_api_sdk.CommonSettingsApi(api_client)
    custom_color_themes_settings_requests_dto = docspace_api_sdk.CustomColorThemesSettingsRequestsDto() # CustomColorThemesSettingsRequestsDto |  (optional)

    try:
        # Save a color theme
        api_response = api_instance.save_portal_color_theme(custom_color_themes_settings_requests_dto=custom_color_themes_settings_requests_dto)
        print("The response of CommonSettingsApi->save_portal_color_theme:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonSettingsApi->save_portal_color_theme: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated color theme configuration: saved themes, selected theme, and plan limit |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_tenant_ai_access_settings**
> TenantAiAccessSettingsWrapper set_tenant_ai_access_settings(tenant_ai_access_settings_dto=tenant_ai_access_settings_dto)

Turns AI functionality (chat, agents, vectorization) on or off for the whole portal; AI is enabled by default.
Requires Owner or DocSpaceAdmin (the EditPortalSettings permission); every other caller is refused. Disabling
it immediately hides the AI Agents folder from root folder listings, makes AI status checks report disabled,
and makes AI chat endpoints unreachable for every user on the tenant, not only the caller. This is a mutating,
idempotent, portal-wide call, and the change is pushed to already-connected clients over the real-time
notification hub rather than waiting for their next request. It returns the saved setting.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_ai_access_settings_dto** | [**TenantAiAccessSettingsDto**](TenantAiAccessSettingsDto.md)|  | [optional] 

### Return type

[**TenantAiAccessSettingsWrapper**](TenantAiAccessSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.tenant_ai_access_settings_dto import TenantAiAccessSettingsDto
from docspace_api_sdk.models.tenant_ai_access_settings_wrapper import TenantAiAccessSettingsWrapper
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
    api_instance = docspace_api_sdk.CommonSettingsApi(api_client)
    tenant_ai_access_settings_dto = docspace_api_sdk.TenantAiAccessSettingsDto() # TenantAiAccessSettingsDto |  (optional)

    try:
        # Set the AI access settings
        api_response = api_instance.set_tenant_ai_access_settings(tenant_ai_access_settings_dto=tenant_ai_access_settings_dto)
        print("The response of CommonSettingsApi->set_tenant_ai_access_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonSettingsApi->set_tenant_ai_access_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Saved AI access setting for the portal |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator, so the AI access setting cannot be changed |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_activation_settings**
> EmailActivationSettingsWrapper update_email_activation_settings(email_activation_settings=email_activation_settings)

Updates the current user's own preference for whether the email confirmation prompt is displayed on their
account. Requires an authenticated session; every role may change its own setting, and the change never
affects any other user. This is a mutating, idempotent call. It returns the settings exactly as submitted,
without validating them against the account's actual email confirmation state, so `show` can be set to `true`
even after the address is already confirmed.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_activation_settings** | [**EmailActivationSettings**](EmailActivationSettings.md)|  | [optional] 

### Return type

[**EmailActivationSettingsWrapper**](EmailActivationSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.email_activation_settings import EmailActivationSettings
from docspace_api_sdk.models.email_activation_settings_wrapper import EmailActivationSettingsWrapper
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
    api_instance = docspace_api_sdk.CommonSettingsApi(api_client)
    email_activation_settings = docspace_api_sdk.EmailActivationSettings() # EmailActivationSettings |  (optional)

    try:
        # Update the email activation settings
        api_response = api_instance.update_email_activation_settings(email_activation_settings=email_activation_settings)
        print("The response of CommonSettingsApi->update_email_activation_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonSettingsApi->update_email_activation_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Email activation settings exactly as submitted |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invitation_settings**
> TenantUserInvitationSettingsWrapper update_invitation_settings(tenant_user_invitation_settings_request_dto=tenant_user_invitation_settings_request_dto)

Sets whether the portal allows inviting new members and new guests. Requires Owner or DocSpaceAdmin (the
EditPortalSettings permission). Disabling member or guest invitations only blocks creating new invitations
going forward; it does not revoke links already issued or remove members already invited. This is a mutating,
idempotent, portal-wide call. It returns the saved setting; read the current value at any time, including
anonymously, from `GET api/2.0/settings/invitationsettings`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_user_invitation_settings_request_dto** | [**TenantUserInvitationSettingsRequestDto**](TenantUserInvitationSettingsRequestDto.md)|  | [optional] 

### Return type

[**TenantUserInvitationSettingsWrapper**](TenantUserInvitationSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.tenant_user_invitation_settings_request_dto import TenantUserInvitationSettingsRequestDto
from docspace_api_sdk.models.tenant_user_invitation_settings_wrapper import TenantUserInvitationSettingsWrapper
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
    api_instance = docspace_api_sdk.CommonSettingsApi(api_client)
    tenant_user_invitation_settings_request_dto = docspace_api_sdk.TenantUserInvitationSettingsRequestDto() # TenantUserInvitationSettingsRequestDto |  (optional)

    try:
        # Update the user invitation settings
        api_response = api_instance.update_invitation_settings(tenant_user_invitation_settings_request_dto=tenant_user_invitation_settings_request_dto)
        print("The response of CommonSettingsApi->update_invitation_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonSettingsApi->update_invitation_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Saved user invitation settings |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

