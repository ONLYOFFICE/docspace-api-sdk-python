# ConvertSpreadsheetLayoutRequest
How a spreadsheet converted to PDF is laid out on the page. A field left out takes the document service default.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ignore_print_area** | **bool** | Whether the print area chosen in the spreadsheet is ignored; false converts only that area. | [optional] 
**orientation** | **str** | The page orientation of the output PDF file: portrait or landscape. | [optional] 
**fit_to_height** | **int** | The number of pages the converted area is fitted into in height; 0 does not fit it. | [optional] 
**scale** | **int** | The scale of the output PDF file, in percent. | [optional] 
**fit_to_width** | **int** | The number of pages the converted area is fitted into in width; 0 does not fit it. | [optional] 
**headings** | **bool** | Whether the row and column headings are printed in the output PDF file. | [optional] 
**grid_lines** | **bool** | Whether the grid lines are printed in the output PDF file. | [optional] 
**margins** | [**ConvertSpreadsheetMarginsRequest**](ConvertSpreadsheetMarginsRequest.md) | The margins of the output PDF file. | [optional] 
**page_size** | [**ConvertSpreadsheetPageSizeRequest**](ConvertSpreadsheetPageSizeRequest.md) | The page size of the output PDF file. | [optional] 

## Example

```python
from docspace_api_sdk.models.convert_spreadsheet_layout_request import ConvertSpreadsheetLayoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertSpreadsheetLayoutRequest from a JSON string
convert_spreadsheet_layout_request_instance = ConvertSpreadsheetLayoutRequest.from_json(json)
# print the JSON string representation of the object
print(ConvertSpreadsheetLayoutRequest.to_json())

# convert the object into a dict
convert_spreadsheet_layout_request_dict = convert_spreadsheet_layout_request_instance.to_dict()
# create an instance of ConvertSpreadsheetLayoutRequest from a dict
convert_spreadsheet_layout_request_from_dict = ConvertSpreadsheetLayoutRequest.from_dict(convert_spreadsheet_layout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


