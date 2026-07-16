# AiModelPricingAiEmbeddingPrice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**alias** | **str** |  | [optional] 
**owned_by** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**price** | [**AiEmbeddingPrice**](AiEmbeddingPrice.md) |  | 

## Example

```python
from docspace_api_sdk.models.ai_model_pricing_ai_embedding_price import AiModelPricingAiEmbeddingPrice

# TODO update the JSON string below
json = "{}"
# create an instance of AiModelPricingAiEmbeddingPrice from a JSON string
ai_model_pricing_ai_embedding_price_instance = AiModelPricingAiEmbeddingPrice.from_json(json)
# print the JSON string representation of the object
print(AiModelPricingAiEmbeddingPrice.to_json())

# convert the object into a dict
ai_model_pricing_ai_embedding_price_dict = ai_model_pricing_ai_embedding_price_instance.to_dict()
# create an instance of AiModelPricingAiEmbeddingPrice from a dict
ai_model_pricing_ai_embedding_price_from_dict = AiModelPricingAiEmbeddingPrice.from_dict(ai_model_pricing_ai_embedding_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


