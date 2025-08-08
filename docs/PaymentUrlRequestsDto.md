# PaymentUrlRequestsDto
The request parameters for the payment URL configuration with quantity information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**back_url** | **str** | The URL where the user will be redirected after payment processing. | [optional] 
**quantity** | **Dict[str, int]** | The quantity of payment | [optional] 

## Example

```python
from docspace_api_sdk.models.payment_url_requests_dto import PaymentUrlRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentUrlRequestsDto from a JSON string
payment_url_requests_dto_instance = PaymentUrlRequestsDto.from_json(json)
# print the JSON string representation of the object
print(PaymentUrlRequestsDto.to_json())

# convert the object into a dict
payment_url_requests_dto_dict = payment_url_requests_dto_instance.to_dict()
# create an instance of PaymentUrlRequestsDto from a dict
payment_url_requests_dto_from_dict = PaymentUrlRequestsDto.from_dict(payment_url_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


