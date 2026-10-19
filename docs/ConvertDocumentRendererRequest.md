# ConvertDocumentRendererRequest
How the text of a pdf, xps or oxps source is read back when converting from it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text_association** | **str** | The rendering mode: blockChar reads the text by single characters, blockLine by separate lines, plainLine as  plain text with a paragraph per line, plainParagraph as plain text with lines combined into paragraphs. | [optional] 

## Example

```python
from docspace_api_sdk.models.convert_document_renderer_request import ConvertDocumentRendererRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertDocumentRendererRequest from a JSON string
convert_document_renderer_request_instance = ConvertDocumentRendererRequest.from_json(json)
# print the JSON string representation of the object
print(ConvertDocumentRendererRequest.to_json())

# convert the object into a dict
convert_document_renderer_request_dict = convert_document_renderer_request_instance.to_dict()
# create an instance of ConvertDocumentRendererRequest from a dict
convert_document_renderer_request_from_dict = ConvertDocumentRendererRequest.from_dict(convert_document_renderer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


