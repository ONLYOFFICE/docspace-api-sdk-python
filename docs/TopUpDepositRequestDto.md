# TopUpDepositRequestDto
Put money on deposit request parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | Amount | [optional] 
**currency** | **str** | The three-character ISO 4217 currency symbol | [optional] 

## Example

```python
from docspace-api-python.models.top_up_deposit_request_dto import TopUpDepositRequestDto

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


