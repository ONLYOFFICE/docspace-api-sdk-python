# CustomerServiceUsageReportDto
One page of the per-service consumption totals, with the paging figures needed to walk the rest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | [**List[CustomerServiceUsageDto]**](CustomerServiceUsageDto.md) | The services on this page, one entry per service rather than per charge. It is empty for a period in  which nothing was consumed as well as for a page past the end of the report. | [optional] 
**offset** | **int** | How many entries were skipped before this page, echoed from the request. | [optional] 
**limit** | **int** | How many entries one page may hold, echoed from the request; it is 25 unless another value was asked for. | [optional] 
**total_quantity** | **int** | How many services match the filters in total, across every page - services, not charges. | [optional] 
**total_page** | **int** | How many pages those entries come to at the current `limit`. | [optional] 
**current_page** | **int** | Which of those pages this one is, as the billing service numbers them. Page through by advancing `offset`  rather than this value, which nothing accepts as an argument. | [optional] 

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


