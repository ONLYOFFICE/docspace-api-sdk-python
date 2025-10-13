# OperationDto
Represents an operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**service** | **str** | Service related to the operation. | [optional] 
**description** | **str** | Brief description of the operation. | [optional] 
**details** | **str** | Brief details of the operation. | [optional] 
**service_unit** | **str** | Unit of the service. | [optional] 
**quantity** | **int** | Quantity of the service used. | [optional] 
**currency** | **str** | The three-character ISO 4217 currency symbol of the operation. | [optional] 
**credit** | **float** | Credit amount of the operation. | [optional] 
**debit** | **float** | Debit amount of the operation. | [optional] 
**participant_name** | **str** | Original name of the participant. | [optional] 
**participant_display_name** | **str** | Display name of the participant. | [optional] 

## Example

```python
from docspace_api_sdk.models.operation_dto import OperationDto

# TODO update the JSON string below
json = "{}"
# create an instance of OperationDto from a JSON string
operation_dto_instance = OperationDto.from_json(json)
# print the JSON string representation of the object
print(OperationDto.to_json())

# convert the object into a dict
operation_dto_dict = operation_dto_instance.to_dict()
# create an instance of OperationDto from a dict
operation_dto_from_dict = OperationDto.from_dict(operation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


