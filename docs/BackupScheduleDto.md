# BackupScheduleDto
The request parameters for setting the backup schedule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_type** | [**BackupStorageType**](BackupStorageType.md) | The storage the scheduled archives are written to. It defaults to `Documents`, and it decides which  keys `storageParams` has to carry. | [optional] 
**storage_params** | [**List[ItemKeyValuePairObjectObject]**](ItemKeyValuePairObjectObject.md) | The settings of the chosen storage, as an array of key and value pairs. `Documents` and  `ThridpartyDocuments` need `folderId`, `Local` needs `filePath`, `ThirdPartyConsumer` needs `module`  plus the settings of that consumer, and `DataStore` needs none. | [optional] 
**backups_stored** | **int** | The number of scheduled copies to keep, from 1 to 30. It defaults to 1, and only the copies this  schedule creates are counted and removed - archives started by hand are left alone. | [optional] 
**cron_params** | [**Cron**](Cron.md) | When the backup runs. It is required: a request without it fails rather than falling back to a  default. | [optional] 
**dump** | **bool** | Schedules a backup of the whole server rather than of this one portal. It requires the space access  permission and works on a standalone installation only. | [optional] 

## Example

```python
from docspace_api_sdk.models.backup_schedule_dto import BackupScheduleDto

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


