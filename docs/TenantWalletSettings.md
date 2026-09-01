# TenantWalletSettings
The tenant wallet settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Specifies whether automatic top-up for the tenant wallet is enabled. | [optional] 
**min_balance** | **int** | The minimum wallet balance at which automatic top-up will be triggered. Must be between 5 and 1000. | [optional] 
**up_to_balance** | **int** | The maximum wallet balance at which automatic top-up will be triggered. Must be between 6 and 5000. | [optional] 
**currency** | **str** | The three-character ISO 4217 currency symbol. | [optional] 
**low_balance_threshold** | **int** | The wallet balance below which a low-balance notification is sent. Set internally, not user-configurable. | [optional] 
**low_balance_notified** | **bool** | Specifies whether a low-balance notification has already been sent for the current dip below ASC.Core.Tenants.TenantWalletSettings.LowBalanceThreshold. | [optional] 
**last_modified** | **datetime** | The date and time when the tenant wallet settings were last modified. | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_wallet_settings import TenantWalletSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TenantWalletSettings from a JSON string
tenant_wallet_settings_instance = TenantWalletSettings.from_json(json)
# print the JSON string representation of the object
print(TenantWalletSettings.to_json())

# convert the object into a dict
tenant_wallet_settings_dict = tenant_wallet_settings_instance.to_dict()
# create an instance of TenantWalletSettings from a dict
tenant_wallet_settings_from_dict = TenantWalletSettings.from_dict(tenant_wallet_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


