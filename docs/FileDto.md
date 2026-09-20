# FileDto
A stored file as the calling account sees it: where it lives, which revision this is, how it can be opened and  what the portal is currently doing with it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The name shown for the entry. For a file it carries the extension, which is how the format is recognised, and  for a room it is the room name. | [optional] 
**access** | [**FileShare**](FileShare.md) | The level the calling account holds on this entry, resolved from its own rights, the groups it belongs to and  any link it came in through. It is the level itself, not what the account may do with it - the action flags  below answer that. | [optional] 
**shared_by** | [**EmployeeDto**](EmployeeDto.md) | Who gave the calling account the access it is using. It is filled in only while the entry is being read  through a share, and never for a caller without an account. | [optional] 
**owned_by** | [**EmployeeDto**](EmployeeDto.md) | Who owns the place the entry is shared from - the creator of the room it lies in, or of the personal section  that holds it. It is filled in only while the entry is being read through a share, and never for a caller  without an account. | [optional] 
**shared** | **bool** | Whether at least one external link exists for the entry, whichever kind. It says nothing about accounts and  groups - those are counted by the flag for members below. | [optional] 
**shared_for_user** | **bool** | Whether at least one account or group has been given rights on the entry directly, as opposed to reaching it  through a link or through the room around it. | [optional] 
**shared_external** | **bool** | Whether one of the entry's links is open to people outside the portal, as opposed to a link that only its own  members can follow. This is the flag to watch when the concern is who can reach the content from outside. | [optional] 
**parent_shared** | **bool** | Whether the entry is reachable because the room or folder around it is shared, rather than through rights of  its own. A copy or a move takes the entry out of that scope. | [optional] 
**short_web_url** | **str** | A shortened address that opens the entry through the link it is being read with. It is an empty string  whenever no link applies, which is the usual case for a member browsing their own rooms. | [optional] 
**created** | [**ApiDateTime**](ApiDateTime.md) | When the entry was created, written with the offset of the portal's time zone. For a file restored from an  older version this is still the moment the file first appeared. | [optional] 
**created_by** | [**EmployeeDto**](EmployeeDto.md) | Who created the entry. It is null for a caller without an account, who is told nothing about the portal's  members. | [optional] 
**updated** | [**ApiDateTime**](ApiDateTime.md) | When the entry last changed, written with the offset of the portal's time zone. It is never reported as  earlier than the creation moment, so the two can be compared safely. | [optional] 
**auto_delete** | [**ApiDateTime**](ApiDateTime.md) | When the entry will disappear on its own, written with the offset of the portal's time zone. It is filled in  only where a removal is actually scheduled - something in the trash while the portal cleans it up  automatically, or a guest's own documents - so a null means nothing is scheduled rather than that the entry is  permanent. | [optional] 
**root_folder_type** | [**FolderType**](FolderType.md) | The section the entry ultimately belongs to, which is what tells a personal document from one inside a room,  from a template and from something in the trash or the archive. | [optional] 
**parent_room_type** | [**FolderType**](FolderType.md) | The kind of room the entry lies in, which decides what the room allows - filling forms, public links,  indexing. It is null for an entry that is not inside a room at all. | [optional] 
**updated_by** | [**EmployeeDto**](EmployeeDto.md) | Who changed the entry last. It is null for a caller without an account. | [optional] 
**provider_item** | **bool** | Set when the entry is stored on a connected third-party account rather than on the portal, and null when it is  stored on the portal. Such an entry is identified by a string rather than a number, and some operations skip  it. | [optional] 
**provider_key** | **str** | Which third-party service holds the entry, matching the keys accepted by the third-party operations. It is  null for an entry stored on the portal. | [optional] 
**provider_id** | **int** | The connected account the entry comes from, for telling apart two connections to the same service. It is null  for an entry stored on the portal. | [optional] 
**order** | **str** | The place of the entry in a room where the members arrange the content themselves, given as the position of  the entry preceded by the positions of the folders leading to it, separated by dots. It is empty when nothing  has been arranged. | [optional] 
**is_favorite** | **bool** | Set when the calling account has marked the entry as a favorite, which is what puts it into the favorites  listing. For a file that is not marked it is null rather than false. | [optional] 
**file_entry_type** | [**FileEntryType**](FileEntryType.md) | Tells a folder from a file, and so which of the two shapes the rest of the object has. A room is reported as a  folder here. | [optional] 
**id** | **int** | The identifier to pass back to the other operations of this entry. It is a number for storage on the portal  and a string for a connected third-party account, and it is unique only within its own kind, so files and  folders may carry the same value. | [optional] 
**root_folder_id** | **int** | The section the entry ultimately lies in, as an identifier that can be listed like any other folder. For an  entry inside a room this is the rooms section, not the room. | [optional] 
**origin_id** | **int** | The folder the entry was deleted from, which is where restoring it puts it back. It is left out of the answer  unless the entry is in the trash. | [optional] 
**origin_room_id** | **int** | The room the entry was deleted from, left out of the answer for anything that was not deleted out of a room. | [optional] 
**origin_title** | **str** | The name of the folder the entry was deleted from, for showing where it would be restored to. It is null for  an entry that is not in the trash. | [optional] 
**origin_room_title** | **str** | The name of the room the entry was deleted from, null for anything that was not deleted out of a room. | [optional] 
**can_share** | **bool** | Whether the calling account may change who has access to the entry, and so whether offering a sharing dialog  for it makes sense. It is false in rooms whose access is fixed by the room itself, such as a private one, even  for its manager. | [optional] 
**share_settings** | [**AiFileEntryDtoAllOfShareSettings**](AiFileEntryDtoAllOfShareSettings.md) |  | [optional] 
**security** | [**AiFileEntryDtoAllOfSecurity**](AiFileEntryDtoAllOfSecurity.md) |  | [optional] 
**available_share_rights** | [**AiFileEntryDtoAllOfAvailableShareRights**](AiFileEntryDtoAllOfAvailableShareRights.md) |  | [optional] 
**request_token** | **str** | The token of the link the entry is being read through, which is the value the external-share operations expect  and which also has to be carried by the download and preview addresses. It is null whenever the entry is not  being read through a link. | [optional] 
**external** | **bool** | Set when the link being used was made for this very entry, and false when the entry is reached through a link  to the room around it. It is null when no link is involved. | [optional] 
**expiration_date** | [**ApiDateTime**](ApiDateTime.md) | When the link being used stops working, written with the offset of the portal's time zone. It is null for a  link that never expires and whenever no link is involved. | [optional] 
**is_link_expired** | **bool** | Set when the link being used has already passed its expiration date, which is why the entry cannot be opened  even though it is described here. It is null when no link is involved. | [optional] 
**folder_id** | **int** | The folder the file is stored in. When the file was reached through a share and the caller cannot open its  real parent, the identifier of the Shared with me section is reported instead, so this is where the file is  visible rather than where it physically sits. | [optional] 
**version** | **int** | The revision this entry describes. It starts at 1 and moves to the next number each time new content is stored  over the file, except for an editing session opened against the file itself, which replaces the content and  keeps the number. `GET api/2.0/files/file/{fileId}/history` lists them all. | [optional] 
**version_group** | **int** | Groups revisions that belong together, which is how a history can fold a long editing session into one entry:  versions saved inside one session share this number, and an upload over the file starts a new group. | [optional] 
**content_length** | **str** | The size already formatted for display, with a unit and the separators of the caller's language. Read  `pureContentLength` for a number to calculate with. | [optional] 
**pure_content_length** | **int** | The size of the stored content in bytes, and null for an empty file. | [optional] 
**file_status** | [**FileStatus**](FileStatus.md) | What the portal is currently doing with the file and how the caller stands towards it - open in the editor,  unread, being converted, and so on. The value is a bit mask that combines those states, so a file can report a  number that matches none of the published members on its own. | [optional] 
**editing_by** | **Dict[str, Optional[str]]** | The accounts that have the file open in the editor at this moment, as account identifier to display name, and  empty when nobody has. The all-zero identifier stands for people who came in through an external link without  signing in, and its name carries their number in brackets when there is more than one. | [optional] 
**mute** | **bool** | Not a property of the file at all: it repeats, inverted, the calling account's own switch for new-item badges,  so it is the same in every entry of one answer. True means that account has badges turned off. | [optional] 
**view_url** | **str** | The address that returns the bytes of the file - a download, in spite of the name; `webUrl` is the address a  person opens. When the file was reached through an external link the address carries the key of that link, so  it keeps working without signing in. | [optional] 
**web_url** | **str** | The page that opens the file in a browser: the editor for a format the portal edits, the media viewer for  pictures, audio and video, and the download address for a format it cannot show at all. | [optional] 
**file_type** | [**FileType**](FileType.md) | The broad kind of content, worked out from the extension, which is what a client uses to pick an icon or a  viewer without parsing `fileExst` itself. | [optional] 
**file_exst** | **str** | The extension of the stored file, leading dot included and always lower case. For a format the portal keeps in  a converted shape this is the extension it is served under, not the one it was uploaded with. | [optional] 
**comment** | **str** | The note kept with this revision. The portal writes it itself for revisions it creates, an upload over an  existing file among them, and an editor stores the note a person typed when saving a version. | [optional] 
**encrypted** | **bool** | True for a file in a private room, whose content the server never sees and which therefore cannot be converted  or taken over by an upload. Null, rather than false, for an ordinary file. | [optional] 
**thumbnail_url** | **str** | The address of the generated preview image. It is filled in only while `thumbnailStatus` says the preview has  been created, and it carries a suffix that changes with the file, so an image cached for an earlier revision  is not reused. | [optional] 
**thumbnail_status** | [**Thumbnail**](Thumbnail.md) | How far the preview image has got. Only the created state means `thumbnailUrl` holds an address; the others  mean there is none, either because it is still being produced or because this format has no preview. | [optional] 
**locked** | **bool** | True while the file is held under a lock that stops anyone but its holder from editing it, and null rather  than false when there is no lock. `lockedBy` names the holder unless the caller is the holder. | [optional] 
**locked_by** | **str** | The display name of the account holding the lock, and null when the caller holds it - so `locked` true  together with no name here means the lock is the caller's own. | [optional] 
**has_draft** | **bool** | For a fillable PDF form, whether the caller already has a filling draft of it, in which case `draftLocation`  says where that draft lives. Null for anything that is not a form. | [optional] 
**form_filling_status** | [**FormFillingStatus**](FormFillingStatus.md) | How far the filling of this form has got for the calling account, and whose turn it is now. It is worked out  only inside a virtual data room, where filling runs in steps; everywhere else it stays at the none value. | [optional] 
**is_form** | **bool** | Whether the PDF is a fillable form rather than a plain document. When the stored classification does not say,  the portal opens the file to find out, so the answer is reliable for a PDF and null for anything else. | [optional] 
**custom_filter_enabled** | **bool** | True while a spreadsheet is in the mode where each person sorts and filters their own view without changing  what the others see, and null rather than false when it is not. | [optional] 
**custom_filter_enabled_by** | **str** | The display name of the account that turned that mode on, and null when the caller turned it on themselves. | [optional] 
**start_filling** | **bool** | For a form in a room for filling, whether it has been released for filling; until then it is still being  prepared and only the people running the room work with it. Null for a file this does not apply to. | [optional] 
**is_filling_preparing** | **bool** | True during the short window in which a released form is still being written out by the editor. Neither  filling nor editing is accepted while it lasts, so a client should wait and read the file again. | [optional] 
**in_process_folder_id** | **int** | Left empty by the portal: the folder holding the caller's draft is reported in `draftLocation` instead. | [optional] 
**in_process_folder_title** | **str** | Left empty by the portal, like the identifier beside it; the draft's folder is named in `draftLocation`. | [optional] 
**results_folder_id** | **int** | The folder that collects the completed copies of this form. It is filled in only for the original form of a  room for filling, and only for a caller allowed to work with that form; null everywhere else. | [optional] 
**draft_location** | [**DraftLocation**](DraftLocation.md) | Where the caller's own filling draft of this form is kept. Null when there is no draft yet, which is the same  thing `hasDraft` reports. | [optional] 
**view_accessibility** | [**FileDtoAllOfViewAccessibility**](FileDtoAllOfViewAccessibility.md) |  | [optional] 
**last_opened** | [**ApiDateTime**](ApiDateTime.md) | The moment the caller last opened the file. It is kept per account and is what orders the Recent section, so  it is null for a file this account has never opened. Written with the offset of the portal's time zone. | [optional] 
**expired** | [**ApiDateTime**](ApiDateTime.md) | The moment the file falls under the lifetime rule of the room holding it and is removed. It is counted from  the first revision rather than the latest one, so editing a file does not postpone it, and it is null when the  room sets no lifetime. Written with the offset of the portal's time zone. | [optional] 
**vectorization_status** | [**VectorizationStatus**](VectorizationStatus.md) | How far the indexing of the file's content for AI search has got. It is null for a file that has never been  queued for indexing, which is every file while the feature is off for the portal. | [optional] 
**external_db_table_name** | **str** | The table collecting the submitted values of this form in the external database configured for its room. The  field is left out of the answer entirely when the form has no such table. | [optional] 
**dimensions** | [**Size**](Size.md) | The pixel size of the picture, measured by reading the stored file rather than taken from any stored metadata.  Null for anything that is not a picture the portal can show, and also when the file could not be read. | [optional] 

## Example

```python
from docspace_api_sdk.models.file_dto import FileDto

# TODO update the JSON string below
json = "{}"
# create an instance of FileDto from a JSON string
file_dto_instance = FileDto.from_json(json)
# print the JSON string representation of the object
print(FileDto.to_json())

# convert the object into a dict
file_dto_dict = file_dto_instance.to_dict()
# create an instance of FileDto from a dict
file_dto_from_dict = FileDto.from_dict(file_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


