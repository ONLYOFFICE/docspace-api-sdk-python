# IpRestrictionsSettingsWrapper
The successful API response containing the IpRestrictionsSettingsDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**IpRestrictionsSettingsDto**](IpRestrictionsSettingsDto.md) | The IpRestrictionsSettingsDto object returned by the operation. | [optional] 
**count** | **int** | How many items this response carries: the length of the page for a list, 1 for a single object | [optional] 
**total** | **int** | How many items the whole list holds across all pages, for working out how many pages to request. Sent only by the operations that page their results, and left out of every other response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.ip_restrictions_settings_wrapper import IpRestrictionsSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of IpRestrictionsSettingsWrapper from a JSON string
ip_restrictions_settings_wrapper_instance = IpRestrictionsSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(IpRestrictionsSettingsWrapper.to_json())

# convert the object into a dict
ip_restrictions_settings_wrapper_dict = ip_restrictions_settings_wrapper_instance.to_dict()
# create an instance of IpRestrictionsSettingsWrapper from a dict
ip_restrictions_settings_wrapper_from_dict = IpRestrictionsSettingsWrapper.from_dict(ip_restrictions_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


