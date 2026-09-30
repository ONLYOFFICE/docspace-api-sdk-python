# CurrenciesDto
One currency the portal's subscription prices can be quoted in, with the region it belongs to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_country_code** | **str** | The two-letter ISO code of the country the currency is that of, which is the region the price list was  picked for rather than the country of the caller. | [optional] 
**iso_currency_symbol** | **str** | The three-letter ISO 4217 code of the currency. On the first item of the answer it is the currency the  amounts from `GET api/2.0/portal/payment/prices` are expressed in. | [optional] 
**currency_native_name** | **str** | The currency name in the language of its own region - not in the portal language, and not a symbol. | [optional] 

## Example

```python
from docspace_api_sdk.models.currencies_dto import CurrenciesDto

# TODO update the JSON string below
json = "{}"
# create an instance of CurrenciesDto from a JSON string
currencies_dto_instance = CurrenciesDto.from_json(json)
# print the JSON string representation of the object
print(CurrenciesDto.to_json())

# convert the object into a dict
currencies_dto_dict = currencies_dto_instance.to_dict()
# create an instance of CurrenciesDto from a dict
currencies_dto_from_dict = CurrenciesDto.from_dict(currencies_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


