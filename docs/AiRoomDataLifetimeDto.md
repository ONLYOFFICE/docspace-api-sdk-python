# AiRoomDataLifetimeDto
The rule by which the files of a room are removed once they have been lying in it for too long.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_permanently** | **bool** | Decides what happens to a file that has grown too old: it is erased outright, or it is moved to the trash of  the account that created the room, from where it can still be brought back. | [optional] 
**period** | [**AiRoomDataLifetimePeriod**](AiRoomDataLifetimePeriod.md) | The unit the age is counted in. Months and years are counted as calendar ones, so the same number of them  covers a different number of days depending on when the clean-up runs. | [optional] 
**value** | **int** | How many periods a file may stay in the room, counted from the moment it was last changed rather than from the  moment the rule was set. Files that are already older than this are removed by the next clean-up. | [optional] 
**enabled** | **bool** | Switches the rule on and off. Switching it off erases the rule instead of keeping it aside, so afterwards the  room reports no rule at all and the other three values have to be sent again to bring it back. | [optional] 

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


