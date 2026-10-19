# EntryMetadataDto
The metadata of an entry: the assigned templates with their values, and the custom fields holding a value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**templates** | [**List[EntryTemplateDto]**](EntryTemplateDto.md) | The assigned metadata templates, each field carrying its value on the entry. | [optional] 
**custom_fields** | [**List[CustomFieldValueDto]**](CustomFieldValueDto.md) | The custom fields with their values. | [optional] 

## Example

```python
from docspace_api_sdk.models.entry_metadata_dto import EntryMetadataDto

# TODO update the JSON string below
json = "{}"
# create an instance of EntryMetadataDto from a JSON string
entry_metadata_dto_instance = EntryMetadataDto.from_json(json)
# print the JSON string representation of the object
print(EntryMetadataDto.to_json())

# convert the object into a dict
entry_metadata_dto_dict = entry_metadata_dto_instance.to_dict()
# create an instance of EntryMetadataDto from a dict
entry_metadata_dto_from_dict = EntryMetadataDto.from_dict(entry_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


