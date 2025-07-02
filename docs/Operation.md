# Operation
Represents an operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Date of the operation. | [optional] 
**service** | **str** | Service related to the operation. | [optional] 
**description** | **str** | Brief description of the operation. | [optional] 
**service_unit** | **str** | Unit of the service. | [optional] 
**quantity** | **int** | Quantity of the service used. | [optional] 
**currency** | **str** | The three-character ISO 4217 currency symbol of the operation. | [optional] 
**credit** | **float** | Credit amount of the operation. | [optional] 
**withdrawal** | **float** | Withdrawal amount of the operation. | [optional] 

## Example

```python
from docspace-api-python.models.operation import Operation

# TODO update the JSON string below
json = "{}"
# create an instance of Operation from a JSON string
operation_instance = Operation.from_json(json)
# print the JSON string representation of the object
print(Operation.to_json())

# convert the object into a dict
operation_dict = operation_instance.to_dict()
# create an instance of Operation from a dict
operation_from_dict = Operation.from_dict(operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


