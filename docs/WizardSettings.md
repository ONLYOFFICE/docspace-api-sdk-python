# WizardSettings
The Wizard settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **bool** | Specifies if the Wizard settings are completed or not | [optional] 
**last_modified** | **datetime** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.wizard_settings import WizardSettings

# TODO update the JSON string below
json = "{}"
# create an instance of WizardSettings from a JSON string
wizard_settings_instance = WizardSettings.from_json(json)
# print the JSON string representation of the object
print(WizardSettings.to_json())

# convert the object into a dict
wizard_settings_dict = wizard_settings_instance.to_dict()
# create an instance of WizardSettings from a dict
wizard_settings_from_dict = WizardSettings.from_dict(wizard_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


