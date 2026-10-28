# CreateMetadataTemplateRequestDto
The request parameters for creating a metadata template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The template name. | 
**visible** | **bool** | Specifies if the template is visible in the UI pickers. | [optional] 
**fields** | [**List[MetadataFieldRequest]**](MetadataFieldRequest.md) | The template metadata fields. | [optional] 

## Example

```python
from docspace_api_sdk.models.create_metadata_template_request_dto import CreateMetadataTemplateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMetadataTemplateRequestDto from a JSON string
create_metadata_template_request_dto_instance = CreateMetadataTemplateRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateMetadataTemplateRequestDto.to_json())

# convert the object into a dict
create_metadata_template_request_dto_dict = create_metadata_template_request_dto_instance.to_dict()
# create an instance of CreateMetadataTemplateRequestDto from a dict
create_metadata_template_request_dto_from_dict = CreateMetadataTemplateRequestDto.from_dict(create_metadata_template_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


