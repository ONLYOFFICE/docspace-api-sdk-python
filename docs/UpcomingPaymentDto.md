# UpcomingPaymentDto
The upcoming payment parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The quota ID. | [optional] 
**name** | **str** | The quota name. | [optional] 
**title** | **str** | The quota title. | [optional] 
**unit_of_measure** | **str** | The quota unit of measure. | [optional] 
**quantity** | **int** | The quantity that will be charged (the next quantity if set, otherwise the current quantity). | [optional] 
**wallet** | **bool** | The quota applies to the wallet or not. | [optional] 
**due_date** | [**ApiDateTime**](ApiDateTime.md) | The API date and time parameters. | [optional] 
**amount** | **float** | The amount that will be charged (unit price multiplied by the quantity). | [optional] 
**currency** | **str** | The three-character ISO 4217 currency symbol of the amount. | [optional] 

## Example

```python
from docspace_api_sdk.models.upcoming_payment_dto import UpcomingPaymentDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpcomingPaymentDto from a JSON string
upcoming_payment_dto_instance = UpcomingPaymentDto.from_json(json)
# print the JSON string representation of the object
print(UpcomingPaymentDto.to_json())

# convert the object into a dict
upcoming_payment_dto_dict = upcoming_payment_dto_instance.to_dict()
# create an instance of UpcomingPaymentDto from a dict
upcoming_payment_dto_from_dict = UpcomingPaymentDto.from_dict(upcoming_payment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


