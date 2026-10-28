# ManageFormFillingDto
The action to apply to the filling of a PDF form.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form_id** | **int** | The PDF form the action applies to. This is the value the operation reads, rather than the identifier in its  route, and the two are to be sent the same. | 
**action** | [**FormFillingManageAction**](FormFillingManageAction.md) | The action to apply. | [optional] 

## Example

```python
from docspace_api_sdk.models.manage_form_filling_dto import ManageFormFillingDto

# TODO update the JSON string below
json = "{}"
# create an instance of ManageFormFillingDto from a JSON string
manage_form_filling_dto_instance = ManageFormFillingDto.from_json(json)
# print the JSON string representation of the object
print(ManageFormFillingDto.to_json())

# convert the object into a dict
manage_form_filling_dto_dict = manage_form_filling_dto_instance.to_dict()
# create an instance of ManageFormFillingDto from a dict
manage_form_filling_dto_from_dict = ManageFormFillingDto.from_dict(manage_form_filling_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


