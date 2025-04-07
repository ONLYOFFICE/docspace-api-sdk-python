# RoomTemplateStatusDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **int** | Template id | [optional] 
**progress** | **float** | Progress | [optional] 
**error** | **str** | Error | [optional] 
**is_completed** | **bool** | IsCompleted | [optional] 

## Example

```python
from docspace.models.room_template_status_dto import RoomTemplateStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoomTemplateStatusDto from a JSON string
room_template_status_dto_instance = RoomTemplateStatusDto.from_json(json)
# print the JSON string representation of the object
print(RoomTemplateStatusDto.to_json())

# convert the object into a dict
room_template_status_dto_dict = room_template_status_dto_instance.to_dict()
# create an instance of RoomTemplateStatusDto from a dict
room_template_status_dto_from_dict = RoomTemplateStatusDto.from_dict(room_template_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


