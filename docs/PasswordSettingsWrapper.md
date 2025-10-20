# PasswordSettingsWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**PasswordSettingsDto**](PasswordSettingsDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.password_settings_wrapper import PasswordSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordSettingsWrapper from a JSON string
password_settings_wrapper_instance = PasswordSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(PasswordSettingsWrapper.to_json())

# convert the object into a dict
password_settings_wrapper_dict = password_settings_wrapper_instance.to_dict()
# create an instance of PasswordSettingsWrapper from a dict
password_settings_wrapper_from_dict = PasswordSettingsWrapper.from_dict(password_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


