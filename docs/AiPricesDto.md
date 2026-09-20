# AiPricesDto
What the AI features cost out of the portal wallet, grouped by the kind of model, in one currency.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | [**List[AiEntryPricingDtoAiChatPriceDto]**](AiEntryPricingDtoAiChatPriceDto.md) | The chat models on offer, each priced per million prompt and completion tokens. A model listed here is one  the installation can bill for, not necessarily one this portal may use -  `GET api/2.0/portal/payment/ai-model/restrictions` says which are allowed. | 
**embedding** | [**List[AiEntryPricingDtoAiEmbeddingPriceDto]**](AiEntryPricingDtoAiEmbeddingPriceDto.md) | The embedding models on offer, priced per million tokens of input; an embedding model has no completion  side, so its price object carries `prompt` alone. | 
**image** | [**List[AiEntryPricingDtoAiImagePriceDto]**](AiEntryPricingDtoAiImagePriceDto.md) | The image models on offer, priced per million prompt and completion tokens plus a price for each image  produced. | 
**web_search** | [**List[AiEntryPricingDtoDecimal]**](AiEntryPricingDtoDecimal.md) | The web search providers on offer. Their `price` is a bare number - the cost of one search - rather than  an object, because there are no tokens to distinguish. | 
**currency** | [**CurrencyInfo**](CurrencyInfo.md) | The currency every price above is expressed in, with its ISO code and symbol. One answer never mixes  currencies, so this is the only place to read it. | 

## Example

```python
from docspace_api_sdk.models.ai_prices_dto import AiPricesDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiPricesDto from a JSON string
ai_prices_dto_instance = AiPricesDto.from_json(json)
# print the JSON string representation of the object
print(AiPricesDto.to_json())

# convert the object into a dict
ai_prices_dto_dict = ai_prices_dto_instance.to_dict()
# create an instance of AiPricesDto from a dict
ai_prices_dto_from_dict = AiPricesDto.from_dict(ai_prices_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


