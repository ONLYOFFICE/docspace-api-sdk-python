# OrdersRequestDtoInteger
The collection of items to be ordered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[OrdersItemRequestDtoInteger]**](OrdersItemRequestDtoInteger.md) | The list of items with their ordering information. | 

## Example

```python
from docspace_api_sdk.models.orders_request_dto_integer import OrdersRequestDtoInteger

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersRequestDtoInteger from a JSON string
orders_request_dto_integer_instance = OrdersRequestDtoInteger.from_json(json)
# print the JSON string representation of the object
print(OrdersRequestDtoInteger.to_json())

# convert the object into a dict
orders_request_dto_integer_dict = orders_request_dto_integer_instance.to_dict()
# create an instance of OrdersRequestDtoInteger from a dict
orders_request_dto_integer_from_dict = OrdersRequestDtoInteger.from_dict(orders_request_dto_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


