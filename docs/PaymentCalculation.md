# PaymentCalculation
The parameters of the calculated payment amount.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **int** | The operation unique identifier. | [optional] 
**amount** | **float** | The calculated payment amount. | [optional] 
**currency** | **str** | The three-character ISO 4217 currency symbol used for the payment calculation. | [optional] 
**quantity** | **int** | The quantity associated with the payment calculation. | [optional] 

## Example

```python
from docspace_api_sdk.models.payment_calculation import PaymentCalculation

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCalculation from a JSON string
payment_calculation_instance = PaymentCalculation.from_json(json)
# print the JSON string representation of the object
print(PaymentCalculation.to_json())

# convert the object into a dict
payment_calculation_dict = payment_calculation_instance.to_dict()
# create an instance of PaymentCalculation from a dict
payment_calculation_from_dict = PaymentCalculation.from_dict(payment_calculation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


