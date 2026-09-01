# DocsCloudPayment
Represents the payment information of a DocsCloud tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cart_id** | **str** | The cart ID. | [optional] 
**product_id** | **int** | The product ID. | [optional] 
**status** | **int** | The payment status. | [optional] 
**interval_unit** | **int** | The interval unit. | [optional] 
**is_year** | **bool** | Whether the payment interval is yearly. | [optional] 
**is_prepaid** | **bool** | Whether the payment is prepaid. | [optional] 
**quantity** | **int** | The quantity. | [optional] 
**currency** | **str** | The three-character ISO 4217 currency symbol of the payment. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_payment import DocsCloudPayment

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudPayment from a JSON string
docs_cloud_payment_instance = DocsCloudPayment.from_json(json)
# print the JSON string representation of the object
print(DocsCloudPayment.to_json())

# convert the object into a dict
docs_cloud_payment_dict = docs_cloud_payment_instance.to_dict()
# create an instance of DocsCloudPayment from a dict
docs_cloud_payment_from_dict = DocsCloudPayment.from_dict(docs_cloud_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


