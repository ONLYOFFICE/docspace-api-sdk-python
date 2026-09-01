# AiModel
AI model metadata. Describes a single model available from a provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Model identifier as used by the provider API (e.g. `gpt-4o`, `claude-sonnet-4-20250514`). | 
**name** | **str** | Human-readable model name for display in the UI. | 
**provider** | [**AiProviderType**](AiProviderType.md) | Provider that offers this model. | 
**reasoning** | **bool** | Whether this model supports extended thinking / chain-of-thought reasoning. | [optional] 
**capabilities** | **float** | Bitmask of model capabilities (Chat, Image, Vision, Tools, etc.). Used to filter models per  {@link  ActionType  } . | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_model import AiModel

# TODO update the JSON string below
json = "{}"
# create an instance of AiModel from a JSON string
ai_model_instance = AiModel.from_json(json)
# print the JSON string representation of the object
print(AiModel.to_json())

# convert the object into a dict
ai_model_dict = ai_model_instance.to_dict()
# create an instance of AiModel from a dict
ai_model_from_dict = AiModel.from_dict(ai_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


