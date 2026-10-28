# LoginSettingsRequestDto
The brute-force protection of the sign-in form: how many failures, over how long, cost how long a block.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt_count** | **int** | How many failed sign-in attempts inside one window are tolerated before the offender is blocked. Attempts are  counted per user name and client address together, so one member being blocked leaves the rest of the portal  signing in normally. | [optional] 
**block_time** | **int** | How long, in seconds, a blocked user name and address pair stays refused. While the block lasts the sign-in  is refused even when the password is finally correct. | [optional] 
**check_period** | **int** | The length, in seconds, of the rolling window the failed attempts are counted over. A wider window makes the  same `attemptCount` stricter, because failures further apart still add up. | [optional] 

## Example

```python
from docspace_api_sdk.models.login_settings_request_dto import LoginSettingsRequestDto

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


