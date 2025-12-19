# BaseStorageSettingsStorageSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module** | **str** |  | [optional] 
**props** | **Dict[str, Optional[str]]** |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**last_modified** | **datetime** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.base_storage_settings_storage_settings import BaseStorageSettingsStorageSettings

# TODO update the JSON string below
json = "{}"
# create an instance of BaseStorageSettingsStorageSettings from a JSON string
base_storage_settings_storage_settings_instance = BaseStorageSettingsStorageSettings.from_json(json)
# print the JSON string representation of the object
print(BaseStorageSettingsStorageSettings.to_json())

# convert the object into a dict
base_storage_settings_storage_settings_dict = base_storage_settings_storage_settings_instance.to_dict()
# create an instance of BaseStorageSettingsStorageSettings from a dict
base_storage_settings_storage_settings_from_dict = BaseStorageSettingsStorageSettings.from_dict(base_storage_settings_storage_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


