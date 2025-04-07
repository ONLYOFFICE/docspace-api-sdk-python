# CreateRoomRequestDto

Request parameters for creating a room

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
**room_type** | [**RoomType**](RoomType.md) |  | [optional] 
**private** | **bool** | Private | [optional] 
**share** | [**List[FileShareParams]**](FileShareParams.md) | Collection of sharing parameters | [optional] 

## Example

```python
from docspace.models.create_room_request_dto import CreateRoomRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRoomRequestDto from a JSON string
create_room_request_dto_instance = CreateRoomRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateRoomRequestDto.to_json())

# convert the object into a dict
create_room_request_dto_dict = create_room_request_dto_instance.to_dict()
# create an instance of CreateRoomRequestDto from a dict
create_room_request_dto_from_dict = CreateRoomRequestDto.from_dict(create_room_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


