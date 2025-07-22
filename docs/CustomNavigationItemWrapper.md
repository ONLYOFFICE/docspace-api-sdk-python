# CustomNavigationItemWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CustomNavigationItem**](CustomNavigationItem.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.custom_navigation_item_wrapper import CustomNavigationItemWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of CustomNavigationItemWrapper from a JSON string
custom_navigation_item_wrapper_instance = CustomNavigationItemWrapper.from_json(json)
# print the JSON string representation of the object
print(CustomNavigationItemWrapper.to_json())

# convert the object into a dict
custom_navigation_item_wrapper_dict = custom_navigation_item_wrapper_instance.to_dict()
# create an instance of CustomNavigationItemWrapper from a dict
custom_navigation_item_wrapper_from_dict = CustomNavigationItemWrapper.from_dict(custom_navigation_item_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


