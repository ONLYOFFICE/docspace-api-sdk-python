# docspace_api_sdk.QuotaApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reset_room_quota**](#reset_room_quota) | **PUT** /api/2.0/files/rooms/resetquota | Reset the room quota limit
[**update_rooms_quota**](#update_rooms_quota) | **PUT** /api/2.0/files/rooms/roomquota | Change the room quota limit


# **reset_room_quota**
> FolderArrayWrapper reset_room_quota(update_rooms_room_ids_request_dto=update_rooms_room_ids_request_dto)

Returns every listed room to the default room quota of the portal and streams the updated rooms back in the
order they were given. This is not the same as removing the limit: the room stops carrying its own value and
starts following the portal default, which a portal administrator can change at any time. The per-room quota
feature has to be on, the caller must be a manager of each listed room, and an archived room or a room in the
trash is refused. The list is not transactional, so rooms processed before a failing one keep the default and
the rest keep what they had. Only numeric room ids are processed, which means ids of rooms stored in a
connected third-party account are silently skipped. Use `PUT api/2.0/files/rooms/roomquota` to set an explicit
value, and a quota of -1 in `PUT api/2.0/files/rooms/{id}` to leave the room with no custom limit at all.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_rooms_room_ids_request_dto** | [**UpdateRoomsRoomIdsRequestDto**](UpdateRoomsRoomIdsRequestDto.md)|  | [optional] 

### Return type

[**FolderArrayWrapper**](FolderArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.folder_array_wrapper import FolderArrayWrapper
from docspace_api_sdk.models.update_rooms_room_ids_request_dto import UpdateRoomsRoomIdsRequestDto
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
    update_rooms_room_ids_request_dto = docspace_api_sdk.UpdateRoomsRoomIdsRequestDto() # UpdateRoomsRoomIdsRequestDto |  (optional)

    try:
        # Reset the room quota limit
        api_response = api_instance.reset_room_quota(update_rooms_room_ids_request_dto=update_rooms_room_ids_request_dto)
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
**200** | The rooms as they are after the default limit was restored |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rooms_quota**
> FolderArrayWrapper update_rooms_quota(update_rooms_quota_request_dto=update_rooms_quota_request_dto)

Sets the same custom storage limit, in bytes, on every listed room and streams the updated rooms back in the
order they were given. The per-room quota feature has to be on for the portal, and the value must stay within
the portal own limit, otherwise the call is refused before anything is written. The caller must be a manager
of each listed room, and an archived room or a room in the trash is refused. The list is not transactional:
rooms processed before the offending one keep their new limit, so a failed call has to be checked room by
room. Only numeric room ids are processed, which means ids of rooms stored in a connected third-party account
are silently skipped. A room whose limit already equals the requested value is left untouched and still
returned. To go back to the portal default use `PUT api/2.0/files/rooms/resetquota`, and to drop the custom
limit entirely send a quota of -1 to `PUT api/2.0/files/rooms/{id}`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_rooms_quota_request_dto** | [**UpdateRoomsQuotaRequestDto**](UpdateRoomsQuotaRequestDto.md)|  | [optional] 

### Return type

[**FolderArrayWrapper**](FolderArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.folder_array_wrapper import FolderArrayWrapper
from docspace_api_sdk.models.update_rooms_quota_request_dto import UpdateRoomsQuotaRequestDto
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
    update_rooms_quota_request_dto = docspace_api_sdk.UpdateRoomsQuotaRequestDto() # UpdateRoomsQuotaRequestDto |  (optional)

    try:
        # Change the room quota limit
        api_response = api_instance.update_rooms_quota(update_rooms_quota_request_dto=update_rooms_quota_request_dto)
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
**200** | The rooms as they are after the new limit was applied |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

