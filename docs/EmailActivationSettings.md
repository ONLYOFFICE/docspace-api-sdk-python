# EmailActivationSettings
The email activation settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**show** | **bool** | Specifies whether the email activation settings is shown or hidden. | [optional] 
**last_modified** | **datetime** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.email_activation_settings import EmailActivationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of EmailActivationSettings from a JSON string
email_activation_settings_instance = EmailActivationSettings.from_json(json)
# print the JSON string representation of the object
print(EmailActivationSettings.to_json())

# convert the object into a dict
email_activation_settings_dict = email_activation_settings_instance.to_dict()
# create an instance of EmailActivationSettings from a dict
email_activation_settings_from_dict = EmailActivationSettings.from_dict(email_activation_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


