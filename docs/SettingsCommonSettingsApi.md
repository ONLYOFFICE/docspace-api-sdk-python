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
[**get_portal_hostname**](#get_portal_hostname) | **GET** /api/2.0/settings/machine | Get hostname
[**get_portal_logo**](#get_portal_logo) | **GET** /api/2.0/settings/logo | Get a portal logo
[**get_portal_settings**](#get_portal_settings) | **GET** /api/2.0/settings | Get the portal settings
[**get_socket_settings**](#get_socket_settings) | **GET** /api/2.0/settings/socket | Get the socket settings
[**get_supported_cultures**](#get_supported_cultures) | **GET** /api/2.0/settings/cultures | Get supported languages
[**get_tenant_user_invitation_settings**](#get_tenant_user_invitation_settings) | **GET** /api/2.0/settings/invitationsettings | Get the user invitation settings
[**get_time_zones**](#get_time_zones) | **GET** /api/2.0/settings/timezones | Get time zones
[**save_dns_settings**](#save_dns_settings) | **PUT** /api/2.0/settings/dns | Save the DNS settings
[**save_mail_domain_settings**](#save_mail_domain_settings) | **POST** /api/2.0/settings/maildomainsettings | Save the mail domain settings
[**save_portal_color_theme**](#save_portal_color_theme) | **PUT** /api/2.0/settings/colortheme | Save a color theme
[**update_email_activation_settings**](#update_email_activation_settings) | **PUT** /api/2.0/settings/emailactivation | Update the email activation settings
[**update_invitation_settings**](#update_invitation_settings) | **PUT** /api/2.0/settings/invitationsettings | Update user invitation settings


# **close_admin_helper**
> close_admin_helper()

Closes the administrator helper notification.

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
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Unauthorized |  -  |
**405** | Not available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_wizard**
> WizardSettingsWrapper complete_wizard(wizard_requests_dto=wizard_requests_dto)

Completes the Wizard settings.

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
**200** | Wizard settings |  -  |
**400** | Incorrect email address/The password is empty |  -  |
**401** | Unauthorized |  -  |
**402** | You must enter a license key or license key is not correct or license expired or user quota does not match the license |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configure_deep_link**
> TenantDeepLinkSettingsWrapper configure_deep_link(deep_link_configuration_requests_dto=deep_link_configuration_requests_dto)

Saves the deep link configuration settings for the portal.

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
**200** | Deep link configuration updated |  -  |
**400** | Invalid deep link configuration |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_portal_color_theme**
> CustomColorThemesSettingsWrapper delete_portal_color_theme(id)

Deletes the portal color theme with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the portal theme to delete. | 

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
    id = 9846 # int | The ID of the portal theme to delete.

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
**200** | Portal theme settings: custom color theme settings, selected or not, limit |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deep_link_settings**
> TenantDeepLinkSettingsWrapper get_deep_link_settings()

Returns the deep link settings.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**TenantDeepLinkSettingsWrapper**](TenantDeepLinkSettingsWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.tenant_deep_link_settings_wrapper import TenantDeepLinkSettingsWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
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
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_settings**
> PaymentSettingsWrapper get_payment_settings()

Returns the portal payment settings.

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
**200** | Payment settings: sales email, feedback and support URL, link to pay for a portal, Standalone or not, current license, maximum quota quantity |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portal_color_theme**
> CustomColorThemesSettingsWrapper get_portal_color_theme()

Returns the portal color theme.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**CustomColorThemesSettingsWrapper**](CustomColorThemesSettingsWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.custom_color_themes_settings_wrapper import CustomColorThemesSettingsWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
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
**200** | Settings of the portal themes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portal_hostname**
> ObjectWrapper get_portal_hostname()

Returns the portal hostname.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**ObjectWrapper**](ObjectWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.object_wrapper import ObjectWrapper
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
        # Get hostname
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
**200** | Portal hostname |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portal_logo**
> StringWrapper get_portal_logo()

Returns the portal logo image URL.

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
**200** | Portal logo image URL |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portal_settings**
> SettingsWrapper get_portal_settings(withpassword=withpassword)

Returns a list of all the available portal settings with the current values for each parameter.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **withpassword** | **bool**| Specifies whether to include the password hashing configuration in the response. | [optional] 

### Return type

[**SettingsWrapper**](SettingsWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.settings_wrapper import SettingsWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.CommonSettingsApi(api_client)
    withpassword = true # bool | Specifies whether to include the password hashing configuration in the response. (optional)

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
**200** | Settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_socket_settings**
> ObjectWrapper get_socket_settings()

Returns the socket settings.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**ObjectWrapper**](ObjectWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.object_wrapper import ObjectWrapper
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
**200** | Socket settings: hub URL |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_cultures**
> STRINGArrayWrapper get_supported_cultures()

Returns a list of all the available portal languages in the format of a two-letter or four-letter language code (e.g. de, en-US, etc.).

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**STRINGArrayWrapper**](STRINGArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.string_array_wrapper import STRINGArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
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
**200** | List of all the available portal languages |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_user_invitation_settings**
> TenantUserInvitationSettingsWrapper get_tenant_user_invitation_settings()

Returns the portal user invitation settings.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**TenantUserInvitationSettingsWrapper**](TenantUserInvitationSettingsWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.tenant_user_invitation_settings_wrapper import TenantUserInvitationSettingsWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
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
**200** | portal user invitation settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_zones**
> TimezonesRequestsArrayWrapper get_time_zones()

Returns a list of all the available portal time zones.

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
**200** | List of all the available time zones with their IDs and display names |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_dns_settings**
> StringWrapper save_dns_settings(dns_settings_requests_dto=dns_settings_requests_dto)

Saves the DNS settings specified in the request to the current portal.

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
**200** | Message about changing DNS |  -  |
**400** | Invalid domain name/incorrect length of doman name |  -  |
**401** | Unauthorized |  -  |
**402** | Your pricing plan does not support this option |  -  |
**405** | Method not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_mail_domain_settings**
> StringWrapper save_mail_domain_settings(mail_domain_settings_requests_dto=mail_domain_settings_requests_dto)

Saves the mail domain settings specified in the request to the portal.

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
**200** | Message about the result of saving the mail domain settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_portal_color_theme**
> CustomColorThemesSettingsWrapper save_portal_color_theme(custom_color_themes_settings_requests_dto=custom_color_themes_settings_requests_dto)

Saves the portal color theme specified in the request.

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
**200** | Portal theme settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_activation_settings**
> EmailActivationSettingsWrapper update_email_activation_settings(email_activation_settings=email_activation_settings)

Updates the email activation settings.

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
**200** | Updated email activation settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invitation_settings**
> TenantUserInvitationSettingsWrapper update_invitation_settings(tenant_user_invitation_settings_request_dto=tenant_user_invitation_settings_request_dto)

Updates the portal user invitation settings.

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
        # Update user invitation settings
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
**200** | Updated user invitation settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

