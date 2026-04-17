# ExportMessageRequestBody
Parameters for exporting an AI chat message to a document.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | [**ExportChatRequestBodyFolderId**](ExportChatRequestBodyFolderId.md) |  | 
**title** | **str** | The file name (without extension) to use for the exported document. | 

## Example

```python
from docspace_api_sdk.models.export_message_request_body import ExportMessageRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ExportMessageRequestBody from a JSON string
export_message_request_body_instance = ExportMessageRequestBody.from_json(json)
# print the JSON string representation of the object
print(ExportMessageRequestBody.to_json())

# convert the object into a dict
export_message_request_body_dict = export_message_request_body_instance.to_dict()
# create an instance of ExportMessageRequestBody from a dict
export_message_request_body_from_dict = ExportMessageRequestBody.from_dict(export_message_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


