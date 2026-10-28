# FolderWrapper
The successful API response containing the FolderDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FolderDto**](FolderDto.md) | The FolderDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.folder_wrapper import FolderWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FolderWrapper from a JSON string
folder_wrapper_instance = FolderWrapper.from_json(json)
# print the JSON string representation of the object
print(FolderWrapper.to_json())

# convert the object into a dict
folder_wrapper_dict = folder_wrapper_instance.to_dict()
# create an instance of FolderWrapper from a dict
folder_wrapper_from_dict = FolderWrapper.from_dict(folder_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


