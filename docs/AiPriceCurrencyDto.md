# AiPriceCurrencyDto
The currency the AI prices are quoted in.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The ISO 4217 code of the currency the prices are quoted in. | 
**symbol** | **str** | The display symbol of the currency. | 

## Example

```python
from docspace_api_sdk.models.ai_price_currency_dto import AiPriceCurrencyDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiPriceCurrencyDto from a JSON string
ai_price_currency_dto_instance = AiPriceCurrencyDto.from_json(json)
# print the JSON string representation of the object
print(AiPriceCurrencyDto.to_json())

# convert the object into a dict
ai_price_currency_dto_dict = ai_price_currency_dto_instance.to_dict()
# create an instance of AiPriceCurrencyDto from a dict
ai_price_currency_dto_from_dict = AiPriceCurrencyDto.from_dict(ai_price_currency_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


