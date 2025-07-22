# NewItemsDtoFileEntryDto
The new item parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**items** | [**List[FileEntryDto]**](FileEntryDto.md) | The list of items. | [optional] 

## Example

```python
from docspace-api-sdk.models.new_items_dto_file_entry_dto import NewItemsDtoFileEntryDto

# TODO update the JSON string below
json = "{}"
# create an instance of NewItemsDtoFileEntryDto from a JSON string
new_items_dto_file_entry_dto_instance = NewItemsDtoFileEntryDto.from_json(json)
# print the JSON string representation of the object
print(NewItemsDtoFileEntryDto.to_json())

# convert the object into a dict
new_items_dto_file_entry_dto_dict = new_items_dto_file_entry_dto_instance.to_dict()
# create an instance of NewItemsDtoFileEntryDto from a dict
new_items_dto_file_entry_dto_from_dict = NewItemsDtoFileEntryDto.from_dict(new_items_dto_file_entry_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


