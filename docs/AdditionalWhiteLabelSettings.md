# AdditionalWhiteLabelSettings
The additional white label settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_docs_enabled** | **bool** | Specifies if the sample documents are displayed or hidden. | [optional] 
**help_center_enabled** | **bool** | Specifies if the Help Center link is available or not. | [optional] 
**feedback_and_support_enabled** | **bool** | Specifies if the \&quot;Feedback &amp; Support\&quot; link is available or not. | [optional] 
**user_forum_enabled** | **bool** | Specifies if the user forum is available or not. | [optional] 
**video_guides_enabled** | **bool** | Specifies if the Video Guides link is available or not. | [optional] 
**license_agreements_enabled** | **bool** | Specifies if the License Agreements link is available or not. | [optional] 
**last_modified** | **datetime** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.additional_white_label_settings import AdditionalWhiteLabelSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalWhiteLabelSettings from a JSON string
additional_white_label_settings_instance = AdditionalWhiteLabelSettings.from_json(json)
# print the JSON string representation of the object
print(AdditionalWhiteLabelSettings.to_json())

# convert the object into a dict
additional_white_label_settings_dict = additional_white_label_settings_instance.to_dict()
# create an instance of AdditionalWhiteLabelSettings from a dict
additional_white_label_settings_from_dict = AdditionalWhiteLabelSettings.from_dict(additional_white_label_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


