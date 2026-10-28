# AiPreferencesSetToolPermissionModeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**AiChatToolPermissionMode**](AiChatToolPermissionMode.md) | New tool permission mode. | 
**entity_id** | **str** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_preferences_set_tool_permission_mode_request import AiPreferencesSetToolPermissionModeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiPreferencesSetToolPermissionModeRequest from a JSON string
ai_preferences_set_tool_permission_mode_request_instance = AiPreferencesSetToolPermissionModeRequest.from_json(json)
# print the JSON string representation of the object
print(AiPreferencesSetToolPermissionModeRequest.to_json())

# convert the object into a dict
ai_preferences_set_tool_permission_mode_request_dict = ai_preferences_set_tool_permission_mode_request_instance.to_dict()
# create an instance of AiPreferencesSetToolPermissionModeRequest from a dict
ai_preferences_set_tool_permission_mode_request_from_dict = AiPreferencesSetToolPermissionModeRequest.from_dict(ai_preferences_set_tool_permission_mode_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


