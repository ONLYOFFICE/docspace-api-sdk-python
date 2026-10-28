# RoomInvitationRequest
One batch of membership changes for a room.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitations** | [**List[RoomInvitation]**](RoomInvitation.md) | Who is added, changed or removed, one entry per subject. The same subject named twice keeps the level of the  last entry, and an empty list is accepted and changes nothing. | [optional] 
**notify** | **bool** | Whether the subjects that gained access are told about it by email. With it off the change is silent, which is  the usual choice when membership is synchronised from another system. | [optional] 
**message** | **str** | The line added to the invitation email. It is used only while the notification is on, and it reaches nobody  whose access was removed. | [optional] 
**culture** | **str** | The language of the invitation email, as a portal culture name such as en-US. Leaving it out sends each  message in the language of its recipient. | [optional] 
**force** | **bool** | Whether a member who still holds a role in an unfinished form is removed anyway. With it off such a removal is  refused and reported through the error of the answer, so the form can be reassigned first. | [optional] 

## Example

```python
from docspace_api_sdk.models.room_invitation_request import RoomInvitationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RoomInvitationRequest from a JSON string
room_invitation_request_instance = RoomInvitationRequest.from_json(json)
# print the JSON string representation of the object
print(RoomInvitationRequest.to_json())

# convert the object into a dict
room_invitation_request_dict = room_invitation_request_instance.to_dict()
# create an instance of RoomInvitationRequest from a dict
room_invitation_request_from_dict = RoomInvitationRequest.from_dict(room_invitation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


