# TfaSettingsArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[TfaSettingsDto]**](TfaSettingsDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.tfa_settings_array_wrapper import TfaSettingsArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TfaSettingsArrayWrapper from a JSON string
tfa_settings_array_wrapper_instance = TfaSettingsArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(TfaSettingsArrayWrapper.to_json())

# convert the object into a dict
tfa_settings_array_wrapper_dict = tfa_settings_array_wrapper_instance.to_dict()
# create an instance of TfaSettingsArrayWrapper from a dict
tfa_settings_array_wrapper_from_dict = TfaSettingsArrayWrapper.from_dict(tfa_settings_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


