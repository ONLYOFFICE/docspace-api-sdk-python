# AiEmbeddingModelPricing
The pricing of a single embedding model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the model, as the provider expects it on the wire. | 
**alias** | **str** | The display name of the model. | [optional] 
**owned_by** | **str** | The owner of the model, as reported by the provider. | [optional] 
**provider** | **str** | The provider that serves the model. | [optional] 
**link** | **str** | The link to the pricing page of the model. | [optional] 
**price** | [**AiEmbeddingPrice**](AiEmbeddingPrice.md) | The price of an embedding model, per token. | 

## Example

```python
from docspace_api_sdk.models.ai_embedding_model_pricing import AiEmbeddingModelPricing

# TODO update the JSON string below
json = "{}"
# create an instance of AiEmbeddingModelPricing from a JSON string
ai_embedding_model_pricing_instance = AiEmbeddingModelPricing.from_json(json)
# print the JSON string representation of the object
print(AiEmbeddingModelPricing.to_json())

# convert the object into a dict
ai_embedding_model_pricing_dict = ai_embedding_model_pricing_instance.to_dict()
# create an instance of AiEmbeddingModelPricing from a dict
ai_embedding_model_pricing_from_dict = AiEmbeddingModelPricing.from_dict(ai_embedding_model_pricing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


