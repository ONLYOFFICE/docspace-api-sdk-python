# BaseStorageSettingsCdnStorageSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module** | **str** |  | [optional] 
**props** | **Dict[str, Optional[str]]** |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**last_modified** | **datetime** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.base_storage_settings_cdn_storage_settings import BaseStorageSettingsCdnStorageSettings

# TODO update the JSON string below
json = "{}"
# create an instance of BaseStorageSettingsCdnStorageSettings from a JSON string
base_storage_settings_cdn_storage_settings_instance = BaseStorageSettingsCdnStorageSettings.from_json(json)
# print the JSON string representation of the object
print(BaseStorageSettingsCdnStorageSettings.to_json())

# convert the object into a dict
base_storage_settings_cdn_storage_settings_dict = base_storage_settings_cdn_storage_settings_instance.to_dict()
# create an instance of BaseStorageSettingsCdnStorageSettings from a dict
base_storage_settings_cdn_storage_settings_from_dict = BaseStorageSettingsCdnStorageSettings.from_dict(base_storage_settings_cdn_storage_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


