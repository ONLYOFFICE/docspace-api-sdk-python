# CustomerOperationsReportDto

Parameters of the request for generating the report on client operations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Start date | [optional] 
**end_date** | **datetime** | End date | [optional] 
**credit** | **bool** | Include credit operations | [optional] 
**withdrawal** | **bool** | Include withdrawal operations | [optional] 

## Example

```python
from docspace.models.customer_operations_report_dto import CustomerOperationsReportDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerOperationsReportDto from a JSON string
customer_operations_report_dto_instance = CustomerOperationsReportDto.from_json(json)
# print the JSON string representation of the object
print(CustomerOperationsReportDto.to_json())

# convert the object into a dict
customer_operations_report_dto_dict = customer_operations_report_dto_instance.to_dict()
# create an instance of CustomerOperationsReportDto from a dict
customer_operations_report_dto_from_dict = CustomerOperationsReportDto.from_dict(customer_operations_report_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


