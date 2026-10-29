# DepositReportDto
One page of the portal wallet's top-ups, with the paging figures needed to walk the rest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | [**List[DepositDto]**](DepositDto.md) | The top-ups on this page. It is empty for a page past the end of the list as well as for a period in which  nothing was paid into the wallet. | [optional] 
**offset** | **int** | How many top-ups were skipped before this page, echoed from the request so a client need not remember what it  asked for. | [optional] 
**limit** | **int** | How many top-ups one page may hold, echoed from the request; it is 25 unless another value was asked for. A  full page is not proof that more exist - compare `currentPage` with `totalPage`. | [optional] 
**total_quantity** | **int** | How many top-ups match the filters in total, across every page. | [optional] 
**total_page** | **int** | How many pages those top-ups come to at the current `limit`. | [optional] 
**current_page** | **int** | Which of those pages this one is, as the billing service numbers them. Page through by advancing `offset`  rather than this value, which nothing accepts as an argument. | [optional] 

## Example

```python
from docspace_api_sdk.models.deposit_report_dto import DepositReportDto

# TODO update the JSON string below
json = "{}"
# create an instance of DepositReportDto from a JSON string
deposit_report_dto_instance = DepositReportDto.from_json(json)
# print the JSON string representation of the object
print(DepositReportDto.to_json())

# convert the object into a dict
deposit_report_dto_dict = deposit_report_dto_instance.to_dict()
# create an instance of DepositReportDto from a dict
deposit_report_dto_from_dict = DepositReportDto.from_dict(deposit_report_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


