# CoversResultArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[CoversResultDto]**](CoversResultDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.covers_result_array_wrapper import CoversResultArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of CoversResultArrayWrapper from a JSON string
covers_result_array_wrapper_instance = CoversResultArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(CoversResultArrayWrapper.to_json())

# convert the object into a dict
covers_result_array_wrapper_dict = covers_result_array_wrapper_instance.to_dict()
# create an instance of CoversResultArrayWrapper from a dict
covers_result_array_wrapper_from_dict = CoversResultArrayWrapper.from_dict(covers_result_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


