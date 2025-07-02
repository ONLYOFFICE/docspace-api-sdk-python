# CurrenciesArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[CurrenciesDto]**](CurrenciesDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.currencies_array_wrapper import CurrenciesArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of CurrenciesArrayWrapper from a JSON string
currencies_array_wrapper_instance = CurrenciesArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(CurrenciesArrayWrapper.to_json())

# convert the object into a dict
currencies_array_wrapper_dict = currencies_array_wrapper_instance.to_dict()
# create an instance of CurrenciesArrayWrapper from a dict
currencies_array_wrapper_from_dict = CurrenciesArrayWrapper.from_dict(currencies_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


