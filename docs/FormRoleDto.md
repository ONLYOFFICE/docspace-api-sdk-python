# FormRoleDto
The form role parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_name** | **str** | The role name. | 
**role_color** | **str** | The role color. | [optional] 
**user** | [**EmployeeFullDto**](EmployeeFullDto.md) |  | [optional] 
**sequence** | **int** | The role sequence. | 
**submitted** | **bool** | Specifies if the role is submitted. | 
**stoped_by** | [**EmployeeFullDto**](EmployeeFullDto.md) |  | [optional] 
**history** | **Dict[str, datetime]** | The role history. | [optional] 
**role_status** | [**FormFillingStatus**](FormFillingStatus.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.form_role_dto import FormRoleDto

# TODO update the JSON string below
json = "{}"
# create an instance of FormRoleDto from a JSON string
form_role_dto_instance = FormRoleDto.from_json(json)
# print the JSON string representation of the object
print(FormRoleDto.to_json())

# convert the object into a dict
form_role_dto_dict = form_role_dto_instance.to_dict()
# create an instance of FormRoleDto from a dict
form_role_dto_from_dict = FormRoleDto.from_dict(form_role_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


