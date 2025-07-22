# UpdateRoomsQuotaRequestDtoInteger
The request parameters for updating the room quota.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_ids** | [**List[BaseBatchRequestDtoFolderIdsInner]**](BaseBatchRequestDtoFolderIdsInner.md) | The list of room IDs. | [optional] 
**quota** | **int** | The room quota. | [optional] 

## Example

```python
from docspace-api-sdk.models.update_rooms_quota_request_dto_integer import UpdateRoomsQuotaRequestDtoInteger

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRoomsQuotaRequestDtoInteger from a JSON string
update_rooms_quota_request_dto_integer_instance = UpdateRoomsQuotaRequestDtoInteger.from_json(json)
# print the JSON string representation of the object
print(UpdateRoomsQuotaRequestDtoInteger.to_json())

# convert the object into a dict
update_rooms_quota_request_dto_integer_dict = update_rooms_quota_request_dto_integer_instance.to_dict()
# create an instance of UpdateRoomsQuotaRequestDtoInteger from a dict
update_rooms_quota_request_dto_integer_from_dict = UpdateRoomsQuotaRequestDtoInteger.from_dict(update_rooms_quota_request_dto_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


