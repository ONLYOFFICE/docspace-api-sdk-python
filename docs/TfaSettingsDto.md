# TfaSettingsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**title** | **str** | Title | [optional] 
**enabled** | **bool** | Specifies if the TFA settings are enabled or not | [optional] 
**avaliable** | **bool** | Specifies if the TFA settings are available or not | [optional] 
**trusted_ips** | **List[str]** | List of trusted IP addresses | [optional] 
**mandatory_users** | **List[str]** | List of users who must use the TFA verification | [optional] 
**mandatory_groups** | **List[str]** | List of groups who must use the TFA verification | [optional] 

## Example

```python
from docspace.models.tfa_settings_dto import TfaSettingsDto

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


