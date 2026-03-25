# UserChatSettingsDto
The user chat settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**web_search_enabled** | **bool** | Indicates whether the AI assistant is allowed to perform web searches when generating responses in this room. | [optional] 
**reasoning_effort** | [**ChatReasoningEffort**](ChatReasoningEffort.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.user_chat_settings_dto import UserChatSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserChatSettingsDto from a JSON string
user_chat_settings_dto_instance = UserChatSettingsDto.from_json(json)
# print the JSON string representation of the object
print(UserChatSettingsDto.to_json())

# convert the object into a dict
user_chat_settings_dto_dict = user_chat_settings_dto_instance.to_dict()
# create an instance of UserChatSettingsDto from a dict
user_chat_settings_dto_from_dict = UserChatSettingsDto.from_dict(user_chat_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


