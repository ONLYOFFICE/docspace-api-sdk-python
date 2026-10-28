# WizardSettingsDto
The state of the portal's first-run setup wizard.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **bool** | Specifies if the Wizard settings are completed or not | [optional] 
**last_modified** | **datetime** | The timestamp indicating when the settings were last modified. | [optional] 

## Example

```python
from docspace_api_sdk.models.wizard_settings_dto import WizardSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of WizardSettingsDto from a JSON string
wizard_settings_dto_instance = WizardSettingsDto.from_json(json)
# print the JSON string representation of the object
print(WizardSettingsDto.to_json())

# convert the object into a dict
wizard_settings_dto_dict = wizard_settings_dto_instance.to_dict()
# create an instance of WizardSettingsDto from a dict
wizard_settings_dto_from_dict = WizardSettingsDto.from_dict(wizard_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


