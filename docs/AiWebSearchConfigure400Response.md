# AiWebSearchConfigure400Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | True when the configuration was persisted. | 
**config** | [**AiWebSearchConfig**](AiWebSearchConfig.md) | The persisted web-search configuration. Present on success. | [optional] 
**error** | **str** | The error message, ready to be shown to the caller. | 

## Example

```python
from docspace_api_sdk.models.ai_web_search_configure400_response import AiWebSearchConfigure400Response

# TODO update the JSON string below
json = "{}"
# create an instance of AiWebSearchConfigure400Response from a JSON string
ai_web_search_configure400_response_instance = AiWebSearchConfigure400Response.from_json(json)
# print the JSON string representation of the object
print(AiWebSearchConfigure400Response.to_json())

# convert the object into a dict
ai_web_search_configure400_response_dict = ai_web_search_configure400_response_instance.to_dict()
# create an instance of AiWebSearchConfigure400Response from a dict
ai_web_search_configure400_response_from_dict = AiWebSearchConfigure400Response.from_dict(ai_web_search_configure400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


