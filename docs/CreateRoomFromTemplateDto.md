# CreateRoomFromTemplateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **int** | Template id | [optional] 
**title** | **str** | Title | [optional] 
**logo** | [**LogoRequest**](LogoRequest.md) |  | [optional] 
**copy_logo** | **bool** | Copy logo | [optional] 
**tags** | **List[str]** | Collection of tags | [optional] 
**color** | **str** | Color | [optional] 
**cover** | **str** | Cover | [optional] 

## Example

```python
from docspace.models.create_room_from_template_dto import CreateRoomFromTemplateDto

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


