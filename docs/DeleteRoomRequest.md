# DeleteRoomRequest

The parameters for deleting a room.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_after** | **bool** | Specifies whether to delete a room after the editing session is finished or not. | [optional] 

## Example

```python
from docspace.models.delete_room_request import DeleteRoomRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRoomRequest from a JSON string
delete_room_request_instance = DeleteRoomRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteRoomRequest.to_json())

# convert the object into a dict
delete_room_request_dict = delete_room_request_instance.to_dict()
# create an instance of DeleteRoomRequest from a dict
delete_room_request_from_dict = DeleteRoomRequest.from_dict(delete_room_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


