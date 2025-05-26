# DeepLinkConfigurationRequestsDto

The request parameters for managing the deep link configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deep_link_settings** | [**TenantDeepLinkSettings**](TenantDeepLinkSettings.md) |  | [optional] 

## Example

```python
from docspace.models.deep_link_configuration_requests_dto import DeepLinkConfigurationRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeepLinkConfigurationRequestsDto from a JSON string
deep_link_configuration_requests_dto_instance = DeepLinkConfigurationRequestsDto.from_json(json)
# print the JSON string representation of the object
print(DeepLinkConfigurationRequestsDto.to_json())

# convert the object into a dict
deep_link_configuration_requests_dto_dict = deep_link_configuration_requests_dto_instance.to_dict()
# create an instance of DeepLinkConfigurationRequestsDto from a dict
deep_link_configuration_requests_dto_from_dict = DeepLinkConfigurationRequestsDto.from_dict(deep_link_configuration_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


