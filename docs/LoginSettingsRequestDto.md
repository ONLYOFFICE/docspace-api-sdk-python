# LoginSettingsRequestDto

The request parameters for configuring login security and performance settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt_count** | **int** | The maximum number of consecutive failed login attempts allowed before triggering account suspension. | [optional] 
**block_time** | **int** | The duration (in minutes) for which an account remains suspended after exceeding maximum login attempts. | [optional] 
**check_period** | **int** | The maximum time (in seconds) allowed for server to process and respond to login requests. | [optional] 

## Example

```python
from docspace.models.login_settings_request_dto import LoginSettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoginSettingsRequestDto from a JSON string
login_settings_request_dto_instance = LoginSettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(LoginSettingsRequestDto.to_json())

# convert the object into a dict
login_settings_request_dto_dict = login_settings_request_dto_instance.to_dict()
# create an instance of LoginSettingsRequestDto from a dict
login_settings_request_dto_from_dict = LoginSettingsRequestDto.from_dict(login_settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


