# TaskProgressResponseDto
The task progress response parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the queued job. It identifies this run of the job and changes every time the job is started again. | 
**error** | **str** | The message of the error that stopped the job. It is empty while the job is running and after a job that  succeeded, and it is the only place where the reason for a failure is reported. | [optional] 
**percentage** | **int** | The share of the job that is already done, from 0 to 100. | 
**is_completed** | **bool** | Specifies whether the job has stopped running. This is the field to poll: true means the job will not change  any more, whether it succeeded, failed or was cancelled, and `status` tells which of the three it is. | 
**status** | [**DistributedTaskStatus**](DistributedTaskStatus.md) | The state of the job: `Created` while it waits in the queue, `Running` while it works, `Completed` once it has  finished on its own, `Canceled` after a terminate operation, and `Failted` when it stopped on an error, in  which case `error` carries the reason. | 

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


