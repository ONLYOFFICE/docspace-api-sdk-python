# AddRoomServersRequestBody
Parameters specifying which MCP servers to assign to the room.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servers** | **List[UUID]** | Set of unique identifiers of MCP servers to associate with the room. A maximum of 5 servers can be assigned per room. | 

## Example

```python
from docspace_api_sdk.models.add_room_servers_request_body import AddRoomServersRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of AddRoomServersRequestBody from a JSON string
add_room_servers_request_body_instance = AddRoomServersRequestBody.from_json(json)
# print the JSON string representation of the object
print(AddRoomServersRequestBody.to_json())

# convert the object into a dict
add_room_servers_request_body_dict = add_room_servers_request_body_instance.to_dict()
# create an instance of AddRoomServersRequestBody from a dict
add_room_servers_request_body_from_dict = AddRoomServersRequestBody.from_dict(add_room_servers_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


