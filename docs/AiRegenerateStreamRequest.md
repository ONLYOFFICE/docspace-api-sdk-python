# AiRegenerateStreamRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread_id** | **str** | Target thread (must already exist). | 
**message_id** | **str** | The user message to re-roll from: everything stored after it is deleted. When omitted, or no longer in the thread, the last user message is used. | [optional] 
**keep_count** | **int** | How many messages from the start of the thread to keep, used when `messageId` does not resolve. The message at `keepCount - 1` has to be a user message; otherwise the value is ignored. | [optional] 
**expected_length** | **int** | The thread length the caller saw when it computed `keepCount`. When it differs from the stored length, `keepCount` is discarded and the last user message is used instead. | [optional] 
**action_args** | [**AiActionArgs**](AiActionArgs.md) | Per-request options of the round: extra tools, reasoning, a prompt override and the connected context. | [optional] 
**entity_id** | **str** | Optional entity (room) scope for profile resolution. | [optional] 
**context_entity_id** | **str** | The folder or room the user is in. Tools run against it and the model is told it is the user's location; falls back to `entityId` when omitted. | [optional] 
**profile_id** | **str** | Session-level profile override for this request only. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_regenerate_stream_request import AiRegenerateStreamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiRegenerateStreamRequest from a JSON string
ai_regenerate_stream_request_instance = AiRegenerateStreamRequest.from_json(json)
# print the JSON string representation of the object
print(AiRegenerateStreamRequest.to_json())

# convert the object into a dict
ai_regenerate_stream_request_dict = ai_regenerate_stream_request_instance.to_dict()
# create an instance of AiRegenerateStreamRequest from a dict
ai_regenerate_stream_request_from_dict = AiRegenerateStreamRequest.from_dict(ai_regenerate_stream_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


