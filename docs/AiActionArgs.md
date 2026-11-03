# AiActionArgs
Per-request options of an AI round: extra tools, the depth of reasoning, a system prompt override and the rooms and folder connected as context.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tools** | [**List[AiMCPItem]**](AiMCPItem.md) | Extra tools offered to the model for this request. | [optional] 
**is_reasoning** | **bool** | Legacy extended-thinking switch; stands for `medium`. `reasoningLevel` wins when both are set. | [optional] 
**reasoning_level** | [**AiReasoningLevel**](AiReasoningLevel.md) | Depth of extended thinking for the round; providers clamp it to what the model accepts. | [optional] 
**prompt** | [**AiActionArgsPrompt**](AiActionArgsPrompt.md) |  | [optional] 
**tool_instructions** | **Dict[str, str]** | Usage notes of the MCP servers the caller holds the connection to, keyed by server type; folded into the system prompt as advisory text. | [optional] 
**context_rooms** | [**List[AiContextRoomRef]**](AiContextRoomRef.md) | Instructions rooms connected to the chat as context, each with the skills the round may use. | [optional] 
**knowledge_rooms** | [**List[AiKnowledgeRoomRef]**](AiKnowledgeRoomRef.md) | Knowledge rooms connected to the chat; the knowledge search tool of the round is limited to them. Each `id` has to be a DocSpace room id. | [optional] 
**knowledge_room** | [**AiKnowledgeRoomRef**](AiKnowledgeRoomRef.md) | A single knowledge room, as an older client sends it. Read only when `knowledgeRooms` is absent; send `knowledgeRooms` instead. | [optional] 
**folder_context** | [**AiFolderContextRef**](AiFolderContextRef.md) | The folder connected to the chat as the round's context. It becomes the location the model is told the user works in, and the entry the round is attributed to. | [optional] 
**entity_id** | **str** | The entry the round is attributed to. A hint, resolved against the caller's own access. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_action_args import AiActionArgs

# TODO update the JSON string below
json = "{}"
# create an instance of AiActionArgs from a JSON string
ai_action_args_instance = AiActionArgs.from_json(json)
# print the JSON string representation of the object
print(AiActionArgs.to_json())

# convert the object into a dict
ai_action_args_dict = ai_action_args_instance.to_dict()
# create an instance of AiActionArgs from a dict
ai_action_args_from_dict = AiActionArgs.from_dict(ai_action_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


