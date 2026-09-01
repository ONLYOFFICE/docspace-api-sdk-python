# AiChatEvent
Discriminated event emitted by the streaming methods of `AIEngine`. The engine never invokes user-supplied middleware or callbacks directly — every observable side-effect is encoded as a `ChatEvent` so the same stream can be replayed over SSE, WebSocket, or in-process.  Pause point: `tool-call-pending` is the only stop. The UI must execute the tool itself (consulting `autoAllow` to decide between the silent path and the approve dialog) and resume via `AIEngine.approveToolCall` or `AIEngine.denyToolCall`.  Other variants are pure data:  - `message-start` / `message-delta` / `message-end` — assistant reply lifecycle. - `message-incomplete` — the provider returned an error or incomplete status. - `thread-title` — auto-generated title ready for a new thread.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Emitted once per `sendWithStream` call, immediately after the user message has been persisted by storage and before the assistant stream starts. Carries the storage-assigned `id` and `createdAt`. The UI uses it to render the user bubble — no client-side optimistic placeholder is needed, which keeps the runtime tree free of phantom nodes from index-fallback ids. | 
**message** | [**AiThreadMessageLike**](AiThreadMessageLike.md) | The message the event is about, in the state it has reached. | [optional] 
**message_id** | **str** | The storage identifier of that message. | [optional] 
**idx** | **float** | The zero-based position of the pending tool call within the message. | [optional] 
**thread_id** | **str** | The thread the event belongs to. | [optional] 
**auto_allow** | **bool** | The consumer should execute the tool without prompting the user. True when the tool is in the persisted always-allow list, or the tool itself opts in via `TMCPItem.requireApproval === false` (host tools default to this). For a client-side tool with a server-side engine, this lets the engine return the pending call already flagged auto-allow so the client runs it and streams the result back without a dialog round-trip. | [optional] 
**server_executed** | **bool** | Set when the tool is served by a server-side system source: the consumer must NOT execute it locally — only show the approval UI (unless `autoAllow`) and resume via `approveToolCall` (no `result` needed) / `denyToolCall`. The engine runs it in-engine. | [optional] 
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


