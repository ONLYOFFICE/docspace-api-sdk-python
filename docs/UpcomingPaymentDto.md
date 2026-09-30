# UpcomingPaymentDto
One charge the portal is going to be billed for at the start of the next period.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The quota that is going to be charged. When a switch to another quota is scheduled, this is the quota  being switched to, so it can differ from what `GET api/2.0/portal/tariff` reports for today. | [optional] 
**name** | **str** | The quota's stable key, which is the same identifier the wallet operations use for a service. | [optional] 
**title** | **str** | The quota name in the portal language, meant to be printed on an invoice preview. | [optional] 
**unit_of_measure** | **str** | What `quantity` counts, in the portal language - seats, administrators, gigabytes. It is empty for a quota  that is simply on or off. | [optional] 
**quantity** | **int** | How much is going to be charged for, which is the quantity scheduled for the next period when one has been  scheduled and today's quantity otherwise. | [optional] 
**wallet** | **bool** | Whether the charge is paid out of the portal wallet rather than from the subscription. | [optional] 
**due_date** | [**ApiDateTime**](ApiDateTime.md) | When the charge falls due, in the portal time zone. | [optional] 
**amount** | **float** | What the charge comes to: the unit price of the quota multiplied by `quantity`. Taxes are not part of it,  and a quota with no price of its own is not listed at all rather than listed with a zero. | [optional] 
**currency** | **str** | The currency `amount` is expressed in, as a three-letter ISO 4217 code. It follows the portal's billing  account, so every entry of one answer carries the same code. | [optional] 

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


