# RenameChatBody
Parameters for renaming an AI chat session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new display name for the chat session (maximum 255 characters). | 

## Example

```python
from docspace_api_sdk.models.rename_chat_body import RenameChatBody

# TODO update the JSON string below
json = "{}"
# create an instance of RenameChatBody from a JSON string
rename_chat_body_instance = RenameChatBody.from_json(json)
# print the JSON string representation of the object
print(RenameChatBody.to_json())

# convert the object into a dict
rename_chat_body_dict = rename_chat_body_instance.to_dict()
# create an instance of RenameChatBody from a dict
rename_chat_body_from_dict = RenameChatBody.from_dict(rename_chat_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


