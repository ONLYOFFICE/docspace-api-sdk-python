# UserInvitation
Which pending room invitations are to be sent again.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users_ids** | **List[UUID]** | The accounts to write to, taken from `GET api/2.0/files/rooms/{id}/share`. Anyone who has already joined, is  not in the room, or is invisible to the caller is skipped without an error, and the field is ignored once  every pending invitation is being resent. | [optional] 
**resend_all** | **bool** | Whether every invitation of the room that is still waiting is sent again. With it on the list of accounts is  ignored, and with it off an empty list means that nothing is sent at all. | [optional] 

## Example

```python
from docspace_api_sdk.models.user_invitation import UserInvitation

# TODO update the JSON string below
json = "{}"
# create an instance of UserInvitation from a JSON string
user_invitation_instance = UserInvitation.from_json(json)
# print the JSON string representation of the object
print(UserInvitation.to_json())

# convert the object into a dict
user_invitation_dict = user_invitation_instance.to_dict()
# create an instance of UserInvitation from a dict
user_invitation_from_dict = UserInvitation.from_dict(user_invitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


