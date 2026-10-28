# AiFileEntryDtoAllOfShareSettings
How many links of each kind currently exist for the entry, counted separately for the primary link and the  additional ones. Kinds with no links are left out, and the whole field is null when the caller may not change  the access or no link exists at all.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **int** |  | [optional] 
**external_link** | **int** |  | [optional] 
**group** | **int** |  | [optional] 
**invitation_link** | **int** |  | [optional] 
**primary_external_link** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_file_entry_dto_all_of_share_settings import AiFileEntryDtoAllOfShareSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AiFileEntryDtoAllOfShareSettings from a JSON string
ai_file_entry_dto_all_of_share_settings_instance = AiFileEntryDtoAllOfShareSettings.from_json(json)
# print the JSON string representation of the object
print(AiFileEntryDtoAllOfShareSettings.to_json())

# convert the object into a dict
ai_file_entry_dto_all_of_share_settings_dict = ai_file_entry_dto_all_of_share_settings_instance.to_dict()
# create an instance of AiFileEntryDtoAllOfShareSettings from a dict
ai_file_entry_dto_all_of_share_settings_from_dict = AiFileEntryDtoAllOfShareSettings.from_dict(ai_file_entry_dto_all_of_share_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


