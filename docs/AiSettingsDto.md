# AiSettingsDto
The AI module settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vectorization_enabled** | **bool** | Indicates whether document vectorization is enabled. | [optional] 
**vectorization_need_reset** | **bool** | Indicates whether the embedding provider API key needs to be reconfigured. | [optional] 
**ai_ready** | **bool** | Indicates whether the AI subsystem is fully configured and operational. | [optional] 
**embedding_model** | **str** | The name of the embedding model used for document vectorization. | 
**system_ai_enabled** | **bool** | Indicates whether the system-level AI provider is enabled. | [optional] 
**recommended_model_for_forms** | **str** | The identifier of the model recommended for form generation. | [optional] 
**tool_permission_mode** | [**AiToolPermissionMode**](AiToolPermissionMode.md) | How tool calls made by the model are approved for the current user. The default applies while the user has stored nothing. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_settings_dto import AiSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiSettingsDto from a JSON string
ai_settings_dto_instance = AiSettingsDto.from_json(json)
# print the JSON string representation of the object
print(AiSettingsDto.to_json())

# convert the object into a dict
ai_settings_dto_dict = ai_settings_dto_instance.to_dict()
# create an instance of AiSettingsDto from a dict
ai_settings_dto_from_dict = AiSettingsDto.from_dict(ai_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


