# FillingFormResultDtoInteger
The parameters of the form filling result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form_number** | **int** | The filling form number. | 
**completed_form** | [**FileDtoInteger**](FileDtoInteger.md) |  | [optional] 
**original_form** | [**FileDtoInteger**](FileDtoInteger.md) |  | [optional] 
**manager** | [**EmployeeFullDto**](EmployeeFullDto.md) |  | [optional] 
**room_id** | **int** | The room ID where filling the form. | 
**is_room_member** | **bool** | Specifies if the manager who fills the form is a room member or not. | [optional] 

## Example

```python
from docspace_api_sdk.models.filling_form_result_dto_integer import FillingFormResultDtoInteger

# TODO update the JSON string below
json = "{}"
# create an instance of FillingFormResultDtoInteger from a JSON string
filling_form_result_dto_integer_instance = FillingFormResultDtoInteger.from_json(json)
# print the JSON string representation of the object
print(FillingFormResultDtoInteger.to_json())

# convert the object into a dict
filling_form_result_dto_integer_dict = filling_form_result_dto_integer_instance.to_dict()
# create an instance of FillingFormResultDtoInteger from a dict
filling_form_result_dto_integer_from_dict = FillingFormResultDtoInteger.from_dict(filling_form_result_dto_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


