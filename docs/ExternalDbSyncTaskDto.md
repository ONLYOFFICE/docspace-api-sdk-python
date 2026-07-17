# ExternalDbSyncTaskDto
The external DB synchronization task parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The task ID. | 
**error** | **str** | The error message if the synchronization failed. | [optional] 
**percentage** | **int** | The progress percentage of the synchronization. | 
**is_completed** | **bool** | Specifies whether the synchronization is completed or not. | 
**status** | [**DistributedTaskStatus**](DistributedTaskStatus.md) |  | 
**forms** | [**List[ExternalDbSyncFormResultDto]**](ExternalDbSyncFormResultDto.md) | The synchronization results for all original forms in the room. | 

## Example

```python
from docspace_api_sdk.models.external_db_sync_task_dto import ExternalDbSyncTaskDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDbSyncTaskDto from a JSON string
external_db_sync_task_dto_instance = ExternalDbSyncTaskDto.from_json(json)
# print the JSON string representation of the object
print(ExternalDbSyncTaskDto.to_json())

# convert the object into a dict
external_db_sync_task_dto_dict = external_db_sync_task_dto_instance.to_dict()
# create an instance of ExternalDbSyncTaskDto from a dict
external_db_sync_task_dto_from_dict = ExternalDbSyncTaskDto.from_dict(external_db_sync_task_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


