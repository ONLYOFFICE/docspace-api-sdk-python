# DiscountCategory
Represents a discount category applied to the price.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The discount category unique identifier. | [optional] 
**value_discount** | **float** | The discount value. | [optional] 
**description** | **str** | The discount category description. | [optional] 
**created** | **datetime** | The date and time when the discount category was created. | [optional] 

## Example

```python
from docspace_api_sdk.models.discount_category import DiscountCategory

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountCategory from a JSON string
discount_category_instance = DiscountCategory.from_json(json)
# print the JSON string representation of the object
print(DiscountCategory.to_json())

# convert the object into a dict
discount_category_dict = discount_category_instance.to_dict()
# create an instance of DiscountCategory from a dict
discount_category_from_dict = DiscountCategory.from_dict(discount_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


