# WebPluginRequests
The configuration settings for the web plugin instance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Controls whether the web plugin is active and operational. | [optional] 
**settings** | **str** | The JSON-formatted configuration settings for the web plugin. | [optional] 

## Example

```python
from docspace_api_sdk.models.web_plugin_requests import WebPluginRequests

# TODO update the JSON string below
json = "{}"
# create an instance of WebPluginRequests from a JSON string
web_plugin_requests_instance = WebPluginRequests.from_json(json)
# print the JSON string representation of the object
print(WebPluginRequests.to_json())

# convert the object into a dict
web_plugin_requests_dict = web_plugin_requests_instance.to_dict()
# create an instance of WebPluginRequests from a dict
web_plugin_requests_from_dict = WebPluginRequests.from_dict(web_plugin_requests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


