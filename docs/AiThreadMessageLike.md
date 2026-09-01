# AiThreadMessageLike

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Storage-assigned message id (absent on inbound drafts). | [optional] 
**role** | **str** | Message author role. | 
**content** | [**AiThreadMessageLikeContent**](AiThreadMessageLikeContent.md) |  | 
**created_at** | **str** | Creation timestamp, ISO-8601 on the wire. | [optional] 
**status** | [**AiThreadMessageLikeStatus**](AiThreadMessageLikeStatus.md) |  | [optional] 
**metadata** | **object** | Arbitrary per-message metadata. | [optional] 
**attachments** | **List[object]** | Attachments linked to the message. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_thread_message_like import AiThreadMessageLike

# TODO update the JSON string below
json = "{}"
# create an instance of AiThreadMessageLike from a JSON string
ai_thread_message_like_instance = AiThreadMessageLike.from_json(json)
# print the JSON string representation of the object
print(AiThreadMessageLike.to_json())

# convert the object into a dict
ai_thread_message_like_dict = ai_thread_message_like_instance.to_dict()
# create an instance of AiThreadMessageLike from a dict
ai_thread_message_like_from_dict = AiThreadMessageLike.from_dict(ai_thread_message_like_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


