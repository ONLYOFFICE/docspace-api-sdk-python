# AiRoomDataLifetimeDto
The room data lifetime information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_permanently** | **bool** | Specifies whether to permanently delete the room data or not. | [optional] 
**period** | [**AiRoomDataLifetimePeriod**](AiRoomDataLifetimePeriod.md) | Specifies the time period type of the room data lifetime. | [optional] 
**value** | **int** | Specifies the time period value of the room data lifetime. | [optional] 
**enabled** | **bool** | Specifies whether the room data lifetime setting is enabled or not. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_room_data_lifetime_dto import AiRoomDataLifetimeDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiRoomDataLifetimeDto from a JSON string
ai_room_data_lifetime_dto_instance = AiRoomDataLifetimeDto.from_json(json)
# print the JSON string representation of the object
print(AiRoomDataLifetimeDto.to_json())

# convert the object into a dict
ai_room_data_lifetime_dto_dict = ai_room_data_lifetime_dto_instance.to_dict()
# create an instance of AiRoomDataLifetimeDto from a dict
ai_room_data_lifetime_dto_from_dict = AiRoomDataLifetimeDto.from_dict(ai_room_data_lifetime_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


