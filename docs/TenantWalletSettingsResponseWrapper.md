# TenantWalletSettingsResponseWrapper
The successful API response containing the TenantWalletSettings object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**TenantWalletSettings**](TenantWalletSettings.md) | The TenantWalletSettings object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_wallet_settings_response_wrapper import TenantWalletSettingsResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TenantWalletSettingsResponseWrapper from a JSON string
tenant_wallet_settings_response_wrapper_instance = TenantWalletSettingsResponseWrapper.from_json(json)
# print the JSON string representation of the object
print(TenantWalletSettingsResponseWrapper.to_json())

# convert the object into a dict
tenant_wallet_settings_response_wrapper_dict = tenant_wallet_settings_response_wrapper_instance.to_dict()
# create an instance of TenantWalletSettingsResponseWrapper from a dict
tenant_wallet_settings_response_wrapper_from_dict = TenantWalletSettingsResponseWrapper.from_dict(tenant_wallet_settings_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


