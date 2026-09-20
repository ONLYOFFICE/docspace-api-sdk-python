# AiFolderContentWrapper
The successful API response containing the FolderContentDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**AiFolderContentDto**](AiFolderContentDto.md) | The FolderContentDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_folder_content_wrapper import AiFolderContentWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of AiFolderContentWrapper from a JSON string
ai_folder_content_wrapper_instance = AiFolderContentWrapper.from_json(json)
# print the JSON string representation of the object
print(AiFolderContentWrapper.to_json())

# convert the object into a dict
ai_folder_content_wrapper_dict = ai_folder_content_wrapper_instance.to_dict()
# create an instance of AiFolderContentWrapper from a dict
ai_folder_content_wrapper_from_dict = AiFolderContentWrapper.from_dict(ai_folder_content_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


