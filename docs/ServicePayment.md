# ServicePayment
Represents service payment information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **int** | The payment operation ID. | [optional] 
**amount** | **float** | The balance of the sub-account in the specified currency. | [optional] 
**currency** | **str** | The three-character ISO 4217 currency symbol. | [optional] 
**quantity** | **int** | Total quantity of operations. | [optional] 
**subscription_id** | **int** | The subscription ID | [optional] 
**start_date** | **datetime** | The subscription start date. | [optional] 
**end_date** | **datetime** | The subscription end date. | [optional] 

## Example

```python
from docspace_api_sdk.models.service_payment import ServicePayment

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePayment from a JSON string
service_payment_instance = ServicePayment.from_json(json)
# print the JSON string representation of the object
print(ServicePayment.to_json())

# convert the object into a dict
service_payment_dict = service_payment_instance.to_dict()
# create an instance of ServicePayment from a dict
service_payment_from_dict = ServicePayment.from_dict(service_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


