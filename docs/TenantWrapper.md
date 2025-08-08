# TenantWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**TenantDto**](TenantDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_wrapper import TenantWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TenantWrapper from a JSON string
tenant_wrapper_instance = TenantWrapper.from_json(json)
# print the JSON string representation of the object
print(TenantWrapper.to_json())

# convert the object into a dict
tenant_wrapper_dict = tenant_wrapper_instance.to_dict()
# create an instance of TenantWrapper from a dict
tenant_wrapper_from_dict = TenantWrapper.from_dict(tenant_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


