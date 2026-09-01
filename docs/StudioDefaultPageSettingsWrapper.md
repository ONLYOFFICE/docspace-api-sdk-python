# StudioDefaultPageSettingsWrapper
The successful API response containing the StudioDefaultPageSettings object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**StudioDefaultPageSettings**](StudioDefaultPageSettings.md) | The StudioDefaultPageSettings object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.studio_default_page_settings_wrapper import StudioDefaultPageSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of StudioDefaultPageSettingsWrapper from a JSON string
studio_default_page_settings_wrapper_instance = StudioDefaultPageSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(StudioDefaultPageSettingsWrapper.to_json())

# convert the object into a dict
studio_default_page_settings_wrapper_dict = studio_default_page_settings_wrapper_instance.to_dict()
# create an instance of StudioDefaultPageSettingsWrapper from a dict
studio_default_page_settings_wrapper_from_dict = StudioDefaultPageSettingsWrapper.from_dict(studio_default_page_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


