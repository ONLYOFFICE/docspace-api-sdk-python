# docspace_api_sdk.SharingApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_external_share_password**](#apply_external_share_password) | **POST** /api/2.0/files/share/{key}/password | 
[**change_file_owner**](#change_file_owner) | **POST** /api/2.0/files/owner | 
[**get_external_share_data**](#get_external_share_data) | **GET** /api/2.0/files/share/{key} | 
[**get_file_security_info**](#get_file_security_info) | **GET** /api/2.0/files/file/{id}/share | 
[**get_folder_security_info**](#get_folder_security_info) | **GET** /api/2.0/files/folder/{id}/share | 
[**get_groups_members_with_file_security**](#get_groups_members_with_file_security) | **GET** /api/2.0/files/file/{fileId}/group/{groupId}/share | 
[**get_groups_members_with_folder_security**](#get_groups_members_with_folder_security) | **GET** /api/2.0/files/folder/{folderId}/group/{groupId}/share | 
[**get_security_info**](#get_security_info) | **POST** /api/2.0/files/share | 
[**get_shared_users**](#get_shared_users) | **GET** /api/2.0/files/file/{fileId}/sharedusers | 
[**remove_security_info**](#remove_security_info) | **DELETE** /api/2.0/files/share | 
[**send_editor_notify**](#send_editor_notify) | **POST** /api/2.0/files/file/{fileId}/sendeditornotify | 
[**set_file_security_info**](#set_file_security_info) | **PUT** /api/2.0/files/file/{fileId}/share | 
[**set_folder_security_info**](#set_folder_security_info) | **PUT** /api/2.0/files/folder/{folderId}/share | 
[**set_security_info**](#set_security_info) | **PUT** /api/2.0/files/share | 


# **apply_external_share_password**
> ExternalShareWrapper apply_external_share_password(key, external_share_request_param)



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
    key = 'some text' # str | The unique document identifier.
    external_share_request_param = docspace_api_sdk.ExternalShareRequestParam() # ExternalShareRequestParam | The external data share request parameters.

    try:
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
**200** | External data |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_file_owner**
> FileEntryBaseArrayWrapper change_file_owner(change_owner_request_dto=change_owner_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_owner_request_dto** | [**ChangeOwnerRequestDto**](ChangeOwnerRequestDto.md)|  | [optional] 

### Return type

[**FileEntryBaseArrayWrapper**](FileEntryBaseArrayWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SharingApi(api_client)
    change_owner_request_dto = docspace_api_sdk.ChangeOwnerRequestDto() # ChangeOwnerRequestDto |  (optional)

    try:
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
**200** | File entry information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_share_data**
> ExternalShareWrapper get_external_share_data(key, file_id=file_id, folder_id=folder_id)



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
    key = 'some text' # str | The unique key of the external shared data.
    file_id = '9846' # str | The unique document identifier. (optional)
    folder_id = '9846' # str | The unique folder identifier. (optional)

    try:
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
**200** | External data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_security_info**
> FileShareArrayWrapper get_file_security_info(id, count=count, start_index=start_index)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The file ID of the request. | 
 **count** | **int**| The number of items to retrieve in the request. | [optional] 
 **start_index** | **int**| The starting index for the query results. | [optional] 

### Return type

[**FileShareArrayWrapper**](FileShareArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_share_array_wrapper import FileShareArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SharingApi(api_client)
    id = 9846 # int | The file ID of the request.
    count = 1234 # int | The number of items to retrieve in the request. (optional)
    start_index = 1234 # int | The starting index for the query results. (optional)

    try:
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
**200** | List of shared file information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_security_info**
> FileShareArrayWrapper get_folder_security_info(id, count=count, start_index=start_index)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The request folder ID. | 
 **count** | **int**| The number of items to retrieve in the request. | [optional] 
 **start_index** | **int**| The starting index for the query results. | [optional] 

### Return type

[**FileShareArrayWrapper**](FileShareArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_share_array_wrapper import FileShareArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SharingApi(api_client)
    id = 9846 # int | The request folder ID.
    count = 1234 # int | The number of items to retrieve in the request. (optional)
    start_index = 1234 # int | The starting index for the query results. (optional)

    try:
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
**200** | List of shared file information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups_members_with_file_security**
> GroupMemberSecurityRequestArrayWrapper get_groups_members_with_file_security(file_id, group_id, count=count, start_index=start_index, filter_value=filter_value)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID. | 
 **group_id** | **str**| The group ID. | 
 **count** | **int**| The number of items to be retrieved in the current query. | [optional] 
 **start_index** | **int**| The starting index for the query result set. | [optional] 
 **filter_value** | **str**| The filter value used for searching or querying group members based on text input. | [optional] 

### Return type

[**GroupMemberSecurityRequestArrayWrapper**](GroupMemberSecurityRequestArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.group_member_security_request_array_wrapper import GroupMemberSecurityRequestArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SharingApi(api_client)
    file_id = 9846 # int | The file ID.
    group_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | The group ID.
    count = 1234 # int | The number of items to be retrieved in the current query. (optional)
    start_index = 1234 # int | The starting index for the query result set. (optional)
    filter_value = 'some text' # str | The filter value used for searching or querying group members based on text input. (optional)

    try:
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
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups_members_with_folder_security**
> GroupMemberSecurityRequestArrayWrapper get_groups_members_with_folder_security(folder_id, group_id, count=count, start_index=start_index, filter_value=filter_value)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID. | 
 **group_id** | **str**| The group ID. | 
 **count** | **int**| The number of items to be retrieved in the current query. | [optional] 
 **start_index** | **int**| The starting index for the query result set. | [optional] 
 **filter_value** | **str**| The filter value used for searching or querying group members based on text input. | [optional] 

### Return type

[**GroupMemberSecurityRequestArrayWrapper**](GroupMemberSecurityRequestArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.group_member_security_request_array_wrapper import GroupMemberSecurityRequestArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SharingApi(api_client)
    folder_id = 9846 # int | The folder ID.
    group_id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | The group ID.
    count = 1234 # int | The number of items to be retrieved in the current query. (optional)
    start_index = 1234 # int | The starting index for the query result set. (optional)
    filter_value = 'some text' # str | The filter value used for searching or querying group members based on text input. (optional)

    try:
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
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security_info**
> FileShareArrayWrapper get_security_info(base_batch_request_dto=base_batch_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_batch_request_dto** | [**BaseBatchRequestDto**](BaseBatchRequestDto.md)|  | [optional] 

### Return type

[**FileShareArrayWrapper**](FileShareArrayWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SharingApi(api_client)
    base_batch_request_dto = docspace_api_sdk.BaseBatchRequestDto() # BaseBatchRequestDto |  (optional)

    try:
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
**200** | List of shared files and folders information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_users**
> MentionWrapperArrayWrapper get_shared_users(file_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID of the request. | 

### Return type

[**MentionWrapperArrayWrapper**](MentionWrapperArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.mention_wrapper_array_wrapper import MentionWrapperArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SharingApi(api_client)
    file_id = 9846 # int | The file ID of the request.

    try:
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
**200** | List of users with their access rights to the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_security_info**
> BooleanWrapper remove_security_info(base_batch_request_dto=base_batch_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_batch_request_dto** | [**BaseBatchRequestDto**](BaseBatchRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SharingApi(api_client)
    base_batch_request_dto = docspace_api_sdk.BaseBatchRequestDto() # BaseBatchRequestDto |  (optional)

    try:
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
**200** | Boolean value: true if the operation is successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_editor_notify**
> AceShortWrapperArrayWrapper send_editor_notify(file_id, mention_message_wrapper=mention_message_wrapper)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID of the mention message. | 
 **mention_message_wrapper** | [**MentionMessageWrapper**](MentionMessageWrapper.md)| The mention message. | [optional] 

### Return type

[**AceShortWrapperArrayWrapper**](AceShortWrapperArrayWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SharingApi(api_client)
    file_id = 9846 # int | The file ID of the mention message.
    mention_message_wrapper = docspace_api_sdk.MentionMessageWrapper() # MentionMessageWrapper | The mention message. (optional)

    try:
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
**200** | List of access rights information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_file_security_info**
> FileShareArrayWrapper set_file_security_info(file_id, security_info_simple_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID. | 
 **security_info_simple_request_dto** | [**SecurityInfoSimpleRequestDto**](SecurityInfoSimpleRequestDto.md)| The parameters of the security information simple request. | 

### Return type

[**FileShareArrayWrapper**](FileShareArrayWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SharingApi(api_client)
    file_id = 9846 # int | The file ID.
    security_info_simple_request_dto = docspace_api_sdk.SecurityInfoSimpleRequestDto() # SecurityInfoSimpleRequestDto | The parameters of the security information simple request.

    try:
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
**200** | List of shared file information: sharing rights, a user who has the access to the specified file, the file is locked by this user or not, this user is an owner of the specified file or not, this user can edit the access to the specified file or not |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_folder_security_info**
> FileShareArrayWrapper set_folder_security_info(folder_id, security_info_simple_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| The folder ID. | 
 **security_info_simple_request_dto** | [**SecurityInfoSimpleRequestDto**](SecurityInfoSimpleRequestDto.md)| The parameters of the security information simple request. | 

### Return type

[**FileShareArrayWrapper**](FileShareArrayWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SharingApi(api_client)
    folder_id = 9846 # int | The folder ID.
    security_info_simple_request_dto = docspace_api_sdk.SecurityInfoSimpleRequestDto() # SecurityInfoSimpleRequestDto | The parameters of the security information simple request.

    try:
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
**200** | List of shared folder information: sharing rights, a user who has the access to the specified folder, the folder is locked by this user or not, this user is an owner of the specified folder or not, this user can edit the access to the specified folder or not |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_security_info**
> FileShareArrayWrapper set_security_info(security_info_request_dto=security_info_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **security_info_request_dto** | [**SecurityInfoRequestDto**](SecurityInfoRequestDto.md)|  | [optional] 

### Return type

[**FileShareArrayWrapper**](FileShareArrayWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.SharingApi(api_client)
    security_info_request_dto = docspace_api_sdk.SecurityInfoRequestDto() # SecurityInfoRequestDto |  (optional)

    try:
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
**200** | List of shared files and folders information: sharing rights, a user who has the access to the specified folder, the folder is locked by this user or not, this user is an owner of the specified folder or not, this user can edit the access to the specified folder or not |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

