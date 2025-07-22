# PaymentCalculationWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**PaymentCalculation**](PaymentCalculation.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.payment_calculation_wrapper import PaymentCalculationWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCalculationWrapper from a JSON string
payment_calculation_wrapper_instance = PaymentCalculationWrapper.from_json(json)
# print the JSON string representation of the object
print(PaymentCalculationWrapper.to_json())

# convert the object into a dict
payment_calculation_wrapper_dict = payment_calculation_wrapper_instance.to_dict()
# create an instance of PaymentCalculationWrapper from a dict
payment_calculation_wrapper_from_dict = PaymentCalculationWrapper.from_dict(payment_calculation_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


