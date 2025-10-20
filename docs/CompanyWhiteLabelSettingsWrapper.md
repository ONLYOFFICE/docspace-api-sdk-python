# CompanyWhiteLabelSettingsWrapper
The company white label settings wrapper.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**CompanyWhiteLabelSettings**](CompanyWhiteLabelSettings.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.company_white_label_settings_wrapper import CompanyWhiteLabelSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyWhiteLabelSettingsWrapper from a JSON string
company_white_label_settings_wrapper_instance = CompanyWhiteLabelSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(CompanyWhiteLabelSettingsWrapper.to_json())

# convert the object into a dict
company_white_label_settings_wrapper_dict = company_white_label_settings_wrapper_instance.to_dict()
# create an instance of CompanyWhiteLabelSettingsWrapper from a dict
company_white_label_settings_wrapper_from_dict = CompanyWhiteLabelSettingsWrapper.from_dict(company_white_label_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


