# AiAttachmentsSaveFileRequestInput
A file attachment draft to persist.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Storage path/key of the file. | 
**content** | **str** | File contents. | 
**type** | **float** | File type discriminator. | 
**title** | **str** | Optional display title. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_attachments_save_file_request_input import AiAttachmentsSaveFileRequestInput

# TODO update the JSON string below
json = "{}"
# create an instance of AiAttachmentsSaveFileRequestInput from a JSON string
ai_attachments_save_file_request_input_instance = AiAttachmentsSaveFileRequestInput.from_json(json)
# print the JSON string representation of the object
print(AiAttachmentsSaveFileRequestInput.to_json())

# convert the object into a dict
ai_attachments_save_file_request_input_dict = ai_attachments_save_file_request_input_instance.to_dict()
# create an instance of AiAttachmentsSaveFileRequestInput from a dict
ai_attachments_save_file_request_input_from_dict = AiAttachmentsSaveFileRequestInput.from_dict(ai_attachments_save_file_request_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


