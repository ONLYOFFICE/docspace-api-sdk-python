# AdditionalWhiteLabelSettingsWrapper
The additional white label settings wrapper.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**AdditionalWhiteLabelSettings**](AdditionalWhiteLabelSettings.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.additional_white_label_settings_wrapper import AdditionalWhiteLabelSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalWhiteLabelSettingsWrapper from a JSON string
additional_white_label_settings_wrapper_instance = AdditionalWhiteLabelSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(AdditionalWhiteLabelSettingsWrapper.to_json())

# convert the object into a dict
additional_white_label_settings_wrapper_dict = additional_white_label_settings_wrapper_instance.to_dict()
# create an instance of AdditionalWhiteLabelSettingsWrapper from a dict
additional_white_label_settings_wrapper_from_dict = AdditionalWhiteLabelSettingsWrapper.from_dict(additional_white_label_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


