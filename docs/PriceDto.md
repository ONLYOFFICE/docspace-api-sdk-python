# PriceDto
What a quota costs, and the currency that amount is in.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | The amount for one billing period, per unit for a quota sold by the unit. It is empty for a quota that is  not sold for money - the free, trial and non-profit ones - and for a quota this installation has no price  list entry for. | [optional] 
**currency_symbol** | **str** | The symbol to print in front of `value`, such as `$`. It is chosen for the currency, not for the portal  language, so it is not a localised format. | [optional] 
**iso_currency_symbol** | **str** | The currency as a three-letter ISO 4217 code, which is the value to compare on when `currencySymbol` is  ambiguous between currencies that share a sign. | [optional] 

## Example

```python
from docspace_api_sdk.models.price_dto import PriceDto

# TODO update the JSON string below
json = "{}"
# create an instance of PriceDto from a JSON string
price_dto_instance = PriceDto.from_json(json)
# print the JSON string representation of the object
print(PriceDto.to_json())

# convert the object into a dict
price_dto_dict = price_dto_instance.to_dict()
# create an instance of PriceDto from a dict
price_dto_from_dict = PriceDto.from_dict(price_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


