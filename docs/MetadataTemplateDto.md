# MetadataTemplateDto
The metadata template information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The template ID. | [optional] 
**name** | **str** | The template name. | [optional] 
**visible** | **bool** | Specifies if the template is visible in the UI pickers. | [optional] 
**create_by** | [**EmployeeDto**](EmployeeDto.md) | The user who created the template. A user who has since left the portal comes back as the lost user placeholder. | [optional] 
**create_on** | [**ApiDateTime**](ApiDateTime.md) | The template creation date. | [optional] 
**modified_by** | [**EmployeeDto**](EmployeeDto.md) | The user who changed the template itself last: its name or its visibility. The creator until somebody changes  it; a change of a field is recorded on the field, not here. | [optional] 
**modified_on** | [**ApiDateTime**](ApiDateTime.md) | The date when the template was modified last. | [optional] 
**fields** | [**List[MetadataFieldDto]**](MetadataFieldDto.md) | The template metadata fields. | [optional] 

## Example

```python
from docspace_api_sdk.models.metadata_template_dto import MetadataTemplateDto

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataTemplateDto from a JSON string
metadata_template_dto_instance = MetadataTemplateDto.from_json(json)
# print the JSON string representation of the object
print(MetadataTemplateDto.to_json())

# convert the object into a dict
metadata_template_dto_dict = metadata_template_dto_instance.to_dict()
# create an instance of MetadataTemplateDto from a dict
metadata_template_dto_from_dict = MetadataTemplateDto.from_dict(metadata_template_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


