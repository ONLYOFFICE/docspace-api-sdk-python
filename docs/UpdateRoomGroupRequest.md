# UpdateRoomGroupRequest
The changes to apply to a room group: its name and the rooms to add or remove.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rooms_to_add** | [**List[DuplicateRequestDtoAllOfFileIds]**](DuplicateRequestDtoAllOfFileIds.md) | The list of room IDs to add to the group. | [optional] 
**rooms_to_remove** | [**List[DuplicateRequestDtoAllOfFileIds]**](DuplicateRequestDtoAllOfFileIds.md) | The list of room IDs to remove from the group. | [optional] 
**group_name** | **str** | The group name. | [optional] 

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


