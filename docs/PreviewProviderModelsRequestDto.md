# PreviewProviderModelsRequestDto
Request parameters for previewing models available from a provider before saving it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ProviderType**](ProviderType.md) |  | [optional] 
**url** | **str** | The API endpoint URL. Required for OpenAiCompatible type; optional for other types that have default URLs. | [optional] 
**key** | **str** | The authentication API key for the AI provider. | 

## Example

```python
from docspace_api_sdk.models.preview_provider_models_request_dto import PreviewProviderModelsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewProviderModelsRequestDto from a JSON string
preview_provider_models_request_dto_instance = PreviewProviderModelsRequestDto.from_json(json)
# print the JSON string representation of the object
print(PreviewProviderModelsRequestDto.to_json())

# convert the object into a dict
preview_provider_models_request_dto_dict = preview_provider_models_request_dto_instance.to_dict()
# create an instance of PreviewProviderModelsRequestDto from a dict
preview_provider_models_request_dto_from_dict = PreviewProviderModelsRequestDto.from_dict(preview_provider_models_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


