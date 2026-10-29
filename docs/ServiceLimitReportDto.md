# ServiceLimitReportDto
A page of the spending limits in force for the portal users.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | [**List[ServiceLimitDto]**](ServiceLimitDto.md) | The limits of this page, one per user; empty when no limit applies to any user or the page is past the end. | [optional] 
**offset** | **int** | The number of limits skipped before this page. | [optional] 
**limit** | **int** | The page size the page was read with. | [optional] 
**total_page** | **int** | The number of pages the whole list takes at this page size. | [optional] 
**current_page** | **int** | The number of this page, starting from 1. | [optional] 
**total_quantity** | **int** | The number of users with a limit in force across all pages. | [optional] 

## Example

```python
from docspace_api_sdk.models.service_limit_report_dto import ServiceLimitReportDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLimitReportDto from a JSON string
service_limit_report_dto_instance = ServiceLimitReportDto.from_json(json)
# print the JSON string representation of the object
print(ServiceLimitReportDto.to_json())

# convert the object into a dict
service_limit_report_dto_dict = service_limit_report_dto_instance.to_dict()
# create an instance of ServiceLimitReportDto from a dict
service_limit_report_dto_from_dict = ServiceLimitReportDto.from_dict(service_limit_report_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


