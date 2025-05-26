# ProviderDto

The provider information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The provider name. | [optional] 
**key** | **str** | The provider key. | [optional] 
**connected** | **bool** | Specifies whether the provider is connected. | [optional] 
**oauth** | **bool** | Specifies if the provider is OAuth. | [optional] 
**redirect_url** | **str** | The provider redirect URL. | [optional] 
**required_connection_url** | **bool** | The required connection URL flag. | [optional] 
**client_id** | **str** | The provider OAuth client ID. | [optional] 

## Example

```python
from docspace.models.provider_dto import ProviderDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderDto from a JSON string
provider_dto_instance = ProviderDto.from_json(json)
# print the JSON string representation of the object
print(ProviderDto.to_json())

# convert the object into a dict
provider_dto_dict = provider_dto_instance.to_dict()
# create an instance of ProviderDto from a dict
provider_dto_from_dict = ProviderDto.from_dict(provider_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


