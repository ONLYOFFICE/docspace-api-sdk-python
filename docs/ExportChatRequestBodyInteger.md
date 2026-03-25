# ExportChatRequestBodyInteger
Parameters for exporting an AI chat session to a document.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | **int** | The identifier of the destination folder where the exported document will be saved. | 
**title** | **str** | The file name (without extension) to use for the exported document. | 

## Example

```python
from docspace_api_sdk.models.export_chat_request_body_integer import ExportChatRequestBodyInteger

# TODO update the JSON string below
json = "{}"
# create an instance of ExportChatRequestBodyInteger from a JSON string
export_chat_request_body_integer_instance = ExportChatRequestBodyInteger.from_json(json)
# print the JSON string representation of the object
print(ExportChatRequestBodyInteger.to_json())

# convert the object into a dict
export_chat_request_body_integer_dict = export_chat_request_body_integer_instance.to_dict()
# create an instance of ExportChatRequestBodyInteger from a dict
export_chat_request_body_integer_from_dict = ExportChatRequestBodyInteger.from_dict(export_chat_request_body_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


