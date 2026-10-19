# TenantWalletSettingsRequestDto
The body of an automatic top-up settings change.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**SetWalletTopUpSettingsRequest**](SetWalletTopUpSettingsRequest.md) | The automatic top-up settings to store. | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_wallet_settings_request_dto import TenantWalletSettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantWalletSettingsRequestDto from a JSON string
tenant_wallet_settings_request_dto_instance = TenantWalletSettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(TenantWalletSettingsRequestDto.to_json())

# convert the object into a dict
tenant_wallet_settings_request_dto_dict = tenant_wallet_settings_request_dto_instance.to_dict()
# create an instance of TenantWalletSettingsRequestDto from a dict
tenant_wallet_settings_request_dto_from_dict = TenantWalletSettingsRequestDto.from_dict(tenant_wallet_settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


