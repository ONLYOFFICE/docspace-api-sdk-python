# EmbeddedConfig

The configuration parameters for the embedded document type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embed_url** | **str** | The absolute URL to the document serving as a source file for the document embedded into the web page. | [optional] 
**save_url** | **str** | The absolute URL that will allow the document to be saved onto the user personal computer. | [optional] [readonly] 
**share_link_param** | **str** | The shared URL parameter. | [optional] 
**share_url** | **str** | The absolute URL that will allow other users to share this document. | [optional] 
**toolbar_docked** | **str** | The place for the embedded viewer toolbar, can be either \&quot;top\&quot; or \&quot;bottom\&quot;. | [optional] [readonly] 

## Example

```python
from docspace.models.embedded_config import EmbeddedConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedConfig from a JSON string
embedded_config_instance = EmbeddedConfig.from_json(json)
# print the JSON string representation of the object
print(EmbeddedConfig.to_json())

# convert the object into a dict
embedded_config_dict = embedded_config_instance.to_dict()
# create an instance of EmbeddedConfig from a dict
embedded_config_from_dict = EmbeddedConfig.from_dict(embedded_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


