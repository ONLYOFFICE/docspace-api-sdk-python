# ExportChatRequestBodyFolderId
The identifier of the destination folder where the exported document will be saved.  Can be an integer for internal folders or a string for third-party storage folders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from docspace_api_sdk.models.export_chat_request_body_folder_id import ExportChatRequestBodyFolderId

# TODO update the JSON string below
json = "{}"
# create an instance of ExportChatRequestBodyFolderId from a JSON string
export_chat_request_body_folder_id_instance = ExportChatRequestBodyFolderId.from_json(json)
# print the JSON string representation of the object
print(ExportChatRequestBodyFolderId.to_json())

# convert the object into a dict
export_chat_request_body_folder_id_dict = export_chat_request_body_folder_id_instance.to_dict()
# create an instance of ExportChatRequestBodyFolderId from a dict
export_chat_request_body_folder_id_from_dict = ExportChatRequestBodyFolderId.from_dict(export_chat_request_body_folder_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


