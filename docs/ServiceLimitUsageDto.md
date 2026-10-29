# ServiceLimitUsageDto
What has been spent against a spending limit in its current period, and what is left.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_start** | **datetime** | The start of the current period, in UTC. | [optional] 
**period_end** | **datetime** | The end of the current period, in UTC: the moment the spending starts again from zero. Null for a lifetime  limit, which never resets. | [optional] 
**amount_consumed** | **float** | The money charged in the current period, in the currency of the limit. | [optional] 
**amount_available** | **float** | The money still available in the current period: the threshold less what was charged and what is reserved for  operations in progress, never below zero. Null when the limit has no money threshold. | [optional] 
**quantity_consumed** | **int** | The quantity consumed in the current period, in the unit of the limit. | [optional] 
**quantity_available** | **int** | The quantity still available in the current period, never below zero; null when the limit has no quantity  threshold. | [optional] 

## Example

```python
from docspace_api_sdk.models.service_limit_usage_dto import ServiceLimitUsageDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLimitUsageDto from a JSON string
service_limit_usage_dto_instance = ServiceLimitUsageDto.from_json(json)
# print the JSON string representation of the object
print(ServiceLimitUsageDto.to_json())

# convert the object into a dict
service_limit_usage_dto_dict = service_limit_usage_dto_instance.to_dict()
# create an instance of ServiceLimitUsageDto from a dict
service_limit_usage_dto_from_dict = ServiceLimitUsageDto.from_dict(service_limit_usage_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


