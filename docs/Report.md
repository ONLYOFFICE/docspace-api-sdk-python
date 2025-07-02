# Report
Represents a report containing a collection of operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | [**List[Operation]**](Operation.md) | Collection of operations. | [optional] 
**offset** | **int** | Offset of the report data. | [optional] 
**limit** | **int** | Limit of the report data. | [optional] 
**total_quantity** | **int** | Total quantity of operations in the report. | [optional] 
**total_page** | **int** | Total number of pages in the report. | [optional] 
**current_page** | **int** | Current page number of the report. | [optional] 

## Example

```python
from docspace-api-python.models.report import Report

# TODO update the JSON string below
json = "{}"
# create an instance of Report from a JSON string
report_instance = Report.from_json(json)
# print the JSON string representation of the object
print(Report.to_json())

# convert the object into a dict
report_dict = report_instance.to_dict()
# create an instance of Report from a dict
report_from_dict = Report.from_dict(report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


