# ConvertSpreadsheetMarginsRequest
The margins of the output PDF file, each a length with its unit: mm, cm or in.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | The left margin of the output PDF file. | [optional] 
**right** | **str** | The right margin of the output PDF file. | [optional] 
**top** | **str** | The top margin of the output PDF file. | [optional] 
**bottom** | **str** | The bottom margin of the output PDF file. | [optional] 

## Example

```python
from docspace_api_sdk.models.convert_spreadsheet_margins_request import ConvertSpreadsheetMarginsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertSpreadsheetMarginsRequest from a JSON string
convert_spreadsheet_margins_request_instance = ConvertSpreadsheetMarginsRequest.from_json(json)
# print the JSON string representation of the object
print(ConvertSpreadsheetMarginsRequest.to_json())

# convert the object into a dict
convert_spreadsheet_margins_request_dict = convert_spreadsheet_margins_request_instance.to_dict()
# create an instance of ConvertSpreadsheetMarginsRequest from a dict
convert_spreadsheet_margins_request_from_dict = ConvertSpreadsheetMarginsRequest.from_dict(convert_spreadsheet_margins_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


