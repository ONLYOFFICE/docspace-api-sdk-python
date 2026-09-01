# AiChatSettingsDto
The chat settings parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **str** | The system prompt for the chat. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_chat_settings_dto import AiChatSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatSettingsDto from a JSON string
ai_chat_settings_dto_instance = AiChatSettingsDto.from_json(json)
# print the JSON string representation of the object
print(AiChatSettingsDto.to_json())

# convert the object into a dict
ai_chat_settings_dto_dict = ai_chat_settings_dto_instance.to_dict()
# create an instance of AiChatSettingsDto from a dict
ai_chat_settings_dto_from_dict = AiChatSettingsDto.from_dict(ai_chat_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


