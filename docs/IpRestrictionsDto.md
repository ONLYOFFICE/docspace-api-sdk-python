# IpRestrictionsDto
The addresses allowed to reach the portal, and whether the restriction is enforced.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_restrictions** | [**List[IpRestrictionBase]**](IpRestrictionBase.md) | The allowed addresses, each entry pairing a single IPv4 or IPv6 address with the flag that limits it to  administrators. This is the whole list that is to hold afterwards: entries not repeated here are deleted.  Ranges written as `from-to` and CIDR blocks are refused with 400, even though the portal matches such forms  when they are already stored. Enforcement spares only the portal owner and the installation own networks, so  a list without the caller address locks the remaining administrators out. | 
**enable** | **bool** | Whether the list is enforced. Leaving it out follows the list - on when addresses are sent, off when the list  is empty - and sending `true` with an empty list is refused with 400, since that would admit nobody. | [optional] 

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


