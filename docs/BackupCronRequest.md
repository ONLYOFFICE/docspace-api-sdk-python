# BackupCronRequest
The request parameters for the time the scheduled backup runs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | [**BackupPeriod**](BackupPeriod.md) | How often the backup runs: `EveryDay`, `EveryWeek` or `EveryMonth`. It defaults to `EveryDay`. | [optional] 
**hour** | **int** | The hour of the day the backup starts at, from 0 to 23. Minutes cannot be chosen - it always starts  on the hour. | [optional] 
**day** | **int** | The day the backup runs on: the day of the week from 1 to 7, Sunday being 1, for `EveryWeek`, and the  day of the month from 1 to 31 for `EveryMonth`. Leave it out for `EveryDay` only - a weekly or monthly  schedule sent without it is rejected. | [optional] 

## Example

```python
from docspace_api_sdk.models.backup_cron_request import BackupCronRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BackupCronRequest from a JSON string
backup_cron_request_instance = BackupCronRequest.from_json(json)
# print the JSON string representation of the object
print(BackupCronRequest.to_json())

# convert the object into a dict
backup_cron_request_dict = backup_cron_request_instance.to_dict()
# create an instance of BackupCronRequest from a dict
backup_cron_request_from_dict = BackupCronRequest.from_dict(backup_cron_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


