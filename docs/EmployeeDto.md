# EmployeeDto
The user parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user ID. | [optional] 
**display_name** | **str** | The user display name. | [optional] 
**title** | **str** | The user title. | [optional] 
**avatar** | **str** | The user avatar. | [optional] 
**avatar_original** | **str** | The user original size avatar. | [optional] 
**avatar_max** | **str** | The user maximum size avatar. | [optional] 
**avatar_medium** | **str** | The user medium size avatar. | [optional] 
**avatar_small** | **str** | The user small size avatar. | [optional] 
**profile_url** | **str** | The user profile URL. | [optional] 
**has_avatar** | **bool** | Specifies if the user has an avatar or not. | [optional] 
**is_anonim** | **bool** | Specifies if the user is anonymous or not. | [optional] 

## Example

```python
from docspace-api-python.models.employee_dto import EmployeeDto

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


