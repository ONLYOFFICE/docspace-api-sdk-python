# PluginsDto

The plugins parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Specifies if the plugins are enabled or not. | [optional] 
**upload** | **bool** | Specifies if the plugins can be uploaded or not. | [optional] 
**delete** | **bool** | Specifies if the plugins can be deleted or not. | [optional] 

## Example

```python
from docspace.models.plugins_dto import PluginsDto

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


