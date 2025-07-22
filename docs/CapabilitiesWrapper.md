# CapabilitiesWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CapabilitiesDto**](CapabilitiesDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.capabilities_wrapper import CapabilitiesWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilitiesWrapper from a JSON string
capabilities_wrapper_instance = CapabilitiesWrapper.from_json(json)
# print the JSON string representation of the object
print(CapabilitiesWrapper.to_json())

# convert the object into a dict
capabilities_wrapper_dict = capabilities_wrapper_instance.to_dict()
# create an instance of CapabilitiesWrapper from a dict
capabilities_wrapper_from_dict = CapabilitiesWrapper.from_dict(capabilities_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


