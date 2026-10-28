# BalanceDto
Represents a balance with an account number and a list of sub-accounts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **int** | The account number. | [optional] 
**sub_account_number** | **int** | The sub-account number. | [optional] 
**account_name** | **str** | The account name. | [optional] 
**account_currency** | **str** | The account currency. | [optional] 
**sub_accounts** | [**List[SubAccountDto]**](SubAccountDto.md) | A list of sub-accounts. | [optional] 
**last_credit** | [**TransactionInfoDto**](TransactionInfoDto.md) | The most recent credit transaction applied to the account. | [optional] 

## Example

```python
from docspace_api_sdk.models.balance_dto import BalanceDto

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceDto from a JSON string
balance_dto_instance = BalanceDto.from_json(json)
# print the JSON string representation of the object
print(BalanceDto.to_json())

# convert the object into a dict
balance_dto_dict = balance_dto_instance.to_dict()
# create an instance of BalanceDto from a dict
balance_dto_from_dict = BalanceDto.from_dict(balance_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


