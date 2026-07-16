# SetAiUserSettingsRequestDto
Request to update per-user AI recommended model visibility settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_recommended_model_visible** | **bool** | Indicates whether the recommended model banner is visible in the AI chat. | [optional] 

## Example

```python
from docspace_api_sdk.models.set_ai_user_settings_request_dto import SetAiUserSettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SetAiUserSettingsRequestDto from a JSON string
set_ai_user_settings_request_dto_instance = SetAiUserSettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(SetAiUserSettingsRequestDto.to_json())

# convert the object into a dict
set_ai_user_settings_request_dto_dict = set_ai_user_settings_request_dto_instance.to_dict()
# create an instance of SetAiUserSettingsRequestDto from a dict
set_ai_user_settings_request_dto_from_dict = SetAiUserSettingsRequestDto.from_dict(set_ai_user_settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


