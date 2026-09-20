# docspace_api_sdk.OpenAIPassthroughApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_openai_chat_completions**](#ai_openai_chat_completions) | **POST** /api/2.0/ai/openai/{profileId}/v1/chat/completions | OpenAI chat completions passthrough
[**ai_openai_images_generations**](#ai_openai_images_generations) | **POST** /api/2.0/ai/openai/{profileId}/v1/images/generations | OpenAI image generation passthrough


# **ai_openai_chat_completions**
> Dict[str, Optional[object]] ai_openai_chat_completions(profile_id, request_body)

OpenAI-compatible chat completions for the document editor's AI plugin. The profile is resolved server-side, its credentials are attached, and the body is forwarded to the provider verbatim - the payload is owned by the plugin's SDK on one end and the provider on the other. A client disconnect cancels the provider call.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The AI provider profile identifier. | 
 **request_body** | [**Dict[str, Optional[object]]**](object.md)| An OpenAI Chat Completions request, forwarded to the provider byte for byte. The shape is the provider's, not this API's, so consult the provider's own reference; the model and the credentials come from the profile in the path and must not be sent here. | 

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
    request_body = None # Dict[str, Optional[object]] | An OpenAI Chat Completions request, forwarded to the provider byte for byte. The shape is the provider's, not this API's, so consult the provider's own reference; the model and the credentials come from the profile in the path and must not be sent here.

    try:
        # OpenAI chat completions passthrough
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
**200** | The provider's own response, relayed verbatim with its status and content type. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**404** | No profile with this identifier exists for the caller. |  -  |
**413** | The request body is larger than this route accepts. |  -  |
**429** | Relayed verbatim from the AI provider, which is rate-limiting this portal's key. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |
**502** | The AI provider could not be reached, or answered with a failure of its own. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_openai_images_generations**
> Dict[str, Optional[object]] ai_openai_images_generations(profile_id, request_body)

OpenAI-compatible image generation for the document editor's AI plugin, working exactly as the chat-completions passthrough does: the profile named by `profileId` is resolved server-side, its credentials are attached, and the body reaches the provider unchanged. The provider's status and body are relayed verbatim, so its 429 and its own error envelope surface as they stand. A body larger than this route accepts is refused before it is forwarded. A client disconnect aborts the provider call.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The AI provider profile identifier. | 
 **request_body** | [**Dict[str, Optional[object]]**](object.md)| An OpenAI image-generation request, forwarded to the provider byte for byte. The shape is the provider's, not this API's, and the credentials come from the profile in the path. | 

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
    request_body = None # Dict[str, Optional[object]] | An OpenAI image-generation request, forwarded to the provider byte for byte. The shape is the provider's, not this API's, and the credentials come from the profile in the path.

    try:
        # OpenAI image generation passthrough
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
**200** | The provider's own response, relayed verbatim with its status and content type. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**404** | No profile with this identifier exists for the caller. |  -  |
**413** | The request body is larger than this route accepts. |  -  |
**429** | Relayed verbatim from the AI provider, which is rate-limiting this portal's key. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |
**502** | The AI provider could not be reached, or answered with a failure of its own. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

