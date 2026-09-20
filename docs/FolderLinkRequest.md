# FolderLinkRequest
The external link of a folder, as it is to be created or rewritten.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_id** | **UUID** | Which link the request addresses: the identifier of an existing link rewrites that link, while an identifier  that is not in use, the empty one included, creates a new link. Take an existing identifier from  `GET api/2.0/files/folder/{id}/links`. | [optional] 
**access** | [**FileShare**](FileShare.md) | The rights a visitor following the link is given. The value that grants nothing revokes the link instead of  setting it, and the answer is then empty. | [optional] 
**expiration_date** | [**ApiDateTime**](ApiDateTime.md) | The moment the link stops working, sent as an ISO-8601 stamp. A moment that lies in the past is ignored,  and leaving the field out gives the link no expiry. | [optional] 
**title** | **str** | The name the link is listed under for the people who manage the folder; a visitor following it never sees the  name. | [optional] 
**password** | **str** | The secret a visitor has to enter before the link opens. Leave it out for a link that opens without one; the  secret itself is never given back, only the fact that one is set. | [optional] 
**deny_download** | **bool** | Whether visitors are left with viewing alone: with true downloading and copying through the link are blocked,  with false they are allowed. | [optional] 
**internal** | **bool** | Whether the link admits signed-in portal members only: with true a visitor has to sign in before the link  opens, with false anyone holding the address may follow it. | [optional] 
**primary** | **bool** | Whether this link becomes the primary link of the folder, the one the Copy link action of a client hands  out; a folder has one primary link at a time. | [optional] 

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


