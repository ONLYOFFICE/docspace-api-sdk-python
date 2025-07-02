# EncryptionSettings
The encryption settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | The encryption password. | [optional] 
**status** | [**EncryprtionStatus**](EncryprtionStatus.md) |  | [optional] 
**notify_users** | **bool** | Specifies if the users will be notified about the encryption operation or not. | [optional] 

## Example

```python
from docspace-api-python.models.encryption_settings import EncryptionSettings

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptionSettings from a JSON string
encryption_settings_instance = EncryptionSettings.from_json(json)
# print the JSON string representation of the object
print(EncryptionSettings.to_json())

# convert the object into a dict
encryption_settings_dict = encryption_settings_instance.to_dict()
# create an instance of EncryptionSettings from a dict
encryption_settings_from_dict = EncryptionSettings.from_dict(encryption_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


