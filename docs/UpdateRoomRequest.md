# UpdateRoomRequest

Parameters for updating a room

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Room name | [optional] 
**quota** | **int** | Room quota | [optional] 
**indexing** | **bool** | Indexing | [optional] 
**deny_download** | **bool** | Room quota | [optional] 
**lifetime** | [**RoomDataLifetimeDto**](RoomDataLifetimeDto.md) |  | [optional] 
**watermark** | [**WatermarkRequestDto**](WatermarkRequestDto.md) |  | [optional] 
**logo** | [**LogoRequest**](LogoRequest.md) |  | [optional] 
**tags** | **List[str]** | List of tags | [optional] 
**color** | **str** | Color | [optional] 
**cover** | **str** | Cover | [optional] 

## Example

```python
from docspace.models.update_room_request import UpdateRoomRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRoomRequest from a JSON string
update_room_request_instance = UpdateRoomRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRoomRequest.to_json())

# convert the object into a dict
update_room_request_dict = update_room_request_instance.to_dict()
# create an instance of UpdateRoomRequest from a dict
update_room_request_from_dict = UpdateRoomRequest.from_dict(update_room_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


