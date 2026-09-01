# XlsxReportResponseDto
The XLSX report task response parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form** | [**FileDtoInteger**](FileDtoInteger.md) | The original form file information. | [optional] 
**task** | [**DocumentBuilderTaskDto**](DocumentBuilderTaskDto.md) | The Document Builder task information. | [optional] 
**is_new_file** | **bool** | Specifies whether the XLSX report file is newly created or an existing file will be updated. | [optional] 

## Example

```python
from docspace_api_sdk.models.xlsx_report_response_dto import XlsxReportResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of XlsxReportResponseDto from a JSON string
xlsx_report_response_dto_instance = XlsxReportResponseDto.from_json(json)
# print the JSON string representation of the object
print(XlsxReportResponseDto.to_json())

# convert the object into a dict
xlsx_report_response_dto_dict = xlsx_report_response_dto_instance.to_dict()
# create an instance of XlsxReportResponseDto from a dict
xlsx_report_response_dto_from_dict = XlsxReportResponseDto.from_dict(xlsx_report_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


