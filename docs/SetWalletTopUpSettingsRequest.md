# SetWalletTopUpSettingsRequest
The part of the automatic top-up settings a payer chooses. The low-balance warning state is kept by the portal  itself and cannot be set here.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether the payment method on file is charged automatically when the wallet balance runs low. | [optional] 
**min_balance** | **int** | The balance below which a top-up is charged, in `currency`. | [optional] 
**up_to_balance** | **int** | The balance a top-up brings the wallet up to, in `currency`. | [optional] 
**currency** | **str** | The three-letter ISO 4217 code both amounts are expressed in; it has to be the currency of the wallet. | [optional] 
**low_balance_threshold** | **int** | Accepted for compatibility with earlier clients and not read: the server keeps its own value. | [optional] 
**low_balance_notified** | **bool** | Accepted for compatibility with earlier clients and not read: the server keeps its own value. | [optional] 
**last_modified** | **datetime** | Accepted for compatibility with earlier clients and not read: the server keeps its own value. | [optional] 

## Example

```python
from docspace_api_sdk.models.set_wallet_top_up_settings_request import SetWalletTopUpSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetWalletTopUpSettingsRequest from a JSON string
set_wallet_top_up_settings_request_instance = SetWalletTopUpSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(SetWalletTopUpSettingsRequest.to_json())

# convert the object into a dict
set_wallet_top_up_settings_request_dict = set_wallet_top_up_settings_request_instance.to_dict()
# create an instance of SetWalletTopUpSettingsRequest from a dict
set_wallet_top_up_settings_request_from_dict = SetWalletTopUpSettingsRequest.from_dict(set_wallet_top_up_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


