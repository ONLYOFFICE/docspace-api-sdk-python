# Int64Wrapper
The successful API response containing the int64 value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **int** | The int64 value returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.int64_wrapper import Int64Wrapper

# TODO update the JSON string below
json = "{}"
# create an instance of Int64Wrapper from a JSON string
int64_wrapper_instance = Int64Wrapper.from_json(json)
# print the JSON string representation of the object
print(Int64Wrapper.to_json())

# convert the object into a dict
int64_wrapper_dict = int64_wrapper_instance.to_dict()
# create an instance of Int64Wrapper from a dict
int64_wrapper_from_dict = Int64Wrapper.from_dict(int64_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


