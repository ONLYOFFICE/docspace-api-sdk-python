# TaskProgressResponseDto
The task progress response parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The task progress ID. | 
**error** | **str** | The task progress error message. | [optional] 
**percentage** | **int** | The percentage of the task progress. | 
**is_completed** | **bool** | Specifies if the task peogress is completed or not. | 
**status** | [**DistributedTaskStatus**](DistributedTaskStatus.md) |  | 

## Example

```python
from docspace_api_sdk.models.task_progress_response_dto import TaskProgressResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of TaskProgressResponseDto from a JSON string
task_progress_response_dto_instance = TaskProgressResponseDto.from_json(json)
# print the JSON string representation of the object
print(TaskProgressResponseDto.to_json())

# convert the object into a dict
task_progress_response_dto_dict = task_progress_response_dto_instance.to_dict()
# create an instance of TaskProgressResponseDto from a dict
task_progress_response_dto_from_dict = TaskProgressResponseDto.from_dict(task_progress_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


