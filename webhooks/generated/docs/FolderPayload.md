# FolderPayload

The folder carried by a folder.* webhook. room.* and agent.* webhooks carry a room in their own payload; a room a folder.* webhook is about (folder.downloaded of a whole room) comes in this shape, told apart by `type`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**EntryId**](EntryId.md) |  | [optional] 
**parent_id** | [**EntryId**](EntryId.md) |  | [optional] 
**root_folder_id** | [**EntryId**](EntryId.md) |  | [optional] 
**title** | **str** | The name of the entry as shown in the portal; for a file it includes the extension. | [optional] 
**file_entry_type** | **int** | Tells a folder or room payload (1) from a file payload (2), so a receiver can pick the schema to read the rest of the object with. Flags of &#x60;FileEntryType&#x60;: 1 &#x3D; Folder, 2 &#x3D; File. | [optional] 
**created** | **datetime** | When the entry was created, in UTC. | [optional] 
**created_by** | [**UserSummaryPayload**](UserSummaryPayload.md) |  | [optional] 
**updated** | **datetime** | When the entry was last changed, in UTC; equal to &#x60;created&#x60; for an entry that has not changed since. | [optional] 
**updated_by** | [**UserSummaryPayload**](UserSummaryPayload.md) |  | [optional] 
**root_folder_type** | **int** | The kind of top-level section the entry sits in, such as My documents, Rooms, Archive or Trash. Values of &#x60;FolderType&#x60;: 0 &#x3D; DEFAULT, 1 &#x3D; COMMON, 2 &#x3D; BUNCH, 3 &#x3D; TRASH, 5 &#x3D; USER, 6 &#x3D; SHARE, 8 &#x3D; Projects, 10 &#x3D; Favorites, 11 &#x3D; Recent, 12 &#x3D; Templates, 13 &#x3D; Privacy, 14 &#x3D; VirtualRooms, 15 &#x3D; FillingFormsRoom, 16 &#x3D; EditingRoom, 19 &#x3D; CustomRoom, 20 &#x3D; Archive, 21 &#x3D; ThirdpartyBackup, 22 &#x3D; PublicRoom, 25 &#x3D; ReadyFormFolder, 26 &#x3D; InProcessFormFolder, 27 &#x3D; FormFillingFolderDone, 28 &#x3D; FormFillingFolderInProgress, 29 &#x3D; VirtualDataRoom, 30 &#x3D; RoomTemplates, 31 &#x3D; AiRoom, 32 &#x3D; Knowledge, 33 &#x3D; ChatOutputs, 34 &#x3D; AiAgents, 35 &#x3D; DefaultTemplates, 36 &#x3D; Forms, 37 &#x3D; Ai. | [optional] 
**parent_room_type** | **int** | The type of the room the entry is inside, at any depth; absent for an entry outside rooms. Values of &#x60;FolderType&#x60;: 0 &#x3D; DEFAULT, 1 &#x3D; COMMON, 2 &#x3D; BUNCH, 3 &#x3D; TRASH, 5 &#x3D; USER, 6 &#x3D; SHARE, 8 &#x3D; Projects, 10 &#x3D; Favorites, 11 &#x3D; Recent, 12 &#x3D; Templates, 13 &#x3D; Privacy, 14 &#x3D; VirtualRooms, 15 &#x3D; FillingFormsRoom, 16 &#x3D; EditingRoom, 19 &#x3D; CustomRoom, 20 &#x3D; Archive, 21 &#x3D; ThirdpartyBackup, 22 &#x3D; PublicRoom, 25 &#x3D; ReadyFormFolder, 26 &#x3D; InProcessFormFolder, 27 &#x3D; FormFillingFolderDone, 28 &#x3D; FormFillingFolderInProgress, 29 &#x3D; VirtualDataRoom, 30 &#x3D; RoomTemplates, 31 &#x3D; AiRoom, 32 &#x3D; Knowledge, 33 &#x3D; ChatOutputs, 34 &#x3D; AiAgents, 35 &#x3D; DefaultTemplates, 36 &#x3D; Forms, 37 &#x3D; Ai. | [optional] 
**origin_id** | [**EntryId**](EntryId.md) |  | [optional] 
**origin_room_id** | [**EntryId**](EntryId.md) |  | [optional] 
**origin_title** | **str** | For an entry in the trash, the name of the folder it was deleted from. | [optional] 
**origin_room_title** | **str** | For an entry in the trash, the name of the room it was deleted from. | [optional] 
**provider_item** | **bool** | True when the entry lives in a connected third-party storage; absent for the portal&#39;s own storage. | [optional] 
**provider_key** | **str** | The connected third-party storage the entry lives in; absent for the portal&#39;s own storage. | [optional] 
**provider_id** | **int** | The ID of the third-party storage connection the entry comes through; absent for the portal&#39;s own storage. | [optional] 
**order** | **int** | The position of the entry in a room with indexing turned on; meaningful only inside such a room. | [optional] 
**files_count** | **int** | The number of files the folder directly contains. | [optional] 
**folders_count** | **int** | The number of subfolders the folder directly contains. | [optional] 
**type** | **int** | The kind of folder: an ordinary one, one the portal creates and maintains itself, such as the folders of a form-filling room, or, for a room a folder.* webhook is about, the kind of room. Values of &#x60;FolderType&#x60;: 0 &#x3D; DEFAULT, 1 &#x3D; COMMON, 2 &#x3D; BUNCH, 3 &#x3D; TRASH, 5 &#x3D; USER, 6 &#x3D; SHARE, 8 &#x3D; Projects, 10 &#x3D; Favorites, 11 &#x3D; Recent, 12 &#x3D; Templates, 13 &#x3D; Privacy, 14 &#x3D; VirtualRooms, 15 &#x3D; FillingFormsRoom, 16 &#x3D; EditingRoom, 19 &#x3D; CustomRoom, 20 &#x3D; Archive, 21 &#x3D; ThirdpartyBackup, 22 &#x3D; PublicRoom, 25 &#x3D; ReadyFormFolder, 26 &#x3D; InProcessFormFolder, 27 &#x3D; FormFillingFolderDone, 28 &#x3D; FormFillingFolderInProgress, 29 &#x3D; VirtualDataRoom, 30 &#x3D; RoomTemplates, 31 &#x3D; AiRoom, 32 &#x3D; Knowledge, 33 &#x3D; ChatOutputs, 34 &#x3D; AiAgents, 35 &#x3D; DefaultTemplates, 36 &#x3D; Forms, 37 &#x3D; Ai. | [optional] 

## Example

```python
from docspace_webhooks_sdk.models.folder_payload import FolderPayload

# TODO update the JSON string below
json = "{}"
# create an instance of FolderPayload from a JSON string
folder_payload_instance = FolderPayload.from_json(json)
# print the JSON string representation of the object
print(FolderPayload.to_json())

# convert the object into a dict
folder_payload_dict = folder_payload_instance.to_dict()
# create an instance of FolderPayload from a dict
folder_payload_from_dict = FolderPayload.from_dict(folder_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


