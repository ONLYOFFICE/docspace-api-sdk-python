# ChatSettingsDto
The chat settings parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **int** | The AI provider ID. | [optional] 
**model_id** | **str** | The AI model ID used for chat completions. | [optional] 
**model_alias** | **str** | The AI model display alias. | [optional] 
**prompt** | **str** | The system prompt for the chat. | [optional] 
**multimodal** | [**ChatMultimodalSettingsDto**](ChatMultimodalSettingsDto.md) |  | [optional] 
**thinking** | **bool** | Indicates whether the model supports extended thinking mode. | [optional] 
**capabilities** | [**AiModelCapabilities**](AiModelCapabilities.md) |  | [optional] 
**internal** | **bool** | Indicates whether this is an internal AI gateway provider. | [optional] [readonly] 

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


