# AiAiApproveToolCallRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **object** |  | 
**allow_always** | **bool** | Persist auto-approve for this tool's name. | [optional] 
**thread_id** | **str** | Thread the assistant message belongs to. | 
**message_id** | **str** | Storage id of the assistant message holding the tool call. | 
**idx** | **float** | Index of the tool-call content part inside `message.content`. | 
**message** | [**AiThreadMessageLike**](AiThreadMessageLike.md) | Snapshot of the assistant message at the time the tool call surfaced. | 
**action_args** | [**AiAiActionArgs**](AiAiActionArgs.md) |  | [optional] 
**entity_id** | **str** |  | [optional] 
**profile_id** | **str** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_ai_approve_tool_call_request import AiAiApproveToolCallRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiAiApproveToolCallRequest from a JSON string
ai_ai_approve_tool_call_request_instance = AiAiApproveToolCallRequest.from_json(json)
# print the JSON string representation of the object
print(AiAiApproveToolCallRequest.to_json())

# convert the object into a dict
ai_ai_approve_tool_call_request_dict = ai_ai_approve_tool_call_request_instance.to_dict()
# create an instance of AiAiApproveToolCallRequest from a dict
ai_ai_approve_tool_call_request_from_dict = AiAiApproveToolCallRequest.from_dict(ai_ai_approve_tool_call_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


