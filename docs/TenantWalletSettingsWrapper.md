# TenantWalletSettingsWrapper
Tenant wallet settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**TenantWalletSettings**](TenantWalletSettings.md) |  | [optional] 

## Example

```python
from docspace-api-sdk.models.tenant_wallet_settings_wrapper import TenantWalletSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TenantWalletSettingsWrapper from a JSON string
tenant_wallet_settings_wrapper_instance = TenantWalletSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(TenantWalletSettingsWrapper.to_json())

# convert the object into a dict
tenant_wallet_settings_wrapper_dict = tenant_wallet_settings_wrapper_instance.to_dict()
# create an instance of TenantWalletSettingsWrapper from a dict
tenant_wallet_settings_wrapper_from_dict = TenantWalletSettingsWrapper.from_dict(tenant_wallet_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


