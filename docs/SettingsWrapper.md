# SettingsWrapper
The successful API response containing the SettingsDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**SettingsDto**](SettingsDto.md) | The SettingsDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.settings_wrapper import SettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsWrapper from a JSON string
settings_wrapper_instance = SettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(SettingsWrapper.to_json())

# convert the object into a dict
settings_wrapper_dict = settings_wrapper_instance.to_dict()
# create an instance of SettingsWrapper from a dict
settings_wrapper_from_dict = SettingsWrapper.from_dict(settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


