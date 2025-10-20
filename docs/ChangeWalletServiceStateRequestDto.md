# ChangeWalletServiceStateRequestDto
The request parameters for changing the tenant wallet service state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | [**TenantWalletService**](TenantWalletService.md) |  | [optional] 
**enabled** | **bool** | Specifies whether the wallet service is enabled. | [optional] 

## Example

```python
from docspace_api_sdk.models.change_wallet_service_state_request_dto import ChangeWalletServiceStateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeWalletServiceStateRequestDto from a JSON string
change_wallet_service_state_request_dto_instance = ChangeWalletServiceStateRequestDto.from_json(json)
# print the JSON string representation of the object
print(ChangeWalletServiceStateRequestDto.to_json())

# convert the object into a dict
change_wallet_service_state_request_dto_dict = change_wallet_service_state_request_dto_instance.to_dict()
# create an instance of ChangeWalletServiceStateRequestDto from a dict
change_wallet_service_state_request_dto_from_dict = ChangeWalletServiceStateRequestDto.from_dict(change_wallet_service_state_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


