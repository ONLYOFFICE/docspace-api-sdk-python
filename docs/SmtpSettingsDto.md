# SmtpSettingsDto
The mail server the portal sends its letters through.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | The host name or address of the mail server. On a cloud portal that has saved no relay of its own every  field of this object comes back empty, because the installation's own server is not disclosed - only  `isDefaultSettings` is set there. | [optional] 
**port** | **int** | The port the mail server is reached on - conventionally 25 or 587 without encryption from the start, 465  with it. It is empty when no port was stored, in which case the portal falls back to its own default. | [optional] 
**sender_address** | **str** | The address the letters are sent from, which appears in the From header and is what a reply goes to. | [optional] 
**sender_display_name** | **str** | The name shown beside that address in a recipient's mailbox. | [optional] 
**credentials_user_name** | **str** | The account the portal signs in to the mail server as, meaningful only while `enableAuth` is `true`. | [optional] 
**credentials_user_password** | **str** | Always empty here: the stored password is never returned, so a client that sends these settings back has  to supply it again rather than echoing what it read. | [optional] 
**enable_ssl** | **bool** | Whether the connection to the mail server is encrypted. | [optional] 
**enable_auth** | **bool** | Whether the portal signs in to the mail server at all. While it is `false` the credentials above are  ignored and the server is expected to accept mail unauthenticated. | [optional] 
**use_ntlm** | **bool** | Always `false` here: the flag is accepted when settings are saved but is not stored, so it never comes  back set and says nothing about how the portal authenticates. | [optional] 
**is_default_settings** | **bool** | Whether the portal is still on the mail configuration of the installation rather than on a relay of its  own. `DELETE api/2.0/smtpsettings/smtp` puts it back to `true`, and while it is `true` on a cloud portal  the fields above are blank rather than showing the installation's server. | [optional] 

## Example

```python
from docspace_api_sdk.models.smtp_settings_dto import SmtpSettingsDto

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


