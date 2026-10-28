# AiAttachmentsSaveFileRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | [**AiAttachmentsSaveFileRequestInput**](AiAttachmentsSaveFileRequestInput.md) |  | 
**entity_id** | **str** | Optional entity (room) scope. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_attachments_save_file_request import AiAttachmentsSaveFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiAttachmentsSaveFileRequest from a JSON string
ai_attachments_save_file_request_instance = AiAttachmentsSaveFileRequest.from_json(json)
# print the JSON string representation of the object
print(AiAttachmentsSaveFileRequest.to_json())

# convert the object into a dict
ai_attachments_save_file_request_dict = ai_attachments_save_file_request_instance.to_dict()
# create an instance of AiAttachmentsSaveFileRequest from a dict
ai_attachments_save_file_request_from_dict = AiAttachmentsSaveFileRequest.from_dict(ai_attachments_save_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


