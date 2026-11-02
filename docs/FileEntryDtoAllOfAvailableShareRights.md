# FileEntryDtoAllOfAvailableShareRights
Which access levels may be handed out on this entry, listed per kind of recipient, so that a client offers  only levels the entry actually supports - a room for filling forms and a plain folder do not accept the same  ones.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **List[str]** |  | [optional] 
**external_link** | **List[str]** |  | [optional] 
**group** | **List[str]** |  | [optional] 
**invitation_link** | **List[str]** |  | [optional] 
**primary_external_link** | **List[str]** |  | [optional] 
**ai_project** | **List[str]** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.file_entry_dto_all_of_available_share_rights import FileEntryDtoAllOfAvailableShareRights

# TODO update the JSON string below
json = "{}"
# create an instance of FileEntryDtoAllOfAvailableShareRights from a JSON string
file_entry_dto_all_of_available_share_rights_instance = FileEntryDtoAllOfAvailableShareRights.from_json(json)
# print the JSON string representation of the object
print(FileEntryDtoAllOfAvailableShareRights.to_json())

# convert the object into a dict
file_entry_dto_all_of_available_share_rights_dict = file_entry_dto_all_of_available_share_rights_instance.to_dict()
# create an instance of FileEntryDtoAllOfAvailableShareRights from a dict
file_entry_dto_all_of_available_share_rights_from_dict = FileEntryDtoAllOfAvailableShareRights.from_dict(file_entry_dto_all_of_available_share_rights_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


