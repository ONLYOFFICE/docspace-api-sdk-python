# CheckDestFolderWrapper
The successful API response containing the CheckDestFolderDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CheckDestFolderDto**](CheckDestFolderDto.md) | The CheckDestFolderDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.check_dest_folder_wrapper import CheckDestFolderWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of CheckDestFolderWrapper from a JSON string
check_dest_folder_wrapper_instance = CheckDestFolderWrapper.from_json(json)
# print the JSON string representation of the object
print(CheckDestFolderWrapper.to_json())

# convert the object into a dict
check_dest_folder_wrapper_dict = check_dest_folder_wrapper_instance.to_dict()
# create an instance of CheckDestFolderWrapper from a dict
check_dest_folder_wrapper_from_dict = CheckDestFolderWrapper.from_dict(check_dest_folder_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


