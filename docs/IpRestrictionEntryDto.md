# IpRestrictionEntryDto
One allowed address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | The IPv4 or IPv6 address. | 
**for_admin** | **bool** | Whether the address admits administrators only. | [optional] 

## Example

```python
from docspace_api_sdk.models.ip_restriction_entry_dto import IpRestrictionEntryDto

# TODO update the JSON string below
json = "{}"
# create an instance of IpRestrictionEntryDto from a JSON string
ip_restriction_entry_dto_instance = IpRestrictionEntryDto.from_json(json)
# print the JSON string representation of the object
print(IpRestrictionEntryDto.to_json())

# convert the object into a dict
ip_restriction_entry_dto_dict = ip_restriction_entry_dto_instance.to_dict()
# create an instance of IpRestrictionEntryDto from a dict
ip_restriction_entry_dto_from_dict = IpRestrictionEntryDto.from_dict(ip_restriction_entry_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


