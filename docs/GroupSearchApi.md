# docspace_api_sdk.SearchApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_groups_with_files_shared**](#get_groups_with_files_shared) | **GET** /api/2.0/group/file/{id} | Get groups with file sharing settings
[**get_groups_with_folders_shared**](#get_groups_with_folders_shared) | **GET** /api/2.0/group/folder/{id} | Get groups with folder sharing settings
[**get_groups_with_rooms_shared**](#get_groups_with_rooms_shared) | **GET** /api/2.0/group/room/{id} | Get groups with room sharing settings


# **get_groups_with_files_shared**
> GroupArrayWrapper get_groups_with_files_shared(id, exclude_shared=exclude_shared, count=count, start_index=start_index, filter_value=filter_value)

Returns groups with their sharing settings for a file with the ID specified in request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The group ID. | 
 **exclude_shared** | **bool**| Specifies whether to exclude the group sharing settings from the response. | [optional] 
 **count** | **int**| The number of groups to retrieve in the request. | [optional] 
 **start_index** | **int**| The starting index from which to begin retrieving groups with their sharing settings. | [optional] 
 **filter_value** | **str**| The text used as a filter for retrieving groups with their sharing settings. | [optional] 

### Return type

[**GroupArrayWrapper**](GroupArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.group_array_wrapper import GroupArrayWrapper
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
    api_instance = docspace_api_sdk.SearchApi(api_client)
    id = 9846 # int | The group ID.
    exclude_shared = true # bool | Specifies whether to exclude the group sharing settings from the response. (optional)
    count = 1234 # int | The number of groups to retrieve in the request. (optional)
    start_index = 1234 # int | The starting index from which to begin retrieving groups with their sharing settings. (optional)
    filter_value = 'some text' # str | The text used as a filter for retrieving groups with their sharing settings. (optional)

    try:
        # Get groups with file sharing settings
        api_response = api_instance.get_groups_with_files_shared(id, exclude_shared=exclude_shared, count=count, start_index=start_index, filter_value=filter_value)
        print("The response of SearchApi->get_groups_with_files_shared:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_groups_with_files_shared: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups_with_folders_shared**
> GroupArrayWrapper get_groups_with_folders_shared(id, exclude_shared=exclude_shared, count=count, start_index=start_index, filter_value=filter_value)

Returns groups with their sharing settings in a folder with the ID specified in request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The group ID. | 
 **exclude_shared** | **bool**| Specifies whether to exclude the group sharing settings from the response. | [optional] 
 **count** | **int**| The number of groups to retrieve in the request. | [optional] 
 **start_index** | **int**| The starting index from which to begin retrieving groups with their sharing settings. | [optional] 
 **filter_value** | **str**| The text used as a filter for retrieving groups with their sharing settings. | [optional] 

### Return type

[**GroupArrayWrapper**](GroupArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.group_array_wrapper import GroupArrayWrapper
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
    api_instance = docspace_api_sdk.SearchApi(api_client)
    id = 9846 # int | The group ID.
    exclude_shared = true # bool | Specifies whether to exclude the group sharing settings from the response. (optional)
    count = 1234 # int | The number of groups to retrieve in the request. (optional)
    start_index = 1234 # int | The starting index from which to begin retrieving groups with their sharing settings. (optional)
    filter_value = 'some text' # str | The text used as a filter for retrieving groups with their sharing settings. (optional)

    try:
        # Get groups with folder sharing settings
        api_response = api_instance.get_groups_with_folders_shared(id, exclude_shared=exclude_shared, count=count, start_index=start_index, filter_value=filter_value)
        print("The response of SearchApi->get_groups_with_folders_shared:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_groups_with_folders_shared: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups_with_rooms_shared**
> GroupArrayWrapper get_groups_with_rooms_shared(id, exclude_shared=exclude_shared, count=count, start_index=start_index, filter_value=filter_value)

Returns groups with their sharing settings in a room with the ID specified in request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The group ID. | 
 **exclude_shared** | **bool**| Specifies whether to exclude the group sharing settings from the response. | [optional] 
 **count** | **int**| The number of groups to retrieve in the request. | [optional] 
 **start_index** | **int**| The starting index from which to begin retrieving groups with their sharing settings. | [optional] 
 **filter_value** | **str**| The text used as a filter for retrieving groups with their sharing settings. | [optional] 

### Return type

[**GroupArrayWrapper**](GroupArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.group_array_wrapper import GroupArrayWrapper
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
    api_instance = docspace_api_sdk.SearchApi(api_client)
    id = 9846 # int | The group ID.
    exclude_shared = true # bool | Specifies whether to exclude the group sharing settings from the response. (optional)
    count = 1234 # int | The number of groups to retrieve in the request. (optional)
    start_index = 1234 # int | The starting index from which to begin retrieving groups with their sharing settings. (optional)
    filter_value = 'some text' # str | The text used as a filter for retrieving groups with their sharing settings. (optional)

    try:
        # Get groups with room sharing settings
        api_response = api_instance.get_groups_with_rooms_shared(id, exclude_shared=exclude_shared, count=count, start_index=start_index, filter_value=filter_value)
        print("The response of SearchApi->get_groups_with_rooms_shared:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_groups_with_rooms_shared: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

