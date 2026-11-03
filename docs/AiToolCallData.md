# AiToolCallData
Identifies a pending tool call to resume — mirrors the library `ToolCallData` (its serializable fields).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread_id** | **str** | Thread the assistant message belongs to. | 
**message_id** | **str** | Storage id of the assistant message holding the tool call. | 
**idx** | **float** | Index of the tool-call content part inside `message.content`. | 
**message** | [**AiThreadMessageLike**](AiThreadMessageLike.md) | A copy of the assistant message as it was when the tool call surfaced. Optional and ignored: the round resumes from the stored message. Leave it out - a long conversation's copy can push the body past the size limit. | [optional] 
**action_args** | [**AiActionArgs**](AiActionArgs.md) | Per-request options of the round: extra tools, reasoning, a prompt override and the connected context. | [optional] 
**entity_id** | **str** | Optional entity (room) scope for profile resolution. | [optional] 
**context_entity_id** | **str** | The folder or room the user is in. Tools run against it and the model is told it is the user's location; falls back to `entityId` when omitted. | [optional] 
**profile_id** | **str** | Session-level profile override for this request only. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_tool_call_data import AiToolCallData

# TODO update the JSON string below
json = "{}"
# create an instance of AiToolCallData from a JSON string
ai_tool_call_data_instance = AiToolCallData.from_json(json)
# print the JSON string representation of the object
print(AiToolCallData.to_json())

# convert the object into a dict
ai_tool_call_data_dict = ai_tool_call_data_instance.to_dict()
# create an instance of AiToolCallData from a dict
ai_tool_call_data_from_dict = AiToolCallData.from_dict(ai_tool_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


