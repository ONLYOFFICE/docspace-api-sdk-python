# CustomerInfo

The customer information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portal_id** | **str** | The portal ID. | [optional] 
**payment_method_status** | [**PaymentMethodStatus**](PaymentMethodStatus.md) |  | [optional] 
**email** | **str** | The email address of the customer. | [optional] 

## Example

```python
from docspace.models.customer_info import CustomerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerInfo from a JSON string
customer_info_instance = CustomerInfo.from_json(json)
# print the JSON string representation of the object
print(CustomerInfo.to_json())

# convert the object into a dict
customer_info_dict = customer_info_instance.to_dict()
# create an instance of CustomerInfo from a dict
customer_info_from_dict = CustomerInfo.from_dict(customer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


