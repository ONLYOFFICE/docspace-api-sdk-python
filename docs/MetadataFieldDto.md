# MetadataFieldDto
The metadata field information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The field ID. | [optional] 
**template_id** | **int** | The ID of the template the field belongs to. | [optional] 
**name** | **str** | The field name. | [optional] 
**type** | [**MetadataFieldType**](MetadataFieldType.md) | The field type. | [optional] 
**options** | [**List[MetadataFieldOptionDto]**](MetadataFieldOptionDto.md) | The choice options of the field. | [optional] 
**order** | **int** | The field display order inside the template. | [optional] 

## Example

```python
from docspace_api_sdk.models.metadata_field_dto import MetadataFieldDto

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataFieldDto from a JSON string
metadata_field_dto_instance = MetadataFieldDto.from_json(json)
# print the JSON string representation of the object
print(MetadataFieldDto.to_json())

# convert the object into a dict
metadata_field_dto_dict = metadata_field_dto_instance.to_dict()
# create an instance of MetadataFieldDto from a dict
metadata_field_dto_from_dict = MetadataFieldDto.from_dict(metadata_field_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


