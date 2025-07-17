# ReportDto
Represents a report containing a collection of operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | [**List[OperationDto]**](OperationDto.md) | Collection of operations. | [optional] 
**offset** | **int** | Offset of the report data. | [optional] 
**limit** | **int** | Limit of the report data. | [optional] 
**total_quantity** | **int** | Total quantity of operations in the report. | [optional] 
**total_page** | **int** | Total number of pages in the report. | [optional] 
**current_page** | **int** | Current page number of the report. | [optional] 

## Example

```python
from docspace-api-python.models.report_dto import ReportDto

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


