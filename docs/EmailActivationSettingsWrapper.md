# EmailActivationSettingsWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**EmailActivationSettings**](EmailActivationSettings.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.email_activation_settings_wrapper import EmailActivationSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of EmailActivationSettingsWrapper from a JSON string
email_activation_settings_wrapper_instance = EmailActivationSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(EmailActivationSettingsWrapper.to_json())

# convert the object into a dict
email_activation_settings_wrapper_dict = email_activation_settings_wrapper_instance.to_dict()
# create an instance of EmailActivationSettingsWrapper from a dict
email_activation_settings_wrapper_from_dict = EmailActivationSettingsWrapper.from_dict(email_activation_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


