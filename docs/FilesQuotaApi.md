# docspace_api_sdk.QuotaApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reset_room_quota**](#reset_room_quota) | **PUT** /api/2.0/files/rooms/resetquota | 
[**update_rooms_quota**](#update_rooms_quota) | **PUT** /api/2.0/files/rooms/roomquota | 


# **reset_room_quota**
> FolderIntegerArrayWrapper reset_room_quota(update_rooms_room_ids_request_dto_integer=update_rooms_room_ids_request_dto_integer)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_rooms_room_ids_request_dto_integer** | [**UpdateRoomsRoomIdsRequestDtoInteger**](UpdateRoomsRoomIdsRequestDtoInteger.md)|  | [optional] 

### Return type

[**FolderIntegerArrayWrapper**](FolderIntegerArrayWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.QuotaApi(api_client)
    update_rooms_room_ids_request_dto_integer = docspace_api_sdk.UpdateRoomsRoomIdsRequestDtoInteger() # UpdateRoomsRoomIdsRequestDtoInteger |  (optional)

    try:
        api_response = api_instance.reset_room_quota(update_rooms_room_ids_request_dto_integer=update_rooms_room_ids_request_dto_integer)
        print("The response of QuotaApi->reset_room_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotaApi->reset_room_quota: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of rooms with the detailed information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rooms_quota**
> FolderIntegerArrayWrapper update_rooms_quota(update_rooms_quota_request_dto_integer=update_rooms_quota_request_dto_integer)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_rooms_quota_request_dto_integer** | [**UpdateRoomsQuotaRequestDtoInteger**](UpdateRoomsQuotaRequestDtoInteger.md)|  | [optional] 

### Return type

[**FolderIntegerArrayWrapper**](FolderIntegerArrayWrapper.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.QuotaApi(api_client)
    update_rooms_quota_request_dto_integer = docspace_api_sdk.UpdateRoomsQuotaRequestDtoInteger() # UpdateRoomsQuotaRequestDtoInteger |  (optional)

    try:
        api_response = api_instance.update_rooms_quota(update_rooms_quota_request_dto_integer=update_rooms_quota_request_dto_integer)
        print("The response of QuotaApi->update_rooms_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotaApi->update_rooms_quota: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of rooms with the detailed information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

