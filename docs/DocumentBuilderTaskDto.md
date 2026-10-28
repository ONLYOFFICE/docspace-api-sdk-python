# DocumentBuilderTaskDto
The state of a background document building task: how far it has got, how it ended, and the file it produced.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the task. It is derived from the portal, the account and the kind of report, so starting the  same report again while it runs returns this same value, which is how a resumed poll is told from a newly  queued build. | 
**error** | **str** | The message of the failure that stopped the build. It is filled in only for a task that ended in the failed  state, and stays empty while the task runs and after it succeeds. | 
**percentage** | **int** | How far the build has got, from 0 to 100. It advances in a few coarse steps rather than smoothly, so it is a  progress hint and not a measure of the time left; wait on the completion flag instead. | 
**is_completed** | **bool** | True once the task has stopped for any reason, a failure and a cancellation included. It is the field to poll  on, and the status tells those outcomes apart. | 
**status** | [**DistributedTaskStatus**](DistributedTaskStatus.md) | How the task ended, or that it has not started yet. Read it together with the completion flag: a stopped task  can be a finished build, a cancelled one or a failure, and only this field separates them. | 
**result_file_id** | **object** |  | 
**result_file_name** | **str** | The name the produced file was saved with, extension included. The name is built from the subject of the  report and is not unique: a second build adds another file instead of replacing the first. | 
**result_file_url** | **str** | The address of the produced file in the document editor, relative to the portal root, so prefix it with the  portal address to open it. It stays empty until the build succeeds. | 

## Example

```python
from docspace_api_sdk.models.document_builder_task_dto import DocumentBuilderTaskDto

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentBuilderTaskDto from a JSON string
document_builder_task_dto_instance = DocumentBuilderTaskDto.from_json(json)
# print the JSON string representation of the object
print(DocumentBuilderTaskDto.to_json())

# convert the object into a dict
document_builder_task_dto_dict = document_builder_task_dto_instance.to_dict()
# create an instance of DocumentBuilderTaskDto from a dict
document_builder_task_dto_from_dict = DocumentBuilderTaskDto.from_dict(document_builder_task_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


