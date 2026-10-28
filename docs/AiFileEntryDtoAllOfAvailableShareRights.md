# AiFileEntryDtoAllOfAvailableShareRights
Which access levels may be handed out on this entry, listed per kind of recipient, so that a client offers  only levels the entry actually supports - a room for filling forms and a plain folder do not accept the same  ones.

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
from docspace_api_sdk.models.ai_file_entry_dto_all_of_available_share_rights import AiFileEntryDtoAllOfAvailableShareRights

# TODO update the JSON string below
json = "{}"
# create an instance of AiFileEntryDtoAllOfAvailableShareRights from a JSON string
ai_file_entry_dto_all_of_available_share_rights_instance = AiFileEntryDtoAllOfAvailableShareRights.from_json(json)
# print the JSON string representation of the object
print(AiFileEntryDtoAllOfAvailableShareRights.to_json())

# convert the object into a dict
ai_file_entry_dto_all_of_available_share_rights_dict = ai_file_entry_dto_all_of_available_share_rights_instance.to_dict()
# create an instance of AiFileEntryDtoAllOfAvailableShareRights from a dict
ai_file_entry_dto_all_of_available_share_rights_from_dict = AiFileEntryDtoAllOfAvailableShareRights.from_dict(ai_file_entry_dto_all_of_available_share_rights_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


