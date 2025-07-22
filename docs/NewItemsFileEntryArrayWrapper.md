# NewItemsFileEntryArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[NewItemsDtoFileEntryDto]**](NewItemsDtoFileEntryDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.new_items_file_entry_array_wrapper import NewItemsFileEntryArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of NewItemsFileEntryArrayWrapper from a JSON string
new_items_file_entry_array_wrapper_instance = NewItemsFileEntryArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(NewItemsFileEntryArrayWrapper.to_json())

# convert the object into a dict
new_items_file_entry_array_wrapper_dict = new_items_file_entry_array_wrapper_instance.to_dict()
# create an instance of NewItemsFileEntryArrayWrapper from a dict
new_items_file_entry_array_wrapper_from_dict = NewItemsFileEntryArrayWrapper.from_dict(new_items_file_entry_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


