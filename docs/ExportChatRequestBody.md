# ExportChatRequestBody
Parameters for exporting an AI chat session to a document.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | [**ExportChatRequestBodyFolderId**](ExportChatRequestBodyFolderId.md) |  | 
**title** | **str** | The file name (without extension) to use for the exported document. | 

## Example

```python
from docspace_api_sdk.models.export_chat_request_body import ExportChatRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ExportChatRequestBody from a JSON string
export_chat_request_body_instance = ExportChatRequestBody.from_json(json)
# print the JSON string representation of the object
print(ExportChatRequestBody.to_json())

# convert the object into a dict
export_chat_request_body_dict = export_chat_request_body_instance.to_dict()
# create an instance of ExportChatRequestBody from a dict
export_chat_request_body_from_dict = ExportChatRequestBody.from_dict(export_chat_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


