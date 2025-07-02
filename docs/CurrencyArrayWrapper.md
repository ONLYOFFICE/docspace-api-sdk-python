# CurrencyArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[Currency]**](Currency.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.currency_array_wrapper import CurrencyArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyArrayWrapper from a JSON string
currency_array_wrapper_instance = CurrencyArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(CurrencyArrayWrapper.to_json())

# convert the object into a dict
currency_array_wrapper_dict = currency_array_wrapper_instance.to_dict()
# create an instance of CurrencyArrayWrapper from a dict
currency_array_wrapper_from_dict = CurrencyArrayWrapper.from_dict(currency_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


