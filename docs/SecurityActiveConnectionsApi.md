# docspace_api_sdk.ActiveConnectionsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_active_connections**](#get_all_active_connections) | **GET** /api/2.0/security/activeconnections | Get active connections
[**log_out_active_connection**](#log_out_active_connection) | **PUT** /api/2.0/security/activeconnections/logout/{loginEventId} | Log out one connection
[**log_out_all_active_connections_change_password**](#log_out_all_active_connections_change_password) | **PUT** /api/2.0/security/activeconnections/logoutallchangepassword | Log out and reset password
[**log_out_all_active_connections_for_user**](#log_out_all_active_connections_for_user) | **PUT** /api/2.0/security/activeconnections/logoutall/{userId} | Log out a user everywhere
[**log_out_all_except_this_connection**](#log_out_all_except_this_connection) | **PUT** /api/2.0/security/activeconnections/logoutallexceptthis | Log out other connections


# **get_all_active_connections**
> ActiveConnectionsWrapper get_all_active_connections()

Lists the connections the calling user currently has open on this portal - one item per successful sign-in
that is still active - so a client can show where the account is signed in and close what does not belong
there. Any signed-in user may call it, nothing has to be called first, and the answer always covers the caller
alone: the operation is read-only, idempotent and cannot show another user's connections. Items cover the last
year and are ordered newest sign-in first, with the caller's own connection moved to the top and its browser,
platform, IP address and location refreshed from the current request. `loginEvent` is the ID of that own
connection and is `0` when the request was authenticated with a token in the `Authorization` header instead of
the portal cookie; nothing is then marked as current, and a user with no stored connections gets a single item
describing the current request. `country` and `city` are resolved from the IP address and stay empty when it
cannot be located. Pass an item's `id` to `PUT api/2.0/security/activeconnections/logout/{loginEventId}` to
end that one connection.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**ActiveConnectionsWrapper**](ActiveConnectionsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.active_connections_wrapper import ActiveConnectionsWrapper
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
    api_instance = docspace_api_sdk.ActiveConnectionsApi(api_client)

    try:
        # Get active connections
        api_response = api_instance.get_all_active_connections()
        print("The response of ActiveConnectionsApi->get_all_active_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActiveConnectionsApi->get_all_active_connections: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The caller's active connections, newest sign-in first, with `loginEvent` pointing at the connection the request itself was made with |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_out_active_connection**
> BooleanWrapper log_out_active_connection(login_event_id)

Closes one active connection: the sign-in behind `loginEventId` is marked inactive, the token and cookie tied
to it stop working, the client holding it is disconnected and a logout entry is written to the portal audit
trail. Take `loginEventId` from the `id` of an item of `GET api/2.0/security/activeconnections`, which also
reports in `loginEvent` which connection the caller is using, so a client can avoid closing its own. A user
may close their own connections, while closing somebody else's requires a DocSpace administrator and any other
caller is refused with 403. The call is mutating, destructive for that one session and idempotent, and it
leaves every other connection of the user alone - `PUT api/2.0/security/activeconnections/logoutallexceptthis`
is the way to close the rest in one go. Only `true` means the connection was open and has just been closed;
`false` comes back when this portal has no such active connection, including one that was already closed, and
after any other failure.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_event_id** | **int**| The sign-in to act on, by login event ID. Take it from the `id` of an item of  `GET api/2.0/security/activeconnections`, which also marks the connection the caller is using, so a client  can avoid picking its own. | 

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
    api_instance = docspace_api_sdk.ActiveConnectionsApi(api_client)
    login_event_id = 12345 # int | The sign-in to act on, by login event ID. Take it from the `id` of an item of  `GET api/2.0/security/activeconnections`, which also marks the connection the caller is using, so a client  can avoid picking its own.

    try:
        # Log out one connection
        api_response = api_instance.log_out_active_connection(login_event_id)
        print("The response of ActiveConnectionsApi->log_out_active_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActiveConnectionsApi->log_out_active_connection: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | `true` when the connection was open and has been closed, `false` when this portal has no such active connection or the attempt failed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator and the connection belongs to another user |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_out_all_active_connections_change_password**
> StringWrapper log_out_all_active_connections_change_password()

Closes every active connection of the calling user and returns the link that user has to open to set a new
password - the answer to a suspicious sign-in seen in `GET api/2.0/security/activeconnections`. Any signed-in
user may call it for their own account and nothing has to be called first; the same clean-up for somebody else
is `PUT api/2.0/security/activeconnections/logoutall/{userId}`. The call is mutating and destructive for
sessions - every token and cookie issued to the user before it stops working and the clients holding them are
disconnected - and it is not idempotent: the request is written to the portal audit trail, which invalidates
the link any earlier call returned, and the caller's own client is handed a fresh cookie in the response and
stays signed in through a new connection. The password itself is not changed here, and the link is handed back
to the caller rather than mailed to the user: the URL carries a time-limited `PasswordChange` key, which the
confirmation page it opens - or `PUT api/2.0/people/{userid}/password` - needs to accept the new password. A
failure is swallowed instead of reported, so an empty body with status 200 means nothing was done and the call
has to be repeated.

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
    api_instance = docspace_api_sdk.ActiveConnectionsApi(api_client)

    try:
        # Log out and reset password
        api_response = api_instance.log_out_all_active_connections_change_password()
        print("The response of ActiveConnectionsApi->log_out_all_active_connections_change_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActiveConnectionsApi->log_out_all_active_connections_change_password: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The URL the user has to open to set a new password, or an empty result when the operation failed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_out_all_active_connections_for_user**
> log_out_all_active_connections_for_user(user_id)

Closes every active connection of one portal user: the connections are marked inactive, every token and cookie
issued to that user before the call stops working, the clients holding them are disconnected and a logout
entry is written to the portal audit trail. Nothing has to be called first; `userId` is the portal user ID
that `GET api/2.0/people` returns. A user may pass their own ID, while ending somebody else's connections
requires a DocSpace administrator and any other caller is refused with 403. The call is mutating, destructive
for those sessions and idempotent - a user with nothing open is not an error - and it returns no content, so
the state afterwards is read from `GET api/2.0/security/activeconnections`. A caller who ends their own
connections is handed a fresh cookie in the response and stays signed in through a new connection. Nothing
else about the user changes: the account stays enabled and the password stays valid, and to keep the current
connection alive instead use `PUT api/2.0/security/activeconnections/logoutallexceptthis`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **UUID**| The portal account the operation acts on, by user ID as `GET api/2.0/people` reports it. Acting on an account  other than the caller's own generally needs administrator rights. | 

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
    api_instance = docspace_api_sdk.ActiveConnectionsApi(api_client)
    user_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The portal account the operation acts on, by user ID as `GET api/2.0/people` reports it. Acting on an account  other than the caller's own generally needs administrator rights.

    try:
        # Log out a user everywhere
        api_instance.log_out_all_active_connections_for_user(user_id)
    except Exception as e:
        print("Exception when calling ActiveConnectionsApi->log_out_all_active_connections_for_user: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The connections of that user have been closed; the response carries no content |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator and the ID in the path is not their own |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_out_all_except_this_connection**
> StringWrapper log_out_all_except_this_connection()

Closes every active connection of the calling user except the one this request was made with, so the current
client keeps working while every other browser and device is signed out. Any signed-in user may call it for
their own account and nothing has to be called first. The connection to keep is the one behind the portal
authentication cookie: a request authenticated with a token in the `Authorization` header has none, and then
every connection of the user is closed, including the one that token belongs to - read `loginEvent` from
`GET api/2.0/security/activeconnections` first to see which connection, if any, will survive. The call is
mutating and destructive for the other sessions, and idempotent: the tokens behind them stop working, their
clients are disconnected at once and a logout entry is written to the portal audit trail. It answers with the
display name of the calling user, while an empty answer with status 200 means the attempt failed and nothing
can be assumed about what was closed.

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
    api_instance = docspace_api_sdk.ActiveConnectionsApi(api_client)

    try:
        # Log out other connections
        api_response = api_instance.log_out_all_except_this_connection()
        print("The response of ActiveConnectionsApi->log_out_all_except_this_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActiveConnectionsApi->log_out_all_except_this_connection: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The display name of the calling user, or an empty result when the operation failed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

