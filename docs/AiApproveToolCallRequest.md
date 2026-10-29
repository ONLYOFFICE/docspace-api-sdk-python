# AiApproveToolCallRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **object** |  | 
**allow_always** | **bool** | Persist auto-approve for this tool's name. | [optional] 
**thread_id** | **str** | Thread the assistant message belongs to. | 
**message_id** | **str** | Storage id of the assistant message holding the tool call. | 
**idx** | **float** | Index of the tool-call content part inside `message.content`. | 
**message** | [**AiThreadMessageLike**](AiThreadMessageLike.md) | Snapshot of the assistant message at the time the tool call surfaced. Optional and ignored: the engine resumes from the stored message, and the copy inflated the body past the parser limit (Bug 84608). | [optional] 
**action_args** | [**AiActionArgs**](AiActionArgs.md) | Per-request engine options: extra tools, reasoning, prompt override. | [optional] 
**entity_id** | **str** | Optional entity (room) scope for profile resolution. | [optional] 
**profile_id** | **str** | Session-level profile override for this request only. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_approve_tool_call_request import AiApproveToolCallRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiApproveToolCallRequest from a JSON string
ai_approve_tool_call_request_instance = AiApproveToolCallRequest.from_json(json)
# print the JSON string representation of the object
print(AiApproveToolCallRequest.to_json())

# convert the object into a dict
ai_approve_tool_call_request_dict = ai_approve_tool_call_request_instance.to_dict()
# create an instance of AiApproveToolCallRequest from a dict
ai_approve_tool_call_request_from_dict = AiApproveToolCallRequest.from_dict(ai_approve_tool_call_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


