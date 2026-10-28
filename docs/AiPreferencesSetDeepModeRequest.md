# AiPreferencesSetDeepModeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **bool** | New deep-mode value. | 
**entity_id** | **str** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_preferences_set_deep_mode_request import AiPreferencesSetDeepModeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiPreferencesSetDeepModeRequest from a JSON string
ai_preferences_set_deep_mode_request_instance = AiPreferencesSetDeepModeRequest.from_json(json)
# print the JSON string representation of the object
print(AiPreferencesSetDeepModeRequest.to_json())

# convert the object into a dict
ai_preferences_set_deep_mode_request_dict = ai_preferences_set_deep_mode_request_instance.to_dict()
# create an instance of AiPreferencesSetDeepModeRequest from a dict
ai_preferences_set_deep_mode_request_from_dict = AiPreferencesSetDeepModeRequest.from_dict(ai_preferences_set_deep_mode_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


