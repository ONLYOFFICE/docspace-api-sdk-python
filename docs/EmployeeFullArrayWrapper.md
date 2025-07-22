# EmployeeFullArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[EmployeeFullDto]**](EmployeeFullDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.employee_full_array_wrapper import EmployeeFullArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeFullArrayWrapper from a JSON string
employee_full_array_wrapper_instance = EmployeeFullArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(EmployeeFullArrayWrapper.to_json())

# convert the object into a dict
employee_full_array_wrapper_dict = employee_full_array_wrapper_instance.to_dict()
# create an instance of EmployeeFullArrayWrapper from a dict
employee_full_array_wrapper_from_dict = EmployeeFullArrayWrapper.from_dict(employee_full_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


