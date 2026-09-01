# CdnStorageSettingsWrapper
The successful API response containing the CdnStorageSettings object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CdnStorageSettings**](CdnStorageSettings.md) | The CdnStorageSettings object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.cdn_storage_settings_wrapper import CdnStorageSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of CdnStorageSettingsWrapper from a JSON string
cdn_storage_settings_wrapper_instance = CdnStorageSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(CdnStorageSettingsWrapper.to_json())

# convert the object into a dict
cdn_storage_settings_wrapper_dict = cdn_storage_settings_wrapper_instance.to_dict()
# create an instance of CdnStorageSettingsWrapper from a dict
cdn_storage_settings_wrapper_from_dict = CdnStorageSettingsWrapper.from_dict(cdn_storage_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


