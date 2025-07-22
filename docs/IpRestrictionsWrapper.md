# IpRestrictionsWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**IpRestrictionsDto**](IpRestrictionsDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.ip_restrictions_wrapper import IpRestrictionsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of IpRestrictionsWrapper from a JSON string
ip_restrictions_wrapper_instance = IpRestrictionsWrapper.from_json(json)
# print the JSON string representation of the object
print(IpRestrictionsWrapper.to_json())

# convert the object into a dict
ip_restrictions_wrapper_dict = ip_restrictions_wrapper_instance.to_dict()
# create an instance of IpRestrictionsWrapper from a dict
ip_restrictions_wrapper_from_dict = IpRestrictionsWrapper.from_dict(ip_restrictions_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


