# CreditAiBalanceRequestDto
The request parameters for crediting AI quota to the customer AI subaccount.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount to transfer from the main balance to the AI subaccount. | [optional] 
**currency** | **str** | The three-character ISO 4217 currency symbol. | [optional] 

## Example

```python
from docspace_api_sdk.models.credit_ai_balance_request_dto import CreditAiBalanceRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreditAiBalanceRequestDto from a JSON string
credit_ai_balance_request_dto_instance = CreditAiBalanceRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreditAiBalanceRequestDto.to_json())

# convert the object into a dict
credit_ai_balance_request_dto_dict = credit_ai_balance_request_dto_instance.to_dict()
# create an instance of CreditAiBalanceRequestDto from a dict
credit_ai_balance_request_dto_from_dict = CreditAiBalanceRequestDto.from_dict(credit_ai_balance_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


