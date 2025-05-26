# BackupRestoreDto

The backup restoring parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_id** | **str** | The backup ID. | [optional] 
**storage_type** | [**BackupStorageType**](BackupStorageType.md) |  | [optional] 
**storage_params** | [**List[ItemKeyValuePairObjectObject]**](ItemKeyValuePairObjectObject.md) | The backup storage parameters. | [optional] 
**notify** | **bool** | Notifies users about the portal restoring process or not. | [optional] 
**dump** | **bool** | Specifies if a dump will be created or not. | [optional] 

## Example

```python
from docspace.models.backup_restore_dto import BackupRestoreDto

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


