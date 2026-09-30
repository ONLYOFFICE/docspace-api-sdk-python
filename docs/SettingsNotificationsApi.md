# docspace_api_sdk.NotificationsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_notification_channels**](#get_notification_channels) | **GET** /api/2.0/settings/notification/channels | Get notification channels
[**get_notification_settings**](#get_notification_settings) | **GET** /api/2.0/settings/notification/{type} | Check notification availability
[**get_rooms_notification_settings**](#get_rooms_notification_settings) | **GET** /api/2.0/settings/notification/rooms | Get muted rooms
[**set_notification_settings**](#set_notification_settings) | **POST** /api/2.0/settings/notification | Set notification status
[**set_rooms_notification_status**](#set_rooms_notification_status) | **POST** /api/2.0/settings/notification/rooms | Mute or unmute a room


# **get_notification_channels**
> NotificationChannelStatusWrapper get_notification_channels()

Lists the ways this installation can deliver a notification, each as the internal name of the channel together
with `isEnabled`: `email.sender` for letters and `telegram.sender` for Telegram messages. The list describes
the installation and the portal rather than the calling user, so every member gets the same answer, and the
call is read-only. Any signed-in member may ask for it, whatever its role, and no permission is demanded. A
channel appears only when the notification service of the running installation is configured with a sender of
that name, so the list can be shorter than the two names above, and an empty list means that configuration
names no channel this build implements. `email.sender` is reported as enabled whenever it is listed, while
`telegram.sender` is reported as enabled only while the portal has a Telegram bot name and token stored, which
is what `POST api/2.0/settings/authservice` writes. An enabled channel says nothing about the caller: a member
also has to connect their own Telegram account, for which `GET api/2.0/settings/telegram/link` hands out the
link and `GET api/2.0/settings/telegram/check` reports the outcome. Which kinds of notification a member
receives is a separate setting, read with `GET api/2.0/settings/notification/{type}`.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**NotificationChannelStatusWrapper**](NotificationChannelStatusWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.notification_channel_status_wrapper import NotificationChannelStatusWrapper
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
    api_instance = docspace_api_sdk.NotificationsApi(api_client)

    try:
        # Get notification channels
        api_response = api_instance.get_notification_channels()
        print("The response of NotificationsApi->get_notification_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_notification_channels: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The notification channels this installation can deliver through, each with the flag that says whether it is enabled |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_settings**
> NotificationSettingsWrapper get_notification_settings(type)

Reports whether one kind of notification is switched on for the calling user, taking the kind as the integer
`type` in the route: 0 the new-item badges the Files responses carry, 1 the room activity letters, 2 the daily
feed digest, 3 the periodic tips letters. The answer describes the caller's own account only - there is no way
to read another member's settings - and the call is read-only and safe to repeat. Every signed-in member reads
its own settings: the portal owner, a DocSpace administrator, a room administrator, a user and a guest are all
accepted, and no permission is demanded. Badges come back switched on for an account that has not changed
them, while the kinds 1, 2 and 3 come back switched off until they are switched on with
`POST api/2.0/settings/notification`. What comes back is the kind that was asked for together with
`isEnabled`. A `type` outside 0-3 is not recognised and the call fails instead of falling back to a default.
The rooms silenced one by one are listed by `GET api/2.0/settings/notification/rooms`, and the delivery
channels of the installation by `GET api/2.0/settings/notification/channels`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**NotificationType**](.md)| The kind of notification being asked about. A value outside the defined set fails the call rather than  falling back to a default. | 

### Return type

[**NotificationSettingsWrapper**](NotificationSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.notification_settings_wrapper import NotificationSettingsWrapper
from docspace_api_sdk.models.notification_type import NotificationType
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
    api_instance = docspace_api_sdk.NotificationsApi(api_client)
    type = docspace_api_sdk.NotificationType() # NotificationType | The kind of notification being asked about. A value outside the defined set fails the call rather than  falling back to a default.

    try:
        # Check notification availability
        api_response = api_instance.get_notification_settings(type)
        print("The response of NotificationsApi->get_notification_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_notification_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The notification kind that was asked for together with the flag that says whether it is switched on for the calling user |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rooms_notification_settings**
> RoomsNotificationSettingsWrapper get_rooms_notification_settings()

Returns the rooms the calling user has silenced, as the `disabledRooms` list of their identifiers. The list
describes the caller's own account only, the call is read-only, and an empty list means nothing is silenced.
Every signed-in member reads its own list, whatever its role - owner, administrator, user or guest - and no
permission is demanded. The identifiers come back the way `POST api/2.0/settings/notification/rooms` stored
them, in the order they were added and without paging; they are kept as opaque values, so both the numeric
identifier of a portal room and the string identifier of a room on a connected third-party account appear
here, and an identifier stays in the list after the room itself is deleted. While a room is on this list its
activity is left out of the hourly room digest and of the daily feed, the letters that room would send at once
are not sent, and its new-item counters are hidden from the Files responses. Silencing a room changes nothing
for its other members. The kinds of notification this list is applied to are switched with
`POST api/2.0/settings/notification`.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**RoomsNotificationSettingsWrapper**](RoomsNotificationSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.rooms_notification_settings_wrapper import RoomsNotificationSettingsWrapper
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
    api_instance = docspace_api_sdk.NotificationsApi(api_client)

    try:
        # Get muted rooms
        api_response = api_instance.get_rooms_notification_settings()
        print("The response of NotificationsApi->get_rooms_notification_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_rooms_notification_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The identifiers of the rooms the calling user has silenced |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_notification_settings**
> NotificationSettingsWrapper set_notification_settings(notification_settings_requests_dto=notification_settings_requests_dto)

Switches one kind of notification on or off for the calling user: send the kind as `type` - 0 the new-item
badges, 1 the room activity letters, 2 the daily feed digest, 3 the periodic tips letters - together with
`isEnabled`. The change touches the caller's own account only, and repeating the call with the same pair
leaves the account as it is. Every signed-in member configures its own settings: the portal owner, a DocSpace
administrator, a room administrator, a user and a guest are all accepted, and no permission is demanded. With
0 switched off the Files responses report `new` as 0 and mark files as muted; with 1 switched off both the
hourly room digest and the letters a room sends at once, such as an editor mention, stop; with 2 switched off
the daily digest stops; with 3 switched off the tips letters stop. What comes back is an echo of the request
rather than a re-read of the stored state, and a `type` outside 0-3 is echoed as well while nothing is stored,
so confirm the result with `GET api/2.0/settings/notification/{type}`. To silence a single room instead of a
whole kind use `POST api/2.0/settings/notification/rooms`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_settings_requests_dto** | [**NotificationSettingsRequestsDto**](NotificationSettingsRequestsDto.md)|  | [optional] 

### Return type

[**NotificationSettingsWrapper**](NotificationSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.notification_settings_requests_dto import NotificationSettingsRequestsDto
from docspace_api_sdk.models.notification_settings_wrapper import NotificationSettingsWrapper
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
    api_instance = docspace_api_sdk.NotificationsApi(api_client)
    notification_settings_requests_dto = docspace_api_sdk.NotificationSettingsRequestsDto() # NotificationSettingsRequestsDto |  (optional)

    try:
        # Set notification status
        api_response = api_instance.set_notification_settings(notification_settings_requests_dto=notification_settings_requests_dto)
        print("The response of NotificationsApi->set_notification_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->set_notification_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The notification kind and state as they were sent in the request |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_rooms_notification_status**
> RoomsNotificationSettingsWrapper set_rooms_notification_status(rooms_notifications_settings_request_dto=rooms_notifications_settings_request_dto)

Adds one room to the calling user's silenced list or takes it off again: `mute` true silences the room, false
lets its notifications through. One call carries one room, so several rooms take several calls, and repeating
a call with the same pair changes nothing. The room is named by `roomsId` and kept as an opaque value: the
numeric identifier of a portal room and the string identifier of a room on a connected third-party account are
both accepted, and neither the room's existence nor the caller's access to it is checked, so a mistyped
identifier is stored as sent. Every signed-in member manages its own list, whatever its role, and the list of
another member cannot be touched. While a room is silenced its activity is left out of the hourly room digest
and of the daily feed, the letters it would send at once are not sent, and its new-item counters are hidden.
The Files responses stop offering the `mute` action on a room once badges, room activity and the daily feed
are all switched off, while this call keeps working. What comes back is the whole updated list, the same shape
`GET api/2.0/settings/notification/rooms` returns.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rooms_notifications_settings_request_dto** | [**RoomsNotificationsSettingsRequestDto**](RoomsNotificationsSettingsRequestDto.md)|  | [optional] 

### Return type

[**RoomsNotificationSettingsWrapper**](RoomsNotificationSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.rooms_notification_settings_wrapper import RoomsNotificationSettingsWrapper
from docspace_api_sdk.models.rooms_notifications_settings_request_dto import RoomsNotificationsSettingsRequestDto
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
    api_instance = docspace_api_sdk.NotificationsApi(api_client)
    rooms_notifications_settings_request_dto = docspace_api_sdk.RoomsNotificationsSettingsRequestDto() # RoomsNotificationsSettingsRequestDto |  (optional)

    try:
        # Mute or unmute a room
        api_response = api_instance.set_rooms_notification_status(rooms_notifications_settings_request_dto=rooms_notifications_settings_request_dto)
        print("The response of NotificationsApi->set_rooms_notification_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->set_rooms_notification_status: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The identifiers of the rooms the calling user has silenced, as the list stands after the change |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

