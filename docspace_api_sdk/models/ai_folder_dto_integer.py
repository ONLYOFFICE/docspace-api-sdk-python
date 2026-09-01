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
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.ai_chat_settings_dto import AiChatSettingsDto
from docspace_api_sdk.models.ai_employee_dto import AiEmployeeDto
from docspace_api_sdk.models.ai_file_entry_type import AiFileEntryType
from docspace_api_sdk.models.ai_file_share import AiFileShare
from docspace_api_sdk.models.ai_folder_type import AiFolderType
from docspace_api_sdk.models.ai_logo import AiLogo
from docspace_api_sdk.models.ai_room_data_lifetime_dto import AiRoomDataLifetimeDto
from docspace_api_sdk.models.ai_room_type import AiRoomType
from docspace_api_sdk.models.ai_watermark_dto import AiWatermarkDto
from docspace_api_sdk.models.file_entry_dto_integer_all_of_available_share_rights import FileEntryDtoIntegerAllOfAvailableShareRights
from docspace_api_sdk.models.file_entry_dto_integer_all_of_security import FileEntryDtoIntegerAllOfSecurity
from docspace_api_sdk.models.file_entry_dto_integer_all_of_share_settings import FileEntryDtoIntegerAllOfShareSettings
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field
from docspace_api_sdk.models.ai_file_entry_dto_integer import AiFileEntryDtoInteger

class AiFolderDtoInteger(AiFileEntryDtoInteger):
    """
    The folder parameters.
    """

    parent_id: Optional[StrictInt] = Field(default=None, description="The parent folder ID of the folder.", alias="parentId", json_schema_extra={"examples": [10]})
    files_count: Optional[StrictInt] = Field(default=None, description="The number of files that the folder contains.", alias="filesCount", json_schema_extra={"examples": [5]})
    folders_count: Optional[StrictInt] = Field(default=None, description="The number of folders that the folder contains.", alias="foldersCount", json_schema_extra={"examples": [7]})
    is_shareable: Optional[StrictBool] = Field(default=None, description="Specifies if the folder can be shared or not.", alias="isShareable", json_schema_extra={"examples": [True]})
    new: Optional[StrictInt] = Field(default=None, description="The new element index in the folder.", json_schema_extra={"examples": [0]})
    mute: Optional[StrictBool] = Field(default=None, description="Specifies if the folder notifications are enabled or not.", json_schema_extra={"examples": [False]})
    tags: Optional[List[StrictStr]] = Field(default=None, description="The list of tags of the folder.", json_schema_extra={"examples": [["tag1", "tag2"]]})
    logo: Optional[AiLogo] = Field(default=None, description="The folder logo.")
    pinned: Optional[StrictBool] = Field(default=None, description="Specifies if the folder is pinned or not.", json_schema_extra={"examples": [False]})
    room_type: Optional[AiRoomType] = Field(default=None, description="The room type of the folder.", alias="roomType")
    private: Optional[StrictBool] = Field(default=None, description="Specifies if the folder is private or not.", json_schema_extra={"examples": [False]})
    indexing: Optional[StrictBool] = Field(default=None, description="Specifies if the folder is indexed or not.", json_schema_extra={"examples": [True]})
    deny_download: Optional[StrictBool] = Field(default=None, description="Specifies if the folder can be downloaded or not.", alias="denyDownload", json_schema_extra={"examples": [False]})
    lifetime: Optional[AiRoomDataLifetimeDto] = Field(default=None, description="The room data lifetime settings of the folder.")
    watermark: Optional[AiWatermarkDto] = Field(default=None, description="The watermark settings of the folder.")
    type: Optional[AiFolderType] = Field(default=None, description="The folder type.")
    in_room: Optional[StrictBool] = Field(default=None, description="Specifies if the folder is placed in the room or not.", alias="inRoom", json_schema_extra={"examples": [False]})
    quota_limit: Optional[StrictInt] = Field(default=None, description="The folder quota limit.", alias="quotaLimit", json_schema_extra={"examples": [1073741824]})
    is_custom_quota: Optional[StrictBool] = Field(default=None, description="Specifies if the folder room has a custom quota or not.", alias="isCustomQuota", json_schema_extra={"examples": [False]})
    used_space: Optional[StrictInt] = Field(default=None, description="How much folder space is used (counter).", alias="usedSpace", json_schema_extra={"examples": [524288000]})
    password_protected: Optional[StrictBool] = Field(default=None, description="Specifies if the folder is password protected or not.", alias="passwordProtected", json_schema_extra={"examples": [False]})
    expired: Optional[StrictBool] = Field(default=None, description="Specifies if an external link to the folder is expired or not.", json_schema_extra={"examples": [False]})
    chat_settings: Optional[AiChatSettingsDto] = Field(default=None, description="The AI chat settings for the folder room. Contains configuration for AI provider, model selection, and custom prompts.  Only applicable to rooms with AI chat functionality enabled. Null if the room does not have chat settings configured.", alias="chatSettings")
    root_room_type: Optional[AiRoomType] = Field(default=None, description="The room type of the root folder. Indicates the type of the parent room if the current folder is nested within a room hierarchy.  This property helps identify the context in which a nested folder exists.", alias="rootRoomType")
    save_form_as_xlsx: Optional[StrictBool] = Field(default=None, description="Specifies whether to save form data as XLSX file.", alias="saveFormAsXLSX", json_schema_extra={"examples": [False]})
    send_form_to_external_db: Optional[StrictBool] = Field(default=None, description="Specifies whether to send form data to external database.", alias="sendFormToExternalDB", json_schema_extra={"examples": [False]})
    original_form_id: Optional[StrictInt] = Field(default=None, description="The original form ID that corresponds to this FormFillingFolderDone folder.", alias="originalFormId", json_schema_extra={"examples": [42]})

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
        """Create an instance of AiFolderDtoInteger from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['createdBy'] = self.created_by.to_dict()
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
            "logo": AiLogo.from_dict(obj["logo"]) if obj.get("logo") is not None else None,
            "pinned": obj.get("pinned"),
            "roomType": obj.get("roomType"),
            "private": obj.get("private"),
            "indexing": obj.get("indexing"),
            "denyDownload": obj.get("denyDownload"),
            "lifetime": AiRoomDataLifetimeDto.from_dict(obj["lifetime"]) if obj.get("lifetime") is not None else None,
            "watermark": AiWatermarkDto.from_dict(obj["watermark"]) if obj.get("watermark") is not None else None,
            "type": obj.get("type"),
            "inRoom": obj.get("inRoom"),
            "quotaLimit": obj.get("quotaLimit"),
            "isCustomQuota": obj.get("isCustomQuota"),
            "usedSpace": obj.get("usedSpace"),
            "passwordProtected": obj.get("passwordProtected"),
            "expired": obj.get("expired"),
            "chatSettings": AiChatSettingsDto.from_dict(obj["chatSettings"]) if obj.get("chatSettings") is not None else None,
            "rootRoomType": obj.get("rootRoomType"),
            "saveFormAsXLSX": obj.get("saveFormAsXLSX"),
            "sendFormToExternalDB": obj.get("sendFormToExternalDB"),
            "originalFormId": obj.get("originalFormId")
        }
        all_fields = {**base_dict, **extra_fields}
        return cls.model_validate(all_fields)


