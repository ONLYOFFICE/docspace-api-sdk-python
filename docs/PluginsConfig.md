# PluginsConfig
The configuration settings to connect the special add-ons.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugins_data** | **List[str]** | The array of absolute URLs to the plugin configuration files. | [optional] [readonly] 

## Example

```python
from docspace-api-python.models.plugins_config import PluginsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PluginsConfig from a JSON string
plugins_config_instance = PluginsConfig.from_json(json)
# print the JSON string representation of the object
print(PluginsConfig.to_json())

# convert the object into a dict
plugins_config_dict = plugins_config_instance.to_dict()
# create an instance of PluginsConfig from a dict
plugins_config_from_dict = PluginsConfig.from_dict(plugins_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


