# Int64Wrapper

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


