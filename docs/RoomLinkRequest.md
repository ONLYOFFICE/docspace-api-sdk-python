# RoomLinkRequest
The room link parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_id** | **str** | The room link ID. | [optional] 
**access** | [**FileShare**](FileShare.md) |  | [optional] 
**expiration_date** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**title** | **str** | The link name. | [optional] 
**link_type** | [**LinkType**](LinkType.md) |  | [optional] 
**password** | **str** | The link password. | [optional] 
**deny_download** | **bool** | Specifies if downloading the file from the link is disabled or not. | [optional] 

## Example

```python
from docspace-api-python.models.room_link_request import RoomLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RoomLinkRequest from a JSON string
room_link_request_instance = RoomLinkRequest.from_json(json)
# print the JSON string representation of the object
print(RoomLinkRequest.to_json())

# convert the object into a dict
room_link_request_dict = room_link_request_instance.to_dict()
# create an instance of RoomLinkRequest from a dict
room_link_request_from_dict = RoomLinkRequest.from_dict(room_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


