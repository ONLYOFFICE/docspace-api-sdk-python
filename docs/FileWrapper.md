# FileWrapper
The successful API response containing the FileDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FileDto**](FileDto.md) | The FileDto object returned by the operation. | [optional] 
**count** | **int** | How many items this response carries: the length of the page for a list, 1 for a single object | [optional] 
**total** | **int** | How many items the whole list holds across all pages, for working out how many pages to request. Sent only by the operations that page their results, and left out of every other response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.file_wrapper import FileWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FileWrapper from a JSON string
file_wrapper_instance = FileWrapper.from_json(json)
# print the JSON string representation of the object
print(FileWrapper.to_json())

# convert the object into a dict
file_wrapper_dict = file_wrapper_instance.to_dict()
# create an instance of FileWrapper from a dict
file_wrapper_from_dict = FileWrapper.from_dict(file_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


