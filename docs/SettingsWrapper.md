# SettingsWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**SettingsDto**](SettingsDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.settings_wrapper import SettingsWrapper

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


