# SaveFormRoleMappingDtoInteger
The parameters for saving form role mapping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form_id** | **int** | The form ID. | [optional] 
**roles** | [**List[FormRole]**](FormRole.md) | The collection of roles. | [optional] 

## Example

```python
from docspace-api-python.models.save_form_role_mapping_dto_integer import SaveFormRoleMappingDtoInteger

# TODO update the JSON string below
json = "{}"
# create an instance of SaveFormRoleMappingDtoInteger from a JSON string
save_form_role_mapping_dto_integer_instance = SaveFormRoleMappingDtoInteger.from_json(json)
# print the JSON string representation of the object
print(SaveFormRoleMappingDtoInteger.to_json())

# convert the object into a dict
save_form_role_mapping_dto_integer_dict = save_form_role_mapping_dto_integer_instance.to_dict()
# create an instance of SaveFormRoleMappingDtoInteger from a dict
save_form_role_mapping_dto_integer_from_dict = SaveFormRoleMappingDtoInteger.from_dict(save_form_role_mapping_dto_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


