# SsoSettingsWrapper
The successful API response containing the SsoSettingsDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**SsoSettingsDto**](SsoSettingsDto.md) | The SsoSettingsDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.sso_settings_wrapper import SsoSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of SsoSettingsWrapper from a JSON string
sso_settings_wrapper_instance = SsoSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(SsoSettingsWrapper.to_json())

# convert the object into a dict
sso_settings_wrapper_dict = sso_settings_wrapper_instance.to_dict()
# create an instance of SsoSettingsWrapper from a dict
sso_settings_wrapper_from_dict = SsoSettingsWrapper.from_dict(sso_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


