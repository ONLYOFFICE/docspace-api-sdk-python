# RoomNewItemsDto
The unseen entries of one room inside a day group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room** | [**FileEntryBaseDto**](FileEntryBaseDto.md) | The room the entries were found in, in its short form: only the identifier, the title, the room type and the  logo are filled in. | [optional] 
**items** | [**List[FileEntryBaseDto]**](FileEntryBaseDto.md) | The files of that room the caller has not opened yet, the most recently changed first. Reading them here does  not clear the badges; opening the room itself does. | [optional] 

## Example

```python
from docspace_api_sdk.models.room_new_items_dto import RoomNewItemsDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoomNewItemsDto from a JSON string
room_new_items_dto_instance = RoomNewItemsDto.from_json(json)
# print the JSON string representation of the object
print(RoomNewItemsDto.to_json())

# convert the object into a dict
room_new_items_dto_dict = room_new_items_dto_instance.to_dict()
# create an instance of RoomNewItemsDto from a dict
room_new_items_dto_from_dict = RoomNewItemsDto.from_dict(room_new_items_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


