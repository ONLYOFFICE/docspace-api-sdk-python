# SsoSettingsV2Wrapper
The successful API response containing the SsoSettingsV2 object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**SsoSettingsV2**](SsoSettingsV2.md) | The SsoSettingsV2 object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.sso_settings_v2_wrapper import SsoSettingsV2Wrapper

# TODO update the JSON string below
json = "{}"
# create an instance of SsoSettingsV2Wrapper from a JSON string
sso_settings_v2_wrapper_instance = SsoSettingsV2Wrapper.from_json(json)
# print the JSON string representation of the object
print(SsoSettingsV2Wrapper.to_json())

# convert the object into a dict
sso_settings_v2_wrapper_dict = sso_settings_v2_wrapper_instance.to_dict()
# create an instance of SsoSettingsV2Wrapper from a dict
sso_settings_v2_wrapper_from_dict = SsoSettingsV2Wrapper.from_dict(sso_settings_v2_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


