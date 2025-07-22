# EmployeeFullWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**EmployeeFullDto**](EmployeeFullDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.employee_full_wrapper import EmployeeFullWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeFullWrapper from a JSON string
employee_full_wrapper_instance = EmployeeFullWrapper.from_json(json)
# print the JSON string representation of the object
print(EmployeeFullWrapper.to_json())

# convert the object into a dict
employee_full_wrapper_dict = employee_full_wrapper_instance.to_dict()
# create an instance of EmployeeFullWrapper from a dict
employee_full_wrapper_from_dict = EmployeeFullWrapper.from_dict(employee_full_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


