# ScheduleWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ScheduleDto**](ScheduleDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.schedule_wrapper import ScheduleWrapper

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


