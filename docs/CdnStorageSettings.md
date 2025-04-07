# CdnStorageSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module** | **str** |  | [optional] 
**props** | **Dict[str, Optional[str]]** |  | [optional] 

## Example

```python
from docspace.models.cdn_storage_settings import CdnStorageSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CdnStorageSettings from a JSON string
cdn_storage_settings_instance = CdnStorageSettings.from_json(json)
# print the JSON string representation of the object
print(CdnStorageSettings.to_json())

# convert the object into a dict
cdn_storage_settings_dict = cdn_storage_settings_instance.to_dict()
# create an instance of CdnStorageSettings from a dict
cdn_storage_settings_from_dict = CdnStorageSettings.from_dict(cdn_storage_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


