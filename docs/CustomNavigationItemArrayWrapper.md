# CustomNavigationItemArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[CustomNavigationItem]**](CustomNavigationItem.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.custom_navigation_item_array_wrapper import CustomNavigationItemArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of CustomNavigationItemArrayWrapper from a JSON string
custom_navigation_item_array_wrapper_instance = CustomNavigationItemArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(CustomNavigationItemArrayWrapper.to_json())

# convert the object into a dict
custom_navigation_item_array_wrapper_dict = custom_navigation_item_array_wrapper_instance.to_dict()
# create an instance of CustomNavigationItemArrayWrapper from a dict
custom_navigation_item_array_wrapper_from_dict = CustomNavigationItemArrayWrapper.from_dict(custom_navigation_item_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


