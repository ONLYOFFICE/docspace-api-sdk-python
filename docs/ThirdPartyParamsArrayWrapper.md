# ThirdPartyParamsArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[ThirdPartyParams]**](ThirdPartyParams.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.third_party_params_array_wrapper import ThirdPartyParamsArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyParamsArrayWrapper from a JSON string
third_party_params_array_wrapper_instance = ThirdPartyParamsArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyParamsArrayWrapper.to_json())

# convert the object into a dict
third_party_params_array_wrapper_dict = third_party_params_array_wrapper_instance.to_dict()
# create an instance of ThirdPartyParamsArrayWrapper from a dict
third_party_params_array_wrapper_from_dict = ThirdPartyParamsArrayWrapper.from_dict(third_party_params_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


