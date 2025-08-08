# Module
The module information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The module ID. | [optional] 
**app_name** | **str** | The module product class name. | [optional] 
**title** | **str** | The module product class name. | [optional] 
**link** | **str** | The URL to the module start page. | [optional] 
**icon_url** | **str** | The module icon URL. | [optional] 
**image_url** | **str** | The module large image URL. | [optional] 
**help_url** | **str** | The module help URL. | [optional] 
**description** | **str** | The module description. | [optional] 
**is_primary** | **bool** | Specifies if the module is primary or not. | [optional] 

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


