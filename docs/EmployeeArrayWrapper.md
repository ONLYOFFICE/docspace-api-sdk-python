# EmployeeArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[EmployeeDto]**](EmployeeDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.employee_array_wrapper import EmployeeArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeArrayWrapper from a JSON string
employee_array_wrapper_instance = EmployeeArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(EmployeeArrayWrapper.to_json())

# convert the object into a dict
employee_array_wrapper_dict = employee_array_wrapper_instance.to_dict()
# create an instance of EmployeeArrayWrapper from a dict
employee_array_wrapper_from_dict = EmployeeArrayWrapper.from_dict(employee_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


