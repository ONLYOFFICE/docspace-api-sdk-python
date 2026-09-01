# LoginSettingsWrapper
The successful API response containing the LoginSettingsDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**LoginSettingsDto**](LoginSettingsDto.md) | The LoginSettingsDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

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


