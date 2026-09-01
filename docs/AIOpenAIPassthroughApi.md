# docspace_api_sdk.OpenAIPassthroughApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_openai_chat_completions**](#ai_openai_chat_completions) | **POST** /api/2.0/ai/openai/{profileId}/v1/chat/completions | OpenAI-compatible chat completions proxied to the profile's provider
[**ai_openai_images_generations**](#ai_openai_images_generations) | **POST** /api/2.0/ai/openai/{profileId}/v1/images/generations | OpenAI-compatible image generation proxied to the profile's provider


# **ai_openai_chat_completions**
> AiSuccessResponse ai_openai_chat_completions(profile_id, request_body)

OpenAI-compatible chat completions for the document editor's AI plugin. The profile is resolved server-side, its credentials are attached, and the body is forwarded to the provider verbatim - the payload is owned by the plugin's SDK on one end and the provider on the other. A client disconnect cancels the provider call.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The AI provider profile identifier. | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.OpenAIPassthroughApi(api_client)
    profile_id = 'profile_id_example' # str | The AI provider profile identifier.
    request_body = None # Dict[str, object] | 

    try:
        # OpenAI-compatible chat completions proxied to the profile's provider
        api_response = api_instance.ai_openai_chat_completions(profile_id, request_body)
        print("The response of OpenAIPassthroughApi->ai_openai_chat_completions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenAIPassthroughApi->ai_openai_chat_completions: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_openai_images_generations**
> AiSuccessResponse ai_openai_images_generations(profile_id, request_body)

OpenAI-compatible image generation for the document editor's AI plugin. As with the chat-completions passthrough, the profile's credentials are attached server-side and the body reaches the provider unchanged.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The AI provider profile identifier. | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.OpenAIPassthroughApi(api_client)
    profile_id = 'profile_id_example' # str | The AI provider profile identifier.
    request_body = None # Dict[str, object] | 

    try:
        # OpenAI-compatible image generation proxied to the profile's provider
        api_response = api_instance.ai_openai_images_generations(profile_id, request_body)
        print("The response of OpenAIPassthroughApi->ai_openai_images_generations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenAIPassthroughApi->ai_openai_images_generations: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

