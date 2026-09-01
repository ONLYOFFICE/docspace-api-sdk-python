# AiExportTextToDocxRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Document title (also the file name). | 
**content** | **str** | Markdown content to convert. | 
**folder_id** | [**AiExportTextToDocxRequestFolderId**](AiExportTextToDocxRequestFolderId.md) |  | 

## Example

```python
from docspace_api_sdk.models.ai_export_text_to_docx_request import AiExportTextToDocxRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiExportTextToDocxRequest from a JSON string
ai_export_text_to_docx_request_instance = AiExportTextToDocxRequest.from_json(json)
# print the JSON string representation of the object
print(AiExportTextToDocxRequest.to_json())

# convert the object into a dict
ai_export_text_to_docx_request_dict = ai_export_text_to_docx_request_instance.to_dict()
# create an instance of AiExportTextToDocxRequest from a dict
ai_export_text_to_docx_request_from_dict = AiExportTextToDocxRequest.from_dict(ai_export_text_to_docx_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


