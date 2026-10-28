# TurnOnAdminMessageSettingsRequestDto
Whether the sign-in page offers the form for writing to the portal administrators.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**turn_on** | **bool** | Whether the form is offered. Switching it off hides the form for everybody and makes the operation that  submits it refuse new messages; letters already sent are untouched. | [optional] 

## Example

```python
from docspace_api_sdk.models.turn_on_admin_message_settings_request_dto import TurnOnAdminMessageSettingsRequestDto

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


