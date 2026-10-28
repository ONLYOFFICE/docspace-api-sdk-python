# ConvertPdfRequest
The settings of a PDF result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form** | **bool** | Whether the result is a fillable PDF form: true keeps the form fields of the source as fields to fill in,  false saves a plain PDF. | [optional] 

## Example

```python
from docspace_api_sdk.models.convert_pdf_request import ConvertPdfRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertPdfRequest from a JSON string
convert_pdf_request_instance = ConvertPdfRequest.from_json(json)
# print the JSON string representation of the object
print(ConvertPdfRequest.to_json())

# convert the object into a dict
convert_pdf_request_dict = convert_pdf_request_instance.to_dict()
# create an instance of ConvertPdfRequest from a dict
convert_pdf_request_from_dict = ConvertPdfRequest.from_dict(convert_pdf_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


