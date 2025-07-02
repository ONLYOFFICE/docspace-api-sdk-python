# ScheduleWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**Schedule**](Schedule.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.schedule_wrapper import ScheduleWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleWrapper from a JSON string
schedule_wrapper_instance = ScheduleWrapper.from_json(json)
# print the JSON string representation of the object
print(ScheduleWrapper.to_json())

# convert the object into a dict
schedule_wrapper_dict = schedule_wrapper_instance.to_dict()
# create an instance of ScheduleWrapper from a dict
schedule_wrapper_from_dict = ScheduleWrapper.from_dict(schedule_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


