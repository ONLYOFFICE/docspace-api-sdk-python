# StorageSettings
The storage settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module** | **str** | The storage name. | [optional] 
**props** | **Dict[str, Optional[str]]** | The storage properties. | [optional] 
**last_modified** | **datetime** | The date and time when the storage settings were last modified. | [optional] 

## Example

```python
from docspace_api_sdk.models.storage_settings import StorageSettings

# TODO update the JSON string below
json = "{}"
# create an instance of StorageSettings from a JSON string
storage_settings_instance = StorageSettings.from_json(json)
# print the JSON string representation of the object
print(StorageSettings.to_json())

# convert the object into a dict
storage_settings_dict = storage_settings_instance.to_dict()
# create an instance of StorageSettings from a dict
storage_settings_from_dict = StorageSettings.from_dict(storage_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


