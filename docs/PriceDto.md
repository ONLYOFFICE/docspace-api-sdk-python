# PriceDto
The price parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | The price value. | [optional] 
**currency_symbol** | **str** | The currency symbol. | [optional] 
**iso_currency_symbol** | **str** | The three-character ISO 4217 currency symbol. | [optional] 

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


