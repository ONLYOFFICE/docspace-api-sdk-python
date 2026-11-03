# AiThreadMessageLikeContentAnyOfInnerInterrupt
A `tool-call` part's pending request for human input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Interrupt kind; always `human`. | 
**payload** | **object** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_thread_message_like_content_any_of_inner_interrupt import AiThreadMessageLikeContentAnyOfInnerInterrupt

# TODO update the JSON string below
json = "{}"
# create an instance of AiThreadMessageLikeContentAnyOfInnerInterrupt from a JSON string
ai_thread_message_like_content_any_of_inner_interrupt_instance = AiThreadMessageLikeContentAnyOfInnerInterrupt.from_json(json)
# print the JSON string representation of the object
print(AiThreadMessageLikeContentAnyOfInnerInterrupt.to_json())

# convert the object into a dict
ai_thread_message_like_content_any_of_inner_interrupt_dict = ai_thread_message_like_content_any_of_inner_interrupt_instance.to_dict()
# create an instance of AiThreadMessageLikeContentAnyOfInnerInterrupt from a dict
ai_thread_message_like_content_any_of_inner_interrupt_from_dict = AiThreadMessageLikeContentAnyOfInnerInterrupt.from_dict(ai_thread_message_like_content_any_of_inner_interrupt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


