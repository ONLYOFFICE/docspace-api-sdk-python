# UserInvitationRequestDto
The user invitation parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The address of somebody who has no portal account yet. An invitation is sent to it and an account is created  once it is accepted, so this is the field to use instead of an account identifier when the person is new to  the portal. | [optional] 
**type** | [**EmployeeType**](EmployeeType.md) | The user type. | [optional] 

## Example

```python
from docspace_api_sdk.models.user_invitation_request_dto import UserInvitationRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserInvitationRequestDto from a JSON string
user_invitation_request_dto_instance = UserInvitationRequestDto.from_json(json)
# print the JSON string representation of the object
print(UserInvitationRequestDto.to_json())

# convert the object into a dict
user_invitation_request_dto_dict = user_invitation_request_dto_instance.to_dict()
# create an instance of UserInvitationRequestDto from a dict
user_invitation_request_dto_from_dict = UserInvitationRequestDto.from_dict(user_invitation_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


