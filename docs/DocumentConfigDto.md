# DocumentConfigDto
The document config parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_type** | **str** | The file type of the document. | [optional] 
**info** | [**InfoConfigDto**](InfoConfigDto.md) |  | [optional] 
**is_linked_for_me** | **bool** | Specifies if the documnet is linked for current user. | [optional] 
**key** | **str** | The document key. | [optional] 
**permissions** | [**PermissionsConfig**](PermissionsConfig.md) |  | [optional] 
**shared_link_param** | **str** | The shared link parameter of the document. | [optional] 
**shared_link_key** | **str** | The shared link key of the document. | [optional] 
**reference_data** | [**FileReferenceData**](FileReferenceData.md) |  | [optional] 
**title** | **str** | The document title. | [optional] 
**url** | **str** | The document url. | [optional] 
**is_form** | **bool** | Indicates whether this is a form. | [optional] 
**options** | [**Options**](Options.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.document_config_dto import DocumentConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentConfigDto from a JSON string
document_config_dto_instance = DocumentConfigDto.from_json(json)
# print the JSON string representation of the object
print(DocumentConfigDto.to_json())

# convert the object into a dict
document_config_dto_dict = document_config_dto_instance.to_dict()
# create an instance of DocumentConfigDto from a dict
document_config_dto_from_dict = DocumentConfigDto.from_dict(document_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


