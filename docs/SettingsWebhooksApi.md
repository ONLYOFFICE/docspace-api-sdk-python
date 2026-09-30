# docspace_api_sdk.WebhooksApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](#create_webhook) | **POST** /api/2.0/settings/webhook | Create a webhook
[**enable_webhook**](#enable_webhook) | **PUT** /api/2.0/settings/webhook/enable | Switch a webhook on or off
[**get_tenant_webhooks**](#get_tenant_webhooks) | **GET** /api/2.0/settings/webhook | Get the portal webhooks
[**get_webhook_triggers**](#get_webhook_triggers) | **GET** /api/2.0/settings/webhook/triggers | Get the webhook triggers
[**get_webhooks_logs**](#get_webhooks_logs) | **GET** /api/2.0/settings/webhooks/log | Get the webhook delivery log
[**remove_webhook**](#remove_webhook) | **DELETE** /api/2.0/settings/webhook/{id} | Remove a webhook
[**retry_webhook**](#retry_webhook) | **PUT** /api/2.0/settings/webhook/{id}/retry | Retry a webhook delivery
[**retry_webhooks**](#retry_webhooks) | **PUT** /api/2.0/settings/webhook/retry | Retry webhook deliveries
[**update_webhook**](#update_webhook) | **PUT** /api/2.0/settings/webhook | Update a webhook


# **create_webhook**
> WebhooksConfigWrapper create_webhook(create_webhooks_config_requests_dto=create_webhooks_config_requests_dto)

Creates a webhook subscription for the current portal: a target URL that the portal calls with a signed JSON
payload whenever one of the subscribed events happens. The target is checked before anything is stored, so it
has to be an absolute `http` or `https` address outside the installation's own network, and it has to answer a
HEAD request with a success code, redirects not being followed. `secretKey` is mandatory here, has to satisfy
the portal password rules published by `GET api/2.0/settings/security/password`, and signs the payloads; it
does not appear in any response. `triggers` is a bitmask of the subscribed events with 0 standing for all of
them; a flag the caller's role may not use is rejected, so take the allowed set from
`GET api/2.0/settings/webhook/triggers`. `ssl=true` additionally demands an `https` target with a valid
certificate, while `ssl=false` leaves the certificate unchecked. Set `targetId` to deliver events about a
single entity only. A subscription fires only for events its creator is allowed to see, and only while it is
enabled. Any role except `Guest` may create one, and each call adds another subscription rather than replacing
an existing one.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_webhooks_config_requests_dto** | [**CreateWebhooksConfigRequestsDto**](CreateWebhooksConfigRequestsDto.md)|  | [optional] 

### Return type

[**WebhooksConfigWrapper**](WebhooksConfigWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.create_webhooks_config_requests_dto import CreateWebhooksConfigRequestsDto
from docspace_api_sdk.models.webhooks_config_wrapper import WebhooksConfigWrapper
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
    api_instance = docspace_api_sdk.WebhooksApi(api_client)
    create_webhooks_config_requests_dto = docspace_api_sdk.CreateWebhooksConfigRequestsDto() # CreateWebhooksConfigRequestsDto |  (optional)

    try:
        # Create a webhook
        api_response = api_instance.create_webhook(create_webhooks_config_requests_dto=create_webhooks_config_requests_dto)
        print("The response of WebhooksApi->create_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->create_webhook: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created webhook subscription, without its secret key |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The target URL is unusable or unreachable, or the secret key or a trigger flag was rejected |  -  |
**403** | The caller is a `Guest`, or a non-admin caller while the developer tools are restricted |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_webhook**
> WebhooksConfigWrapper enable_webhook(update_webhooks_config_requests_dto=update_webhooks_config_requests_dto)

Switches one webhook subscription on or off, leaving the rest of its parameters as they are. Only `id` and
`enabled` are read from the body: `name`, `uri`, `secretKey`, `ssl`, `triggers` and `targetId` are demanded by
the schema but ignored here, so change any of them with `PUT api/2.0/settings/webhook` instead. Switching a
subscription on re-checks what is already stored, probing the saved URL with a HEAD request and re-validating
the saved secret against the current portal password rules, and the call is refused with 400 when either
fails: a subscription whose target has gone away, or whose secret predates a tightening of the password rules,
cannot be switched on until it is updated. Switching one off is not validated. While a subscription is off its
events are dropped rather than queued, so nothing arrives from that period once it is switched on again. A
`DocSpaceAdmin` may switch any subscription in the portal, anyone else only their own, and a `Guest` is
refused. The response carries the subscription in its new state, and repeating the call changes nothing
further.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_webhooks_config_requests_dto** | [**UpdateWebhooksConfigRequestsDto**](UpdateWebhooksConfigRequestsDto.md)|  | [optional] 

### Return type

[**WebhooksConfigWrapper**](WebhooksConfigWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.update_webhooks_config_requests_dto import UpdateWebhooksConfigRequestsDto
from docspace_api_sdk.models.webhooks_config_wrapper import WebhooksConfigWrapper
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
    api_instance = docspace_api_sdk.WebhooksApi(api_client)
    update_webhooks_config_requests_dto = docspace_api_sdk.UpdateWebhooksConfigRequestsDto() # UpdateWebhooksConfigRequestsDto |  (optional)

    try:
        # Switch a webhook on or off
        api_response = api_instance.enable_webhook(update_webhooks_config_requests_dto=update_webhooks_config_requests_dto)
        print("The response of WebhooksApi->enable_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->enable_webhook: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The webhook subscription in its new state, without its secret key |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The saved target no longer answers, or the saved secret no longer passes the password rules |  -  |
**403** | The subscription belongs to another member, or the caller may not use webhooks at all |  -  |
**404** | No webhook subscription with this ID exists in the portal |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_webhooks**
> WebhooksConfigWithStatusArrayWrapper get_tenant_webhooks()

Returns the webhook subscriptions of the current portal, each together with the outcome of its most recent
delivery. The portal owner and a `DocSpaceAdmin` see every subscription in the portal, while a `RoomAdmin` or
a `User` sees only the ones they created themselves, so the same call answers differently depending on who
asks. A `Guest` may not use webhooks at all and is refused, and so is any non-admin caller while the portal
keeps the developer tools restricted, which `GET api/2.0/settings/devtoolsaccess` reports. Every entry pairs
the stored configuration with `status`, the HTTP status code the target answered on the last attempt, where 0
means nothing has been delivered yet, while the secret key is not part of the response. The list is neither
paginated nor ordered, and an empty list simply means no subscription exists for the caller. Nothing is
written and the call is safe to repeat. Create a subscription with `POST api/2.0/settings/webhook`, and
inspect single deliveries with `GET api/2.0/settings/webhooks/log`.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**WebhooksConfigWithStatusArrayWrapper**](WebhooksConfigWithStatusArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.webhooks_config_with_status_array_wrapper import WebhooksConfigWithStatusArrayWrapper
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
    api_instance = docspace_api_sdk.WebhooksApi(api_client)

    try:
        # Get the portal webhooks
        api_response = api_instance.get_tenant_webhooks()
        print("The response of WebhooksApi->get_tenant_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_tenant_webhooks: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The webhook subscriptions visible to the caller, each with the status of its last delivery |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is a `Guest`, or a non-admin caller while the developer tools are restricted |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_triggers**
> WebhookTriggerArrayWrapper get_webhook_triggers()

Returns the catalogue of events a webhook subscription can listen to, in the order the portal presents them:
user events, then group, file, folder, room, form and agent ones. Each entry carries the event name as it
appears in a payload, such as `file.created`, the bit value to put into the `triggers` bitmask of a
subscription, and `available`, telling whether the caller's own role may subscribe to that event at all: a
`User` cannot subscribe to the creation of users, groups or rooms, for instance, while a `RoomAdmin` can. Add
the bit values of the wanted events together to build `triggers`; the entry named `*` has the value 0 and
stands for every event, so it is used on its own rather than added. Events unavailable to the caller are
listed all the same, but passing one to `POST api/2.0/settings/webhook` or `PUT api/2.0/settings/webhook` is
rejected as an invalid request. This is fixed reference data: the same for every portal, not paginated,
changing only with the product version, and readable by any authenticated caller, a `Guest` included. Nothing
is written.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**WebhookTriggerArrayWrapper**](WebhookTriggerArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.webhook_trigger_array_wrapper import WebhookTriggerArrayWrapper
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
    api_instance = docspace_api_sdk.WebhooksApi(api_client)

    try:
        # Get the webhook triggers
        api_response = api_instance.get_webhook_triggers()
        print("The response of WebhooksApi->get_webhook_triggers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhook_triggers: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The triggers a webhook may subscribe to, each marked available for the caller's role or not |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhooks_logs**
> WebhooksLogArrayWrapper get_webhooks_logs(delivery_from=delivery_from, delivery_to=delivery_to, hook_uri=hook_uri, config_id=config_id, event_id=event_id, group_status=group_status, user_id=user_id, trigger=trigger, count=count, start_index=start_index)

Returns the delivery records of the portal webhooks, one record per attempt, carrying the trigger, the request
and response headers and bodies, the HTTP `status` the target answered and the `delivery` moment, the last two
staying empty while an attempt is still on its way. Records come newest first and are paged with `startIndex`
and `count`, at most 100 at a time, while the number of records matching the filter is reported as `total`
beside the response. Filters combine with AND: `deliveryFrom` and `deliveryTo` bound the delivery moment,
`hookUri` matches the subscription URL exactly, `configId` picks one subscription, `eventId` one single
record, `groupStatus` keeps only the answered status classes it names with 0 meaning no status filter, and
`trigger` narrows to one event with 0 meaning all of them. `userId` filters by who created the subscription
rather than by who caused the event, and for a caller who is not a `DocSpaceAdmin` it is forced to the caller,
so a non-admin only ever sees deliveries of their own subscriptions. A `Guest` is refused. Nothing is written.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_from** | **datetime**| The earliest delivery moment a record may carry. Records of attempts still on their way have no delivery  moment yet and fall outside any bound set here. | [optional] 
 **delivery_to** | **datetime**| The latest delivery moment a record may carry. All the filters combine with AND, so it narrows whatever the  other ones already kept. | [optional] 
 **hook_uri** | **str**| The subscription target address, matched in full rather than as a prefix. Filtering by `configId` is the  reliable way to pick one subscription, since several may share an address. | [optional] 
 **config_id** | **int**| The subscription whose deliveries are kept, by the `id` that `GET api/2.0/settings/webhook` reports. | [optional] 
 **event_id** | **int**| A single delivery record, by its own identifier. It narrows the answer to that one record, which is how a  client follows up a retry it queued earlier. | [optional] 
 **group_status** | [**WebhookGroupStatus**](.md)| The classes of answered status to keep, as a bitmask; 0 keeps every record whatever the target answered. | [optional] 
 **user_id** | **UUID**| The member whose subscriptions the records belong to, by portal user ID - who created the subscription, not  who caused the event. For a caller who is not a DocSpace administrator it is overwritten with the caller own  ID, so such a caller never sees another member deliveries whatever is sent here. | [optional] 
 **trigger** | [**WebhookTrigger**](.md)| The single event kind to keep; 0 keeps every kind. It names one trigger rather than a mask of several, unlike  the `triggers` a subscription is created with. | [optional] 
 **count** | **int**| How many records one page may hold. The maximum is also the default, so a client that wants shorter pages has  to ask for them; the number of records matching the filter comes back as `total` beside the page. | [optional] 
 **start_index** | **int**| How many matching records to skip before the page begins, counting from the newest. Advance it by `count` to  walk back through the log. | [optional] 

### Return type

[**WebhooksLogArrayWrapper**](WebhooksLogArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.webhook_group_status import WebhookGroupStatus
from docspace_api_sdk.models.webhook_trigger import WebhookTrigger
from docspace_api_sdk.models.webhooks_log_array_wrapper import WebhooksLogArrayWrapper
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
    api_instance = docspace_api_sdk.WebhooksApi(api_client)
    delivery_from = '2024-01-15T10:30:00Z' # datetime | The earliest delivery moment a record may carry. Records of attempts still on their way have no delivery  moment yet and fall outside any bound set here. (optional)
    delivery_to = '2024-01-15T10:30:00Z' # datetime | The latest delivery moment a record may carry. All the filters combine with AND, so it narrows whatever the  other ones already kept. (optional)
    hook_uri = 'https://example.com/webhook' # str | The subscription target address, matched in full rather than as a prefix. Filtering by `configId` is the  reliable way to pick one subscription, since several may share an address. (optional)
    config_id = 1 # int | The subscription whose deliveries are kept, by the `id` that `GET api/2.0/settings/webhook` reports. (optional)
    event_id = 1 # int | A single delivery record, by its own identifier. It narrows the answer to that one record, which is how a  client follows up a retry it queued earlier. (optional)
    group_status = docspace_api_sdk.WebhookGroupStatus() # WebhookGroupStatus | The classes of answered status to keep, as a bitmask; 0 keeps every record whatever the target answered. (optional)
    user_id = UUID('{}') # UUID | The member whose subscriptions the records belong to, by portal user ID - who created the subscription, not  who caused the event. For a caller who is not a DocSpace administrator it is overwritten with the caller own  ID, so such a caller never sees another member deliveries whatever is sent here. (optional)
    trigger = docspace_api_sdk.WebhookTrigger() # WebhookTrigger | The single event kind to keep; 0 keeps every kind. It names one trigger rather than a mask of several, unlike  the `triggers` a subscription is created with. (optional)
    count = 1 # int | How many records one page may hold. The maximum is also the default, so a client that wants shorter pages has  to ask for them; the number of records matching the filter comes back as `total` beside the page. (optional)
    start_index = 1 # int | How many matching records to skip before the page begins, counting from the newest. Advance it by `count` to  walk back through the log. (optional)

    try:
        # Get the webhook delivery log
        api_response = api_instance.get_webhooks_logs(delivery_from=delivery_from, delivery_to=delivery_to, hook_uri=hook_uri, config_id=config_id, event_id=event_id, group_status=group_status, user_id=user_id, trigger=trigger, count=count, start_index=start_index)
        print("The response of WebhooksApi->get_webhooks_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhooks_logs: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matching delivery records, newest first, with the total count reported beside them |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is a `Guest`, or a non-admin caller while the developer tools are restricted |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_webhook**
> WebhooksConfigWrapper remove_webhook(id)

Removes one webhook subscription from the current portal for good, addressed by `id` in the path. Deliveries
stop with it: matching events are no longer queued, and there is no undo, so a subscription dropped by mistake
has to be created again with `POST api/2.0/settings/webhook`, which gives it a new identifier and needs a new
secret key. To pause deliveries without losing the configuration, switch the subscription off with
`PUT api/2.0/settings/webhook/enable` instead. A `DocSpaceAdmin` may remove any subscription in the portal,
anyone else only the ones they created, and a `Guest` may not use webhooks at all. The response repeats the
subscription as it was just before the removal, so the caller can record what disappeared, again without the
secret key. An identifier that no longer exists gives 404, which is what a second removal of the same
subscription answers as well, so a repeated call is harmless but reports the state truthfully rather than
pretending to succeed.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the object the operation acts on, as the listing operation of that kind of object reports  it. It has to match the shape the route declares - a GUID where the route is typed as one - since a value of  another shape does not match the route at all and is answered as not found. | 

### Return type

[**WebhooksConfigWrapper**](WebhooksConfigWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.webhooks_config_wrapper import WebhooksConfigWrapper
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
    api_instance = docspace_api_sdk.WebhooksApi(api_client)
    id = 1 # int | The identifier of the object the operation acts on, as the listing operation of that kind of object reports  it. It has to match the shape the route declares - a GUID where the route is typed as one - since a value of  another shape does not match the route at all and is answered as not found.

    try:
        # Remove a webhook
        api_response = api_instance.remove_webhook(id)
        print("The response of WebhooksApi->remove_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->remove_webhook: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The removed webhook subscription, as it was just before the removal |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The subscription belongs to another member, or the caller may not use webhooks at all |  -  |
**404** | No webhook subscription with this ID exists in the portal |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_webhook**
> WebhooksLogWrapper retry_webhook(id)

Sends one past webhook delivery again. The `id` in the path is that of a delivery record from
`GET api/2.0/settings/webhooks/log`, not of a subscription, and the payload kept in that record is sent once
more to the subscription it belongs to. The work is asynchronous: a fresh delivery record is created and
queued at once, and the response describes that new record, with an identifier of its own and with `status`
and `delivery` not filled in yet. To learn the outcome, read `GET api/2.0/settings/webhooks/log` with
`eventId` set to the returned identifier until `delivery` appears. The original record stays as it is, and
every call queues one more attempt, so this is not safe to repeat blindly. A `DocSpaceAdmin` may retry any
delivery in the portal, anyone else only deliveries of the subscriptions they created, and a `Guest` is
refused. An `id` of 0 is rejected as an invalid request and an unknown one gives 404. The operation is rate
limited, so a burst of calls is answered with 429; to retry several records use
`PUT api/2.0/settings/webhook/retry`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the object the operation acts on, as the listing operation of that kind of object reports  it. It has to match the shape the route declares - a GUID where the route is typed as one - since a value of  another shape does not match the route at all and is answered as not found. | 

### Return type

[**WebhooksLogWrapper**](WebhooksLogWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.webhooks_log_wrapper import WebhooksLogWrapper
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
    api_instance = docspace_api_sdk.WebhooksApi(api_client)
    id = 1 # int | The identifier of the object the operation acts on, as the listing operation of that kind of object reports  it. It has to match the shape the route declares - a GUID where the route is typed as one - since a value of  another shape does not match the route at all and is answered as not found.

    try:
        # Retry a webhook delivery
        api_response = api_instance.retry_webhook(id)
        print("The response of WebhooksApi->retry_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->retry_webhook: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly queued delivery record, with its status and delivery moment not filled in yet |  * X-RateLimit-Limit - Rate limit: 5 requests per 15 minutes per user/IP. <br>  * X-RateLimit-Remaining - Requests remaining in the current 15-minute window. <br>  * X-RateLimit-Reset -  <br>  |
**400** | The delivery record identifier is 0 |  -  |
**403** | The delivery belongs to another member's subscription, or the caller may not use webhooks |  -  |
**404** | No delivery record with this ID exists in the portal |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying (5 req / 15 min limit per user/IP). <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_webhooks**
> WebhooksLogArrayWrapper retry_webhooks(webhook_retry_requests_dto=webhook_retry_requests_dto)

Sends a batch of past webhook deliveries again. `ids` holds the identifiers of delivery records from
`GET api/2.0/settings/webhooks/log`; each of them is sent once more to the subscription it belongs to as a
fresh delivery record, queued for asynchronous delivery, and the response lists those new records with
`status` and `delivery` not filled in yet. Records that do not exist, and records of another member's
subscription when the caller is not a `DocSpaceAdmin`, are skipped in silence instead of failing the call, so
a response shorter than `ids` is the only sign that something was left out: compare the counts rather than
assuming everything was queued. An empty `ids` list is accepted and queues nothing. Read the outcomes from
`GET api/2.0/settings/webhooks/log`, matching the returned identifiers with `eventId`. Every call queues
another round of attempts, and the original records stay as they are. A `Guest` is refused. The operation is
rate limited, so a burst of calls is answered with 429. For a single record
`PUT api/2.0/settings/webhook/{id}/retry` reports a missing or forbidden record instead of skipping it.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_retry_requests_dto** | [**WebhookRetryRequestsDto**](WebhookRetryRequestsDto.md)|  | [optional] 

### Return type

[**WebhooksLogArrayWrapper**](WebhooksLogArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.webhook_retry_requests_dto import WebhookRetryRequestsDto
from docspace_api_sdk.models.webhooks_log_array_wrapper import WebhooksLogArrayWrapper
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
    api_instance = docspace_api_sdk.WebhooksApi(api_client)
    webhook_retry_requests_dto = docspace_api_sdk.WebhookRetryRequestsDto() # WebhookRetryRequestsDto |  (optional)

    try:
        # Retry webhook deliveries
        api_response = api_instance.retry_webhooks(webhook_retry_requests_dto=webhook_retry_requests_dto)
        print("The response of WebhooksApi->retry_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->retry_webhooks: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly queued delivery records, one for every identifier that could be retried |  * X-RateLimit-Limit - Rate limit: 5 requests per 15 minutes per user/IP. <br>  * X-RateLimit-Remaining - Requests remaining in the current 15-minute window. <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is a `Guest`, or a non-admin caller while the developer tools are restricted |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying (5 req / 15 min limit per user/IP). <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> WebhooksConfigWrapper update_webhook(update_webhooks_config_requests_dto=update_webhooks_config_requests_dto)

Replaces the stored parameters of one webhook subscription, which is addressed by `id` in the body rather than
in the path. Every field of the request overwrites the stored one, so a payload that leaves out `enabled`,
`ssl`, `triggers` or `targetId` resets them to off, all events and no target: read the current values with
`GET api/2.0/settings/webhook` first and send back whatever should stay. `secretKey` is the one exception, an
empty value keeping the existing secret and a new one having to satisfy the portal password rules. The new
target is validated exactly as on creation, that is it must sit outside the installation's own network and
answer a HEAD request, and trigger flags the caller's role may not use are rejected. That validation runs
before the subscription is looked up, so an unusable payload is refused with 400 even when no subscription
with this `id` exists. A `DocSpaceAdmin` may update any subscription in the portal, anyone else only their
own, and a `Guest` is refused. Sending the same payload twice leaves the same state. Use
`PUT api/2.0/settings/webhook/enable` to switch a subscription on or off without touching anything else.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_webhooks_config_requests_dto** | [**UpdateWebhooksConfigRequestsDto**](UpdateWebhooksConfigRequestsDto.md)|  | [optional] 

### Return type

[**WebhooksConfigWrapper**](WebhooksConfigWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.update_webhooks_config_requests_dto import UpdateWebhooksConfigRequestsDto
from docspace_api_sdk.models.webhooks_config_wrapper import WebhooksConfigWrapper
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
    api_instance = docspace_api_sdk.WebhooksApi(api_client)
    update_webhooks_config_requests_dto = docspace_api_sdk.UpdateWebhooksConfigRequestsDto() # UpdateWebhooksConfigRequestsDto |  (optional)

    try:
        # Update a webhook
        api_response = api_instance.update_webhook(update_webhooks_config_requests_dto=update_webhooks_config_requests_dto)
        print("The response of WebhooksApi->update_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->update_webhook: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated webhook subscription, without its secret key |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The target URL is unusable or unreachable, or the secret key or a trigger flag was rejected |  -  |
**403** | The subscription belongs to another member, or the caller may not use webhooks at all |  -  |
**404** | No webhook subscription with this ID exists in the portal |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

