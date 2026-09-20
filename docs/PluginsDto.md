# PluginsDto
What the installation allows to be done with web plugins.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether web plugins run on this portal at all. While it is `false` the operations under  `api/2.0/settings/webplugins` are of no use, whatever the other two flags say. All three are `false`  unless the installation switched plugins on in its configuration. | [optional] 
**upload** | **bool** | Whether an administrator may add a plugin of their own through  `POST api/2.0/settings/webplugins`. While it is `false` only the plugins that ship with the installation  are available. | [optional] 
**delete** | **bool** | Whether an added plugin may be removed again through `DELETE api/2.0/settings/webplugins/{name}`. The  plugins that ship with the installation cannot be removed regardless of this flag. | [optional] 

## Example

```python
from docspace_api_sdk.models.plugins_dto import PluginsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PluginsDto from a JSON string
plugins_dto_instance = PluginsDto.from_json(json)
# print the JSON string representation of the object
print(PluginsDto.to_json())

# convert the object into a dict
plugins_dto_dict = plugins_dto_instance.to_dict()
# create an instance of PluginsDto from a dict
plugins_dto_from_dict = PluginsDto.from_dict(plugins_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


