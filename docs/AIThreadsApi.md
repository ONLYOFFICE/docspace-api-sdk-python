# docspace_api_sdk.ThreadsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_threads_append_user_message**](#ai_threads_append_user_message) | **POST** /api/2.0/ai/threads/append-user-message | Append user message
[**ai_threads_clear_messages**](#ai_threads_clear_messages) | **DELETE** /api/2.0/ai/threads/clear-messages | Clear messages
[**ai_threads_create**](#ai_threads_create) | **POST** /api/2.0/ai/threads/create | Create
[**ai_threads_delete**](#ai_threads_delete) | **DELETE** /api/2.0/ai/threads/delete | Delete
[**ai_threads_delete_message**](#ai_threads_delete_message) | **DELETE** /api/2.0/ai/threads/delete-message | Delete message
[**ai_threads_get_by_id**](#ai_threads_get_by_id) | **GET** /api/2.0/ai/threads/get-by-id | Get by id
[**ai_threads_get_message_by_id**](#ai_threads_get_message_by_id) | **GET** /api/2.0/ai/threads/get-message-by-id | Get message by id
[**ai_threads_list**](#ai_threads_list) | **GET** /api/2.0/ai/threads/list | List
[**ai_threads_open_or_create**](#ai_threads_open_or_create) | **POST** /api/2.0/ai/threads/open-or-create | Open or create
[**ai_threads_read_messages**](#ai_threads_read_messages) | **GET** /api/2.0/ai/threads/read-messages | Read messages
[**ai_threads_regenerate_title**](#ai_threads_regenerate_title) | **POST** /api/2.0/ai/threads/regenerate-title | Regenerate title
[**ai_threads_rename**](#ai_threads_rename) | **PUT** /api/2.0/ai/threads/rename | Rename
[**ai_threads_touch**](#ai_threads_touch) | **POST** /api/2.0/ai/threads/touch | Touch
[**ai_threads_update_message**](#ai_threads_update_message) | **PUT** /api/2.0/ai/threads/update-message | Update message


# **ai_threads_append_user_message**
> AiThreadMessageLike ai_threads_append_user_message(ai_threads_append_user_message_request)

Persists a user message in a thread and bumps the thread's last-edit date so it resurfaces in the sidebar. Optionally rebinds the thread to another profile when the model changed mid-conversation.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_threads_append_user_message_request** | [**AiThreadsAppendUserMessageRequest**](AiThreadsAppendUserMessageRequest.md)|  | 

### Return type

[**AiThreadMessageLike**](AiThreadMessageLike.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_thread_message_like import AiThreadMessageLike
from docspace_api_sdk.models.ai_threads_append_user_message_request import AiThreadsAppendUserMessageRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ThreadsApi(api_client)
    ai_threads_append_user_message_request = docspace_api_sdk.AiThreadsAppendUserMessageRequest() # AiThreadsAppendUserMessageRequest | 

    try:
        # Append user message
        api_response = api_instance.ai_threads_append_user_message(ai_threads_append_user_message_request)
        print("The response of ThreadsApi->ai_threads_append_user_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadsApi->ai_threads_append_user_message: %s\n" % e)
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

# **ai_threads_clear_messages**
> AiSuccessResponse ai_threads_clear_messages(body)

Drops every message of a thread while keeping the thread itself, and bumps its last-edit date.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

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
    api_instance = docspace_api_sdk.ThreadsApi(api_client)
    body = 'body_example' # str | 

    try:
        # Clear messages
        api_response = api_instance.ai_threads_clear_messages(body)
        print("The response of ThreadsApi->ai_threads_clear_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadsApi->ai_threads_clear_messages: %s\n" % e)
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

# **ai_threads_create**
> AiThread ai_threads_create(ai_threads_create_request)

Creates a chat thread with a caller-supplied title. Use `open-or-create` instead when the title should be generated from the first user message.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_threads_create_request** | [**AiThreadsCreateRequest**](AiThreadsCreateRequest.md)|  | 

### Return type

[**AiThread**](AiThread.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_thread import AiThread
from docspace_api_sdk.models.ai_threads_create_request import AiThreadsCreateRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ThreadsApi(api_client)
    ai_threads_create_request = docspace_api_sdk.AiThreadsCreateRequest() # AiThreadsCreateRequest | 

    try:
        # Create
        api_response = api_instance.ai_threads_create(ai_threads_create_request)
        print("The response of ThreadsApi->ai_threads_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadsApi->ai_threads_create: %s\n" % e)
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

# **ai_threads_delete**
> AiSuccessResponse ai_threads_delete(body)

Deletes a chat thread together with its messages.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

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
    api_instance = docspace_api_sdk.ThreadsApi(api_client)
    body = 'body_example' # str | 

    try:
        # Delete
        api_response = api_instance.ai_threads_delete(body)
        print("The response of ThreadsApi->ai_threads_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadsApi->ai_threads_delete: %s\n" % e)
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

# **ai_threads_delete_message**
> AiSuccessResponse ai_threads_delete_message(body)

Deletes one chat message, leaving the rest of the thread untouched.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

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
    api_instance = docspace_api_sdk.ThreadsApi(api_client)
    body = 'body_example' # str | 

    try:
        # Delete message
        api_response = api_instance.ai_threads_delete_message(body)
        print("The response of ThreadsApi->ai_threads_delete_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadsApi->ai_threads_delete_message: %s\n" % e)
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

# **ai_threads_get_by_id**
> AiThread ai_threads_get_by_id(thread_id)

Returns one chat thread, or an empty result when the identifier is unknown.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| The chat thread identifier. | 

### Return type

[**AiThread**](AiThread.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_thread import AiThread
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ThreadsApi(api_client)
    thread_id = 'thread_id_example' # str | The chat thread identifier.

    try:
        # Get by id
        api_response = api_instance.ai_threads_get_by_id(thread_id)
        print("The response of ThreadsApi->ai_threads_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadsApi->ai_threads_get_by_id: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_threads_get_message_by_id**
> AiThreadMessageLike ai_threads_get_message_by_id(message_id)

Returns one chat message by its globally unique identifier.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| The globally unique chat message identifier. | 

### Return type

[**AiThreadMessageLike**](AiThreadMessageLike.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_thread_message_like import AiThreadMessageLike
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ThreadsApi(api_client)
    message_id = 'message_id_example' # str | The globally unique chat message identifier.

    try:
        # Get message by id
        api_response = api_instance.ai_threads_get_message_by_id(message_id)
        print("The response of ThreadsApi->ai_threads_get_message_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadsApi->ai_threads_get_message_by_id: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_threads_list**
> List[AiThread] ai_threads_list(entity_id=entity_id, count=count, cursor=cursor, query=query)

Lists the chat threads of the scope, most recently edited first. Supports cursor pagination and a server-side case-insensitive title search.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. | [optional] 
 **count** | **str**| The maximum number of items to return in one page. | [optional] 
 **cursor** | **str**| The keyset pagination cursor: the JSON-encoded sort key of the last item already received. Omit for the first page. | [optional] 
 **query** | **str**| The full-text query the thread list is filtered by. | [optional] 

### Return type

[**List[AiThread]**](AiThread.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_thread import AiThread
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ThreadsApi(api_client)
    entity_id = 'entity_id_example' # str | The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. (optional)
    count = 'count_example' # str | The maximum number of items to return in one page. (optional)
    cursor = 'cursor_example' # str | The keyset pagination cursor: the JSON-encoded sort key of the last item already received. Omit for the first page. (optional)
    query = 'query_example' # str | The full-text query the thread list is filtered by. (optional)

    try:
        # List
        api_response = api_instance.ai_threads_list(entity_id=entity_id, count=count, cursor=cursor, query=query)
        print("The response of ThreadsApi->ai_threads_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadsApi->ai_threads_list: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_threads_open_or_create**
> AiOpenOrCreateResult ai_threads_open_or_create(ai_threads_open_or_create_request)

Opens a chat thread and returns its history, or creates one with a title generated from the supplied first message. That first message is not persisted - the caller decides whether to follow up with `append-user-message`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_threads_open_or_create_request** | [**AiThreadsOpenOrCreateRequest**](AiThreadsOpenOrCreateRequest.md)|  | 

### Return type

[**AiOpenOrCreateResult**](AiOpenOrCreateResult.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_open_or_create_result import AiOpenOrCreateResult
from docspace_api_sdk.models.ai_threads_open_or_create_request import AiThreadsOpenOrCreateRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ThreadsApi(api_client)
    ai_threads_open_or_create_request = docspace_api_sdk.AiThreadsOpenOrCreateRequest() # AiThreadsOpenOrCreateRequest | 

    try:
        # Open or create
        api_response = api_instance.ai_threads_open_or_create(ai_threads_open_or_create_request)
        print("The response of ThreadsApi->ai_threads_open_or_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadsApi->ai_threads_open_or_create: %s\n" % e)
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

# **ai_threads_read_messages**
> List[AiThreadMessageLike] ai_threads_read_messages(thread_id, count=count, cursor=cursor, direction=direction)

Reads the messages of a thread, with the same cursor pagination as the thread list.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| The chat thread identifier. | 
 **count** | **str**| The maximum number of items to return in one page. | [optional] 
 **cursor** | **str**| The keyset pagination cursor: the JSON-encoded sort key of the last item already received. Omit for the first page. | [optional] 
 **direction** | **str**| The order the message page is read in. Only desc turns the read around and pages back from the newest message; omit for the forward read. | [optional] 

### Return type

[**List[AiThreadMessageLike]**](AiThreadMessageLike.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_thread_message_like import AiThreadMessageLike
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ThreadsApi(api_client)
    thread_id = 'thread_id_example' # str | The chat thread identifier.
    count = 'count_example' # str | The maximum number of items to return in one page. (optional)
    cursor = 'cursor_example' # str | The keyset pagination cursor: the JSON-encoded sort key of the last item already received. Omit for the first page. (optional)
    direction = 'direction_example' # str | The order the message page is read in. Only desc turns the read around and pages back from the newest message; omit for the forward read. (optional)

    try:
        # Read messages
        api_response = api_instance.ai_threads_read_messages(thread_id, count=count, cursor=cursor, direction=direction)
        print("The response of ThreadsApi->ai_threads_read_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadsApi->ai_threads_read_messages: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_threads_regenerate_title**
> str ai_threads_regenerate_title(ai_threads_regenerate_title_request)

Generates a fresh title from the thread's first user message and persists it. Fails when the thread has no user message yet.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_threads_regenerate_title_request** | [**AiThreadsRegenerateTitleRequest**](AiThreadsRegenerateTitleRequest.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_threads_regenerate_title_request import AiThreadsRegenerateTitleRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ThreadsApi(api_client)
    ai_threads_regenerate_title_request = docspace_api_sdk.AiThreadsRegenerateTitleRequest() # AiThreadsRegenerateTitleRequest | 

    try:
        # Regenerate title
        api_response = api_instance.ai_threads_regenerate_title(ai_threads_regenerate_title_request)
        print("The response of ThreadsApi->ai_threads_regenerate_title:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadsApi->ai_threads_regenerate_title: %s\n" % e)
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

# **ai_threads_rename**
> AiSuccessResponse ai_threads_rename(ai_threads_rename_request)

Renames a chat thread and bumps its last-edit date so the new title shows up in the sidebar.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_threads_rename_request** | [**AiThreadsRenameRequest**](AiThreadsRenameRequest.md)|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
from docspace_api_sdk.models.ai_threads_rename_request import AiThreadsRenameRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ThreadsApi(api_client)
    ai_threads_rename_request = docspace_api_sdk.AiThreadsRenameRequest() # AiThreadsRenameRequest | 

    try:
        # Rename
        api_response = api_instance.ai_threads_rename(ai_threads_rename_request)
        print("The response of ThreadsApi->ai_threads_rename:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadsApi->ai_threads_rename: %s\n" % e)
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

# **ai_threads_touch**
> AiSuccessResponse ai_threads_touch(ai_threads_touch_request)

Bumps a thread's last-edit date, and optionally rebinds it to another profile, when something other than a new message - a model switch, say - should resurface it.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_threads_touch_request** | [**AiThreadsTouchRequest**](AiThreadsTouchRequest.md)|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
from docspace_api_sdk.models.ai_threads_touch_request import AiThreadsTouchRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ThreadsApi(api_client)
    ai_threads_touch_request = docspace_api_sdk.AiThreadsTouchRequest() # AiThreadsTouchRequest | 

    try:
        # Touch
        api_response = api_instance.ai_threads_touch(ai_threads_touch_request)
        print("The response of ThreadsApi->ai_threads_touch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadsApi->ai_threads_touch: %s\n" % e)
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

# **ai_threads_update_message**
> AiSuccessResponse ai_threads_update_message(ai_threads_update_message_request)

Replaces the content of a chat message - used by the edit and regenerate flows that change a message outside the streaming lifecycle.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_threads_update_message_request** | [**AiThreadsUpdateMessageRequest**](AiThreadsUpdateMessageRequest.md)|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
from docspace_api_sdk.models.ai_threads_update_message_request import AiThreadsUpdateMessageRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ThreadsApi(api_client)
    ai_threads_update_message_request = docspace_api_sdk.AiThreadsUpdateMessageRequest() # AiThreadsUpdateMessageRequest | 

    try:
        # Update message
        api_response = api_instance.ai_threads_update_message(ai_threads_update_message_request)
        print("The response of ThreadsApi->ai_threads_update_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadsApi->ai_threads_update_message: %s\n" % e)
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

