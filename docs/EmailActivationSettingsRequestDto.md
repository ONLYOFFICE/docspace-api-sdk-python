# EmailActivationSettingsRequestDto
Whether the calling user wants to keep seeing the reminder to confirm their email address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**show** | **bool** | Whether the reminder is shown; send false to dismiss it for the calling user. | [optional] 
**last_modified** | **datetime** | Accepted for compatibility with earlier clients and not read: the server keeps its own value. | [optional] 

## Example

```python
from docspace_api_sdk.models.email_activation_settings_request_dto import EmailActivationSettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmailActivationSettingsRequestDto from a JSON string
email_activation_settings_request_dto_instance = EmailActivationSettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(EmailActivationSettingsRequestDto.to_json())

# convert the object into a dict
email_activation_settings_request_dto_dict = email_activation_settings_request_dto_instance.to_dict()
# create an instance of EmailActivationSettingsRequestDto from a dict
email_activation_settings_request_dto_from_dict = EmailActivationSettingsRequestDto.from_dict(email_activation_settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


