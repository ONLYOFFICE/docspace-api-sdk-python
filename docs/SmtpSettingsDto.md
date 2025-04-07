# SmtpSettingsDto

SMTP settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Host | [optional] 
**port** | **int** | Port | [optional] 
**sender_address** | **str** | Sender address | [optional] 
**sender_display_name** | **str** | Sender display name | [optional] 
**credentials_user_name** | **str** | Credentials username | [optional] 
**credentials_user_password** | **str** | Credentials user password | [optional] 
**enable_ssl** | **bool** | Enables SSL or not | [optional] 
**enable_auth** | **bool** | Enables authentication or not | [optional] 
**use_ntlm** | **bool** | Specifies whether to use NTLM or not | [optional] 
**is_default_settings** | **bool** | Specifies if the current settings are default or not | [optional] 

## Example

```python
from docspace.models.smtp_settings_dto import SmtpSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SmtpSettingsDto from a JSON string
smtp_settings_dto_instance = SmtpSettingsDto.from_json(json)
# print the JSON string representation of the object
print(SmtpSettingsDto.to_json())

# convert the object into a dict
smtp_settings_dto_dict = smtp_settings_dto_instance.to_dict()
# create an instance of SmtpSettingsDto from a dict
smtp_settings_dto_from_dict = SmtpSettingsDto.from_dict(smtp_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


