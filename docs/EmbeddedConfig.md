# EmbeddedConfig
The addresses the framed viewer needs. It is reported for the embedded layout only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embed_url** | **str** | The page to put into the frame. It is empty when the opening carries no external share key, since a framed  viewer cannot authenticate a portal member. | [optional] 
**save_url** | **str** | Where the download button of the framed viewer leads. | [optional] [readonly] 
**share_link_param** | **str** | The query fragment carrying the external share key, ampersand included, out of which the addresses around it  are built. | [optional] 
**share_url** | **str** | The address behind the share button of the framed viewer, the document opened full-screen for reading. It is  empty when the opening carries no external share key. | [optional] 
**toolbar_docked** | **str** | Where the framed viewer puts its toolbar. The portal always asks for the top. | [optional] [readonly] 

## Example

```python
from docspace_api_sdk.models.embedded_config import EmbeddedConfig

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


