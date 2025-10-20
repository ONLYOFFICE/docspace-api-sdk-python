# TenantWalletServiceSettings
The wallet services settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled_services** | **List[int]** | The list of the enabled wallet services. | [optional] 
**last_modified** | **datetime** | The date and time when the wallet services settings were last modified. | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_wallet_service_settings import TenantWalletServiceSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TenantWalletServiceSettings from a JSON string
tenant_wallet_service_settings_instance = TenantWalletServiceSettings.from_json(json)
# print the JSON string representation of the object
print(TenantWalletServiceSettings.to_json())

# convert the object into a dict
tenant_wallet_service_settings_dict = tenant_wallet_service_settings_instance.to_dict()
# create an instance of TenantWalletServiceSettings from a dict
tenant_wallet_service_settings_from_dict = TenantWalletServiceSettings.from_dict(tenant_wallet_service_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


