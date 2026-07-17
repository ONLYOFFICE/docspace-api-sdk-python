# RoomGroupRequestDto
The request parameters for creating a room group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Group name | 
**icon** | **str** | Group icon | 
**rooms** | [**List[DuplicateRequestDtoAllOfFileIds]**](DuplicateRequestDtoAllOfFileIds.md) | The list of room IDs. | 

## Example

```python
from docspace_api_sdk.models.room_group_request_dto import RoomGroupRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoomGroupRequestDto from a JSON string
room_group_request_dto_instance = RoomGroupRequestDto.from_json(json)
# print the JSON string representation of the object
print(RoomGroupRequestDto.to_json())

# convert the object into a dict
room_group_request_dto_dict = room_group_request_dto_instance.to_dict()
# create an instance of RoomGroupRequestDto from a dict
room_group_request_dto_from_dict = RoomGroupRequestDto.from_dict(room_group_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


