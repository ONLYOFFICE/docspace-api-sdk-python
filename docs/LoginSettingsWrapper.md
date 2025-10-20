# LoginSettingsWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**LoginSettingsDto**](LoginSettingsDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.login_settings_wrapper import LoginSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of LoginSettingsWrapper from a JSON string
login_settings_wrapper_instance = LoginSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(LoginSettingsWrapper.to_json())

# convert the object into a dict
login_settings_wrapper_dict = login_settings_wrapper_instance.to_dict()
# create an instance of LoginSettingsWrapper from a dict
login_settings_wrapper_from_dict = LoginSettingsWrapper.from_dict(login_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


