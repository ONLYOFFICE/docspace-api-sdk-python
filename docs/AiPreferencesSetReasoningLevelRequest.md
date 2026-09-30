# AiPreferencesSetReasoningLevelRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**AiAiReasoningLevel**](AiAiReasoningLevel.md) | New extended-thinking depth; `off` turns deep mode off. | 
**entity_id** | **str** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_preferences_set_reasoning_level_request import AiPreferencesSetReasoningLevelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiPreferencesSetReasoningLevelRequest from a JSON string
ai_preferences_set_reasoning_level_request_instance = AiPreferencesSetReasoningLevelRequest.from_json(json)
# print the JSON string representation of the object
print(AiPreferencesSetReasoningLevelRequest.to_json())

# convert the object into a dict
ai_preferences_set_reasoning_level_request_dict = ai_preferences_set_reasoning_level_request_instance.to_dict()
# create an instance of AiPreferencesSetReasoningLevelRequest from a dict
ai_preferences_set_reasoning_level_request_from_dict = AiPreferencesSetReasoningLevelRequest.from_dict(ai_preferences_set_reasoning_level_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


