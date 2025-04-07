# CustomNavigationItem

Custom navigation parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id | [optional] 
**label** | **str** | Label | [optional] 
**url** | **str** | URL | [optional] 
**big_img** | **str** | Big image | [optional] 
**small_img** | **str** | Small image | [optional] 
**show_in_menu** | **bool** | Show in menu or not | [optional] 
**show_on_home_page** | **bool** | Show on home page or not | [optional] 

## Example

```python
from docspace.models.custom_navigation_item import CustomNavigationItem

# TODO update the JSON string below
json = "{}"
# create an instance of CustomNavigationItem from a JSON string
custom_navigation_item_instance = CustomNavigationItem.from_json(json)
# print the JSON string representation of the object
print(CustomNavigationItem.to_json())

# convert the object into a dict
custom_navigation_item_dict = custom_navigation_item_instance.to_dict()
# create an instance of CustomNavigationItem from a dict
custom_navigation_item_from_dict = CustomNavigationItem.from_dict(custom_navigation_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


