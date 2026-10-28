# AiMetadataMatchDto
Where a text search met the metadata of a file, a folder or a room: one string value that holds the searched text,  with the field it belongs to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **int** | The ID of the metadata template the matching field belongs to. Null for a custom field, which belongs to no  template the API shows. | [optional] 
**field_id** | **int** | The ID of the matching template field. Null for a custom field, which is addressed by its name alone. | [optional] 
**field_name** | **str** | The name of the matching field: the template field or the custom field as it is shown in the entry metadata. | [optional] 
**value** | **str** | The stored value that holds the searched text, as it was written, not only the matching part of it. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_metadata_match_dto import AiMetadataMatchDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiMetadataMatchDto from a JSON string
ai_metadata_match_dto_instance = AiMetadataMatchDto.from_json(json)
# print the JSON string representation of the object
print(AiMetadataMatchDto.to_json())

# convert the object into a dict
ai_metadata_match_dto_dict = ai_metadata_match_dto_instance.to_dict()
# create an instance of AiMetadataMatchDto from a dict
ai_metadata_match_dto_from_dict = AiMetadataMatchDto.from_dict(ai_metadata_match_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


