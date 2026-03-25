# DefaultTemplateSettingsResetRequestDto
Default templates settings reset request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_extension** | **str** | File extension of a template to reset | 

## Example

```python
from docspace_api_sdk.models.default_template_settings_reset_request_dto import DefaultTemplateSettingsResetRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultTemplateSettingsResetRequestDto from a JSON string
default_template_settings_reset_request_dto_instance = DefaultTemplateSettingsResetRequestDto.from_json(json)
# print the JSON string representation of the object
print(DefaultTemplateSettingsResetRequestDto.to_json())

# convert the object into a dict
default_template_settings_reset_request_dto_dict = default_template_settings_reset_request_dto_instance.to_dict()
# create an instance of DefaultTemplateSettingsResetRequestDto from a dict
default_template_settings_reset_request_dto_from_dict = DefaultTemplateSettingsResetRequestDto.from_dict(default_template_settings_reset_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


