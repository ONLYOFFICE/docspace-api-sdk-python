# FolderLinkRequest
The folder link parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_id** | **str** | The folder link ID. | [optional] 
**access** | [**FileShare**](FileShare.md) |  | [optional] 
**expiration_date** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**title** | **str** | The link name. | [optional] 
**password** | **str** | The link password. | [optional] 
**deny_download** | **bool** | Specifies if downloading the file from the link is disabled or not. | [optional] 
**internal** | **bool** | The link scope, whether it is internal or not. | [optional] 
**primary** | **bool** | Specifies whether the folder link is primary or not. | [optional] 

## Example

```python
from docspace_api_sdk.models.folder_link_request import FolderLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FolderLinkRequest from a JSON string
folder_link_request_instance = FolderLinkRequest.from_json(json)
# print the JSON string representation of the object
print(FolderLinkRequest.to_json())

# convert the object into a dict
folder_link_request_dict = folder_link_request_instance.to_dict()
# create an instance of FolderLinkRequest from a dict
folder_link_request_from_dict = FolderLinkRequest.from_dict(folder_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


