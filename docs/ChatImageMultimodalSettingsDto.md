# ChatImageMultimodalSettingsDto
The image multimodal settings for the chat model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formats** | **List[str]** | The supported image formats. | [optional] 

## Example

```python
from docspace_api_sdk.models.chat_image_multimodal_settings_dto import ChatImageMultimodalSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ChatImageMultimodalSettingsDto from a JSON string
chat_image_multimodal_settings_dto_instance = ChatImageMultimodalSettingsDto.from_json(json)
# print the JSON string representation of the object
print(ChatImageMultimodalSettingsDto.to_json())

# convert the object into a dict
chat_image_multimodal_settings_dto_dict = chat_image_multimodal_settings_dto_instance.to_dict()
# create an instance of ChatImageMultimodalSettingsDto from a dict
chat_image_multimodal_settings_dto_from_dict = ChatImageMultimodalSettingsDto.from_dict(chat_image_multimodal_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


