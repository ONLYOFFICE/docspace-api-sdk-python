#
# (c) Copyright Ascensio System SIA 2026
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#



from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.ai_file_entry_dto_all_of_available_share_rights import AiFileEntryDtoAllOfAvailableShareRights
from docspace_api_sdk.models.ai_file_entry_dto_all_of_security import AiFileEntryDtoAllOfSecurity
from docspace_api_sdk.models.ai_file_entry_dto_all_of_share_settings import AiFileEntryDtoAllOfShareSettings
from docspace_api_sdk.models.api_date_time import ApiDateTime
from docspace_api_sdk.models.employee_dto import EmployeeDto
from docspace_api_sdk.models.file_dto_all_of_view_accessibility import FileDtoAllOfViewAccessibility
from docspace_api_sdk.models.file_entry_type import FileEntryType
from docspace_api_sdk.models.file_share import FileShare
from docspace_api_sdk.models.file_status import FileStatus
from docspace_api_sdk.models.file_type import FileType
from docspace_api_sdk.models.folder_type import FolderType
from docspace_api_sdk.models.form_filling_status import FormFillingStatus
from docspace_api_sdk.models.size import Size
from docspace_api_sdk.models.third_party_draft_location import ThirdPartyDraftLocation
from docspace_api_sdk.models.thumbnail import Thumbnail
from docspace_api_sdk.models.vectorization_status import VectorizationStatus
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field
from docspace_api_sdk.models.third_party_file_entry_dto import ThirdPartyFileEntryDto

class ThirdPartyFileDto(ThirdPartyFileEntryDto):
    """
    A stored file as the calling account sees it: where it lives, which revision this is, how it can be opened and  what the portal is currently doing with it.
    """

    folder_id: Optional[StrictStr] = Field(default=None, description="The folder the file is stored in. When the file was reached through a share and the caller cannot open its  real parent, the identifier of the Shared with me section is reported instead, so this is where the file is  visible rather than where it physically sits.", alias="folderId", json_schema_extra={"examples": ["sbox-42"]})
    version: Optional[StrictInt] = Field(default=None, description="The revision this entry describes. It starts at 1 and moves to the next number each time new content is stored  over the file, except for an editing session opened against the file itself, which replaces the content and  keeps the number. `GET api/2.0/files/file/{fileId}/history` lists them all.", json_schema_extra={"examples": [3]})
    version_group: Optional[StrictInt] = Field(default=None, description="Groups revisions that belong together, which is how a history can fold a long editing session into one entry:  versions saved inside one session share this number, and an upload over the file starts a new group.", alias="versionGroup", json_schema_extra={"examples": [1]})
    content_length: Optional[StrictStr] = Field(default=None, description="The size already formatted for display, with a unit and the separators of the caller's language. Read  `pureContentLength` for a number to calculate with.", alias="contentLength", json_schema_extra={"examples": ["1.29 MB"]})
    pure_content_length: Optional[StrictInt] = Field(default=None, description="The size of the stored content in bytes, and null for an empty file.", alias="pureContentLength", json_schema_extra={"examples": [1352001]})
    file_status: Optional[FileStatus] = Field(default=None, description="What the portal is currently doing with the file and how the caller stands towards it - open in the editor,  unread, being converted, and so on. The value is a bit mask that combines those states, so a file can report a  number that matches none of the published members on its own.", alias="fileStatus")
    editing_by: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="The accounts that have the file open in the editor at this moment, as account identifier to display name, and  empty when nobody has. The all-zero identifier stands for people who came in through an external link without  signing in, and its name carries their number in brackets when there is more than one.", alias="editingBy", json_schema_extra={"examples": [{"9a1e28c4-51f2-4f6b-b0a3-0c21e7f2a7d1": "John Doe"}]})
    mute: Optional[StrictBool] = Field(default=None, description="Not a property of the file at all: it repeats, inverted, the calling account's own switch for new-item badges,  so it is the same in every entry of one answer. True means that account has badges turned off.", json_schema_extra={"examples": [False]})
    view_url: Optional[StrictStr] = Field(default=None, description="The address that returns the bytes of the file - a download, in spite of the name; `webUrl` is the address a  person opens. When the file was reached through an external link the address carries the key of that link, so  it keeps working without signing in.", alias="viewUrl", json_schema_extra={"examples": ["https://example.com/filehandler.ashx?action=download&fileid=2221"]})
    web_url: Optional[StrictStr] = Field(default=None, description="The page that opens the file in a browser: the editor for a format the portal edits, the media viewer for  pictures, audio and video, and the download address for a format it cannot show at all.", alias="webUrl", json_schema_extra={"examples": ["https://example.com/doceditor?fileid=2221"]})
    file_type: Optional[FileType] = Field(default=None, description="The broad kind of content, worked out from the extension, which is what a client uses to pick an icon or a  viewer without parsing `fileExst` itself.", alias="fileType")
    file_exst: Optional[StrictStr] = Field(default=None, description="The extension of the stored file, leading dot included and always lower case. For a format the portal keeps in  a converted shape this is the extension it is served under, not the one it was uploaded with.", alias="fileExst", json_schema_extra={"examples": [".docx"]})
    comment: Optional[StrictStr] = Field(default=None, description="The note kept with this revision. The portal writes it itself for revisions it creates, an upload over an  existing file among them, and an editor stores the note a person typed when saving a version.", json_schema_extra={"examples": ["Uploaded file"]})
    encrypted: Optional[StrictBool] = Field(default=None, description="True for a file in a private room, whose content the server never sees and which therefore cannot be converted  or taken over by an upload. Null, rather than false, for an ordinary file.", json_schema_extra={"examples": [False]})
    thumbnail_url: Optional[StrictStr] = Field(default=None, description="The address of the generated preview image. It is filled in only while `thumbnailStatus` says the preview has  been created, and it carries a suffix that changes with the file, so an image cached for an earlier revision  is not reused.", alias="thumbnailUrl", json_schema_extra={"examples": ["https://example.com/filehandler.ashx?action=thumb&fileid=2221"]})
    thumbnail_status: Optional[Thumbnail] = Field(default=None, description="How far the preview image has got. Only the created state means `thumbnailUrl` holds an address; the others  mean there is none, either because it is still being produced or because this format has no preview.", alias="thumbnailStatus")
    locked: Optional[StrictBool] = Field(default=None, description="True while the file is held under a lock that stops anyone but its holder from editing it, and null rather  than false when there is no lock. `lockedBy` names the holder unless the caller is the holder.", json_schema_extra={"examples": [False]})
    locked_by: Optional[StrictStr] = Field(default=None, description="The display name of the account holding the lock, and null when the caller holds it - so `locked` true  together with no name here means the lock is the caller's own.", alias="lockedBy", json_schema_extra={"examples": ["John Doe"]})
    has_draft: Optional[StrictBool] = Field(default=None, description="For a fillable PDF form, whether the caller already has a filling draft of it, in which case `draftLocation`  says where that draft lives. Null for anything that is not a form.", alias="hasDraft", json_schema_extra={"examples": [False]})
    form_filling_status: Optional[FormFillingStatus] = Field(default=None, description="How far the filling of this form has got for the calling account, and whose turn it is now. It is worked out  only inside a virtual data room, where filling runs in steps; everywhere else it stays at the none value.", alias="formFillingStatus")
    is_form: Optional[StrictBool] = Field(default=None, description="Whether the file is a PDF, and so offered as a fillable form. It is null for any other file type.", alias="isForm", json_schema_extra={"examples": [True]})
    custom_filter_enabled: Optional[StrictBool] = Field(default=None, description="True while a spreadsheet is in the mode where each person sorts and filters their own view without changing  what the others see, and null rather than false when it is not.", alias="customFilterEnabled", json_schema_extra={"examples": [False]})
    custom_filter_enabled_by: Optional[StrictStr] = Field(default=None, description="The display name of the account that turned that mode on, and null when the caller turned it on themselves.", alias="customFilterEnabledBy", json_schema_extra={"examples": ["John Doe"]})
    start_filling: Optional[StrictBool] = Field(default=None, description="For a form in a room for filling, whether it has been released for filling; until then it is still being  prepared and only the people running the room work with it. Null for a file this does not apply to.", alias="startFilling", json_schema_extra={"examples": [True]})
    is_filling_preparing: Optional[StrictBool] = Field(default=None, description="True during the short window in which a released form is still being written out by the editor. Neither  filling nor editing is accepted while it lasts, so a client should wait and read the file again.", alias="isFillingPreparing", json_schema_extra={"examples": [False]})
    in_process_folder_id: Optional[StrictInt] = Field(default=None, description="Left empty by the portal: the folder holding the caller's draft is reported in `draftLocation` instead.", alias="inProcessFolderId", json_schema_extra={"examples": [10]})
    in_process_folder_title: Optional[StrictStr] = Field(default=None, description="Left empty by the portal, like the identifier beside it; the draft's folder is named in `draftLocation`.", alias="inProcessFolderTitle", json_schema_extra={"examples": ["In Process"]})
    results_folder_id: Optional[StrictInt] = Field(default=None, description="The folder that collects the completed copies of this form. It is filled in only for the original form of a  room for filling, and only for a caller allowed to work with that form; null everywhere else.", alias="resultsFolderId", json_schema_extra={"examples": [55]})
    draft_location: Optional[ThirdPartyDraftLocation] = Field(default=None, description="Where the caller's own filling draft of this form is kept. Null when there is no draft yet, which is the same  thing `hasDraft` reports.", alias="draftLocation")
    view_accessibility: Optional[FileDtoAllOfViewAccessibility] = Field(default=None, alias="viewAccessibility")
    last_opened: Optional[ApiDateTime] = Field(default=None, description="The moment the caller last opened the file. It is kept per account and is what orders the Recent section, so  it is null for a file this account has never opened. Written with the offset of the portal's time zone.", alias="lastOpened")
    expired: Optional[ApiDateTime] = Field(default=None, description="The moment the file falls under the lifetime rule of the room holding it and is removed. It is counted from  the first revision rather than the latest one, so editing a file does not postpone it, and it is null when the  room sets no lifetime. Written with the offset of the portal's time zone.")
    vectorization_status: Optional[VectorizationStatus] = Field(default=None, description="How far the indexing of the file's content for AI search has got. It is null for a file that has never been  queued for indexing, which is every file while the feature is off for the portal.", alias="vectorizationStatus")
    external_db_table_name: Optional[StrictStr] = Field(default=None, description="The table collecting the submitted values of this form in the external database configured for its room. The  field is left out of the answer entirely when the form has no such table.", alias="externalDbTableName", json_schema_extra={"examples": ["form_123_v1"]})
    dimensions: Optional[Size] = Field(default=None, description="The pixel size of the picture, measured by reading the stored file rather than taken from any stored metadata.  Null for anything that is not a picture the portal can show, and also when the file could not be read.")

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ThirdPartyFileDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of shared_by
        if self.shared_by:
            _dict['sharedBy'] = self.shared_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owned_by
        if self.owned_by:
            _dict['ownedBy'] = self.owned_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created
        if self.created:
            _dict['created'] = self.created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['createdBy'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated
        if self.updated:
            _dict['updated'] = self.updated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of auto_delete
        if self.auto_delete:
            _dict['autoDelete'] = self.auto_delete.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated_by
        if self.updated_by:
            _dict['updatedBy'] = self.updated_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of share_settings
        if self.share_settings:
            _dict['shareSettings'] = self.share_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of security
        if self.security:
            _dict['security'] = self.security.to_dict()
        # override the default output from pydantic by calling `to_dict()` of available_share_rights
        if self.available_share_rights:
            _dict['availableShareRights'] = self.available_share_rights.to_dict()
        # override the default output from pydantic by calling `to_dict()` of expiration_date
        if self.expiration_date:
            _dict['expirationDate'] = self.expiration_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of draft_location
        if self.draft_location:
            _dict['draftLocation'] = self.draft_location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of view_accessibility
        if self.view_accessibility:
            _dict['viewAccessibility'] = self.view_accessibility.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_opened
        if self.last_opened:
            _dict['lastOpened'] = self.last_opened.to_dict()
        # override the default output from pydantic by calling `to_dict()` of expired
        if self.expired:
            _dict['expired'] = self.expired.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dimensions
        if self.dimensions:
            _dict['dimensions'] = self.dimensions.to_dict()
        # set to None if share_settings (nullable) is None
        # and model_fields_set contains the field
        if self.share_settings is None and "share_settings" in self.model_fields_set:
            _dict['shareSettings'] = None

        # set to None if security (nullable) is None
        # and model_fields_set contains the field
        if self.security is None and "security" in self.model_fields_set:
            _dict['security'] = None

        # set to None if available_share_rights (nullable) is None
        # and model_fields_set contains the field
        if self.available_share_rights is None and "available_share_rights" in self.model_fields_set:
            _dict['availableShareRights'] = None

        # set to None if folder_id (nullable) is None
        # and model_fields_set contains the field
        if self.folder_id is None and "folder_id" in self.model_fields_set:
            _dict['folderId'] = None

        # set to None if content_length (nullable) is None
        # and model_fields_set contains the field
        if self.content_length is None and "content_length" in self.model_fields_set:
            _dict['contentLength'] = None

        # set to None if pure_content_length (nullable) is None
        # and model_fields_set contains the field
        if self.pure_content_length is None and "pure_content_length" in self.model_fields_set:
            _dict['pureContentLength'] = None

        # set to None if view_url (nullable) is None
        # and model_fields_set contains the field
        if self.view_url is None and "view_url" in self.model_fields_set:
            _dict['viewUrl'] = None

        # set to None if web_url (nullable) is None
        # and model_fields_set contains the field
        if self.web_url is None and "web_url" in self.model_fields_set:
            _dict['webUrl'] = None

        # set to None if file_exst (nullable) is None
        # and model_fields_set contains the field
        if self.file_exst is None and "file_exst" in self.model_fields_set:
            _dict['fileExst'] = None

        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict['comment'] = None

        # set to None if encrypted (nullable) is None
        # and model_fields_set contains the field
        if self.encrypted is None and "encrypted" in self.model_fields_set:
            _dict['encrypted'] = None

        # set to None if thumbnail_url (nullable) is None
        # and model_fields_set contains the field
        if self.thumbnail_url is None and "thumbnail_url" in self.model_fields_set:
            _dict['thumbnailUrl'] = None

        # set to None if locked (nullable) is None
        # and model_fields_set contains the field
        if self.locked is None and "locked" in self.model_fields_set:
            _dict['locked'] = None

        # set to None if locked_by (nullable) is None
        # and model_fields_set contains the field
        if self.locked_by is None and "locked_by" in self.model_fields_set:
            _dict['lockedBy'] = None

        # set to None if has_draft (nullable) is None
        # and model_fields_set contains the field
        if self.has_draft is None and "has_draft" in self.model_fields_set:
            _dict['hasDraft'] = None

        # set to None if is_form (nullable) is None
        # and model_fields_set contains the field
        if self.is_form is None and "is_form" in self.model_fields_set:
            _dict['isForm'] = None

        # set to None if custom_filter_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.custom_filter_enabled is None and "custom_filter_enabled" in self.model_fields_set:
            _dict['customFilterEnabled'] = None

        # set to None if custom_filter_enabled_by (nullable) is None
        # and model_fields_set contains the field
        if self.custom_filter_enabled_by is None and "custom_filter_enabled_by" in self.model_fields_set:
            _dict['customFilterEnabledBy'] = None

        # set to None if start_filling (nullable) is None
        # and model_fields_set contains the field
        if self.start_filling is None and "start_filling" in self.model_fields_set:
            _dict['startFilling'] = None

        # set to None if is_filling_preparing (nullable) is None
        # and model_fields_set contains the field
        if self.is_filling_preparing is None and "is_filling_preparing" in self.model_fields_set:
            _dict['isFillingPreparing'] = None

        # set to None if in_process_folder_id (nullable) is None
        # and model_fields_set contains the field
        if self.in_process_folder_id is None and "in_process_folder_id" in self.model_fields_set:
            _dict['inProcessFolderId'] = None

        # set to None if in_process_folder_title (nullable) is None
        # and model_fields_set contains the field
        if self.in_process_folder_title is None and "in_process_folder_title" in self.model_fields_set:
            _dict['inProcessFolderTitle'] = None

        # set to None if results_folder_id (nullable) is None
        # and model_fields_set contains the field
        if self.results_folder_id is None and "results_folder_id" in self.model_fields_set:
            _dict['resultsFolderId'] = None

        # set to None if view_accessibility (nullable) is None
        # and model_fields_set contains the field
        if self.view_accessibility is None and "view_accessibility" in self.model_fields_set:
            _dict['viewAccessibility'] = None

        # set to None if external_db_table_name (nullable) is None
        # and model_fields_set contains the field
        if self.external_db_table_name is None and "external_db_table_name" in self.model_fields_set:
            _dict['externalDbTableName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance from a dict"""
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        base_obj = super().from_dict(obj)
        base_dict = base_obj.model_dump() if hasattr(base_obj, "model_dump") else dict(base_obj or {})

        extra_fields = {
            "folderId": obj.get("folderId"),
            "version": obj.get("version"),
            "versionGroup": obj.get("versionGroup"),
            "contentLength": obj.get("contentLength"),
            "pureContentLength": obj.get("pureContentLength"),
            "fileStatus": obj.get("fileStatus"),
            "editingBy": obj.get("editingBy"),
            "mute": obj.get("mute"),
            "viewUrl": obj.get("viewUrl"),
            "webUrl": obj.get("webUrl"),
            "fileType": obj.get("fileType"),
            "fileExst": obj.get("fileExst"),
            "comment": obj.get("comment"),
            "encrypted": obj.get("encrypted"),
            "thumbnailUrl": obj.get("thumbnailUrl"),
            "thumbnailStatus": obj.get("thumbnailStatus"),
            "locked": obj.get("locked"),
            "lockedBy": obj.get("lockedBy"),
            "hasDraft": obj.get("hasDraft"),
            "formFillingStatus": obj.get("formFillingStatus"),
            "isForm": obj.get("isForm"),
            "customFilterEnabled": obj.get("customFilterEnabled"),
            "customFilterEnabledBy": obj.get("customFilterEnabledBy"),
            "startFilling": obj.get("startFilling"),
            "isFillingPreparing": obj.get("isFillingPreparing"),
            "inProcessFolderId": obj.get("inProcessFolderId"),
            "inProcessFolderTitle": obj.get("inProcessFolderTitle"),
            "resultsFolderId": obj.get("resultsFolderId"),
            "draftLocation": ThirdPartyDraftLocation.from_dict(obj["draftLocation"]) if obj.get("draftLocation") is not None else None,
            "viewAccessibility": FileDtoAllOfViewAccessibility.from_dict(obj["viewAccessibility"]) if obj.get("viewAccessibility") is not None else None,
            "lastOpened": ApiDateTime.from_dict(obj["lastOpened"]) if obj.get("lastOpened") is not None else None,
            "expired": ApiDateTime.from_dict(obj["expired"]) if obj.get("expired") is not None else None,
            "vectorizationStatus": obj.get("vectorizationStatus"),
            "externalDbTableName": obj.get("externalDbTableName"),
            "dimensions": Size.from_dict(obj["dimensions"]) if obj.get("dimensions") is not None else None
        }
        all_fields = {**base_dict, **extra_fields}
        return cls.model_validate(all_fields)


