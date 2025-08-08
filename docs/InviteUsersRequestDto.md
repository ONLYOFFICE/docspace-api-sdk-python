# InviteUsersRequestDto
The request parameters for inviting users.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitations** | [**List[UserInvitationRequestDto]**](UserInvitationRequestDto.md) | The list of user invitations. | 
**culture** | **str** | The culture code of invitations. | [optional] 

## Example

```python
from docspace_api_sdk.models.invite_users_request_dto import InviteUsersRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of InviteUsersRequestDto from a JSON string
invite_users_request_dto_instance = InviteUsersRequestDto.from_json(json)
# print the JSON string representation of the object
print(InviteUsersRequestDto.to_json())

# convert the object into a dict
invite_users_request_dto_dict = invite_users_request_dto_instance.to_dict()
# create an instance of InviteUsersRequestDto from a dict
invite_users_request_dto_from_dict = InviteUsersRequestDto.from_dict(invite_users_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


