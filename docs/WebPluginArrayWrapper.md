# WebPluginArrayWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[WebPluginDto]**](WebPluginDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.web_plugin_array_wrapper import WebPluginArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of WebPluginArrayWrapper from a JSON string
web_plugin_array_wrapper_instance = WebPluginArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(WebPluginArrayWrapper.to_json())

# convert the object into a dict
web_plugin_array_wrapper_dict = web_plugin_array_wrapper_instance.to_dict()
# create an instance of WebPluginArrayWrapper from a dict
web_plugin_array_wrapper_from_dict = WebPluginArrayWrapper.from_dict(web_plugin_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


