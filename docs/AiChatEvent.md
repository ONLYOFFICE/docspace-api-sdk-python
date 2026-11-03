# AiChatEvent
One event of a chat stream, told apart by `type`: `message-start`, `message-delta` and `message-end` frame the assistant reply, `message-incomplete` reports a provider error or an unfinished answer, `thread-title` carries a generated title, and `tool-call-pending` pauses the round until the call is approved (`POST api/2.0/ai/ai/approve-tool-call`) or denied (`POST api/2.0/ai/ai/deny-tool-call`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Emitted once per `sendWithStream` call, immediately after the user message has been persisted by storage and before the assistant stream starts. Carries the storage-assigned `id` and `createdAt`. The UI uses it to render the user bubble — no client-side optimistic placeholder is needed, which keeps the runtime tree free of phantom nodes from index-fallback ids. | 
**message** | [**AiThreadMessageLike**](AiThreadMessageLike.md) | The message the event is about, in the state it has reached. | [optional] 
**message_id** | **str** | The storage identifier of that message. | [optional] 
**idx** | **float** | The zero-based position of the pending tool call within the message. | [optional] 
**thread_id** | **str** | The thread the event belongs to. | [optional] 
**auto_allow** | **bool** | The tool runs without asking the user, as the user's tool permission mode decides: under `ask` never - the always-allow list, `requireApproval` and the annotations are all ignored; under `auto` a tool on the always-allow list, one with `requireApproval: false`, or one annotated `readOnlyHint: true` or `destructiveHint: false`; under `allow` every tool. | [optional] 
**server_executed** | **bool** | The tool is run by the service itself: the client must not run it, only ask for approval (unless `autoAllow`) and approve or deny the call - an approval needs no `result`. | [optional] 
**title** | **str** | The generated thread title. | [optional] 
**profile_id** | **str** | The profile that generated the title, when one was used. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_chat_event import AiChatEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatEvent from a JSON string
ai_chat_event_instance = AiChatEvent.from_json(json)
# print the JSON string representation of the object
print(AiChatEvent.to_json())

# convert the object into a dict
ai_chat_event_dict = ai_chat_event_instance.to_dict()
# create an instance of AiChatEvent from a dict
ai_chat_event_from_dict = AiChatEvent.from_dict(ai_chat_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


