# StartUpdateUserTypeDto
The parameters for updating the type of the user or guest when reassigning rooms and shared files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EmployeeType**](EmployeeType.md) |  | [optional] 
**user_id** | **str** | The user ID. | [optional] 
**reassign_user_id** | **str** | The user ID to reassign. | [optional] 

## Example

```python
from docspace-api-python.models.start_update_user_type_dto import StartUpdateUserTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of StartUpdateUserTypeDto from a JSON string
start_update_user_type_dto_instance = StartUpdateUserTypeDto.from_json(json)
# print the JSON string representation of the object
print(StartUpdateUserTypeDto.to_json())

# convert the object into a dict
start_update_user_type_dto_dict = start_update_user_type_dto_instance.to_dict()
# create an instance of StartUpdateUserTypeDto from a dict
start_update_user_type_dto_from_dict = StartUpdateUserTypeDto.from_dict(start_update_user_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


