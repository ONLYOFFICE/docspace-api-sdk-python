# TurnOnAdminMessageSettingsRequestDto
The request parameters for enabling or disabling administrator messaging system.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**turn_on** | **bool** | The global switch for the administrator messaging functionality. | [optional] 

## Example

```python
from docspace-api-python.models.turn_on_admin_message_settings_request_dto import TurnOnAdminMessageSettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of TurnOnAdminMessageSettingsRequestDto from a JSON string
turn_on_admin_message_settings_request_dto_instance = TurnOnAdminMessageSettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(TurnOnAdminMessageSettingsRequestDto.to_json())

# convert the object into a dict
turn_on_admin_message_settings_request_dto_dict = turn_on_admin_message_settings_request_dto_instance.to_dict()
# create an instance of TurnOnAdminMessageSettingsRequestDto from a dict
turn_on_admin_message_settings_request_dto_from_dict = TurnOnAdminMessageSettingsRequestDto.from_dict(turn_on_admin_message_settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


