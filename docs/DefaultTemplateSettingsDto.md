# DefaultTemplateSettingsDto
The blank document the portal creates for each extension it covers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DefaultTemplateItemDto]**](DefaultTemplateItemDto.md) | One entry per extension the portal's built-in template set covers, whether or not a custom blank has been  chosen for it, so the list is never empty and its length follows the template set rather than the number of  custom blanks. Entries come in the order an interface shows them: text document, spreadsheet, presentation and  PDF first, everything else by extension. | 

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


