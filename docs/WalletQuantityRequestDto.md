# WalletQuantityRequestDto
The wallet service being bought or scheduled, and the way its quantity is applied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **Dict[str, Optional[int]]** | The wallet service and the number of units of it, as a single pair. The key is the `serviceName` of a service  from `GET api/2.0/portal/payment/walletservices`, and the value is read according to  `productQuantityType`: the units to add, or the total the service is to have in the next period. Minimum  quantities apply per service - disk storage starts at 100 units, the Docs Connect Dev Pack at 10, and the  administrators may not be fewer than the portal already has. Exactly one pair is accepted, and a null or zero  value cancels a change scheduled earlier rather than buying nothing. | 
**product_quantity_type** | [**ProductQuantityType**](ProductQuantityType.md) | How the number in `quantity` is applied. `Add` buys the units straight away and charges them to the portal  wallet, while `Set` charges nothing now and records the quantity the service is to have from the next period.  Only these two are accepted here; `Sub` and `Renew` are refused with 400. | [optional] 

## Example

```python
from docspace_api_sdk.models.wallet_quantity_request_dto import WalletQuantityRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of WalletQuantityRequestDto from a JSON string
wallet_quantity_request_dto_instance = WalletQuantityRequestDto.from_json(json)
# print the JSON string representation of the object
print(WalletQuantityRequestDto.to_json())

# convert the object into a dict
wallet_quantity_request_dto_dict = wallet_quantity_request_dto_instance.to_dict()
# create an instance of WalletQuantityRequestDto from a dict
wallet_quantity_request_dto_from_dict = WalletQuantityRequestDto.from_dict(wallet_quantity_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


