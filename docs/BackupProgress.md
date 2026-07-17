# BackupProgress
The backup progress parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_completed** | **bool** | Specifies if the backup is completed or not. | [optional] 
**progress** | **int** | The backup progress in percentage. | [optional] 
**error** | **str** | The backup error message. | [optional] 
**warning** | **str** | The backup warning message. | [optional] 
**link** | **str** | The backup link. | [optional] 
**tenant_id** | **int** | The tenant ID. | [optional] 
**backup_progress_enum** | [**BackupProgressEnum**](BackupProgressEnum.md) |  | [optional] 
**status** | [**DistributedTaskStatus**](DistributedTaskStatus.md) |  | [optional] 
**task_id** | **str** | The task ID. | [optional] 

## Example

```python
from docspace_api_sdk.models.backup_progress import BackupProgress

# TODO update the JSON string below
json = "{}"
# create an instance of BackupProgress from a JSON string
backup_progress_instance = BackupProgress.from_json(json)
# print the JSON string representation of the object
print(BackupProgress.to_json())

# convert the object into a dict
backup_progress_dict = backup_progress_instance.to_dict()
# create an instance of BackupProgress from a dict
backup_progress_from_dict = BackupProgress.from_dict(backup_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


