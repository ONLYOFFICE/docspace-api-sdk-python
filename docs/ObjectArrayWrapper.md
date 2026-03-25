# ObjectArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **List[object]** |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.object_array_wrapper import ObjectArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectArrayWrapper from a JSON string
object_array_wrapper_instance = ObjectArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(ObjectArrayWrapper.to_json())

# convert the object into a dict
object_array_wrapper_dict = object_array_wrapper_instance.to_dict()
# create an instance of ObjectArrayWrapper from a dict
object_array_wrapper_from_dict = ObjectArrayWrapper.from_dict(object_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


