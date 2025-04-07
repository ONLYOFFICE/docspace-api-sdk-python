# AdditionalWhiteLabelSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_docs_enabled** | **bool** | Specifies if the start document is enabled or not | [optional] 
**help_center_enabled** | **bool** | Specifies if the help center is enabled or not | [optional] 
**feedback_and_support_enabled** | **bool** | Specifies if feedback and support are available or not | [optional] 
**user_forum_enabled** | **bool** | Specifies if the user forum is enabled or not | [optional] 
**video_guides_enabled** | **bool** | Specifies if the video guides are enabled or not | [optional] 
**license_agreements_enabled** | **bool** | Specifies if the license agreements are enabled or not | [optional] 

## Example

```python
from docspace.models.additional_white_label_settings import AdditionalWhiteLabelSettings

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


