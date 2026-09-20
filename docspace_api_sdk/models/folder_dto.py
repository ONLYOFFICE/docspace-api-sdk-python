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
from docspace_api_sdk.models.chat_settings_dto import ChatSettingsDto
from docspace_api_sdk.models.employee_dto import EmployeeDto
from docspace_api_sdk.models.file_entry_type import FileEntryType
from docspace_api_sdk.models.file_share import FileShare
from docspace_api_sdk.models.folder_type import FolderType
from docspace_api_sdk.models.logo import Logo
from docspace_api_sdk.models.room_data_lifetime_dto import RoomDataLifetimeDto
from docspace_api_sdk.models.room_type import RoomType
from docspace_api_sdk.models.watermark_dto import WatermarkDto
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field
from docspace_api_sdk.models.file_entry_dto import FileEntryDto

class FolderDto(FileEntryDto):
    """
    The folder, with the fields that only a room carries filled in when the folder is a room.
    """

    parent_id: Optional[StrictInt] = Field(default=None, description="The folder this one is listed in. For a room it is the root of the section the room lives in, and for an entry  opened through a sharing link whose real parent the caller may not read it is the root of the section with the  entries shared with them.", alias="parentId", json_schema_extra={"examples": [10]})
    files_count: Optional[StrictInt] = Field(default=None, description="How many files lie directly in the folder, without counting the subfolders. The roots of the `Rooms`, room  templates and default templates sections always report 0, because the number is not collected for them.", alias="filesCount", json_schema_extra={"examples": [5]})
    folders_count: Optional[StrictInt] = Field(default=None, description="How many subfolders lie directly in the folder. For an AI room the two service subfolders it always holds are  subtracted, so the number matches what a listing of it shows, and the roots of the `Rooms` and templates  sections report 0.", alias="foldersCount", json_schema_extra={"examples": [7]})
    is_shareable: Optional[StrictBool] = Field(default=None, description="Whether the caller may hand out access to the folder. It is filled in only for the folder a folder-contents  answer is about, and is null in every other answer, so null says nothing about the sharing rights.", alias="isShareable", json_schema_extra={"examples": [True]})
    new: Optional[StrictInt] = Field(default=None, description="How many entries inside the folder the caller has not opened yet, the number drawn as the badge on it. An  account that turned the badges off in its own settings always reads 0 here, so 0 alone does not prove that  everything has been seen.", json_schema_extra={"examples": [3]})
    mute: Optional[StrictBool] = Field(default=None, description="Whether the caller silenced the notifications of this room: true means no message about its activity reaches  them. The choice belongs to the reading account rather than to the room, so two members of one room read  different values.", json_schema_extra={"examples": [False]})
    tags: Optional[List[StrictStr]] = Field(default=None, description="The names of the tags attached to the room. Empty for a folder that is not a room, since only rooms carry  tags, and the names are the ones from the portal tag catalogue.", json_schema_extra={"examples": [["Marketing", "Q3"]]})
    logo: Optional[Logo] = Field(default=None, description="The addresses of the room logo in four sizes, together with the colour and the built-in cover that are drawn  when no logo was uploaded. A room without a logo answers with four empty addresses rather than with null, and  the field is null for a folder that is not a room.")
    pinned: Optional[StrictBool] = Field(default=None, description="Whether the caller pinned the room to the top of their own room list. Pinning is personal and is lost when the  room is archived.", json_schema_extra={"examples": [False]})
    room_type: Optional[RoomType] = Field(default=None, description="The kind of the room, which decides the default access rules of its members. Null for a folder that is not a  room.", alias="roomType")
    private: Optional[StrictBool] = Field(default=None, description="Whether the room is a private one, which limits it to the accounts invited into it and needs encryption keys  set up for each of them.", json_schema_extra={"examples": [False]})
    indexing: Optional[StrictBool] = Field(default=None, description="Whether the contents of the room are kept in an explicit numbered order, the one reported as `order` on each  entry, instead of being left to the sorting the reader asks for.", json_schema_extra={"examples": [True]})
    deny_download: Optional[StrictBool] = Field(default=None, description="Whether downloading and printing the contents of the room is forbidden, which leaves its members with viewing  and editing in the editor.", alias="denyDownload", json_schema_extra={"examples": [False]})
    lifetime: Optional[RoomDataLifetimeDto] = Field(default=None, description="The rule by which the files of the room are removed once they grow old. Null when the room has no such rule,  which is also what is reported after the rule is switched off, because switching it off erases it.")
    watermark: Optional[WatermarkDto] = Field(default=None, description="The watermark stamped over the documents of the room while they are viewed and printed. Null when the room has  no watermark, and for every folder that is not a room.")
    type: Optional[FolderType] = Field(default=None, description="The part the folder plays inside its room: one of the service folders of the form-filling flow, or the  knowledge and result storages of an AI room. It stays null for an ordinary folder and for the room itself, so  it does not describe folders in general.")
    in_room: Optional[StrictBool] = Field(default=None, description="Whether the caller holds the room through an invitation of their own: true for the account that created it and  for a member invited personally, false when the access comes from a group they belong to, and null for a  folder that is not a room.", alias="inRoom", json_schema_extra={"examples": [False]})
    quota_limit: Optional[StrictInt] = Field(default=None, description="How much space the files of the room may take, in bytes. It is the limit set on this room, or the portal  default for rooms when none was set. Null when the tariff of the portal does not count room statistics, when  room quotas are switched off, when the room lies in the archive or the trash, or when the caller may only read  it.", alias="quotaLimit", json_schema_extra={"examples": [1073741824]})
    is_custom_quota: Optional[StrictBool] = Field(default=None, description="Whether `quotaLimit` is a limit set on this room (true) or the portal default for rooms (false). Null exactly  when `quotaLimit` is null.", alias="isCustomQuota", json_schema_extra={"examples": [False]})
    used_space: Optional[StrictInt] = Field(default=None, description="How much the files of the room take, in bytes, as of the last time the counter was recomputed. The counter is  refreshed when a file operation finishes, so a read right after an upload or a deletion can still report the  previous figure. Null for a folder that is not a room.", alias="usedSpace", json_schema_extra={"examples": [524288000]})
    password_protected: Optional[StrictBool] = Field(default=None, description="Whether the sharing link the folder was opened through asks for a password that has not been entered yet.  While it is true the contents stay unreadable; send the password to `POST api/2.0/files/share/{key}/password`  first. Null when the folder was not reached through a link.", alias="passwordProtected", json_schema_extra={"examples": [False]})
    expired: Optional[StrictBool] = Field(default=None, description="Deprecated, read `isLinkExpired` instead: whether the sharing link the folder was opened through has run out  of its lifetime.", json_schema_extra={"examples": [False]})
    chat_settings: Optional[ChatSettingsDto] = Field(default=None, description="The chat configuration of an AI room. Only the system prompt is reported here, whatever else the room stores,  and the field is null for every folder that is not an AI room.", alias="chatSettings")
    root_room_type: Optional[RoomType] = Field(default=None, description="The kind of the room the folder lies in. It is filled in only for the folder a folder-contents answer is  about, and only when that room is an AI room, so it is null in every other answer and for every other room  kind.", alias="rootRoomType")
    save_form_as_xlsx: Optional[StrictBool] = Field(default=None, description="Whether the answers collected in this form-filling room are also gathered into a spreadsheet next to the  completed copies. Filled in for form-filling rooms only.", alias="saveFormAsXLSX", json_schema_extra={"examples": [False]})
    send_form_to_external_db: Optional[StrictBool] = Field(default=None, description="Whether the answers collected in this form-filling room are also pushed into the external database configured  for the portal. Filled in for form-filling rooms only.", alias="sendFormToExternalDB", json_schema_extra={"examples": [False]})
    original_form_id: Optional[StrictInt] = Field(default=None, description="The form the completed copies in this folder were filled from, taken from the copy submitted last. Null while  the folder holds no completed copy, and for every folder that does not collect them.", alias="originalFormId", json_schema_extra={"examples": [42]})

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
        """Create an instance of FolderDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of logo
        if self.logo:
            _dict['logo'] = self.logo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lifetime
        if self.lifetime:
            _dict['lifetime'] = self.lifetime.to_dict()
        # override the default output from pydantic by calling `to_dict()` of watermark
        if self.watermark:
            _dict['watermark'] = self.watermark.to_dict()
        # override the default output from pydantic by calling `to_dict()` of chat_settings
        if self.chat_settings:
            _dict['chatSettings'] = self.chat_settings.to_dict()
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

        # set to None if is_shareable (nullable) is None
        # and model_fields_set contains the field
        if self.is_shareable is None and "is_shareable" in self.model_fields_set:
            _dict['isShareable'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if in_room (nullable) is None
        # and model_fields_set contains the field
        if self.in_room is None and "in_room" in self.model_fields_set:
            _dict['inRoom'] = None

        # set to None if quota_limit (nullable) is None
        # and model_fields_set contains the field
        if self.quota_limit is None and "quota_limit" in self.model_fields_set:
            _dict['quotaLimit'] = None

        # set to None if is_custom_quota (nullable) is None
        # and model_fields_set contains the field
        if self.is_custom_quota is None and "is_custom_quota" in self.model_fields_set:
            _dict['isCustomQuota'] = None

        # set to None if used_space (nullable) is None
        # and model_fields_set contains the field
        if self.used_space is None and "used_space" in self.model_fields_set:
            _dict['usedSpace'] = None

        # set to None if password_protected (nullable) is None
        # and model_fields_set contains the field
        if self.password_protected is None and "password_protected" in self.model_fields_set:
            _dict['passwordProtected'] = None

        # set to None if expired (nullable) is None
        # and model_fields_set contains the field
        if self.expired is None and "expired" in self.model_fields_set:
            _dict['expired'] = None

        # set to None if save_form_as_xlsx (nullable) is None
        # and model_fields_set contains the field
        if self.save_form_as_xlsx is None and "save_form_as_xlsx" in self.model_fields_set:
            _dict['saveFormAsXLSX'] = None

        # set to None if send_form_to_external_db (nullable) is None
        # and model_fields_set contains the field
        if self.send_form_to_external_db is None and "send_form_to_external_db" in self.model_fields_set:
            _dict['sendFormToExternalDB'] = None

        # set to None if original_form_id (nullable) is None
        # and model_fields_set contains the field
        if self.original_form_id is None and "original_form_id" in self.model_fields_set:
            _dict['originalFormId'] = None

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
            "parentId": obj.get("parentId"),
            "filesCount": obj.get("filesCount"),
            "foldersCount": obj.get("foldersCount"),
            "isShareable": obj.get("isShareable"),
            "new": obj.get("new"),
            "mute": obj.get("mute"),
            "tags": obj.get("tags"),
            "logo": Logo.from_dict(obj["logo"]) if obj.get("logo") is not None else None,
            "pinned": obj.get("pinned"),
            "roomType": obj.get("roomType"),
            "private": obj.get("private"),
            "indexing": obj.get("indexing"),
            "denyDownload": obj.get("denyDownload"),
            "lifetime": RoomDataLifetimeDto.from_dict(obj["lifetime"]) if obj.get("lifetime") is not None else None,
            "watermark": WatermarkDto.from_dict(obj["watermark"]) if obj.get("watermark") is not None else None,
            "type": obj.get("type"),
            "inRoom": obj.get("inRoom"),
            "quotaLimit": obj.get("quotaLimit"),
            "isCustomQuota": obj.get("isCustomQuota"),
            "usedSpace": obj.get("usedSpace"),
            "passwordProtected": obj.get("passwordProtected"),
            "expired": obj.get("expired"),
            "chatSettings": ChatSettingsDto.from_dict(obj["chatSettings"]) if obj.get("chatSettings") is not None else None,
            "rootRoomType": obj.get("rootRoomType"),
            "saveFormAsXLSX": obj.get("saveFormAsXLSX"),
            "sendFormToExternalDB": obj.get("sendFormToExternalDB"),
            "originalFormId": obj.get("originalFormId")
        }
        all_fields = {**base_dict, **extra_fields}
        return cls.model_validate(all_fields)


