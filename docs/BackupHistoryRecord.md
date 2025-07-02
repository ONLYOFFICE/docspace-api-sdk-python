# BackupHistoryRecord

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**storage_type** | [**BackupStorageType**](BackupStorageType.md) |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**expires_on** | **datetime** |  | [optional] 

## Example

```python
from docspace-api-python.models.backup_history_record import BackupHistoryRecord

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


