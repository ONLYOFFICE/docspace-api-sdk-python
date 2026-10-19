# PasswordHashSettingsDto
The parameters a client hashes a password with before sending it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | The length of the hash, in bytes. | [optional] 
**iterations** | **int** | The number of PBKDF2 iterations. | [optional] 
**salt** | **str** | The salt the installation hashes passwords with. | [optional] 

## Example

```python
from docspace_api_sdk.models.password_hash_settings_dto import PasswordHashSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordHashSettingsDto from a JSON string
password_hash_settings_dto_instance = PasswordHashSettingsDto.from_json(json)
# print the JSON string representation of the object
print(PasswordHashSettingsDto.to_json())

# convert the object into a dict
password_hash_settings_dto_dict = password_hash_settings_dto_instance.to_dict()
# create an instance of PasswordHashSettingsDto from a dict
password_hash_settings_dto_from_dict = PasswordHashSettingsDto.from_dict(password_hash_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


