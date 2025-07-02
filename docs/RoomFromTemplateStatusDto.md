# RoomFromTemplateStatusDto
The progress parameters of creating a room from the template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_id** | **int** | The room ID. | [optional] 
**progress** | **float** | The progress of creating a room from the template. | [optional] 
**error** | **str** | The error message that is sent when a room is not created successfully from the template. | [optional] 
**is_completed** | **bool** | Specifies whether the process of creating a room from the template is completed. | [optional] 

## Example

```python
from docspace-api-python.models.room_from_template_status_dto import RoomFromTemplateStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoomFromTemplateStatusDto from a JSON string
room_from_template_status_dto_instance = RoomFromTemplateStatusDto.from_json(json)
# print the JSON string representation of the object
print(RoomFromTemplateStatusDto.to_json())

# convert the object into a dict
room_from_template_status_dto_dict = room_from_template_status_dto_instance.to_dict()
# create an instance of RoomFromTemplateStatusDto from a dict
room_from_template_status_dto_from_dict = RoomFromTemplateStatusDto.from_dict(room_from_template_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


