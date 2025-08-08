# FillingFormResultDtoString
The parameters of the form filling result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form_number** | **int** | The filling form number. | [optional] 
**completed_form** | [**FileDtoString**](FileDtoString.md) |  | [optional] 
**original_form** | [**FileDtoString**](FileDtoString.md) |  | [optional] 
**manager** | [**EmployeeFullDto**](EmployeeFullDto.md) |  | [optional] 
**room_id** | **str** | The room ID where filling the form. | [optional] 
**is_room_member** | **bool** | Specifies if the manager who fills the form is a room member or not. | [optional] 

## Example

```python
from docspace_api_sdk.models.filling_form_result_dto_string import FillingFormResultDtoString

# TODO update the JSON string below
json = "{}"
# create an instance of FillingFormResultDtoString from a JSON string
filling_form_result_dto_string_instance = FillingFormResultDtoString.from_json(json)
# print the JSON string representation of the object
print(FillingFormResultDtoString.to_json())

# convert the object into a dict
filling_form_result_dto_string_dict = filling_form_result_dto_string_instance.to_dict()
# create an instance of FillingFormResultDtoString from a dict
filling_form_result_dto_string_from_dict = FillingFormResultDtoString.from_dict(filling_form_result_dto_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


