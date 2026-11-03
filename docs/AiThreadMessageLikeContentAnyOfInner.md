# AiThreadMessageLikeContentAnyOfInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Part kind: `text`, `reasoning`, `source`, `image`, `file`, `audio`, `data` or `tool-call`. | 
**text** | **str** | The text of a `text` or `reasoning` part. | [optional] 
**parent_id** | **str** | Id of the part this one belongs to, on `text`, `reasoning`, `source` and `tool-call` parts. On a `reasoning` part the chat library keeps the provider's thinking signature here. | [optional] 
**source_type** | **str** | A `source` part's source kind; always `url`. | [optional] 
**id** | **str** | A `source` part's id. | [optional] 
**url** | **str** | A `source` part's URL. | [optional] 
**title** | **str** | A `source` part's title. | [optional] 
**image** | **str** | An `image` part's picture, as a URL (usually a `data:` URL). For an image the user attached, a JSON string `{ ref, title, kind: image }` naming the stored attachment instead. | [optional] 
**mime_type** | **str** | A `file` part's media type. For a file the user attached, a JSON string `{ ref, title, kind: file, path, type }` naming the stored attachment instead - the chat library carries the reference here. | [optional] 
**data** | **str** | A `file` part's content; empty when the part references an attachment. (A `data` part would carry its payload here too, as any JSON value; neither the chat library nor this service writes one.) | [optional] 
**filename** | **str** | The file name of a `file` or `image` part. | [optional] 
**name** | **str** | An `image` part's display name, or a `data` part's name. | [optional] 
**audio** | [**AiThreadMessageLikeContentAnyOfInnerAudio**](AiThreadMessageLikeContentAnyOfInnerAudio.md) |  | [optional] 
**tool_call_id** | **str** | A `tool-call` part's call id. | [optional] 
**tool_name** | **str** | A `tool-call` part's tool name. | [optional] 
**args** | **object** | A `tool-call` part's arguments. | [optional] 
**args_text** | **str** | A `tool-call` part's arguments as the model streamed them, JSON text. | [optional] 
**result** | **object** |  | [optional] 
**is_error** | **bool** | Whether a `tool-call` part's result is an error. | [optional] 
**artifact** | **object** |  | [optional] 
**interrupt** | [**AiThreadMessageLikeContentAnyOfInnerInterrupt**](AiThreadMessageLikeContentAnyOfInnerInterrupt.md) |  | [optional] 
**messages** | **List[object]** | Messages of a sub-agent run inside a `tool-call` part. | [optional] 
**metadata** | **object** | Provider-specific data of a `tool-call` part - for a Gemini call, `{ thoughtSignature }`, which has to be sent back with the call. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_thread_message_like_content_any_of_inner import AiThreadMessageLikeContentAnyOfInner

# TODO update the JSON string below
json = "{}"
# create an instance of AiThreadMessageLikeContentAnyOfInner from a JSON string
ai_thread_message_like_content_any_of_inner_instance = AiThreadMessageLikeContentAnyOfInner.from_json(json)
# print the JSON string representation of the object
print(AiThreadMessageLikeContentAnyOfInner.to_json())

# convert the object into a dict
ai_thread_message_like_content_any_of_inner_dict = ai_thread_message_like_content_any_of_inner_instance.to_dict()
# create an instance of AiThreadMessageLikeContentAnyOfInner from a dict
ai_thread_message_like_content_any_of_inner_from_dict = AiThreadMessageLikeContentAnyOfInner.from_dict(ai_thread_message_like_content_any_of_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


