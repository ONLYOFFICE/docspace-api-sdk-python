# BackupHistoryRecord

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**file_name** | **str** |  | 
**storage_type** | [**BackupStorageType**](BackupStorageType.md) |  | 
**created_on** | **datetime** |  | 
**expires_on** | **datetime** |  | 

## Example

```python
from docspace_api_sdk.models.backup_history_record import BackupHistoryRecord

# TODO update the JSON string below
json = "{}"
# create an instance of BackupHistoryRecord from a JSON string
backup_history_record_instance = BackupHistoryRecord.from_json(json)
# print the JSON string representation of the object
print(BackupHistoryRecord.to_json())

# convert the object into a dict
backup_history_record_dict = backup_history_record_instance.to_dict()
# create an instance of BackupHistoryRecord from a dict
backup_history_record_from_dict = BackupHistoryRecord.from_dict(backup_history_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


