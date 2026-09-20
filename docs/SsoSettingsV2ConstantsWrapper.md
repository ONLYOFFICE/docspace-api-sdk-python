# SsoSettingsV2ConstantsWrapper
The successful API response containing the SsoSettingsV2ConstantsDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**SsoSettingsV2ConstantsDto**](SsoSettingsV2ConstantsDto.md) | The SsoSettingsV2ConstantsDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.sso_settings_v2_constants_wrapper import SsoSettingsV2ConstantsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of SsoSettingsV2ConstantsWrapper from a JSON string
sso_settings_v2_constants_wrapper_instance = SsoSettingsV2ConstantsWrapper.from_json(json)
# print the JSON string representation of the object
print(SsoSettingsV2ConstantsWrapper.to_json())

# convert the object into a dict
sso_settings_v2_constants_wrapper_dict = sso_settings_v2_constants_wrapper_instance.to_dict()
# create an instance of SsoSettingsV2ConstantsWrapper from a dict
sso_settings_v2_constants_wrapper_from_dict = SsoSettingsV2ConstantsWrapper.from_dict(sso_settings_v2_constants_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


