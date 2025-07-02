# TariffWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**Tariff**](Tariff.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.tariff_wrapper import TariffWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TariffWrapper from a JSON string
tariff_wrapper_instance = TariffWrapper.from_json(json)
# print the JSON string representation of the object
print(TariffWrapper.to_json())

# convert the object into a dict
tariff_wrapper_dict = tariff_wrapper_instance.to_dict()
# create an instance of TariffWrapper from a dict
tariff_wrapper_from_dict = TariffWrapper.from_dict(tariff_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


