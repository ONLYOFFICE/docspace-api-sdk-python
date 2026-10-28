# EncryptionSettingsDto
The state of the portal's storage encryption.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Always an empty string: the encryption password is never returned. | [optional] 
**status** | [**EncryptionStatus**](EncryptionStatus.md) | Whether the storage is encrypted, decrypted, or on its way to either. | [optional] 
**notify_users** | **bool** | Whether the users are notified when the operation starts and ends. | [optional] 

## Example

```python
from docspace_api_sdk.models.encryption_settings_dto import EncryptionSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptionSettingsDto from a JSON string
encryption_settings_dto_instance = EncryptionSettingsDto.from_json(json)
# print the JSON string representation of the object
print(EncryptionSettingsDto.to_json())

# convert the object into a dict
encryption_settings_dto_dict = encryption_settings_dto_instance.to_dict()
# create an instance of EncryptionSettingsDto from a dict
encryption_settings_dto_from_dict = EncryptionSettingsDto.from_dict(encryption_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


