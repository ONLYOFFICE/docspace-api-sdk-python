# IpRestrictionsDto
The parameters for configuring new IP restriction settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_restrictions** | [**List[IpRestrictionBase]**](IpRestrictionBase.md) | The list of IP restriction addresses. | 
**enable** | **bool** | Specifies whether to enable IP restrictions or not. | [optional] 

## Example

```python
from docspace_api_sdk.models.ip_restrictions_dto import IpRestrictionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of IpRestrictionsDto from a JSON string
ip_restrictions_dto_instance = IpRestrictionsDto.from_json(json)
# print the JSON string representation of the object
print(IpRestrictionsDto.to_json())

# convert the object into a dict
ip_restrictions_dto_dict = ip_restrictions_dto_instance.to_dict()
# create an instance of IpRestrictionsDto from a dict
ip_restrictions_dto_from_dict = IpRestrictionsDto.from_dict(ip_restrictions_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


