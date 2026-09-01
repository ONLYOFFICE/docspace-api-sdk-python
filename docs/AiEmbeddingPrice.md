# AiEmbeddingPrice
The price of an embedding model, per token.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **float** | The price of a single input token. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_embedding_price import AiEmbeddingPrice

# TODO update the JSON string below
json = "{}"
# create an instance of AiEmbeddingPrice from a JSON string
ai_embedding_price_instance = AiEmbeddingPrice.from_json(json)
# print the JSON string representation of the object
print(AiEmbeddingPrice.to_json())

# convert the object into a dict
ai_embedding_price_dict = ai_embedding_price_instance.to_dict()
# create an instance of AiEmbeddingPrice from a dict
ai_embedding_price_from_dict = AiEmbeddingPrice.from_dict(ai_embedding_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


