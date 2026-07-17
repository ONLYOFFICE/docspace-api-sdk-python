# ContinueChatBody
Parameters for continuing an AI chat session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The user message to append to the conversation. | 
**context_folder_id** | **int** | The optional collection of file identifiers to attach as context for the AI model. | [optional] 
**files** | [**List[ContinueChatBodyFilesInner]**](ContinueChatBodyFilesInner.md) | The list of attached files. | [optional] 

## Example

```python
from docspace_api_sdk.models.continue_chat_body import ContinueChatBody

# TODO update the JSON string below
json = "{}"
# create an instance of ContinueChatBody from a JSON string
continue_chat_body_instance = ContinueChatBody.from_json(json)
# print the JSON string representation of the object
print(ContinueChatBody.to_json())

# convert the object into a dict
continue_chat_body_dict = continue_chat_body_instance.to_dict()
# create an instance of ContinueChatBody from a dict
continue_chat_body_from_dict = ContinueChatBody.from_dict(continue_chat_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


