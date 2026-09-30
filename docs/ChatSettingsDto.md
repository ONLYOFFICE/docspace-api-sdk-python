# ChatSettingsDto
The chat configuration of an AI room.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **str** | The instruction put in front of every conversation held in the room, which sets the role the assistant takes  and the way it answers. Empty when the room was left on the behaviour the portal provides by default. | [optional] 

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


