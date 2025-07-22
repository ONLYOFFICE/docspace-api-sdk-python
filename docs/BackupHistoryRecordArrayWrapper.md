# BackupHistoryRecordArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[BackupHistoryRecord]**](BackupHistoryRecord.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.backup_history_record_array_wrapper import BackupHistoryRecordArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of BackupHistoryRecordArrayWrapper from a JSON string
backup_history_record_array_wrapper_instance = BackupHistoryRecordArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(BackupHistoryRecordArrayWrapper.to_json())

# convert the object into a dict
backup_history_record_array_wrapper_dict = backup_history_record_array_wrapper_instance.to_dict()
# create an instance of BackupHistoryRecordArrayWrapper from a dict
backup_history_record_array_wrapper_from_dict = BackupHistoryRecordArrayWrapper.from_dict(backup_history_record_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


