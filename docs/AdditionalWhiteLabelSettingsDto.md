# AdditionalWhiteLabelSettingsDto
The additional white label settings parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_docs_enabled** | **bool** | Specifies if the sample documents are displayed or hidden. | [optional] 
**help_center_enabled** | **bool** | Specifies if the Help Center link is available or not. | [optional] 
**feedback_and_support_enabled** | **bool** | Specifies if the \&quot;Feedback &amp; Support\&quot; link is available or not. | [optional] 
**user_forum_enabled** | **bool** | Specifies if the user forum is available or not. | [optional] 
**video_guides_enabled** | **bool** | Specifies if the Video Guides link is available or not. | [optional] 
**license_agreements_enabled** | **bool** | Specifies if the License Agreements link is available or not. | [optional] 
**is_default** | **bool** | Specifies if the additional white label settings are default or not. | [optional] 

## Example

```python
from docspace_api_sdk.models.additional_white_label_settings_dto import AdditionalWhiteLabelSettingsDto

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


