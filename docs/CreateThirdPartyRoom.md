# CreateThirdPartyRoom

Parameters for creating a room

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_as_new_folder** | **bool** | Create as new folder | [optional] 
**title** | **str** | Room name | [optional] 
**room_type** | [**RoomType**](RoomType.md) |  | [optional] 
**private** | **bool** | Private | [optional] 
**indexing** | **bool** | Indexing | [optional] 
**deny_download** | **bool** | Deny download | [optional] 
**color** | **str** | Color | [optional] 
**cover** | **str** | Cover | [optional] 
**tags** | **List[str]** | Tags | [optional] 
**logo** | [**LogoRequest**](LogoRequest.md) |  | [optional] 

## Example

```python
from docspace.models.create_third_party_room import CreateThirdPartyRoom

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


