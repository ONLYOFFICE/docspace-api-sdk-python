# CurrencyInfo
The currency the AI prices are quoted in.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The ISO 4217 code of the currency the prices are quoted in. | 
**symbol** | **str** | The display symbol of the currency. | 

## Example

```python
from docspace_api_sdk.models.currency_info import CurrencyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyInfo from a JSON string
currency_info_instance = CurrencyInfo.from_json(json)
# print the JSON string representation of the object
print(CurrencyInfo.to_json())

# convert the object into a dict
currency_info_dict = currency_info_instance.to_dict()
# create an instance of CurrencyInfo from a dict
currency_info_from_dict = CurrencyInfo.from_dict(currency_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


