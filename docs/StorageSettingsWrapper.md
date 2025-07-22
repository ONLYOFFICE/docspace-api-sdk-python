# StorageSettingsWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**StorageSettings**](StorageSettings.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.storage_settings_wrapper import StorageSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of StorageSettingsWrapper from a JSON string
storage_settings_wrapper_instance = StorageSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(StorageSettingsWrapper.to_json())

# convert the object into a dict
storage_settings_wrapper_dict = storage_settings_wrapper_instance.to_dict()
# create an instance of StorageSettingsWrapper from a dict
storage_settings_wrapper_from_dict = StorageSettingsWrapper.from_dict(storage_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


