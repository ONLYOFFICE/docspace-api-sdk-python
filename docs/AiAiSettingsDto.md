# AiAiSettingsDto
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

## Example

```python
from docspace_api_sdk.models.ai_ai_settings_dto import AiAiSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiAiSettingsDto from a JSON string
ai_ai_settings_dto_instance = AiAiSettingsDto.from_json(json)
# print the JSON string representation of the object
print(AiAiSettingsDto.to_json())

# convert the object into a dict
ai_ai_settings_dto_dict = ai_ai_settings_dto_instance.to_dict()
# create an instance of AiAiSettingsDto from a dict
ai_ai_settings_dto_from_dict = AiAiSettingsDto.from_dict(ai_ai_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


