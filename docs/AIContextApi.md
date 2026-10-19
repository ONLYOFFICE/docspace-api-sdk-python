# docspace_api_sdk.ContextApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_context_get_context_folders**](#ai_context_get_context_folders) | **GET** /api/2.0/ai/context/get-context-folders | Get context folders
[**ai_context_get_room_skill**](#ai_context_get_room_skill) | **GET** /api/2.0/ai/context/get-room-skill | Get room skill
[**ai_context_get_room_skills**](#ai_context_get_room_skills) | **GET** /api/2.0/ai/context/get-room-skills | Get room skills


# **ai_context_get_context_folders**
> AiSuccessResponse ai_context_get_context_folders()



For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_context_get_room_skill**
> AiSuccessResponse ai_context_get_room_skill(cloud, room_id, skill_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud** | **str**|  | 
 **room_id** | **str**|  | 
 **skill_id** | **str**|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
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
    cloud = 'cloud_example' # str | 
    room_id = 'room_id_example' # str | 
    skill_id = 'skill_id_example' # str | 

    try:
        # Get room skill
        api_response = api_instance.ai_context_get_room_skill(cloud, room_id, skill_id)
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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_context_get_room_skills**
> AiSuccessResponse ai_context_get_room_skills(cloud, room_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud** | **str**|  | 
 **room_id** | **str**|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
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
    cloud = 'cloud_example' # str | 
    room_id = 'room_id_example' # str | 

    try:
        # Get room skills
        api_response = api_instance.ai_context_get_room_skills(cloud, room_id)
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
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, the caller is a guest, or the room named by `entityId` is one the caller cannot open. Relayed from the DocSpace AI service or the Files API. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

