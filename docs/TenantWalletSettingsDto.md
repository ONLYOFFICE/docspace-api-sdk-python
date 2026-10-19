# TenantWalletSettingsDto
The automatic wallet top-up settings of the portal, together with the low-balance warning state the portal keeps  for them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether the payment method on file is charged automatically when the wallet balance runs low. | [optional] 
**min_balance** | **int** | The balance below which a top-up is charged, in `currency`; 0 while top-up has never been configured. | [optional] 
**up_to_balance** | **int** | The balance a top-up brings the wallet up to, in `currency`; 0 while top-up has never been configured. | [optional] 
**currency** | **str** | The three-letter ISO 4217 code both amounts are expressed in, or `null` while top-up has never been configured. | [optional] 
**low_balance_threshold** | **int** | The wallet balance below which the portal sends its low-balance warning. The portal maintains it; it cannot be  set by a request. | [optional] 
**low_balance_notified** | **bool** | Whether the low-balance warning has already been sent for the current dip below `lowBalanceThreshold`. The  portal maintains it, and switching top-up on re-arms it. | [optional] 
**last_modified** | **datetime** | When the settings were last stored; when they were never stored, the moment they were read instead. | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_wallet_settings_dto import TenantWalletSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantWalletSettingsDto from a JSON string
tenant_wallet_settings_dto_instance = TenantWalletSettingsDto.from_json(json)
# print the JSON string representation of the object
print(TenantWalletSettingsDto.to_json())

# convert the object into a dict
tenant_wallet_settings_dto_dict = tenant_wallet_settings_dto_instance.to_dict()
# create an instance of TenantWalletSettingsDto from a dict
tenant_wallet_settings_dto_from_dict = TenantWalletSettingsDto.from_dict(tenant_wallet_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


