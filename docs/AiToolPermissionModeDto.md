# AiToolPermissionModeDto
The current user's tool permission mode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | [**AiToolPermissionMode**](AiToolPermissionMode.md) | How tool calls made by the model are approved for the current user. The default applies while the user has stored nothing. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_tool_permission_mode_dto import AiToolPermissionModeDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiToolPermissionModeDto from a JSON string
ai_tool_permission_mode_dto_instance = AiToolPermissionModeDto.from_json(json)
# print the JSON string representation of the object
print(AiToolPermissionModeDto.to_json())

# convert the object into a dict
ai_tool_permission_mode_dto_dict = ai_tool_permission_mode_dto_instance.to_dict()
# create an instance of AiToolPermissionModeDto from a dict
ai_tool_permission_mode_dto_from_dict = AiToolPermissionModeDto.from_dict(ai_tool_permission_mode_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


