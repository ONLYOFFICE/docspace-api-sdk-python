# WebPluginDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | [optional] 
**version** | **str** | Version | [optional] 
**description** | **str** | Description | [optional] 
**license** | **str** | License | [optional] 
**author** | **str** | Author | [optional] 
**home_page** | **str** | Home page | [optional] 
**plugin_name** | **str** | PluginName | [optional] 
**scopes** | **str** | Scopes | [optional] 
**image** | **str** | Image | [optional] 
**create_by** | [**EmployeeDto**](EmployeeDto.md) |  | [optional] 
**create_on** | **datetime** | Create on | [optional] 
**enabled** | **bool** | Enabled | [optional] 
**system** | **bool** | System | [optional] 
**url** | **str** | Url | [optional] 
**settings** | **str** | Settings | [optional] 

## Example

```python
from docspace.models.web_plugin_dto import WebPluginDto

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


