# CustomFieldValueDto
The custom text field of an entry: a free-form name with its value. Custom fields belong to no template, need no  assignment and are addressed by name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The field name. | [optional] 
**value** | **str** | The field value on the entry. | [optional] 

## Example

```python
from docspace_api_sdk.models.custom_field_value_dto import CustomFieldValueDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldValueDto from a JSON string
custom_field_value_dto_instance = CustomFieldValueDto.from_json(json)
# print the JSON string representation of the object
print(CustomFieldValueDto.to_json())

# convert the object into a dict
custom_field_value_dto_dict = custom_field_value_dto_instance.to_dict()
# create an instance of CustomFieldValueDto from a dict
custom_field_value_dto_from_dict = CustomFieldValueDto.from_dict(custom_field_value_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


