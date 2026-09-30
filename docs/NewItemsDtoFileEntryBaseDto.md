# NewItemsDtoFileEntryBaseDto
One day of the entries the caller has not opened yet, the groups running from the most recent day backwards.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | [**ApiDateTime**](ApiDateTime.md) | The day the grouped entries were last changed, written with the offset of the portal time zone. The time part  is the moment of the newest entry of the group. | 
**items** | [**List[FileEntryBaseDto]**](FileEntryBaseDto.md) | What changed on that day, the most recent first. Folders are left out of it, so an entry here is always a file  or a room that holds them. | 

## Example

```python
from docspace_api_sdk.models.new_items_dto_file_entry_base_dto import NewItemsDtoFileEntryBaseDto

# TODO update the JSON string below
json = "{}"
# create an instance of NewItemsDtoFileEntryBaseDto from a JSON string
new_items_dto_file_entry_base_dto_instance = NewItemsDtoFileEntryBaseDto.from_json(json)
# print the JSON string representation of the object
print(NewItemsDtoFileEntryBaseDto.to_json())

# convert the object into a dict
new_items_dto_file_entry_base_dto_dict = new_items_dto_file_entry_base_dto_instance.to_dict()
# create an instance of NewItemsDtoFileEntryBaseDto from a dict
new_items_dto_file_entry_base_dto_from_dict = NewItemsDtoFileEntryBaseDto.from_dict(new_items_dto_file_entry_base_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


