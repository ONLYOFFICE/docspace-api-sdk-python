# AssignMetadataTemplates
The parameters for assigning metadata templates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_ids** | **List[int]** | The metadata template IDs. | 
**cascade** | **bool** | Specifies if the templates are propagated to the folder sub-entries. | [optional] 
**conflict_resolve_type** | [**MetadataConflictResolveType**](MetadataConflictResolveType.md) | The conflict resolve type for the cascade assignment. | [optional] 

## Example

```python
from docspace_api_sdk.models.assign_metadata_templates import AssignMetadataTemplates

# TODO update the JSON string below
json = "{}"
# create an instance of AssignMetadataTemplates from a JSON string
assign_metadata_templates_instance = AssignMetadataTemplates.from_json(json)
# print the JSON string representation of the object
print(AssignMetadataTemplates.to_json())

# convert the object into a dict
assign_metadata_templates_dict = assign_metadata_templates_instance.to_dict()
# create an instance of AssignMetadataTemplates from a dict
assign_metadata_templates_from_dict = AssignMetadataTemplates.from_dict(assign_metadata_templates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


