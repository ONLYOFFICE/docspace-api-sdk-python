# StartNewChatBody
Parameters for starting a new AI chat session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The initial user message to send to the AI assistant. | 
**context_folder_id** | **int** | The optional collection of file identifiers to attach as context for the AI model. | [optional] 
**files** | [**List[ContinueChatBodyFilesInner]**](ContinueChatBodyFilesInner.md) | The list of attached files. | [optional] 

## Example

```python
from docspace_api_sdk.models.start_new_chat_body import StartNewChatBody

# TODO update the JSON string below
json = "{}"
# create an instance of StartNewChatBody from a JSON string
start_new_chat_body_instance = StartNewChatBody.from_json(json)
# print the JSON string representation of the object
print(StartNewChatBody.to_json())

# convert the object into a dict
start_new_chat_body_dict = start_new_chat_body_instance.to_dict()
# create an instance of StartNewChatBody from a dict
start_new_chat_body_from_dict = StartNewChatBody.from_dict(start_new_chat_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


