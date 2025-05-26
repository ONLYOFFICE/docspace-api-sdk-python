# OrderRequestDto

The parameters for ordering requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **int** | The order value. | [optional] 

## Example

```python
from docspace.models.order_request_dto import OrderRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrderRequestDto from a JSON string
order_request_dto_instance = OrderRequestDto.from_json(json)
# print the JSON string representation of the object
print(OrderRequestDto.to_json())

# convert the object into a dict
order_request_dto_dict = order_request_dto_instance.to_dict()
# create an instance of OrderRequestDto from a dict
order_request_dto_from_dict = OrderRequestDto.from_dict(order_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


