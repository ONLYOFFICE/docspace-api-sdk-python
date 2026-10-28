# DefaultTemplateSettingsRequestDtoSelectedFile
The document to copy as the blank: a number for a file stored in the portal, a string for one in a connected  third-party storage. Take the identifier from a folder listing such as `GET api/2.0/files/{folderId}`; the  caller must be allowed to copy that file, and its extension must be the one named below.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from docspace_api_sdk.models.default_template_settings_request_dto_selected_file import DefaultTemplateSettingsRequestDtoSelectedFile

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultTemplateSettingsRequestDtoSelectedFile from a JSON string
default_template_settings_request_dto_selected_file_instance = DefaultTemplateSettingsRequestDtoSelectedFile.from_json(json)
# print the JSON string representation of the object
print(DefaultTemplateSettingsRequestDtoSelectedFile.to_json())

# convert the object into a dict
default_template_settings_request_dto_selected_file_dict = default_template_settings_request_dto_selected_file_instance.to_dict()
# create an instance of DefaultTemplateSettingsRequestDtoSelectedFile from a dict
default_template_settings_request_dto_selected_file_from_dict = DefaultTemplateSettingsRequestDtoSelectedFile.from_dict(default_template_settings_request_dto_selected_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


