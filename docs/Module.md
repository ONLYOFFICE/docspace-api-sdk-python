# Module
The descriptor of a portal module: what it is called, where it starts and how it is pictured.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | The identifier of the module. It is the same in every portal and in every language, so use it rather than the  title to tell modules apart. | [optional] 
**app_name** | **str** | The short system name of the module, the one that appears in its addresses and in the portal configuration.  Unlike the title it is not translated. | [optional] 
**title** | **str** | The display name of the module, already translated for the calling account, so it changes with the language  and must not be compared against a fixed string. | [optional] 
**link** | **str** | The address of the start page of the module, to be opened in a browser rather than called as an API. | [optional] 
**icon_url** | **str** | The address of the small icon of the module, meant for a menu entry. | [optional] 
**image_url** | **str** | The address of the large image of the module, meant for a tile or a start screen. | [optional] 
**help_url** | **str** | The address of the help section of the module. It is empty when the portal publishes no help for it. | [optional] 
**description** | **str** | The one-line description of the module shown next to its title, translated for the calling account. | [optional] 
**is_primary** | **bool** | Whether the portal opens this module first when no other destination is given. | [optional] 

## Example

```python
from docspace_api_sdk.models.module import Module

# TODO update the JSON string below
json = "{}"
# create an instance of Module from a JSON string
module_instance = Module.from_json(json)
# print the JSON string representation of the object
print(Module.to_json())

# convert the object into a dict
module_dict = module_instance.to_dict()
# create an instance of Module from a dict
module_from_dict = Module.from_dict(module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


