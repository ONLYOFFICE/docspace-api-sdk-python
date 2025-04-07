# TaskProgressResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**error** | **str** | Error | [optional] 
**percentage** | **int** | Percentage | [optional] 
**is_completed** | **bool** | IsCompleted | [optional] 
**status** | [**DistributedTaskStatus**](DistributedTaskStatus.md) |  | [optional] 

## Example

```python
from docspace.models.task_progress_response_dto import TaskProgressResponseDto

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


