# AiAiSendStreamBody
Shared body of the two streaming send endpoints (`sendWithStream` and its OpenAI-framed twin) — the `Chat` action is implied, so there is no `actionType`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread_id** | **str** | Target thread; a new one is created (with an auto title) when omitted. | [optional] 
**user_message** | [**AiThreadMessageLike**](AiThreadMessageLike.md) | The user turn to send. | 
**action_args** | [**AiAiActionArgs**](AiAiActionArgs.md) | Per-request engine options: extra tools, reasoning, prompt override. | [optional] 
**entity_id** | **str** | Optional entity (room) scope for profile resolution. | [optional] 
**profile_id** | **str** | Session-level profile override for this request only. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_ai_send_stream_body import AiAiSendStreamBody

# TODO update the JSON string below
json = "{}"
# create an instance of AiAiSendStreamBody from a JSON string
ai_ai_send_stream_body_instance = AiAiSendStreamBody.from_json(json)
# print the JSON string representation of the object
print(AiAiSendStreamBody.to_json())

# convert the object into a dict
ai_ai_send_stream_body_dict = ai_ai_send_stream_body_instance.to_dict()
# create an instance of AiAiSendStreamBody from a dict
ai_ai_send_stream_body_from_dict = AiAiSendStreamBody.from_dict(ai_ai_send_stream_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


