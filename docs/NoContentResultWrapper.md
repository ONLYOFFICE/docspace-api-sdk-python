# NoContentResultWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**NoContentResult**](NoContentResult.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.no_content_result_wrapper import NoContentResultWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of NoContentResultWrapper from a JSON string
no_content_result_wrapper_instance = NoContentResultWrapper.from_json(json)
# print the JSON string representation of the object
print(NoContentResultWrapper.to_json())

# convert the object into a dict
no_content_result_wrapper_dict = no_content_result_wrapper_instance.to_dict()
# create an instance of NoContentResultWrapper from a dict
no_content_result_wrapper_from_dict = NoContentResultWrapper.from_dict(no_content_result_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


