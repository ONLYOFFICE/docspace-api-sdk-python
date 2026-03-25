# DeleteRoomServersRequestBody
Parameters specifying which MCP servers to detach from the room.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servers** | **List[UUID]** | Set of unique identifiers of MCP servers to remove from the room. Associated connections and tool configurations will also be cleaned up. | 

## Example

```python
from docspace_api_sdk.models.delete_room_servers_request_body import DeleteRoomServersRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRoomServersRequestBody from a JSON string
delete_room_servers_request_body_instance = DeleteRoomServersRequestBody.from_json(json)
# print the JSON string representation of the object
print(DeleteRoomServersRequestBody.to_json())

# convert the object into a dict
delete_room_servers_request_body_dict = delete_room_servers_request_body_instance.to_dict()
# create an instance of DeleteRoomServersRequestBody from a dict
delete_room_servers_request_body_from_dict = DeleteRoomServersRequestBody.from_dict(delete_room_servers_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


