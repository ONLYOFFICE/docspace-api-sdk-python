# Int32Wrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **int** |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.int32_wrapper import Int32Wrapper

# TODO update the JSON string below
json = "{}"
# create an instance of Int32Wrapper from a JSON string
int32_wrapper_instance = Int32Wrapper.from_json(json)
# print the JSON string representation of the object
print(Int32Wrapper.to_json())

# convert the object into a dict
int32_wrapper_dict = int32_wrapper_instance.to_dict()
# create an instance of Int32Wrapper from a dict
int32_wrapper_from_dict = Int32Wrapper.from_dict(int32_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


