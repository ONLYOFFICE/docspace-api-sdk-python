# FileLinkWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FileLink**](FileLink.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.file_link_wrapper import FileLinkWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FileLinkWrapper from a JSON string
file_link_wrapper_instance = FileLinkWrapper.from_json(json)
# print the JSON string representation of the object
print(FileLinkWrapper.to_json())

# convert the object into a dict
file_link_wrapper_dict = file_link_wrapper_instance.to_dict()
# create an instance of FileLinkWrapper from a dict
file_link_wrapper_from_dict = FileLinkWrapper.from_dict(file_link_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


