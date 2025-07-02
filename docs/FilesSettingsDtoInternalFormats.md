# FilesSettingsDtoInternalFormats
The internal file formats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown** | **str** |  | [optional] 
**archive** | **str** |  | [optional] 
**video** | **str** |  | [optional] 
**audio** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**spreadsheet** | **str** |  | [optional] 
**presentation** | **str** |  | [optional] 
**document** | **str** |  | [optional] 
**pdf** | **str** |  | [optional] 

## Example

```python
from docspace-api-python.models.files_settings_dto_internal_formats import FilesSettingsDtoInternalFormats

# TODO update the JSON string below
json = "{}"
# create an instance of FilesSettingsDtoInternalFormats from a JSON string
files_settings_dto_internal_formats_instance = FilesSettingsDtoInternalFormats.from_json(json)
# print the JSON string representation of the object
print(FilesSettingsDtoInternalFormats.to_json())

# convert the object into a dict
files_settings_dto_internal_formats_dict = files_settings_dto_internal_formats_instance.to_dict()
# create an instance of FilesSettingsDtoInternalFormats from a dict
files_settings_dto_internal_formats_from_dict = FilesSettingsDtoInternalFormats.from_dict(files_settings_dto_internal_formats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


