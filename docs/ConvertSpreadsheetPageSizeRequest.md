# ConvertSpreadsheetPageSizeRequest
The page size of the output PDF file, each side a length with its unit: mm, cm or in.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **str** | The page height of the output PDF file. | [optional] 
**width** | **str** | The page width of the output PDF file. | [optional] 

## Example

```python
from docspace_api_sdk.models.convert_spreadsheet_page_size_request import ConvertSpreadsheetPageSizeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertSpreadsheetPageSizeRequest from a JSON string
convert_spreadsheet_page_size_request_instance = ConvertSpreadsheetPageSizeRequest.from_json(json)
# print the JSON string representation of the object
print(ConvertSpreadsheetPageSizeRequest.to_json())

# convert the object into a dict
convert_spreadsheet_page_size_request_dict = convert_spreadsheet_page_size_request_instance.to_dict()
# create an instance of ConvertSpreadsheetPageSizeRequest from a dict
convert_spreadsheet_page_size_request_from_dict = ConvertSpreadsheetPageSizeRequest.from_dict(convert_spreadsheet_page_size_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


