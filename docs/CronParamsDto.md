# CronParamsDto
The time a scheduled backup runs at.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | [**BackupPeriod**](BackupPeriod.md) | How often the backup runs: 0 for every day, 1 for every week and 2 for every month. | [optional] 
**hour** | **int** | The hour of the day the backup starts at, from 0 to 23. | [optional] 
**day** | **int** | The day the backup runs on: the day of the week from 1 to 7, Sunday being 1, for a weekly schedule,  and the day of the month from 1 to 31 for a monthly one. It is 0 for a daily schedule. | [optional] 

## Example

```python
from docspace_api_sdk.models.cron_params_dto import CronParamsDto

# TODO update the JSON string below
json = "{}"
# create an instance of CronParamsDto from a JSON string
cron_params_dto_instance = CronParamsDto.from_json(json)
# print the JSON string representation of the object
print(CronParamsDto.to_json())

# convert the object into a dict
cron_params_dto_dict = cron_params_dto_instance.to_dict()
# create an instance of CronParamsDto from a dict
cron_params_dto_from_dict = CronParamsDto.from_dict(cron_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


