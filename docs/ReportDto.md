# ReportDto
Represents a report containing a collection of operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | [**List[OperationDto]**](OperationDto.md) | A collection of operations. | [optional] 
**offset** | **int** | The report data offset. | [optional] 
**limit** | **int** | The report data limit. | [optional] 
**total_quantity** | **int** | The total quantity of operations in the report. | [optional] 
**total_page** | **int** | The total number of pages in the report. | [optional] 
**current_page** | **int** | The current page number of the report. | [optional] 

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


