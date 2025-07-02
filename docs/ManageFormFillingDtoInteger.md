# ManageFormFillingDtoInteger
The parameters for managing form filling.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form_id** | **int** | The ID of the form to manage. | [optional] 
**action** | [**FormFillingManageAction**](FormFillingManageAction.md) |  | [optional] 

## Example

```python
from docspace-api-python.models.manage_form_filling_dto_integer import ManageFormFillingDtoInteger

# TODO update the JSON string below
json = "{}"
# create an instance of ManageFormFillingDtoInteger from a JSON string
manage_form_filling_dto_integer_instance = ManageFormFillingDtoInteger.from_json(json)
# print the JSON string representation of the object
print(ManageFormFillingDtoInteger.to_json())

# convert the object into a dict
manage_form_filling_dto_integer_dict = manage_form_filling_dto_integer_instance.to_dict()
# create an instance of ManageFormFillingDtoInteger from a dict
manage_form_filling_dto_integer_from_dict = ManageFormFillingDtoInteger.from_dict(manage_form_filling_dto_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


