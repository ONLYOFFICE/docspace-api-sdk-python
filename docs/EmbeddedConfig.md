# EmbeddedConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embed_url** | **str** | Embed url | [optional] [readonly] 
**save_url** | **str** | Save url | [optional] [readonly] 
**share_link_param** | **str** | Share link param | [optional] 
**share_url** | **str** | Share url | [optional] [readonly] 
**toolbar_docked** | **str** | Toolbar docked | [optional] [readonly] 

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


