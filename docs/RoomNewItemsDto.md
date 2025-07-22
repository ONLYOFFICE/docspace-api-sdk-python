# RoomNewItemsDto
The room new items information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room** | [**FileEntryDto**](FileEntryDto.md) |  | [optional] 
**items** | [**List[FileEntryDto]**](FileEntryDto.md) | The list of file entry items. | [optional] 

## Example

```python
from docspace-api-sdk.models.room_new_items_dto import RoomNewItemsDto

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


