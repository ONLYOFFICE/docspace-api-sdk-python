# TimeBound
Represents the period the price is effective in.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The date and time when the period starts. | [optional] 
**end_date** | **datetime** | The date and time when the period ends. | [optional] 

## Example

```python
from docspace_api_sdk.models.time_bound import TimeBound

# TODO update the JSON string below
json = "{}"
# create an instance of TimeBound from a JSON string
time_bound_instance = TimeBound.from_json(json)
# print the JSON string representation of the object
print(TimeBound.to_json())

# convert the object into a dict
time_bound_dict = time_bound_instance.to_dict()
# create an instance of TimeBound from a dict
time_bound_from_dict = TimeBound.from_dict(time_bound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


