# SsoSettingsV2Wrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**SsoSettingsV2**](SsoSettingsV2.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.sso_settings_v2_wrapper import SsoSettingsV2Wrapper

# TODO update the JSON string below
json = "{}"
# create an instance of SsoSettingsV2Wrapper from a JSON string
sso_settings_v2_wrapper_instance = SsoSettingsV2Wrapper.from_json(json)
# print the JSON string representation of the object
print(SsoSettingsV2Wrapper.to_json())

# convert the object into a dict
sso_settings_v2_wrapper_dict = sso_settings_v2_wrapper_instance.to_dict()
# create an instance of SsoSettingsV2Wrapper from a dict
sso_settings_v2_wrapper_from_dict = SsoSettingsV2Wrapper.from_dict(sso_settings_v2_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


