# docspace_api_sdk.ModuleEventsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_module_event**](#send_module_event) | **POST** /api/2.0/portal/moduleevents | Send a module event


# **send_module_event**
> send_module_event(x_module_key=x_module_key, send_module_event_request=send_module_event_request)

Delivers one event from an integration module to the browsers of the portal named by the request host, over
the socket connection every open DocSpace page already keeps. No user session is needed: the caller
identifies itself with the module key in the `X-Module-Key` header, which the installation administrator
issues and allows for a list of portals. Set exactly one addressee - `user`, the e-mail of a portal user,
reaches only that user's open sessions without any subscription, and `room` reaches everyone in the portal
subscribed to `plugin-{module}-{room}`. Browsers receive `plugin:{module}:{event}` with `{ message }`, the
module name taken from the key, never from the body. The call only hands the event over: nothing is stored,
a user with no open session never sees it, and a repeated call delivers it again. Keep `message` a signal to
re-read, such as an unread count. The body is limited to 64 KB. A missing or unknown key fails with 401, a
portal the key is not allowed for with 403, an unknown or inactive user with 404, and invalid names or not
exactly one addressee with 400.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_module_key** | **str**| The secret key the installation administrator issued to the module. It is not a user or portal credential:  the module the event belongs to is the one this key is configured for, so the key is the module's identity. | [optional] 
 **send_module_event_request** | [**SendModuleEventRequest**](SendModuleEventRequest.md)| The event to deliver. | [optional] 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.send_module_event_request import SendModuleEventRequest
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
    api_instance = docspace_api_sdk.ModuleEventsApi(api_client)
    x_module_key = 'mk_Q2hhdE1vZHVsZUtleTIwMjYtMTAtMjM' # str | The secret key the installation administrator issued to the module. It is not a user or portal credential:  the module the event belongs to is the one this key is configured for, so the key is the module's identity. (optional)
    send_module_event_request = docspace_api_sdk.SendModuleEventRequest() # SendModuleEventRequest | The event to deliver. (optional)

    try:
        # Send a module event
        api_instance.send_module_event(x_module_key=x_module_key, send_module_event_request=send_module_event_request)
    except Exception as e:
        print("Exception when calling ModuleEventsApi->send_module_event: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The event was handed to the socket service for delivery |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The body is missing, the event or room name is invalid, or there is not exactly one addressee |  -  |
**401** | The X-Module-Key header is missing or matches no configured module |  -  |
**402** | The portal's payment has lapsed |  -  |
**403** | The module key is not allowed for this portal |  -  |
**404** | No active user of this portal has the given e-mail |  -  |
**413** | The body is larger than 64 KB |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

