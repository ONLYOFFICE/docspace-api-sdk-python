# EnabledModuleArrayWrapper
The successful API response containing the list of EnabledModuleDto objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[EnabledModuleDto]**](EnabledModuleDto.md) | The list of EnabledModuleDto objects returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.enabled_module_array_wrapper import EnabledModuleArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of EnabledModuleArrayWrapper from a JSON string
enabled_module_array_wrapper_instance = EnabledModuleArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(EnabledModuleArrayWrapper.to_json())

# convert the object into a dict
enabled_module_array_wrapper_dict = enabled_module_array_wrapper_instance.to_dict()
# create an instance of EnabledModuleArrayWrapper from a dict
enabled_module_array_wrapper_from_dict = EnabledModuleArrayWrapper.from_dict(enabled_module_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


