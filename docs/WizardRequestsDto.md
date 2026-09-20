# WizardRequestsDto
What the initial setup wizard needs to finish a new portal: the owner credentials and the portal locale.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The address the portal owner account is created with, which is also the address every administrative letter  goes to afterwards. It has to be a well-formed email address; a malformed one leaves the wizard unfinished. | 
**password_hash** | **str** | The owner password, already hashed in the client rather than sent in the clear. Hash it with the `salt`,  iteration count and hash size that `GET api/2.0/settings?withpassword=true` publishes, so the portal can  recognise it later; an empty value leaves the wizard unfinished. | 
**lng** | **str** | The portal interface language, as a culture name such as `en-US`. It has to be one of the cultures enabled  for the installation, and an unknown one leaves the shipped default in place instead of failing the wizard. | [optional] 
**time_zone** | **str** | The time zone every portal date is rendered in, as an IANA identifier such as `Europe/Riga`. A value that  matches nothing falls back to UTC rather than failing the wizard. | [optional] 
**ami_id** | **str** | The identifier of the Amazon Machine Image the portal was launched from, for an installation started from an  AWS image. It is recorded for the installation record only and changes nothing about the portal; leave it out  anywhere else. | [optional] 
**subscribe_from_site** | **bool** | Whether the owner agrees to receive product news at the address in `email`. It is a mailing consent and has  no bearing on the portal notifications, which are subscribed separately. | [optional] 

## Example

```python
from docspace_api_sdk.models.wizard_requests_dto import WizardRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of WizardRequestsDto from a JSON string
wizard_requests_dto_instance = WizardRequestsDto.from_json(json)
# print the JSON string representation of the object
print(WizardRequestsDto.to_json())

# convert the object into a dict
wizard_requests_dto_dict = wizard_requests_dto_instance.to_dict()
# create an instance of WizardRequestsDto from a dict
wizard_requests_dto_from_dict = WizardRequestsDto.from_dict(wizard_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


