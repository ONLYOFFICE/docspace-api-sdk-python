# CreateBackupScheduleRequestDto
The request parameters for setting the backup schedule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_type** | [**BackupStorageType**](BackupStorageType.md) | The storage the scheduled archives are written to. It defaults to `Documents`, and it decides which  keys `storageParams` has to carry. | [optional] 
**storage_params** | [**List[ItemKeyValuePairObjectObject]**](ItemKeyValuePairObjectObject.md) | The settings of the chosen storage, as an array of key and value pairs. `Documents` and  `ThridpartyDocuments` need `folderId`, `Local` needs `filePath`, `ThirdPartyConsumer` needs `module`  plus the settings of that consumer, and `DataStore` needs none. | [optional] 
**backups_stored** | **int** | The number of scheduled copies to keep, from 1 to 30. It defaults to 1, and only the copies this  schedule creates are counted and removed - archives started by hand are left alone. | [optional] 
**cron_params** | [**BackupCronRequest**](BackupCronRequest.md) | When the backup runs. It is required: a request without it is rejected rather than falling back to  a default. | [optional] 
**dump** | **bool** | Schedules a backup of the whole server rather than of this one portal. It requires the space access  permission and works on a standalone installation only. | [optional] 

## Example

```python
from docspace_api_sdk.models.create_backup_schedule_request_dto import CreateBackupScheduleRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBackupScheduleRequestDto from a JSON string
create_backup_schedule_request_dto_instance = CreateBackupScheduleRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateBackupScheduleRequestDto.to_json())

# convert the object into a dict
create_backup_schedule_request_dto_dict = create_backup_schedule_request_dto_instance.to_dict()
# create an instance of CreateBackupScheduleRequestDto from a dict
create_backup_schedule_request_dto_from_dict = CreateBackupScheduleRequestDto.from_dict(create_backup_schedule_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


