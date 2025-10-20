# QuantityRequestDto
The request parameters for specifying payment quantity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **Dict[str, int]** | The mapping of item identifiers to their respective quantities in the payment. | [optional] 

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


