# AiAttachmentsSaveFilesManyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | [**List[AiAttachmentsSaveFileRequestInput]**](AiAttachmentsSaveFileRequestInput.md) |  | 
**entity_id** | **str** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_attachments_save_files_many_request import AiAttachmentsSaveFilesManyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiAttachmentsSaveFilesManyRequest from a JSON string
ai_attachments_save_files_many_request_instance = AiAttachmentsSaveFilesManyRequest.from_json(json)
# print the JSON string representation of the object
print(AiAttachmentsSaveFilesManyRequest.to_json())

# convert the object into a dict
ai_attachments_save_files_many_request_dict = ai_attachments_save_files_many_request_instance.to_dict()
# create an instance of AiAttachmentsSaveFilesManyRequest from a dict
ai_attachments_save_files_many_request_from_dict = AiAttachmentsSaveFilesManyRequest.from_dict(ai_attachments_save_files_many_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


