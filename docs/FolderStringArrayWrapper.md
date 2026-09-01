# FolderStringArrayWrapper
The successful API response containing the list of FolderDtoString objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[FolderDtoString]**](FolderDtoString.md) | The list of FolderDtoString objects returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.folder_string_array_wrapper import FolderStringArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FolderStringArrayWrapper from a JSON string
folder_string_array_wrapper_instance = FolderStringArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(FolderStringArrayWrapper.to_json())

# convert the object into a dict
folder_string_array_wrapper_dict = folder_string_array_wrapper_instance.to_dict()
# create an instance of FolderStringArrayWrapper from a dict
folder_string_array_wrapper_from_dict = FolderStringArrayWrapper.from_dict(folder_string_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


