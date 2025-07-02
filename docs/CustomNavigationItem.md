# CustomNavigationItem
The custom navigation item parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the custom navigation item. | [optional] 
**label** | **str** | The label of the custom navigation item. | [optional] 
**url** | **str** | The URL of the custom navigation item. | [optional] 
**big_img** | **str** | The big image of the custom navigation item. | [optional] 
**small_img** | **str** | The small image of the custom navigation item. | [optional] 
**show_in_menu** | **bool** | Specifies whether to show the custom navigation item in menu or not. | [optional] 
**show_on_home_page** | **bool** | Specifies whether to show the custom navigation item on home page or not. | [optional] 

## Example

```python
from docspace-api-python.models.custom_navigation_item import CustomNavigationItem

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


