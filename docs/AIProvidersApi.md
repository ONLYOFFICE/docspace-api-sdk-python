# docspace_api_sdk.ProvidersApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_provider**](#add_provider) | **POST** /api/2.0/ai/providers | Add an AI provider
[**delete_providers**](#delete_providers) | **DELETE** /api/2.0/ai/providers | Delete AI providers
[**get_available_providers**](#get_available_providers) | **GET** /api/2.0/ai/providers/available | Get available AI provider types
[**get_default_provider**](#get_default_provider) | **GET** /api/2.0/ai/providers/default | Get the default AI provider
[**get_provider_models**](#get_provider_models) | **GET** /api/2.0/ai/providers/{providerId}/models | Get all models for a provider with their settings
[**get_providers**](#get_providers) | **GET** /api/2.0/ai/providers | Get AI providers
[**preview_provider_models**](#preview_provider_models) | **POST** /api/2.0/ai/providers/models/preview | Preview models for a new AI provider
[**set_default_provider**](#set_default_provider) | **PUT** /api/2.0/ai/providers/default | Set the default AI provider
[**update_provider**](#update_provider) | **PUT** /api/2.0/ai/providers/{id} | Update an AI provider


# **add_provider**
> AiProviderWrapper add_provider(create_provider_request_dto=create_provider_request_dto)

Registers a new AI provider for the current tenant by specifying its type, display title, API endpoint URL, and authentication key.
The provider becomes available for AI chat conversations after creation. This action is rate-limited.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_provider_request_dto** | [**CreateProviderRequestDto**](CreateProviderRequestDto.md)|  | [optional] 

### Return type

[**AiProviderWrapper**](AiProviderWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_provider_wrapper import AiProviderWrapper
from docspace_api_sdk.models.create_provider_request_dto import CreateProviderRequestDto
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
    api_instance = docspace_api_sdk.ProvidersApi(api_client)
    create_provider_request_dto = docspace_api_sdk.CreateProviderRequestDto() # CreateProviderRequestDto |  (optional)

    try:
        # Add an AI provider
        api_response = api_instance.add_provider(create_provider_request_dto=create_provider_request_dto)
        print("The response of ProvidersApi->add_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->add_provider: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created AI provider details |  * X-RateLimit-Limit - Rate limit: 10 requests per 1 minutes per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**400** | Invalid connection data or provider with this name already exists |  -  |
**403** | You don't have enough permission to manage providers |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_providers**
> delete_providers(remove_provider_request_dto=remove_provider_request_dto)

Permanently deletes one or more AI providers by their identifiers.
All specified providers are removed from the current tenant. This action cannot be undone.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_provider_request_dto** | [**RemoveProviderRequestDto**](RemoveProviderRequestDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.remove_provider_request_dto import RemoveProviderRequestDto
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
    api_instance = docspace_api_sdk.ProvidersApi(api_client)
    remove_provider_request_dto = docspace_api_sdk.RemoveProviderRequestDto() # RemoveProviderRequestDto |  (optional)

    try:
        # Delete AI providers
        api_instance.delete_providers(remove_provider_request_dto=remove_provider_request_dto)
    except Exception as e:
        print("Exception when calling ProvidersApi->delete_providers: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The providers were successfully deleted |  -  |
**403** | You don't have enough permission to manage providers |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_providers**
> ProviderSettingsArrayWrapper get_available_providers()

Returns the list of AI provider types that are available for configuration on the current instance.
Each entry includes the provider type identifier and the default API endpoint URL.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**ProviderSettingsArrayWrapper**](ProviderSettingsArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.provider_settings_array_wrapper import ProviderSettingsArrayWrapper
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
    api_instance = docspace_api_sdk.ProvidersApi(api_client)

    try:
        # Get available AI provider types
        api_response = api_instance.get_available_providers()
        print("The response of ProvidersApi->get_available_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->get_available_providers: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of available AI provider types |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_provider**
> DefaultProviderWrapper get_default_provider()

Returns the default AI provider and model configured for the current tenant.
Returns null if the tenant does not have any registered providers.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**DefaultProviderWrapper**](DefaultProviderWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.default_provider_wrapper import DefaultProviderWrapper
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
    api_instance = docspace_api_sdk.ProvidersApi(api_client)

    try:
        # Get the default AI provider
        api_response = api_instance.get_default_provider()
        print("The response of ProvidersApi->get_default_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->get_default_provider: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default provider information or null if not set |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provider_models**
> ModelSettingsArrayWrapper get_provider_models(provider_id)

Returns the full list of AI models available from a provider, including both recommended and additional models.
Each model includes its current settings: enabled state, display alias, and capabilities (vision, tool calling, thinking).
Recommended models are enabled by default and their alias and capabilities come from configuration.
Additional models are disabled by default and can be configured by the admin.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **int**| The identifier of the AI provider. | 

### Return type

[**ModelSettingsArrayWrapper**](ModelSettingsArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.model_settings_array_wrapper import ModelSettingsArrayWrapper
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
    api_instance = docspace_api_sdk.ProvidersApi(api_client)
    provider_id = 1 # int | The identifier of the AI provider.

    try:
        # Get all models for a provider with their settings
        api_response = api_instance.get_provider_models(provider_id)
        print("The response of ProvidersApi->get_provider_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->get_provider_models: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of models with settings |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You don't have enough permission to manage providers |  -  |
**404** | Provider not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_providers**
> AiProviderArrayWrapper get_providers(start_index=start_index, count=count)

Returns a paginated list of AI providers configured for the current tenant.
Supports pagination via the startIndex and count query parameters. The total number of providers is included in the response metadata.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_index** | **int**| The number of items to skip before returning results (zero-based offset). Defaults to 0. | [optional] 
 **count** | **int**| The maximum number of items to return per page. Defaults to 100. | [optional] 

### Return type

[**AiProviderArrayWrapper**](AiProviderArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_provider_array_wrapper import AiProviderArrayWrapper
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
    api_instance = docspace_api_sdk.ProvidersApi(api_client)
    start_index = 0 # int | The number of items to skip before returning results (zero-based offset). Defaults to 0. (optional)
    count = 100 # int | The maximum number of items to return per page. Defaults to 100. (optional)

    try:
        # Get AI providers
        api_response = api_instance.get_providers(start_index=start_index, count=count)
        print("The response of ProvidersApi->get_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->get_providers: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of AI providers |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_provider_models**
> ModelSettingsArrayWrapper preview_provider_models(preview_provider_models_request_dto=preview_provider_models_request_dto)

Connects to the specified AI provider using the provided credentials and returns the available models
with their default settings. This is used to preview models before saving the provider.
Recommended models are enabled by default with configuration-defined settings.
Additional models are disabled by default with empty capabilities.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preview_provider_models_request_dto** | [**PreviewProviderModelsRequestDto**](PreviewProviderModelsRequestDto.md)|  | [optional] 

### Return type

[**ModelSettingsArrayWrapper**](ModelSettingsArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.model_settings_array_wrapper import ModelSettingsArrayWrapper
from docspace_api_sdk.models.preview_provider_models_request_dto import PreviewProviderModelsRequestDto
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
    api_instance = docspace_api_sdk.ProvidersApi(api_client)
    preview_provider_models_request_dto = docspace_api_sdk.PreviewProviderModelsRequestDto() # PreviewProviderModelsRequestDto |  (optional)

    try:
        # Preview models for a new AI provider
        api_response = api_instance.preview_provider_models(preview_provider_models_request_dto=preview_provider_models_request_dto)
        print("The response of ProvidersApi->preview_provider_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->preview_provider_models: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of models with default settings |  * X-RateLimit-Limit - Rate limit: 10 requests per 1 minutes per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**400** | Invalid connection data or unsupported provider type |  -  |
**403** | You don't have enough permission to manage providers |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_default_provider**
> DefaultProviderWrapper set_default_provider(set_default_provider_request_dto=set_default_provider_request_dto)

Sets the default AI provider and model for the current tenant.
The specified provider and model will be used as the default for all new AI chat sessions within the tenant.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_default_provider_request_dto** | [**SetDefaultProviderRequestDto**](SetDefaultProviderRequestDto.md)|  | [optional] 

### Return type

[**DefaultProviderWrapper**](DefaultProviderWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.default_provider_wrapper import DefaultProviderWrapper
from docspace_api_sdk.models.set_default_provider_request_dto import SetDefaultProviderRequestDto
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
    api_instance = docspace_api_sdk.ProvidersApi(api_client)
    set_default_provider_request_dto = docspace_api_sdk.SetDefaultProviderRequestDto() # SetDefaultProviderRequestDto |  (optional)

    try:
        # Set the default AI provider
        api_response = api_instance.set_default_provider(set_default_provider_request_dto=set_default_provider_request_dto)
        print("The response of ProvidersApi->set_default_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->set_default_provider: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default provider information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You don't have enough permission to manage providers |  -  |
**404** | Provider not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_provider**
> AiProviderWrapper update_provider(id, update_provider_body)

Updates the configuration of an existing AI provider, including its display title, API endpoint URL, and authentication key.
Only the fields provided in the request body will be updated. This action is rate-limited.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the AI provider to update. | 
 **update_provider_body** | [**UpdateProviderBody**](UpdateProviderBody.md)| The AI provider configuration parameters to update. | 

### Return type

[**AiProviderWrapper**](AiProviderWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_provider_wrapper import AiProviderWrapper
from docspace_api_sdk.models.update_provider_body import UpdateProviderBody
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
    api_instance = docspace_api_sdk.ProvidersApi(api_client)
    id = 1 # int | The identifier of the AI provider to update.
    update_provider_body = docspace_api_sdk.UpdateProviderBody() # UpdateProviderBody | The AI provider configuration parameters to update.

    try:
        # Update an AI provider
        api_response = api_instance.update_provider(id, update_provider_body)
        print("The response of ProvidersApi->update_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->update_provider: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated AI provider details |  * X-RateLimit-Limit - Rate limit: 10 requests per 1 minutes per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**400** | Invalid connection data or provider with this name already exists |  -  |
**403** | You don't have enough permission to manage providers |  -  |
**404** | The provider with the specified ID was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

