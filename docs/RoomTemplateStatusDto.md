# RoomTemplateStatusDto
The progress of the job that builds a room template out of an existing room.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **int** | The template the job is building. It is meaningful once the job has created the template folder, and the  template can be opened with the room operations only after `isCompleted` turns true. | 
**progress** | **float** | How far the job has got. The value climbs while the contents of the room are being copied and reaches its  maximum at the very end, so it is an indication of life rather than a reliable estimate of the time left. | 
**error** | **str** | Why the job stopped. It is empty while the job runs and after a successful one; when it is filled the  half-built template has already been removed, so nothing has to be cleaned up by the caller. | [optional] 
**is_completed** | **bool** | Whether the job has ended. It is set both after a successful build and after a failure, so `error` is what  tells the two apart, and the record keeps answering with the same values until another job is started. | 

## Example

```python
from docspace_api_sdk.models.room_template_status_dto import RoomTemplateStatusDto

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


