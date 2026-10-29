# FileEntryPayload

What every file, folder and room webhook payload has in common.  All dates are in UTC. A delivery goes only to a subscription owner who may see the entry, and it carries no per-user state: no access rights, share settings, favourite flag or thumbnail. Read those from the REST API by the entry ID when they are needed.

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

## Example

```python
from docspace_webhooks_sdk.models.file_entry_payload import FileEntryPayload

# TODO update the JSON string below
json = "{}"
# create an instance of FileEntryPayload from a JSON string
file_entry_payload_instance = FileEntryPayload.from_json(json)
# print the JSON string representation of the object
print(FileEntryPayload.to_json())

# convert the object into a dict
file_entry_payload_dict = file_entry_payload_instance.to_dict()
# create an instance of FileEntryPayload from a dict
file_entry_payload_from_dict = FileEntryPayload.from_dict(file_entry_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


