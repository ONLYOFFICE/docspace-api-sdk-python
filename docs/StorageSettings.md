# StorageSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module** | **str** |  | [optional] 
**props** | **Dict[str, Optional[str]]** |  | [optional] 
**last_modified** | **datetime** |  | [optional] 

## Example

```python
from docspace-api-python.models.storage_settings import StorageSettings

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


