# TimeBoundDto
Represents the period the price is effective in.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The date and time when the period starts. | [optional] 
**end_date** | **datetime** | The date and time when the period ends. | [optional] 

## Example

```python
from docspace_api_sdk.models.time_bound_dto import TimeBoundDto

# TODO update the JSON string below
json = "{}"
# create an instance of TimeBoundDto from a JSON string
time_bound_dto_instance = TimeBoundDto.from_json(json)
# print the JSON string representation of the object
print(TimeBoundDto.to_json())

# convert the object into a dict
time_bound_dto_dict = time_bound_dto_instance.to_dict()
# create an instance of TimeBoundDto from a dict
time_bound_dto_from_dict = TimeBoundDto.from_dict(time_bound_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


