# CurrencyAmount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The three-character ISO 4217 currency symbol. | [optional] 
**amount** | **float** | The amount in the specified currency. | [optional] 

## Example

```python
from docspace_api_sdk.models.currency_amount import CurrencyAmount

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyAmount from a JSON string
currency_amount_instance = CurrencyAmount.from_json(json)
# print the JSON string representation of the object
print(CurrencyAmount.to_json())

# convert the object into a dict
currency_amount_dict = currency_amount_instance.to_dict()
# create an instance of CurrencyAmount from a dict
currency_amount_from_dict = CurrencyAmount.from_dict(currency_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


