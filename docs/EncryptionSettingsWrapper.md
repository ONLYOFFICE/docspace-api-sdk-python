# EncryptionSettingsWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**EncryptionSettings**](EncryptionSettings.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.encryption_settings_wrapper import EncryptionSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptionSettingsWrapper from a JSON string
encryption_settings_wrapper_instance = EncryptionSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(EncryptionSettingsWrapper.to_json())

# convert the object into a dict
encryption_settings_wrapper_dict = encryption_settings_wrapper_instance.to_dict()
# create an instance of EncryptionSettingsWrapper from a dict
encryption_settings_wrapper_from_dict = EncryptionSettingsWrapper.from_dict(encryption_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


