# PaymentUrlRequestDto
The request parameters for the payment URL configuration with quantity information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**back_url** | **str** | The URL where the user will be redirected after payment cancellation. | 
**success_url** | **str** | The URL where the user will be redirected after successful payment. | 
**quantity** | **Dict[str, int]** | The payment quantity. | [optional] 

## Example

```python
from docspace_api_sdk.models.payment_url_request_dto import PaymentUrlRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentUrlRequestDto from a JSON string
payment_url_request_dto_instance = PaymentUrlRequestDto.from_json(json)
# print the JSON string representation of the object
print(PaymentUrlRequestDto.to_json())

# convert the object into a dict
payment_url_request_dto_dict = payment_url_request_dto_instance.to_dict()
# create an instance of PaymentUrlRequestDto from a dict
payment_url_request_dto_from_dict = PaymentUrlRequestDto.from_dict(payment_url_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


