# Schedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_type** | [**BackupStorageType**](BackupStorageType.md) |  | [optional] 
**storage_params** | **Dict[str, Optional[str]]** |  | [optional] 
**cron_params** | [**CronParams**](CronParams.md) |  | [optional] 
**backups_stored** | **int** |  | [optional] 
**last_backup_time** | **datetime** |  | [optional] 
**dump** | **bool** |  | [optional] 

## Example

```python
from docspace.models.schedule import Schedule

# TODO update the JSON string below
json = "{}"
# create an instance of Schedule from a JSON string
schedule_instance = Schedule.from_json(json)
# print the JSON string representation of the object
print(Schedule.to_json())

# convert the object into a dict
schedule_dict = schedule_instance.to_dict()
# create an instance of Schedule from a dict
schedule_from_dict = Schedule.from_dict(schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


