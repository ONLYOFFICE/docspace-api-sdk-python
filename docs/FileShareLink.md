# FileShareLink
A sharing link of a file, a folder or a room, with everything set on it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | The identifier of the link, the one to send back as `linkId` to change or delete it. | [optional] 
**title** | **str** | The name the link is listed under, which its author is free to choose and to leave empty. | [optional] 
**share_link** | **str** | The shortened address to hand out. Opening it is what turns the link into access; the address stays the same  while the link exists. | [optional] 
**expiration_date** | [**ApiDateTime**](ApiDateTime.md) | The moment the link stops working, written with the offset of the portal time zone. Null when the link was  left without an end. | [optional] 
**link_type** | [**LinkType**](LinkType.md) | Which of the two jobs the link does: letting somebody into the room as a member, or handing out the entry  itself. The counters of uses are filled in for the first kind only. | [optional] 
**password** | **str** | The password a visitor has to send before the link resolves, readable only by those who may manage the link.  Empty when the link asks for none. | [optional] 
**deny_download** | **bool** | Whether visitors coming through this link may only read the entry in the editor and not download or print it. | [optional] 
**is_expired** | **bool** | Whether the moment in `expirationDate` has already passed, which leaves the link in place but refuses  everybody who opens it. | [optional] 
**primary** | **bool** | Whether this is the one link the entry always keeps: a public or a form-filling room is given it at creation,  and deleting it there only makes a new one. | [optional] 
**internal** | **bool** | Whether the visitor has to sign in to the portal before the link resolves, as opposed to it being open to  anybody who has the address. | [optional] 
**request_token** | **str** | The key that stands for this link in the calls that resolve it, such as `GET api/2.0/files/share/{key}`. It is  filled in for links that hand out the entry, and empty for the ones that invite into a room. | [optional] 
**max_use_count** | **int** | How many accounts may still join the room through this invitation link in total. Null on a link that hands out  the entry, where nothing is counted. | [optional] 
**current_use_count** | **int** | How many accounts have already joined through this invitation link. Once it reaches `maxUseCount` the link  stops letting anybody else in. Null on a link that hands out the entry. | [optional] 

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


