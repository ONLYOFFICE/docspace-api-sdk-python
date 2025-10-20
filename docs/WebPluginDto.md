# WebPluginDto
The web plugin information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The web plugin name. | 
**version** | **str** | The web plugin version. | 
**min_doc_space_version** | **str** | The minimum version of DocSpace with which the plugin is guaranteed to work. | [optional] 
**description** | **str** | The web plugin description. | 
**license** | **str** | The web plugin license. | 
**author** | **str** | The web plugin author. | 
**home_page** | **str** | The web plugin home page URL. | 
**plugin_name** | **str** | The name by which the web plugin is registered in the window object. | 
**scopes** | **str** | The web plugin scopes. | 
**image** | **str** | The web plugin image. | 
**create_by** | [**EmployeeDto**](EmployeeDto.md) |  | 
**create_on** | **datetime** | The date and time when the web plugin was created. | 
**enabled** | **bool** | Specifies if the web plugin is enabled or not. | 
**system** | **bool** | Specifies if the web plugin is system or not. | 
**url** | **str** | The web plugin URL. | 
**settings** | **str** | The web plugin settings. | 

## Example

```python
from docspace_api_sdk.models.web_plugin_dto import WebPluginDto

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


