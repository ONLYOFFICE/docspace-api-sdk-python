# TransactionInfoDto
Represents information about the transaction applied to an account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The date and time when the credit transaction occurred. | [optional] 
**currency** | **str** | The three-character ISO 4217 currency symbol. | [optional] 
**amount** | **float** | The amount in the specified currency. | [optional] 

## Example

```python
from docspace_api_sdk.models.transaction_info_dto import TransactionInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionInfoDto from a JSON string
transaction_info_dto_instance = TransactionInfoDto.from_json(json)
# print the JSON string representation of the object
print(TransactionInfoDto.to_json())

# convert the object into a dict
transaction_info_dto_dict = transaction_info_dto_instance.to_dict()
# create an instance of TransactionInfoDto from a dict
transaction_info_dto_from_dict = TransactionInfoDto.from_dict(transaction_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


