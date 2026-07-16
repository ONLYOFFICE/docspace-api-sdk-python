# CustomerServiceUsageReportRequestDto
The request parameters for generating a customer service usage report.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_name** | **str** | The service name. | [optional] 
**start_date** | **datetime** | The report start date. | [optional] 
**end_date** | **datetime** | The report end date. | [optional] 
**participant_name** | **str** | The participant name. | [optional] 
**status** | [**OperationStatus**](OperationStatus.md) |  | [optional] 
**metadata** | **Dict[str, Optional[str]]** | Metadata key-value pairs to filter by. | [optional] 
**order_by** | **str** | The field to order by. | [optional] 
**order_type** | [**OperationOrderType**](OperationOrderType.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.customer_service_usage_report_request_dto import CustomerServiceUsageReportRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerServiceUsageReportRequestDto from a JSON string
customer_service_usage_report_request_dto_instance = CustomerServiceUsageReportRequestDto.from_json(json)
# print the JSON string representation of the object
print(CustomerServiceUsageReportRequestDto.to_json())

# convert the object into a dict
customer_service_usage_report_request_dto_dict = customer_service_usage_report_request_dto_instance.to_dict()
# create an instance of CustomerServiceUsageReportRequestDto from a dict
customer_service_usage_report_request_dto_from_dict = CustomerServiceUsageReportRequestDto.from_dict(customer_service_usage_report_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


