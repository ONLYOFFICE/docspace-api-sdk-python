# RoomTemplateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_id** | **int** | Room id | [optional] 
**title** | **str** | Title | [optional] 
**logo** | [**LogoRequest**](LogoRequest.md) |  | [optional] 
**copy_logo** | **bool** | Copy room logo | [optional] 
**share** | **List[str]** | Collection of share user emails | [optional] 
**groups** | **List[str]** | Collection of share groups | [optional] 
**public** | **bool** | Public | [optional] 
**tags** | **List[str]** | Collection of tags | [optional] 
**color** | **str** | Color | [optional] 
**cover** | **str** | Cover | [optional] 

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


