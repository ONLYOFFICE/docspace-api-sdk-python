# FileEntryDtoIntegerAllOfShareSettings
A dictionary representing the sharing settings for the file entry.

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
from docspace_api_sdk.models.file_entry_dto_integer_all_of_share_settings import FileEntryDtoIntegerAllOfShareSettings

# TODO update the JSON string below
json = "{}"
# create an instance of FileEntryDtoIntegerAllOfShareSettings from a JSON string
file_entry_dto_integer_all_of_share_settings_instance = FileEntryDtoIntegerAllOfShareSettings.from_json(json)
# print the JSON string representation of the object
print(FileEntryDtoIntegerAllOfShareSettings.to_json())

# convert the object into a dict
file_entry_dto_integer_all_of_share_settings_dict = file_entry_dto_integer_all_of_share_settings_instance.to_dict()
# create an instance of FileEntryDtoIntegerAllOfShareSettings from a dict
file_entry_dto_integer_all_of_share_settings_from_dict = FileEntryDtoIntegerAllOfShareSettings.from_dict(file_entry_dto_integer_all_of_share_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


