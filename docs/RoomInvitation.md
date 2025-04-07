# RoomInvitation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address | [optional] 
**id** | **str** | ID of the user with whom we want to share a room | [optional] 
**access** | [**FileShare**](FileShare.md) |  | [optional] 

## Example

```python
from docspace.models.room_invitation import RoomInvitation

# TODO update the JSON string below
json = "{}"
# create an instance of RoomInvitation from a JSON string
room_invitation_instance = RoomInvitation.from_json(json)
# print the JSON string representation of the object
print(RoomInvitation.to_json())

# convert the object into a dict
room_invitation_dict = room_invitation_instance.to_dict()
# create an instance of RoomInvitation from a dict
room_invitation_from_dict = RoomInvitation.from_dict(room_invitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


