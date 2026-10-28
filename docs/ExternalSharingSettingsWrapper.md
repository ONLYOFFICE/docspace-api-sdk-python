# ExternalSharingSettingsWrapper
The successful API response containing the ExternalSharingSettingsDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ExternalSharingSettingsDto**](ExternalSharingSettingsDto.md) | The ExternalSharingSettingsDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.external_sharing_settings_wrapper import ExternalSharingSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalSharingSettingsWrapper from a JSON string
external_sharing_settings_wrapper_instance = ExternalSharingSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(ExternalSharingSettingsWrapper.to_json())

# convert the object into a dict
external_sharing_settings_wrapper_dict = external_sharing_settings_wrapper_instance.to_dict()
# create an instance of ExternalSharingSettingsWrapper from a dict
external_sharing_settings_wrapper_from_dict = ExternalSharingSettingsWrapper.from_dict(external_sharing_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


