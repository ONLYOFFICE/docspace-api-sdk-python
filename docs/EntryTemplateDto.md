# EntryTemplateDto
A metadata template assigned to an entry: the template with every field of it, each field carrying its value on the entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The template ID. | [optional] 
**name** | **str** | The template name. | [optional] 
**visible** | **bool** | Specifies if the template is visible in the UI pickers. | [optional] 
**cascade** | **bool** | Whether the template cascades from this entry to the folders and files below it. Only a folder or a room can  cascade; on a file the value is always false. | [optional] 
**conflict_resolve_type** | [**MetadataConflictResolveType**](MetadataConflictResolveType.md) | How the cascade of this entry treats a value an entry below already holds. Null while the template does not  cascade from this entry. | [optional] 
**fields** | [**List[EntryFieldDto]**](EntryFieldDto.md) | The template fields with their values on the entry. | [optional] 

## Example

```python
from docspace_api_sdk.models.entry_template_dto import EntryTemplateDto

# TODO update the JSON string below
json = "{}"
# create an instance of EntryTemplateDto from a JSON string
entry_template_dto_instance = EntryTemplateDto.from_json(json)
# print the JSON string representation of the object
print(EntryTemplateDto.to_json())

# convert the object into a dict
entry_template_dto_dict = entry_template_dto_instance.to_dict()
# create an instance of EntryTemplateDto from a dict
entry_template_dto_from_dict = EntryTemplateDto.from_dict(entry_template_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


