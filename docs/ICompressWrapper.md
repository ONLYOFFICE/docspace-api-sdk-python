# ICompressWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **object** | The archiving class unification interface. | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.i_compress_wrapper import ICompressWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ICompressWrapper from a JSON string
i_compress_wrapper_instance = ICompressWrapper.from_json(json)
# print the JSON string representation of the object
print(ICompressWrapper.to_json())

# convert the object into a dict
i_compress_wrapper_dict = i_compress_wrapper_instance.to_dict()
# create an instance of ICompressWrapper from a dict
i_compress_wrapper_from_dict = ICompressWrapper.from_dict(i_compress_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


