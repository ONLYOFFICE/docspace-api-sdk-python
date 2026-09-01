# StorageSettingsWrapper
The successful API response containing the StorageSettings object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**StorageSettings**](StorageSettings.md) | The StorageSettings object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.storage_settings_wrapper import StorageSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of StorageSettingsWrapper from a JSON string
storage_settings_wrapper_instance = StorageSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(StorageSettingsWrapper.to_json())

# convert the object into a dict
storage_settings_wrapper_dict = storage_settings_wrapper_instance.to_dict()
# create an instance of StorageSettingsWrapper from a dict
storage_settings_wrapper_from_dict = StorageSettingsWrapper.from_dict(storage_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


