# AiAiUserSettingsDto
The per-user AI settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_recommended_model_visible** | **bool** | Indicates whether the recommended model banner is visible in the AI chat for the current user. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_ai_user_settings_dto import AiAiUserSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiAiUserSettingsDto from a JSON string
ai_ai_user_settings_dto_instance = AiAiUserSettingsDto.from_json(json)
# print the JSON string representation of the object
print(AiAiUserSettingsDto.to_json())

# convert the object into a dict
ai_ai_user_settings_dto_dict = ai_ai_user_settings_dto_instance.to_dict()
# create an instance of AiAiUserSettingsDto from a dict
ai_ai_user_settings_dto_from_dict = AiAiUserSettingsDto.from_dict(ai_ai_user_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


