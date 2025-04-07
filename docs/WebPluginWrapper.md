# WebPluginWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**WebPluginDto**](WebPluginDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.web_plugin_wrapper import WebPluginWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of WebPluginWrapper from a JSON string
web_plugin_wrapper_instance = WebPluginWrapper.from_json(json)
# print the JSON string representation of the object
print(WebPluginWrapper.to_json())

# convert the object into a dict
web_plugin_wrapper_dict = web_plugin_wrapper_instance.to_dict()
# create an instance of WebPluginWrapper from a dict
web_plugin_wrapper_from_dict = WebPluginWrapper.from_dict(web_plugin_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


