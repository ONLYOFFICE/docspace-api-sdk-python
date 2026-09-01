# AiAiToolCallData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread_id** | **str** | Thread the assistant message belongs to. | 
**message_id** | **str** | Storage id of the assistant message holding the tool call. | 
**idx** | **float** | Index of the tool-call content part inside `message.content`. | 
**message** | [**AiThreadMessageLike**](AiThreadMessageLike.md) | Snapshot of the assistant message at the time the tool call surfaced. | 
**action_args** | [**AiAiActionArgs**](AiAiActionArgs.md) |  | [optional] 
**entity_id** | **str** |  | [optional] 
**profile_id** | **str** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_ai_tool_call_data import AiAiToolCallData

# TODO update the JSON string below
json = "{}"
# create an instance of AiAiToolCallData from a JSON string
ai_ai_tool_call_data_instance = AiAiToolCallData.from_json(json)
# print the JSON string representation of the object
print(AiAiToolCallData.to_json())

# convert the object into a dict
ai_ai_tool_call_data_dict = ai_ai_tool_call_data_instance.to_dict()
# create an instance of AiAiToolCallData from a dict
ai_ai_tool_call_data_from_dict = AiAiToolCallData.from_dict(ai_ai_tool_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


