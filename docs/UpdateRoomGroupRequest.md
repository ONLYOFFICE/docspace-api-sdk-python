# UpdateRoomGroupRequest
The changes to apply to a room group: a new name, rooms to attach and rooms to detach, in any combination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rooms_to_add** | [**List[DuplicateRequestDtoAllOfFileIds]**](DuplicateRequestDtoAllOfFileIds.md) | The rooms to attach to the group, each given as a number for a room stored in the portal or as a string for a  room on a connected third-party account. Every identifier has to name a room the caller can read; repeats and  rooms the group already holds are collapsed rather than refused. | [optional] 
**rooms_to_remove** | [**List[DuplicateRequestDtoAllOfFileIds]**](DuplicateRequestDtoAllOfFileIds.md) | The rooms to detach from the group, in the same two forms. Detaching leaves the room and its content  untouched, and a room the group already holds can be detached even when the caller has lost access to it in  the meantime. | [optional] 
**group_name** | **str** | The new name of the group, trimmed of surrounding spaces before it is stored. Leaving the member out keeps the  current name, and a name that is blank once trimmed is refused. | [optional] 

## Example

```python
from docspace_api_sdk.models.update_room_group_request import UpdateRoomGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRoomGroupRequest from a JSON string
update_room_group_request_instance = UpdateRoomGroupRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRoomGroupRequest.to_json())

# convert the object into a dict
update_room_group_request_dict = update_room_group_request_instance.to_dict()
# create an instance of UpdateRoomGroupRequest from a dict
update_room_group_request_from_dict = UpdateRoomGroupRequest.from_dict(update_room_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


