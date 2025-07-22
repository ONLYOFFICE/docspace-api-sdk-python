# TemplatesConfig
The presence or absence of the templates in the \"Create New...\" menu option.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** | The absolute URL to the image for template. | [optional] 
**title** | **str** | The template title that will be displayed in the \&quot;Create New...\&quot; menu option. | [optional] 
**url** | **str** | The absolute URL to the document where it will be created and available after creation. | [optional] 

## Example

```python
from docspace-api-sdk.models.templates_config import TemplatesConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatesConfig from a JSON string
templates_config_instance = TemplatesConfig.from_json(json)
# print the JSON string representation of the object
print(TemplatesConfig.to_json())

# convert the object into a dict
templates_config_dict = templates_config_instance.to_dict()
# create an instance of TemplatesConfig from a dict
templates_config_from_dict = TemplatesConfig.from_dict(templates_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


