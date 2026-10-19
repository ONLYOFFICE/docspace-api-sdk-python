# StartBackupRequestDto
The request parameters for starting a backup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_type** | [**BackupStorageType**](BackupStorageType.md) | The storage the archive is written to. It defaults to `Documents`, and it decides which keys  `storageParams` has to carry. | [optional] 
**storage_params** | [**List[ItemKeyValuePairObjectObject]**](ItemKeyValuePairObjectObject.md) | The settings of the chosen storage, as an array of key and value pairs. `Documents` needs an integer  `folderId`, `ThridpartyDocuments` a provider-specific non-integer `folderId`, `Local` a `filePath`,  `ThirdPartyConsumer` a `module` plus the settings of that consumer, and `DataStore` none. The  `subdir` key is added by the operation itself and must not be sent. | [optional] 
**dump** | **bool** | Backs up the whole server rather than this one portal. It requires the space access permission and  works on a standalone installation only. | [optional] 

## Example

```python
from docspace_api_sdk.models.start_backup_request_dto import StartBackupRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of StartBackupRequestDto from a JSON string
start_backup_request_dto_instance = StartBackupRequestDto.from_json(json)
# print the JSON string representation of the object
print(StartBackupRequestDto.to_json())

# convert the object into a dict
start_backup_request_dto_dict = start_backup_request_dto_instance.to_dict()
# create an instance of StartBackupRequestDto from a dict
start_backup_request_dto_from_dict = StartBackupRequestDto.from_dict(start_backup_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


