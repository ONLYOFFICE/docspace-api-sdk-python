# VectorizationSettingsDto
The vectorization settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EmbeddingProviderType**](EmbeddingProviderType.md) |  | [optional] 
**need_reset** | **bool** | Indicates whether the embedding provider API key needs to be reconfigured. | [optional] 

## Example

```python
from docspace_api_sdk.models.vectorization_settings_dto import VectorizationSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of VectorizationSettingsDto from a JSON string
vectorization_settings_dto_instance = VectorizationSettingsDto.from_json(json)
# print the JSON string representation of the object
print(VectorizationSettingsDto.to_json())

# convert the object into a dict
vectorization_settings_dto_dict = vectorization_settings_dto_instance.to_dict()
# create an instance of VectorizationSettingsDto from a dict
vectorization_settings_dto_from_dict = VectorizationSettingsDto.from_dict(vectorization_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


