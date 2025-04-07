# BackupProgress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_completed** | **bool** |  | [optional] 
**progress** | **int** |  | [optional] 
**error** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**tenant_id** | **int** |  | [optional] 
**backup_progress_enum** | [**BackupProgressEnum**](BackupProgressEnum.md) |  | [optional] 
**task_id** | **str** |  | [optional] 

## Example

```python
from docspace.models.backup_progress import BackupProgress

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


