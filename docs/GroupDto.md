# GroupDto
The group parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The group name. | [optional] 
**parent** | **str** | The parent group ID. | [optional] 
**category** | **str** | The group category ID. | [optional] 
**id** | **str** | The group ID. | [optional] 
**is_ldap** | **bool** | Specifies if the LDAP settings are enabled for the group or not. | [optional] 
**manager** | [**EmployeeFullDto**](EmployeeFullDto.md) |  | [optional] 
**members** | [**List[EmployeeFullDto]**](EmployeeFullDto.md) | The list of group members. | [optional] 
**shared** | **bool** | Specifies whether the group can be shared or not. | [optional] 
**members_count** | **int** | The number of group members. | [optional] 

## Example

```python
from docspace_api_sdk.models.group_dto import GroupDto

# TODO update the JSON string below
json = "{}"
# create an instance of GroupDto from a JSON string
group_dto_instance = GroupDto.from_json(json)
# print the JSON string representation of the object
print(GroupDto.to_json())

# convert the object into a dict
group_dto_dict = group_dto_instance.to_dict()
# create an instance of GroupDto from a dict
group_dto_from_dict = GroupDto.from_dict(group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


