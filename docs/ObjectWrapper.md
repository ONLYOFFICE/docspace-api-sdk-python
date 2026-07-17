# ObjectWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **object** |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.object_wrapper import ObjectWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectWrapper from a JSON string
object_wrapper_instance = ObjectWrapper.from_json(json)
# print the JSON string representation of the object
print(ObjectWrapper.to_json())

# convert the object into a dict
object_wrapper_dict = object_wrapper_instance.to_dict()
# create an instance of ObjectWrapper from a dict
object_wrapper_from_dict = ObjectWrapper.from_dict(object_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


