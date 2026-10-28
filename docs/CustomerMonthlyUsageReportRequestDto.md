# CustomerMonthlyUsageReportRequestDto
The period covered by the monthly wallet spending report.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The beginning of the reported period, inclusive. The months are cut in the portal time zone rather than in  UTC, so spending at the turn of a month falls where the portal sees it; defaults to the portal creation date. | [optional] 
**end_date** | **datetime** | The end of the reported period, inclusive. Cut in the portal time zone in the same way as `startDate`, and  defaults to the moment the call is made. | [optional] 

## Example

```python
from docspace_api_sdk.models.customer_monthly_usage_report_request_dto import CustomerMonthlyUsageReportRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerMonthlyUsageReportRequestDto from a JSON string
customer_monthly_usage_report_request_dto_instance = CustomerMonthlyUsageReportRequestDto.from_json(json)
# print the JSON string representation of the object
print(CustomerMonthlyUsageReportRequestDto.to_json())

# convert the object into a dict
customer_monthly_usage_report_request_dto_dict = customer_monthly_usage_report_request_dto_instance.to_dict()
# create an instance of CustomerMonthlyUsageReportRequestDto from a dict
customer_monthly_usage_report_request_dto_from_dict = CustomerMonthlyUsageReportRequestDto.from_dict(customer_monthly_usage_report_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


