# docspace_api_sdk.ChatApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**continue_chat**](#continue_chat) | **POST** /api/2.0/ai/chats/{chatId}/messages | Send a message to an existing AI chat
[**delete_chat**](#delete_chat) | **DELETE** /api/2.0/ai/chats/{chatId} | Delete an AI chat
[**export_chat**](#export_chat) | **POST** /api/2.0/ai/chats/{chatId}/messages/export | Export AI chat messages to a file
[**get_chat**](#get_chat) | **GET** /api/2.0/ai/chats/{chatId} | Get an AI chat by ID
[**get_chat_models**](#get_chat_models) | **GET** /api/2.0/ai/chats/models | Get available AI models
[**get_chats**](#get_chats) | **GET** /api/2.0/ai/rooms/{roomId}/chats | Get AI chats in a room
[**get_messages**](#get_messages) | **GET** /api/2.0/ai/chats/{chatId}/messages | Get messages of an AI chat
[**get_user_chats_settings**](#get_user_chats_settings) | **GET** /api/2.0/ai/rooms/{roomId}/chats/config | Get user chat settings for a room
[**provide_permission**](#provide_permission) | **POST** /api/2.0/ai/chats/tool-permissions/{callId}/decision | Submit a tool execution permission decision
[**rename_chat**](#rename_chat) | **PUT** /api/2.0/ai/chats/{chatId} | Rename an AI chat
[**set_user_chats_settings**](#set_user_chats_settings) | **PUT** /api/2.0/ai/rooms/{roomId}/chats/config | Update user chat settings for a room
[**start_new_chat**](#start_new_chat) | **POST** /api/2.0/ai/rooms/{roomId}/chats | Start a new AI chat


# **continue_chat**
> continue_chat(chat_id, continue_chat_body)

Appends a new user message to an existing chat session and streams the AI assistant's response.
The full conversation history of the chat is sent to the AI provider to maintain context.
The response is delivered as a Server-Sent Events (SSE) stream with periodic keep-alive pings.
File references can optionally be attached to provide additional context.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_id** | **UUID**| The unique identifier of the existing AI chat session to continue. | 
 **continue_chat_body** | [**ContinueChatBody**](ContinueChatBody.md)| The message and optional file attachments. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.continue_chat_body import ContinueChatBody
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
    api_instance = docspace_api_sdk.ChatApi(api_client)
    chat_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The unique identifier of the existing AI chat session to continue.
    continue_chat_body = docspace_api_sdk.ContinueChatBody() # ContinueChatBody | The message and optional file attachments.

    try:
        # Send a message to an existing AI chat
        api_instance.continue_chat(chat_id, continue_chat_body)
    except Exception as e:
        print("Exception when calling ChatApi->continue_chat: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSE stream of ChatCompletion events (text/event-stream) |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The message is empty or one or more file attachments could not be processed |  -  |
**403** | You don't have enough permission to access the chat in this room |  -  |
**404** | The specified chat, room, or AI provider was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_chat**
> delete_chat(chat_id)

Permanently deletes an AI chat session along with all of its messages.
Only the chat owner can delete their own chat sessions. This action cannot be undone.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_id** | **UUID**| The unique identifier of the AI chat session to delete. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

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

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ChatApi(api_client)
    chat_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The unique identifier of the AI chat session to delete.

    try:
        # Delete an AI chat
        api_instance.delete_chat(chat_id)
    except Exception as e:
        print("Exception when calling ChatApi->delete_chat: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The chat was successfully deleted |  -  |
**404** | The chat with the specified ID was not found or does not belong to the current user |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_chat**
> export_chat(chat_id, export_chat_request_body)

Exports the entire message history of an AI chat session and saves it as a document in the specified folder.
The exported file is created with the provided title. Only the chat owner can export their own chat sessions.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_id** | **UUID**| The unique identifier of the AI chat session to export. | 
 **export_chat_request_body** | [**ExportChatRequestBody**](ExportChatRequestBody.md)| The export parameters including destination folder and file title. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.export_chat_request_body import ExportChatRequestBody
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
    api_instance = docspace_api_sdk.ChatApi(api_client)
    chat_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The unique identifier of the AI chat session to export.
    export_chat_request_body = docspace_api_sdk.ExportChatRequestBody() # ExportChatRequestBody | The export parameters including destination folder and file title.

    try:
        # Export AI chat messages to a file
        api_instance.export_chat(chat_id, export_chat_request_body)
    except Exception as e:
        print("Exception when calling ChatApi->export_chat: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The chat messages were successfully exported to the specified folder |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The chat with the specified ID was not found or does not belong to the current user |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat**
> ChatWrapper get_chat(chat_id)

Retrieves the metadata of a single AI chat session, including its title, creation date, and the user who created it.
Only the chat owner can access their own chat sessions.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_id** | **UUID**| The unique identifier of the AI chat session to retrieve. | 

### Return type

[**ChatWrapper**](ChatWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.chat_wrapper import ChatWrapper
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
    api_instance = docspace_api_sdk.ChatApi(api_client)
    chat_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The unique identifier of the AI chat session to retrieve.

    try:
        # Get an AI chat by ID
        api_response = api_instance.get_chat(chat_id)
        print("The response of ChatApi->get_chat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->get_chat: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chat session details |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The chat with the specified ID was not found or does not belong to the current user |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat_models**
> ModelArrayWrapper get_chat_models(provider=provider)

Returns the list of AI models available for chat conversations.
Optionally filters the results to models from a specific provider when the provider query parameter is specified.
Each model entry includes the provider ID, provider display name, and the model identifier.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **int**| The optional AI provider identifier to filter models by. When set to 0, models from all providers are returned. | [optional] 

### Return type

[**ModelArrayWrapper**](ModelArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.model_array_wrapper import ModelArrayWrapper
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
    api_instance = docspace_api_sdk.ChatApi(api_client)
    provider = 1 # int | The optional AI provider identifier to filter models by. When set to 0, models from all providers are returned. (optional)

    try:
        # Get available AI models
        api_response = api_instance.get_chat_models(provider=provider)
        print("The response of ChatApi->get_chat_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->get_chat_models: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of available AI models |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chats**
> ChatArrayWrapper get_chats(room_id, start_index=start_index, count=count)

Returns a paginated list of AI chat sessions that belong to the current user within the specified room.
Supports pagination via the startIndex and count query parameters. The total number of chats is included in the response metadata.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **int**| The identifier of the room whose AI chat sessions are to be listed. | 
 **start_index** | **int**| The number of items to skip before returning results (zero-based offset). Defaults to 0. | [optional] 
 **count** | **int**| The maximum number of items to return per page. Defaults to 100. | [optional] 

### Return type

[**ChatArrayWrapper**](ChatArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.chat_array_wrapper import ChatArrayWrapper
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
    api_instance = docspace_api_sdk.ChatApi(api_client)
    room_id = 42 # int | The identifier of the room whose AI chat sessions are to be listed.
    start_index = 0 # int | The number of items to skip before returning results (zero-based offset). Defaults to 0. (optional)
    count = 100 # int | The maximum number of items to return per page. Defaults to 100. (optional)

    try:
        # Get AI chats in a room
        api_response = api_instance.get_chats(room_id, start_index=start_index, count=count)
        print("The response of ChatApi->get_chats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->get_chats: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of chat sessions in the room |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to access chats in this room |  -  |
**404** | The room with the specified ID was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messages**
> MessageArrayWrapper get_messages(chat_id, start_index=start_index, count=count)

Returns a paginated list of messages from an AI chat session owned by the current user.
Each message includes its role (user or assistant), content blocks (text, tool calls, attachments), and timestamp.
Supports pagination via the startIndex and count query parameters. The total number of messages is included in the response metadata.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_id** | **UUID**| The unique identifier of the AI chat session whose messages are to be listed. | 
 **start_index** | **int**| The number of items to skip before returning results (zero-based offset). Defaults to 0. | [optional] 
 **count** | **int**| The maximum number of items to return per page. Defaults to 100. | [optional] 

### Return type

[**MessageArrayWrapper**](MessageArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.message_array_wrapper import MessageArrayWrapper
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
    api_instance = docspace_api_sdk.ChatApi(api_client)
    chat_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The unique identifier of the AI chat session whose messages are to be listed.
    start_index = 0 # int | The number of items to skip before returning results (zero-based offset). Defaults to 0. (optional)
    count = 100 # int | The maximum number of items to return per page. Defaults to 100. (optional)

    try:
        # Get messages of an AI chat
        api_response = api_instance.get_messages(chat_id, start_index=start_index, count=count)
        print("The response of ChatApi->get_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->get_messages: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of messages in the chat |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The chat with the specified ID was not found or does not belong to the current user |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_chats_settings**
> UserChatSettingsWrapper get_user_chats_settings(room_id)

Retrieves the current user's personal AI chat preferences for the specified room,
including whether web search is enabled for AI-assisted responses.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **int**| The identifier of the room whose chat settings are to be retrieved. | 

### Return type

[**UserChatSettingsWrapper**](UserChatSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.user_chat_settings_wrapper import UserChatSettingsWrapper
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
    api_instance = docspace_api_sdk.ChatApi(api_client)
    room_id = 42 # int | The identifier of the room whose chat settings are to be retrieved.

    try:
        # Get user chat settings for a room
        api_response = api_instance.get_user_chats_settings(room_id)
        print("The response of ChatApi->get_user_chats_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->get_user_chats_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current user chat settings |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to access chats in this room |  -  |
**404** | The room with the specified ID was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provide_permission**
> provide_permission(call_id, tool_decision_request_body)

Provides the user's approval or denial decision for a pending MCP (Model Context Protocol) tool execution request.
When an AI assistant attempts to invoke an external tool that requires explicit user consent,
the client receives a permission prompt via the SSE stream. This endpoint is used to submit the user's decision
so that the AI chat session can proceed accordingly.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**| The unique identifier of the pending tool execution call awaiting a permission decision. | 
 **tool_decision_request_body** | [**ToolDecisionRequestBody**](ToolDecisionRequestBody.md)| The permission decision parameters. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.tool_decision_request_body import ToolDecisionRequestBody
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
    api_instance = docspace_api_sdk.ChatApi(api_client)
    call_id = 'call_abc123' # str | The unique identifier of the pending tool execution call awaiting a permission decision.
    tool_decision_request_body = docspace_api_sdk.ToolDecisionRequestBody() # ToolDecisionRequestBody | The permission decision parameters.

    try:
        # Submit a tool execution permission decision
        api_instance.provide_permission(call_id, tool_decision_request_body)
    except Exception as e:
        print("Exception when calling ChatApi->provide_permission: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The permission decision was successfully recorded |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_chat**
> ChatWrapper rename_chat(chat_id, rename_chat_body)

Updates the display title of an existing AI chat session owned by the current user.
The new name must not exceed 255 characters.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_id** | **UUID**| The unique identifier of the AI chat session to rename. | 
 **rename_chat_body** | [**RenameChatBody**](RenameChatBody.md)| The new chat name. | 

### Return type

[**ChatWrapper**](ChatWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.chat_wrapper import ChatWrapper
from docspace_api_sdk.models.rename_chat_body import RenameChatBody
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
    api_instance = docspace_api_sdk.ChatApi(api_client)
    chat_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The unique identifier of the AI chat session to rename.
    rename_chat_body = docspace_api_sdk.RenameChatBody() # RenameChatBody | The new chat name.

    try:
        # Rename an AI chat
        api_response = api_instance.rename_chat(chat_id, rename_chat_body)
        print("The response of ChatApi->rename_chat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->rename_chat: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated chat session details |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The chat with the specified ID was not found or does not belong to the current user |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_chats_settings**
> UserChatSettingsWrapper set_user_chats_settings(room_id, set_user_chat_settings_request_body)

Saves the current user's personal AI chat preferences for the specified room.
Currently supports toggling the web search capability, which allows the AI assistant to search the internet when generating responses.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **int**| The identifier of the room whose chat settings are to be updated. | 
 **set_user_chat_settings_request_body** | [**SetUserChatSettingsRequestBody**](SetUserChatSettingsRequestBody.md)| The chat settings to apply. | 

### Return type

[**UserChatSettingsWrapper**](UserChatSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.set_user_chat_settings_request_body import SetUserChatSettingsRequestBody
from docspace_api_sdk.models.user_chat_settings_wrapper import UserChatSettingsWrapper
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
    api_instance = docspace_api_sdk.ChatApi(api_client)
    room_id = 42 # int | The identifier of the room whose chat settings are to be updated.
    set_user_chat_settings_request_body = docspace_api_sdk.SetUserChatSettingsRequestBody() # SetUserChatSettingsRequestBody | The chat settings to apply.

    try:
        # Update user chat settings for a room
        api_response = api_instance.set_user_chats_settings(room_id, set_user_chat_settings_request_body)
        print("The response of ChatApi->set_user_chats_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->set_user_chats_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated user chat settings |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | You don't have enough permission to access chats in this room |  -  |
**404** | The room with the specified ID was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_new_chat**
> start_new_chat(room_id, start_new_chat_body)

Creates a new AI chat session within the specified room and sends the initial message to the configured AI provider.
The response is delivered as a Server-Sent Events (SSE) stream containing completion chunks (text deltas, tool calls, tool results, and message lifecycle events)
with periodic keep-alive pings every 5 seconds. File references can be included as context for the AI model.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **int**| The identifier of the room in which to create the new AI chat session. | 
 **start_new_chat_body** | [**StartNewChatBody**](StartNewChatBody.md)| The initial message and optional file attachments. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.start_new_chat_body import StartNewChatBody
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
    api_instance = docspace_api_sdk.ChatApi(api_client)
    room_id = 42 # int | The identifier of the room in which to create the new AI chat session.
    start_new_chat_body = docspace_api_sdk.StartNewChatBody() # StartNewChatBody | The initial message and optional file attachments.

    try:
        # Start a new AI chat
        api_instance.start_new_chat(room_id, start_new_chat_body)
    except Exception as e:
        print("Exception when calling ChatApi->start_new_chat: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSE stream of ChatCompletion events (text/event-stream) |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The message is empty or one or more file attachments could not be processed |  -  |
**403** | You don't have enough permission to access the chat in this room |  -  |
**404** | The specified room or AI provider was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

