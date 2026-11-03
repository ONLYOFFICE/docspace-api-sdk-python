# docspace_api_sdk.ContextApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_context_get_context_folders**](#ai_context_get_context_folders) | **GET** /api/2.0/ai/context/get-context-folders | Get context folders
[**ai_context_get_knowledge_folders**](#ai_context_get_knowledge_folders) | **GET** /api/2.0/ai/context/get-knowledge-folders | Get knowledge folders
[**ai_context_get_room_skill**](#ai_context_get_room_skill) | **GET** /api/2.0/ai/context/get-room-skill | Get room skill
[**ai_context_get_room_skills**](#ai_context_get_room_skills) | **GET** /api/2.0/ai/context/get-room-skills | Get room skills


# **ai_context_get_context_folders**
> List[AiContextFolder] ai_context_get_context_folders()

Lists the Instructions rooms the caller can connect to a chat as context, grouped under the account they belong to (`docspace` for this portal). Only a room the caller can read that holds at least one skill is listed: one without skills would connect nothing. An empty list means there is nothing to connect. At most 1000 Instructions rooms are read; any beyond them are left out without a signal. Read the skills of one room with `GET api/2.0/ai/context/get-room-skills`. This is a read-only operation.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AiContextFolder]**](AiContextFolder.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_context_folder import AiContextFolder
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
    api_instance = docspace_api_sdk.ContextApi(api_client)

    try:
        # Get context folders
        api_response = api_instance.ai_context_get_context_folders()
        print("The response of ContextApi->ai_context_get_context_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextApi->ai_context_get_context_folders: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Instructions rooms the caller can connect, grouped by account. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_context_get_knowledge_folders**
> List[AiContextFolder] ai_context_get_knowledge_folders()

Lists the Knowledge rooms the caller can connect to a chat as its knowledge base, grouped under the account they belong to (`docspace` for this portal). A connected Knowledge room limits the knowledge search of a round to it (`actionArgs.knowledgeRooms`). An empty list means there is none the caller can read. At most 1000 Knowledge rooms are listed; any beyond them are left out without a signal. This is a read-only operation.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AiContextFolder]**](AiContextFolder.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_context_folder import AiContextFolder
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
    api_instance = docspace_api_sdk.ContextApi(api_client)

    try:
        # Get knowledge folders
        api_response = api_instance.ai_context_get_knowledge_folders()
        print("The response of ContextApi->ai_context_get_knowledge_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextApi->ai_context_get_knowledge_folders: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Knowledge rooms the caller can connect, grouped by account. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_context_get_room_skill**
> str ai_context_get_room_skill(room_id, skill_id, cloud=cloud)

Returns the Markdown file of one skill of an Instructions room as a JSON string. `roomId` and `skillId` are required, and the skill has to be one of that room's skills: the ID of any other file, readable or not, answers 404, as does a room that is not an Instructions room the caller can read. Only the first 256 KiB of the file are read, which covers the 64 K characters a chat passes to the model; a longer file comes back cut there without a signal. This is a read-only operation.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **str**| The Instructions room identifier. | 
 **skill_id** | **str**| The skill identifier, as `GET api/2.0/ai/context/get-room-skills` lists it. | 
 **cloud** | **str**| The account the room belongs to. Only `docspace`, this portal, exists, and the value is not read; omit it. | [optional] 

### Return type

**str**

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
    api_instance = docspace_api_sdk.ContextApi(api_client)
    room_id = 'room_id_example' # str | The Instructions room identifier.
    skill_id = 'skill_id_example' # str | The skill identifier, as `GET api/2.0/ai/context/get-room-skills` lists it.
    cloud = 'cloud_example' # str | The account the room belongs to. Only `docspace`, this portal, exists, and the value is not read; omit it. (optional)

    try:
        # Get room skill
        api_response = api_instance.ai_context_get_room_skill(room_id, skill_id, cloud=cloud)
        print("The response of ContextApi->ai_context_get_room_skill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextApi->ai_context_get_room_skill: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The skill's Markdown file as a JSON string, its first 256 KiB. |  -  |
**400** | `roomId` or `skillId` is missing. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**404** | The room is not an Instructions room the caller can read, or `skillId` is not one of its skills. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_context_get_room_skills**
> List[AiRoomSkill] ai_context_get_room_skills(room_id, cloud=cloud)

Lists the skills of one Instructions room: the ID, name and description from the frontmatter of each skill file, not its body. `roomId` is required; `cloud` is accepted and not read. A room that is not an Instructions room the caller can read answers 404. Read the body of one skill with `GET api/2.0/ai/context/get-room-skill`. This is a read-only operation.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **str**| The Instructions room identifier. | 
 **cloud** | **str**| The account the room belongs to. Only `docspace`, this portal, exists, and the value is not read; omit it. | [optional] 

### Return type

[**List[AiRoomSkill]**](AiRoomSkill.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_room_skill import AiRoomSkill
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
    api_instance = docspace_api_sdk.ContextApi(api_client)
    room_id = 'room_id_example' # str | The Instructions room identifier.
    cloud = 'cloud_example' # str | The account the room belongs to. Only `docspace`, this portal, exists, and the value is not read; omit it. (optional)

    try:
        # Get room skills
        api_response = api_instance.ai_context_get_room_skills(room_id, cloud=cloud)
        print("The response of ContextApi->ai_context_get_room_skills:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextApi->ai_context_get_room_skills: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The skills of the room, frontmatter only. |  -  |
**400** | `roomId` is missing. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**404** | The room is not an Instructions room the caller can read. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

