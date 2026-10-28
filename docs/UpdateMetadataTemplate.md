# UpdateMetadataTemplate
The parameters for updating a metadata template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new template name. | [optional] 
**visible** | **bool** | Specifies if the template is visible in the UI pickers. | [optional] 

## Example

```python
from docspace_api_sdk.models.update_metadata_template import UpdateMetadataTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMetadataTemplate from a JSON string
update_metadata_template_instance = UpdateMetadataTemplate.from_json(json)
# print the JSON string representation of the object
print(UpdateMetadataTemplate.to_json())

# convert the object into a dict
update_metadata_template_dict = update_metadata_template_instance.to_dict()
# create an instance of UpdateMetadataTemplate from a dict
update_metadata_template_from_dict = UpdateMetadataTemplate.from_dict(update_metadata_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


