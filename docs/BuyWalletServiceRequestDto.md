# BuyWalletServiceRequestDto
The request parameters for buying wallet service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | Number of services provided. | [optional] 
**service_name** | **str** | The service name. | [optional] 

## Example

```python
from docspace_api_sdk.models.buy_wallet_service_request_dto import BuyWalletServiceRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of BuyWalletServiceRequestDto from a JSON string
buy_wallet_service_request_dto_instance = BuyWalletServiceRequestDto.from_json(json)
# print the JSON string representation of the object
print(BuyWalletServiceRequestDto.to_json())

# convert the object into a dict
buy_wallet_service_request_dto_dict = buy_wallet_service_request_dto_instance.to_dict()
# create an instance of BuyWalletServiceRequestDto from a dict
buy_wallet_service_request_dto_from_dict = BuyWalletServiceRequestDto.from_dict(buy_wallet_service_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


