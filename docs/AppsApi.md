# docspace_api_sdk.AppsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](#get) | **GET** /api/2.0/apps/{id} | Get an app
[**get_all**](#get_all) | **GET** /api/2.0/apps | Get all apps
[**get_settings**](#get_settings) | **GET** /api/2.0/apps/{id}/settings | Get app settings
[**set_enabled**](#set_enabled) | **PUT** /api/2.0/apps/{id}/enabled | Enable or disable an app
[**set_settings**](#set_settings) | **PUT** /api/2.0/apps/{id}/settings | Save app settings


# **get**
> AppWrapper get(id)

Returns one portal application by its identifier - one of the feature modules the portal can turn on, such as
`ai-rooms` or `docs-cloud` - with the enabled state and the settings document stored for the current portal.
The identifier must be an application declared in the installation configuration: take it
from `GET api/2.0/apps`, because an unknown identifier is rejected instead of creating anything. Any
authenticated portal member may read it. The call is read-only and idempotent. The result carries the
identifier, the enabled flag of the current portal and the settings JSON document, which is empty while the
portal has never saved settings for this application. An application that is not configured on this
installation fails with 404, so this is also the way to find out whether an application exists here at all.
Use `GET api/2.0/apps` to read all applications in one call, or `GET api/2.0/apps/{id}/settings` when only the
settings document is needed.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The application to read, by the identifier `GET api/2.0/apps` reports - one of the feature modules the portal  can turn on, such as `ai-room` or `docs-cloud`. An identifier not declared in the installation configuration  answers 404, which is also how a caller learns that an application does not exist here. | 

### Return type

[**AppWrapper**](AppWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.app_wrapper import AppWrapper
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
    api_instance = docspace_api_sdk.AppsApi(api_client)
    id = 'ai-room' # str | The application to read, by the identifier `GET api/2.0/apps` reports - one of the feature modules the portal  can turn on, such as `ai-room` or `docs-cloud`. An identifier not declared in the installation configuration  answers 404, which is also how a caller learns that an application does not exist here.

    try:
        # Get an app
        api_response = api_instance.get(id)
        print("The response of AppsApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The application with the enabled state and the settings of the current portal |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | No application with this identifier is configured on this installation |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all**
> AppArrayWrapper get_all()

Returns every portal application available on this installation, each with the state it has for the current
portal: the feature modules the portal can turn on and configure, such as `ai-rooms` or `docs-cloud`. The set
of applications and their initial enabled state come from the installation configuration and cannot be changed
through the API; only the enabled flag and the settings document are stored per portal, by
`PUT api/2.0/apps/{id}/enabled` and `PUT api/2.0/apps/{id}/settings`. Any authenticated portal member may read
the list. The call is read-only and idempotent. The list follows the order of the configuration, and every item
carries the application identifier, whether the application is enabled for the current portal, and the settings
JSON document saved for it, which is empty while the portal has never saved one. An empty list means that no
applications are configured on this installation, not that they are all disabled. There is neither paging nor
filtering here: to read a single application use `GET api/2.0/apps/{id}`.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**AppArrayWrapper**](AppArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.app_array_wrapper import AppArrayWrapper
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
    api_instance = docspace_api_sdk.AppsApi(api_client)

    try:
        # Get all apps
        api_response = api_instance.get_all()
        print("The response of AppsApi->get_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_all: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The portal applications configured on this installation, each with the enabled state and the settings of the current portal |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> UnknownNullableWrapper get_settings(id)

Returns only the settings document of one portal application, such as `ai-rooms` or `docs-cloud`: the JSON
that the current portal has saved for it through `PUT api/2.0/apps/{id}/settings`, with no wrapper around it.
The identifier must be an application declared in the installation configuration, as listed by
`GET api/2.0/apps`. Any authenticated portal member
may read it. The call is read-only and idempotent. The document comes back exactly as it was saved: its shape
is defined by the application itself and is not validated by the portal, and an empty result means that the
portal has never saved settings for this application, so the application uses its own defaults. The enabled
state is not part of the answer: read it from `GET api/2.0/apps/{id}`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The application to read, by the identifier `GET api/2.0/apps` reports - one of the feature modules the portal  can turn on, such as `ai-room` or `docs-cloud`. An identifier not declared in the installation configuration  answers 404, which is also how a caller learns that an application does not exist here. | 

### Return type

[**UnknownNullableWrapper**](UnknownNullableWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.unknown_nullable_wrapper import UnknownNullableWrapper
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
    api_instance = docspace_api_sdk.AppsApi(api_client)
    id = 'ai-room' # str | The application to read, by the identifier `GET api/2.0/apps` reports - one of the feature modules the portal  can turn on, such as `ai-room` or `docs-cloud`. An identifier not declared in the installation configuration  answers 404, which is also how a caller learns that an application does not exist here.

    try:
        # Get app settings
        api_response = api_instance.get_settings(id)
        print("The response of AppsApi->get_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The settings document saved for the application, or an empty result if the portal has never saved one |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | No application with this identifier is configured on this installation |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_enabled**
> AppWrapper set_enabled(id, set_app_enabled_body)

Turns one portal application on or off for the current portal, and notifies the clients connected to the portal
so that they can show or hide it without being reloaded. The identifier must be an application declared in the
installation configuration, as listed by `GET api/2.0/apps`. The caller must be a portal administrator allowed
to edit the portal settings. The call is mutating and idempotent: it stores the flag for this portal, overriding
the default that the configuration gives the application, and repeating it with the same value changes nothing.
Disabling an application does not delete its settings document, which stays saved and applies again as soon as
the application is enabled. The response is the application in its new state, including that settings document.
Only the enabled flag is affected here: to change the settings document use `PUT api/2.0/apps/{id}/settings`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The application to switch, by the identifier `GET api/2.0/apps` reports. It has to be an application declared  in the installation configuration; an unknown identifier answers 404 rather than creating anything. | 
 **set_app_enabled_body** | [**SetAppEnabledBody**](SetAppEnabledBody.md)| The new state of the application. Only the enabled flag travels here; the settings document is changed  through `PUT api/2.0/apps/{id}/settings`. | 

### Return type

[**AppWrapper**](AppWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.app_wrapper import AppWrapper
from docspace_api_sdk.models.set_app_enabled_body import SetAppEnabledBody
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
    api_instance = docspace_api_sdk.AppsApi(api_client)
    id = 'ai-room' # str | The application to switch, by the identifier `GET api/2.0/apps` reports. It has to be an application declared  in the installation configuration; an unknown identifier answers 404 rather than creating anything.
    set_app_enabled_body = docspace_api_sdk.SetAppEnabledBody() # SetAppEnabledBody | The new state of the application. Only the enabled flag travels here; the settings document is changed  through `PUT api/2.0/apps/{id}/settings`.

    try:
        # Enable or disable an app
        api_response = api_instance.set_enabled(id, set_app_enabled_body)
        print("The response of AppsApi->set_enabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->set_enabled: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The application in its new state, with the saved settings document left untouched |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not allowed to edit the portal settings |  -  |
**404** | No application with this identifier is configured on this installation |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_settings**
> AppWrapper set_settings(id, set_app_settings_body)

Stores the application-specific settings document of one portal application for the current portal. The
identifier must be an application declared in the installation configuration, as listed by `GET api/2.0/apps`.
The caller must be a portal administrator allowed to edit the portal settings. The call is mutating and
idempotent, and it replaces the whole document instead of merging into it: read the current one with
`GET api/2.0/apps/{id}/settings`, change it and send it back complete, or send `null` to drop the saved document
and let the application fall back to its own defaults. Any valid JSON value is accepted, since the content is
stored as it is and is interpreted by the application rather than by the portal, while a body that is not valid
JSON fails with 400 and stores nothing. The response is the application in its new state, with the stored
document echoed back. Unlike `PUT api/2.0/apps/{id}/enabled`, this operation sends no notification to the
connected clients, which pick the new settings up on their next read.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The application whose configuration is stored, by the identifier `GET api/2.0/apps` reports. An identifier  not declared in the installation configuration answers 404. | 
 **set_app_settings_body** | [**SetAppSettingsBody**](SetAppSettingsBody.md)| The configuration to store for this portal, replacing whatever was stored before. | 

### Return type

[**AppWrapper**](AppWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.app_wrapper import AppWrapper
from docspace_api_sdk.models.set_app_settings_body import SetAppSettingsBody
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
    api_instance = docspace_api_sdk.AppsApi(api_client)
    id = 'ai-room' # str | The application whose configuration is stored, by the identifier `GET api/2.0/apps` reports. An identifier  not declared in the installation configuration answers 404.
    set_app_settings_body = docspace_api_sdk.SetAppSettingsBody() # SetAppSettingsBody | The configuration to store for this portal, replacing whatever was stored before.

    try:
        # Save app settings
        api_response = api_instance.set_settings(id, set_app_settings_body)
        print("The response of AppsApi->set_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->set_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The application in its new state, with the stored settings document |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The request body is not a valid JSON document, so no settings are stored |  -  |
**403** | The caller is not allowed to edit the portal settings |  -  |
**404** | No application with this identifier is configured on this installation |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

