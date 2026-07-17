# WebSearchSettingsDto
The web search settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indicates whether web search is currently enabled. | [optional] 
**type** | [**EngineType**](EngineType.md) |  | [optional] 
**need_reset** | **bool** | Indicates whether the web search API key needs to be reconfigured. | [optional] 

## Example

```python
from docspace_api_sdk.models.web_search_settings_dto import WebSearchSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebSearchSettingsDto from a JSON string
web_search_settings_dto_instance = WebSearchSettingsDto.from_json(json)
# print the JSON string representation of the object
print(WebSearchSettingsDto.to_json())

# convert the object into a dict
web_search_settings_dto_dict = web_search_settings_dto_instance.to_dict()
# create an instance of WebSearchSettingsDto from a dict
web_search_settings_dto_from_dict = WebSearchSettingsDto.from_dict(web_search_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


