# SetUserChatSettingsRequestBody
Parameters for updating user chat settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**web_search_enabled** | **bool** | Indicates whether the AI assistant is allowed to perform web searches when generating responses. | [optional] 
**reasoning_effort** | [**ChatReasoningEffort**](ChatReasoningEffort.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.set_user_chat_settings_request_body import SetUserChatSettingsRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of SetUserChatSettingsRequestBody from a JSON string
set_user_chat_settings_request_body_instance = SetUserChatSettingsRequestBody.from_json(json)
# print the JSON string representation of the object
print(SetUserChatSettingsRequestBody.to_json())

# convert the object into a dict
set_user_chat_settings_request_body_dict = set_user_chat_settings_request_body_instance.to_dict()
# create an instance of SetUserChatSettingsRequestBody from a dict
set_user_chat_settings_request_body_from_dict = SetUserChatSettingsRequestBody.from_dict(set_user_chat_settings_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


