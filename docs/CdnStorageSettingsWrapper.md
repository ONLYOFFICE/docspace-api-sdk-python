# CdnStorageSettingsWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CdnStorageSettings**](CdnStorageSettings.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.cdn_storage_settings_wrapper import CdnStorageSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of CdnStorageSettingsWrapper from a JSON string
cdn_storage_settings_wrapper_instance = CdnStorageSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(CdnStorageSettingsWrapper.to_json())

# convert the object into a dict
cdn_storage_settings_wrapper_dict = cdn_storage_settings_wrapper_instance.to_dict()
# create an instance of CdnStorageSettingsWrapper from a dict
cdn_storage_settings_wrapper_from_dict = CdnStorageSettingsWrapper.from_dict(cdn_storage_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


