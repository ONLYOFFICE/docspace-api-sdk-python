# LoginSettingsDto
The login settings parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt_count** | **int** | The maximum number of consecutive failed login attempts allowed before triggering account suspension. | 
**block_time** | **int** | The duration (in minutes) for which an account remains suspended after exceeding maximum login attempts. | 
**check_period** | **int** | The maximum time (in seconds) allowed for server to process and respond to login requests. | 
**is_default** | **bool** | Specifies if these settings are default or not | 

## Example

```python
from docspace_api_sdk.models.login_settings_dto import LoginSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoginSettingsDto from a JSON string
login_settings_dto_instance = LoginSettingsDto.from_json(json)
# print the JSON string representation of the object
print(LoginSettingsDto.to_json())

# convert the object into a dict
login_settings_dto_dict = login_settings_dto_instance.to_dict()
# create an instance of LoginSettingsDto from a dict
login_settings_dto_from_dict = LoginSettingsDto.from_dict(login_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


