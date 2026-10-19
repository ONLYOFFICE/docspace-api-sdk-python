# OrderByDto
The sorting parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_asc** | **bool** | Specifies if the order is ascending. | [optional] 
**var_property** | [**SortedByType**](SortedByType.md) | The parameters by which the files will be sorted. | [optional] 

## Example

```python
from docspace_api_sdk.models.order_by_dto import OrderByDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrderByDto from a JSON string
order_by_dto_instance = OrderByDto.from_json(json)
# print the JSON string representation of the object
print(OrderByDto.to_json())

# convert the object into a dict
order_by_dto_dict = order_by_dto_instance.to_dict()
# create an instance of OrderByDto from a dict
order_by_dto_from_dict = OrderByDto.from_dict(order_by_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


