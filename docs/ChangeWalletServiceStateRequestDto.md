# ChangeWalletServiceStateRequestDto
Which wallet service is switched, and which way.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | [**TenantWalletService**](TenantWalletService.md) | The service being switched, given by its catalogue name. Switching it on only makes it available to the  portal; its units are still bought with `PUT api/2.0/portal/payment/updatewallet`. | [optional] 
**enabled** | **bool** | Which way the service is switched: `true` makes it available to the portal, `false` withdraws it. Setting the  state the service already has changes nothing. | [optional] 

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


