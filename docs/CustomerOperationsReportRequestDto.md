# CustomerOperationsReportRequestDto
The request parameters for generating a report on client operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The report start date. | [optional] 
**end_date** | **datetime** | The report end date. | [optional] 
**participant_name** | **str** | The participant name. | [optional] 
**credit** | **bool** | Specifies whether to include credit operations in the report. | [optional] 
**debit** | **bool** | Specifies whether to include debit operations in the report. | [optional] 

## Example

```python
from docspace_api_sdk.models.customer_operations_report_request_dto import CustomerOperationsReportRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerOperationsReportRequestDto from a JSON string
customer_operations_report_request_dto_instance = CustomerOperationsReportRequestDto.from_json(json)
# print the JSON string representation of the object
print(CustomerOperationsReportRequestDto.to_json())

# convert the object into a dict
customer_operations_report_request_dto_dict = customer_operations_report_request_dto_instance.to_dict()
# create an instance of CustomerOperationsReportRequestDto from a dict
customer_operations_report_request_dto_from_dict = CustomerOperationsReportRequestDto.from_dict(customer_operations_report_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


