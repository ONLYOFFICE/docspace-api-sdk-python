# BackupScheduleDto

The backup schedule parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_type** | [**BackupStorageType**](BackupStorageType.md) |  | [optional] 
**storage_params** | [**List[ItemKeyValuePairObjectObject]**](ItemKeyValuePairObjectObject.md) | The backup storage parameters. | [optional] 
**backups_stored** | **int** | The maximum number of the stored backup copies. | [optional] 
**cron_params** | [**Cron**](Cron.md) |  | [optional] 
**dump** | **bool** | Specifies if a dump will be created or not. | [optional] 

## Example

```python
from docspace.models.backup_schedule_dto import BackupScheduleDto

# TODO update the JSON string below
json = "{}"
# create an instance of BackupScheduleDto from a JSON string
backup_schedule_dto_instance = BackupScheduleDto.from_json(json)
# print the JSON string representation of the object
print(BackupScheduleDto.to_json())

# convert the object into a dict
backup_schedule_dto_dict = backup_schedule_dto_instance.to_dict()
# create an instance of BackupScheduleDto from a dict
backup_schedule_dto_from_dict = BackupScheduleDto.from_dict(backup_schedule_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


