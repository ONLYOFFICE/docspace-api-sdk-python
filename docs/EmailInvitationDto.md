# EmailInvitationDto
The email invitation parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The address of somebody who has no portal account yet. An invitation is sent to it and an account is created  once it is accepted, so this is the field to use instead of an account identifier when the person is new to  the portal. | [optional] 

## Example

```python
from docspace_api_sdk.models.email_invitation_dto import EmailInvitationDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmailInvitationDto from a JSON string
email_invitation_dto_instance = EmailInvitationDto.from_json(json)
# print the JSON string representation of the object
print(EmailInvitationDto.to_json())

# convert the object into a dict
email_invitation_dto_dict = email_invitation_dto_instance.to_dict()
# create an instance of EmailInvitationDto from a dict
email_invitation_dto_from_dict = EmailInvitationDto.from_dict(email_invitation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


