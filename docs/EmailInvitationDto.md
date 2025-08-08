# EmailInvitationDto
The email invitation parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email address. | [optional] 

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


