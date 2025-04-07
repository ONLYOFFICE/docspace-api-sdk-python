# AdditionalWhiteLabelSettingsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_docs_enabled** | **bool** | Specifies if the start document is enabled or not | [optional] 
**help_center_enabled** | **bool** | Specifies if the help center is enabled or not | [optional] 
**feedback_and_support_enabled** | **bool** | Specifies if feedback and support are available or not | [optional] 
**user_forum_enabled** | **bool** | Specifies if the user forum is enabled or not | [optional] 
**video_guides_enabled** | **bool** | Specifies if the video guides are enabled or not | [optional] 
**license_agreements_enabled** | **bool** | Specifies if the license agreements are enabled or not | [optional] 
**is_default** | **bool** | Specifies if these settings are default or not | [optional] 

## Example

```python
from docspace.models.additional_white_label_settings_dto import AdditionalWhiteLabelSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalWhiteLabelSettingsDto from a JSON string
additional_white_label_settings_dto_instance = AdditionalWhiteLabelSettingsDto.from_json(json)
# print the JSON string representation of the object
print(AdditionalWhiteLabelSettingsDto.to_json())

# convert the object into a dict
additional_white_label_settings_dto_dict = additional_white_label_settings_dto_instance.to_dict()
# create an instance of AdditionalWhiteLabelSettingsDto from a dict
additional_white_label_settings_dto_from_dict = AdditionalWhiteLabelSettingsDto.from_dict(additional_white_label_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


