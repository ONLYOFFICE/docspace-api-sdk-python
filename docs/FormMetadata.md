# FormMetadata
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
from docspace_api_sdk.models.form_metadata import FormMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FormMetadata from a JSON string
form_metadata_instance = FormMetadata.from_json(json)
# print the JSON string representation of the object
print(FormMetadata.to_json())

# convert the object into a dict
form_metadata_dict = form_metadata_instance.to_dict()
# create an instance of FormMetadata from a dict
form_metadata_from_dict = FormMetadata.from_dict(form_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


