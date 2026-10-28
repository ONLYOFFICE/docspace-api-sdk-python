# EmployeeWrapper
The successful API response containing the EmployeeDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**EmployeeDto**](EmployeeDto.md) | The EmployeeDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.employee_wrapper import EmployeeWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeWrapper from a JSON string
employee_wrapper_instance = EmployeeWrapper.from_json(json)
# print the JSON string representation of the object
print(EmployeeWrapper.to_json())

# convert the object into a dict
employee_wrapper_dict = employee_wrapper_instance.to_dict()
# create an instance of EmployeeWrapper from a dict
employee_wrapper_from_dict = EmployeeWrapper.from_dict(employee_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


