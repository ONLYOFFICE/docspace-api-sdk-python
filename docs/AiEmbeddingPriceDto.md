# AiEmbeddingPriceDto
What an embedding model charges, which has one direction only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **float** | The cost of one million tokens turned into vectors. Embedding produces no completion, so this single  figure is the whole price. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_embedding_price_dto import AiEmbeddingPriceDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiEmbeddingPriceDto from a JSON string
ai_embedding_price_dto_instance = AiEmbeddingPriceDto.from_json(json)
# print the JSON string representation of the object
print(AiEmbeddingPriceDto.to_json())

# convert the object into a dict
ai_embedding_price_dto_dict = ai_embedding_price_dto_instance.to_dict()
# create an instance of AiEmbeddingPriceDto from a dict
ai_embedding_price_dto_from_dict = AiEmbeddingPriceDto.from_dict(ai_embedding_price_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


