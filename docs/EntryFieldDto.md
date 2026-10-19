# EntryFieldDto
A metadata template field with its value on the entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The field ID. | [optional] 
**name** | **str** | The field name. | [optional] 
**type** | [**MetadataFieldType**](MetadataFieldType.md) | The field type. | [optional] 
**options** | [**List[MetadataFieldOptionDto]**](MetadataFieldOptionDto.md) | The choice options of the field. | [optional] 
**order** | **int** | The field display order inside the template. | [optional] 
**value** | [**MetadataValueDto**](MetadataValueDto.md) | The value of the field on the entry, or `null` when the entry holds no value for it. | [optional] 

## Example

```python
from docspace_api_sdk.models.entry_field_dto import EntryFieldDto

# TODO update the JSON string below
json = "{}"
# create an instance of EntryFieldDto from a JSON string
entry_field_dto_instance = EntryFieldDto.from_json(json)
# print the JSON string representation of the object
print(EntryFieldDto.to_json())

# convert the object into a dict
entry_field_dto_dict = entry_field_dto_instance.to_dict()
# create an instance of EntryFieldDto from a dict
entry_field_dto_from_dict = EntryFieldDto.from_dict(entry_field_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


