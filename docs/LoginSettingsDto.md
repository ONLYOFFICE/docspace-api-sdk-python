# LoginSettingsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt_count** | **int** | Maximum number of the user attempts to log in | [optional] 
**block_time** | **int** | The time for which the user will be blocked after unsuccessful login attempts | [optional] 
**check_period** | **int** | The time to wait for a response from the server | [optional] 
**is_default** | **bool** | Specifies if these settings are default or not | [optional] 

## Example

```python
from docspace.models.login_settings_dto import LoginSettingsDto

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


