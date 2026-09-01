# RoomGroupDto
The room security parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The group ID. | [optional] 
**name** | **str** | Group name | [optional] 
**icon** | [**MultiSizeLogoCover**](MultiSizeLogoCover.md) | Group icon | [optional] 
**user_id** | **UUID** | The user ID. | [optional] 
**rooms** | [**List[FileEntryBaseDto]**](FileEntryBaseDto.md) | The list of rooms in the group. | [optional] 
**total_rooms** | **int** | Total number of rooms in the group. | [optional] 

## Example

```python
from docspace_api_sdk.models.room_group_dto import RoomGroupDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoomGroupDto from a JSON string
room_group_dto_instance = RoomGroupDto.from_json(json)
# print the JSON string representation of the object
print(RoomGroupDto.to_json())

# convert the object into a dict
room_group_dto_dict = room_group_dto_instance.to_dict()
# create an instance of RoomGroupDto from a dict
room_group_dto_from_dict = RoomGroupDto.from_dict(room_group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


