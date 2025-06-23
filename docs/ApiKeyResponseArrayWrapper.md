# ApiKeyResponseArrayWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[ApiKeyResponseDto]**](ApiKeyResponseDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.api_key_response_array_wrapper import ApiKeyResponseArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyResponseArrayWrapper from a JSON string
api_key_response_array_wrapper_instance = ApiKeyResponseArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(ApiKeyResponseArrayWrapper.to_json())

# convert the object into a dict
api_key_response_array_wrapper_dict = api_key_response_array_wrapper_instance.to_dict()
# create an instance of ApiKeyResponseArrayWrapper from a dict
api_key_response_array_wrapper_from_dict = ApiKeyResponseArrayWrapper.from_dict(api_key_response_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


