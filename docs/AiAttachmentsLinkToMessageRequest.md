# AiAttachmentsLinkToMessageRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | Attachment ids to bind. | 
**message_id** | **str** | Owning message id. | 
**thread_id** | **str** | Owning thread id. | 

## Example

```python
from docspace_api_sdk.models.ai_attachments_link_to_message_request import AiAttachmentsLinkToMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiAttachmentsLinkToMessageRequest from a JSON string
ai_attachments_link_to_message_request_instance = AiAttachmentsLinkToMessageRequest.from_json(json)
# print the JSON string representation of the object
print(AiAttachmentsLinkToMessageRequest.to_json())

# convert the object into a dict
ai_attachments_link_to_message_request_dict = ai_attachments_link_to_message_request_instance.to_dict()
# create an instance of AiAttachmentsLinkToMessageRequest from a dict
ai_attachments_link_to_message_request_from_dict = AiAttachmentsLinkToMessageRequest.from_dict(ai_attachments_link_to_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


