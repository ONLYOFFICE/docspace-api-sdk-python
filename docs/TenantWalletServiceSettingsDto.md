# TenantWalletServiceSettingsDto
The wallet services an administrator switched on for the portal by hand.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled_services** | **List[int]** | The list of the enabled wallet services. | [optional] 
**last_modified** | **datetime** | The date and time when the wallet services settings were last modified. | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_wallet_service_settings_dto import TenantWalletServiceSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantWalletServiceSettingsDto from a JSON string
tenant_wallet_service_settings_dto_instance = TenantWalletServiceSettingsDto.from_json(json)
# print the JSON string representation of the object
print(TenantWalletServiceSettingsDto.to_json())

# convert the object into a dict
tenant_wallet_service_settings_dto_dict = tenant_wallet_service_settings_dto_instance.to_dict()
# create an instance of TenantWalletServiceSettingsDto from a dict
tenant_wallet_service_settings_dto_from_dict = TenantWalletServiceSettingsDto.from_dict(tenant_wallet_service_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


