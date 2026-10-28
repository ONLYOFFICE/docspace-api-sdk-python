# RoomGroupRequestDto
The name, the icon and the rooms of a room group to create.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name to show the group under. Surrounding spaces are trimmed before it is stored, a name that is blank  once trimmed is refused, and the name does not have to differ from the names of the caller's other groups. | 
**icon** | **str** | The icon of the group, given as the identifier of one of the built-in covers listed by  `GET api/2.0/files/rooms/covers`. An uploaded image cannot be used, and any value that is not one of those  identifiers is refused. | 
**rooms** | [**List[DuplicateRequestDtoAllOfFileIds]**](DuplicateRequestDtoAllOfFileIds.md) | The rooms to gather in the group, each given as a number for a room stored in the portal or as a string for a  room on a connected third-party account. Every identifier has to name a room the caller can read; repeats are  collapsed, and an element of any other shape - a decimal number, a number sent as a string, null - is refused. | 
**search_area** | [**SearchArea**](SearchArea.md) | The section the group belongs to: Active for Rooms and Forms for Forms. Active when omitted. | [optional] 

## Example

```python
from docspace_api_sdk.models.room_group_request_dto import RoomGroupRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoomGroupRequestDto from a JSON string
room_group_request_dto_instance = RoomGroupRequestDto.from_json(json)
# print the JSON string representation of the object
print(RoomGroupRequestDto.to_json())

# convert the object into a dict
room_group_request_dto_dict = room_group_request_dto_instance.to_dict()
# create an instance of RoomGroupRequestDto from a dict
room_group_request_dto_from_dict = RoomGroupRequestDto.from_dict(room_group_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


