# CurrenciesDto
The currencies parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_country_code** | **str** | The ISO country code. | [optional] 
**iso_currency_symbol** | **str** | The ISO currency symbol. | [optional] 
**currency_native_name** | **str** | The currency native name. | [optional] 

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


