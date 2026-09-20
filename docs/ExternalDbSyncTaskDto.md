# ExternalDbSyncTaskDto
The state of the job that exports the collected form data of a form filling room into the external database of the  portal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the job, which stays the same while a job for this room exists and is worth quoting when a  failure has to be traced in the portal logs. Polling is done by room, so the value is not needed to read the  state again. | 
**error** | **str** | The message of a failure that stopped the whole job. It is empty while the job is running and after a job that  ended without such a failure; a job that finished with individual forms rejected reports those in `forms` and  leaves this field empty. | [optional] 
**percentage** | **int** | How much of the work is done, from 0 to 100. It advances as the forms of the room are processed one by one, so  it is a usable progress indicator for a room with many forms and jumps straight to the end for a room with  one. | 
**is_completed** | **bool** | Whether the job has ended. It is set both for a job that finished its work and for one that stopped on an  error, so this is the flag to poll for, and `status` and `error` are what tell the two apart. | 
**status** | [**DistributedTaskStatus**](DistributedTaskStatus.md) | How the job ended, or how far it has got: queued, running, finished, cancelled or failed. It is the only field  that separates a successful end from a failed one once `isCompleted` is set. | 
**forms** | [**List[ExternalDbSyncFormResultDto]**](ExternalDbSyncFormResultDto.md) | The outcome for every original form of the room, one entry each. The list is empty while the job is running  and is filled in only when the job ends, so it is what to read after `isCompleted` turns true; it stays empty  for a room that holds no forms at all. | 

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


