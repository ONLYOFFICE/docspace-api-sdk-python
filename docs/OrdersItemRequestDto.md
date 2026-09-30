# OrdersItemRequestDto
One entry to move to a given position inside its folder.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_id** | **int** | The file or folder to move. | 
**entry_type** | [**FileEntryType**](FileEntryType.md) | Which of the two the identifier names, because a file and a folder may carry the same number. | 
**order** | **int** | The position the entry is to take, counting from 1. The entry that held it, and everything after it, is  shifted to make room. A dotted path such as 1.2.3 is accepted as well, of which only the last segment is  read. | 

## Example

```python
from docspace_api_sdk.models.orders_item_request_dto import OrdersItemRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersItemRequestDto from a JSON string
orders_item_request_dto_instance = OrdersItemRequestDto.from_json(json)
# print the JSON string representation of the object
print(OrdersItemRequestDto.to_json())

# convert the object into a dict
orders_item_request_dto_dict = orders_item_request_dto_instance.to_dict()
# create an instance of OrdersItemRequestDto from a dict
orders_item_request_dto_from_dict = OrdersItemRequestDto.from_dict(orders_item_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


