# FormMetadataDto
The metadata of a single form field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The form field key. | [optional] 
**type** | **str** | The form field type. | [optional] 
**format** | **str** | The form field format. | [optional] 
**possible_values** | **List[str]** | The list of possible values for the form field. | [optional] 

## Example

```python
from docspace_api_sdk.models.form_metadata_dto import FormMetadataDto

# TODO update the JSON string below
json = "{}"
# create an instance of FormMetadataDto from a JSON string
form_metadata_dto_instance = FormMetadataDto.from_json(json)
# print the JSON string representation of the object
print(FormMetadataDto.to_json())

# convert the object into a dict
form_metadata_dto_dict = form_metadata_dto_instance.to_dict()
# create an instance of FormMetadataDto from a dict
form_metadata_dto_from_dict = FormMetadataDto.from_dict(form_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


