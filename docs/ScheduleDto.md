# ScheduleDto
The backup schedule parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_type** | [**BackupStorageType**](BackupStorageType.md) |  | 
**storage_params** | **Dict[str, Optional[str]]** | The backup storage parameters. | 
**cron_params** | [**CronParams**](CronParams.md) |  | 
**backups_stored** | **int** | The maximum number of the stored backup copies. | [optional] 
**last_backup_time** | **datetime** | The date and time when the last backup was reated. | 
**dump** | **bool** | Specifies if a dump will be created or not. | 

## Example

```python
from docspace_api_sdk.models.schedule_dto import ScheduleDto

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleDto from a JSON string
schedule_dto_instance = ScheduleDto.from_json(json)
# print the JSON string representation of the object
print(ScheduleDto.to_json())

# convert the object into a dict
schedule_dto_dict = schedule_dto_instance.to_dict()
# create an instance of ScheduleDto from a dict
schedule_dto_from_dict = ScheduleDto.from_dict(schedule_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


