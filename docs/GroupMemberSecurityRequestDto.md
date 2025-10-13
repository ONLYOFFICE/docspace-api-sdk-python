# GroupMemberSecurityRequestDto
The security request parameters of the group member.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**EmployeeFullDto**](EmployeeFullDto.md) |  | 
**group_access** | [**FileShare**](FileShare.md) |  | 
**user_access** | [**FileShare**](FileShare.md) |  | [optional] 
**overridden** | **bool** | Specifies if the group access rights are overridden or not. | 
**can_edit_access** | **bool** | Specifies if the group member can edit the group access rights or not. | 
**owner** | **bool** | Specifies if the group member is a group owner or not. | 

## Example

```python
from docspace_api_sdk.models.group_member_security_request_dto import GroupMemberSecurityRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMemberSecurityRequestDto from a JSON string
group_member_security_request_dto_instance = GroupMemberSecurityRequestDto.from_json(json)
# print the JSON string representation of the object
print(GroupMemberSecurityRequestDto.to_json())

# convert the object into a dict
group_member_security_request_dto_dict = group_member_security_request_dto_instance.to_dict()
# create an instance of GroupMemberSecurityRequestDto from a dict
group_member_security_request_dto_from_dict = GroupMemberSecurityRequestDto.from_dict(group_member_security_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


