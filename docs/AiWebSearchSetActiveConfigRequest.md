# AiWebSearchSetActiveConfigRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**AiWebSearchConfig**](AiWebSearchConfig.md) |  | 
**entity_id** | **str** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_web_search_set_active_config_request import AiWebSearchSetActiveConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiWebSearchSetActiveConfigRequest from a JSON string
ai_web_search_set_active_config_request_instance = AiWebSearchSetActiveConfigRequest.from_json(json)
# print the JSON string representation of the object
print(AiWebSearchSetActiveConfigRequest.to_json())

# convert the object into a dict
ai_web_search_set_active_config_request_dict = ai_web_search_set_active_config_request_instance.to_dict()
# create an instance of AiWebSearchSetActiveConfigRequest from a dict
ai_web_search_set_active_config_request_from_dict = AiWebSearchSetActiveConfigRequest.from_dict(ai_web_search_set_active_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


