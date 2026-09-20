# WebPluginRequests
The state the portal keeps for an installed web plugin: whether it runs, and its own settings blob.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether the plugin runs in this portal. Switching it on adds the domains its manifest declares to the portal  Content Security Policy and switching it off takes them away again; connected clients are told of the new  state without a reload. | [optional] 
**settings** | **str** | The configuration the plugin reads at run time, as a JSON document serialised into a string. Its shape is  defined by the plugin and not by the portal, which stores it encrypted for this portal alone. It replaces  whatever was stored rather than merging into it, so send `{}` when there is nothing to keep. | 

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


