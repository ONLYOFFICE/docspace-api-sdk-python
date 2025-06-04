# PaymentCalculation

The payment calculation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **int** |  | [optional] 
**amount** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 

## Example

```python
from docspace.models.payment_calculation import PaymentCalculation

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


