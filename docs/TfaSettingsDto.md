# TfaSettingsDto
The parameters representing the Two-Factor Authentication (TFA) configuration settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the TFA configuration. | [optional] 
**title** | **str** | The display name or description of the TFA configuration. | [optional] 
**enabled** | **bool** | Indicates whether the TFA configuration is currently active. | [optional] 
**avaliable** | **bool** | Indicates whether the TFA configuration can be used. | [optional] 
**trusted_ips** | **List[str]** | The list of IP addresses that are exempt from TFA requirements. | [optional] 
**mandatory_users** | **List[str]** | The list of user IDs that are required to use TFA. | [optional] 
**mandatory_groups** | **List[str]** | The list of group IDs whose members are required to use TFA. | [optional] 

## Example

```python
from docspace-api-sdk.models.tfa_settings_dto import TfaSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TfaSettingsDto from a JSON string
tfa_settings_dto_instance = TfaSettingsDto.from_json(json)
# print the JSON string representation of the object
print(TfaSettingsDto.to_json())

# convert the object into a dict
tfa_settings_dto_dict = tfa_settings_dto_instance.to_dict()
# create an instance of TfaSettingsDto from a dict
tfa_settings_dto_from_dict = TfaSettingsDto.from_dict(tfa_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


