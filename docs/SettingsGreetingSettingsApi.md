# docspace_api_sdk.GreetingSettingsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_greeting_settings**](#get_greeting_settings) | **GET** /api/2.0/settings/greetingsettings | Get greeting settings
[**get_is_default_greeting_settings**](#get_is_default_greeting_settings) | **GET** /api/2.0/settings/greetingsettings/isdefault | Check the default greeting settings
[**restore_greeting_settings**](#restore_greeting_settings) | **POST** /api/2.0/settings/greetingsettings/restore | Restore the greeting settings
[**save_greeting_settings**](#save_greeting_settings) | **POST** /api/2.0/settings/greetingsettings | Save the greeting settings


# **get_greeting_settings**
> StringWrapper get_greeting_settings()

Returns the greeting title of the current portal - the caption shown as the welcome heading on the sign-in
page, kept as the portal name. Any authenticated user may call it and no administrative right is needed; the
call is read-only. The title comes back as a bare string and is never empty: when the portal has no title of
its own, the built-in default caption is returned instead, localized to the caller's language. Because of that
fallback this operation cannot tell a saved title from the default one - call
`GET api/2.0/settings/greetingsettings/isdefault` when that distinction matters. The same string is part of
the portal settings answer as the `greetingSettings` field of `GET api/2.0/settings`, so a client that already
reads the settings needs no separate call. The value is a caption only: it is neither the portal address nor
the white-label logo text of the header, which is returned by `GET api/2.0/settings/whitelabel/logotext`.

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
    api_instance = docspace_api_sdk.GreetingSettingsApi(api_client)

    try:
        # Get greeting settings
        api_response = api_instance.get_greeting_settings()
        print("The response of GreetingSettingsApi->get_greeting_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GreetingSettingsApi->get_greeting_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The greeting title of the portal, or the localized default caption when the portal has no title of its own |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_is_default_greeting_settings**
> BooleanWrapper get_is_default_greeting_settings()

Reports whether the current portal still shows the built-in greeting caption instead of a title of its own.
The check is read-only and open to any authenticated user, with no administrative right required. It answers
`true` while no title is stored for the portal - the state after
`POST api/2.0/settings/greetingsettings/restore` on an installation that configures no portal name, and also
after saving an empty `title` - and `false` as soon as a non-empty title has been saved. Use it together with
`GET api/2.0/settings/greetingsettings`: that operation substitutes the localized default caption for a
missing title, so only these two calls together separate a default greeting from a custom one that happens to
repeat the default wording. The answer covers the greeting title alone; whether the white-label logos and logo
text are still the default ones is reported by `GET api/2.0/settings/whitelabel/logos/isdefault` and
`GET api/2.0/settings/whitelabel/logotext/isdefault`.

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
    api_instance = docspace_api_sdk.GreetingSettingsApi(api_client)

    try:
        # Check the default greeting settings
        api_response = api_instance.get_is_default_greeting_settings()
        print("The response of GreetingSettingsApi->get_is_default_greeting_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GreetingSettingsApi->get_is_default_greeting_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the portal has no greeting title of its own and the built-in default caption is shown |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_greeting_settings**
> StringWrapper restore_greeting_settings()

Drops the custom greeting title of the current portal and puts back the title configured for the installation,
which is an empty value unless the installation defines a portal name of its own. The caller needs the
portal-settings right of a DocSpace administrator, otherwise the call is refused. The change is immediate for
every user of the portal and a second call changes nothing, so a retry after a failed attempt is safe. The
answer is the greeting in force afterwards: the configured title when there is one, and the localized default
caption when the stored title ends up empty - in that case `GET api/2.0/settings/greetingsettings/isdefault`
starts answering `true`. Only the caption is touched: the portal logos and the white-label logo text keep
their values and are reset separately by `PUT api/2.0/settings/whitelabel/logos/restore` and
`PUT api/2.0/settings/whitelabel/logotext/restore`. To set a title instead of the default one use
`POST api/2.0/settings/greetingsettings`.

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
    api_instance = docspace_api_sdk.GreetingSettingsApi(api_client)

    try:
        # Restore the greeting settings
        api_response = api_instance.restore_greeting_settings()
        print("The response of GreetingSettingsApi->restore_greeting_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GreetingSettingsApi->restore_greeting_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The greeting title in force after the restore, or the localized default caption when the installation configures none |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_greeting_settings**
> StringWrapper save_greeting_settings(greeting_settings_requests_dto=greeting_settings_requests_dto)

Replaces the greeting title of the current portal with the `title` from the request, storing it as the portal
name. The caller needs the portal-settings right of a DocSpace administrator, otherwise the call is refused.
The new caption takes effect at once for every user of the portal and the change is written to the audit
trail; repeating the call with the same title leaves the portal in the same state. A missing `title` or one
longer than 255 characters is rejected as an invalid request before the handler runs. On a cloud portal with a
free or trial plan the title is also matched against the character rule configured for the installation and a
title that breaks it is refused, while a paid cloud plan and a server installation apply no character check.
An empty `title` clears the greeting: the portal falls back to the built-in default caption and
`GET api/2.0/settings/greetingsettings/isdefault` starts answering `true`. What comes back is a localized
confirmation message, not the stored title - read the title with `GET api/2.0/settings/greetingsettings`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **greeting_settings_requests_dto** | [**GreetingSettingsRequestsDto**](GreetingSettingsRequestsDto.md)|  | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.greeting_settings_requests_dto import GreetingSettingsRequestsDto
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
    api_instance = docspace_api_sdk.GreetingSettingsApi(api_client)
    greeting_settings_requests_dto = docspace_api_sdk.GreetingSettingsRequestsDto() # GreetingSettingsRequestsDto |  (optional)

    try:
        # Save the greeting settings
        api_response = api_instance.save_greeting_settings(greeting_settings_requests_dto=greeting_settings_requests_dto)
        print("The response of GreetingSettingsApi->save_greeting_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GreetingSettingsApi->save_greeting_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A localized message confirming that the greeting title has been saved |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

