# StorageSettingsDto
The storage the portal keeps its data in, or serves its static content from.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module** | **str** | The storage module, or `null` when the built-in storage is used. | [optional] 
**props** | **Dict[str, Optional[str]]** | The connection properties stored for the module. | [optional] 
**last_modified** | **datetime** | When the settings were last stored. | [optional] 

## Example

```python
from docspace_api_sdk.models.storage_settings_dto import StorageSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of StorageSettingsDto from a JSON string
storage_settings_dto_instance = StorageSettingsDto.from_json(json)
# print the JSON string representation of the object
print(StorageSettingsDto.to_json())

# convert the object into a dict
storage_settings_dto_dict = storage_settings_dto_instance.to_dict()
# create an instance of StorageSettingsDto from a dict
storage_settings_dto_from_dict = StorageSettingsDto.from_dict(storage_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


