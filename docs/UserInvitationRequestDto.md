# UserInvitationRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EmployeeType**](EmployeeType.md) |  | [optional] 
**email** | **str** | Email address | [optional] 

## Example

```python
from docspace.models.user_invitation_request_dto import UserInvitationRequestDto

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


