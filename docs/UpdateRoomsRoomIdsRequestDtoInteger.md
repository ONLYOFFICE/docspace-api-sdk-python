# UpdateRoomsRoomIdsRequestDtoInteger
The request parameters for updating the room.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_ids** | [**List[DuplicateRequestDtoAllOfFileIds]**](DuplicateRequestDtoAllOfFileIds.md) | The list of room IDs. | [optional] 

## Example

```python
from docspace_api_sdk.models.update_rooms_room_ids_request_dto_integer import UpdateRoomsRoomIdsRequestDtoInteger

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRoomsRoomIdsRequestDtoInteger from a JSON string
update_rooms_room_ids_request_dto_integer_instance = UpdateRoomsRoomIdsRequestDtoInteger.from_json(json)
# print the JSON string representation of the object
print(UpdateRoomsRoomIdsRequestDtoInteger.to_json())

# convert the object into a dict
update_rooms_room_ids_request_dto_integer_dict = update_rooms_room_ids_request_dto_integer_instance.to_dict()
# create an instance of UpdateRoomsRoomIdsRequestDtoInteger from a dict
update_rooms_room_ids_request_dto_integer_from_dict = UpdateRoomsRoomIdsRequestDtoInteger.from_dict(update_rooms_room_ids_request_dto_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


