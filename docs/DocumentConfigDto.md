# DocumentConfigDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_type** | **str** | File type | [optional] 
**info** | [**InfoConfigDto**](InfoConfigDto.md) |  | [optional] 
**is_linked_for_me** | **bool** | Is linked for me | [optional] 
**key** | **str** | Key | [optional] 
**permissions** | [**PermissionsConfig**](PermissionsConfig.md) |  | [optional] 
**shared_link_param** | **str** | Shared link param | [optional] 
**shared_link_key** | **str** | Shared link key | [optional] 
**reference_data** | [**FileReferenceData**](FileReferenceData.md) |  | [optional] 
**title** | **str** | Title | [optional] 
**url** | **str** | Url | [optional] 
**options** | [**Options**](Options.md) |  | [optional] 

## Example

```python
from docspace.models.document_config_dto import DocumentConfigDto

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


