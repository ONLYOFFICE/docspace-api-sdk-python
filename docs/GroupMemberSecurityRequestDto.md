# GroupMemberSecurityRequestDto
One member of a portal group together with the access that member has on the file or folder the group was granted  rights to. Every line of the answer describes the same file or folder and differs only in the member and in the  level that applies to them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**EmployeeFullDto**](EmployeeFullDto.md) | The member the line is about, as the portal reports the account: the display name, the avatar and the portal  role to show next to the access level. | 
**group_access** | [**FileShare**](FileShare.md) | The level granted to the group as a whole on this file or folder. It belongs to the group record rather than  to the member, so the same value repeats on every line of the answer; a group whose record was set back to  none is answered with an empty list instead. | 
**user_access** | [**FileShare**](FileShare.md) | The level granted to this member alone on the same file or folder, or `null` when the member has no record of  their own and the group level is what applies. The member who created the file or folder is always reported  here as a room manager, whatever their own record says. | [optional] 
**overridden** | **bool** | Whether `userAccess` is the level that decides what the member may do. When it is false the member inherits  `groupAccess`, and the creator of the file or folder is always reported as overridden because of the room  manager level forced onto them. | 
**can_edit_access** | **bool** | Whether the caller may still change the level of this member. It comes back false on the line of the member  who created the file or folder, on the line of the caller themselves, and on every line at once when the  caller may read the file or folder but not manage access to it. | 
**owner** | **bool** | Whether this member created the file or folder - the owner of the entry, not the owner of the group. Their  level is reported as a room manager one and cannot be taken away through this group. | 

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


