# RoomDataLifetimeDto
The room data lifetime information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_permanently** | **bool** | Specifies whether to permanently delete the room data or not. | [optional] 
**period** | [**RoomDataLifetimePeriod**](RoomDataLifetimePeriod.md) |  | [optional] 
**value** | **int** | Specifies the time period value of the room data lifetime. | [optional] 
**enabled** | **bool** | Specifies whether the room data lifetime setting is enabled or not. | [optional] 

## Example

```python
from docspace-api-python.models.room_data_lifetime_dto import RoomDataLifetimeDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoomDataLifetimeDto from a JSON string
room_data_lifetime_dto_instance = RoomDataLifetimeDto.from_json(json)
# print the JSON string representation of the object
print(RoomDataLifetimeDto.to_json())

# convert the object into a dict
room_data_lifetime_dto_dict = room_data_lifetime_dto_instance.to_dict()
# create an instance of RoomDataLifetimeDto from a dict
room_data_lifetime_dto_from_dict = RoomDataLifetimeDto.from_dict(room_data_lifetime_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


