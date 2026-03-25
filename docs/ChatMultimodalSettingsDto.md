# ChatMultimodalSettingsDto
The multimodal settings for the chat model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | [**ChatImageMultimodalSettingsDto**](ChatImageMultimodalSettingsDto.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.chat_multimodal_settings_dto import ChatMultimodalSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMultimodalSettingsDto from a JSON string
chat_multimodal_settings_dto_instance = ChatMultimodalSettingsDto.from_json(json)
# print the JSON string representation of the object
print(ChatMultimodalSettingsDto.to_json())

# convert the object into a dict
chat_multimodal_settings_dto_dict = chat_multimodal_settings_dto_instance.to_dict()
# create an instance of ChatMultimodalSettingsDto from a dict
chat_multimodal_settings_dto_from_dict = ChatMultimodalSettingsDto.from_dict(chat_multimodal_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


