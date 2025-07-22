# FileShareWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FileShareDto**](FileShareDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.file_share_wrapper import FileShareWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FileShareWrapper from a JSON string
file_share_wrapper_instance = FileShareWrapper.from_json(json)
# print the JSON string representation of the object
print(FileShareWrapper.to_json())

# convert the object into a dict
file_share_wrapper_dict = file_share_wrapper_instance.to_dict()
# create an instance of FileShareWrapper from a dict
file_share_wrapper_from_dict = FileShareWrapper.from_dict(file_share_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


