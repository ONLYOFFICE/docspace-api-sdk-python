# CreateRoomFromTemplateDto
The parameters for creating a room from a template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **int** | The template ID from which the room to be created. | 
**title** | **str** | The room title. | 
**logo** | [**LogoRequest**](LogoRequest.md) |  | [optional] 
**copy_logo** | **bool** | Specifies whether to copy a logo or not. | [optional] 
**tags** | **List[str]** | The collection of tags. | [optional] 
**color** | **str** | The color of the room to be created. | [optional] 
**cover** | **str** | The cover of the room to be created. | [optional] 
**quota** | **int** | The room quota. | [optional] 
**indexing** | **bool** | Specifies whether to create a room with indexing. | [optional] 
**deny_download** | **bool** | Specifies whether to deny downloads from the room. | [optional] 
**lifetime** | [**RoomDataLifetimeDto**](RoomDataLifetimeDto.md) |  | [optional] 
**watermark** | [**WatermarkRequestDto**](WatermarkRequestDto.md) |  | [optional] 
**private** | **bool** | Specifies whether the room to be created is private or not. | [optional] 

## Example

```python
from docspace-api-sdk.models.create_room_from_template_dto import CreateRoomFromTemplateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRoomFromTemplateDto from a JSON string
create_room_from_template_dto_instance = CreateRoomFromTemplateDto.from_json(json)
# print the JSON string representation of the object
print(CreateRoomFromTemplateDto.to_json())

# convert the object into a dict
create_room_from_template_dto_dict = create_room_from_template_dto_instance.to_dict()
# create an instance of CreateRoomFromTemplateDto from a dict
create_room_from_template_dto_from_dict = CreateRoomFromTemplateDto.from_dict(create_room_from_template_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


