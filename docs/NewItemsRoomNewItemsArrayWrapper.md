# NewItemsRoomNewItemsArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[NewItemsDtoRoomNewItemsDto]**](NewItemsDtoRoomNewItemsDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.new_items_room_new_items_array_wrapper import NewItemsRoomNewItemsArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of NewItemsRoomNewItemsArrayWrapper from a JSON string
new_items_room_new_items_array_wrapper_instance = NewItemsRoomNewItemsArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(NewItemsRoomNewItemsArrayWrapper.to_json())

# convert the object into a dict
new_items_room_new_items_array_wrapper_dict = new_items_room_new_items_array_wrapper_instance.to_dict()
# create an instance of NewItemsRoomNewItemsArrayWrapper from a dict
new_items_room_new_items_array_wrapper_from_dict = NewItemsRoomNewItemsArrayWrapper.from_dict(new_items_room_new_items_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


