# FileEntryDtoIntegerAllOfAvailableShareRights
The available external rights of the file entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **List[str]** |  | [optional] 
**external_link** | **List[str]** |  | [optional] 
**group** | **List[str]** |  | [optional] 
**invitation_link** | **List[str]** |  | [optional] 
**primary_external_link** | **List[str]** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.file_entry_dto_integer_all_of_available_share_rights import FileEntryDtoIntegerAllOfAvailableShareRights

# TODO update the JSON string below
json = "{}"
# create an instance of FileEntryDtoIntegerAllOfAvailableShareRights from a JSON string
file_entry_dto_integer_all_of_available_share_rights_instance = FileEntryDtoIntegerAllOfAvailableShareRights.from_json(json)
# print the JSON string representation of the object
print(FileEntryDtoIntegerAllOfAvailableShareRights.to_json())

# convert the object into a dict
file_entry_dto_integer_all_of_available_share_rights_dict = file_entry_dto_integer_all_of_available_share_rights_instance.to_dict()
# create an instance of FileEntryDtoIntegerAllOfAvailableShareRights from a dict
file_entry_dto_integer_all_of_available_share_rights_from_dict = FileEntryDtoIntegerAllOfAvailableShareRights.from_dict(file_entry_dto_integer_all_of_available_share_rights_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


