# ArchiveRoomRequest
The body of a room archiving request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_after** | **bool** | Whether the record of the finished job may be dropped without being read. With it off the record waits for the  first poll, which is what lets the caller learn how the move ended; it has no effect on the room itself. | [optional] 

## Example

```python
from docspace_api_sdk.models.archive_room_request import ArchiveRoomRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ArchiveRoomRequest from a JSON string
archive_room_request_instance = ArchiveRoomRequest.from_json(json)
# print the JSON string representation of the object
print(ArchiveRoomRequest.to_json())

# convert the object into a dict
archive_room_request_dict = archive_room_request_instance.to_dict()
# create an instance of ArchiveRoomRequest from a dict
archive_room_request_from_dict = ArchiveRoomRequest.from_dict(archive_room_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


