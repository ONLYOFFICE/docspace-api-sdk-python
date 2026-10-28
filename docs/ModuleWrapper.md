# ModuleWrapper
The successful API response containing the Module object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**Module**](Module.md) | The Module object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.module_wrapper import ModuleWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleWrapper from a JSON string
module_wrapper_instance = ModuleWrapper.from_json(json)
# print the JSON string representation of the object
print(ModuleWrapper.to_json())

# convert the object into a dict
module_wrapper_dict = module_wrapper_instance.to_dict()
# create an instance of ModuleWrapper from a dict
module_wrapper_from_dict = ModuleWrapper.from_dict(module_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


