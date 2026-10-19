# IpRestrictionDto
The IP restiction parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The IP restiction ID. | [optional] 
**tenant_id** | **int** | The tenant ID. | [optional] 
**ip** | **str** | The IP address. | 
**for_admin** | **bool** | Specifies if the IP address is for administrator users only or not. | [optional] 

## Example

```python
from docspace_api_sdk.models.ip_restriction_dto import IpRestrictionDto

# TODO update the JSON string below
json = "{}"
# create an instance of IpRestrictionDto from a JSON string
ip_restriction_dto_instance = IpRestrictionDto.from_json(json)
# print the JSON string representation of the object
print(IpRestrictionDto.to_json())

# convert the object into a dict
ip_restriction_dto_dict = ip_restriction_dto_instance.to_dict()
# create an instance of IpRestrictionDto from a dict
ip_restriction_dto_from_dict = IpRestrictionDto.from_dict(ip_restriction_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


