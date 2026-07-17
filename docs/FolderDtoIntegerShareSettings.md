# FolderDtoIntegerShareSettings
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
from docspace_api_sdk.models.folder_dto_integer_share_settings import FolderDtoIntegerShareSettings

# TODO update the JSON string below
json = "{}"
# create an instance of FolderDtoIntegerShareSettings from a JSON string
folder_dto_integer_share_settings_instance = FolderDtoIntegerShareSettings.from_json(json)
# print the JSON string representation of the object
print(FolderDtoIntegerShareSettings.to_json())

# convert the object into a dict
folder_dto_integer_share_settings_dict = folder_dto_integer_share_settings_instance.to_dict()
# create an instance of FolderDtoIntegerShareSettings from a dict
folder_dto_integer_share_settings_from_dict = FolderDtoIntegerShareSettings.from_dict(folder_dto_integer_share_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


