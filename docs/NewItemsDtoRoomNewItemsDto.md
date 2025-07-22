# NewItemsDtoRoomNewItemsDto
The new item parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**items** | [**List[RoomNewItemsDto]**](RoomNewItemsDto.md) | The list of items. | [optional] 

## Example

```python
from docspace-api-sdk.models.new_items_dto_room_new_items_dto import NewItemsDtoRoomNewItemsDto

# TODO update the JSON string below
json = "{}"
# create an instance of NewItemsDtoRoomNewItemsDto from a JSON string
new_items_dto_room_new_items_dto_instance = NewItemsDtoRoomNewItemsDto.from_json(json)
# print the JSON string representation of the object
print(NewItemsDtoRoomNewItemsDto.to_json())

# convert the object into a dict
new_items_dto_room_new_items_dto_dict = new_items_dto_room_new_items_dto_instance.to_dict()
# create an instance of NewItemsDtoRoomNewItemsDto from a dict
new_items_dto_room_new_items_dto_from_dict = NewItemsDtoRoomNewItemsDto.from_dict(new_items_dto_room_new_items_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


