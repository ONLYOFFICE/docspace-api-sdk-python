# MetadataValueDto
The value of a metadata field on an entry. Exactly one of the value properties is set, the one matching the field type:  `stringValue` for a string field, `numberValue` for a number field, `dateValue` for a date field,  `optionIds` for a single or multiple choice field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string_value** | **str** | The string value. | [optional] 
**number_value** | **int** | The number value. | [optional] 
**date_value** | [**ApiDateTime**](ApiDateTime.md) | The date value. | [optional] 
**option_ids** | **List[UUID]** | The selected choice option IDs. | [optional] 

## Example

```python
from docspace_api_sdk.models.metadata_value_dto import MetadataValueDto

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataValueDto from a JSON string
metadata_value_dto_instance = MetadataValueDto.from_json(json)
# print the JSON string representation of the object
print(MetadataValueDto.to_json())

# convert the object into a dict
metadata_value_dto_dict = metadata_value_dto_instance.to_dict()
# create an instance of MetadataValueDto from a dict
metadata_value_dto_from_dict = MetadataValueDto.from_dict(metadata_value_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


