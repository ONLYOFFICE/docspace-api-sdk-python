# MetadataFieldOptionDto
The metadata field choice option.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | The option ID. | [optional] 
**value** | **str** | The option value. | [optional] 

## Example

```python
from docspace_api_sdk.models.metadata_field_option_dto import MetadataFieldOptionDto

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataFieldOptionDto from a JSON string
metadata_field_option_dto_instance = MetadataFieldOptionDto.from_json(json)
# print the JSON string representation of the object
print(MetadataFieldOptionDto.to_json())

# convert the object into a dict
metadata_field_option_dto_dict = metadata_field_option_dto_instance.to_dict()
# create an instance of MetadataFieldOptionDto from a dict
metadata_field_option_dto_from_dict = MetadataFieldOptionDto.from_dict(metadata_field_option_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


