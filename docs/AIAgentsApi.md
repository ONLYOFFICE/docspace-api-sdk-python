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
> AiFolderIntegerWrapper ai_agents_create(ai_agents_create_request)

Creates an AI agent room in the .NET AI service and binds the supplied `profileId` to it as a `Chat` assignment. The instruction is stored on the room as a prompt-only chat setting; a failed binding is reported as an error even though the room already exists.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_agents_create_request** | [**AiAgentsCreateRequest**](AiAgentsCreateRequest.md)|  | 

### Return type

[**AiFolderIntegerWrapper**](AiFolderIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_agents_create_request import AiAgentsCreateRequest
from docspace_api_sdk.models.ai_folder_integer_wrapper import AiFolderIntegerWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_agents_delete**
> AiFileOperationWrapper ai_agents_delete(id, ai_agents_delete_request)

Deletes an AI agent room.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The agent identifier. | 
 **ai_agents_delete_request** | [**AiAgentsDeleteRequest**](AiAgentsDeleteRequest.md)|  | 

### Return type

[**AiFileOperationWrapper**](AiFileOperationWrapper.md)

### Authorization

No authorization required

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

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AgentsApi(api_client)
    id = 'id_example' # str | The agent identifier.
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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_agents_get**
> AiFolderIntegerWrapper ai_agents_get(id)

Returns one AI agent room, enriched with the `profileId` bound to it so an edit form can prefill the profile selector. A missing assignment simply leaves `profileId` out.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The agent identifier. | 

### Return type

[**AiFolderIntegerWrapper**](AiFolderIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_folder_integer_wrapper import AiFolderIntegerWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AgentsApi(api_client)
    id = 'id_example' # str | The agent identifier.

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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_agents_list**
> AiFolderContentIntegerWrapper ai_agents_list()

Lists the portal's AI agent rooms. Query parameters are forwarded unchanged to the .NET AI service, which answers with its folder-content payload.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**AiFolderContentIntegerWrapper**](AiFolderContentIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_folder_content_integer_wrapper import AiFolderContentIntegerWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AgentsApi(api_client)

    try:
        # List agents
        api_response = api_instance.ai_agents_list()
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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_agents_news**
> AiNewItemsAgentNewItemsArrayWrapper ai_agents_news()

Lists the new items across the caller's AI agent rooms.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**AiNewItemsAgentNewItemsArrayWrapper**](AiNewItemsAgentNewItemsArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_new_items_agent_new_items_array_wrapper import AiNewItemsAgentNewItemsArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_agents_reset_quota**
> AiFolderIntegerArrayWrapper ai_agents_reset_quota(ai_agents_reset_quota_request)

Resets the storage quota of the given AI agent rooms.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_agents_reset_quota_request** | [**AiAgentsResetQuotaRequest**](AiAgentsResetQuotaRequest.md)|  | 

### Return type

[**AiFolderIntegerArrayWrapper**](AiFolderIntegerArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_agents_reset_quota_request import AiAgentsResetQuotaRequest
from docspace_api_sdk.models.ai_folder_integer_array_wrapper import AiFolderIntegerArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_agents_update**
> AiFolderIntegerWrapper ai_agents_update(id, ai_agents_update_request)

Updates an AI agent room - title, tags, instruction. `profileId` is not part of the room contract: it is stripped from the forwarded body and re-bound as the agent's assignment afterwards.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The agent identifier. | 
 **ai_agents_update_request** | [**AiAgentsUpdateRequest**](AiAgentsUpdateRequest.md)|  | 

### Return type

[**AiFolderIntegerWrapper**](AiFolderIntegerWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_agents_update_request import AiAgentsUpdateRequest
from docspace_api_sdk.models.ai_folder_integer_wrapper import AiFolderIntegerWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AgentsApi(api_client)
    id = 'id_example' # str | The agent identifier.
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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_agents_update_quota**
> AiFolderIntegerArrayWrapper ai_agents_update_quota(ai_agents_update_quota_request)

Changes the storage quota of the given AI agent rooms.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_agents_update_quota_request** | [**AiAgentsUpdateQuotaRequest**](AiAgentsUpdateQuotaRequest.md)|  | 

### Return type

[**AiFolderIntegerArrayWrapper**](AiFolderIntegerArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_agents_update_quota_request import AiAgentsUpdateQuotaRequest
from docspace_api_sdk.models.ai_folder_integer_array_wrapper import AiFolderIntegerArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

