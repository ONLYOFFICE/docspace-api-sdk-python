# ScheduleDto
The backup schedule of a portal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_type** | [**BackupStorageType**](BackupStorageType.md) | The storage the scheduled archives are written to, reported as a number rather than as the name the  schedule was created with. | 
**storage_params** | **Dict[str, Optional[str]]** | The settings of the storage, as an object keyed by parameter name - not as the array of key and value  pairs the schedule was created with, so it cannot be sent back unchanged. For every storage type  except `ThirdPartyConsumer` the `folderId` key is built from the stored base path. | 
**cron_params** | [**CronParams**](CronParams.md) | When the backup runs, read back from the stored cron expression. `day` is 0 for a daily schedule,  because a daily one has no day. | 
**backups_stored** | **int** | The number of scheduled copies kept. It is null, not 0, when the schedule keeps an unlimited number. | [optional] 
**last_backup_time** | **datetime** | The date and time the schedule last ran at. It is `0001-01-01T00:00:00` until the schedule has run  for the first time. | 
**dump** | **bool** | Specifies whether this schedule backs up the whole server instead of one portal. | 

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


