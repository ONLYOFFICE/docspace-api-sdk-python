# AdminMessageSettingsRequestsDto
The message sent to the portal administrators, with the CAPTCHA proof that a person wrote it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | What the sender wants to tell the portal administrators. Markup is stripped before the letter is written, so  a body that carries nothing but markup counts as empty and is refused with 400. | 
**email** | **str** | The address the sender can be answered at, which the letter is signed with. It has to be a well-formed email  address. | 
**culture** | **str** | The language the letter is written in, as a culture name such as `en-US`. A culture the installation does not  have falls back to the portal language rather than failing the call. | [optional] 
**recaptcha_type** | [**RecaptchaType**](RecaptchaType.md) | Which CAPTCHA service the proof in `recaptchaResponse` came from. It has to match the service the  installation is configured with, which `GET api/2.0/capabilities` reports; the default value means the  installation is left to decide. | [optional] 
**recaptcha_response** | **str** | The token the CAPTCHA widget produced in the browser, passed on unchanged for the portal to verify with the  CAPTCHA service. It is single-use and short-lived, so it cannot be reused for a second message. | [optional] 

## Example

```python
from docspace_api_sdk.models.admin_message_settings_requests_dto import AdminMessageSettingsRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AdminMessageSettingsRequestsDto from a JSON string
admin_message_settings_requests_dto_instance = AdminMessageSettingsRequestsDto.from_json(json)
# print the JSON string representation of the object
print(AdminMessageSettingsRequestsDto.to_json())

# convert the object into a dict
admin_message_settings_requests_dto_dict = admin_message_settings_requests_dto_instance.to_dict()
# create an instance of AdminMessageSettingsRequestsDto from a dict
admin_message_settings_requests_dto_from_dict = AdminMessageSettingsRequestsDto.from_dict(admin_message_settings_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


