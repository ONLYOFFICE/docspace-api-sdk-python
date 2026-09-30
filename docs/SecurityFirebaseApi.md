# docspace_api_sdk.FirebaseApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**doc_register_pusn_notification_device**](#doc_register_pusn_notification_device) | **POST** /api/2.0/settings/push/docregisterdevice | Register a push device
[**subscribe_documents_push_notification**](#subscribe_documents_push_notification) | **PUT** /api/2.0/settings/push/docsubscribe | Set push subscription


# **doc_register_pusn_notification_device**
> FireBaseUserWrapper doc_register_pusn_notification_device(firebase_requests_dto=firebase_requests_dto)

Registers one mobile device of the calling user for the push notifications of the Documents application, by
storing the Firebase token that device was issued together with the initial `isSubscribed` state. The token is
handed out by Firebase to the mobile client, so obtain it there before calling: nothing here checks it, and it
is kept as an opaque string of up to 255 characters. Every signed-in member registers its own devices,
whatever its role - owner, administrator, user or guest - and a registration is bound to the caller and the
current portal, so another member's devices cannot be touched. The call is safe to repeat, but it is not an
update: a token already registered comes back as it stands and `isSubscribed` from the request is ignored, so
switch an existing registration on or off with `PUT api/2.0/settings/push/docsubscribe` instead. What comes
back is the stored registration, with `application` always `doc` and `isSubscribed` as stored. Only a
subscribed device is sent the room activity messages, such as an invitation to a room, a role change, an
archived room or a new document in a room, and only while the installation itself is configured with Firebase
credentials.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firebase_requests_dto** | [**FirebaseRequestsDto**](FirebaseRequestsDto.md)|  | [optional] 

### Return type

[**FireBaseUserWrapper**](FireBaseUserWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.fire_base_user_wrapper import FireBaseUserWrapper
from docspace_api_sdk.models.firebase_requests_dto import FirebaseRequestsDto
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
    api_instance = docspace_api_sdk.FirebaseApi(api_client)
    firebase_requests_dto = docspace_api_sdk.FirebaseRequestsDto() # FirebaseRequestsDto |  (optional)

    try:
        # Register a push device
        api_response = api_instance.doc_register_pusn_notification_device(firebase_requests_dto=firebase_requests_dto)
        print("The response of FirebaseApi->doc_register_pusn_notification_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirebaseApi->doc_register_pusn_notification_device: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The stored device registration of the calling user, with the Firebase token, the `doc` application and the subscription state as they are kept |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_documents_push_notification**
> FireBaseUserWrapper subscribe_documents_push_notification(firebase_requests_dto=firebase_requests_dto)

Switches the push notifications of the Documents application on or off for one already registered device of
the calling user: send that device's Firebase token together with `isSubscribed` true to let the messages
through or false to stop them. The device has to be registered first with
`POST api/2.0/settings/push/docregisterdevice`, and only the subscription state is written - the token is
matched, never changed. Every signed-in member manages its own devices, whatever its role - owner,
administrator, user or guest - and a token that belongs to another member or to another portal is not matched
at all, so nothing of theirs can be switched. Repeating the call with the same pair leaves the registration as
it is. What comes back is the updated registration, while an empty response means no registration of the
caller carries that token and nothing was stored - register the device and call again. A device switched off
keeps its token stored but is left out of the delivery, and the other devices of the same member are
unaffected. Which kinds of notification the account receives at all is a separate setting, read with
`GET api/2.0/settings/notification/{type}`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firebase_requests_dto** | [**FirebaseRequestsDto**](FirebaseRequestsDto.md)|  | [optional] 

### Return type

[**FireBaseUserWrapper**](FireBaseUserWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.fire_base_user_wrapper import FireBaseUserWrapper
from docspace_api_sdk.models.firebase_requests_dto import FirebaseRequestsDto
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
    api_instance = docspace_api_sdk.FirebaseApi(api_client)
    firebase_requests_dto = docspace_api_sdk.FirebaseRequestsDto() # FirebaseRequestsDto |  (optional)

    try:
        # Set push subscription
        api_response = api_instance.subscribe_documents_push_notification(firebase_requests_dto=firebase_requests_dto)
        print("The response of FirebaseApi->subscribe_documents_push_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirebaseApi->subscribe_documents_push_notification: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The device registration as it stands after the change, or an empty response when no registration of the calling user carries the token that was sent |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

