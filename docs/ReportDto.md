# ReportDto
One page of the portal wallet's money movements, with the paging figures needed to walk the rest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | [**List[OperationDto]**](OperationDto.md) | The movements on this page - top-ups, charges, refunds and corrections alike, newest first. It is empty  for a page past the end of the report as well as for a period in which nothing happened. | [optional] 
**offset** | **int** | How many movements were skipped before this page, echoed from the request so a client need not remember  what it asked for. | [optional] 
**limit** | **int** | How many movements one page may hold, echoed from the request; it is 25 unless another value was asked  for. A full page is not proof that more exist - compare `currentPage` with `totalPage`. | [optional] 
**total_quantity** | **int** | How many movements match the filters in total, across every page. | [optional] 
**total_page** | **int** | How many pages those movements come to at the current `limit`. | [optional] 
**current_page** | **int** | Which of those pages this one is, as the billing service numbers them. Page through by advancing `offset`  rather than this value, which nothing accepts as an argument. | [optional] 

## Example

```python
from docspace_api_sdk.models.report_dto import ReportDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReportDto from a JSON string
report_dto_instance = ReportDto.from_json(json)
# print the JSON string representation of the object
print(ReportDto.to_json())

# convert the object into a dict
report_dto_dict = report_dto_instance.to_dict()
# create an instance of ReportDto from a dict
report_dto_from_dict = ReportDto.from_dict(report_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


