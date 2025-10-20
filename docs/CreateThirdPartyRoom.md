# CreateThirdPartyRoom
The parameters for creating a third-party room.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_as_new_folder** | **bool** | Specifies whether to create a third-party room as a new folder or not. | [optional] 
**title** | **str** | The third-party room name to be created. | 
**room_type** | [**RoomType**](RoomType.md) |  | 
**private** | **bool** | Specifies whether to create the private third-party room or not. | [optional] 
**indexing** | **bool** | Specifies whether to create the third-party room with indexing. | [optional] 
**deny_download** | **bool** | Specifies whether to deny downloads from the third-party room. | [optional] 
**color** | **str** | The color of the third-party room. | [optional] 
**cover** | **str** | The cover of the third-party room. | [optional] 
**tags** | **List[str]** | The list of tags of the third-party room. | [optional] 
**logo** | [**LogoRequest**](LogoRequest.md) |  | [optional] 

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


