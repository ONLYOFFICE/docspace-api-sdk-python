# FileReferenceWrapper
The successful API response containing the FileReference object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FileReference**](FileReference.md) | The FileReference object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

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


