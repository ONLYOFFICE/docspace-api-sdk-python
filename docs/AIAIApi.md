# docspace_api_sdk.AIApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_ai_approve_tool_call**](#ai_ai_approve_tool_call) | **POST** /api/2.0/ai/ai/approve-tool-call | Approve tool call
[**ai_ai_deny_tool_call**](#ai_ai_deny_tool_call) | **POST** /api/2.0/ai/ai/deny-tool-call | Deny tool call
[**ai_ai_regenerate_stream**](#ai_ai_regenerate_stream) | **POST** /api/2.0/ai/ai/regenerate-stream | Regenerate stream
[**ai_ai_send**](#ai_ai_send) | **POST** /api/2.0/ai/ai/send | Send
[**ai_ai_send_custom**](#ai_ai_send_custom) | **POST** /api/2.0/ai/ai/send-custom | Send custom
[**ai_ai_send_with_stream**](#ai_ai_send_with_stream) | **POST** /api/2.0/ai/ai/send-with-stream | Send with stream
[**ai_ai_send_with_stream_open_ai**](#ai_ai_send_with_stream_open_ai) | **POST** /api/2.0/ai/ai/send-with-stream-openai | Send with stream open ai


# **ai_ai_approve_tool_call**
> AiChatEvent ai_ai_approve_tool_call(ai_ai_approve_tool_call_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_ai_approve_tool_call_request** | [**AiAiApproveToolCallRequest**](AiAiApproveToolCallRequest.md)|  | 

### Return type

[**AiChatEvent**](AiChatEvent.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_ai_approve_tool_call_request import AiAiApproveToolCallRequest
from docspace_api_sdk.models.ai_chat_event import AiChatEvent
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AIApi(api_client)
    ai_ai_approve_tool_call_request = docspace_api_sdk.AiAiApproveToolCallRequest() # AiAiApproveToolCallRequest | 

    try:
        # Approve tool call
        api_response = api_instance.ai_ai_approve_tool_call(ai_ai_approve_tool_call_request)
        print("The response of AIApi->ai_ai_approve_tool_call:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIApi->ai_ai_approve_tool_call: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-ndjson, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newline-delimited stream of chat events — one JSON `ChatEvent` object per line. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_ai_deny_tool_call**
> AiChatEvent ai_ai_deny_tool_call(ai_ai_tool_call_data)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_ai_tool_call_data** | [**AiAiToolCallData**](AiAiToolCallData.md)|  | 

### Return type

[**AiChatEvent**](AiChatEvent.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_ai_tool_call_data import AiAiToolCallData
from docspace_api_sdk.models.ai_chat_event import AiChatEvent
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AIApi(api_client)
    ai_ai_tool_call_data = docspace_api_sdk.AiAiToolCallData() # AiAiToolCallData | 

    try:
        # Deny tool call
        api_response = api_instance.ai_ai_deny_tool_call(ai_ai_tool_call_data)
        print("The response of AIApi->ai_ai_deny_tool_call:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIApi->ai_ai_deny_tool_call: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-ndjson, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newline-delimited stream of chat events — one JSON `ChatEvent` object per line. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_ai_regenerate_stream**
> AiChatEvent ai_ai_regenerate_stream(ai_ai_regenerate_stream_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_ai_regenerate_stream_request** | [**AiAiRegenerateStreamRequest**](AiAiRegenerateStreamRequest.md)|  | 

### Return type

[**AiChatEvent**](AiChatEvent.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_ai_regenerate_stream_request import AiAiRegenerateStreamRequest
from docspace_api_sdk.models.ai_chat_event import AiChatEvent
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AIApi(api_client)
    ai_ai_regenerate_stream_request = docspace_api_sdk.AiAiRegenerateStreamRequest() # AiAiRegenerateStreamRequest | 

    try:
        # Regenerate stream
        api_response = api_instance.ai_ai_regenerate_stream(ai_ai_regenerate_stream_request)
        print("The response of AIApi->ai_ai_regenerate_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIApi->ai_ai_regenerate_stream: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-ndjson, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newline-delimited stream of chat events — one JSON `ChatEvent` object per line. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_ai_send**
> AiThreadMessageLike ai_ai_send(ai_ai_send_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_ai_send_request** | [**AiAiSendRequest**](AiAiSendRequest.md)|  | 

### Return type

[**AiThreadMessageLike**](AiThreadMessageLike.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_ai_send_request import AiAiSendRequest
from docspace_api_sdk.models.ai_thread_message_like import AiThreadMessageLike
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AIApi(api_client)
    ai_ai_send_request = docspace_api_sdk.AiAiSendRequest() # AiAiSendRequest | 

    try:
        # Send
        api_response = api_instance.ai_ai_send(ai_ai_send_request)
        print("The response of AIApi->ai_ai_send:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIApi->ai_ai_send: %s\n" % e)
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

# **ai_ai_send_custom**
> AiThreadMessageLike ai_ai_send_custom(ai_ai_send_custom_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_ai_send_custom_request** | [**AiAiSendCustomRequest**](AiAiSendCustomRequest.md)|  | 

### Return type

[**AiThreadMessageLike**](AiThreadMessageLike.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_ai_send_custom_request import AiAiSendCustomRequest
from docspace_api_sdk.models.ai_thread_message_like import AiThreadMessageLike
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AIApi(api_client)
    ai_ai_send_custom_request = docspace_api_sdk.AiAiSendCustomRequest() # AiAiSendCustomRequest | 

    try:
        # Send custom
        api_response = api_instance.ai_ai_send_custom(ai_ai_send_custom_request)
        print("The response of AIApi->ai_ai_send_custom:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIApi->ai_ai_send_custom: %s\n" % e)
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

# **ai_ai_send_with_stream**
> AiChatEvent ai_ai_send_with_stream(ai_ai_send_stream_body)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_ai_send_stream_body** | [**AiAiSendStreamBody**](AiAiSendStreamBody.md)|  | 

### Return type

[**AiChatEvent**](AiChatEvent.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_ai_send_stream_body import AiAiSendStreamBody
from docspace_api_sdk.models.ai_chat_event import AiChatEvent
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AIApi(api_client)
    ai_ai_send_stream_body = docspace_api_sdk.AiAiSendStreamBody() # AiAiSendStreamBody | 

    try:
        # Send with stream
        api_response = api_instance.ai_ai_send_with_stream(ai_ai_send_stream_body)
        print("The response of AIApi->ai_ai_send_with_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIApi->ai_ai_send_with_stream: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-ndjson, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newline-delimited stream of chat events — one JSON `ChatEvent` object per line. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_ai_send_with_stream_open_ai**
> AiOpenAIStreamChunk ai_ai_send_with_stream_open_ai(ai_ai_send_stream_body)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_ai_send_stream_body** | [**AiAiSendStreamBody**](AiAiSendStreamBody.md)|  | 

### Return type

[**AiOpenAIStreamChunk**](AiOpenAIStreamChunk.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_ai_send_stream_body import AiAiSendStreamBody
from docspace_api_sdk.models.ai_open_ai_stream_chunk import AiOpenAIStreamChunk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AIApi(api_client)
    ai_ai_send_stream_body = docspace_api_sdk.AiAiSendStreamBody() # AiAiSendStreamBody | 

    try:
        # Send with stream open ai
        api_response = api_instance.ai_ai_send_with_stream_open_ai(ai_ai_send_stream_body)
        print("The response of AIApi->ai_ai_send_with_stream_open_ai:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIApi->ai_ai_send_with_stream_open_ai: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/event-stream, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server-sent events stream of OpenAI `chat.completion.chunk` objects, terminated by a `[DONE]` sentinel. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

