# TenantWalletSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enabled | [optional] 
**min_balance** | **int** | Minimun balance | [optional] 
**up_to_balance** | **int** | Up to balance | [optional] 
**currency** | **str** | The three-character ISO 4217 currency symbol. | [optional] 
**last_modified** | **datetime** |  | [optional] 

## Example

```python
from docspace.models.tenant_wallet_settings import TenantWalletSettings

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


