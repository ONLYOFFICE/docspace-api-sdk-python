# DefaultTemplateSettingsDto
Default templates settings parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DefaultTemplateItemDto]**](DefaultTemplateItemDto.md) | Default templates list. | 

## Example

```python
from docspace_api_sdk.models.default_template_settings_dto import DefaultTemplateSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultTemplateSettingsDto from a JSON string
default_template_settings_dto_instance = DefaultTemplateSettingsDto.from_json(json)
# print the JSON string representation of the object
print(DefaultTemplateSettingsDto.to_json())

# convert the object into a dict
default_template_settings_dto_dict = default_template_settings_dto_instance.to_dict()
# create an instance of DefaultTemplateSettingsDto from a dict
default_template_settings_dto_from_dict = DefaultTemplateSettingsDto.from_dict(default_template_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


