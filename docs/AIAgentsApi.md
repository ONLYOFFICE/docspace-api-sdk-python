# docspace_api_sdk.AgentsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_agents_create**](#ai_agents_create) | **POST** /api/2.0/ai/agents | Create an agent
[**ai_agents_delete**](#ai_agents_delete) | **DELETE** /api/2.0/ai/agents/{id} | Delete an agent
[**ai_agents_get**](#ai_agents_get) | **GET** /api/2.0/ai/agents/{id} | Get an agent
[**ai_agents_list**](#ai_agents_list) | **GET** /api/2.0/ai/agents | List agents
[**ai_agents_news**](#ai_agents_news) | **GET** /api/2.0/ai/agents/news | List agent news items
[**ai_agents_reset_quota**](#ai_agents_reset_quota) | **PUT** /api/2.0/ai/agents/resetquota | Reset agents' quota
[**ai_agents_update**](#ai_agents_update) | **PUT** /api/2.0/ai/agents/{id} | Update an agent
[**ai_agents_update_quota**](#ai_agents_update_quota) | **PUT** /api/2.0/ai/agents/agentquota | Update agents' quota


# **ai_agents_create**
> AiFolderWrapper ai_agents_create(ai_agents_create_request)

Creates an AI agent room and binds a model to it, in that order. `profileId` is required, has to be a UUID, has to name an existing profile, and that profile has to support chat - an image-only model is refused here rather than failing on every later request. `prompt` is required and is stored on the room as its standing instruction with any markup stripped, so it cannot round-trip HTML into another user's reply. The two steps are not atomic: when the room is created but the model binding fails, the call reports an error and the room is left behind, so re-bind it with `PUT api/2.0/ai/agents/{id}` rather than creating a second one.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_agents_create_request** | [**AiAgentsCreateRequest**](AiAgentsCreateRequest.md)|  | 

### Return type

[**AiFolderWrapper**](AiFolderWrapper.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_agents_create_request import AiAgentsCreateRequest
from docspace_api_sdk.models.ai_folder_wrapper import AiFolderWrapper
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
    api_instance = docspace_api_sdk.AgentsApi(api_client)
    ai_agents_create_request = docspace_api_sdk.AiAgentsCreateRequest() # AiAgentsCreateRequest | 

    try:
        # Create an agent
        api_response = api_instance.ai_agents_create(ai_agents_create_request)
        print("The response of AgentsApi->ai_agents_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->ai_agents_create: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created agent room, with the model already bound to it. |  -  |
**400** | `profileId` is missing, is not a UUID, names no existing profile, or names one that does not support chat; or `prompt` is missing. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_agents_delete**
> AiFileOperationWrapper ai_agents_delete(id, ai_agents_delete_request)

Deletes an AI agent room. The ID has to be the room's integer identifier, and the body is forwarded to the DocSpace AI service unchanged, so it accepts the same options as deleting an ordinary room - `deleteAfter` among them. Deletion is asynchronous there: the answer is a file-operation payload to poll, not a completed result. The agent's model binding is deliberately left behind, because the upstream assignment API has no per-entry delete, so an orphaned assignment row survives the room.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The agent identifier. | 
 **ai_agents_delete_request** | [**AiAgentsDeleteRequest**](AiAgentsDeleteRequest.md)|  | 

### Return type

[**AiFileOperationWrapper**](AiFileOperationWrapper.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_agents_delete_request import AiAgentsDeleteRequest
from docspace_api_sdk.models.ai_file_operation_wrapper import AiFileOperationWrapper
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
    api_instance = docspace_api_sdk.AgentsApi(api_client)
    id = '1234' # str | The agent identifier.
    ai_agents_delete_request = docspace_api_sdk.AiAgentsDeleteRequest() # AiAgentsDeleteRequest | 

    try:
        # Delete an agent
        api_response = api_instance.ai_agents_delete(id, ai_agents_delete_request)
        print("The response of AgentsApi->ai_agents_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->ai_agents_delete: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The queued file operation. Deletion runs asynchronously, so poll DocSpace for its outcome. |  -  |
**400** | The agent ID is not a positive integer. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_agents_get**
> AiAgentsGet200Response ai_agents_get(id)

Returns one AI agent room, enriched with the `profileId` currently bound to it so an edit form can prefill its model selector. The ID is the room's integer identifier, and a non-integer value is refused rather than passed on to fail opaquely upstream. The binding lives in an assignment rather than on the room, so it is looked up separately: a missing or unreadable assignment simply leaves `profileId` out of the answer instead of failing the call. The standing instruction comes back on the room as `chatSettings.prompt`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The agent identifier. | 

### Return type

[**AiAgentsGet200Response**](AiAgentsGet200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_agents_get200_response import AiAgentsGet200Response
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
    api_instance = docspace_api_sdk.AgentsApi(api_client)
    id = '1234' # str | The agent identifier.

    try:
        # Get an agent
        api_response = api_instance.ai_agents_get(id)
        print("The response of AgentsApi->ai_agents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->ai_agents_get: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The agent room, with `profileId` added when a model is bound to it. |  -  |
**400** | The agent ID is not a positive integer. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_agents_list**
> AiFolderContentWrapper ai_agents_list(subject_id=subject_id, subject_owner_id=subject_owner_id, exclude_subject=exclude_subject, tags=tags, without_tags=without_tags, quota_filter=quota_filter, filter_value=filter_value, sort_by=sort_by, sort_order=sort_order, start_index=start_index, count=count)

Lists the portal's AI agent rooms. The query is forwarded unchanged to the DocSpace AI service, so it takes the same paging, sorting and filtering parameters as an ordinary room listing, and the answer is that service's folder-content payload rather than a shape of this API's own. Array and object query values are dropped rather than guessed at, so send flat strings. The profile bound to each agent is not included here - read one agent with `GET api/2.0/ai/agents/{id}` for that.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id** | **str**| Show only the agent rooms this user takes part in. | [optional] 
 **subject_owner_id** | **str**| Show only the agent rooms owned by this user. | [optional] 
 **exclude_subject** | **bool**| Invert the user filter: leave out what `subjectId` selects instead of keeping it. | [optional] 
 **tags** | **str**| Show only the agent rooms carrying these tags, comma-separated. | [optional] 
 **without_tags** | **bool**| Show only the agent rooms that carry no tags at all. | [optional] 
 **quota_filter** | **int**| Filter by quota kind: 0 for all, 1 for the default quota, 2 for a custom one. | [optional] 
 **filter_value** | **str**| Show only the agent rooms whose title matches this text. | [optional] 
 **sort_by** | **str**| Field to sort by, for example `DateAndTime`. | [optional] 
 **sort_order** | **str**| Sort direction, `ascending` or `descending`. | [optional] 
 **start_index** | **int**| Index of the first entry to return; 0 starts at the beginning. | [optional] 
 **count** | **int**| How many entries to return. The internal service applies its own default. | [optional] 

### Return type

[**AiFolderContentWrapper**](AiFolderContentWrapper.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_folder_content_wrapper import AiFolderContentWrapper
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
    api_instance = docspace_api_sdk.AgentsApi(api_client)
    subject_id = '00000000-0000-0000-0000-000000000000' # str | Show only the agent rooms this user takes part in. (optional)
    subject_owner_id = '00000000-0000-0000-0000-000000000000' # str | Show only the agent rooms owned by this user. (optional)
    exclude_subject = false # bool | Invert the user filter: leave out what `subjectId` selects instead of keeping it. (optional)
    tags = 'ai,assistant' # str | Show only the agent rooms carrying these tags, comma-separated. (optional)
    without_tags = false # bool | Show only the agent rooms that carry no tags at all. (optional)
    quota_filter = 0 # int | Filter by quota kind: 0 for all, 1 for the default quota, 2 for a custom one. (optional)
    filter_value = 'assistant' # str | Show only the agent rooms whose title matches this text. (optional)
    sort_by = 'DateAndTime' # str | Field to sort by, for example `DateAndTime`. (optional)
    sort_order = 'descending' # str | Sort direction, `ascending` or `descending`. (optional)
    start_index = 0 # int | Index of the first entry to return; 0 starts at the beginning. (optional)
    count = 25 # int | How many entries to return. The internal service applies its own default. (optional)

    try:
        # List agents
        api_response = api_instance.ai_agents_list(subject_id=subject_id, subject_owner_id=subject_owner_id, exclude_subject=exclude_subject, tags=tags, without_tags=without_tags, quota_filter=quota_filter, filter_value=filter_value, sort_by=sort_by, sort_order=sort_order, start_index=start_index, count=count)
        print("The response of AgentsApi->ai_agents_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->ai_agents_list: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The agent rooms, in the DocSpace AI service's folder-content envelope. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_agents_news**
> AiNewItemsAgentNewItemsArrayWrapper ai_agents_news()

Lists the unread items across the caller's AI agent rooms, so a badge can be rendered without walking each room. It takes no parameters and is scoped to the caller by the DocSpace AI service. The answer is that service's new-items payload. This is a read-only operation and does not mark anything as seen.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**AiNewItemsAgentNewItemsArrayWrapper**](AiNewItemsAgentNewItemsArrayWrapper.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_new_items_agent_new_items_array_wrapper import AiNewItemsAgentNewItemsArrayWrapper
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
    api_instance = docspace_api_sdk.AgentsApi(api_client)

    try:
        # List agent news items
        api_response = api_instance.ai_agents_news()
        print("The response of AgentsApi->ai_agents_news:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->ai_agents_news: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The unread items of the caller's agent rooms. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_agents_reset_quota**
> AiFolderArrayWrapper ai_agents_reset_quota(ai_agents_reset_quota_request)

Returns the listed AI agent rooms to the portal's default storage quota, forwarding `roomIds` to the DocSpace AI service unchanged. The answer is that service's payload, one updated room per entry. This is the counterpart of `PUT api/2.0/ai/agents/agentquota` and takes no quota value of its own. Rooms already on the default are unaffected.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_agents_reset_quota_request** | [**AiAgentsResetQuotaRequest**](AiAgentsResetQuotaRequest.md)|  | 

### Return type

[**AiFolderArrayWrapper**](AiFolderArrayWrapper.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_agents_reset_quota_request import AiAgentsResetQuotaRequest
from docspace_api_sdk.models.ai_folder_array_wrapper import AiFolderArrayWrapper
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
    api_instance = docspace_api_sdk.AgentsApi(api_client)
    ai_agents_reset_quota_request = docspace_api_sdk.AiAgentsResetQuotaRequest() # AiAgentsResetQuotaRequest | 

    try:
        # Reset agents' quota
        api_response = api_instance.ai_agents_reset_quota(ai_agents_reset_quota_request)
        print("The response of AgentsApi->ai_agents_reset_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->ai_agents_reset_quota: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated agent rooms, one entry each. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_agents_update**
> AiFolderWrapper ai_agents_update(id, ai_agents_update_request)

Changes an AI agent room - its title, tags or standing instruction - and optionally rebinds its model. The ID has to be the room's integer identifier. `profileId` is not part of the room contract: it is taken out of the forwarded body and applied afterwards as the agent's assignment, and it has to be a UUID naming an existing chat-capable profile. An instruction sent as `chatSettings.prompt` has its markup stripped, as on create; note that when `chatSettings` is present the upstream service still requires the rest of that object to be valid, so send it whole.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The agent identifier. | 
 **ai_agents_update_request** | [**AiAgentsUpdateRequest**](AiAgentsUpdateRequest.md)|  | 

### Return type

[**AiFolderWrapper**](AiFolderWrapper.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_agents_update_request import AiAgentsUpdateRequest
from docspace_api_sdk.models.ai_folder_wrapper import AiFolderWrapper
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
    api_instance = docspace_api_sdk.AgentsApi(api_client)
    id = '1234' # str | The agent identifier.
    ai_agents_update_request = docspace_api_sdk.AiAgentsUpdateRequest() # AiAgentsUpdateRequest | 

    try:
        # Update an agent
        api_response = api_instance.ai_agents_update(id, ai_agents_update_request)
        print("The response of AgentsApi->ai_agents_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->ai_agents_update: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated agent room. |  -  |
**400** | The agent ID is not a positive integer, or `profileId` is not a UUID, names no existing profile, or names one that does not support chat. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_agents_update_quota**
> AiFolderArrayWrapper ai_agents_update_quota(ai_agents_update_quota_request)

Sets the storage quota of the listed AI agent rooms in one call, forwarding `roomIds` and `quota` to the DocSpace AI service unchanged. The answer is that service's payload, one updated room per entry. A quota applies to the room's stored files, not to the model usage of its chats. Use `PUT api/2.0/ai/agents/resetquota` to return rooms to the portal default instead of naming a number.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_agents_update_quota_request** | [**AiAgentsUpdateQuotaRequest**](AiAgentsUpdateQuotaRequest.md)|  | 

### Return type

[**AiFolderArrayWrapper**](AiFolderArrayWrapper.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_agents_update_quota_request import AiAgentsUpdateQuotaRequest
from docspace_api_sdk.models.ai_folder_array_wrapper import AiFolderArrayWrapper
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
    api_instance = docspace_api_sdk.AgentsApi(api_client)
    ai_agents_update_quota_request = docspace_api_sdk.AiAgentsUpdateQuotaRequest() # AiAgentsUpdateQuotaRequest | 

    try:
        # Update agents' quota
        api_response = api_instance.ai_agents_update_quota(ai_agents_update_quota_request)
        print("The response of AgentsApi->ai_agents_update_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->ai_agents_update_quota: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated agent rooms, one entry each. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

