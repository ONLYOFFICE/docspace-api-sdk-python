# docspace_api_sdk.AIApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_approve_tool_call**](#ai_approve_tool_call) | **POST** /api/2.0/ai/ai/approve-tool-call | Approve tool call
[**ai_deny_tool_call**](#ai_deny_tool_call) | **POST** /api/2.0/ai/ai/deny-tool-call | Deny tool call
[**ai_regenerate_stream**](#ai_regenerate_stream) | **POST** /api/2.0/ai/ai/regenerate-stream | Regenerate stream
[**ai_send**](#ai_send) | **POST** /api/2.0/ai/ai/send | Run an AI action
[**ai_send_custom**](#ai_send_custom) | **POST** /api/2.0/ai/ai/send-custom | Send custom
[**ai_send_with_stream**](#ai_send_with_stream) | **POST** /api/2.0/ai/ai/send-with-stream | Send with stream
[**ai_send_with_stream_open_ai**](#ai_send_with_stream_open_ai) | **POST** /api/2.0/ai/ai/send-with-stream-openai | Stream a chat in OpenAI format


# **ai_approve_tool_call**
> AiChatEvent ai_approve_tool_call(ai_approve_tool_call_request)

Resumes a chat round that a tool call has paused, and streams the continuation as newline-delimited `ChatEvent` objects. The result supplied in the request is persisted onto the assistant message that issued the call, so the tool is not executed here - the caller runs it and reports the outcome. The round continues against the augmented history and may pause again on a further tool call. Call `POST api/2.0/ai/ai/deny-tool-call` instead to refuse the call and let the model answer without it.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_approve_tool_call_request** | [**AiApproveToolCallRequest**](AiApproveToolCallRequest.md)|  | 

### Return type

[**AiChatEvent**](AiChatEvent.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_approve_tool_call_request import AiApproveToolCallRequest
from docspace_api_sdk.models.ai_chat_event import AiChatEvent
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
    api_instance = docspace_api_sdk.AIApi(api_client)
    ai_approve_tool_call_request = docspace_api_sdk.AiApproveToolCallRequest() # AiApproveToolCallRequest | 

    try:
        # Approve tool call
        api_response = api_instance.ai_approve_tool_call(ai_approve_tool_call_request)
        print("The response of AIApi->ai_approve_tool_call:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIApi->ai_approve_tool_call: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-ndjson, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newline-delimited stream of chat events — one JSON `ChatEvent` object per line. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_deny_tool_call**
> AiChatEvent ai_deny_tool_call(ai_tool_call_data)

Refuses the tool call a chat round is paused on and resumes it immediately, streaming the continuation as newline-delimited `ChatEvent` objects. The literal `User deny tool call` is persisted in place of the tool result, so the model sees an explicit refusal rather than a missing answer and may reply without the tool or ask for something else. Nothing is executed and no result is accepted from the caller. Use `POST api/2.0/ai/ai/approve-tool-call` to supply a result instead.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_tool_call_data** | [**AiToolCallData**](AiToolCallData.md)|  | 

### Return type

[**AiChatEvent**](AiChatEvent.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_chat_event import AiChatEvent
from docspace_api_sdk.models.ai_tool_call_data import AiToolCallData
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
    api_instance = docspace_api_sdk.AIApi(api_client)
    ai_tool_call_data = docspace_api_sdk.AiToolCallData() # AiToolCallData | 

    try:
        # Deny tool call
        api_response = api_instance.ai_deny_tool_call(ai_tool_call_data)
        print("The response of AIApi->ai_deny_tool_call:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIApi->ai_deny_tool_call: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-ndjson, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newline-delimited stream of chat events — one JSON `ChatEvent` object per line. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_regenerate_stream**
> AiChatEvent ai_regenerate_stream(ai_regenerate_stream_request)

Re-rolls the last assistant reply of an existing thread: every message after the last user message - the previous reply and any tool-call hops - is dropped, and a fresh reply is streamed as newline-delimited `ChatEvent` objects against the unchanged prompt. The thread has to exist already, `threadId` is required, and no title is generated. The dropped messages are gone for good, so this is a destructive operation on the thread's tail rather than a retry that keeps both answers. Unlike `send-with-stream` the profile is not verified before the stream opens, so an unusable model surfaces as an error frame inside the 200 rather than as a 4xx.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_regenerate_stream_request** | [**AiRegenerateStreamRequest**](AiRegenerateStreamRequest.md)|  | 

### Return type

[**AiChatEvent**](AiChatEvent.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_chat_event import AiChatEvent
from docspace_api_sdk.models.ai_regenerate_stream_request import AiRegenerateStreamRequest
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
    api_instance = docspace_api_sdk.AIApi(api_client)
    ai_regenerate_stream_request = docspace_api_sdk.AiRegenerateStreamRequest() # AiRegenerateStreamRequest | 

    try:
        # Regenerate stream
        api_response = api_instance.ai_regenerate_stream(ai_regenerate_stream_request)
        print("The response of AIApi->ai_regenerate_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIApi->ai_regenerate_stream: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-ndjson, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newline-delimited stream of chat events — one JSON `ChatEvent` object per line. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_send**
> AiThreadMessageLike ai_send(ai_send_request)

Runs one AI action and returns the whole answer as a single JSON document. The model is the profile bound to `actionType`, falling back to the `Default` assignment slot, so this operation accepts no `profileId` of its own. `actionType` has to be a known action and `userMessage` has to carry text or an attachment, or the call answers 400 before anything runs. Nothing is persisted - no thread is opened, no message is stored and no title is generated - which makes it the one to use for a stand-alone completion rather than for a conversation. `entityId` and `contextEntityId` set the scope of the round, which decides the workspace context and the custom MCP servers it may reach. For a conversation that keeps its history, use `POST api/2.0/ai/ai/send-with-stream` instead.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_send_request** | [**AiSendRequest**](AiSendRequest.md)|  | 

### Return type

[**AiThreadMessageLike**](AiThreadMessageLike.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_send_request import AiSendRequest
from docspace_api_sdk.models.ai_thread_message_like import AiThreadMessageLike
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
    api_instance = docspace_api_sdk.AIApi(api_client)
    ai_send_request = docspace_api_sdk.AiSendRequest() # AiSendRequest | 

    try:
        # Run an AI action
        api_response = api_instance.ai_send(ai_send_request)
        print("The response of AIApi->ai_send:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIApi->ai_send: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The assistant's reply as one message. Nothing was persisted. |  -  |
**400** | `actionType` is missing or unknown, or `userMessage` carries neither text nor an attachment. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_send_custom**
> AiThreadMessageLike ai_send_custom(ai_send_custom_request)

Runs a free-form one-turn call against a system prompt supplied in the request, with no thread, no history and nothing persisted. The model is the explicit `profileId` when it resolves, otherwise the `Default` assignment slot. `systemPrompt` is required and `userMessage` has to carry text or an attachment, or the call answers 400 before anything runs. The shape of the answer depends on the body rather than on the route: with `isStream: true` it arrives as a newline-delimited stream of chat events, and without it as a single JSON document, so a client has to handle both; `isStream` has to be a real boolean when sent, a string is refused. Use `POST api/2.0/ai/ai/send` when the prompt should come from the portal's own action configuration instead of from the caller.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_send_custom_request** | [**AiSendCustomRequest**](AiSendCustomRequest.md)|  | 

### Return type

[**AiThreadMessageLike**](AiThreadMessageLike.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_send_custom_request import AiSendCustomRequest
from docspace_api_sdk.models.ai_thread_message_like import AiThreadMessageLike
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
    api_instance = docspace_api_sdk.AIApi(api_client)
    ai_send_custom_request = docspace_api_sdk.AiSendCustomRequest() # AiSendCustomRequest | 

    try:
        # Send custom
        api_response = api_instance.ai_send_custom(ai_send_custom_request)
        print("The response of AIApi->ai_send_custom:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIApi->ai_send_custom: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The assistant's reply as one message, or a newline-delimited stream of chat events when `isStream` was set. Nothing was persisted. |  -  |
**400** | `systemPrompt` is missing or empty, `userMessage` carries neither text nor an attachment, or `isStream` is not a boolean. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_send_with_stream**
> AiChatEvent ai_send_with_stream(ai_send_stream_body)

Runs one chat round and streams it back as newline-delimited `ChatEvent` objects. Omitting `threadId` opens a new thread, which requires that `entityId` names a room the caller can open and that a profile resolves for it; the user message and the reply are persisted either way, and a new thread also gets a generated title. The model is settled in a fixed order - an agent's assignment in scope overrides everything, then the explicit `profileId`, then the one stored on the thread, then the `Chat` assignment - and the effective profile is checked before the stream opens, so an unknown one fails with 400 rather than as an error buried in a 200. A tool call pauses the round and ends the stream; resume it with `POST api/2.0/ai/ai/approve-tool-call` or `POST api/2.0/ai/ai/deny-tool-call`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_send_stream_body** | [**AiSendStreamBody**](AiSendStreamBody.md)|  | 

### Return type

[**AiChatEvent**](AiChatEvent.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_chat_event import AiChatEvent
from docspace_api_sdk.models.ai_send_stream_body import AiSendStreamBody
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
    api_instance = docspace_api_sdk.AIApi(api_client)
    ai_send_stream_body = docspace_api_sdk.AiSendStreamBody() # AiSendStreamBody | 

    try:
        # Send with stream
        api_response = api_instance.ai_send_with_stream(ai_send_stream_body)
        print("The response of AIApi->ai_send_with_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIApi->ai_send_with_stream: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-ndjson, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newline-delimited stream of chat events — one JSON `ChatEvent` object per line. |  -  |
**400** | The prompt is empty, more attachments were sent than the limit allows, or no AI profile could be resolved for the requested action. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**402** | The portal has no paid AI quota left, so the profile bound to this action cannot be dispatched. `error` carries the portal's explanation in the caller's language. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**404** | The `entityId` names a room the caller cannot open, or no live profile is bound to it. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_send_with_stream_open_ai**
> AiOpenAIStreamChunk ai_send_with_stream_open_ai(ai_send_stream_body)

The same chat round as `send-with-stream`, re-encoded as a server-sent-events stream of OpenAI `chat.completion.chunk` objects terminated by a `[DONE]` sentinel. Thread handling, persistence, title generation and the profile pre-flight are identical, and a tool call ends the stream with `finish_reason: tool_calls` instead of a pause event - resume it through the same approve and deny operations. Unlike `send-with-stream` it does not reject an empty user message and does not enforce the per-kind attachment cap, so validate both before calling. Choose this route only for a client that already speaks the OpenAI wire format; `POST api/2.0/ai/ai/send-with-stream` is the native one.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_send_stream_body** | [**AiSendStreamBody**](AiSendStreamBody.md)|  | 

### Return type

[**AiOpenAIStreamChunk**](AiOpenAIStreamChunk.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_open_ai_stream_chunk import AiOpenAIStreamChunk
from docspace_api_sdk.models.ai_send_stream_body import AiSendStreamBody
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
    api_instance = docspace_api_sdk.AIApi(api_client)
    ai_send_stream_body = docspace_api_sdk.AiSendStreamBody() # AiSendStreamBody | 

    try:
        # Stream a chat in OpenAI format
        api_response = api_instance.ai_send_with_stream_open_ai(ai_send_stream_body)
        print("The response of AIApi->ai_send_with_stream_open_ai:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIApi->ai_send_with_stream_open_ai: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/event-stream, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server-sent events stream of OpenAI `chat.completion.chunk` objects, terminated by a `[DONE]` sentinel. |  -  |
**400** | The prompt is empty, or no AI profile could be resolved for the requested action. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**402** | The portal has no paid AI quota left, so the profile bound to this action cannot be dispatched. `error` carries the portal's explanation in the caller's language. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

