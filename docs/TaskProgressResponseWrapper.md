# TaskProgressResponseWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**TaskProgressResponseDto**](TaskProgressResponseDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.task_progress_response_wrapper import TaskProgressResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TaskProgressResponseWrapper from a JSON string
task_progress_response_wrapper_instance = TaskProgressResponseWrapper.from_json(json)
# print the JSON string representation of the object
print(TaskProgressResponseWrapper.to_json())

# convert the object into a dict
task_progress_response_wrapper_dict = task_progress_response_wrapper_instance.to_dict()
# create an instance of TaskProgressResponseWrapper from a dict
task_progress_response_wrapper_from_dict = TaskProgressResponseWrapper.from_dict(task_progress_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


