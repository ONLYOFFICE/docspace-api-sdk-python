# FileReferenceWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FileReference**](FileReference.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.file_reference_wrapper import FileReferenceWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FileReferenceWrapper from a JSON string
file_reference_wrapper_instance = FileReferenceWrapper.from_json(json)
# print the JSON string representation of the object
print(FileReferenceWrapper.to_json())

# convert the object into a dict
file_reference_wrapper_dict = file_reference_wrapper_instance.to_dict()
# create an instance of FileReferenceWrapper from a dict
file_reference_wrapper_from_dict = FileReferenceWrapper.from_dict(file_reference_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


