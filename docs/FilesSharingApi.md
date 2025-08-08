# docspace_api_sdk.SharingApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_external_share_password**](#apply_external_share_password) | **POST** /api/2.0/files/share/{key}/password | 
[**change_file_owner**](#change_file_owner) | **POST** /api/2.0/files/owner | 
[**get_external_share_data**](#get_external_share_data) | **GET** /api/2.0/files/share/{key} | 
[**get_shared_users**](#get_shared_users) | **GET** /api/2.0/files/file/{fileId}/sharedusers | 
[**send_editor_notify**](#send_editor_notify) | **POST** /api/2.0/files/file/{fileId}/sendeditornotify | 


# **apply_external_share_password**
> ExternalShareWrapper apply_external_share_password(key, external_share_request_param=external_share_request_param)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The unique document identifier. | 
 **external_share_request_param** | [**ExternalShareRequestParam**](ExternalShareRequestParam.md)| The external data share request parameters. | [optional] 

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
    external_share_request_param = docspace_api_sdk.ExternalShareRequestParam() # ExternalShareRequestParam | The external data share request parameters. (optional)

    try:
        api_response = api_instance.apply_external_share_password(key, external_share_request_param=external_share_request_param)
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
> ExternalShareWrapper get_external_share_data(key, file_id=file_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The unique key of the external shared data. | 
 **file_id** | **str**| The unique document identifier. | [optional] 

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

    try:
        api_response = api_instance.get_external_share_data(key, file_id=file_id)
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

