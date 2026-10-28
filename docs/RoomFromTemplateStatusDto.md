# RoomFromTemplateStatusDto
The progress of the job that creates a room out of a room template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_id** | **int** | The room the job is creating. It is meaningful once the room exists, which is guaranteed only after  `isCompleted` turns true and `error` stays empty; until then it carries no usable id. | 
**progress** | **float** | How far the job has got. The value climbs while the contents of the template are being copied into the new  room and reaches its maximum at the very end. | 
**error** | **str** | Why the job stopped. It is empty while the job runs and after a successful one, and a filled value means that  no room was created, so the request has to be repeated rather than waited out. | 
**is_completed** | **bool** | Whether the job has ended. It is set both after a successful creation and after a failure, so it is the flag  to poll for, while `error` is what separates the two outcomes. | 

## Example

```python
from docspace_api_sdk.models.room_from_template_status_dto import RoomFromTemplateStatusDto

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


