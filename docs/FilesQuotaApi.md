# docspace.FilesQuotaApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reset_room_quota**](FilesQuotaApi.md#reset_room_quota) | **PUT** /api/2.0/files/rooms/resetquota | Reset a room quota limit
[**update_rooms_quota**](FilesQuotaApi.md#update_rooms_quota) | **PUT** /api/2.0/files/rooms/roomquota | Change a room quota limit


# **reset_room_quota**
> FolderIntegerArrayWrapper reset_room_quota(update_rooms_room_ids_request_dto_integer=update_rooms_room_ids_request_dto_integer)

Reset a room quota limit

Resets a quota limit for the rooms with the IDs specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.folder_integer_array_wrapper import FolderIntegerArrayWrapper
from docspace.models.update_rooms_room_ids_request_dto_integer import UpdateRoomsRoomIdsRequestDtoInteger
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.FilesQuotaApi(api_client)
    update_rooms_room_ids_request_dto_integer = docspace.UpdateRoomsRoomIdsRequestDtoInteger() # UpdateRoomsRoomIdsRequestDtoInteger |  (optional)

    try:
        # Reset a room quota limit
        api_response = api_instance.reset_room_quota(update_rooms_room_ids_request_dto_integer=update_rooms_room_ids_request_dto_integer)
        print("The response of FilesQuotaApi->reset_room_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesQuotaApi->reset_room_quota: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_rooms_room_ids_request_dto_integer** | [**UpdateRoomsRoomIdsRequestDtoInteger**](UpdateRoomsRoomIdsRequestDtoInteger.md)|  | [optional] 

### Return type

[**FolderIntegerArrayWrapper**](FolderIntegerArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

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

Change a room quota limit

Changes a quota limit for the rooms with the IDs specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.folder_integer_array_wrapper import FolderIntegerArrayWrapper
from docspace.models.update_rooms_quota_request_dto_integer import UpdateRoomsQuotaRequestDtoInteger
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.FilesQuotaApi(api_client)
    update_rooms_quota_request_dto_integer = docspace.UpdateRoomsQuotaRequestDtoInteger() # UpdateRoomsQuotaRequestDtoInteger |  (optional)

    try:
        # Change a room quota limit
        api_response = api_instance.update_rooms_quota(update_rooms_quota_request_dto_integer=update_rooms_quota_request_dto_integer)
        print("The response of FilesQuotaApi->update_rooms_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesQuotaApi->update_rooms_quota: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_rooms_quota_request_dto_integer** | [**UpdateRoomsQuotaRequestDtoInteger**](UpdateRoomsQuotaRequestDtoInteger.md)|  | [optional] 

### Return type

[**FolderIntegerArrayWrapper**](FolderIntegerArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of rooms with the detailed information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

