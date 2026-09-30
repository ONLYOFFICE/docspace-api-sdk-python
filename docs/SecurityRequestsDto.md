# SecurityRequestsDto
Which member is granted or denied the administrator role of which portal module.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **UUID** | The module the role applies to, given by its GUID. The all-zero GUID stands for the portal itself and grants  or revokes the DocSpace administrator role, which covers every module at once; a GUID that names no module  group is stored without effect rather than refused. | 
**user_id** | **UUID** | The portal member the role is given to or taken from, by user ID. The member has to exist already - nobody is  created here - and promoting a guest or a plain member turns them into a paid one. | 
**administrator** | **bool** | Which way the role goes: `true` adds the member to the module administrator group, `false` removes them from  it. Taking away the portal-wide role also drops the member from every product group. | [optional] 

## Example

```python
from docspace_api_sdk.models.security_requests_dto import SecurityRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityRequestsDto from a JSON string
security_requests_dto_instance = SecurityRequestsDto.from_json(json)
# print the JSON string representation of the object
print(SecurityRequestsDto.to_json())

# convert the object into a dict
security_requests_dto_dict = security_requests_dto_instance.to_dict()
# create an instance of SecurityRequestsDto from a dict
security_requests_dto_from_dict = SecurityRequestsDto.from_dict(security_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


