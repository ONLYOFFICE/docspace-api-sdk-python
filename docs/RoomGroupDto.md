# RoomGroupDto
A personal collection of rooms: the name and icon it was given, the account that owns it, and the rooms it gathers  at the moment it was read.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier of the group, which addresses it in every other group operation and is kept for as long as the  group exists. | [optional] 
**name** | **str** | The name its owner gave the group, stored trimmed of surrounding spaces. Names are not unique, so two groups  of the same account can be told apart only by their identifier. | [optional] 
**icon** | [**MultiSizeLogoCover**](MultiSizeLogoCover.md) | The built-in cover chosen for the group, carrying the cover identifier and its rendering in each available  size. Null when the group has no icon, either because it was never given one or because the icon was cleared  by setting it to an empty value. | [optional] 
**user_id** | **UUID** | The account that created the group and the only one able to read, change or delete it; for any other member of  the portal the group does not exist. | [optional] 
**search_area** | [**SearchArea**](SearchArea.md) | The section the group belongs to, which categorizes it within the application's structure. This property determines  which area of the interface the group is associated with and affects how its rooms are filtered and displayed.  Common values include Active for standard rooms, Forms for form-based rooms, Archive for archived content, and  Templates for template rooms. The search area ensures that when retrieving a group, only rooms that belong to  the specified section are included in the results, maintaining proper organizational boundaries within the system. | [optional] 
**rooms** | [**List[FileEntryBaseDto]**](FileEntryBaseDto.md) | The rooms the group gathers, those stored in the portal first and those on connected third-party accounts  after them. Null when the group was asked for without its members, and an empty array when the group holds no  room the caller can still see. A room moved to the archive is left out until it is taken out of the archive. | [optional] 
**total_rooms** | **int** | How many rooms the group shows: the same rooms `rooms` lists, so archived ones are not counted either. It is  filled even when the rooms themselves were not asked for, which makes it the cheap way to tell an empty group  from a populated one. | [optional] 

## Example

```python
from docspace_api_sdk.models.room_group_dto import RoomGroupDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoomGroupDto from a JSON string
room_group_dto_instance = RoomGroupDto.from_json(json)
# print the JSON string representation of the object
print(RoomGroupDto.to_json())

# convert the object into a dict
room_group_dto_dict = room_group_dto_instance.to_dict()
# create an instance of RoomGroupDto from a dict
room_group_dto_from_dict = RoomGroupDto.from_dict(room_group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


