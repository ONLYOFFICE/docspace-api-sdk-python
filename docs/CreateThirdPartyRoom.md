# CreateThirdPartyRoom
The room to be created out of a folder of a connected third-party storage account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_as_new_folder** | **bool** | Creates a new folder named after `title` inside the folder named in the path and turns that subfolder into the  room, leaving the named folder itself untouched. When omitted, the named folder becomes the room and keeps  everything it already holds. | [optional] 
**title** | **str** | The name the room is shown under. It is stored on the connected account, so it does not have to match the name  of the folder in the storage; with `createAsNewFolder` it is also the name given to the created subfolder. | 
**room_type** | [**RoomType**](RoomType.md) | The kind of room the folder becomes, which decides the default access rules of its members and cannot be  changed afterwards. | 
**private** | **bool** | Restricts the room to the members explicitly invited into it. The flag is kept on the connected storage  account rather than on the folder, so every folder read through that account reports the same value. | [optional] 
**indexing** | **bool** | Keeps the contents of the room in an explicit numbered order, the one reported as `order` on every entry,  instead of leaving the order to the reader. | [optional] 
**deny_download** | **bool** | Forbids downloading and printing the contents of the room, which leaves the members with viewing and editing  in the editor only. | [optional] 
**color** | **str** | The background colour drawn behind the cover of the room, as six hexadecimal digits without a leading number  sign. An empty value restores the colour the portal picks by default. | [optional] 
**cover** | **str** | The drawing shown on the room tile, named by one of the built-in cover identifiers returned by  `GET api/2.0/files/rooms/covers`. An empty value leaves the room without a cover, and any other unknown value  is rejected as an invalid request. | [optional] 
**tags** | **List[str]** | The tags to attach to the room, named by their text. A name that is not in the portal tag catalogue yet is  added to it, and `GET api/2.0/files/tags` lists the names already there. | [optional] 
**logo** | [**LogoRequest**](LogoRequest.md) | The picture to use as the room logo, which has to be uploaded with `POST api/2.0/files/logos` first; leaving  it out keeps the room on its cover and colour. | [optional] 

## Example

```python
from docspace_api_sdk.models.create_third_party_room import CreateThirdPartyRoom

# TODO update the JSON string below
json = "{}"
# create an instance of CreateThirdPartyRoom from a JSON string
create_third_party_room_instance = CreateThirdPartyRoom.from_json(json)
# print the JSON string representation of the object
print(CreateThirdPartyRoom.to_json())

# convert the object into a dict
create_third_party_room_dict = create_third_party_room_instance.to_dict()
# create an instance of CreateThirdPartyRoom from a dict
create_third_party_room_from_dict = CreateThirdPartyRoom.from_dict(create_third_party_room_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


