# StudioDefaultPageSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_folder_type** | [**FolderType**](FolderType.md) | Specifies the type of the default folder associated with the settings. | [optional] 
**last_modified** | **datetime** | The timestamp indicating when the settings were last modified. | [optional] 

## Example

```python
from docspace_api_sdk.models.studio_default_page_settings import StudioDefaultPageSettings

# TODO update the JSON string below
json = "{}"
# create an instance of StudioDefaultPageSettings from a JSON string
studio_default_page_settings_instance = StudioDefaultPageSettings.from_json(json)
# print the JSON string representation of the object
print(StudioDefaultPageSettings.to_json())

# convert the object into a dict
studio_default_page_settings_dict = studio_default_page_settings_instance.to_dict()
# create an instance of StudioDefaultPageSettings from a dict
studio_default_page_settings_from_dict = StudioDefaultPageSettings.from_dict(studio_default_page_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


