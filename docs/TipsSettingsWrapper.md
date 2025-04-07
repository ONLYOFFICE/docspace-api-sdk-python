# TipsSettingsWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**TipsSettings**](TipsSettings.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.tips_settings_wrapper import TipsSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TipsSettingsWrapper from a JSON string
tips_settings_wrapper_instance = TipsSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(TipsSettingsWrapper.to_json())

# convert the object into a dict
tips_settings_wrapper_dict = tips_settings_wrapper_instance.to_dict()
# create an instance of TipsSettingsWrapper from a dict
tips_settings_wrapper_from_dict = TipsSettingsWrapper.from_dict(tips_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


