# ProviderArrayWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[ProviderDto]**](ProviderDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.provider_array_wrapper import ProviderArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderArrayWrapper from a JSON string
provider_array_wrapper_instance = ProviderArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(ProviderArrayWrapper.to_json())

# convert the object into a dict
provider_array_wrapper_dict = provider_array_wrapper_instance.to_dict()
# create an instance of ProviderArrayWrapper from a dict
provider_array_wrapper_from_dict = ProviderArrayWrapper.from_dict(provider_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


