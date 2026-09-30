# CustomerInfoDto
The billing customer behind the portal, and which portal member pays for it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portal_id** | **str** | The portal's identifier in the billing system, which is what support and invoices refer to. It is not the  portal alias. | [optional] [readonly] 
**payment_method_status** | [**PaymentMethodStatus**](PaymentMethodStatus.md) | Whether a payment method is stored for the account and usable. Without one the portal can hold a wallet  balance but cannot be charged automatically. | [optional] 
**payment_method_type** | **str** | The customer's payment method type. | [optional] [readonly] 
**is_delayed_payment_method** | **bool** | Indicates whether the customer's payment method is delayed, i.e. the money reaches the wallet only after  the transfer settles rather than immediately. | [optional] [readonly] 
**email** | **str** | The address the billing account is registered to, lower-cased. It need not belong to a portal member,  which is exactly when `payer` stays empty. | [optional] [readonly] 
**payer** | [**EmployeeDto**](EmployeeDto.md) | The portal member whose account is behind the billing address. It is empty when `email` matches no member  of this portal, and while it is empty every operation of this group that only the payer may call is out  of reach for everybody. | [optional] 

## Example

```python
from docspace_api_sdk.models.customer_info_dto import CustomerInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerInfoDto from a JSON string
customer_info_dto_instance = CustomerInfoDto.from_json(json)
# print the JSON string representation of the object
print(CustomerInfoDto.to_json())

# convert the object into a dict
customer_info_dto_dict = customer_info_dto_instance.to_dict()
# create an instance of CustomerInfoDto from a dict
customer_info_dto_from_dict = CustomerInfoDto.from_dict(customer_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


