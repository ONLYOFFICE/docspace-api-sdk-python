# docspace.SettingsWebhooksApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](SettingsWebhooksApi.md#create_webhook) | **POST** /api/2.0/settings/webhook | Create a webhook
[**disable_web_hook**](SettingsWebhooksApi.md#disable_web_hook) | **PUT** /api/2.0/settings/webhook/{id} | Disable a webhook
[**get_journal**](SettingsWebhooksApi.md#get_journal) | **GET** /api/2.0/settings/webhooks/log | Get webhook logs
[**get_tenant_webhooks**](SettingsWebhooksApi.md#get_tenant_webhooks) | **GET** /api/2.0/settings/webhook | Get webhooks
[**remove_webhook**](SettingsWebhooksApi.md#remove_webhook) | **DELETE** /api/2.0/settings/webhook/{id} | Remove a webhook
[**retry_webhook**](SettingsWebhooksApi.md#retry_webhook) | **PUT** /api/2.0/settings/webhook/{id}/retry | Retry a webhook
[**retry_webhooks**](SettingsWebhooksApi.md#retry_webhooks) | **PUT** /api/2.0/settings/webhook/retry | Retry webhooks
[**settings**](SettingsWebhooksApi.md#settings) | **GET** /api/2.0/settings/webhooks | Get webhook settings
[**update_webhook**](SettingsWebhooksApi.md#update_webhook) | **PUT** /api/2.0/settings/webhook | Update a webhook


# **create_webhook**
> WebhooksConfigWrapper create_webhook(webhooks_config_requests_dto=webhooks_config_requests_dto)

Create a webhook

Creates a new tenant webhook with the parameters specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.webhooks_config_requests_dto import WebhooksConfigRequestsDto
from docspace.models.webhooks_config_wrapper import WebhooksConfigWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.SettingsWebhooksApi(api_client)
    webhooks_config_requests_dto = docspace.WebhooksConfigRequestsDto() # WebhooksConfigRequestsDto |  (optional)

    try:
        # Create a webhook
        api_response = api_instance.create_webhook(webhooks_config_requests_dto=webhooks_config_requests_dto)
        print("The response of SettingsWebhooksApi->create_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsWebhooksApi->create_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhooks_config_requests_dto** | [**WebhooksConfigRequestsDto**](WebhooksConfigRequestsDto.md)|  | [optional] 

### Return type

[**WebhooksConfigWrapper**](WebhooksConfigWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tenant webhook with its config parameters |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_web_hook**
> WebhookWrapper disable_web_hook(id)

Disable a webhook

Disables a webhook with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.webhook_wrapper import WebhookWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.SettingsWebhooksApi(api_client)
    id = 9846 # int | Id

    try:
        # Disable a webhook
        api_response = api_instance.disable_web_hook(id)
        print("The response of SettingsWebhooksApi->disable_web_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsWebhooksApi->disable_web_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id | 

### Return type

[**WebhookWrapper**](WebhookWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_journal**
> WebhooksLogArrayWrapper get_journal(delivery_from=delivery_from, delivery_to=delivery_to, hook_uri=hook_uri, webhook_id=webhook_id, config_id=config_id, event_id=event_id, group_status=group_status)

Get webhook logs

Returns the logs of the webhook activities.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.webhook_group_status import WebhookGroupStatus
from docspace.models.webhooks_log_array_wrapper import WebhooksLogArrayWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.SettingsWebhooksApi(api_client)
    delivery_from = '2008-04-10T06:30+04:00' # datetime | Delivey start time (optional)
    delivery_to = '2008-04-10T06:30+04:00' # datetime | Delivey end time (optional)
    hook_uri = 'some text' # str | Hook URI (optional)
    webhook_id = 1234 # int | Webhook ID (optional)
    config_id = 1234 # int | Config ID (optional)
    event_id = 1234 # int | Event ID (optional)
    group_status = docspace.WebhookGroupStatus() # WebhookGroupStatus | Webhook group status (optional)

    try:
        # Get webhook logs
        api_response = api_instance.get_journal(delivery_from=delivery_from, delivery_to=delivery_to, hook_uri=hook_uri, webhook_id=webhook_id, config_id=config_id, event_id=event_id, group_status=group_status)
        print("The response of SettingsWebhooksApi->get_journal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsWebhooksApi->get_journal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_from** | **datetime**| Delivey start time | [optional] 
 **delivery_to** | **datetime**| Delivey end time | [optional] 
 **hook_uri** | **str**| Hook URI | [optional] 
 **webhook_id** | **int**| Webhook ID | [optional] 
 **config_id** | **int**| Config ID | [optional] 
 **event_id** | **int**| Event ID | [optional] 
 **group_status** | [**WebhookGroupStatus**](.md)| Webhook group status | [optional] 

### Return type

[**WebhooksLogArrayWrapper**](WebhooksLogArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Logs of the webhook activities |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_webhooks**
> WebhooksConfigWithStatusArrayWrapper get_tenant_webhooks()

Get webhooks

Returns a list of the tenant webhooks.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.webhooks_config_with_status_array_wrapper import WebhooksConfigWithStatusArrayWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.SettingsWebhooksApi(api_client)

    try:
        # Get webhooks
        api_response = api_instance.get_tenant_webhooks()
        print("The response of SettingsWebhooksApi->get_tenant_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsWebhooksApi->get_tenant_webhooks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WebhooksConfigWithStatusArrayWrapper**](WebhooksConfigWithStatusArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tenant webhooks with their config parameters |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_webhook**
> WebhooksConfigWrapper remove_webhook(id)

Remove a webhook

Removes the tenant webhook with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.webhooks_config_wrapper import WebhooksConfigWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.SettingsWebhooksApi(api_client)
    id = 9846 # int | Id

    try:
        # Remove a webhook
        api_response = api_instance.remove_webhook(id)
        print("The response of SettingsWebhooksApi->remove_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsWebhooksApi->remove_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id | 

### Return type

[**WebhooksConfigWrapper**](WebhooksConfigWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

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

Retry a webhook

Retries a webhook with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.webhooks_log_wrapper import WebhooksLogWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.SettingsWebhooksApi(api_client)
    id = 9846 # int | Id

    try:
        # Retry a webhook
        api_response = api_instance.retry_webhook(id)
        print("The response of SettingsWebhooksApi->retry_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsWebhooksApi->retry_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id | 

### Return type

[**WebhooksLogWrapper**](WebhooksLogWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

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

Retry webhooks

Retries all the webhooks with the IDs specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.webhook_retry_requests_dto import WebhookRetryRequestsDto
from docspace.models.webhooks_log_array_wrapper import WebhooksLogArrayWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.SettingsWebhooksApi(api_client)
    webhook_retry_requests_dto = docspace.WebhookRetryRequestsDto() # WebhookRetryRequestsDto |  (optional)

    try:
        # Retry webhooks
        api_response = api_instance.retry_webhooks(webhook_retry_requests_dto=webhook_retry_requests_dto)
        print("The response of SettingsWebhooksApi->retry_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsWebhooksApi->retry_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_retry_requests_dto** | [**WebhookRetryRequestsDto**](WebhookRetryRequestsDto.md)|  | [optional] 

### Return type

[**WebhooksLogArrayWrapper**](WebhooksLogArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Logs of the webhook activities |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings**
> WebhookArrayWrapper settings()

Get webhook settings

Returns settings of all webhooks.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.webhook_array_wrapper import WebhookArrayWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.SettingsWebhooksApi(api_client)

    try:
        # Get webhook settings
        api_response = api_instance.settings()
        print("The response of SettingsWebhooksApi->settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsWebhooksApi->settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WebhookArrayWrapper**](WebhookArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of webhook settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> WebhooksConfigWrapper update_webhook(webhooks_config_requests_dto=webhooks_config_requests_dto)

Update a webhook

Updates the tenant webhook with the parameters specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.webhooks_config_requests_dto import WebhooksConfigRequestsDto
from docspace.models.webhooks_config_wrapper import WebhooksConfigWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.SettingsWebhooksApi(api_client)
    webhooks_config_requests_dto = docspace.WebhooksConfigRequestsDto() # WebhooksConfigRequestsDto |  (optional)

    try:
        # Update a webhook
        api_response = api_instance.update_webhook(webhooks_config_requests_dto=webhooks_config_requests_dto)
        print("The response of SettingsWebhooksApi->update_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsWebhooksApi->update_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhooks_config_requests_dto** | [**WebhooksConfigRequestsDto**](WebhooksConfigRequestsDto.md)|  | [optional] 

### Return type

[**WebhooksConfigWrapper**](WebhooksConfigWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated tenant webhook with its config parameters |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

