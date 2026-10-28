# UpdateRoomsRoomIdsRequestDto
The rooms that are to go back to the default storage limit of the portal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_ids** | [**List[DuplicateRequestDtoAllOfFileIds]**](DuplicateRequestDtoAllOfFileIds.md) | The rooms to reset, named by the identifiers that `GET api/2.0/files/rooms` reports. Only whole numbers are  processed, so identifiers of rooms kept in a connected third-party account are skipped without an error. | [optional] 

## Example

```python
from docspace_api_sdk.models.update_rooms_room_ids_request_dto import UpdateRoomsRoomIdsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRoomsRoomIdsRequestDto from a JSON string
update_rooms_room_ids_request_dto_instance = UpdateRoomsRoomIdsRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateRoomsRoomIdsRequestDto.to_json())

# convert the object into a dict
update_rooms_room_ids_request_dto_dict = update_rooms_room_ids_request_dto_instance.to_dict()
# create an instance of UpdateRoomsRoomIdsRequestDto from a dict
update_rooms_room_ids_request_dto_from_dict = UpdateRoomsRoomIdsRequestDto.from_dict(update_rooms_room_ids_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


