# FileShareLink
A shareable link for a file with its configuration and status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the shared link. | [optional] 
**title** | **str** | The title of the shared content. | [optional] 
**share_link** | **str** | The URL for accessing the shared content. | [optional] 
**expiration_date** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**link_type** | [**LinkType**](LinkType.md) |  | [optional] 
**password** | **str** | The password protection for accessing the shared content. | [optional] 
**deny_download** | **bool** | Indicates whether downloading of the shared content is prohibited. | [optional] 
**is_expired** | **bool** | Indicates whether the shared link has expired. | [optional] 
**primary** | **bool** | Indicates whether this is the primary shared link. | [optional] 
**internal** | **bool** | Indicates whether the link is for the internal sharing only. | [optional] 
**request_token** | **str** | The token for validating access requests. | [optional] 

## Example

```python
from docspace_api_sdk.models.file_share_link import FileShareLink

# TODO update the JSON string below
json = "{}"
# create an instance of FileShareLink from a JSON string
file_share_link_instance = FileShareLink.from_json(json)
# print the JSON string representation of the object
print(FileShareLink.to_json())

# convert the object into a dict
file_share_link_dict = file_share_link_instance.to_dict()
# create an instance of FileShareLink from a dict
file_share_link_from_dict = FileShareLink.from_dict(file_share_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


