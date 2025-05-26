# PerformCustomerOperationRequestDto

Parameters for performing a customer operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_account** | **int** | Service account | [optional] 
**session_id** | **int** | Session ID | [optional] 
**quantity** | **int** | Quantity | [optional] 

## Example

```python
from docspace.models.perform_customer_operation_request_dto import PerformCustomerOperationRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of PerformCustomerOperationRequestDto from a JSON string
perform_customer_operation_request_dto_instance = PerformCustomerOperationRequestDto.from_json(json)
# print the JSON string representation of the object
print(PerformCustomerOperationRequestDto.to_json())

# convert the object into a dict
perform_customer_operation_request_dto_dict = perform_customer_operation_request_dto_instance.to_dict()
# create an instance of PerformCustomerOperationRequestDto from a dict
perform_customer_operation_request_dto_from_dict = PerformCustomerOperationRequestDto.from_dict(perform_customer_operation_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


