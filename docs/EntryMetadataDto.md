# EntryMetadataDto
The metadata of an entry: the assigned templates with their values, and the custom fields holding a value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**templates** | [**List[EntryTemplateDto]**](EntryTemplateDto.md) | The assigned metadata templates, each field carrying its value on the entry. | [optional] 
**custom_fields** | [**List[CustomFieldValueDto]**](CustomFieldValueDto.md) | The custom fields with their values. | [optional] 
**has_metadata_fields** | **bool** | Whether the entry has a metadata field a user can see and fill, by hand or with the AI filling: a field of a  template in `templates` whose `visible` is true, or a custom field in `customFields`. False when both lists are  empty, when every template is hidden, or when none of the visible ones has a field. It says nothing about the  values: it stays true once every field is filled. The same flag is carried by the entry in a folder listing and  in the file and folder info responses as `hasMetadataFields`, so a client that has the listing needs no call here  to decide whether to offer the filling. | [optional] 

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


