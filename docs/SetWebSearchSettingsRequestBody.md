# SetWebSearchSettingsRequestBody
Parameters for configuring web search settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indicates whether web search is enabled for AI chat sessions. | [optional] 
**type** | [**EngineType**](EngineType.md) |  | [optional] 
**key** | **str** | The API key for the selected web search engine. Pass null to keep the existing key unchanged. | [optional] 

## Example

```python
from docspace_api_sdk.models.set_web_search_settings_request_body import SetWebSearchSettingsRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of SetWebSearchSettingsRequestBody from a JSON string
set_web_search_settings_request_body_instance = SetWebSearchSettingsRequestBody.from_json(json)
# print the JSON string representation of the object
print(SetWebSearchSettingsRequestBody.to_json())

# convert the object into a dict
set_web_search_settings_request_body_dict = set_web_search_settings_request_body_instance.to_dict()
# create an instance of SetWebSearchSettingsRequestBody from a dict
set_web_search_settings_request_body_from_dict = SetWebSearchSettingsRequestBody.from_dict(set_web_search_settings_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


