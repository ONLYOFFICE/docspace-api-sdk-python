# TopUpDepositRequestDto
How much money is charged to the payment method on file and added to the portal wallet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The sum to charge, as a whole number of units of `currency` - 10 means ten dollars and not ten cents. The  bounds are what one call may move, not what the wallet may hold, so a larger top-up is made of several calls. | [optional] 
**currency** | **str** | The currency the charge is made in, as an ISO 4217 code in upper case. It has to be one of the accounting  currencies this installation supports, which `GET api/2.0/portal/payment/accounting/currencies` lists; any  other code is refused with 400. The money lands on the wallet sub-account of that currency, so topping up in  a second currency does not add to the first one. | [optional] 

## Example

```python
from docspace_api_sdk.models.top_up_deposit_request_dto import TopUpDepositRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of TopUpDepositRequestDto from a JSON string
top_up_deposit_request_dto_instance = TopUpDepositRequestDto.from_json(json)
# print the JSON string representation of the object
print(TopUpDepositRequestDto.to_json())

# convert the object into a dict
top_up_deposit_request_dto_dict = top_up_deposit_request_dto_instance.to_dict()
# create an instance of TopUpDepositRequestDto from a dict
top_up_deposit_request_dto_from_dict = TopUpDepositRequestDto.from_dict(top_up_deposit_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


