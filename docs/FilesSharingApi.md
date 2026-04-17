# docspace_api_sdk.SharingApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_external_share_password**](#apply_external_share_password) | **POST** /api/2.0/files/share/{key}/password | Apply external data password
[**change_file_owner**](#change_file_owner) | **POST** /api/2.0/files/owner | Change the file owner
[**get_external_share_data**](#get_external_share_data) | **GET** /api/2.0/files/share/{key} | Get the external data
[**get_file_security_info**](#get_file_security_info) | **GET** /api/2.0/files/file/{id}/share | Get the shared file information
[**get_folder_security_info**](#get_folder_security_info) | **GET** /api/2.0/files/folder/{id}/share | Get the shared folder information
[**get_groups_members_with_file_security**](#get_groups_members_with_file_security) | **GET** /api/2.0/files/file/{fileId}/group/{groupId}/share | Get file group members with security information
[**get_groups_members_with_folder_security**](#get_groups_members_with_folder_security) | **GET** /api/2.0/files/folder/{folderId}/group/{groupId}/share | Get folder group members with security information
[**get_security_info**](#get_security_info) | **POST** /api/2.0/files/share | Get the sharing rights
[**get_shared_users**](#get_shared_users) | **GET** /api/2.0/files/file/{fileId}/sharedusers | Get user access rights by file ID
[**remove_security_info**](#remove_security_info) | **DELETE** /api/2.0/files/share | Remove the sharing rights
[**send_editor_notify**](#send_editor_notify) | **POST** /api/2.0/files/file/{fileId}/sendeditornotify | Send the mention message
[**set_file_security_info**](#set_file_security_info) | **PUT** /api/2.0/files/file/{fileId}/share | Share a file
[**set_folder_security_info**](#set_folder_security_info) | **PUT** /api/2.0/files/folder/{folderId}/share | Share a folder
[**set_security_info**](#set_security_info) | **PUT** /api/2.0/files/share | Set the sharing rights


# **apply_external_share_password**
> ExternalShareWrapper apply_external_share_password(key, external_share_request_param)

Applies a password specified in the request to get the external data.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The unique document identifier. | 
 **external_share_request_param** | [**ExternalShareRequestParam**](ExternalShareRequestParam.md)| The external data share request parameters. | 

### Return type

[**ExternalShareWrapper**](ExternalShareWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.external_share_request_param import ExternalShareRequestParam
from docspace_api_sdk.models.external_share_wrapper import ExternalShareWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SharingApi(api_client)
    key = 'doc_key_123' # str | The unique document identifier.
    external_share_request_param = docspace_api_sdk.ExternalShareRequestParam() # ExternalShareRequestParam | The external data share request parameters.

    try:
        # Apply external data password
        api_response = api_instance.apply_external_share_password(key, external_share_request_param)
        print("The response of SharingApi->apply_external_share_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharingApi->apply_external_share_password: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | External data |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**429** | Too many requests |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_file_owner**
> FileEntryBaseArrayWrapper change_file_owner(change_owner_request_dto=change_owner_request_dto)

Changes the owner of the file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_owner_request_dto** | [**ChangeOwnerRequestDto**](ChangeOwnerRequestDto.md)|  | [optional] 

### Return type

[**FileEntryBaseArrayWrapper**](FileEntryBaseArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.change_owner_request_dto import ChangeOwnerRequestDto
from docspace_api_sdk.models.file_entry_base_array_wrapper import FileEntryBaseArrayWrapper
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
    api_instance = docspace_api_sdk.SharingApi(api_client)
    change_owner_request_dto = docspace_api_sdk.ChangeOwnerRequestDto() # ChangeOwnerRequestDto |  (optional)

    try:
        # Change the file owner
        api_response = api_instance.change_file_owner(change_owner_request_dto=change_owner_request_dto)
        print("The response of SharingApi->change_file_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharingApi->change_file_owner: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File entry information |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_share_data**
> ExternalShareWrapper get_external_share_data(key, file_id=file_id, folder_id=folder_id)

Returns the external data by the key specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The unique key of the external shared data. | 
 **file_id** | **str**| The unique document identifier. | [optional] 
 **folder_id** | **str**| The unique folder identifier. | [optional] 

### Return type

[**ExternalShareWrapper**](ExternalShareWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.external_share_wrapper import ExternalShareWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SharingApi(api_client)
    key = 'doc_key_123' # str | The unique key of the external shared data.
    file_id = '1' # str | The unique document identifier. (optional)
    folder_id = '1' # str | The unique folder identifier. (optional)

    try:
        # Get the external data
        api_response = api_instance.get_external_share_data(key, file_id=file_id, folder_id=folder_id)
        print("The response of SharingApi->get_external_share_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharingApi->get_external_share_data: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | External data |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_security_info**
> FileShareArrayWrapper get_file_security_info(id, count=count, start_index=start_index)

Returns the detailed information about the shared file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The file unique identifier. | 
 **count** | **int**| The number of items to retrieve in the request. | [optional] 
 **start_index** | **int**| The starting index for the query results. | [optional] 

### Return type

[**FileShareArrayWrapper**](FileShareArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_share_array_wrapper import FileShareArrayWrapper
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
    api_instance = docspace_api_sdk.SharingApi(api_client)
    id = 10 # int | The file unique identifier.
    count = 25 # int | The number of items to retrieve in the request. (optional)
    start_index = 0 # int | The starting index for the query results. (optional)

    try:
        # Get the shared file information
        api_response = api_instance.get_file_security_info(id, count=count, start_index=start_index)
        print("The response of SharingApi->get_file_security_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharingApi->get_file_security_info: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of shared file information |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_security_info**
> FileShareArrayWrapper get_folder_security_info(id, count=count, start_index=start_index)

Returns the detailed information about the shared folder with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The folder unique identifier. | 
 **count** | **int**| The number of items to retrieve in the request. | [optional] 
 **start_index** | **int**| The starting index for the query results. | [optional] 

### Return type

[**FileShareArrayWrapper**](FileShareArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_share_array_wrapper import FileShareArrayWrapper
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
    api_instance = docspace_api_sdk.SharingApi(api_client)
    id = 10 # int | The folder unique identifier.
    count = 25 # int | The number of items to retrieve in the request. (optional)
    start_index = 0 # int | The starting index for the query results. (optional)

    try:
        # Get the shared folder information
        api_response = api_instance.get_folder_security_info(id, count=count, start_index=start_index)
        print("The response of SharingApi->get_folder_security_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharingApi->get_folder_security_info: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of shared file information |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups_members_with_file_security**
> GroupMemberSecurityRequestArrayWrapper get_groups_members_with_file_security(file_id, group_id, count=count, start_index=start_index, filter_value=filter_value)

Returns the group members with their file security information.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID. | 
 **group_id** | **UUID**| The group ID. | 
 **count** | **int**| The number of items to be retrieved in the current query. | [optional] 
 **start_index** | **int**| The starting index for the query result set. | [optional] 
 **filter_value** | **str**| The filter value used for searching or querying group members based on text input. | [optional] 

### Return type

[**GroupMemberSecurityRequestArrayWrapper**](GroupMemberSecurityRequestArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.group_member_security_request_array_wrapper import GroupMemberSecurityRequestArrayWrapper
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
    api_instance = docspace_api_sdk.SharingApi(api_client)
    file_id = 1 # int | The file ID.
    group_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The group ID.
    count = 25 # int | The number of items to be retrieved in the current query. (optional)
    start_index = 0 # int | The starting index for the query result set. (optional)
    filter_value = 'My Document' # str | The filter value used for searching or querying group members based on text input. (optional)

    try:
        # Get file group members with security information
        api_response = api_instance.get_groups_members_with_file_security(file_id, group_id, count=count, start_index=start_index, filter_value=filter_value)
        print("The response of SharingApi->get_groups_members_with_file_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharingApi->get_groups_members_with_file_security: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups_members_with_folder_security**
> GroupMemberSecurityRequestArrayWrapper get_groups_members_with_folder_security(folder_id, group_id, count=count, start_index=start_index, filter_value=filter_value)

Returns the group members with their folder security information.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID. | 
 **group_id** | **UUID**| The group ID. | 
 **count** | **int**| The number of items to be retrieved in the current query. | [optional] 
 **start_index** | **int**| The starting index for the query result set. | [optional] 
 **filter_value** | **str**| The filter value used for searching or querying group members based on text input. | [optional] 

### Return type

[**GroupMemberSecurityRequestArrayWrapper**](GroupMemberSecurityRequestArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.group_member_security_request_array_wrapper import GroupMemberSecurityRequestArrayWrapper
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
    api_instance = docspace_api_sdk.SharingApi(api_client)
    folder_id = 1 # int | The folder ID.
    group_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The group ID.
    count = 25 # int | The number of items to be retrieved in the current query. (optional)
    start_index = 0 # int | The starting index for the query result set. (optional)
    filter_value = 'My Document' # str | The filter value used for searching or querying group members based on text input. (optional)

    try:
        # Get folder group members with security information
        api_response = api_instance.get_groups_members_with_folder_security(folder_id, group_id, count=count, start_index=start_index, filter_value=filter_value)
        print("The response of SharingApi->get_groups_members_with_folder_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharingApi->get_groups_members_with_folder_security: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security_info**
> FileShareArrayWrapper get_security_info(base_batch_request_dto=base_batch_request_dto)

Returns the sharing rights for all the files and folders specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_batch_request_dto** | [**BaseBatchRequestDto**](BaseBatchRequestDto.md)|  | [optional] 

### Return type

[**FileShareArrayWrapper**](FileShareArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.base_batch_request_dto import BaseBatchRequestDto
from docspace_api_sdk.models.file_share_array_wrapper import FileShareArrayWrapper
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
    api_instance = docspace_api_sdk.SharingApi(api_client)
    base_batch_request_dto = docspace_api_sdk.BaseBatchRequestDto() # BaseBatchRequestDto |  (optional)

    try:
        # Get the sharing rights
        api_response = api_instance.get_security_info(base_batch_request_dto=base_batch_request_dto)
        print("The response of SharingApi->get_security_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharingApi->get_security_info: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of shared files and folders information |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_users**
> MentionWrapperArrayWrapper get_shared_users(file_id)

Returns a list of users with their access rights to the file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file unique identifier. | 

### Return type

[**MentionWrapperArrayWrapper**](MentionWrapperArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.mention_wrapper_array_wrapper import MentionWrapperArrayWrapper
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
    api_instance = docspace_api_sdk.SharingApi(api_client)
    file_id = 1 # int | The file unique identifier.

    try:
        # Get user access rights by file ID
        api_response = api_instance.get_shared_users(file_id)
        print("The response of SharingApi->get_shared_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharingApi->get_shared_users: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users with their access rights to the file |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_security_info**
> BooleanWrapper remove_security_info(base_batch_request_dto=base_batch_request_dto)

Removes the sharing rights from all the files and folders specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_batch_request_dto** | [**BaseBatchRequestDto**](BaseBatchRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.base_batch_request_dto import BaseBatchRequestDto
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
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
    api_instance = docspace_api_sdk.SharingApi(api_client)
    base_batch_request_dto = docspace_api_sdk.BaseBatchRequestDto() # BaseBatchRequestDto |  (optional)

    try:
        # Remove the sharing rights
        api_response = api_instance.remove_security_info(base_batch_request_dto=base_batch_request_dto)
        print("The response of SharingApi->remove_security_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharingApi->remove_security_info: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_editor_notify**
> AceShortWrapperArrayWrapper send_editor_notify(file_id, mention_message_wrapper=mention_message_wrapper)

Sends a message to the users who are mentioned in the file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID with the mention message. | 
 **mention_message_wrapper** | [**MentionMessageWrapper**](MentionMessageWrapper.md)| The mention message. | [optional] 

### Return type

[**AceShortWrapperArrayWrapper**](AceShortWrapperArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ace_short_wrapper_array_wrapper import AceShortWrapperArrayWrapper
from docspace_api_sdk.models.mention_message_wrapper import MentionMessageWrapper
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
    api_instance = docspace_api_sdk.SharingApi(api_client)
    file_id = 56 # int | The file ID with the mention message.
    mention_message_wrapper = docspace_api_sdk.MentionMessageWrapper() # MentionMessageWrapper | The mention message. (optional)

    try:
        # Send the mention message
        api_response = api_instance.send_editor_notify(file_id, mention_message_wrapper=mention_message_wrapper)
        print("The response of SharingApi->send_editor_notify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharingApi->send_editor_notify: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of access rights information |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The list of email addresses is empty |  -  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | The required file was not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_file_security_info**
> FileShareArrayWrapper set_file_security_info(file_id, security_info_simple_request_dto)

Sets the sharing settings to a file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID. | 
 **security_info_simple_request_dto** | [**SecurityInfoSimpleRequestDto**](SecurityInfoSimpleRequestDto.md)| The parameters of the security information simple request. | 

### Return type

[**FileShareArrayWrapper**](FileShareArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_share_array_wrapper import FileShareArrayWrapper
from docspace_api_sdk.models.security_info_simple_request_dto import SecurityInfoSimpleRequestDto
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
    api_instance = docspace_api_sdk.SharingApi(api_client)
    file_id = 1 # int | The file ID.
    security_info_simple_request_dto = docspace_api_sdk.SecurityInfoSimpleRequestDto() # SecurityInfoSimpleRequestDto | The parameters of the security information simple request.

    try:
        # Share a file
        api_response = api_instance.set_file_security_info(file_id, security_info_simple_request_dto)
        print("The response of SharingApi->set_file_security_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharingApi->set_file_security_info: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of shared file information: sharing rights, a user who has the access to the specified file, the file is locked by this user or not, this user is an owner of the specified file or not, this user can edit the access to the specified file or not |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_folder_security_info**
> FileShareArrayWrapper set_folder_security_info(folder_id, security_info_simple_request_dto)

Sets the sharing settings to a folder with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID. | 
 **security_info_simple_request_dto** | [**SecurityInfoSimpleRequestDto**](SecurityInfoSimpleRequestDto.md)| The parameters of the security information simple request. | 

### Return type

[**FileShareArrayWrapper**](FileShareArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_share_array_wrapper import FileShareArrayWrapper
from docspace_api_sdk.models.security_info_simple_request_dto import SecurityInfoSimpleRequestDto
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
    api_instance = docspace_api_sdk.SharingApi(api_client)
    folder_id = 1 # int | The folder ID.
    security_info_simple_request_dto = docspace_api_sdk.SecurityInfoSimpleRequestDto() # SecurityInfoSimpleRequestDto | The parameters of the security information simple request.

    try:
        # Share a folder
        api_response = api_instance.set_folder_security_info(folder_id, security_info_simple_request_dto)
        print("The response of SharingApi->set_folder_security_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharingApi->set_folder_security_info: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of shared folder information: sharing rights, a user who has the access to the specified folder, the folder is locked by this user or not, this user is an owner of the specified folder or not, this user can edit the access to the specified folder or not |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_security_info**
> FileShareArrayWrapper set_security_info(security_info_request_dto=security_info_request_dto)

Sets the sharing rights to all the files and folders specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **security_info_request_dto** | [**SecurityInfoRequestDto**](SecurityInfoRequestDto.md)|  | [optional] 

### Return type

[**FileShareArrayWrapper**](FileShareArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_share_array_wrapper import FileShareArrayWrapper
from docspace_api_sdk.models.security_info_request_dto import SecurityInfoRequestDto
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
    api_instance = docspace_api_sdk.SharingApi(api_client)
    security_info_request_dto = docspace_api_sdk.SecurityInfoRequestDto() # SecurityInfoRequestDto |  (optional)

    try:
        # Set the sharing rights
        api_response = api_instance.set_security_info(security_info_request_dto=security_info_request_dto)
        print("The response of SharingApi->set_security_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharingApi->set_security_info: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of shared files and folders information: sharing rights, a user who has the access to the specified folder, the folder is locked by this user or not, this user is an owner of the specified folder or not, this user can edit the access to the specified folder or not |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

