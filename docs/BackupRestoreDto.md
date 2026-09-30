# BackupRestoreDto
The request parameters for restoring a portal from a backup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_id** | **str** | The ID of the backup to restore from, as listed by `GET api/2.0/backup/getbackuphistory`. Send  anything that is not a GUID to restore from a file given by `storageParams` instead; an all-zero GUID  selects neither, because it parses as a GUID and then matches no record. | 
**storage_type** | [**BackupStorageType**](BackupStorageType.md) | The storage the archive is read from. It defaults to `Documents` and is only used when `backupId` is  not a GUID, because a known backup carries the storage of its own record. | [optional] 
**storage_params** | [**List[ItemKeyValuePairObjectObject]**](ItemKeyValuePairObjectObject.md) | The location of the archive, as an array of key and value pairs. The key read here is `filePath` -  not the `folderId` a backup is started with - and it holds a file ID for `Documents`, a  provider-specific file ID for `ThridpartyDocuments` and a path on the server for `Local`. It is only  used when `backupId` is not a GUID. | [optional] 
**notify** | **bool** | Chooses who is emailed when the restoring starts and when it finishes: every active user of the  portal when true, and its owner alone when false. Mail goes only to accounts that have been  activated, so this decides the audience rather than whether anybody is notified at all. | [optional] 
**dump** | **bool** | Restores the whole server rather than this one portal. It requires the space access permission. | [optional] 

## Example

```python
from docspace_api_sdk.models.backup_restore_dto import BackupRestoreDto

# TODO update the JSON string below
json = "{}"
# create an instance of BackupRestoreDto from a JSON string
backup_restore_dto_instance = BackupRestoreDto.from_json(json)
# print the JSON string representation of the object
print(BackupRestoreDto.to_json())

# convert the object into a dict
backup_restore_dto_dict = backup_restore_dto_instance.to_dict()
# create an instance of BackupRestoreDto from a dict
backup_restore_dto_from_dict = BackupRestoreDto.from_dict(backup_restore_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


