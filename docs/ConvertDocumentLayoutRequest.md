# ConvertDocumentLayoutRequest
The layout of forms printed as pdf documents or images.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draw_place_holders** | **bool** | Whether an empty form field shows its placeholder text in the result; false leaves it blank. | [optional] 
**draw_form_highlight** | **bool** | Whether form fields keep their highlight colour in the result; false draws them without it. | [optional] 
**is_print** | **bool** | Whether the print mode is turned on. It only applies to a docx converted into pdf: with the print mode off  the highlight flag does nothing and the placeholder flag saves the forms in the pdf. | [optional] 

## Example

```python
from docspace_api_sdk.models.convert_document_layout_request import ConvertDocumentLayoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertDocumentLayoutRequest from a JSON string
convert_document_layout_request_instance = ConvertDocumentLayoutRequest.from_json(json)
# print the JSON string representation of the object
print(ConvertDocumentLayoutRequest.to_json())

# convert the object into a dict
convert_document_layout_request_dict = convert_document_layout_request_instance.to_dict()
# create an instance of ConvertDocumentLayoutRequest from a dict
convert_document_layout_request_from_dict = ConvertDocumentLayoutRequest.from_dict(convert_document_layout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


