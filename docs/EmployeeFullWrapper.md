# EmployeeFullWrapper
The successful API response containing the EmployeeFullDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**EmployeeFullDto**](EmployeeFullDto.md) | The EmployeeFullDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.employee_full_wrapper import EmployeeFullWrapper

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


