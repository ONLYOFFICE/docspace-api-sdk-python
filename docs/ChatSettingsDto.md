# ChatSettingsDto
The chat settings parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **str** | The system prompt for the chat. | [optional] 

## Example

```python
from docspace_api_sdk.models.chat_settings_dto import ChatSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ChatSettingsDto from a JSON string
chat_settings_dto_instance = ChatSettingsDto.from_json(json)
# print the JSON string representation of the object
print(ChatSettingsDto.to_json())

# convert the object into a dict
chat_settings_dto_dict = chat_settings_dto_instance.to_dict()
# create an instance of ChatSettingsDto from a dict
chat_settings_dto_from_dict = ChatSettingsDto.from_dict(chat_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


