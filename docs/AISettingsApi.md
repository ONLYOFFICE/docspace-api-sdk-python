# docspace_api_sdk.SettingsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ai_settings**](#get_ai_settings) | **GET** /api/2.0/ai/config | Get AI settings
[**get_ai_user_settings**](#get_ai_user_settings) | **GET** /api/2.0/ai/config/user | Get per-user AI settings
[**get_vectorization_settings**](#get_vectorization_settings) | **GET** /api/2.0/ai/config/vectorization | Get vectorization settings
[**get_web_search_settings**](#get_web_search_settings) | **GET** /api/2.0/ai/config/web-search | Get web search settings
[**set_ai_user_settings**](#set_ai_user_settings) | **PUT** /api/2.0/ai/config/user | Update per-user AI settings
[**set_vectorization_settings**](#set_vectorization_settings) | **PUT** /api/2.0/ai/config/vectorization | Update vectorization settings
[**set_web_search_settings**](#set_web_search_settings) | **PUT** /api/2.0/ai/config/web-search | Update web search settings


# **get_ai_settings**
> AiSettingsWrapper get_ai_settings()

Retrieves the combined AI configuration for the current portal, including the status of web search,
vectorization, and AI readiness, along with tool names and the portal MCP server identifier.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**AiSettingsWrapper**](AiSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_settings_wrapper import AiSettingsWrapper
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
    api_instance = docspace_api_sdk.SettingsApi(api_client)

    try:
        # Get AI settings
        api_response = api_instance.get_ai_settings()
        print("The response of SettingsApi->get_ai_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_ai_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current AI settings |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_user_settings**
> AiUserSettingsWrapper get_ai_user_settings()

Retrieves the current user's AI settings, including the recommended model banner visibility preference.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**AiUserSettingsWrapper**](AiUserSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_user_settings_wrapper import AiUserSettingsWrapper
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
    api_instance = docspace_api_sdk.SettingsApi(api_client)

    try:
        # Get per-user AI settings
        api_response = api_instance.get_ai_user_settings()
        print("The response of SettingsApi->get_ai_user_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_ai_user_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current per-user AI settings |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vectorization_settings**
> VectorizationSettingsWrapper get_vectorization_settings()

Retrieves the current embedding provider settings used for document vectorization,
including the configured provider type and whether the API key needs to be reset.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**VectorizationSettingsWrapper**](VectorizationSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.vectorization_settings_wrapper import VectorizationSettingsWrapper
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
    api_instance = docspace_api_sdk.SettingsApi(api_client)

    try:
        # Get vectorization settings
        api_response = api_instance.get_vectorization_settings()
        print("The response of SettingsApi->get_vectorization_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_vectorization_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current vectorization settings |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_search_settings**
> WebSearchSettingsWrapper get_web_search_settings()

Retrieves the current web search integration settings for AI chat sessions,
including whether web search is enabled, the configured search engine type, and whether the API key needs to be reset.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**WebSearchSettingsWrapper**](WebSearchSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.web_search_settings_wrapper import WebSearchSettingsWrapper
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
    api_instance = docspace_api_sdk.SettingsApi(api_client)

    try:
        # Get web search settings
        api_response = api_instance.get_web_search_settings()
        print("The response of SettingsApi->get_web_search_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_web_search_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current web search settings |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_ai_user_settings**
> AiUserSettingsWrapper set_ai_user_settings(set_ai_user_settings_request_dto=set_ai_user_settings_request_dto)

Updates the current user's AI recommended model banner visibility preferences.
Each user's settings are stored independently.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_ai_user_settings_request_dto** | [**SetAiUserSettingsRequestDto**](SetAiUserSettingsRequestDto.md)|  | [optional] 

### Return type

[**AiUserSettingsWrapper**](AiUserSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_user_settings_wrapper import AiUserSettingsWrapper
from docspace_api_sdk.models.set_ai_user_settings_request_dto import SetAiUserSettingsRequestDto
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
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    set_ai_user_settings_request_dto = docspace_api_sdk.SetAiUserSettingsRequestDto() # SetAiUserSettingsRequestDto |  (optional)

    try:
        # Update per-user AI settings
        api_response = api_instance.set_ai_user_settings(set_ai_user_settings_request_dto=set_ai_user_settings_request_dto)
        print("The response of SettingsApi->set_ai_user_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->set_ai_user_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated per-user AI settings |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_vectorization_settings**
> VectorizationSettingsWrapper set_vectorization_settings(set_embedding_config_request_body)

Configures the embedding provider used for document vectorization at the portal level.
Vectorization enables semantic search and knowledge retrieval capabilities in AI chat sessions.
Allows selecting the embedding provider type and providing the API key for the chosen provider.
Only portal administrators can modify these settings.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_embedding_config_request_body** | [**SetEmbeddingConfigRequestBody**](SetEmbeddingConfigRequestBody.md)| The embedding provider configuration parameters. | 

### Return type

[**VectorizationSettingsWrapper**](VectorizationSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.set_embedding_config_request_body import SetEmbeddingConfigRequestBody
from docspace_api_sdk.models.vectorization_settings_wrapper import VectorizationSettingsWrapper
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
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    set_embedding_config_request_body = docspace_api_sdk.SetEmbeddingConfigRequestBody() # SetEmbeddingConfigRequestBody | The embedding provider configuration parameters.

    try:
        # Update vectorization settings
        api_response = api_instance.set_vectorization_settings(set_embedding_config_request_body)
        print("The response of SettingsApi->set_vectorization_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->set_vectorization_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated vectorization settings |  * X-RateLimit-Limit - Rate limit: 10 requests per 1 minutes per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_web_search_settings**
> WebSearchSettingsWrapper set_web_search_settings(set_web_search_settings_request_body)

Configures the web search integration for AI chat sessions at the portal level.
Allows enabling or disabling web search, selecting the search engine type, and providing the API key for the chosen engine.
Only portal administrators can modify these settings.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_web_search_settings_request_body** | [**SetWebSearchSettingsRequestBody**](SetWebSearchSettingsRequestBody.md)| The web search configuration parameters. | 

### Return type

[**WebSearchSettingsWrapper**](WebSearchSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.set_web_search_settings_request_body import SetWebSearchSettingsRequestBody
from docspace_api_sdk.models.web_search_settings_wrapper import WebSearchSettingsWrapper
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
    api_instance = docspace_api_sdk.SettingsApi(api_client)
    set_web_search_settings_request_body = docspace_api_sdk.SetWebSearchSettingsRequestBody() # SetWebSearchSettingsRequestBody | The web search configuration parameters.

    try:
        # Update web search settings
        api_response = api_instance.set_web_search_settings(set_web_search_settings_request_body)
        print("The response of SettingsApi->set_web_search_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->set_web_search_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated web search settings |  * X-RateLimit-Limit - Rate limit: 10 requests per 1 minutes per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

