# CustomerInfoDto
The customer information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portal_id** | **str** | The portal ID. | [optional] [readonly] 
**payment_method_status** | [**PaymentMethodStatus**](PaymentMethodStatus.md) |  | [optional] 
**email** | **str** | The email address of the customer. | [optional] [readonly] 
**payer** | [**EmployeeDto**](EmployeeDto.md) |  | [optional] 

## Example

```python
from docspace-api-sdk.models.customer_info_dto import CustomerInfoDto

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


