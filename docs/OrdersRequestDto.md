# OrdersRequestDto
The request that moves several files and folders to given positions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[OrdersItemRequestDto]**](OrdersItemRequestDto.md) | The entries to move, applied one after another in the order they are sent, so each of them shifts the  neighbours the ones before it left behind. | 

## Example

```python
from docspace_api_sdk.models.orders_request_dto import OrdersRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersRequestDto from a JSON string
orders_request_dto_instance = OrdersRequestDto.from_json(json)
# print the JSON string representation of the object
print(OrdersRequestDto.to_json())

# convert the object into a dict
orders_request_dto_dict = orders_request_dto_instance.to_dict()
# create an instance of OrdersRequestDto from a dict
orders_request_dto_from_dict = OrdersRequestDto.from_dict(orders_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


