# EmployeeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**display_name** | **str** | Display name | [optional] 
**title** | **str** | Title | [optional] 
**avatar** | **str** | Avatar | [optional] 
**avatar_original** | **str** | Original size avatar | [optional] 
**avatar_max** | **str** | Maximum size avatar | [optional] 
**avatar_medium** | **str** | Medium size avatar | [optional] 
**avatar_small** | **str** | Small avatar | [optional] 
**profile_url** | **str** | Profile URL | [optional] 
**has_avatar** | **bool** | Specifies if the user has an avatar or not | [optional] 
**is_anonim** | **bool** | Specifies if the user is an anonim or not | [optional] 

## Example

```python
from docspace.models.employee_dto import EmployeeDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeDto from a JSON string
employee_dto_instance = EmployeeDto.from_json(json)
# print the JSON string representation of the object
print(EmployeeDto.to_json())

# convert the object into a dict
employee_dto_dict = employee_dto_instance.to_dict()
# create an instance of EmployeeDto from a dict
employee_dto_from_dict = EmployeeDto.from_dict(employee_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


