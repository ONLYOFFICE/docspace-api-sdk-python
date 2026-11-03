# AiThreadMessageLikeStatus
Delivery/generation status of the message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | `running`, `requires-action`, `complete` or `incomplete`. | 
**reason** | **str** | Why the message is in that state: `tool-calls` or `interrupt` for `requires-action`; `stop` or `unknown` for `complete`; `cancelled`, `tool-calls`, `length`, `content-filter`, `other` or `error` for `incomplete`. An `incomplete` message the chat stored carries `cancelled` (the round was stopped) or `error`. | [optional] 
**error** | [**AiChatErrorPayload**](AiChatErrorPayload.md) | What failed, on an `incomplete` message whose `reason` is `error`. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_thread_message_like_status import AiThreadMessageLikeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AiThreadMessageLikeStatus from a JSON string
ai_thread_message_like_status_instance = AiThreadMessageLikeStatus.from_json(json)
# print the JSON string representation of the object
print(AiThreadMessageLikeStatus.to_json())

# convert the object into a dict
ai_thread_message_like_status_dict = ai_thread_message_like_status_instance.to_dict()
# create an instance of AiThreadMessageLikeStatus from a dict
ai_thread_message_like_status_from_dict = AiThreadMessageLikeStatus.from_dict(ai_thread_message_like_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


