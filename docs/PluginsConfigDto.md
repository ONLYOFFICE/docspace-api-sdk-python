# PluginsConfigDto
Which editor add-ons the portal connects. It currently connects none.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugins_data** | **List[str]** | The array of absolute URLs to the plugin configuration files. | [optional] [readonly] 

## Example

```python
from docspace_api_sdk.models.plugins_config_dto import PluginsConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of PluginsConfigDto from a JSON string
plugins_config_dto_instance = PluginsConfigDto.from_json(json)
# print the JSON string representation of the object
print(PluginsConfigDto.to_json())

# convert the object into a dict
plugins_config_dto_dict = plugins_config_dto_instance.to_dict()
# create an instance of PluginsConfigDto from a dict
plugins_config_dto_from_dict = PluginsConfigDto.from_dict(plugins_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


