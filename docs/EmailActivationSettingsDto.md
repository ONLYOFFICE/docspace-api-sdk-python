# EmailActivationSettingsDto
Whether the calling user is shown the reminder to confirm their email address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**show** | **bool** | Specifies whether the email activation settings are shown or hidden. | [optional] 
**last_modified** | **datetime** | The timestamp indicating when the settings were last modified. | [optional] 

## Example

```python
from docspace_api_sdk.models.email_activation_settings_dto import EmailActivationSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmailActivationSettingsDto from a JSON string
email_activation_settings_dto_instance = EmailActivationSettingsDto.from_json(json)
# print the JSON string representation of the object
print(EmailActivationSettingsDto.to_json())

# convert the object into a dict
email_activation_settings_dto_dict = email_activation_settings_dto_instance.to_dict()
# create an instance of EmailActivationSettingsDto from a dict
email_activation_settings_dto_from_dict = EmailActivationSettingsDto.from_dict(email_activation_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


