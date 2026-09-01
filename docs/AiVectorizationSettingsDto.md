# AiVectorizationSettingsDto
The vectorization settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AiEmbeddingProviderType**](AiEmbeddingProviderType.md) | The type of embedding provider configured for document vectorization. | [optional] 
**need_reset** | **bool** | Indicates whether the embedding provider API key needs to be reconfigured. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_vectorization_settings_dto import AiVectorizationSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiVectorizationSettingsDto from a JSON string
ai_vectorization_settings_dto_instance = AiVectorizationSettingsDto.from_json(json)
# print the JSON string representation of the object
print(AiVectorizationSettingsDto.to_json())

# convert the object into a dict
ai_vectorization_settings_dto_dict = ai_vectorization_settings_dto_instance.to_dict()
# create an instance of AiVectorizationSettingsDto from a dict
ai_vectorization_settings_dto_from_dict = AiVectorizationSettingsDto.from_dict(ai_vectorization_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


