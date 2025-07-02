# docspace-api-python.SettingsWebhooksApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](#create_webhook) | **POST** /api/2.0/settings/webhook | Create a webhook
[**enable_webhook**](#enable_webhook) | **PUT** /api/2.0/settings/webhook/enable | Enable a webhook
[**get_tenant_webhooks**](#get_tenant_webhooks) | **GET** /api/2.0/settings/webhook | Get webhooks
[**get_webhook_triggers**](#get_webhook_triggers) | **GET** /api/2.0/settings/webhook/triggers | Get webhook triggers
[**get_webhooks_logs**](#get_webhooks_logs) | **GET** /api/2.0/settings/webhooks/log | Get webhook logs
[**remove_webhook**](#remove_webhook) | **DELETE** /api/2.0/settings/webhook/{id} | Remove a webhook
[**retry_webhook**](#retry_webhook) | **PUT** /api/2.0/settings/webhook/{id}/retry | Retry a webhook
[**retry_webhooks**](#retry_webhooks) | **PUT** /api/2.0/settings/webhook/retry | Retry webhooks
[**update_webhook**](#update_webhook) | **PUT** /api/2.0/settings/webhook | Update a webhook


# **create_webhook**
> WebhooksConfigWrapper create_webhook(create_webhooks_config_requests_dto=create_webhooks_config_requests_dto)

Creates a new tenant webhook with the parameters specified in the request.

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
import docspace-api-python
from docspace-api-python.models.create_webhooks_config_requests_dto import CreateWebhooksConfigRequestsDto
from docspace-api-python.models.webhooks_config_wrapper import WebhooksConfigWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.SettingsWebhooksApi(api_client)
    create_webhooks_config_requests_dto = docspace-api-python.CreateWebhooksConfigRequestsDto() # CreateWebhooksConfigRequestsDto |  (optional)

    try:
        # Create a webhook
        api_response = api_instance.create_webhook(create_webhooks_config_requests_dto=create_webhooks_config_requests_dto)
        print("The response of SettingsWebhooksApi->create_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsWebhooksApi->create_webhook: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tenant webhook with its config parameters |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_webhook**
> WebhooksConfigWrapper enable_webhook(update_webhooks_config_requests_dto=update_webhooks_config_requests_dto)

Enables or disables a tenant webhook with the parameters specified in the request.

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
import docspace-api-python
from docspace-api-python.models.update_webhooks_config_requests_dto import UpdateWebhooksConfigRequestsDto
from docspace-api-python.models.webhooks_config_wrapper import WebhooksConfigWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.SettingsWebhooksApi(api_client)
    update_webhooks_config_requests_dto = docspace-api-python.UpdateWebhooksConfigRequestsDto() # UpdateWebhooksConfigRequestsDto |  (optional)

    try:
        # Enable a webhook
        api_response = api_instance.enable_webhook(update_webhooks_config_requests_dto=update_webhooks_config_requests_dto)
        print("The response of SettingsWebhooksApi->enable_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsWebhooksApi->enable_webhook: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Enable or disable tenant webhook |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_webhooks**
> WebhooksConfigWithStatusArrayWrapper get_tenant_webhooks()

Returns a list of the tenant webhooks.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**WebhooksConfigWithStatusArrayWrapper**](WebhooksConfigWithStatusArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.webhooks_config_with_status_array_wrapper import WebhooksConfigWithStatusArrayWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.SettingsWebhooksApi(api_client)

    try:
        # Get webhooks
        api_response = api_instance.get_tenant_webhooks()
        print("The response of SettingsWebhooksApi->get_tenant_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsWebhooksApi->get_tenant_webhooks: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tenant webhooks with their config parameters |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_triggers**
> UnknownWrapper get_webhook_triggers()

Returns a list of triggers for a webhook.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**UnknownWrapper**](UnknownWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.unknown_wrapper import UnknownWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.SettingsWebhooksApi(api_client)

    try:
        # Get webhook triggers
        api_response = api_instance.get_webhook_triggers()
        print("The response of SettingsWebhooksApi->get_webhook_triggers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsWebhooksApi->get_webhook_triggers: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of triggers for a webhook |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhooks_logs**
> WebhooksLogArrayWrapper get_webhooks_logs(delivery_from=delivery_from, delivery_to=delivery_to, hook_uri=hook_uri, config_id=config_id, event_id=event_id, group_status=group_status, user_id=user_id, trigger=trigger, count=count, start_index=start_index)

Returns the logs of the webhook activities.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_from** | **datetime**| The delivery start time for filtering webhook logs. | [optional] 
 **delivery_to** | **datetime**| The delivery end time for filtering webhook logs. | [optional] 
 **hook_uri** | **str**| The destination URL where webhooks are delivered. | [optional] 
 **config_id** | **int**| The webhook configuration identifier. | [optional] 
 **event_id** | **int**| The unique identifier of the event that triggered the webhook. | [optional] 
 **group_status** | [**WebhookGroupStatus**](.md)| The status of the webhook delivery group. | [optional] 
 **user_id** | **str**| The identifier of the user associated with the webhook event. | [optional] 
 **trigger** | [**WebhookTrigger**](.md)| The type of event that triggered the webhook. | [optional] 
 **count** | **int**| The maximum number of webhook log records to return in the query response. | [optional] 
 **start_index** | **int**| Specifies the starting index for retrieving webhook logs.  Used for pagination in the webhook delivery log queries. | [optional] 

### Return type

[**WebhooksLogArrayWrapper**](WebhooksLogArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.webhook_group_status import WebhookGroupStatus
from docspace-api-python.models.webhook_trigger import WebhookTrigger
from docspace-api-python.models.webhooks_log_array_wrapper import WebhooksLogArrayWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.SettingsWebhooksApi(api_client)
    delivery_from = '2008-04-10T06:30+04:00' # datetime | The delivery start time for filtering webhook logs. (optional)
    delivery_to = '2008-04-10T06:30+04:00' # datetime | The delivery end time for filtering webhook logs. (optional)
    hook_uri = 'some text' # str | The destination URL where webhooks are delivered. (optional)
    config_id = 1234 # int | The webhook configuration identifier. (optional)
    event_id = 1234 # int | The unique identifier of the event that triggered the webhook. (optional)
    group_status = docspace-api-python.WebhookGroupStatus() # WebhookGroupStatus | The status of the webhook delivery group. (optional)
    user_id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28' # str | The identifier of the user associated with the webhook event. (optional)
    trigger = docspace-api-python.WebhookTrigger() # WebhookTrigger | The type of event that triggered the webhook. (optional)
    count = 1234 # int | The maximum number of webhook log records to return in the query response. (optional)
    start_index = 1234 # int | Specifies the starting index for retrieving webhook logs.  Used for pagination in the webhook delivery log queries. (optional)

    try:
        # Get webhook logs
        api_response = api_instance.get_webhooks_logs(delivery_from=delivery_from, delivery_to=delivery_to, hook_uri=hook_uri, config_id=config_id, event_id=event_id, group_status=group_status, user_id=user_id, trigger=trigger, count=count, start_index=start_index)
        print("The response of SettingsWebhooksApi->get_webhooks_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsWebhooksApi->get_webhooks_logs: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Logs of the webhook activities |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_webhook**
> WebhooksConfigWrapper remove_webhook(id)

Removes a tenant webhook with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID extracted from the route parameters. | 

### Return type

[**WebhooksConfigWrapper**](WebhooksConfigWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.webhooks_config_wrapper import WebhooksConfigWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.SettingsWebhooksApi(api_client)
    id = 9846 # int | The ID extracted from the route parameters.

    try:
        # Remove a webhook
        api_response = api_instance.remove_webhook(id)
        print("The response of SettingsWebhooksApi->remove_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsWebhooksApi->remove_webhook: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tenant webhook with its config parameters |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_webhook**
> WebhooksLogWrapper retry_webhook(id)

Retries a webhook with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID extracted from the route parameters. | 

### Return type

[**WebhooksLogWrapper**](WebhooksLogWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.webhooks_log_wrapper import WebhooksLogWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.SettingsWebhooksApi(api_client)
    id = 9846 # int | The ID extracted from the route parameters.

    try:
        # Retry a webhook
        api_response = api_instance.retry_webhook(id)
        print("The response of SettingsWebhooksApi->retry_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsWebhooksApi->retry_webhook: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Logs of the webhook activities |  -  |
**400** | Id incorrect |  -  |
**401** | Unauthorized |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_webhooks**
> WebhooksLogArrayWrapper retry_webhooks(webhook_retry_requests_dto=webhook_retry_requests_dto)

Retries all the webhooks with the IDs specified in the request.

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
import docspace-api-python
from docspace-api-python.models.webhook_retry_requests_dto import WebhookRetryRequestsDto
from docspace-api-python.models.webhooks_log_array_wrapper import WebhooksLogArrayWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.SettingsWebhooksApi(api_client)
    webhook_retry_requests_dto = docspace-api-python.WebhookRetryRequestsDto() # WebhookRetryRequestsDto |  (optional)

    try:
        # Retry webhooks
        api_response = api_instance.retry_webhooks(webhook_retry_requests_dto=webhook_retry_requests_dto)
        print("The response of SettingsWebhooksApi->retry_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsWebhooksApi->retry_webhooks: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Logs of the webhook activities |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> WebhooksConfigWrapper update_webhook(update_webhooks_config_requests_dto=update_webhooks_config_requests_dto)

Updates a tenant webhook with the parameters specified in the request.

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
import docspace-api-python
from docspace-api-python.models.update_webhooks_config_requests_dto import UpdateWebhooksConfigRequestsDto
from docspace-api-python.models.webhooks_config_wrapper import WebhooksConfigWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.SettingsWebhooksApi(api_client)
    update_webhooks_config_requests_dto = docspace-api-python.UpdateWebhooksConfigRequestsDto() # UpdateWebhooksConfigRequestsDto |  (optional)

    try:
        # Update a webhook
        api_response = api_instance.update_webhook(update_webhooks_config_requests_dto=update_webhooks_config_requests_dto)
        print("The response of SettingsWebhooksApi->update_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsWebhooksApi->update_webhook: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated tenant webhook with its config parameters |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

