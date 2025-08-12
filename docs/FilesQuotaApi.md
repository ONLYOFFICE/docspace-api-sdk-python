# docspace_api_sdk.QuotaApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reset_room_quota**](#reset_room_quota) | **PUT** /api/2.0/files/rooms/resetquota | Reset the room quota limit
[**update_rooms_quota**](#update_rooms_quota) | **PUT** /api/2.0/files/rooms/roomquota | Change the room quota limit


# **reset_room_quota**
> FolderIntegerArrayWrapper reset_room_quota(update_rooms_room_ids_request_dto_integer=update_rooms_room_ids_request_dto_integer)

Resets the quota limit for the rooms with the IDs specified in the request.

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
    api_instance = docspace_api_sdk.QuotaApi(api_client)
    update_rooms_room_ids_request_dto_integer = docspace_api_sdk.UpdateRoomsRoomIdsRequestDtoInteger() # UpdateRoomsRoomIdsRequestDtoInteger |  (optional)

    try:
        # Reset the room quota limit
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
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rooms_quota**
> FolderIntegerArrayWrapper update_rooms_quota(update_rooms_quota_request_dto_integer=update_rooms_quota_request_dto_integer)

Changes the quota limit for the rooms with the IDs specified in the request.

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
    api_instance = docspace_api_sdk.QuotaApi(api_client)
    update_rooms_quota_request_dto_integer = docspace_api_sdk.UpdateRoomsQuotaRequestDtoInteger() # UpdateRoomsQuotaRequestDtoInteger |  (optional)

    try:
        # Change the room quota limit
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
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

