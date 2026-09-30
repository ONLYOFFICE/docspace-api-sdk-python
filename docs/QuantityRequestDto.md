# QuantityRequestDto
The new size of the portal subscription.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **Dict[str, int]** | The plan and the number of units it is to cover, as a single pair. While the portal is on a priced plan the  key has to be the `name` of that same plan, which `GET api/2.0/portal/payment/quota` reports, because the  subscription is resized rather than swapped; the value is the total the subscription is to have afterwards,  not the difference. Exactly one pair is accepted, and a value that is already in effect is refused with 400. | 

## Example

```python
from docspace_api_sdk.models.quantity_request_dto import QuantityRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of QuantityRequestDto from a JSON string
quantity_request_dto_instance = QuantityRequestDto.from_json(json)
# print the JSON string representation of the object
print(QuantityRequestDto.to_json())

# convert the object into a dict
quantity_request_dto_dict = quantity_request_dto_instance.to_dict()
# create an instance of QuantityRequestDto from a dict
quantity_request_dto_from_dict = QuantityRequestDto.from_dict(quantity_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


