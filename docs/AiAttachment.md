# AiAttachment
Persistent record for a single attachment (file or image) referenced from a user message. Files carry extracted text in `content`; images carry base64 data in `base64`. Metadata (`title`, `path`, `type`) is always present for display purposes regardless of whether the heavy payload is loaded.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Storage-assigned UUID. | 
**kind** | **str** | file | image. | 
**source** | **str** | Origin of the attachment. `user` — uploaded by the user in the composer (the default when unset, for backward compatibility). `tool` — produced by a tool call (e.g. `generate_image`). Lets the integrator's adapter route or apply policies (separate bucket, quotas, TTL, CDN) per source. | [optional] 
**title** | **str** | Display label (filename or user-visible title). | 
**content** | **str** | Extracted text for files. | [optional] 
**var_base64** | **str** | Base64 data URL for images. | [optional] 
**path** | **str** | Original host file path (for files). | [optional] 
**type** | **float** | ONLYOFFICE file type code (for files). | [optional] 
**message_id** | **str** | Owning message id once linked. Unset while the attachment is a draft. | [optional] 
**thread_id** | **str** | Owning thread id once linked. Unset while the attachment is a draft. | [optional] 
**entity_id** | **str** | Opaque scope token (entity / room) the attachment was created in. Drafts carry it so an entity switch keeps in-flight composer state isolated; once linked to a message the field is redundant with the thread's own entity binding. | [optional] 
**created_at** | **float** | Storage-assigned creation timestamp. | 
**can_analyze** | **bool** | Whether the attached form can be analyzed. | [optional] 
**form_keys** | [**List[AiAttachmentFormKeysInner]**](AiAttachmentFormKeysInner.md) | Keys of the fields inside the form. `key` is the field identifier, `text` its human-readable label. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_attachment import AiAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of AiAttachment from a JSON string
ai_attachment_instance = AiAttachment.from_json(json)
# print the JSON string representation of the object
print(AiAttachment.to_json())

# convert the object into a dict
ai_attachment_dict = ai_attachment_instance.to_dict()
# create an instance of AiAttachment from a dict
ai_attachment_from_dict = AiAttachment.from_dict(ai_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


