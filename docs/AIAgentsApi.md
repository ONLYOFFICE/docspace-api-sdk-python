# docspace_api_sdk.AgentsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agent**](#create_agent) | **POST** /api/2.0/ai/agents | Create an ai agent
[**delete_agent**](#delete_agent) | **DELETE** /api/2.0/ai/agents/{id} | Remove an ai agent
[**get_agent_info**](#get_agent_info) | **GET** /api/2.0/ai/agents/{id} | Return an ai agent
[**get_agents**](#get_agents) | **GET** /api/2.0/ai/agents | Get ai agents
[**get_agents_new_items**](#get_agents_new_items) | **GET** /api/2.0/ai/agents/news | Get the room new items
[**reset_agents_quota**](#reset_agents_quota) | **PUT** /api/2.0/ai/agents/resetquota | Reset the AI agents quota limit
[**update_agent**](#update_agent) | **PUT** /api/2.0/ai/agents/{id} | Update an ai agent
[**update_agents_quota**](#update_agents_quota) | **PUT** /api/2.0/ai/agents/agentquota | Change the AI agent quota limit


# **create_agent**
> FolderIntegerWrapper create_agent(create_agent_request_dto=create_agent_request_dto)

Creates an ai agent.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_agent_request_dto** | [**CreateAgentRequestDto**](CreateAgentRequestDto.md)|  | [optional] 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.create_agent_request_dto import CreateAgentRequestDto
from docspace_api_sdk.models.folder_integer_wrapper import FolderIntegerWrapper
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
    api_instance = docspace_api_sdk.AgentsApi(api_client)
    create_agent_request_dto = docspace_api_sdk.CreateAgentRequestDto() # CreateAgentRequestDto |  (optional)

    try:
        # Create an ai agent
        api_response = api_instance.create_agent(create_agent_request_dto=create_agent_request_dto)
        print("The response of AgentsApi->create_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->create_agent: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent information |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent**
> FileOperationWrapper delete_agent(id, delete_room_request)

Removes an ai agent.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room ID. | 
 **delete_room_request** | [**DeleteRoomRequest**](DeleteRoomRequest.md)| The parameters for deleting a room. | 

### Return type

[**FileOperationWrapper**](FileOperationWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.delete_room_request import DeleteRoomRequest
from docspace_api_sdk.models.file_operation_wrapper import FileOperationWrapper
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
    api_instance = docspace_api_sdk.AgentsApi(api_client)
    id = 10 # int | The room ID.
    delete_room_request = docspace_api_sdk.DeleteRoomRequest() # DeleteRoomRequest | The parameters for deleting a room.

    try:
        # Remove an ai agent
        api_response = api_instance.delete_agent(id, delete_room_request)
        print("The response of AgentsApi->delete_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->delete_agent: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File operation |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_info**
> FolderIntegerWrapper get_agent_info(id)

Returns an ai agent.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room ID. | 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.folder_integer_wrapper import FolderIntegerWrapper
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
    api_instance = docspace_api_sdk.AgentsApi(api_client)
    id = 1 # int | The room ID.

    try:
        # Return an ai agent
        api_response = api_instance.get_agent_info(id)
        print("The response of AgentsApi->get_agent_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agent_info: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent information |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agents**
> FolderContentIntegerWrapper get_agents(subject_id=subject_id, subject_owner_id=subject_owner_id, without_tags=without_tags, tags=tags, exclude_subject=exclude_subject, subject_filter=subject_filter, quota_filter=quota_filter, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)

Get ai agents

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id** | **str**| The filter by user ID. | [optional] 
 **subject_owner_id** | **str**| The filter by room owner ID. | [optional] 
 **without_tags** | **bool**| Specifies whether to search by tags or not. | [optional] 
 **tags** | **str**| The tags in the serialized format. | [optional] 
 **exclude_subject** | **bool**| Specifies whether to exclude search by user or group ID. | [optional] 
 **subject_filter** | [**SubjectFilter**](.md)| The filter by user (Owner - 0, Member - 1). | [optional] 
 **quota_filter** | [**QuotaFilter**](.md)| The filter by quota (All - 0, Default - 1, Custom - 2). | [optional] 
 **count** | **int**| Specifies the maximum number of items to retrieve. | [optional] 
 **start_index** | **int**| The index from which to start retrieving the room content. | [optional] 
 **sort_by** | **str**| Specifies the field by which the room content should be sorted. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The order in which the results are sorted. | [optional] 
 **filter_value** | **str**| The text filter value used to refine search or query operations. | [optional] 

### Return type

[**FolderContentIntegerWrapper**](FolderContentIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.folder_content_integer_wrapper import FolderContentIntegerWrapper
from docspace_api_sdk.models.quota_filter import QuotaFilter
from docspace_api_sdk.models.sort_order import SortOrder
from docspace_api_sdk.models.subject_filter import SubjectFilter
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
    api_instance = docspace_api_sdk.AgentsApi(api_client)
    subject_id = '00000000-0000-0000-0000-000000000000' # str | The filter by user ID. (optional)
    subject_owner_id = '00000000-0000-0000-0000-000000000000' # str | The filter by room owner ID. (optional)
    without_tags = false # bool | Specifies whether to search by tags or not. (optional)
    tags = 'ai,assistant' # str | The tags in the serialized format. (optional)
    exclude_subject = false # bool | Specifies whether to exclude search by user or group ID. (optional)
    subject_filter = docspace_api_sdk.SubjectFilter() # SubjectFilter | The filter by user (Owner - 0, Member - 1). (optional)
    quota_filter = docspace_api_sdk.QuotaFilter() # QuotaFilter | The filter by quota (All - 0, Default - 1, Custom - 2). (optional)
    count = 25 # int | Specifies the maximum number of items to retrieve. (optional)
    start_index = 0 # int | The index from which to start retrieving the room content. (optional)
    sort_by = 'DateAndTime' # str | Specifies the field by which the room content should be sorted. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_value = 'my agent' # str | The text filter value used to refine search or query operations. (optional)

    try:
        # Get ai agents
        api_response = api_instance.get_agents(subject_id=subject_id, subject_owner_id=subject_owner_id, without_tags=without_tags, tags=tags, exclude_subject=exclude_subject, subject_filter=subject_filter, quota_filter=quota_filter, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_value=filter_value)
        print("The response of AgentsApi->get_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agents: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent information |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agents_new_items**
> NewItemsAgentNewItemsArrayWrapper get_agents_new_items()

Returns the room new items.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**NewItemsAgentNewItemsArrayWrapper**](NewItemsAgentNewItemsArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.new_items_agent_new_items_array_wrapper import NewItemsAgentNewItemsArrayWrapper
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
    api_instance = docspace_api_sdk.AgentsApi(api_client)

    try:
        # Get the room new items
        api_response = api_instance.get_agents_new_items()
        print("The response of AgentsApi->get_agents_new_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agents_new_items: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of new items |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_agents_quota**
> FolderIntegerArrayWrapper reset_agents_quota(update_rooms_room_ids_request_dto_integer=update_rooms_room_ids_request_dto_integer)

Resets the quota limit for the AI agents with the IDs specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_rooms_room_ids_request_dto_integer** | [**UpdateRoomsRoomIdsRequestDtoInteger**](UpdateRoomsRoomIdsRequestDtoInteger.md)|  | [optional] 

### Return type

[**FolderIntegerArrayWrapper**](FolderIntegerArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.folder_integer_array_wrapper import FolderIntegerArrayWrapper
from docspace_api_sdk.models.update_rooms_room_ids_request_dto_integer import UpdateRoomsRoomIdsRequestDtoInteger
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
    api_instance = docspace_api_sdk.AgentsApi(api_client)
    update_rooms_room_ids_request_dto_integer = docspace_api_sdk.UpdateRoomsRoomIdsRequestDtoInteger() # UpdateRoomsRoomIdsRequestDtoInteger |  (optional)

    try:
        # Reset the AI agents quota limit
        api_response = api_instance.reset_agents_quota(update_rooms_room_ids_request_dto_integer=update_rooms_room_ids_request_dto_integer)
        print("The response of AgentsApi->reset_agents_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->reset_agents_quota: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of AI agents with the detailed information |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent**
> FolderIntegerWrapper update_agent(id, update_room_request)

Updates an ai agent.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The room ID. | 
 **update_room_request** | [**UpdateRoomRequest**](UpdateRoomRequest.md)| The request parameters for updating a room. | 

### Return type

[**FolderIntegerWrapper**](FolderIntegerWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.folder_integer_wrapper import FolderIntegerWrapper
from docspace_api_sdk.models.update_room_request import UpdateRoomRequest
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
    api_instance = docspace_api_sdk.AgentsApi(api_client)
    id = 56 # int | The room ID.
    update_room_request = docspace_api_sdk.UpdateRoomRequest() # UpdateRoomRequest | The request parameters for updating a room.

    try:
        # Update an ai agent
        api_response = api_instance.update_agent(id, update_room_request)
        print("The response of AgentsApi->update_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->update_agent: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated agent information |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agents_quota**
> FolderIntegerArrayWrapper update_agents_quota(update_rooms_quota_request_dto_integer=update_rooms_quota_request_dto_integer)

Changes the quota limit for the AI agents with the IDs specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_rooms_quota_request_dto_integer** | [**UpdateRoomsQuotaRequestDtoInteger**](UpdateRoomsQuotaRequestDtoInteger.md)|  | [optional] 

### Return type

[**FolderIntegerArrayWrapper**](FolderIntegerArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.folder_integer_array_wrapper import FolderIntegerArrayWrapper
from docspace_api_sdk.models.update_rooms_quota_request_dto_integer import UpdateRoomsQuotaRequestDtoInteger
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
    api_instance = docspace_api_sdk.AgentsApi(api_client)
    update_rooms_quota_request_dto_integer = docspace_api_sdk.UpdateRoomsQuotaRequestDtoInteger() # UpdateRoomsQuotaRequestDtoInteger |  (optional)

    try:
        # Change the AI agent quota limit
        api_response = api_instance.update_agents_quota(update_rooms_quota_request_dto_integer=update_rooms_quota_request_dto_integer)
        print("The response of AgentsApi->update_agents_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->update_agents_quota: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of AI agents with the detailed information |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

