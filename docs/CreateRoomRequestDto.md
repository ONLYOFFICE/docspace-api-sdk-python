# CreateRoomRequestDto
The request parameters for creating a room.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The room name. | 
**quota** | **int** | The room quota. | [optional] 
**indexing** | **bool** | Specifies whether to create a room with indexing. | [optional] 
**deny_download** | **bool** | Specifies whether to deny downloads from the room. | [optional] 
**lifetime** | [**RoomDataLifetimeDto**](RoomDataLifetimeDto.md) | The room data lifetime information. | [optional] 
**watermark** | [**WatermarkRequestDto**](WatermarkRequestDto.md) | The request parameters for adding watermarks. | [optional] 
**logo** | [**LogoRequest**](LogoRequest.md) | The logo request parameters. | [optional] 
**tags** | **List[str]** | The list of tags. | [optional] 
**color** | **str** | The room color, as a six-digit hexadecimal value without a leading '#'. | [optional] 
**cover** | **str** | The room cover. | [optional] 
**room_type** | [**RoomType**](RoomType.md) | The room type. | 
**private** | **bool** | Specifies whether the room to be created is private or not. | [optional] 
**share** | [**List[FileShareParams]**](FileShareParams.md) | The collection of sharing parameters. | [optional] 
**chat_settings** | [**ChatSettings**](ChatSettings.md) | The chat settings. | [optional] 
**send_form_to_external_db** | **bool** | Specifies whether to send form data to external database. | [optional] 
**save_form_as_xlsx** | **bool** | Specifies whether to save form data as XLSX file. | [optional] 

## Example

```python
from docspace_api_sdk.models.create_room_request_dto import CreateRoomRequestDto

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


