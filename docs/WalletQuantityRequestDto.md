# WalletQuantityRequestDto
The request parameters for the wallet payment quantity specifications.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **Dict[str, Optional[int]]** | The mapping of item identifiers with their respective quantities in the payment. | [optional] 
**product_quantity_type** | [**ProductQuantityType**](ProductQuantityType.md) |  | [optional] 

## Example

```python
from docspace-api-python.models.wallet_quantity_request_dto import WalletQuantityRequestDto

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


