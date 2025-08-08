# CookieSettingsWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CookieSettingsDto**](CookieSettingsDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.cookie_settings_wrapper import CookieSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of CookieSettingsWrapper from a JSON string
cookie_settings_wrapper_instance = CookieSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(CookieSettingsWrapper.to_json())

# convert the object into a dict
cookie_settings_wrapper_dict = cookie_settings_wrapper_instance.to_dict()
# create an instance of CookieSettingsWrapper from a dict
cookie_settings_wrapper_from_dict = CookieSettingsWrapper.from_dict(cookie_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


