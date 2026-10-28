# LoginSettingsDto
The brute-force protection of the sign-in form: how many failures, over how long, cost how long a block.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt_count** | **int** | How many failed attempts inside one window are tolerated before the offender is blocked. Attempts are  counted per user name and client address together, so one member being blocked leaves the rest of the  portal signing in normally. | 
**block_time** | **int** | How long, in seconds, a blocked user name and address pair stays refused. While the block lasts the  sign-in is refused even once the password is correct. | 
**check_period** | **int** | The length, in seconds, of the rolling window the failures are counted over. It is not a request timeout: a  wider window makes the same `attemptCount` stricter, because failures further apart still add up. | 
**is_default** | **bool** | Whether the three numbers above still match the ones the installation ships with. It turns `false` as soon  as any of them is saved differently, and `true` again after  `DELETE api/2.0/settings/security/loginsettings`. | 

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


