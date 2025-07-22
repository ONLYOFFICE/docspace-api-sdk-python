# WebPluginDto
The web plugin information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The web plugin name. | [optional] 
**version** | **str** | The web plugin version. | [optional] 
**description** | **str** | The web plugin description. | [optional] 
**license** | **str** | The web plugin license. | [optional] 
**author** | **str** | The web plugin author. | [optional] 
**home_page** | **str** | The web plugin home page URL. | [optional] 
**plugin_name** | **str** | The name by which the web plugin is registered in the window object. | [optional] 
**scopes** | **str** | The web plugin scopes. | [optional] 
**image** | **str** | The web plugin image. | [optional] 
**create_by** | [**EmployeeDto**](EmployeeDto.md) |  | [optional] 
**create_on** | **datetime** | The date and time when the web plugin was created. | [optional] 
**enabled** | **bool** | Specifies if the web plugin is enabled or not. | [optional] 
**system** | **bool** | Specifies if the web plugin is system or not. | [optional] 
**url** | **str** | The web plugin URL. | [optional] 
**settings** | **str** | The web plugin settings. | [optional] 

## Example

```python
from docspace-api-sdk.models.web_plugin_dto import WebPluginDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebPluginDto from a JSON string
web_plugin_dto_instance = WebPluginDto.from_json(json)
# print the JSON string representation of the object
print(WebPluginDto.to_json())

# convert the object into a dict
web_plugin_dto_dict = web_plugin_dto_instance.to_dict()
# create an instance of WebPluginDto from a dict
web_plugin_dto_from_dict = WebPluginDto.from_dict(web_plugin_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


