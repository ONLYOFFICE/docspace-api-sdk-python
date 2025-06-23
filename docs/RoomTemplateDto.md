# RoomTemplateDto

The room template parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_id** | **int** | The room template ID. | 
**title** | **str** | The room template title. | [optional] 
**logo** | [**LogoRequest**](LogoRequest.md) |  | [optional] 
**copy_logo** | **bool** | Specifies whether to copy room logo or not. | [optional] 
**share** | **List[str]** | The collection of email addresses of users with whom to share a room. | [optional] 
**groups** | **List[str]** | The collection of groups with whom to share a room. | [optional] 
**public** | **bool** | Specifies whether the room template is public or not. | [optional] 
**tags** | **List[str]** | The collection of tags. | [optional] 
**color** | **str** | The color of the room template. | [optional] 
**cover** | **str** | The cover of the room template. | [optional] 
**quota** | **int** | Room quota | [optional] 

## Example

```python
from docspace.models.room_template_dto import RoomTemplateDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoomTemplateDto from a JSON string
room_template_dto_instance = RoomTemplateDto.from_json(json)
# print the JSON string representation of the object
print(RoomTemplateDto.to_json())

# convert the object into a dict
room_template_dto_dict = room_template_dto_instance.to_dict()
# create an instance of RoomTemplateDto from a dict
room_template_dto_from_dict = RoomTemplateDto.from_dict(room_template_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


