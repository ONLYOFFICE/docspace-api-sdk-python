# docspace_api_sdk.TelegramApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_telegram**](#check_telegram) | **GET** /api/2.0/settings/telegram/check | Check the Telegram connection
[**link_telegram**](#link_telegram) | **GET** /api/2.0/settings/telegram/link | Get the Telegram link
[**unlink_telegram**](#unlink_telegram) | **DELETE** /api/2.0/settings/telegram/link | Unlink Telegram


# **check_telegram**
> TelegramStatusWrapper check_telegram()

Reports whether the current user's account is linked to the portal's Telegram bot, and under which Telegram
username. The bot keys must be configured for the portal beforehand with `POST api/2.0/settings/authservice`;
until a bot is configured, linking cannot be completed and the status never reaches the linked state. Any
authenticated user may call it, and only for their own account: there is no way to read another member's
Telegram status. This is a read-only, idempotent call. The returned `status` is published as a number, where
`0` means the account is not linked, `1` means it is linked, and `2` means a registration link has been issued
and the portal is still waiting for the user to open it in Telegram. The `username` field is filled in only in
state `1` and comes back empty in the other two. Start or resume linking with
`GET api/2.0/settings/telegram/link`, and drop an established link with
`DELETE api/2.0/settings/telegram/link`.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**TelegramStatusWrapper**](TelegramStatusWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.telegram_status_wrapper import TelegramStatusWrapper
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
    api_instance = docspace_api_sdk.TelegramApi(api_client)

    try:
        # Check the Telegram connection
        api_response = api_instance.check_telegram()
        print("The response of TelegramApi->check_telegram:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TelegramApi->check_telegram: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current user's Telegram link state, with the username filled in only when linked |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_telegram**
> StringWrapper link_telegram()

Returns the personal `t.me` deep link that connects the current user's account to the portal's Telegram bot,
so that notifications can be delivered to that user in Telegram. The bot keys must be configured for the
portal beforehand with `POST api/2.0/settings/authservice`; without a configured bot name the response comes
back empty. Any authenticated user may call it, and the link always belongs to the caller's own account. The
call mutates state: unless the user still has an outstanding registration token it issues a fresh one, so
calling it twice in a row hands back the same link instead of invalidating the first. That token is
short-lived (20 minutes with the default configuration), and once it has expired the operation has to be
called again for a new link. Linking itself is completed in Telegram, not here, so poll
`GET api/2.0/settings/telegram/check` until its `status` becomes `1`. Remove an established link with
`DELETE api/2.0/settings/telegram/link`.

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
    api_instance = docspace_api_sdk.TelegramApi(api_client)

    try:
        # Get the Telegram link
        api_response = api_instance.link_telegram()
        print("The response of TelegramApi->link_telegram:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TelegramApi->link_telegram: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A `t.me` deep link that connects the caller's account to the portal's Telegram bot |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_telegram**
> BooleanWrapper unlink_telegram()

Removes the link between the current user's account and the portal's Telegram bot, so that this user stops
receiving notifications in Telegram. Any authenticated user may call it, and only for their own account: one
member cannot unlink another. Nothing has to be linked beforehand, and the call is destructive but idempotent,
returning `true` both when a link was removed and when there was none to remove, so a retry after a timeout is
safe. Only the portal-side link is dropped: the chat itself stays in the user's Telegram, and the portal's bot
configuration is untouched, so the other members keep their own links. Re-linking is not automatic, request a
new link with `GET api/2.0/settings/telegram/link` and confirm the result with
`GET api/2.0/settings/telegram/check`. Delivery over the other notification channels is unaffected; the
channels enabled for the portal are listed by `GET api/2.0/settings/notification/channels`.

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
    api_instance = docspace_api_sdk.TelegramApi(api_client)

    try:
        # Unlink Telegram
        api_response = api_instance.unlink_telegram()
        print("The response of TelegramApi->unlink_telegram:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TelegramApi->unlink_telegram: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Always `true` once the caller has no link to the Telegram bot |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

