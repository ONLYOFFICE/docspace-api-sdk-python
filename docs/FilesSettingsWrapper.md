# FilesSettingsWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FilesSettingsDto**](FilesSettingsDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.files_settings_wrapper import FilesSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FilesSettingsWrapper from a JSON string
files_settings_wrapper_instance = FilesSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(FilesSettingsWrapper.to_json())

# convert the object into a dict
files_settings_wrapper_dict = files_settings_wrapper_instance.to_dict()
# create an instance of FilesSettingsWrapper from a dict
files_settings_wrapper_from_dict = FilesSettingsWrapper.from_dict(files_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


