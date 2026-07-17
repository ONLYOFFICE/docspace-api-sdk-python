# ModelDto
The AI model information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **int** | The unique identifier of the AI provider that offers this model. | [optional] 
**provider_title** | **str** | The human-readable display name of the AI provider (e.g., OpenAI, Anthropic). | 
**model_id** | **str** | The model identifier as recognized by the AI provider (e.g., gpt-4o, claude-sonnet-4-20250514). | 
**alias** | **str** | The display name for the model. | [optional] 
**capabilities** | [**AiModelCapabilities**](AiModelCapabilities.md) |  | [optional] 
**price** | [**AiChatPrice**](AiChatPrice.md) |  | [optional] 
**currency** | [**CurrencyInfo**](CurrencyInfo.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.model_dto import ModelDto

# TODO update the JSON string below
json = "{}"
# create an instance of ModelDto from a JSON string
model_dto_instance = ModelDto.from_json(json)
# print the JSON string representation of the object
print(ModelDto.to_json())

# convert the object into a dict
model_dto_dict = model_dto_instance.to_dict()
# create an instance of ModelDto from a dict
model_dto_from_dict = ModelDto.from_dict(model_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


