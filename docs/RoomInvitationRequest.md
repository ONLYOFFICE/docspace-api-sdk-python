# RoomInvitationRequest

Request parameters for inviting users to a room

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitations** | [**List[RoomInvitation]**](RoomInvitation.md) | Collection of invitation parameters | [optional] 
**notify** | **bool** | Notifies users about the shared room or not | [optional] 
**message** | **str** | Message to send when notifying about the shared room | [optional] 
**culture** | **str** | Culture | [optional] 

## Example

```python
from docspace.models.room_invitation_request import RoomInvitationRequest

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


