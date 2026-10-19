# docspace_api_sdk.OpenAIPassthroughApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_openai_chat_completions**](#ai_openai_chat_completions) | **POST** /api/2.0/ai/openai/{profileId}/v1/chat/completions | OpenAI chat completions passthrough
[**ai_openai_images_generations**](#ai_openai_images_generations) | **POST** /api/2.0/ai/openai/{profileId}/v1/images/generations | OpenAI image generation passthrough


# **ai_openai_chat_completions**
> Dict[str, Optional[object]] ai_openai_chat_completions(profile_id, ai_openai_chat_completions_request)

OpenAI-compatible chat completions for the document editor's AI plugin. The profile is resolved server-side, its credentials are attached, and the body is forwarded to the provider as sent - the payload is owned by the plugin's SDK on one end and the provider on the other - except that a JSON body which names no `model` gets the profile's model filled in; a `model` the body carries wins. The provider's 4xx answers are relayed with their status and body, so a 429 and the provider's own error envelope surface as they stand; a 5xx from the provider or from the hop in front of it is not relayed - its detail stays in the server log and the call answers a fixed 502 envelope. A client disconnect cancels the provider call.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The AI provider profile identifier. | 
 **ai_openai_chat_completions_request** | [**Dict[str, Optional[object]]**](object.md)| An OpenAI Chat Completions request, forwarded to the provider as sent. The shape is the provider's, not this API's, so consult the provider's own reference. The credentials come from the profile in the path and must not be sent here; the profile's model is used when the body names none, and a `model` in the body takes precedence. | 

### Return type

**Dict[str, Optional[object]]**

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

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

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.OpenAIPassthroughApi(api_client)
    profile_id = '00000000-0000-0000-0000-000000000000' # str | The AI provider profile identifier.
    ai_openai_chat_completions_request = None # Dict[str, Optional[object]] | An OpenAI Chat Completions request, forwarded to the provider as sent. The shape is the provider's, not this API's, so consult the provider's own reference. The credentials come from the profile in the path and must not be sent here; the profile's model is used when the body names none, and a `model` in the body takes precedence.

    try:
        # OpenAI chat completions passthrough
        api_response = api_instance.ai_openai_chat_completions(profile_id, ai_openai_chat_completions_request)
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
**200** | The provider's own response, relayed with its status and content type (a 5xx excepted). |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**404** | No profile with this identifier exists for the caller. |  -  |
**413** | The request body is larger than this route accepts. |  -  |
**429** | Relayed verbatim from the AI provider, which is rate-limiting this portal's key. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |
**502** | The provider, or the hop in front of it, failed or answered a 5xx; the detail is in the server log. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_openai_images_generations**
> Dict[str, object] ai_openai_images_generations(profile_id, ai_openai_images_generations_request)

OpenAI-compatible image generation for the document editor's AI plugin, working as the chat-completions passthrough does: the profile named by `profileId` is resolved server-side, its credentials are attached, and the body reaches the provider as sent. The documented OpenAI fields are checked first - `prompt` has to be a non-empty string, `n` a positive integer, `model`, `size`, `quality`, `style` and `response_format` strings when present - and a body failing that answers 400 instead of whatever the provider would have made of it; fields outside that set are passed on untouched. The provider's 4xx status and body are relayed, so its 429 and its own error envelope surface as they stand; a 5xx is replaced by a fixed 502 envelope with the detail kept in the server log. A body larger than this route accepts is refused before it is forwarded. A client disconnect aborts the provider call.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The AI provider profile identifier. | 
 **ai_openai_images_generations_request** | [**Dict[str, Optional[object]]**](object.md)| An OpenAI image-generation request, forwarded to the provider as sent once its documented fields pass a type check. The shape is the provider's, not this API's, and the credentials come from the profile in the path. | 

### Return type

**Dict[str, object]**

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

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

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.OpenAIPassthroughApi(api_client)
    profile_id = '00000000-0000-0000-0000-000000000000' # str | The AI provider profile identifier.
    ai_openai_images_generations_request = None # Dict[str, Optional[object]] | An OpenAI image-generation request, forwarded to the provider as sent once its documented fields pass a type check. The shape is the provider's, not this API's, and the credentials come from the profile in the path.

    try:
        # OpenAI image generation passthrough
        api_response = api_instance.ai_openai_images_generations(profile_id, ai_openai_images_generations_request)
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
**200** | The provider's own response, relayed with its status and content type (a 5xx excepted). |  -  |
**400** | `prompt` is missing or empty, `n` is not a positive integer, or a documented string field has another type. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**404** | No profile with this identifier exists for the caller. |  -  |
**413** | The request body is larger than this route accepts. |  -  |
**429** | Relayed verbatim from the AI provider, which is rate-limiting this portal's key. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |
**502** | The provider, or the hop in front of it, failed or answered a 5xx; the detail is in the server log. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

