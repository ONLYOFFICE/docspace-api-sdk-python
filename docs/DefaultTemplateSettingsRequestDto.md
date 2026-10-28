# DefaultTemplateSettingsRequestDto
The document to use as the blank the portal creates for one extension.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_file** | [**DefaultTemplateSettingsRequestDtoSelectedFile**](DefaultTemplateSettingsRequestDtoSelectedFile.md) |  | 
**file_extension** | **str** | The extension the blank is set for, written in lower case with the leading dot. Only the extensions the  portal's built-in template set covers are accepted, and `GET api/2.0/files/settings/defaulttemplate` returns  exactly that list; an extension outside it leaves the settings unchanged instead of failing. | 

## Example

```python
from docspace_api_sdk.models.default_template_settings_request_dto import DefaultTemplateSettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultTemplateSettingsRequestDto from a JSON string
default_template_settings_request_dto_instance = DefaultTemplateSettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(DefaultTemplateSettingsRequestDto.to_json())

# convert the object into a dict
default_template_settings_request_dto_dict = default_template_settings_request_dto_instance.to_dict()
# create an instance of DefaultTemplateSettingsRequestDto from a dict
default_template_settings_request_dto_from_dict = DefaultTemplateSettingsRequestDto.from_dict(default_template_settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


