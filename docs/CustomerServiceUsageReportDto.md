# CustomerServiceUsageReportDto
Represents a paged report of customer service usage statistics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | [**List[CustomerServiceUsageDto]**](CustomerServiceUsageDto.md) | A collection of service usage statistics. | [optional] 
**offset** | **int** | The report data offset. | [optional] 
**limit** | **int** | The report data limit. | [optional] 
**total_quantity** | **int** | The total quantity of records in the report. | [optional] 
**total_page** | **int** | The total number of pages in the report. | [optional] 
**current_page** | **int** | The current page number of the report. | [optional] 

## Example

```python
from docspace_api_sdk.models.customer_service_usage_report_dto import CustomerServiceUsageReportDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerServiceUsageReportDto from a JSON string
customer_service_usage_report_dto_instance = CustomerServiceUsageReportDto.from_json(json)
# print the JSON string representation of the object
print(CustomerServiceUsageReportDto.to_json())

# convert the object into a dict
customer_service_usage_report_dto_dict = customer_service_usage_report_dto_instance.to_dict()
# create an instance of CustomerServiceUsageReportDto from a dict
customer_service_usage_report_dto_from_dict = CustomerServiceUsageReportDto.from_dict(customer_service_usage_report_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


