# OrdersItemRequestDtoInteger
An item in the ordering request with its entry type and ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_id** | **int** | The entry unique identifier (file or folder). | [optional] 
**entry_type** | [**FileEntryType**](FileEntryType.md) |  | [optional] 
**order** | **int** | The order value. | [optional] 

## Example

```python
from docspace-api-python.models.orders_item_request_dto_integer import OrdersItemRequestDtoInteger

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersItemRequestDtoInteger from a JSON string
orders_item_request_dto_integer_instance = OrdersItemRequestDtoInteger.from_json(json)
# print the JSON string representation of the object
print(OrdersItemRequestDtoInteger.to_json())

# convert the object into a dict
orders_item_request_dto_integer_dict = orders_item_request_dto_integer_instance.to_dict()
# create an instance of OrdersItemRequestDtoInteger from a dict
orders_item_request_dto_integer_from_dict = OrdersItemRequestDtoInteger.from_dict(orders_item_request_dto_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


